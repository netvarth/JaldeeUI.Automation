import pytest
import random
import string
import uuid
import pyautogui
import time
import datetime
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime, timedelta
import allure
from allure_commons.types import AttachmentType
import os

scale_url = "https://scale.jaldee.com/business/"
prod_url = "https://www.jaldee.com/business/"
localhost_url = "https://localhost:4200/business/"
test_scale_url = "https://test.jaldee.com/business/"
test_mail = ".test@jaldee.com"
consumer_url = "https://scale.jaldee.com/visionhospital/"


def create_user_data():
    fake = Faker()
    first_name = fake.first_name()
    print(first_name)
    last_name = fake.last_name()
    print(last_name)
    cons_manual_id = "".join(random.choices(string.ascii_letters + string.digits, k=3))
    print(cons_manual_id)
    random_digits = fake.numerify(text="#######")
    # random_digits = ''.join(random.choices(string.digits, k=7))
    phonenumber = f"{555}{random_digits}"
    print(phonenumber)
    email = f"{first_name}.{last_name}{test_mail}"
    print(email)
    return [first_name, last_name, cons_manual_id, phonenumber, email]


@pytest.fixture()
def login(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--ignore-ssl-errors=yes")
    chrome_options.add_argument("--ignore-certificate-errors")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=chrome_options
    )
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)

    # 5550005540  Netvarth123  5555556030  Jaldee01
    driver.find_element(By.ID, "loginId").send_keys("5550005540")
    driver.find_element(By.ID, "password").send_keys("Netvarth123")
    driver.find_element(By.XPATH, "//div[@class='mt-2']").click()
    # time.sleep(10)
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()


def generate_random_salutation():
    salutations = ["Mr.", "Ms.", "Mrs.", "Master", "Miss", "B/o", "Dr.", "Adv.", "Fr."]
    return random.choice(salutations)


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
    print(email)
    return [first_name, last_name, phonenumber, email]
