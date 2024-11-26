import time

from Framework.common_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Post deployment signup")
def test_signup():

    current_date = datetime.now().strftime("%d-%m-%Y")
    print("Post-Deployment Signup",current_date)
    try:
        login = webdriver.Chrome(
            service=ChromeService(
                executable_path=r"Drivers\chromedriver-win64\chromedriver.exe"
            )
        )
        login.get("https://www.jaldee.com/business/")
        login.maximize_window()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Sign Up']"))
        ).click()

        time.sleep(3)
        first_name, last_name, cons_manual_id, phonenumber1, email = create_user_data()
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber1)
        login.find_element(By.XPATH, "//input[@id='Firstname']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='Lastname']").send_keys(str(last_name))

        time.sleep(3)
        signup_button = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='signup']"))
        )

        # Scroll into view if needed
        login.execute_script("arguments[0].scrollIntoView(true);", signup_button)

        # Additional wait to ensure the element is not covered by any other element
        time.sleep(1)

        signup_button.click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h6[normalize-space()='Healthcare']")
            )
        ).click()

        next_button = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@class='form-submit']"))
        )

        login.execute_script("arguments[0].scrollIntoView(true);", next_button)

        time.sleep(1)

        next_button.click()

        # login.find_element(By.XPATH,"//h6[normalize-space()='Doctor / Clinic']").click()

        next_button1 = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Next']"))
        )

        login.execute_script("arguments[0].scrollIntoView(true);", next_button1)

        time.sleep(1)

        next_button1.click()

        time.sleep(2)

        next_button2 = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='signup']"))
        )
        login.execute_script("arguments[0].scrollIntoView(true);", next_button2)
        time.sleep(1)
        next_button2.click()

        try:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        except:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter OTP']"))
        ).send_keys("55555")

        confirm_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Confirm OTP']")
            )
        )

        login.execute_script("arguments[0].scrollIntoView(true);", confirm_button)

        time.sleep(1)
        confirm_button.click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='loginId']"))
        ).send_keys(phonenumber1)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='newpassfield']"))
        ).send_keys("Jaldee01")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Re-enter Password']")
            )
        ).send_keys("Jaldee01")

        join_button = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='signup']"))
        )

        join_button.click()

        time.sleep(2)

        welcome_message = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//button[normalize-space()='Take me to assissted account setup']",
                )
            )
        )

        # Get the text of the confirmation message
        actual_message = welcome_message.text
        print("Actual welcome message:", actual_message)

        # Assert the expected text
        expected_message = "Take me to assissted account setup"
        assert (
            actual_message == expected_message
        ), f"Expected '{expected_message}', but got '{actual_message}'"

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@class='underline']"))
        ).click()

        time.sleep(1)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='My Account']")
            )
        ).click()

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='About Us']")
            )
        ).click()

        business_name = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[@aria-owns='bname']"))
        )

        time.sleep(2)
        comp_name = "Business_" + str(uuid.uuid4())[:4]
        business_name.click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='bname']"))
        ).send_keys(comp_name)

        name = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[@aria-owns='busername']"))
        )

        time.sleep(2)
        comp_busername = "Busername_" + str(uuid.uuid4())[:4]
        name.click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='busername']"))
        ).send_keys(comp_busername)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@id='bdesc']"))
        ).send_keys(
            "I'm trying to write a test with selenium in python language for a web page that manages users. In this page someone can add role for users and if a role exists while adding it, an alert raises. I don't know if the alert is a javascript alert or an element of the web page. I want to automatically check the existence of the alert, because checking for the role in the list wastes time and has an enormous load."
        )

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()

        try:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        except:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[normalize-space()='Educational Qualifications']")
            )
        ).click()

        time.sleep(2)
        education = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//mat-label[normalize-space()='Education']")
            )
        )
        education.click()
        education.click()

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='MD']"))
        ).click()

        login.find_element(By.XPATH, "//input[@id='qualifiedFrom']").send_keys(
            "MG University"
        )
        time.sleep(4)
        login.find_element(By.XPATH, "//mat-label[normalize-space()='Month']").click()
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='June']"))
        ).click()

        login.find_element(By.XPATH, "//mat-label[normalize-space()='Year']").click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//span[@class='mdc-list-item__primary-text'][normalize-space()='2006']",
                )
            )
        ).click()

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Gender']"))
        ).click()

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Male']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]"))
        ).click()

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()

        try:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        except:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Location']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Choose your location in the MAP']")
            )
        ).click()

        time.sleep(2)

        try:
            # Locate the input field using XPath
            input_field = login.find_element(By.XPATH, "//input[@id='pac-input']")

            # Input "Thrissur" into the text field
            input_field.send_keys("Thrissur")
            time.sleep(3)

            # Wait for the suggestions to appear and select the appropriate one
            wait = WebDriverWait(login, 10)
            suggestions = wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='pac-item']"))
            )

            time.sleep(3)

            # Iterate through the suggestions and select the one that matches "Thrissur, Kerala, India"
            for suggestion in suggestions:
                if "Thrissur, Kerala, India" in suggestion.text:
                    suggestion.click()
                    break

        finally:
            print("Loaction : Thrissur, Kerala, India")

        time.sleep(2)
        login.find_element(
            By.XPATH, "//button[@type='button']//span[@class='mdc-button__label']"
        ).click()
        time.sleep(2)
        login.find_element(By.XPATH, "//span[@class='mdc-button__label']").click()
        # login.find_element(
        #     By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']"
        # ).click()

        time.sleep(5)
        WebDriverWait(login, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[normalize-space()='Specializations']")
            )
        ).click()

        specializations_list = ["Cardiology", "Ophthalmology", "Neurology"]

        for i in range(len(specializations_list)):
            print(specializations_list[i])
            specializations_xpath = f"//div[@class='specializationouter ng-star-inserted']//label[normalize-space()='{specializations_list[i].title()}']"

            print(specializations_xpath)
            time.sleep(3)
            WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, specializations_xpath))
            ).click()

        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()

        try:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        except:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='edit-txt custId-cursor']")
            )
        ).click()

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='mdc-switch__icons'])[1]")
            )
        ).click()

        time.sleep(6)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='mdc-switch__icons'])[2]")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
            )
        ).click()

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[normalize-space()='Set when you want to accept bookings.']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-button[1]//button[1]//span[1]"))
        ).click()

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='form-group queue-selection']//i[@class='fa fa-square-o ng-star-inserted'][normalize-space()='Select All']",
                )
            )
        ).click()

        HH = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "(//input[@placeholder='HH'])[2]",
                )
            )
        )
        HH.clear()
        HH.send_keys("11")

        MM = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "(//input[@placeholder='MM'])[2]",
                )
            )
        )
        MM.clear()
        MM.send_keys("55")
        
        ampm= WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//ngb-timepicker[@formcontrolname='qendtime']//button[@type='button'][normalize-space()='AM']"))
        ).click()

        time.sleep(2)
        select_btn = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[normalize-space()='Consultation']",
                )
            )
        )

        login.execute_script("arguments[0].click();", select_btn)

        time.sleep(1)
        title = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[normalize-space()='Title for Schedule * (not visible to public)']",
                )
            )
        )
        login.execute_script("arguments[0].click();", title)
        title_input = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='qname']"))
        )
        title_input.send_keys("Test Schedule")

        time_slot = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[normalize-space()='Time Slot Duration (min) *']")
            )
        )
        login.execute_script("arguments[0].click();", time_slot)

        time_slot_input = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@formcontrolname='timeSlot']")
            )
        )
        time_slot_input.send_keys("10")

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()

        try:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        except:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
            )
        ).click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
            )
        ).click()

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//body[1]/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-provider-settings[1]/section[1]/app-old-settings[1]/section[1]/div[1]/div[1]/div[3]/div[1]/div[2]/ul[1]/li[1]/a[1]/p[1]",
                )
            )
        ).click()

        time.sleep(3)

        mdc_switch = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='mdc-switch__ripple']"))
        )

        login.execute_script("arguments[0].click();", mdc_switch)

        # time.sleep(2)
        # login.find_element(
        #     By.XPATH, "//label[normalize-space()='Allow online appointments for today']"
        # ).click()

        # time.sleep(2)
        # login.find_element(
        #     By.XPATH, "//label[normalize-space()='Allow online appointments for future']"
        # ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
            )
        ).click()

        time.sleep(1)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//img[@src='./assets/images/menu/home-color.png']")
            )
        ).click()

        time.sleep(5)
        print("New patient created")
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
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//b[normalize-space()='Create New Patient']")
            )
        )
        element_appoint.click()
        login.implicitly_wait(3)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        # login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(
            By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
        ).send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(5)
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
        wait = WebDriverWait(login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)



        time.sleep(4)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
        ).click()

        try:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        except:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        time.sleep(3)

        home_button = WebDriverWait(login, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@id='kt_quick_user_toggle']//span[contains(@class, 'bname')]")
        ))
        
        login.execute_script("arguments[0].click();", home_button)
        # home_button.click()

        time.sleep(2)

        signout_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[normalize-space()='Sign Out']"))
        )
        login.execute_script("arguments[0].click();", signout_button)
        # signout_button.click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[normalize-space()='Forgot Password ?']"))
        ).click()
    
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='loginId'])[2]"))
        ).send_keys(phonenumber1)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()

        time.sleep(3)
        # otp_digits = "5555"
        otp_digits = "55555"
        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )
        for i, otp_input in enumerate(otp_inputs):
            otp_input.send_keys(otp_digits[i])


        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='newpassfield']"))
        ).send_keys("Jaldee123")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Re-enter Password']"))
        ).send_keys("Jaldee123")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()
        print("Password change successfully")

        time.sleep(5)
    
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e


