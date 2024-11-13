from Framework.common_utils import *
import allure
from allure_commons.types import AttachmentType
import os
first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Auto Invoice for Walkin Appointment and Sharepayment link and Settled")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appointment_autoinvoice(login):
    try:
        time.sleep(5)
        wait_and_click(login, By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]") 
        time.sleep(2)
        wait_and_click(login, By.XPATH, "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]") 
        time.sleep(3)
        wait_and_click(login, By.XPATH, "//b[contains(text(),'Create New Patient')]") 
        time.sleep(3)
        login.implicitly_wait(3)

        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(5)
        wait_and_click(login, By.CSS_SELECTOR, "p-dropdown[optionlabel='place']") 
        time.sleep(3)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
        print("Department : ENT")
        user_dropdown_xpath = ("(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
                            "ng-dirty'])[1]")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_option_xpath))).click()
        print("Select user : Naveen")

        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        service = login.find_element(By.XPATH, service_dropdown_xpath)
        scroll_to_element(login, service)
        service.click()

        service_option_xpath = ("(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
                                "Consultation'])[2]")
        wait_and_click(login, By.XPATH, service_option_xpath) 
        print("Select Service : Naveen Consultation")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']") 
        time_slot = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
        time_slot.click()
        print("Time Slot:", time_slot.text)
        note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
        scroll_to_element(login,note_input)
        time.sleep(2)
        note_input.click()
        time.sleep(2)
        login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Save']")
        time.sleep(2)
        login.find_element(By.XPATH,
                        "//span[normalize-space()='Confirm']").click()
        
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        

        while True:
            try:
                print("before in loop")
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
                )

                next_button.click()

            except:
                print("EC caught:")
                break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()
        time.sleep(3)
        viewdetails = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='View Details'])[1]"))
        )
        scroll_to_element(login, viewdetails)
        time.sleep(2)
        viewdetails.click()
        time.sleep(3)
        booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='fw-bold ng-star-inserted'])[1]"))
        )
        actual_booking_id = booking_Id.text.strip('"').strip()
        print("Actual_BookingId:",actual_booking_id)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Invoices'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]") 
        time.sleep(2)
        invoice_booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Booking Reference :']/following-sibling::div[contains(@class, 'invoice-detail-style')]"))
        )
        expected_invoice_booking_Id = invoice_booking_Id.text.strip('"')
        print("Expected_BookingId:",expected_invoice_booking_Id)
        print(f"Expected_BookingId: '{expected_invoice_booking_Id}', Actual_BookingId: '{actual_booking_id}'")
        assert actual_booking_id == expected_invoice_booking_Id, f"Expected_BookingId: '{expected_invoice_booking_Id}', but got Actual_BookingId: '{actual_booking_id}'"
        time.sleep(2)
        scroll_to_window(login)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Share Payment Link']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        expected_message = "The invoice has been sent to the patient"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Settle Invoice']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "Invoice Settled Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(3)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Auto Invoice paybycash for Walkin Appointment and Settled Invoice")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appointment_paybycash(login):
    try:
        time.sleep(5)
        wait_and_click(login, By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]") 
        time.sleep(2)
        wait_and_click(login, By.XPATH, "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]") 
        time.sleep(3)
        wait_and_click(login, By.XPATH, "//b[contains(text(),'Create New Patient')]") 
        time.sleep(3)
        login.implicitly_wait(3)

        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(5)
        wait_and_click(login, By.CSS_SELECTOR, "p-dropdown[optionlabel='place']") 
        time.sleep(3)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
        print("Department : ENT")
        user_dropdown_xpath = ("(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
                            "ng-dirty'])[1]")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_option_xpath))).click()
        print("Select user : Naveen")

        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        service = login.find_element(By.XPATH, service_dropdown_xpath)
        scroll_to_element(login, service)
        service.click()

        service_option_xpath = ("(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
                                "Consultation'])[2]")
        wait_and_click(login, By.XPATH, service_option_xpath) 
        print("Select Service : Naveen Consultation")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']") 
        time_slot = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
        time_slot.click()
        print("Time Slot:", time_slot.text)
        note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
        scroll_to_element(login,note_input)
        time.sleep(2)
        note_input.click()
        time.sleep(2)
        login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Save']")
        time.sleep(2)
        login.find_element(By.XPATH,
                        "//span[normalize-space()='Confirm']").click()
        
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        

        while True:
            try:
                print("before in loop")
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
                )

                next_button.click()

            except:
                print("EC caught:")
                break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()
        time.sleep(3)
        viewdetails = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='View Details'])[1]"))
        )
        scroll_to_element(login, viewdetails)
        time.sleep(2)
        viewdetails.click()
        time.sleep(3)
        booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='fw-bold ng-star-inserted'])[1]"))
        )
        actual_booking_id = booking_Id.text.strip('"').strip()
        print("Actual_BookingId:",actual_booking_id)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Invoices'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]") 
        time.sleep(2)
        invoice_booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Booking Reference :']/following-sibling::div[contains(@class, 'invoice-detail-style')]"))
        )
        expected_invoice_booking_Id = invoice_booking_Id.text.strip('"')
        print("Expected_BookingId:",expected_invoice_booking_Id)
        print(f"Expected_BookingId: '{expected_invoice_booking_Id}', Actual_BookingId: '{actual_booking_id}'")
        assert actual_booking_id == expected_invoice_booking_Id, f"Expected_BookingId: '{expected_invoice_booking_Id}', but got Actual_BookingId: '{actual_booking_id}'"
        time.sleep(2)
        scroll_to_window(login)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Pay by Cash']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Pay']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        expected_message = "Payment completed successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Settle Invoice']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "Invoice Settled Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(3)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Auto Invoice paybyothers for Walkin Appointment and Cancelled Invoice")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appointment_paybyothers(login):
    try:
        time.sleep(5)
        wait_and_click(login, By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]") 
        time.sleep(2)
        wait_and_click(login, By.XPATH, "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]") 
        time.sleep(3)
        wait_and_click(login, By.XPATH, "//b[contains(text(),'Create New Patient')]") 
        time.sleep(3)
        login.implicitly_wait(3)

        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(5)
        wait_and_click(login, By.CSS_SELECTOR, "p-dropdown[optionlabel='place']") 
        time.sleep(3)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
        print("Department : ENT")
        user_dropdown_xpath = ("(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
                            "ng-dirty'])[1]")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_option_xpath))).click()
        print("Select user : Naveen")

        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        service = login.find_element(By.XPATH, service_dropdown_xpath)
        scroll_to_element(login, service)
        service.click()

        service_option_xpath = ("(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
                                "Consultation'])[2]")
        wait_and_click(login, By.XPATH, service_option_xpath) 
        print("Select Service : Naveen Consultation")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']") 
        time_slot = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
        time_slot.click()
        print("Time Slot:", time_slot.text)
        note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
        scroll_to_element(login,note_input)
        time.sleep(2)
        note_input.click()
        time.sleep(2)
        login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Save']")
        time.sleep(2)
        login.find_element(By.XPATH,
                        "//span[normalize-space()='Confirm']").click()
        
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        

        while True:
            try:
                print("before in loop")
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
                )

                next_button.click()

            except:
                print("EC caught:")
                break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()
        time.sleep(3)
        viewdetails = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='View Details'])[1]"))
        )
        scroll_to_element(login, viewdetails)
        time.sleep(2)
        viewdetails.click()
        time.sleep(3)
        booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='fw-bold ng-star-inserted'])[1]"))
        )
        actual_booking_id = booking_Id.text.strip('"').strip()
        print("Actual_BookingId:",actual_booking_id)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Invoices'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]") 
        time.sleep(2)
        invoice_booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Booking Reference :']/following-sibling::div[contains(@class, 'invoice-detail-style')]"))
        )
        expected_invoice_booking_Id = invoice_booking_Id.text.strip('"')
        print("Expected_BookingId:",expected_invoice_booking_Id)
        print(f"Expected_BookingId: '{expected_invoice_booking_Id}', Actual_BookingId: '{actual_booking_id}'")
        assert actual_booking_id == expected_invoice_booking_Id, f"Expected_BookingId: '{expected_invoice_booking_Id}', but got Actual_BookingId: '{actual_booking_id}'"
        time.sleep(2)
        scroll_to_window(login)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Pay by Others']")
        time.sleep(2)
        paybutton = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Pay']"))
        )
        scroll_to_element(login, paybutton)
        time.sleep(2)
        paybutton.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        expected_message = "Payment completed successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Cancel Invoice']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "Invoice Cancelled Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(3)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Auto Invoice sharepdf for Walkin Appointment")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appointment_sharepdf(login):
    try:
        time.sleep(5)
        wait_and_click(login, By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]") 
        time.sleep(2)
        wait_and_click(login, By.XPATH, "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]") 
        time.sleep(3)
        wait_and_click(login, By.XPATH, "//b[contains(text(),'Create New Patient')]") 
        time.sleep(3)
        login.implicitly_wait(3)

        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(5)
        wait_and_click(login, By.CSS_SELECTOR, "p-dropdown[optionlabel='place']") 
        time.sleep(3)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
        print("Department : ENT")
        user_dropdown_xpath = ("(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
                            "ng-dirty'])[1]")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_option_xpath))).click()
        print("Select user : Naveen")

        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        service = login.find_element(By.XPATH, service_dropdown_xpath)
        scroll_to_element(login, service)
        service.click()

        service_option_xpath = ("(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
                                "Consultation'])[2]")
        wait_and_click(login, By.XPATH, service_option_xpath) 
        print("Select Service : Naveen Consultation")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']") 
        time_slot = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
        time_slot.click()
        print("Time Slot:", time_slot.text)
        note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
        scroll_to_element(login,note_input)
        time.sleep(2)
        note_input.click()
        time.sleep(2)
        login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Save']")
        time.sleep(2)
        login.find_element(By.XPATH,
                        "//span[normalize-space()='Confirm']").click()
        
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        

        while True:
            try:
                print("before in loop")
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
                )

                next_button.click()

            except:
                print("EC caught:")
                break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()
        time.sleep(3)
        viewdetails = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='View Details'])[1]"))
        )
        scroll_to_element(login, viewdetails)
        time.sleep(2)
        viewdetails.click()
        time.sleep(3)
        booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='fw-bold ng-star-inserted'])[1]"))
        )
        actual_booking_id = booking_Id.text.strip('"').strip()
        print("Actual_BookingId:",actual_booking_id)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Invoices'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]") 
        time.sleep(2)
        invoice_booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Booking Reference :']/following-sibling::div[contains(@class, 'invoice-detail-style')]"))
        )
        expected_invoice_booking_Id = invoice_booking_Id.text.strip('"')
        print("Expected_BookingId:",expected_invoice_booking_Id)
        print(f"Expected_BookingId: '{expected_invoice_booking_Id}', Actual_BookingId: '{actual_booking_id}'")
        assert actual_booking_id == expected_invoice_booking_Id, f"Expected_BookingId: '{expected_invoice_booking_Id}', but got Actual_BookingId: '{actual_booking_id}'"
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Share PDF']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "The invoice has been sent to the patient"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(3)

    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Auto Invoice discount and sharepdf for Walkin Appointment")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appointment_discountsharepdf(login):
    try:
        time.sleep(5)
        wait_and_click(login, By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]") 
        time.sleep(2)
        wait_and_click(login, By.XPATH, "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]") 
        time.sleep(3)
        wait_and_click(login, By.XPATH, "//b[contains(text(),'Create New Patient')]") 
        time.sleep(3)
        login.implicitly_wait(3)

        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(5)
        wait_and_click(login, By.CSS_SELECTOR, "p-dropdown[optionlabel='place']") 
        time.sleep(3)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
        print("Department : ENT")
        user_dropdown_xpath = ("(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
                            "ng-dirty'])[1]")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_option_xpath))).click()
        print("Select user : Naveen")

        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        service = login.find_element(By.XPATH, service_dropdown_xpath)
        scroll_to_element(login, service)
        service.click()

        service_option_xpath = ("(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
                                "Consultation'])[2]")
        wait_and_click(login, By.XPATH, service_option_xpath) 
        print("Select Service : Naveen Consultation")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']") 
        time_slot = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
        time_slot.click()
        print("Time Slot:", time_slot.text)
        note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
        scroll_to_element(login,note_input)
        time.sleep(2)
        note_input.click()
        time.sleep(2)
        login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Save']")
        time.sleep(2)
        login.find_element(By.XPATH,
                        "//span[normalize-space()='Confirm']").click()
        
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        

        while True:
            try:
                print("before in loop")
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
                )

                next_button.click()

            except:
                print("EC caught:")
                break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()
        time.sleep(3)
        viewdetails = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='View Details'])[1]"))
        )
        scroll_to_element(login, viewdetails)
        time.sleep(2)
        viewdetails.click()
        time.sleep(3)
        booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='fw-bold ng-star-inserted'])[1]"))
        )
        actual_booking_id = booking_Id.text.strip('"').strip()
        print("Actual_BookingId:",actual_booking_id)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Invoices'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]") 
        time.sleep(2)
        invoice_booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Booking Reference :']/following-sibling::div[contains(@class, 'invoice-detail-style')]"))
        )
        expected_invoice_booking_Id = invoice_booking_Id.text.strip('"')
        print("Expected_BookingId:",expected_invoice_booking_Id)
        print(f"Expected_BookingId: '{expected_invoice_booking_Id}', Actual_BookingId: '{actual_booking_id}'")
        assert actual_booking_id == expected_invoice_booking_Id, f"Expected_BookingId: '{expected_invoice_booking_Id}', but got Actual_BookingId: '{actual_booking_id}'"
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Edit']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[@class='symbol-label']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-list-item__primary-text'][normalize-space()='Apply Discount']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//select[./option[text()='Select Discount']])[3]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//option[normalize-space()='On Demand Discount'])[3]")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Amount']", 50)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Apply'])[3]")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "Discount Applied Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Update']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "Updated Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Share PDF']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "The invoice has been sent to the patient"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(3)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Auto Invoice edit and add adhocitem and subservice for Walkin Appointment")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appointment_adhocitem_subservice_sharepdf(login):
    try:
        time.sleep(5)
        wait_and_click(login, By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]") 
        time.sleep(2)
        wait_and_click(login, By.XPATH, "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]") 
        time.sleep(3)
        wait_and_click(login, By.XPATH, "//b[contains(text(),'Create New Patient')]") 
        time.sleep(3)
        login.implicitly_wait(3)

        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(5)
        wait_and_click(login, By.CSS_SELECTOR, "p-dropdown[optionlabel='place']") 
        time.sleep(3)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
        print("Department : ENT")
        user_dropdown_xpath = ("(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
                            "ng-dirty'])[1]")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_option_xpath))).click()
        print("Select user : Naveen")

        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        service = login.find_element(By.XPATH, service_dropdown_xpath)
        scroll_to_element(login, service)
        service.click()

        service_option_xpath = ("(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
                                "Consultation'])[2]")
        wait_and_click(login, By.XPATH, service_option_xpath) 
        print("Select Service : Naveen Consultation")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']") 
        time_slot = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
        time_slot.click()
        print("Time Slot:", time_slot.text)
        note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
        scroll_to_element(login,note_input)
        time.sleep(2)
        note_input.click()
        time.sleep(2)
        login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Save']")
        time.sleep(2)
        login.find_element(By.XPATH,
                        "//span[normalize-space()='Confirm']").click()
        
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        

        while True:
            try:
                print("before in loop")
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
                )

                next_button.click()

            except:
                print("EC caught:")
                break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()
        time.sleep(3)
        viewdetails = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='View Details'])[1]"))
        )
        scroll_to_element(login, viewdetails)
        time.sleep(2)
        viewdetails.click()
        time.sleep(3)
        booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='fw-bold ng-star-inserted'])[1]"))
        )
        actual_booking_id = booking_Id.text.strip('"').strip()
        print("Actual_BookingId:",actual_booking_id)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Invoices'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]") 
        time.sleep(2)
        invoice_booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Booking Reference :']/following-sibling::div[contains(@class, 'invoice-detail-style')]"))
        )
        expected_invoice_booking_Id = invoice_booking_Id.text.strip('"')
        print("Expected_BookingId:",expected_invoice_booking_Id)
        print(f"Expected_BookingId: '{expected_invoice_booking_Id}', Actual_BookingId: '{actual_booking_id}'")
        assert actual_booking_id == expected_invoice_booking_Id, f"Expected_BookingId: '{expected_invoice_booking_Id}', but got Actual_BookingId: '{actual_booking_id}'"
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Edit']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[@class='symbol-label']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Add Procedure/']")
        time.sleep(2)
        itemname = f"item{''.join(random.choices(string.ascii_letters + string.digits, k=8))}"
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Choose Procedure/Item']", itemname)
        time.sleep(2)
        quantity = login.find_element(By.XPATH, "(//input[@id='mat-input-4'])[1]")
        quantity.clear()
        quantity_input_value = random.randint(1, 10)  # Random number for quantity
        quantity.send_keys(str(quantity_input_value))
        time.sleep(2)
        price = login.find_element(By.XPATH, "(//input[@id='mat-input-4'])[2]")
        price.clear()
        price_input_value = random.randint(5, 500)  # Random number for quantity
        price.send_keys(str(price_input_value))
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='symbol-label']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Add Procedure/']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//input[@placeholder='Choose Procedure/Item']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[normalize-space()='Naveen Consultation 1']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='p-multiselect-label p-placeholder']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='p-checkbox p-component'])[1]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Update']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "Updated Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Share PDF']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "The invoice has been sent to the patient"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//i[@class='fa fa-arrow-left']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='fa fa-arrow-left']")
        time.sleep(2)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e
 
