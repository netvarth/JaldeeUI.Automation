import time
import random
import allure
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
import allure
from allure_commons.types import AttachmentType
from faker import Faker


test_mail = ".test@jaldee.com"


@pytest.fixture()
def login():
    driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://scale.jaldee.com/visionhospital/")
    driver.maximize_window()
    yield driver
    driver.quit()


def create_users_data():
    fake = Faker()
    first_name = fake.first_name()
    print(first_name)
    last_name = fake.last_name()
    print(last_name)
    random_digits = fake.numerify(text="#######")
    phonenumber = f"{555}{random_digits}"
    print(phonenumber)
    email = f"{first_name}.{last_name}{test_mail}"
    return [first_name, last_name, phonenumber, email]


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("valid user and valid password")
def test_validnumber_validpassword(login):

    try:
        time.sleep(2)
        login.find_element(By.XPATH, "//a[normalize-space()='My Bookings']").click()

        first_name, last_name, phonenumber = create_users_data()

        user = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        )
        user.send_keys(phonenumber)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='continue ng-star-inserted']")
            )
        ).click()

        time.sleep(2)

        otp_digits = "55555"

        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )

        for i, otp_input in enumerate(otp_inputs):

            # print(i)
            # print(otp_input)
            otp_input.send_keys(otp_digits[i])

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='continue ng-star-inserted']")
            )
        ).click()

        time.sleep(2)

        login.find_element(By.XPATH, "(//input[@id='first_name'])[1]").send_keys(
            str(first_name)
        )
        login.find_element(By.XPATH, "(//input[@id='first_name'])[2]").send_keys(
            str(last_name)
        )
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Next']")
            )
        ).click()

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

#########################################################################################################################

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("consumer userid and  invalid password")
def test_userid_invalid_password(login):
    try:
        time.sleep(2)
        login.find_element(By.XPATH, "//a[normalize-space()='My Bookings']").click()

        first_name, last_name, phonenumber = create_users_data()

        user = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        )
        user.send_keys(phonenumber)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='continue ng-star-inserted']")
            )
        ).click()

        time.sleep(2)

        otp_digits = "55554"

        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )

        for i, otp_input in enumerate(otp_inputs):

            # print(i)
            # print(otp_input)
            otp_input.send_keys(otp_digits[i])

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='continue ng-star-inserted']")
            )
        ).click()

        element_msg = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mat-simple-snack-bar-content']")
            )
        )

        message = element_msg.text
        print("Snack bar message:", message)

        # Assert that the snack bar message is as expected
        expected_message = "OTP validation failed"
        assert (
            message == expected_message
        ), f"Expected message '{expected_message}' but got '{message}'"

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e


#############################################################################################################################################


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Login with international number")
def test_login_international(login):
    try:
        time.sleep(2)
        login.find_element(By.XPATH, "//a[normalize-space()='My Bookings']").click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='iti__arrow']"))
        ).click()
        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='United States']")
            )
        ).click()

        user = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        )
        user.send_keys("201 553-4696")

        login.find_element(
            By.XPATH, "//span[@class='continue ng-star-inserted']"
        ).click()

        otp_digits = "5555"

        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )

        for i, otp_input in enumerate(otp_inputs):

            # print(i)
            # print(otp_input)
            otp_input.send_keys(otp_digits[i])

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='continue ng-star-inserted']")
            )
        ).click()

        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e


###################################################################################################################################

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Login with international number")
def test_login_international(login):

    try:

        time.sleep(2)
        login.find_element(By.XPATH, "//a[normalize-space()='My Bookings']").click()

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e    