############################################################################################################################################################

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Post deployment Provider Appointment")
@pytest.mark.parametrize("url", ["https://www.jaldee.com/business/"])
def test_create_patient(login):

    current_date = datetime.now().strftime("%d-%m-%Y")
    print("Post-Deployment Provider Appointment",current_date)
    try:
        time.sleep(5)
        print("New patient created")
        
        
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
        
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//b[normalize-space()='Create New Patient']")
                )
            )
        element_appoint.click()

        login.implicitly_wait(3)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(
            str(first_name)
        )
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(
            str(last_name)
        )
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(
            By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
        ).send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
        
        time.sleep(5)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm']"))
        ).click()
        
        time.sleep(4)
        WebDriverWait(login, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//img[@src='./assets/images/menu/settings.png']"))
        ).click()
        
        
        fea_cust = login.find_element(By.XPATH, "//div[normalize-space()='Features and Customization']")
        login.execute_script("arguments[0].scrollIntoView();", fea_cust)
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Custom Fields']"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Label']"))
        ).click()
        
        label_name1 = "Label" + str(uuid.uuid1())[:3]
        label_namebox1 = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='displayName']"))
        )
        label_namebox1.clear()
        label_namebox1.send_keys(label_name1)
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']"))
        ).click()
        
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/app-sidebar-menu[1]/div[1]/div[2]/div[1]/ul[1]/li[2]/a[1]/div[1]/span[1]/span[1]/img[1]"))
        ).click()
        
        time.sleep(2)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]",
                )
            )
        )
        element.click()
        

        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
        #     )
        # ).send_keys("920720600")
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
            )
        ).send_keys("9207206005")

        time.sleep(3)

        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[contains(text(),'Id : temp#87')]")
        #     )
        # ).click()
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Id : temp#87')]")
            )
        ).click()

        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        element = login.find_element(By.XPATH, service_dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//li[@aria-label='Consultation']//div[contains(text(),'Consultation')]",
                )
            )
        ).click()

        print("Select Service :  Consultation ")

        time.sleep(3)
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

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Notes')]"))
        ).click()

        login.find_element(By.XPATH, "//textarea[@id='message']").send_keys(
            "Note for the walkin appointment"
        )

        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
        ).click()

        print("Note added for walkin appointment")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Upload File']")
            )
        ).click()

        time.sleep(8)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(4)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
        ).click()

        print("Appointment confirm successfully")

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
        View_Detail_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(), 'View Details')]")
            )
        )
        View_Detail_button.click()

    #********************************Apply Label************************************

        # time.sleep(3)
        # more_actions_button = WebDriverWait(login, 10).until(
        #     EC.visibility_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='More Actions']")
        #     )
        # )
        # more_actions_button.click()
        
        # WebDriverWait(login, 10).until(
        #         EC.presence_of_element_located(
        #             (By.XPATH, "//button[normalize-space()='Apply Labels']"))
        # ).click()
            
        # login.implicitly_wait(5)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='Create New']"))
        # ).click()
        
        # label_name = "Label" + str(uuid.uuid1())[:3]
        # label_namebox = WebDriverWait(login, 10).until(
        # EC.presence_of_element_located((By.XPATH, "//input[@id='displayName']"))
        # )
        # label_namebox.clear()
        # label_namebox.send_keys(label_name)
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='Create']"))
        # ).click()
        
        # label_xpath = f"//label[normalize-space()='{label_name}']"

        # # Wait for the label to appear and click on it
        # label = WebDriverWait(login, 10).until(
        # EC.presence_of_element_located((By.XPATH, label_xpath))
        # ).click()
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='Apply']"))
        # ).click()
        
        # Selected_label = WebDriverWait(login, 10).until(
        # EC.presence_of_element_located(
        #         (By.XPATH, label_xpath))
        # )

        # # Get the text of the confirmation message
        # actual_label = Selected_label.text
        # print("Selected Label:", actual_label)

        # # Assert the expected text
        # expected_label = Selected_label.text
        # assert (
        #     actual_label == expected_label
        # ), f"Expected '{expected_label}', but got '{actual_label}'"
        
        # # Applying Filter
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']"))
        # ).click()
        
        # login.implicitly_wait(5)
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//i[@class='pi pi-filter-fill']"))
        # ).click()
        
        # time.sleep(3)
        # Label_filter = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[contains(text(),'Labels')]"))
        # )
        # login.execute_script("arguments[0].scrollIntoView();", Label_filter)
        # Label_filter.click()
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//div[contains(text(),'Select Labels')]"))
        # ).click()

        # time.sleep(3)
        
        #     # Wait for the list to be visible
        # WebDriverWait(login, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, "//ul[@role='listbox']"))
        # )
        
        # # Locate all the list items
        # list_items = WebDriverWait(login, 10).until(
        #     EC.presence_of_all_elements_located((By.XPATH, "//ul[@role='listbox']//li"))
        # )

        # # Get the last item in the list
        # last_item = list_items[-1]

        # # Initialize ActionChains
        # actions = ActionChains(login)

        # # Move to the last item and click it
        # actions.move_to_element(last_item).click().perform()
        
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//timesicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']//*[name()='path' and contains(@d,'M8.01186 7')]"))
        # ).click()
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[contains(text(),'Apply')]"))
        # ).click()
        
        # time.sleep(3)

        # # while True:
        # #     try:
        # #         WebDriverWait(login, 10).until(
        # #             EC.presence_of_element_located(
        # #                 (
        # #                     By.XPATH,
        # #                     "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",   
        # #                 ) 
        # #             )
        # #         ).click()
                

        # #     except:
        # #         break

        # last_element_in_accordian = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (
        #             By.XPATH,
        #             "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
        #         )
        #     )
        # )
        # last_element_in_accordian.click()
        

        # assert (
        #     actual_label == expected_label
        # ), f"Expected '{expected_label}', but got '{actual_label}'"
        
        # time.sleep(2)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//i[@class='pi pi-filter-fill']"))
        # ).click()
        
        # # WebDriverWait(login, 10).until(
        # #     EC.presence_of_element_located(
        # #         (By.XPATH, "//span[normalize-space()='Reset']"))
        # # ).click()

        # reset_button = WebDriverWait(login, 15).until(
        #     EC.presence_of_element_located(
        #     (By.XPATH, "//span[normalize-space()='Reset']"))
        #     )        
        # login.execute_script("arguments[0].click();", reset_button)
        
        # time.sleep(1)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//timesicon[contains(@class, 'p-element') and contains(@class, 'p-icon-wrapper') and contains(@class, 'ng-star-inserted')]//*[contains(@class, 'p-icon')]"))
        # ).click()
        
        # time.sleep(1)
        # login.refresh()

        # time.sleep(2)
        # while True:
        #     try:
        #         WebDriverWait(login, 10).until(
        #             EC.presence_of_element_located(
        #                 (
        #                     By.XPATH,
        #                     "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",   
        #                 ) 
        #             )
        #         ).click()
                

        #     except:
        #         break

        # last_element_in_accordian = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (
        #             By.XPATH,
        #             "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
        #         )
        #     )
        # )
        # last_element_in_accordian.click()

        # time.sleep(3)
        # View_Detail_button = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[contains(text(), 'View Details')]")
        #     )
        # )
        # View_Detail_button.click()
        
        time.sleep(3)
        more_actions_button = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[normalize-space()='More Actions']")
            )
        )
        more_actions_button.click()

        # ****************************** Send Message ****************************

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[normalize-space()='Send Message']")
            )
        ).click()
        time.sleep(3)
        login.find_element(By.XPATH, " //textarea[@id='messageData']").send_keys(
            "Send Message to the Patient"
        )
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[normalize-space()='Click here to select the files']")
            )
        ).click()
        time.sleep(8)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'send')]"))
        ).click()

        print("Send Message Successfully")

        # ******************* Send Attachment ************************

        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[normalize-space()='Send Attachments']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[normalize-space()='Click here to select the files']")
            )
        ).click()

        time.sleep(8)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'send')]"))
        ).click()

        print("Attachment Send Successfully")

        # ********************* Create the Prescription and Sharing *************************

        time.sleep(5)
        WebDriverWait(login, 10)
        login.find_element(By.XPATH, "//span[normalize-space()='Prescriptions']").click()

        for i in range(3):
            login.find_element(
                By.XPATH, "//button[normalize-space()='+ Add Medicine']"
            ).click()
            login.find_element(By.XPATH, "//input[@role='searchbox']").send_keys("Medicine")

            before_XPath = "//*[contains(@id, 'pr_id')]/tbody/tr"
            aftertd_XPath_1 = "/td[2]"
            aftertd_XPath_2 = "/td[3]"
            aftertd_XPath_3 = "/td[4]"
            aftertd_XPath_4 = "/td[5]"
            textarea_xpath = "//input[@role='searchbox']"
            row = i + 1
            if i > 0:
                trXPath = before_XPath + str([row])
            else:
                trXPath = before_XPath

            PreFinalXPath = trXPath + aftertd_XPath_1
            FinalXPath = PreFinalXPath + textarea_xpath

            Dose = login.find_element(By.XPATH, PreFinalXPath)
            Dose.click()
            Dose1 = login.find_element(By.XPATH, FinalXPath)
            Dose1.send_keys("650 mg")

            PreFinalXPath = trXPath + aftertd_XPath_2
            FinalXPath = PreFinalXPath + textarea_xpath

            Frequency = login.find_element(By.XPATH, PreFinalXPath)
            Frequency.click()
            Frequency1 = login.find_element(By.XPATH, FinalXPath)
            Frequency1.send_keys("1-1-1")

            PreFinalXPath = trXPath + aftertd_XPath_3
            FinalXPath = PreFinalXPath + textarea_xpath
            Duration = login.find_element(By.XPATH, PreFinalXPath)
            Duration.click()
            Duration1 = login.find_element(By.XPATH, FinalXPath)
            Duration1.send_keys("5 Days")

            PreFinalXPath = trXPath + aftertd_XPath_4
            FinalXPath = PreFinalXPath + textarea_xpath
            Notes = login.find_element(By.XPATH, PreFinalXPath)
            Notes.click()
            Notes1 = login.find_element(By.XPATH, FinalXPath)
            Notes1.send_keys("After Food")

        # dropdown_locator_xpath = "/html[1]/body[1]/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-provider-appointment-detail[1]/div[1]/div[1]/div[1]/div[1]/app-booking-details[1]/div[2]/app-customer-record[1]/div[1]/div[2]/div[1]/app-prescriptions[1]/div[1]/div[1]/div[2]/div[1]/app-create[1]/div[1]/div[3]/div[1]/span[1]/mat-select[1]"
        # dropdown_element = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, dropdown_locator_xpath)))

        # dropdown_element.click()

        # option_locator_xpath = "//div[normalize-space()='Naveen KP']"
        # option_element = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, option_locator_xpath)))

        # option_element.click()

        login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(8)
        print("prescription created successfully")

        login.find_element(By.XPATH, "//img[@alt='share']").click()
        time.sleep(3)
        login.find_element(
            By.XPATH, "//textarea[@placeholder='Enter message description']"
        ).send_keys("prescription message")

        login.find_element(By.XPATH, "//span[normalize-space()='Email']").click()
        login.find_element(By.XPATH, "//span[normalize-space()='Whatsapp']").click()
        time.sleep(2)
        WebDriverWait(login, 30).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@type='button'][normalize-space()='Share']")
            )
        ).click()
        print("Prescription Shared Successfully")

        # ************************* Case Creation and Sharing *********************

        time.sleep(3)
        Patient_Record_tab = WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Patient Record']")
            )
        )
        login.execute_script("arguments[0].click();", Patient_Record_tab)

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='+ Create Case']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Case Description']")
            )
        ).send_keys("test case for case")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder = 'Enter Chief Complaint']")
            )
        ).send_keys("Fever",Keys.RETURN)

        time.sleep(2)
        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='History']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder = 'Enter History']")
            )
        ).send_keys("Viral fever",Keys.RETURN)
       
        time.sleep(2)
        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Medication']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Medication']")
            )
        ).send_keys(" No medication",Keys.RETURN)
        
        time.sleep(2)
        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Vital Signs']")
            )
        ).click()

        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Pulse Rate , Max : 999']"
        ).send_keys("560")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Respiration , Max : 90']"
        ).send_keys("62")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Temperature , Max : 200']"
        ).send_keys("123")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Systolic , Max : 500']"
        ).send_keys("264")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Diastolic , Max : 500']"
        ).send_keys("287")

        time.sleep(2)
        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Immunization History']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Immunization History']")
            )
        ).send_keys("No History of Immunization History",Keys.RETURN)
        
        time.sleep(2)
        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Treatment Plan']"))
        ).click()
            
        
        treat_name = "Treatment" + str(uuid.uuid4())[:4]
        treat_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@role='searchbox']"))
        )
        treat_namebox.clear()
        treat_namebox.send_keys(treat_name)
        
        
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='p-multiselect-label p-placeholder']"))
        ).click()
        
        
        dropdown_xpath = "//span[normalize-space()='Swaraj K']"
        element = login.find_element(By.XPATH, dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        
        time.sleep(3)
        # WebDriverWait(login, 15).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[@class='btn btn-white shadow fw-bold']"))
        # ).click()
        add_step = WebDriverWait(login, 15).until(
            EC.presence_of_element_located(
            (By.XPATH, "//button[@class='btn btn-white shadow fw-bold']"))
            )        
        login.execute_script("arguments[0].click();", add_step)

        time.sleep(1)
        step_name = "Step" + str(uuid.uuid1())[:1]
        step_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Name']"))
        )
        step_namebox.clear()
        step_namebox.send_keys(step_name)
        
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-multiselect[@optionlabel='firstName']//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted']"))
        ).click()
        
        time.sleep(2)
        element1 = login.find_element(By.XPATH, dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element1)
        element1.click()
        
        time.sleep(3)
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='d-flex']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']")
            )
        ).click()
        
        
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//div[@aria-expanded='false']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']"))
        # ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='In Progress']"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Step Notes']"))
        ).send_keys("Steps for notes")
        
        WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//label[@for='treatmentPlanAattachments']")
        )
        ).click()

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Treatment Notes']"))
        ).send_keys("Note for the treatment")
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Prescription']")
            )
        ).click()

        time.sleep(2)
        for i in range(5):
            login.find_element(
                By.XPATH, "//button[normalize-space()='+ Add Medicine']"
            ).click()
            login.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(
                "Medicine"
            )

            before_XPath = "//*[contains(@id, 'pr_id')]/tbody/tr"
            aftertd_XPath_1 = "/td[2]"
            aftertd_XPath_2 = "/td[3]"
            aftertd_XPath_3 = "/td[4]"
            aftertd_XPath_4 = "/td[5]"
            textarea_xpath = "//input[@role='searchbox']"
            row = i + 1
            if i > 0:
                trXPath = before_XPath + str([row])
            else:
                trXPath = before_XPath

            PreFinalXPath = trXPath + aftertd_XPath_1
            FinalXPath = PreFinalXPath + textarea_xpath

            Dose = login.find_element(By.XPATH, PreFinalXPath)
            Dose.click()
            Dose1 = login.find_element(By.XPATH, FinalXPath)
            Dose1.send_keys("650 mg")

            PreFinalXPath = trXPath + aftertd_XPath_2
            FinalXPath = PreFinalXPath + textarea_xpath

            Frequency = login.find_element(By.XPATH, PreFinalXPath)
            Frequency.click()
            Frequency1 = login.find_element(By.XPATH, FinalXPath)
            Frequency1.send_keys("1-1-1")

            PreFinalXPath = trXPath + aftertd_XPath_3
            FinalXPath = PreFinalXPath + textarea_xpath
            Duration = login.find_element(By.XPATH, PreFinalXPath)
            Duration.click()
            Duration1 = login.find_element(By.XPATH, FinalXPath)
            Duration1.send_keys("5 Days")

            PreFinalXPath = trXPath + aftertd_XPath_4
            FinalXPath = PreFinalXPath + textarea_xpath
            Notes = login.find_element(By.XPATH, PreFinalXPath)
            Notes.click()
            Notes1 = login.find_element(By.XPATH, FinalXPath)
            Notes1.send_keys("After Food")
        time.sleep(2)
        login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        time.sleep(2)
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Observations']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Observations']")
            )
        ).send_keys("Minor fever",Keys.RETURN)
        
        time.sleep(2)
        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Diagnosis']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Diagnosis']")
            )
        ).send_keys("High temperature",Keys.RETURN)
        
        time.sleep(2)
        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()


        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[@class='add-action-btn']"))
        ).click()
        
        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")


        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Share')]"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter message description']")
            )
        ).send_keys("case sharing testing")

        login.find_element(By.XPATH, "//span[contains(text(),'Email')]").click()
        login.find_element(By.XPATH, "//span[contains(text(),'Whatsapp')]").click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Share')]"))
        ).click()

        print("Case file Shared successfully")

        
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//i[@class='pi pi-arrow-left back-btn-arrow']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
            )
        ).click()

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

        # ************************* Auto Invoice and Sharing ************************

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='View Invoice']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
        ).click()

        time.sleep(3)
        print("Auto Invoice")
        print("Successfully send the Payment Link to the patient")
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Edit']"))
        ).click()
        
        time.sleep(2)
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        ).click()
        
        time.sleep(2)    
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='SubConsultation']"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        print("Added Sub Service to the Invoice")
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        ).click()
        
        item_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Choose Procedure/Item']"))
        )
        item_button.click()
        item_button.send_keys("item1234")
        
        time.sleep(3)
        price = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='mat-input-4'])[2]"))
        )
        price.clear()
        price.click()
        price.send_keys("1")
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        print("Added ADHOC item to the Invoice")
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Update']"))
        ).click()
        
        
        
        try:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        except:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)
        
        time.sleep(3)
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Send']")
            )
        ).click()
        
        try:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        except:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)
        
        
        time.sleep(3)
        login.find_element(By.XPATH, "//i[@class='fa fa-arrow-left']").click()


        time.sleep(3)
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

        # ********************** Manual Invoice and Sharing ***********************

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='New Invoice']")
            )
        ).click()

        add_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']")
            )
        )
        login.execute_script("arguments[0].scrollIntoView();", add_button)
        login.execute_script("arguments[0].click();", add_button)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Choose Procedure/Item']")
            )
        ).click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='item-name'][normalize-space()='Consultation']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add']"))
        ).click()

        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
        ).click()

        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
        ).click()

        time.sleep(5)
        print("Manual Invoice")
        print("Successfully send the Payment Link to the patient")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Edit']"))
        ).click()
        
        time.sleep(2)
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        ).click()
        
        time.sleep(2)    
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='SubConsultation']"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        print("Added Sub Service to the Invoice")
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        ).click()
        
        item_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Choose Procedure/Item']"))
        )
        item_button.click()
        item_button.send_keys("item1234")
        
        time.sleep(3)
        price = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='mat-input-4'])[2]"))
        )
        price.clear()
        price.click()
        price.send_keys("1")
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        print("Added ADHOC item to the Invoice")
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Update']"))
        ).click()
        
        
        
        try:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        except:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)
            
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Send']")
            )
        ).click()
        
        try:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        except:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)
        

        time.sleep(3)

        login.find_element(By.XPATH, "//i[@class='fa fa-arrow-left']").click()

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
        View_Detail_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(), 'View Details')]")
            )
        )
        View_Detail_button.click()

        # *************************** Reschedule **********************

        time.sleep(3)
        login.find_element(By.XPATH, "//button[contains(text(),'Reschedule')]").click()
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='reschedule-date-picker']")
            )
        ).click()

        today_date = datetime.now()
        print(today_date.day)
        today_xpath_expression = "//span[@class='example-custom-date-class d-pad-15 ng-star-inserted'][normalize-space()='{}']".format(
            today_date.day
        )
        print(today_xpath_expression)
        tomorrow_date = today_date + timedelta(days=1)
        print(tomorrow_date.day)
        today_date = datetime.now()
        print(today_date.day)
        today_xpath_expression = "//span[@class='example-custom-date-class d-pad-15 ng-star-inserted'][normalize-space()='{}']".format(
            today_date.day
        )
        print(today_xpath_expression)
        tomorrow_date = today_date + timedelta(days=1)
        print(tomorrow_date.day)
