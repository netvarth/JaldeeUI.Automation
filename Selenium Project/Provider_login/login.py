import time
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


@pytest.fixture()
def login():
    driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://scale.jaldee.com/business/")
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("valid userid and valid password")
def test_valid_userid_password(login):
    try:
        login.find_element(By.ID, "loginId").send_keys("5555556030")
        login.find_element(By.ID, "password").send_keys("Jaldee01")
        login.find_element(By.XPATH, "//div[@class='mt-2']").click()
        time.sleep(3)
        print("Login Successfully")

        try:
            # Wait until the image is present in the DOM
            element_present = EC.presence_of_element_located(
                (By.XPATH, "//img[@src='assets/images/dashboard/welcome.gif']")
            )
            WebDriverWait(login, 10).until(element_present)
            print("Image is present on the page.")
        except TimeoutException:
            print("Image not found on the page.")
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e


########################################################################################################################################################


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("valid userid and invalid password")
def test_valid_userid_invalid_password(login):
    try:
        login.find_element(By.ID, "loginId").send_keys("5555556030")
        login.find_element(By.ID, "password").send_keys("Jaldee1")
        login.find_element(By.XPATH, "//div[@class='mt-2']").click()
        time.sleep(3)

        element_msg = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='mat-mdc-snack-bar-label mdc-snackbar__label']",
                )
            )
        )
        message = element_msg.text
        print("Snack bar message:", message)

        # Assert that the snack bar message is as expected
        expected_message = "Invalid password."
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


###################################################################################################################################################


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invalid userid and Invalid password")
def test_invalid_userid_invalid_password(login):
    try:
        login.find_element(By.ID, "loginId").send_keys("55555560")
        login.find_element(By.ID, "password").send_keys("Jaldee1")
        login.find_element(By.XPATH, "//div[@class='mt-2']").click()
        time.sleep(3)

        element_msg = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='mat-mdc-snack-bar-label mdc-snackbar__label']",
                )
            )
        )
        message = element_msg.text
        print("Snack bar message:", message)

        # Assert that the snack bar message is as expected
        expected_message = "This login id is not registered with Jaldee. Sign up now with Jaldee to avail our services."
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


##########################################################################################################################################################


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Attempt more than 3 time")
def test_attempt_4time(login):
    try:
        for _ in range(4):
            login.find_element(By.ID, "loginId").clear()
            login.find_element(By.ID, "password").clear()
            login.find_element(By.ID, "loginId").send_keys("5555556030")
            login.find_element(By.ID, "password").send_keys("55467")
            login.find_element(By.XPATH, "//div[@class='mt-2']").click()
            time.sleep(3)

        element_msg = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='mat-mdc-snack-bar-label mdc-snackbar__label']",
                )
            )
        )
        message = element_msg.text
        print("Snack bar message:", message)

        # Assert that the snack bar message is as expected
        expected_message = "Account locked due to multiple failed login attempts. Please try again after 1 minute."
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


########################################################################################################################################################################


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Forfget password")
def test_forget_password(login):
    try:
        time.sleep(2)
        login.find_element(
            By.XPATH, "//a[normalize-space()='Forgot Password ?']"
        ).click()
        time.sleep(3)
        userid = login.find_element(By.ID, "loginId")
        userid.send_keys("5555556030")
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-button__label']")
            )
        ).click()
        otp_digits = "55555"

        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(login, 10).until(
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

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-button__label']")
            )
        ).click()

        login.find_element(By.XPATH, "//input[@id='newpassfield']").send_keys(
            "Jaldee01"
        )
        login.find_element(
            By.Xpath, "//input[@placeholder='Re-enter Password']"
        ).send_keys("Jaldee01")
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-button__label']")
            )
        ).click()

        time.sleep(2)

        login.find_element(By.ID, "loginId").send_keys("5555556030")
        login.find_element(By.ID, "password").send_keys("Jaldee01")
        login.find_element(By.XPATH, "//div[@class='mt-2']").click()
        time.sleep(1)
        try:

            element_present = EC.presence_of_element_located(
                (By.XPATH, "//img[@src='assets/images/dashboard/welcome.gif']")
            )
            WebDriverWait(login, 10).until(element_present)
            print("Image is present on the page.")
        except TimeoutException:
            print("Image not found on the page.")

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