from Framework.consumer_common_utils import *

@pytest.fixture()
def consumer_onlineappointment_booking_id(consumer_login):
    print("Online Appointment")
    try:
        consumer_data = create_consumer_data()
        time.sleep(5)
        # Scroll to the element
        book_now_button = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Book Now']")
            )
        )
        consumer_login.execute_script("arguments[0].scrollIntoView();", book_now_button)

        # Wait for the element to be clickable
        clickable_book_now_button = WebDriverWait(consumer_login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Book Now']"))
        )

        # Attempt to click the element
        try:
            clickable_book_now_button.click()
        except:
            # If click is intercepted, click using JavaScript
            consumer_login.execute_script("arguments[0].click();", clickable_book_now_button)

        wait = WebDriverWait(consumer_login, 10)
        location_button = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='deptName ng-star-inserted'][contains(text(),'Chavakkad')]",
                )
            )
        )
        location_button.click()

        wait = WebDriverWait(consumer_login, 10)
        depart_button = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='deptName ng-star-inserted'][normalize-space()='ENT']",
                )
            )
        )
        depart_button.click()

        wait = WebDriverWait(consumer_login, 10)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Dr.Naveen KP')]")
            )
        ).click()

        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//app-appointment-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][contains(text(),'service')]",
                )
            )
        ).click()
        time.sleep(3)
        consumer_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        Today_Date = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(@class, 'mat-calendar-body-cell') and contains(@class, 'mat-calendar-body-active') and contains(@class, 'example-custom-date-class') and @aria-pressed='true' and @aria-current='date']")
            )
        )
        Today_Date.click()
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(consumer_login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='mdc-evolution-chip__cell mdc-evolution-chip__cell--primary'])[1]"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)
        next_button = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Next']")
            )
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", next_button)
        next_button.click()
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        ).send_keys(consumer_data['phonenumber'])
        print("New Consumer Phone Number:", consumer_data['phonenumber'])
        consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        time.sleep(5)
        otp_inputs = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )
        for i, otp_input in enumerate(otp_inputs):
            otp_input.send_keys(consumer_data['otp'][i])
        consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='first_name'])[1]"))
        ).send_keys(consumer_data['first_name'])
        print("New Consumer Firstname:", consumer_data['first_name'])
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='first_name'])[2]"))
        ).send_keys(consumer_data['last_name'])
        print("New Consumer Lastname:", consumer_data['last_name'])
        consumer_login.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        time.sleep(5)
        consumer_notes = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Add Notes you may have...']")
            )
        )
        consumer_notes.send_keys("Notes added from conumser side")
        time.sleep(3)
        uploadfile = WebDriverWait(consumer_login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='uploadFileTxt']"))
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", uploadfile)
        time.sleep(2)
        uploadfile.click()
        time.sleep(2)
        current_working_directory = os.getcwd()
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        time.sleep(3)
        confirmbutton = WebDriverWait(consumer_login, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm']")
            )
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", confirmbutton)
        time.sleep(2)
        confirmbutton.click()
        time.sleep(5)
        booking_id_element = consumer_login.find_element(By.XPATH, "//div[@class='bookingIdFlex ng-star-inserted']")
        full_text = booking_id_element.text
        consumer_onlineappointment_booking_id = full_text.split(":")[1].strip()
        print("Booking ID:", consumer_onlineappointment_booking_id)
        
        time.sleep(2)
        Ok_button = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", Ok_button)
        time.sleep(2)
        Ok_button.click()
        time.sleep(2)
        print("New Consumer Appointment booking confirmed successfully")
        return consumer_onlineappointment_booking_id
        
    finally:
        consumer_login.quit()