#======================================================
        # current_month = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[contains(@class, 'p-datepicker-month')]"))
        # )

        # current_year = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[contains(@class, 'p-datepicker-year')]"))
        # )

        # if current_month.text.lower() != tomorrow_date.strftime("%b").lower() or current_year.text.lower() != tomorrow_date.strftime("%Y").lower():

        #     login.find_element(By.XPATH, "//button[contains(@class, 'p-datepicker-next')]").click()
#====================================================================
        tomorrow_xpath_expression = "//span[@class='example-custom-date-class d-pad-15 ng-star-inserted'][normalize-space()='{}']".format(
            tomorrow_date.day
        )
        print(tomorrow_xpath_expression)

        Tomorrow_Date = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, tomorrow_xpath_expression))
        )
        time.sleep(3)
        Tomorrow_Date.click()
        print("Tomorrow Date:", Tomorrow_Date.text)

        wait = WebDriverWait(login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected= 'false']"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)

        reschedule_button = WebDriverWait(login, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='btn btn-primary reschedule-btn']")
            )
        )
        reschedule_button.click()
        print("Reschedule Successfully")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Today')]"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Future']"))
        ).click()

        time.sleep(5)

        # while True:
        #     try:

        #         next_button = WebDriverWait(login, 10).until(
        #             EC.presence_of_element_located(
        #                 (
        #                     By.XPATH,
        #                     "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
        #                 )
        #             )
        #         )

        #         next_button.click()

        #     except:
        #         # print("EC caught:")
        #         break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
                )
            )
        )
        last_element_in_accordian.click()

        # *******************Cancellation **********************

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Change Status']")
            )
        ).click()
    
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Cancel')]"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'No Show Up')]")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()
        time.sleep(5)
        print("Successfully Cancel Appointment")

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e