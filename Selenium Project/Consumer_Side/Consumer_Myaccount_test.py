from Framework.consumer_common_utils import *

def test_signup_myaccount(consumer_login):
    try:
        consumer_data = create_consumer_data()
        time.sleep(5)
        wait_and_locate_click(consumer_login, By.XPATH, "//a[normalize-space()='My Bookings']")
        time.sleep(2)
        wait_and_send_keys(consumer_login, By.XPATH, "//input[@id='phone']", consumer_data['phonenumber'])
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
        wait_and_send_keys(consumer_login, By.XPATH, "(//input[@id='first_name'])[1]", consumer_data['first_name'])
        print("New Consumer Firstname:", consumer_data['first_name'])
        wait_and_send_keys(consumer_login, By.XPATH, "(//input[@id='first_name'])[2]", consumer_data['last_name'])
        print("New Consumer Lastname:", consumer_data['last_name'])
        consumer_login.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        time.sleep(5)
        wait_and_locate_click(consumer_login, By.XPATH, "//span[@class='lgin cust ng-star-inserted']//span[@class='mat-mdc-button-touch-target']")
        wait_and_locate_click(consumer_login, By.XPATH, "//span[contains(text(),'My Account')]")
        wait_and_locate_click(consumer_login, By.XPATH, "//mat-select[@id='titles']")
        time.sleep(3)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        wait_and_locate_click(consumer_login, By.XPATH, salutation_option_xpath, 15)
        time.sleep(3)
        email = consumer_data['email']
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
        consumer_login.find_element(By.XPATH, "//button[normalize-space()='2024']").click()
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
        # consumer_login.execute_script("window.scrollTo(0, 0);")
        # time.sleep(2)
        # current_working_directory = os.getcwd()
        # absolute_path = os.path.abspath(
        #     os.path.join(current_working_directory, r"Extras\test.png")
        # )
        # pyautogui.write(absolute_path)
        # pyautogui.press("enter")
        # time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//span[@class='updateBtnText ng-star-inserted']")
        message = get_snack_bar_message(consumer_login)
        print("Snack bar message:", message)
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//span[@class='deleteac']")
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(2)
        
    except Exception as e:
        allure.attach(  
            consumer_login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        )
        raise e 
    
def test_signup_myaccount_familymember(consumer_login):
    try:
        consumer_data = create_consumer_data()
        time.sleep(5)
        wait_and_locate_click(consumer_login, By.XPATH, "//a[normalize-space()='My Bookings']")
        time.sleep(2)
        wait_and_send_keys(consumer_login, By.XPATH, "//input[@id='phone']", consumer_data['phonenumber'])
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
        wait_and_send_keys(consumer_login, By.XPATH, "(//input[@id='first_name'])[1]", consumer_data['first_name'])
        print("New Consumer Firstname:", consumer_data['first_name'])
        wait_and_send_keys(consumer_login, By.XPATH, "(//input[@id='first_name'])[2]", consumer_data['last_name'])
        print("New Consumer Lastname:", consumer_data['last_name'])
        consumer_login.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        time.sleep(5)
        wait_and_locate_click(consumer_login, By.XPATH, "//span[@class='lgin cust ng-star-inserted']//span[@class='mat-mdc-button-touch-target']")
        wait_and_locate_click(consumer_login, By.XPATH, "//span[contains(text(),'My Account')]")
        time.sleep(3)
        consumer_data = create_consumer_data()
        wait_and_locate_click(consumer_login, By.XPATH, "//span[normalize-space()='Family Members']")
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//span[@class='btnTextCust']")
        time.sleep(3)
        selectbtn = WebDriverWait(consumer_login, 10).until(
            EC.element_to_be_clickable(
            (By.XPATH,"(//div[@class='salutation'])[2]"))
        )
        selectbtn.click()
        time.sleep(2)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//li[@aria-label ='{salutation}']"
        wait_and_locate_click(consumer_login, By.XPATH, salutation_option_xpath, 15)
        time.sleep(5)
        wait_and_send_keys(consumer_login, By.XPATH, "(//input[@id='first_name'])[2]", consumer_data['first_name'])
        print("Familymemeber Firstname:", consumer_data['first_name'])
        wait_and_send_keys(consumer_login, By.XPATH, "(//input[@id='last_name'])[2]", consumer_data['last_name'])
        print("Familymemeber Lastname:", consumer_data['last_name'])
        time.sleep(5)
        # wait_and_locate_click(consumer_login, By.XPATH, "//input[@placeholder='DD/MM/YYYY']")
        # time.sleep(3)
        # consumer_login.find_element(By.XPATH, "//button[normalize-space()='2024']").click()
        # time.sleep(2)
        # backward_arrow = consumer_login.find_element(By.XPATH,
        #                                     "//button[contains(@class, 'p-ripple') and contains(@class, 'p-element') and contains(@class, 'p-datepicker-prev') and contains(@class, 'p-link') and contains(@class, 'ng-star-inserted')]")
        # for i in range(4):
        #     backward_arrow.click()
        # time.sleep(2)
        # [year, month, day] = Generate_dob()
        # print(year, month, day)
        # year_xpath = f"//span[normalize-space()='{year}']"
        # print(year_xpath)
        # time.sleep(2)
        # wait_and_locate_click(consumer_login, By.XPATH, year_xpath)
        # time.sleep(2)
        # month_xpath = f"//span[normalize-space()='{month}']"
        # print(month_xpath)
        # wait_and_locate_click(consumer_login, By.XPATH, month_xpath)
        # time.sleep(2)
        # day_formatted = str(day).lstrip("0")  # Remove leading zero for comparison
        # day_xpath = f"//span[normalize-space()='{day_formatted}' or normalize-space()='{day}']"
        # print(day_xpath)
        # wait_and_locate_click(consumer_login, By.XPATH, day_xpath)
        # time.sleep(3)
        # wait_and_locate_click(consumer_login, By.XPATH, "//input[@placeholder='DD/MM/YYYY']")
        # time.sleep(3)
        # wait_and_locate_click(consumer_login, By.XPATH, "//span[@aria-label='Gender']")
        # time.sleep(2)
        # wait_and_locate_click(consumer_login, By.XPATH, "//li[@aria-label='female']")
        # time.sleep(2)
        wait_and_send_keys(consumer_login, By.XPATH, "(//input[@id='phone'])[1]", consumer_data['phonenumber'])
        print("Family member Phone Number:", consumer_data['phonenumber'])
        time.sleep(2)
        email = consumer_data['email']
        email_input = WebDriverWait(consumer_login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='email']")) 
        )
        email_input.send_keys(email)
        time.sleep(2)
        print("Family member Email:", consumer_data['email'])
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Save'])[2]")
        message = get_snack_bar_message(consumer_login)
        print("Snack bar message:", message)
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//i[@class='fa fa-window-close hoverCross']")
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "//div[@class='btnClrTextRemove ng-star-inserted']")
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "//button[normalize-space()='Confirm']")
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            consumer_login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        )
        raise e 

