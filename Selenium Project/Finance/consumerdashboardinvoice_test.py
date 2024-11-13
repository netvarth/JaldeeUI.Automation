
from Framework.consumer_common_utils import *


@pytest.fixture()
def onlinetokeninvoiceid(consumer_login):
    try:
        time.sleep(5)
        consumer_data = create_consumer_data()

        book_now_button = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Book Now']")
            )
        )
        consumer_login.execute_script("arguments[0].scrollIntoView();", book_now_button)

        clickable_book_now_button = WebDriverWait(consumer_login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Book Now']"))
        )
        try:
            clickable_book_now_button.click()
        except:
            consumer_login.execute_script("arguments[0].click();", clickable_book_now_button)
        time.sleep(2)
        location_button = WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located((By.XPATH,"//div[@class='deptName ng-star-inserted'][contains(text(),'Chavakkad')]",))
        )
        location_button.click()
        selectdepart = WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located((By.XPATH,"//div[@class='deptName ng-star-inserted'][normalize-space()='Global Service']",)))
        selectdepart.click()
        service_card = WebDriverWait(consumer_login, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='service-container']")))
        consumer_login.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", service_card)
        prepayment_checkin =WebDriverWait(consumer_login, 10).until(EC.presence_of_element_located((By.XPATH,"//app-checkin-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][contains(text(),'Prepayment Consultation')]",)))
        prepayment_checkin.click()
        time.sleep(3)
        consumer_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        Today_Date = WebDriverWait(consumer_login, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-pressed='true']")))
        Today_Date.click()
        print("Today Date:", Today_Date.text)
        queue = WebDriverWait(consumer_login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='mdc-evolution-chip__cell mdc-evolution-chip__cell--primary']")))
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", queue)
        time.sleep(2)
        queue.click()
        print("Queue:", queue.text)
        time.sleep(2)
        next_button = WebDriverWait(consumer_login, 10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Next']")))
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", next_button)
        time.sleep(3)
        next_button.click()
        time.sleep(3)
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
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='email_id']")
            )
        ).send_keys(consumer_data['email'])
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Ok']"))
        ).click()
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'NET BANKING')]"))
        ).click()

        time.sleep(3)
        makepayment = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH,"//button[@type='button']//span[@class='mat-mdc-button-touch-target']") )
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", makepayment)
        consumer_login.execute_script("arguments[0].click();", makepayment)
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(@class,'ptm-paymode-name ptm-lightbold')]"))
        ).click()

        time.sleep(1)

        WebDriverWait(consumer_login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'SBI')]"))
        ).click()

        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'ptm-emi-overlay')]//div[contains(@class,'')]//div[@id='checkout-button']//button[contains(@class,'ptm-nav-selectable')][contains(text(),'Pay ₹100')]",))
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
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btnd']"))
        ).click()

        # Optionally, switch back to the main window

        consumer_login.switch_to.window(main_window_handle)
        message = get_snack_bar_message(consumer_login)
        print("Snack bar message:", message)
        time.sleep(2)
        Ok_button = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", Ok_button)
        time.sleep(2)
        Ok_button.click()
        time.sleep(2)
        print("New Consumer token booking confirmed successfully")
        time.sleep(2)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='My Bookings']"))
        ).click()
        time.sleep(2)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@class='amountDueBtn'][normalize-space()='Invoice'])[1]"))
        ).click()
        time.sleep(2)
        tokeninvoiceid = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='ng-star-inserted'])[2]"))
        ).text
        onlinetokeninvoiceid = tokeninvoiceid.split('#')[1].strip()
        print("Online Token Invoice Id:", onlinetokeninvoiceid)
        Net_banking = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-radio'])[4]"))
        )
        scroll_to_element(consumer_login, Net_banking)
        time.sleep(2)
        Net_banking.click()
        time.sleep(2)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='MaKe Payment']"))
        ).click()
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[@class='ptm-paymode-name ptm-lightbold ']"))
        ).click()
        time.sleep(2)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='SBI']"))
        ).click()
        time.sleep(1)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'ptm-overlay-wrapper btn-enabled')]//button[contains(@class,'')][contains(text(),'Pay ₹350')]"))
        ).click()
        time.sleep(2)
        main_window_handle = consumer_login.current_window_handle
        WebDriverWait(consumer_login, 10).until(EC.new_window_is_opened)
        all_window_handles = consumer_login.window_handles
        new_window_handle = None
        for handle in all_window_handles:
            if handle != main_window_handle:
                new_window_handle = handle
                break
        consumer_login.switch_to.window(new_window_handle)
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btnd']"))
        ).click()
        time.sleep(2)
        consumer_login.switch_to.window(main_window_handle)
        message = get_snack_bar_message(consumer_login)
        print("Snack bar message:", message)
        time.sleep(2)
        return onlinetokeninvoiceid
    finally:
        consumer_login.quit()



from Framework.consumer_common_utils import *