from Framework.common_utils import *
import allure
from allure_commons.types import AttachmentType
import os

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Auto Invoice for online Appointment")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_onlineappointment_autoinvoice(consumer_onlineappointment_booking_id,login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        invoices = WebDriverWait(login, 15).until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Invoices'])[1]"))
        )
        scroll_to_element(login,invoices)
        time.sleep(2) 
        invoices.click()
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]") 
        time.sleep(2)
        invoice_booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Booking Reference :']/following-sibling::div[contains(@class, 'invoice-detail-style')]"))
        )
        expected_invoice_booking_Id = invoice_booking_Id.text.strip('"')
        print("Expected_BookingId:",expected_invoice_booking_Id)
        print(f"Expected_BookingId: '{expected_invoice_booking_Id}', Actual_BookingId: '{consumer_onlineappointment_booking_id}'")
        assert consumer_onlineappointment_booking_id == expected_invoice_booking_Id, f"Expected_BookingId: '{expected_invoice_booking_Id}', but got Actual_BookingId: '{consumer_onlineappointment_booking_id}'"
        time.sleep(2)
        scroll_to_window(login)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Share Payment Link']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        expected_message = "The invoice has been sent to the patient"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Settle Invoice']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "Invoice Settled Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(3)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e
    

from Framework.consumer_common_utils import *

