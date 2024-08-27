from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.common import TimeoutException

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("MR_COMM_TEMPLATE")



@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def add_text_to_editor(login, text):
    # Locate the rich text editor and ensure it is focused
    editor = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']//p"))
    )
    login.execute_script("arguments[0].scrollIntoView(true);", editor)  # Scroll into view
    editor.clear()
    editor.click()  # Focus on the editor
    editor.send_keys(text)  # Use send_keys to add text
    print(editor.text)

@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_MR_Template(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//img[contains(@src, 'settings.gif')]//following::div[contains(text(),'Settings')]")
        time.sleep(3)
        commun = wait_and_locate_click(login, By.XPATH, "//div[normalize-space()='Communications And Notifications']")
        login.execute_script("window.scrollTo(0, document.body.scrollHeight);", commun)
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Notifications']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//h2[normalize-space()='Custom Templates']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create New']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='context']//div[@aria-label='dropdown trigger']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[@id='p-highlighted-option']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='displayName']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Share Prescription']")
        time.sleep(3)
        uniquename = f"Share{''.join(random.choices(string.ascii_letters + string.digits, k=8))}"
        wait_and_send_keys(login, By.XPATH, "//div[@class='form-group']//input[contains(@class, 'p-inputtext')]", uniquename)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//input[@id='mat-mdc-checkbox-1-input']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//input[@id='mat-mdc-checkbox-2-input']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save & Next']")
        time.sleep(2)
        editors = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']//p"))
        )
        editors.click()
        while True:
            try:
                # Click to open the dropdown menu
                wait_and_locate_click(login, By.XPATH, "//div[@class='form-group text-ceditor pointer-cursor']//span[@class='mgn-lt-5'][normalize-space()='Add Variables']")
                time.sleep(2)
                
                # Define the dropdown and options locators
                dropdown_xpath = "//div[@class='p-dropdown-items-wrapper']//ul[@role='listbox']"
                options_xpath = ".//li[@role='option']"
                
                # Wait until the dropdown menu is visible
                WebDriverWait(login, 10).until(
                    EC.visibility_of_element_located((By.XPATH, dropdown_xpath))
                )

                while True:
                    try:
                        # Locate the dropdown menu and all options in it
                        dropdown_element = login.find_element(By.XPATH, dropdown_xpath)
                        options = dropdown_element.find_elements(By.XPATH, options_xpath)
                        
                        # If no options found, break the loop
                        if not options:
                            print("No more options found.")
                            return
                        formatted_text = {}  # Initialize a dictionary to store options
                        # Iterate over options and select each one
                        for i in range(len(options)):
                            try:
                                # Get the updated options list
                                dropdown_element = login.find_element(By.XPATH, dropdown_xpath)
                                options = dropdown_element.find_elements(By.XPATH, options_xpath)
                                option = options[i]  # Select the current option
                                
                                # Wait until the option is clickable
                                WebDriverWait(login, 10).until(
                                    EC.element_to_be_clickable(option)
                                )
                                
                                option_text = option.text
                                # Store the formatted text
                                formatted_text[i] = option_text
                                print(f"Selecting option: {option_text} at position {i}")
                                option.click()
                                time.sleep(1)  # Adjust the delay as needed

                                # Reopen the dropdown menu
                                wait_and_locate_click(login, By.XPATH, "//div[@class='form-group text-ceditor pointer-cursor']//span[@class='mgn-lt-5'][normalize-space()='Add Variables']")
                                time.sleep(2)

                            except Exception as e:
                                print(f"Error selecting option: {e}")
                                break
                        # Exit if no more options can be selected
                        break
                        
                    except Exception as e:
                        print(f"Error while interacting with dropdown: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")
                break
                                 
         # Construct the final message with the formatted options
        editor_text = (
            f"Hello {formatted_text.get(0, '[d_var_consumerName]')}\n"
            f"Your {formatted_text.get(1, '[d_var_providerName]')} {formatted_text.get(2, '[d_var_business]')} has shared a prescription with you.\n"
            f"Doctor's Note: {formatted_text.get(3, '[d_var_message]')}\n"
            f"Link: {formatted_text.get(4, '[d_var_prescriptionLink]')}"
        )
        # Debug output
        print(f"Constructed editor text:\n{editor_text}")
        # Add the final formatted text to the editor
        add_text_to_editor(login, editor_text)
        # wait_and_locate_click(login, By.XPATH, "//div[@class='actiondiv mgn-lt-10 desktop-only']//button[@type='submit'][normalize-space()='Update']")
        time.sleep(2)
        # wait_and_visible_click(login, By.XPATH, "(//span[contains(text(),'Inactive')])[1]")
        # time.sleep(2)
            

        
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  