@pytest.fixture()
def onlineappointmentinvoiceid(consumer_login):
    try:
        time.sleep(5)
        consumer_data = create_consumer_data()

        book_now_button = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Book Now']")
            )
        )
        consumer_login.execute_script("arguments[0].scrollIntoView();", book_now_button)

        clickable_book_now_button = WebDriverWait(consumer_login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Book Now']"))
        )
        try:
            clickable_book_now_button.click()
        except:
            consumer_login.execute_script("arguments[0].click();", clickable_book_now_button)
        time.sleep(2)
        location_button = WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located((By.XPATH,"//div[@class='deptName ng-star-inserted'][contains(text(),'Chavakkad')]",))
        )
        location_button.click()
        selectdepart = WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located((By.XPATH,"//div[@class='deptName ng-star-inserted'][normalize-space()='Global Service']",)))
        selectdepart.click()
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
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='email_id']")
            )
        ).send_keys(consumer_data['email'])
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Ok']"))
        ).click()
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'NET BANKING')]"))
        ).click()

        time.sleep(3)
        makepayment = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH,"//button[@type='button']//span[@class='mat-mdc-button-touch-target']") )
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", makepayment)
        consumer_login.execute_script("arguments[0].click();", makepayment)
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(@class,'ptm-paymode-name ptm-lightbold')]"))
        ).click()

        time.sleep(1)

        WebDriverWait(consumer_login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'SBI')]"))
        ).click()

        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'ptm-emi-overlay')]//div[contains(@class,'')]//div[@id='checkout-button']//button[contains(@class,'ptm-nav-selectable')][contains(text(),'Pay ₹100')]",))
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
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btnd']"))
        ).click()

        # Optionally, switch back to the main window

        consumer_login.switch_to.window(main_window_handle)
        message = get_snack_bar_message(consumer_login)
        print("Snack bar message:", message)
        time.sleep(2)
        Ok_button = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", Ok_button)
        time.sleep(2)
        Ok_button.click()
        time.sleep(2)
        print("New Consumer token booking confirmed successfully")
        time.sleep(2)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='My Bookings']"))
        ).click()
        time.sleep(2)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@class='amountDueBtn'][normalize-space()='Invoice'])[1]"))
        ).click()
        time.sleep(2)
        appointmentinvoiceid = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='ng-star-inserted'])[2]"))
        ).text
        onlineappointmentinvoiceid = appointmentinvoiceid.split('#')[1].strip()
        print("Online Appointment Invoice Id:", onlineappointmentinvoiceid)
        Net_banking = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-radio'])[4]"))
        )
        scroll_to_element(consumer_login, Net_banking)
        time.sleep(2)
        Net_banking.click()
        time.sleep(2)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='MaKe Payment']"))
        ).click()
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[@class='ptm-paymode-name ptm-lightbold ']"))
        ).click()
        time.sleep(2)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='SBI']"))
        ).click()
        time.sleep(1)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'ptm-overlay-wrapper btn-enabled')]//button[contains(@class,'')][contains(text(),'Pay ₹350')]"))
        ).click()
        time.sleep(2)
        main_window_handle = consumer_login.current_window_handle
        WebDriverWait(consumer_login, 10).until(EC.new_window_is_opened)
        all_window_handles = consumer_login.window_handles
        new_window_handle = None
        for handle in all_window_handles:
            if handle != main_window_handle:
                new_window_handle = handle
                break
        consumer_login.switch_to.window(new_window_handle)
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btnd']"))
        ).click()
        time.sleep(2)
        consumer_login.switch_to.window(main_window_handle)
        message = get_snack_bar_message(consumer_login)
        print("Snack bar message:", message)
        time.sleep(2)
        return onlineappointmentinvoiceid

    finally:
        consumer_login.quit() 


from Framework.common_utils import *
import allure
from allure_commons.types import AttachmentType

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Consumer Appointment Invoice Id and Assign User on Finance Invoices")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_consumer_appointment_invoiceId(onlineappointmentinvoiceid, login):
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
        time.sleep(2)
        invoice_booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[1]"))
        ).text
    
        print("Expected_Appointment_BookingId:",invoice_booking_Id)
        print(f"Expected_Appointment_BookingId: '{invoice_booking_Id}', Actual_Appointment_BookingId: '{onlineappointmentinvoiceid}'")
        assert onlineappointmentinvoiceid == invoice_booking_Id, f"Expected_Appointment_BookingId: '{invoice_booking_Id}', but got Actual_Appointment_BookingId: '{onlineappointmentinvoiceid}'"
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//tbody/tr[1]/td[10]/div[1]/button[2]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Assign User']") 
        time.sleep(3)
        wait_and_click(login, By.XPATH, "//span[@class='mdc-button__label']") 
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(2)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Consumer Token Invoice Id and Assign User on Finance Invoices")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_consumer_token_invoiceId(onlinetokeninvoiceid, login):
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
        time.sleep(2)
        invoice_booking_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[1]"))
        ).text
    
        print("Expected_Appointment_BookingId:",invoice_booking_Id)
        print(f"Expected_Appointment_BookingId: '{invoice_booking_Id}', Actual_Appointment_BookingId: '{onlinetokeninvoiceid}'")
        assert onlinetokeninvoiceid == invoice_booking_Id, f"Expected_Appointment_BookingId: '{invoice_booking_Id}', but got Actual_Appointment_BookingId: '{onlinetokeninvoiceid}'"
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//tbody/tr[1]/td[10]/div[1]/button[2]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Assign User']") 
        time.sleep(3)
        wait_and_click(login, By.XPATH, "//span[@class='mdc-button__label']") 
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(2)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e