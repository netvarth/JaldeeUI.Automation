from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.common import TimeoutException

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("MR_COMM_TEMPLATE")
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
        wait_and_send_keys(login, By.XPATH, "//div[@class='form-group']//input[contains(@class, 'p-inputtext')]", 'Share')
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
        wait_and_locate_click(login, By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']//p")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//div[@class='form-group text-ceditor pointer-cursor']//span[@class='mgn-lt-5'][normalize-space()='Add Variables']")
        time.sleep(2)
        # Wait until the dropdown menu is visible
        dropdown_xpath = "//div[@class='p-dropdown-items-wrapper']//ul[@role='listbox']"
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, dropdown_xpath))
        )
       # Iterate over and select each option
        while True:
            try:
                # Locate the dropdown menu
                dropdown_element = login.find_element(By.XPATH, dropdown_xpath)
                
                # Locate all options in the dropdown menu
                options_xpath = ".//li[@role='option']"
                options = dropdown_element.find_elements(By.XPATH, options_xpath)
                
                # If no options found, break the loop
                if not options:
                    break

                for option in options:
                    option_text = option.text
                    print(f"Selecting option: {option_text}")
                    option.click()
                    time.sleep(1)  # Adjust the delay as needed

                    # Reopen the dropdown menu for the next selection
                    wait_and_locate_click(login, By.XPATH, "//div[@class='form-group text-ceditor pointer-cursor']//span[@class='mgn-lt-5'][normalize-space()='Add Variables']")
                    time.sleep(2)
                    wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='context']//div[@aria-label='dropdown trigger']")
                    
                    # Wait until the dropdown menu is visible again
                    WebDriverWait(login, 10).until(
                        EC.visibility_of_element_located((By.XPATH, dropdown_xpath))
                    )
                    
            except Exception as e:
                print(f"An error occurred: {e}")
                break

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  