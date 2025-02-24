from Framework.common_utils import *

# @pytest.fixture()
# def login():

    
#     driver = webdriver.Chrome(
#         service=ChromeService(
#             executable_path=r"Drivers\chromedriver-win64\chromedriver.exe"
#         )
#     )
#     driver.get("  ")
#     driver.maximize_window()
#     yield driver
#     driver.quit()  # Ensure the browser is closed properly

@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_online_lead_workflow(login):
    try:

        wait = WebDriverWait(login, 20)
        first_name, last_name, phonenumber, email = create_users_data()

        wait.until(
            EC.presence_of_element_located(
                (By. XPATH, "//input[@placeholder='Enter First Name']"))
        ).send_keys(first_name)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Last Name']"))
        ).send_keys(last_name)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='phone']"))
        ).send_keys(phonenumber)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Email Id']"))
        ).send_keys(email)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter City']"))
        ).send_keys("Trissur")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Notes']"))
        ).send_keys("notes for lead from consumer")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[text()='Submit']"))
        ).click()

        time.sleep(5)
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


        message_element = WebDriverWait(login, 20).until(
                EC.presence_of_element_located((By.XPATH, "//*[text()='Thank you']"))
            )

        # Retrieve the text and print it for verification
        message_text = message_element.text
        print(f"Message found: '{message_text}'")

        # Assert that the text matches "Converted to Appointment"
        assert message_text == "Thank you", "Expected message 'Thank you' not found on the page."

        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
