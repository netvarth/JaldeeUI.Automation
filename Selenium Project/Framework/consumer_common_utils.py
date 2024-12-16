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
def consumer_login():

    driver = webdriver.Chrome(
        service=ChromeService(
            executable_path=r"Drivers\chromedriver-win64\chromedriver.exe"
        )
    )
    # driver.get("https://scale.jaldee.com/visionhospital/")
    driver.get("https://scale.jaldee.com/RangSweets")
    # driver.get("https://www.jaldee.com/02s7i59")#ProductionOrder
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
    test_email = "test@jaldee.com"
    email = f"{first_name}.{test_email}"

    return {
        "first_name": first_name,
        "last_name": last_name,
        "phonenumber": phonenumber,
        "email": email,
        "otp": "55555"  
    }

def scroll_to_window(consumer_login):
    consumer_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def scroll_to_element(consumer_login, element):
    consumer_login.execute_script("arguments[0].scrollIntoView(true);", element)


def wait_and_click(consumer_login, by, value, timeout=10):
    element = WebDriverWait(consumer_login, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()
    return element

def wait_and_locate_click(consumer_login, by, value, timeout=10):
    element = WebDriverWait(consumer_login, timeout).until(EC.presence_of_element_located((by, value)))
    element.click()
    return element

def wait_and_visible_click(consumer_login, by, value, timeout=10):
    element = WebDriverWait(consumer_login, timeout).until(EC.visibility_of_element_located((by, value)))
    element.click()
    return element

def wait_and_send_keys(consumer_login, by, value, keys, timeout=10):
    element = WebDriverWait(consumer_login, timeout).until(EC.presence_of_element_located((by, value)))
    element.send_keys(keys)
    return element

def wait_for_text(consumer_login, by, value, timeout=10):
    element = WebDriverWait(consumer_login, timeout).until(EC.presence_of_element_located((by, value)))
    return element.text

def get_snack_bar_message(consumer_login, timeout=10):
    try:
        # Try to get the normal snack bar message
        snack_bar = WebDriverWait(consumer_login, timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        return message

    except:
        # If not found, try to get the error snack bar message
        try:
            snack_bar = WebDriverWait(consumer_login, timeout).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            return message
        except Exception as e:
            return None
        
def Generate_dob():
    fake = Faker()
    dob = fake.date_of_birth(minimum_age=35, maximum_age=43)
    year = dob.strftime("%Y")
    month = dob.strftime("%b")
    day = dob.strftime("%d")
    return [year, month, day]