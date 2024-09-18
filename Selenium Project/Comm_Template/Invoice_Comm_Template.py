from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.common import TimeoutException

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoice Share Payment Link")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_paymentlink_sharing(login):
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
        test_check_and_toggle(login)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create New']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='context']//div[@aria-label='dropdown trigger']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[@id='p-highlighted-option']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='displayName']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Share Payment Link']")
        time.sleep(3)
        uniquename = f"Sharepay{''.join(random.choices(string.ascii_letters + string.digits, k=8))}"
        wait_and_send_keys(login, By.XPATH, "//div[@class='form-group']//input[contains(@class, 'p-inputtext')]", uniquename)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//input[@id='mat-mdc-checkbox-1-input']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//input[@id='mat-mdc-checkbox-2-input']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save & Next']")
        time.sleep(2)
        editors = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']//p"))
        )
        editors.click()
        editors.send_keys("Hello")
        editors.send_keys(Keys.SPACE)
        wait_and_locate_click(login, By.XPATH, "//div[@class='form-group text-ceditor pointer-cursor']//span[@class='mgn-lt-5'][normalize-space()='Add Variables']")
        time.sleep(2)
        consumer_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Consumer name']")) 
        )
        consumer_name.click()   
        editors.send_keys(Keys.ENTER)
        editors.send_keys("View Your Invoice")
        editors.send_keys(Keys.SPACE)  
        wait_and_locate_click(login, By.XPATH, "//div[@class='form-group text-ceditor pointer-cursor']//span[@class='mgn-lt-5'][normalize-space()='Add Variables']")
        time.sleep(2)
        payment_link = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Payment Link']")) 
        )
        payment_link.click()
        time.sleep(2)
        email_subject_line = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[1]/input[1]"))
        )
        email_subject_line.click()
        email_subject_line.send_keys("Jaldee Invoice Payment Link")
        time.sleep(2)
        header_notes = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[2]/input[1]"))
        )
        header_notes.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[3]")
        Payment_Link = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Payment Link']")) 
        )
        Payment_Link.click()
        time.sleep(2)
        salutation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[3]/input[1]"))
        )
        salutation.click()
        salutation.send_keys("Greetings!!")
        time.sleep(2)
        Signature = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[4]/input[1]"))
        )
        Signature.click()
        Signature.send_keys("Thank you for using Jaldee")
        time.sleep(2)
        Footer = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[5]/input[1]"))
        )
        Footer.click()
        Footer.send_keys("Powered by Jaldee business")
        time.sleep(2)
        # editors.send_keys(Keys.ENTER) 
        # wait_and_locate_click(login, By.XPATH, "//div[@class='form-group text-ceditor pointer-cursor']//span[@class='mgn-lt-5'][normalize-space()='Add Variables']")
        # business_name = WebDriverWait(login, 20).until(
        # EC.presence_of_element_located(
        #     (By.XPATH, "//li[@aria-label='Business Name']")) 
        # )
        # business_name.click()
        # editors.send_keys(Keys.ENTER)
        wait_and_locate_click(login, By.XPATH, "(//button[@type='submit'][normalize-space()='Update'])[1]")
        time.sleep(2)
        wait_and_visible_click(login, By.XPATH, "(//span[contains(text(),'Inactive')])[1]")
        time.sleep(2)
        WebDriverWait(login,20).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='pi pi-bars text-light']")
        )
        ).click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Finance')]")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create Invoice']")
        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Name or Phone or Email or Id']", '9400553615')
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 105']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add Procedure/Item']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='item-name'][normalize-space()='Consultation']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
        time.sleep(2)
        login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Get Payment']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Share Payment Link']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    