@pytest.fixture()
def onlineprepayment_appointment_booking_id(consumer_login):
    try:
        print("Prepayment Appointment")
        # consumer_data = create_consumer_data()
        # time.sleep(5)
        # Scroll to the element
        book_now_button = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Book Now']")
            )
        )
        consumer_login.execute_script("arguments[0].scrollIntoView();", book_now_button)

        # Wait for the element to be clickable
        clickable_book_now_button = WebDriverWait(consumer_login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Book Now']"))
        )

        # Attempt to click the element
        try:
            clickable_book_now_button.click()
        except:
            # If click is intercepted, click using JavaScript
            consumer_login.execute_script("arguments[0].click();", clickable_book_now_button)

        wait = WebDriverWait(consumer_login, 10)
        location_button = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='deptName ng-star-inserted'][contains(text(),'Chavakkad')]",
                )
            )
        )
        location_button.click()

        wait = WebDriverWait(consumer_login, 10)
        depart_button = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='deptName ng-star-inserted'][normalize-space()='Global Service']",
                )
            )
        )
        depart_button.click()

        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//app-appointment-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][contains(text(),' Prepayment Consultation ')]",
                )
            )
        ).click()
        time.sleep(3)
        consumer_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        Today_Date = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(@class, 'mat-calendar-body-cell') and contains(@class, 'mat-calendar-body-active') and contains(@class, 'example-custom-date-class') and @aria-pressed='true' and @aria-current='date']")
            )
        )
        Today_Date.click()
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(consumer_login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='mdc-evolution-chip__cell mdc-evolution-chip__cell--primary'])[1]"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)
        next_button = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Next']")
            )
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", next_button)
        time.sleep(3)
        next_button.click()
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        ).send_keys(9400553615)
        
        consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        time.sleep(5)
        otp_digits = "5555"
        # otp_digits = "55555"
        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )

        for i, otp_input in enumerate(otp_inputs):
            otp_input.send_keys(otp_digits[i])

        consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

        time.sleep(3)


        WebDriverWait(consumer_login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(text(),'NET BANKING')]")
                )
        ).click()

        time.sleep(3)
        makepayment = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                        "//button[@type='button']//span[@class='mat-mdc-button-touch-target']",
                )
            )
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", makepayment)
        consumer_login.execute_script("arguments[0].click();", makepayment)
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[contains(@class,'ptm-paymode-name ptm-lightbold')]")
            )
        ).click()

        time.sleep(1)

        WebDriverWait(consumer_login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'SBI')]"))
        ).click()

        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class,'ptm-emi-overlay')]//div[contains(@class,'')]//div[@id='checkout-button']//button[contains(@class,'ptm-nav-selectable')][contains(text(),'Pay ₹100')]",
                )
            )
        ).click()

            # Handle the popup window
            # Save the current window handle
        main_window_handle = consumer_login.current_window_handle

            # Wait until the new window is present
        WebDriverWait(consumer_login, 10).until(EC.new_window_is_opened)

            # Get all window handles
        all_window_handles = consumer_login.window_handles

            # Find the new window handle (the popup window)
        new_window_handle = None
        for handle in all_window_handles:
            if handle != main_window_handle:
                new_window_handle = handle
                break

            # Switch to the new window
        consumer_login.switch_to.window(new_window_handle)
        # Now interact with elements in the new window
        # For example, clicking the success button
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btnd']"))
        ).click()
        time.sleep(2)
        consumer_login.switch_to.window(main_window_handle)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        bookings_id_element = consumer_login.find_element(By.XPATH, "//div[@class='bookingIdFlex ng-star-inserted']")
        full_texts = bookings_id_element.text
        onlineprepayment_appointment_booking_id = full_texts.split(":")[1].strip()
        print("Booking ID:", onlineprepayment_appointment_booking_id)
        time.sleep(2)
        Ok_button = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", Ok_button)
        time.sleep(2)
        Ok_button.click()
        time.sleep(3)
        print("New Consumer Prepayment Appointment booking confirmed successfully")
        time.sleep(3)
        return onlineprepayment_appointment_booking_id
        
    finally:
        consumer_login.quit()

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Auto Invoice for online Prepayment Appointment")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_onlineprepaidappointment_autoinvoice(onlineprepayment_appointment_booking_id,login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        invoices = WebDriverWait(login, 15).until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Invoices'])[1]"))
        )
        scroll_to_element(login,invoices)
        time.sleep(2) 
        invoices.click()
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]") 
        time.sleep(2)
        invoice_booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Booking Reference :']/following-sibling::div[contains(@class, 'invoice-detail-style')]"))
        )
        expected_invoice_booking_Id = invoice_booking_Id.text.strip('"')
        print("Expected_BookingId:",expected_invoice_booking_Id)
        print(f"Expected_BookingId: '{expected_invoice_booking_Id}', Actual_BookingId: '{onlineprepayment_appointment_booking_id}'")
        assert onlineprepayment_appointment_booking_id == expected_invoice_booking_Id, f"Expected_BookingId: '{expected_invoice_booking_Id}', but got Actual_BookingId: '{onlineprepayment_appointment_booking_id}'"
        time.sleep(2)
        scroll_to_window(login)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Pay by Cash']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Pay']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        expected_message = "Payment completed successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Settle Invoice']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "Invoice Settled Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(3)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Auto Invoice for online Prepayment Appointment and Refund")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_onlineprepaidappointment_refund(onlineprepayment_appointment_booking_id,login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        invoices = WebDriverWait(login, 15).until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Invoices'])[1]"))
        )
        scroll_to_element(login,invoices)
        time.sleep(2) 
        invoices.click()
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]") 
        time.sleep(2)
        invoice_booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Booking Reference :']/following-sibling::div[contains(@class, 'invoice-detail-style')]"))
        )
        expected_invoice_booking_Id = invoice_booking_Id.text.strip('"')
        print("Expected_BookingId:",expected_invoice_booking_Id)
        print(f"Expected_BookingId: '{expected_invoice_booking_Id}', Actual_BookingId: '{onlineprepayment_appointment_booking_id}'")
        assert onlineprepayment_appointment_booking_id == expected_invoice_booking_Id, f"Expected_BookingId: '{expected_invoice_booking_Id}', but got Actual_BookingId: '{onlineprepayment_appointment_booking_id}'"
        time.sleep(2)
        scroll_to_window(login)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Refund']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@class='btn btn-primary btn-square lh-p4 font-weight-bold font-size-xs ng-star-inserted'])[1]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Pay by Cash']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        print("Refund Pay by cash Successfully")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Settle Invoice']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "Invoice Settled Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(3)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e
    

