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
        assert message == expected_message, f"Expected message '{expected_message}' but got '{message}'"

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

###################################################################################################################################### 

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invalid userid and Invalid password")
def test_invalid_userid_invalid_password(login):
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
        assert message == expected_message, f"Expected message '{expected_message}' but got '{message}'"

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e