# Function to check and interact with elements
def test_check_and_toggle(login):
    wait = WebDriverWait(login, 10)
    while True:
        try:
            # Find all spans with the text 'Share Payment Link'
            share_payment_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[contains(text(),'Share Payment Link')]")))
            print(f"Found {len(share_payment_elements)} 'Share Payment Link' elements on the current page.")

            # Flag to check if any template was disabled
            template_disabled = False

            # Iterate through the elements
            for share_payment in share_payment_elements:
                try:
                    # Find the closest mat-slide-toggle element associated with the span
                    slide_toggle = share_payment.find_element(By.XPATH, "//span[normalize-space()='Active']")
                    # button = slide_toggle.find_element(By.XPATH, ".//button[contains(@class, 'mdc-switch')]")
                    # if 'mdc-switch--checked' in button.get_attribute('class'):
                        # Click the button to deactivate it
                    if slide_toggle.text == "Active":
                        # button.click()
                        slide_toggle.click()
                        print("Toggle button deactivated.")
                        template_disabled = True
                        break  # Exit the loop after processing one item
                except Exception as e:
                    print(f"Error processing 'Share Payment Link' element: {e}")
                    continue  # Continue with the next element if an error occurs

            # If a template was disabled, exit the loop
            if template_disabled:
                break

            # Try to find the next page button
            try:
                next_page_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']")))
                login.execute_script("arguments[0].scrollIntoView(true);", next_page_button)
                next_page_button.click()
                print("Navigating to the next page.")
                # Wait a bit after navigating to ensure the new page loads
                wait.until(EC.staleness_of(share_payment_elements[0]))  # Wait until old elements are no longer attached to the DOM
            except Exception as e:
                print(f"No more pages or error finding next page button: {e}")
                break  # Exit loop if no more pages or if an error occurs

        except Exception as e:
            print(f"An error occurred: {e}")
            break