from Framework.consumer_common_utils import *
import allure
from allure_commons.types import AttachmentType
import os
@pytest.fixture()
def onlineprepayment_appointment_AGOFF(consumer_login):
    try:
        print("Prepayment Appointment Autogenerate Invoice Off")
        # consumer_data = create_consumer_data()
        # time.sleep(5)
        # Scroll to the element
        book_now_button = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Book Now']")
            )
        )
        consumer_login.execute_script("arguments[0].scrollIntoView();", book_now_button)

        # Wait for the element to be clickable
        clickable_book_now_button = WebDriverWait(consumer_login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Book Now']"))
        )

        # Attempt to click the element
        try:
            clickable_book_now_button.click()
        except:
            # If click is intercepted, click using JavaScript
            consumer_login.execute_script("arguments[0].click();", clickable_book_now_button)

        wait = WebDriverWait(consumer_login, 10)
        location_button = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='deptName ng-star-inserted'][contains(text(),'Chavakkad')]",
                )
            )
        )
        location_button.click()

        wait = WebDriverWait(consumer_login, 10)
        depart_button = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='deptName ng-star-inserted'][normalize-space()='Global Service']",
                )
            )
        )
        depart_button.click()

        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//app-appointment-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][normalize-space()='Prepayment Consultation With AG Off']",
                )
            )
        ).click()
        time.sleep(3)
        consumer_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        Today_Date = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(@class, 'mat-calendar-body-cell') and contains(@class, 'mat-calendar-body-active') and contains(@class, 'example-custom-date-class') and @aria-pressed='true' and @aria-current='date']")
            )
        )
        Today_Date.click()
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(consumer_login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='mdc-evolution-chip__cell mdc-evolution-chip__cell--primary'])[1]"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)
        next_button = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Next']")
            )
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", next_button)
        time.sleep(3)
        next_button.click()
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        ).send_keys(9400553615)
        
        consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        time.sleep(5)
        otp_digits = "5555"
        # otp_digits = "55555"
        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )

        for i, otp_input in enumerate(otp_inputs):
            otp_input.send_keys(otp_digits[i])

        consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

        time.sleep(3)


        WebDriverWait(consumer_login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(text(),'NET BANKING')]")
                )
        ).click()

        time.sleep(3)
        makepayment = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                        "//button[@type='button']//span[@class='mat-mdc-button-touch-target']",
                )
            )
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", makepayment)
        consumer_login.execute_script("arguments[0].click();", makepayment)
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[contains(@class,'ptm-paymode-name ptm-lightbold')]")
            )
        ).click()

        time.sleep(1)

        WebDriverWait(consumer_login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'SBI')]"))
        ).click()

        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class,'ptm-emi-overlay')]//div[contains(@class,'')]//div[@id='checkout-button']//button[contains(@class,'ptm-nav-selectable')][contains(text(),'Pay ₹100')]",
                )
            )
        ).click()

            # Handle the popup window
            # Save the current window handle
        main_window_handle = consumer_login.current_window_handle

            # Wait until the new window is present
        WebDriverWait(consumer_login, 10).until(EC.new_window_is_opened)

            # Get all window handles
        all_window_handles = consumer_login.window_handles

            # Find the new window handle (the popup window)
        new_window_handle = None
        for handle in all_window_handles:
            if handle != main_window_handle:
                new_window_handle = handle
                break

            # Switch to the new window
        consumer_login.switch_to.window(new_window_handle)
        # Now interact with elements in the new window
        # For example, clicking the success button
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btnd']"))
        ).click()
        time.sleep(2)
        consumer_login.switch_to.window(main_window_handle)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        bookings_id_element = consumer_login.find_element(By.XPATH, "//div[@class='bookingIdFlex ng-star-inserted']")
        full_texts = bookings_id_element.text
        onlineprepayment_appointment_booking_id = full_texts.split(":")[1].strip()
        print("Booking ID:", onlineprepayment_appointment_booking_id)
        time.sleep(2)
        Ok_button = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", Ok_button)
        time.sleep(2)
        Ok_button.click()
        time.sleep(3)
        print("New Consumer Prepayment Appointment booking confirmed successfully")
        time.sleep(3)
        return onlineprepayment_appointment_booking_id
        
    finally:
        consumer_login.quit()

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Manual Invoice for online Prepayment Appointment")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_onlineprepaidappointment_AGOFF(onlineprepayment_appointment_AGOFF,login):
    try:
        time.sleep(5)
        wait_and_click(login, By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]") 
        time.sleep(2)
        while True:
            try:
                print("before in loop")
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
                )

                next_button.click()

            except:
                print("EC caught:")
                break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()
        time.sleep(3)
        scroll_to_window(login)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Create Invoice']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='fa fa-arrow-left']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        invoices = WebDriverWait(login, 15).until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Invoices'])[1]"))
        )
        scroll_to_element(login,invoices)
        time.sleep(2) 
        invoices.click()
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]") 
        time.sleep(2)
        invoice_booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Booking Reference :']/following-sibling::div[contains(@class, 'invoice-detail-style')]"))
        )
        expected_invoice_booking_Id = invoice_booking_Id.text.strip('"')
        print("Expected_BookingId:",expected_invoice_booking_Id)
        print(f"Expected_BookingId: '{expected_invoice_booking_Id}', Actual_BookingId: '{onlineprepayment_appointment_AGOFF}'")
        assert onlineprepayment_appointment_AGOFF == expected_invoice_booking_Id, f"Expected_BookingId: '{expected_invoice_booking_Id}', but got Actual_BookingId: '{onlineprepayment_appointment_AGOFF}'"
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Share PDF']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "The invoice has been sent to the patient"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(3)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e
    

