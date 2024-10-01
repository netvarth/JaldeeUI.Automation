from Framework.consumer_common_utils import *

def test_signup_appointment_booking(login):
    try:
        consumer_data = create_consumer_data()
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//a[normalize-space()='My Bookings']")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@id='phone']", consumer_data['phonenumber'])
        print("New Consumer Phone Number:", consumer_data['phonenumber'])
        login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        time.sleep(5)
        otp_inputs = WebDriverWait(login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )
        for i, otp_input in enumerate(otp_inputs):
            otp_input.send_keys(consumer_data['otp'][i])
        login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        wait_and_send_keys(login, By.XPATH, "(//input[@id='first_name'])[1]", consumer_data['first_name'])
        print("New Consumer Firstname:", consumer_data['first_name'])
        wait_and_send_keys(login, By.XPATH, "(//input[@id='first_name'])[2]", consumer_data['last_name'])
        print("New Consumer Lastname:", consumer_data['last_name'])
        login.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//span[@class='lgin cust ng-star-inserted']//span[@class='mat-mdc-button-touch-target']")
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'My Account')]")
        wait_and_locate_click(login, By.XPATH, "//mat-select[@id='titles']")
        time.sleep(3)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        wait_and_locate_click(login, By.XPATH, salutation_option_xpath, 15)
        time.sleep(3)
        email = consumer_data['email']
        email_input = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='email']")) 
        )
        email_input.send_keys(email)
        time.sleep(3)
        confirmation_email_input = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='email1']")) 
        )
        confirmation_email_input.send_keys(email)
        time.sleep(3)
        scroll_to_window(login)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[@class='updateBtnText ng-star-inserted']")
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