def disable_active_templates(login):
    wait = WebDriverWait(login, 10)
    while True:
        try:
            # Find all spans with the text 'Share Payment Link'
            share_invoice_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[contains(text(),'Share Invoice Link')]")))
            print(f"Found {len(share_invoice_elements)} 'Share Payment Link' elements on the current page.")

            if not share_invoice_elements:
                print("No 'Share Invoice Link' elements found on this page.")
                break  # Exit loop if no elements found on the current page

            # Flag to check if any template was disabled
            template_disabled = False

            # Iterate through the elements
            for share_invoice in share_invoice_elements:
                try:
                    # Find the status text 'Active'
                    status_text_element = share_invoice.find_element(By.XPATH, ".//span[normalize-space()='Active']")
                    
                    if status_text_element.text == "Active":
                        # Click the status text to deactivate it
                        ActionChains(login).move_to_element(status_text_element).click().perform()
                        print("Template deactivated.")
                        template_disabled = True
                        break  # Exit the loop after processing one item
                except Exception as e:
                    print(f"Error processing 'Share Invoice Link' element: {e}")
                    continue  # Continue with the next element if an error occurs

            # If a template was disabled, exit the loop
            if template_disabled:
                break

            # Try to find the next page button
            try:
                next_page_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']")))
                next_page_button.click()
                print("Navigating to the next page.")
                # Wait a bit after navigating to ensure the new page loads
                wait.until(EC.staleness_of(share_invoice_elements[0]))  # Wait until old elements are no longer attached to the DOM
            except Exception as e:
                print(f"No more pages or error finding next page button: {e}")
                break  # Exit loop if no more pages or if an error occurs

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoice Share Pdf")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_invoicepdf_sharing(login):
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
        disable_active_templates(login)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create New']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='context']//div[@aria-label='dropdown trigger']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[@id='p-highlighted-option']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='displayName']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Share Invoice Link']")
        time.sleep(3)
        uniquename = f"ShareInvoice{''.join(random.choices(string.ascii_letters + string.digits, k=8))}"
        wait_and_send_keys(login, By.XPATH, "//div[@class='form-group']//input[contains(@class, 'p-inputtext')]", uniquename)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//input[@id='mat-mdc-checkbox-1-input']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//input[@id='mat-mdc-checkbox-2-input']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save & Next']")
        time.sleep(2)
        editors = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']//p"))
        )
        editors.click()
        editors.send_keys("Hello")
        editors.send_keys(Keys.SPACE)
        wait_and_locate_click(login, By.XPATH, "//div[@class='form-group text-ceditor pointer-cursor']//span[@class='mgn-lt-5'][normalize-space()='Add Variables']")
        time.sleep(2)
        consumer_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Consumer name']")) 
        )
        consumer_name.click()   
        editors.send_keys(Keys.ENTER)
        editors.send_keys("View Your Shared Invoice")
        editors.send_keys(Keys.SPACE)  
        wait_and_locate_click(login, By.XPATH, "//div[@class='form-group text-ceditor pointer-cursor']//span[@class='mgn-lt-5'][normalize-space()='Add Variables']")
        time.sleep(2)
        invoice_link = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Invoice Link']")) 
        )
        invoice_link.click()
        time.sleep(2)
        email_subject_line = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[1]/input[1]"))
        )
        email_subject_line.click()
        email_subject_line.send_keys("Jaldee Invoice PDF Link")
        time.sleep(2)
        header_notes = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[2]/input[1]"))
        )
        header_notes.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[3]")
        Invoice_Link = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Invoice Link']")) 
        )
        Invoice_Link.click()
        time.sleep(2)
        salutation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[3]/input[1]"))
        )
        salutation.click()
        salutation.send_keys("Greetings!!")
        time.sleep(2)
        Signature = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[4]/input[1]"))
        )
        Signature.click()
        Signature.send_keys("Thank you for using Jaldee")
        time.sleep(2)
        Footer = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[5]/input[1]"))
        )
        Footer.click()
        Footer.send_keys("Powered by Jaldee business")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@type='submit'][normalize-space()='Update'])[1]")
        time.sleep(2)
        wait_and_visible_click(login, By.XPATH, "(//span[contains(text(),'Inactive')])[1]")
        time.sleep(2)
        WebDriverWait(login,20).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='pi pi-bars text-light']")
        )
        ).click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Finance')]")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create Invoice']")
        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Name or Phone or Email or Id']", '9400553615')
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 105']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add Procedure/Item']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='item-name'][normalize-space()='Consultation']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
        time.sleep(2)
        login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Share PDF']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Appointment Invoice Share Pdf")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_appointmentinvoicepdf_sharing(login):
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
        disable_active_templates(login)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create New']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='context']//div[@aria-label='dropdown trigger']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[@id='p-highlighted-option']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='displayName']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Share Invoice Link']")
        time.sleep(3)
        uniquename = f"ShareInvoice{''.join(random.choices(string.ascii_letters + string.digits, k=8))}"
        wait_and_send_keys(login, By.XPATH, "//div[@class='form-group']//input[contains(@class, 'p-inputtext')]", uniquename)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//input[@id='mat-mdc-checkbox-1-input']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//input[@id='mat-mdc-checkbox-2-input']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save & Next']")
        time.sleep(2)
        editors = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']//p"))
        )
        editors.click()
        editors.send_keys("Hello")
        editors.send_keys(Keys.SPACE)
        wait_and_locate_click(login, By.XPATH, "//div[@class='form-group text-ceditor pointer-cursor']//span[@class='mgn-lt-5'][normalize-space()='Add Variables']")
        time.sleep(2)
        consumer_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Consumer name']")) 
        )
        consumer_name.click()   
        editors.send_keys(Keys.ENTER)
        editors.send_keys("View Your Shared Invoice")
        editors.send_keys(Keys.SPACE)  
        wait_and_locate_click(login, By.XPATH, "//div[@class='form-group text-ceditor pointer-cursor']//span[@class='mgn-lt-5'][normalize-space()='Add Variables']")
        time.sleep(2)
        invoice_link = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Invoice Link']")) 
        )
        invoice_link.click()
        time.sleep(2)
        email_subject_line = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[1]/input[1]"))
        )
        email_subject_line.click()
        email_subject_line.send_keys("Jaldee Invoice PDF Link")
        time.sleep(2)
        header_notes = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[2]/input[1]"))
        )
        header_notes.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[3]")
        Invoice_Link = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Invoice Link']")) 
        )
        Invoice_Link.click()
        time.sleep(2)
        salutation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[3]/input[1]"))
        )
        salutation.click()
        salutation.send_keys("Greetings!!")
        time.sleep(2)
        Signature = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[4]/input[1]"))
        )
        Signature.click()
        Signature.send_keys("Thank you for using Jaldee")
        time.sleep(2)
        Footer = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[5]/input[1]"))
        )
        Footer.click()
        Footer.send_keys("Powered by Jaldee business")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@type='submit'][normalize-space()='Update'])[1]")
        time.sleep(2)
        wait_and_visible_click(login, By.XPATH, "(//span[contains(text(),'Inactive')])[1]")
        time.sleep(2)
        WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[@src='./assets/images/menu/home-color.png']"))
        ).click()

        WebDriverWait(login, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]",
                )
            )
        ).click()
        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]",
                )
            )
        )
        element.click()
        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
            )
        ).send_keys("9400553615")
        time.sleep(2)
        login.implicitly_wait(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Id : 105']")
            )
        ).click()

        login.implicitly_wait(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "p-dropdown[optionlabel='place']")
            )
        ).click()

        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        login.implicitly_wait(5)

        login.find_element(
            By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']"
        ).click()
        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
        print("Department : ENT")
        user_dropdown_xpath = (
            "(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
            "ng-dirty'])[1]"
        )
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))
        ).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, user_option_xpath))
        ).click()
        print("Select user : Naveen")

        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        element = login.find_element(By.XPATH, service_dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        service_option_xpath = (
            "(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
            "Consultation'])[2]"
        )
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, service_option_xpath))
        ).click()
        print("Select Service : Naveen Consultation")
        time.sleep(5)
        Today_Date = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']",
                )
            )
        )
        
        Today_Date.click()
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Confirm')]")
            )
        ).click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(5)

        while True:
            try:

                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                        )
                    )
                )

                next_button.click()

            except:

                break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
                )
            )
        )
        last_element_in_accordian.click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Invoice']"))
        ).click()

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Share PDF']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Token Invoice Share Pdf")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_tokeninvoicepdf_sharing(login):
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
        disable_active_templates(login)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create New']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='context']//div[@aria-label='dropdown trigger']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[@id='p-highlighted-option']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='displayName']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Share Invoice Link']")
        time.sleep(3)
        uniquename = f"ShareInvoice{''.join(random.choices(string.ascii_letters + string.digits, k=8))}"
        wait_and_send_keys(login, By.XPATH, "//div[@class='form-group']//input[contains(@class, 'p-inputtext')]", uniquename)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//input[@id='mat-mdc-checkbox-1-input']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//input[@id='mat-mdc-checkbox-2-input']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save & Next']")
        time.sleep(2)
        editors = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']//p"))
        )
        editors.click()
        editors.send_keys("Hello")
        editors.send_keys(Keys.SPACE)
        wait_and_locate_click(login, By.XPATH, "//div[@class='form-group text-ceditor pointer-cursor']//span[@class='mgn-lt-5'][normalize-space()='Add Variables']")
        time.sleep(2)
        consumer_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Consumer name']")) 
        )
        consumer_name.click()   
        editors.send_keys(Keys.ENTER)
        editors.send_keys("View Your Shared Invoice")
        editors.send_keys(Keys.SPACE)  
        wait_and_locate_click(login, By.XPATH, "//div[@class='form-group text-ceditor pointer-cursor']//span[@class='mgn-lt-5'][normalize-space()='Add Variables']")
        time.sleep(2)
        invoice_link = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Invoice Link']")) 
        )
        invoice_link.click()
        time.sleep(2)
        email_subject_line = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[1]/input[1]"))
        )
        email_subject_line.click()
        email_subject_line.send_keys("Jaldee Invoice PDF Link")
        time.sleep(2)
        header_notes = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[2]/input[1]"))
        )
        header_notes.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[3]")
        Invoice_Link = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Invoice Link']")) 
        )
        Invoice_Link.click()
        time.sleep(2)
        salutation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[3]/input[1]"))
        )
        salutation.click()
        salutation.send_keys("Greetings!!")
        time.sleep(2)
        Signature = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[4]/input[1]"))
        )
        Signature.click()
        Signature.send_keys("Thank you for using Jaldee")
        time.sleep(2)
        Footer = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[5]/input[1]"))
        )
        Footer.click()
        Footer.send_keys("Powered by Jaldee business")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@type='submit'][normalize-space()='Update'])[1]")
        time.sleep(2)
        wait_and_visible_click(login, By.XPATH, "(//span[contains(text(),'Inactive')])[1]")
        time.sleep(2)
        WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[@src='./assets/images/menu/home-color.png']"))
        ).click()

        WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Tokens')]"))
        ).click()
        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Token']"))
        )
        element.click()

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
            )
        ).send_keys("9400553615")
        time.sleep(2)
        login.implicitly_wait(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 105']"))
        ).click()

        time.sleep(3)
        wait = WebDriverWait(login, 10)
        Today_Date = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']",
                )
            )
        )
        Today_Date.click()
        print("Today Date:", Today_Date.text)

        print("Time Slot: 00:00 AM - 11:59 PM")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
        ).click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(5)
        while True:
            try:
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                        )
                    )
                )

                next_button.click()

            except:
                break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
                )
            )
        )
        last_element_in_accordian.click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Invoice']"))
        ).click()

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Share PDF']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Appointment Invoice Share Pdf")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_autogeninvoiceoff_paymentsharing(login):
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
        test_check_and_toggle(login)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create New']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='context']//div[@aria-label='dropdown trigger']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[@id='p-highlighted-option']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='displayName']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Share Payment Link']")
        time.sleep(3)
        uniquename = f"ShareInvoice{''.join(random.choices(string.ascii_letters + string.digits, k=8))}"
        wait_and_send_keys(login, By.XPATH, "//div[@class='form-group']//input[contains(@class, 'p-inputtext')]", uniquename)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//input[@id='mat-mdc-checkbox-1-input']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//input[@id='mat-mdc-checkbox-2-input']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save & Next']")
        time.sleep(2)
        editors = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']//p"))
        )
        editors.click()
        editors.send_keys("Hello")
        editors.send_keys(Keys.SPACE)
        wait_and_locate_click(login, By.XPATH, "//div[@class='form-group text-ceditor pointer-cursor']//span[@class='mgn-lt-5'][normalize-space()='Add Variables']")
        time.sleep(2)
        consumer_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Consumer name']")) 
        )
        consumer_name.click()   
        editors.send_keys(Keys.ENTER)
        editors.send_keys("Click Your Payment Link")
        editors.send_keys(Keys.SPACE)  
        wait_and_locate_click(login, By.XPATH, "//div[@class='form-group text-ceditor pointer-cursor']//span[@class='mgn-lt-5'][normalize-space()='Add Variables']")
        time.sleep(2)
        invoice_link = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Payment Link']")) 
        )
        invoice_link.click()
        time.sleep(2)
        email_subject_line = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[1]/input[1]"))
        )
        email_subject_line.click()
        email_subject_line.send_keys("Jaldee Invoice payment Link")
        time.sleep(2)
        header_notes = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[2]/input[1]"))
        )
        header_notes.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[3]")
        Invoice_Link = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Payment Link']")) 
        )
        Invoice_Link.click()
        time.sleep(2)
        salutation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[3]/input[1]"))
        )
        salutation.click()
        salutation.send_keys("Greetings!!")
        time.sleep(2)
        Signature = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[4]/input[1]"))
        )
        Signature.click()
        Signature.send_keys("Thank you for using Jaldee")
        time.sleep(2)
        Footer = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[5]/input[1]"))
        )
        Footer.click()
        Footer.send_keys("Powered by Jaldee business")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@type='submit'][normalize-space()='Update'])[1]")
        time.sleep(2)
        wait_and_visible_click(login, By.XPATH, "(//span[contains(text(),'Inactive')])[1]")
        time.sleep(2)
        WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[@src='./assets/images/menu/home-color.png']"))
        ).click()

        WebDriverWait(login, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]",
                )
            )
        ).click()
        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]",
                )
            )
        )
        element.click()
        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
            )
        ).send_keys("9400553615")
        time.sleep(2)
        login.implicitly_wait(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Id : 105']")
            )
        ).click()

        login.implicitly_wait(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "p-dropdown[optionlabel='place']")
            )
        ).click()

        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        login.implicitly_wait(5)

        login.find_element(
            By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']"
        ).click()
        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
        print("Department : ENT")
        user_dropdown_xpath = (
            "(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
            "ng-dirty'])[1]"
        )
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))
        ).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, user_option_xpath))
        ).click()
        print("Select user : Naveen")

        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        element = login.find_element(By.XPATH, service_dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        service_option_xpath = (
            "//li[contains(@aria-label,'service')]//div[1]"
        )
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, service_option_xpath))
        ).click()
        print("Select Service : Naveen Consultation")
        time.sleep(5)
        Today_Date = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']",
                )
            )
        )
        
        Today_Date.click()
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Confirm')]")
            )
        ).click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(5)

        while True:
            try:

                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                        )
                    )
                )

                next_button.click()

            except:

                break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
                )
            )
        )
        last_element_in_accordian.click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Payment Info']"))
        ).click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Get Payment']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Share Payment Link']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

    

    

    

    


    

  
    