from Framework.common_utils import *
import allure
from allure_commons.types import AttachmentType
import os
first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Manual Invoice for Walkin Appointment")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_walkinappointment_manualinvoice(login):
    try:
        time.sleep(5)
        wait_and_click(login, By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]") 
        time.sleep(2)
        wait_and_click(login, By.XPATH, "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]") 
        time.sleep(3)
        wait_and_click(login, By.XPATH, "//b[contains(text(),'Create New Patient')]") 
        time.sleep(3)
        login.implicitly_wait(3)

        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(5)
        wait_and_click(login, By.CSS_SELECTOR, "p-dropdown[optionlabel='place']") 
        time.sleep(3)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@aria-label='Global Service'])[1]").click()
        print("Department : Globalservice")
        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        service = login.find_element(By.XPATH, service_dropdown_xpath)
        scroll_to_element(login, service)
        service.click()
        service_option_xpath = ("//li[@aria-label='Prepayment Consultation With AG Off']")
        wait_and_click(login, By.XPATH, service_option_xpath) 
        print("Select Service : service")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']") 
        time_slot = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
        time_slot.click()
        print("Time Slot:", time_slot.text)
        note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
        scroll_to_element(login,note_input)
        time.sleep(2)
        note_input.click()
        time.sleep(2)
        login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Save']")
        time.sleep(2)
        login.find_element(By.XPATH,
                        "//span[normalize-space()='Confirm']").click()
        
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        while True:
            try:
                print("before in loop")
                next_button = WebDriverWait(login, 15).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
                )
                next_button.click()
            except:
                print("EC caught:")
                break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()
        time.sleep(3)
        scroll_to_window(login)
        time.sleep(2)
        createinvoice = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create Invoice']"))
        )
        time.sleep(2)
        createinvoice.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='fa fa-arrow-left']") 
        time.sleep(3)
        while True:
            try:
                print("before in loop")
                next_button = WebDriverWait(login, 15).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
                )
                next_button.click()
            except:
                print("EC caught:")
                break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()
        time.sleep(2)
        view_details_button = WebDriverWait(last_element_in_accordian, 15).until(
            EC.presence_of_element_located((By.XPATH, ".//button[normalize-space()='View Details']"))
        )
        view_details_button.click()
        time.sleep(2)
        booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='fw-bold ng-star-inserted'])[1]"))
        )
        actual_booking_id = booking_Id.text.strip('"').strip()
        print("Actual_BookingId:",actual_booking_id)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Invoices'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]") 
        time.sleep(2)
        invoice_booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Booking Reference :']/following-sibling::div[contains(@class, 'invoice-detail-style')]"))
        )
        expected_invoice_booking_Id = invoice_booking_Id.text.strip('"')
        print("Expected_BookingId:",expected_invoice_booking_Id)
        print(f"Expected_BookingId: '{expected_invoice_booking_Id}', Actual_BookingId: '{actual_booking_id}'")
        assert actual_booking_id == expected_invoice_booking_Id, f"Expected_BookingId: '{expected_invoice_booking_Id}', but got Actual_BookingId: '{actual_booking_id}'"
        time.sleep(2)
        scroll_to_window(login)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Share Payment Link']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        expected_message = "The invoice has been sent to the patient"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Settle Invoice']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "Invoice Settled Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(3)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e



