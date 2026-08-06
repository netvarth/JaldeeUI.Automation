import random
import time
from datetime import datetime, timedelta

import allure
import pyautogui
import pytest
from allure_commons.types import AttachmentType
from faker import Faker
from selenium import webdriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


sales_order_consumer_scale_url = "https://scale.jaldee.com/orison"
consumer_login_url = "https://scale.jaldee.com/RangSweets"
consumer_login_url_1 = "https://scale.jaldee.com/visionhospital/"
consumer_login_url_2 = "https://jaldee.com/royalclinic/"
Scale_Lab_order_consumer_url = (
    "https://scale.jaldee.com/customapp/63c2083?"
    "inst_id=1&app_id=1&partner=true"
)


@pytest.fixture()
def consumer_login(url):
    chrome_options = webdriver.ChromeOptions()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection_enabled": False,
        "password_manager_enabled": False,
    }

    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-password-manager-reauthentication")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    # Selenium Manager automatically selects/downloads a ChromeDriver
    # compatible with the locally installed Chrome browser.
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        driver.maximize_window()
        yield driver
    finally:
        driver.quit()


def generate_random_salutation():
    salutations = [
        "Mr.",
        "Ms.",
        "Mrs.",
        "Master",
        "Miss",
        "B/o",
        "Dr.",
        "Adv.",
        "Fr.",
    ]
    return random.choice(salutations)


def create_consumer_data(role="consumer"):
    """
    Generate random consumer/family-member data.

    The role argument is retained for compatibility with existing tests.
    """
    fake = Faker()
    first_name = fake.first_name().lower()
    last_name = fake.last_name().lower()
    random_digits = fake.numerify(text="#######")
    phonenumber = f"555{random_digits}"
    email = f"{first_name}.{last_name}@jaldee.com"

    return [first_name, last_name, phonenumber, email]


def scroll_to_window(consumer_login):
    consumer_login.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )


def scroll_to_element(consumer_login, element):
    consumer_login.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        element,
    )


def click_to_element(consumer_login, element):
    consumer_login.execute_script("arguments[0].click();", element)


def wait_and_click(consumer_login, by, value, timeout=10, retries=3):
    last_exception = None

    for attempt in range(1, retries + 1):
        try:
            wait = WebDriverWait(consumer_login, timeout)
            element = wait.until(EC.element_to_be_clickable((by, value)))

            consumer_login.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                element,
            )

            try:
                element.click()
            except ElementClickInterceptedException:
                element = wait.until(EC.element_to_be_clickable((by, value)))
                consumer_login.execute_script("arguments[0].click();", element)

            return element

        except (
            StaleElementReferenceException,
            ElementClickInterceptedException,
            TimeoutException,
        ) as exc:
            last_exception = exc

            if attempt == retries:
                raise

            time.sleep(1)

    raise last_exception


def wait_and_locate_click(consumer_login, by, value, timeout=10, retries=3):
    return wait_and_click(
        consumer_login,
        by,
        value,
        timeout=timeout,
        retries=retries,
    )


def wait_and_locate_all_click(consumer_login, by, value, timeout=30):
    elements = WebDriverWait(consumer_login, timeout).until(
        EC.presence_of_all_elements_located((by, value))
    )

    for element in elements:
        try:
            consumer_login.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                element,
            )
            element.click()
        except (
            StaleElementReferenceException,
            ElementClickInterceptedException,
        ):
            consumer_login.execute_script("arguments[0].click();", element)

    return elements


def wait_and_visible_click(consumer_login, by, value, timeout=10, retries=3):
    last_exception = None

    for attempt in range(1, retries + 1):
        try:
            wait = WebDriverWait(consumer_login, timeout)
            element = wait.until(EC.visibility_of_element_located((by, value)))
            element = wait.until(EC.element_to_be_clickable((by, value)))

            try:
                element.click()
            except ElementClickInterceptedException:
                element = wait.until(EC.element_to_be_clickable((by, value)))
                consumer_login.execute_script("arguments[0].click();", element)

            return element

        except (
            StaleElementReferenceException,
            ElementClickInterceptedException,
            TimeoutException,
        ) as exc:
            last_exception = exc

            if attempt == retries:
                raise

            time.sleep(1)

    raise last_exception


def wait_and_send_keys(
    consumer_login,
    by,
    value,
    keys,
    timeout=10,
    clear_first=False,
):
    element = WebDriverWait(consumer_login, timeout).until(
        EC.visibility_of_element_located((by, value))
    )

    if clear_first:
        element.clear()

    element.send_keys(keys)
    return element


def wait_for_text(consumer_login, by, value, timeout=10):
    element = WebDriverWait(consumer_login, timeout).until(
        EC.visibility_of_element_located((by, value))
    )
    return element.text.strip()


def get_snack_bar_message(consumer_login, timeout=10):
    selectors = [
        (By.CLASS_NAME, "snackbarnormal"),
        (By.CLASS_NAME, "snackbarerror"),
        (
            By.CSS_SELECTOR,
            ".mat-mdc-snack-bar-label.mdc-snackbar__label",
        ),
    ]

    for by, selector in selectors:
        try:
            snack_bar = WebDriverWait(consumer_login, timeout).until(
                EC.visibility_of_element_located((by, selector))
            )

            message = snack_bar.text.strip()
            if message:
                return message

        except TimeoutException:
            continue

    return None


def Generate_dob():
    fake = Faker()
    dob = fake.date_of_birth(minimum_age=35, maximum_age=43)

    year = dob.strftime("%Y")
    month = dob.strftime("%b")
    day = dob.strftime("%d")

    return [year, month, day]