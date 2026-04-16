from Framework.consumer_common_utils import *


@pytest.mark.parametrize("url", [consumer_login_url_1])
def test_signup_myaccount(consumer_login):
    try:
        consumer_data = create_consumer_data()
        time.sleep(5)
        wait_and_locate_click(consumer_login, By.XPATH, "//a[normalize-space()='My Bookings']")
        time.sleep(2)
        first_name, last_name, phonenumber, email = consumer_data
        wait_and_send_keys(consumer_login, By.XPATH, "//input[@placeholder='81234 56789']", phonenumber)
        print("New Consumer Phone Number:", phonenumber)
        consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        time.sleep(5)
        otp_digits = "55555"
        # otp_digits = "55555"
        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )

        # print("Number of OTP input fields:", len(otp_inputs))
        # print(otp_inputs)

        for i, otp_input in enumerate(otp_inputs):

            # print(i)
            # print(otp_input)
            otp_input.send_keys(otp_digits[i])

        consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        wait_and_send_keys(consumer_login, By.XPATH, "(//input[@id='first_name'])[1]", first_name)
        print("New Consumer Firstname:", first_name)
        wait_and_send_keys(consumer_login, By.XPATH, "(//input[@id='first_name'])[2]", last_name)
        print("New Consumer Lastname:", last_name)
        consumer_login.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        
        time.sleep(5)
        wait_and_locate_click(consumer_login, By.XPATH, "//button[@id='btnUser']")
        wait_and_locate_click(consumer_login, By.XPATH, "//button[@id='btnUserProfile']")
        wait_and_locate_click(consumer_login, By.XPATH, "//mat-select[@id='titles']")
        
        time.sleep(3)

        salutation = generate_random_salutation()
        salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        wait_and_locate_click(consumer_login, By.XPATH, salutation_option_xpath, 15)
        time.sleep(3)

        email_input = WebDriverWait(consumer_login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='email']")) 
        )
        email_input.send_keys(email)

        time.sleep(3)
        confirmation_email_input = WebDriverWait(consumer_login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='email1']")) 
        )
        confirmation_email_input.send_keys(email)
        print(email_input.text)
        time.sleep(3)
        scroll_to_window(consumer_login)
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//button[@type='button']")
        time.sleep(2)
        consumer_login.find_element(By.XPATH, "//button[normalize-space()='2026']").click()
        time.sleep(2)
        backward_arrow = consumer_login.find_element(By.XPATH,
                                            "//button[contains(@class, 'p-ripple') and contains(@class, 'p-element') and contains(@class, 'p-datepicker-prev') and contains(@class, 'p-link') and contains(@class, 'ng-star-inserted')]")
        for i in range(4):
            backward_arrow.click()
        time.sleep(2)
        [year, month, day] = Generate_dob()
        print(year, month, day)
        year_xpath = f"//span[normalize-space()='{year}']"
        print(year_xpath)
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, year_xpath)
        time.sleep(2)
        month_xpath = f"//span[normalize-space()='{month}']"
        print(month_xpath)
        wait_and_locate_click(consumer_login, By.XPATH, month_xpath)
        time.sleep(2)
        day_formatted = str(day).lstrip("0")  # Remove leading zero for comparison
        day_xpath = f"//span[normalize-space()='{day_formatted}' or normalize-space()='{day}']"
        print(day_xpath)
        wait_and_locate_click(consumer_login, By.XPATH, day_xpath)
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//input[@placeholder='DD/MM/YYYY']")
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//div[@aria-label='dropdown trigger']")
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "//li[@aria-label='female']")
        time.sleep(2)
        
        wait_and_locate_click(consumer_login, By.XPATH, "//button[@id='btnUpdate']")
        msg = get_snack_bar_message(consumer_login)
        print("Snack bar message:", msg)

        time.sleep(3)
        delete_element = consumer_login.find_element(By.XPATH, "//span[@class='deleteac']")
        consumer_login.execute_script("arguments[0].click();", delete_element)
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//button[@id='btnYes']")
        time.sleep(2)
        
    except Exception as e:
        allure.attach(  
            consumer_login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        )
        raise e 


@pytest.mark.parametrize("url", [consumer_login_url_1])    
def test_signup_myaccount_familymember(consumer_login):
    
    try:

        time.sleep(5)

        Consumer_data = create_consumer_data("consumer")
        Family = create_consumer_data("family")


        first_name, last_name, phonenumber, email = Consumer_data
        wait_and_locate_click(consumer_login, By.XPATH, "//a[normalize-space()='My Bookings']")
        time.sleep(2)
        wait_and_send_keys(consumer_login, By.XPATH, "//input[@placeholder='81234 56789']", phonenumber)
        print("New Consumer Phone Number:", phonenumber)
        consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        time.sleep(5)
        otp_digits = "55555"
        # otp_digits = "55555"
        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )

        # print("Number of OTP input fields:", len(otp_inputs))
        # print(otp_inputs)

        for i, otp_input in enumerate(otp_inputs):

            # print(i)
            # print(otp_input)
            otp_input.send_keys(otp_digits[i])

        consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        
        time.sleep(3)
        wait_and_send_keys(consumer_login, By.XPATH, "(//input[@id='first_name'])[1]", first_name)
        print("New Consumer Firstname:", first_name)
        wait_and_send_keys(consumer_login, By.XPATH, "(//input[@id='first_name'])[2]", last_name)
        print("New Consumer Lastname:", last_name)
        consumer_login.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        time.sleep(5)
        wait_and_locate_click(consumer_login, By.XPATH, "//button[@id='btnUser']")
        wait_and_locate_click(consumer_login, By.XPATH, "//button[@id='btnUserProfile']")
        time.sleep(3)
        
        first_name, last_name, phonenumber, email = Family
        wait_and_locate_click(consumer_login, By.XPATH, "//span[normalize-space()='Family Members']")
        time.sleep(3)

        wait_and_locate_click(consumer_login, By.XPATH, "//span[@class='btnTextCust']")
        time.sleep(3)

        
        selectbtn = consumer_login.find_element(By.XPATH, "//span[@aria-label='Select']")
        consumer_login.execute_script("arguments[0].click();", selectbtn)   
      
        # time.sleep(2)
        # salutation = generate_random_salutation()
        # salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        # wait_and_locate_click(consumer_login, By.XPATH, salutation_option_xpath, 15)

        time.sleep(5)
        wait_and_send_keys(consumer_login, By.XPATH, "//input[@id='first_name']", first_name)
        print("Familymemeber Firstname:", first_name)

        wait_and_send_keys(consumer_login, By.XPATH, "//input[@id='last_name']", last_name)
        print("Familymemeber Lastname:", last_name)

        time.sleep(5)
        
        wait_and_send_keys(consumer_login, By.XPATH, "//input[@placeholder='81234 56789']", phonenumber)
        print("Family member Phone Number:", phonenumber)
        time.sleep(2)

        email_input = WebDriverWait(consumer_login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='email']")) 
        )
        email_input.send_keys(email)
        time.sleep(2)
        print("Family member Email:", email)
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "//button[@id='btnSave']")
        # msg = get_snack_bar_message(consumer_login)
        # print("Snack bar message:", msg)
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//i[@class='fa fa-arrow-left clrChangeHeader']")
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "//span[@class='deleteac']")
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "//button[@id='btnYes']")
        time.sleep(2)
        
    except Exception as e:
        allure.attach(  
            consumer_login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        )
        raise e 
