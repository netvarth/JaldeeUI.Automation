import time
from datetime import datetime, timedelta

import pyautogui
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import os
from faker import Faker
import random
import string
from selenium.common import TimeoutException
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def login():

    driver = webdriver.Chrome(
        service=ChromeService(
            executable_path=r"Drivers\chromedriver-win64\chromedriver.exe"
        )
    )
    driver.get("https://scale.jaldee.com/visionhospital/")
    driver.maximize_window()
    yield driver
    driver.quit() 

def generate_random_salutation():
    salutations = ["Mr.", "Ms.", "Mrs.", "Master", "Miss", "B/o", "Dr.", "Adv.", "Fr."]
    return random.choice(salutations)

def create_consumer_data():
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    random_digits = fake.numerify(text="#######")
    phonenumber = f"555{random_digits}"
    test_email = "@jaldee.com"
    email = f"{first_name}.{last_name}{test_email}"

    return {
        "first_name": first_name,
        "last_name": last_name,
        "phonenumber": phonenumber,
        "email": email,
        "otp": "55555"  
    }

def scroll_to_window(login):
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def scroll_to_element(login, element):
    login.execute_script("arguments[0].scrollIntoView(true);", element)


def wait_and_click(login, by, value, timeout=10):
    element = WebDriverWait(login, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()
    return element

def wait_and_locate_click(login, by, value, timeout=10):
    element = WebDriverWait(login, timeout).until(EC.presence_of_element_located((by, value)))
    element.click()
    return element

def wait_and_visible_click(login, by, value, timeout=10):
    element = WebDriverWait(login, timeout).until(EC.visibility_of_element_located((by, value)))
    element.click()
    return element

def wait_and_send_keys(login, by, value, keys, timeout=10):
    element = WebDriverWait(login, timeout).until(EC.presence_of_element_located((by, value)))
    element.send_keys(keys)
    return element

def wait_for_text(login, by, value, timeout=10):
    element = WebDriverWait(login, timeout).until(EC.presence_of_element_located((by, value)))
    return element.text

def get_snack_bar_message(login, timeout=10):
    try:
        # Try to get the normal snack bar message
        snack_bar = WebDriverWait(login, timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        return message

    except:
        # If not found, try to get the error snack bar message
        try:
            snack_bar = WebDriverWait(login, timeout).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            return message
        except Exception as e:
            return None