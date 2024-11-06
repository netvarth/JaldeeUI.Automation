from Framework.common_utils import *
import allure
from allure_commons.types import AttachmentType
import os
first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Auto Invoice for Walkin Appointment")
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
@allure.title("Auto Invoice paybycash for Walkin Appointment")
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
@allure.title("Auto Invoice paybyothers for Walkin Appointment")
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
        scroll_to_window(login)
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