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
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
import allure
from allure_commons.types import AttachmentType
import os
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import TimeoutException




test_url = "https://test.jaldee.com/business/"
scale_url = "https://scale.jaldee.com/business/"
prod_url = "https://www.jaldee.com/business/"
localhost_url = "https://localhost:4200/business/"
test_scale_url = "https://scale.jaldeetest.in/business/"
test_mail = ".test@jaldee.com"
consumer_url = "https://scale.jaldee.com/visionhospital/"
test_consumer_url = "https://scale.jaldeetest.in/visionhospital/"
test_prod_url = "https://beta.jaldee.com/business/"
sales_officer = "001920"
credit_head = "001921"
branch_manager = "001922"
password = "Jaldee01"
main_scale = "5555556030"
main_prod = "5550005540"
scale_consumer = "9207206005"
prod_sales_officer = "001921"
prod_credit_head = "001922"
prod_branch_manager = "001923" 
# sales_order_scale = "556131"
sales_order_scale = "55789"
membership_scale = "556232"
test_user = "Krishnadas"
password_1 = "Netvarth1"
Lab_order_user = "556333"




def create_user_data():
    fake = Faker()
    first_name = fake.first_name()
    # print(first_name)
    last_name = fake.last_name()
    # print(last_name)
    cons_manual_id = "".join(random.choices(string.ascii_letters + string.digits, k=3))
    # print(cons_manual_id)
    random_digits = fake.numerify(text="#######")
    # random_digits = ''.join(random.choices(string.digits, k=7))
    phonenumber = f"{555}{random_digits}"
    # print(phonenumber)
    email = f"{first_name}.{last_name}{test_mail}"
    # print(email)
    return [first_name, last_name, cons_manual_id, phonenumber, email]


@pytest.fixture()
# def login(url, username, password):

#     driver = webdriver.Chrome(
#         service=ChromeService(
#             executable_path=r"Drivers\chromedriver-win64\chromedriver.exe"
#         )
#     )
#     driver.get(url)
#     driver.maximize_window()
#     time.sleep(5)
#     driver.find_element(By.ID, "loginId").send_keys(username)   
#     driver.find_element(By.ID, "password").send_keys(password)
#     driver.find_element(By.XPATH, "//div[@class='mt-2']").click()
#     driver.implicitly_wait(5)
#     yield driver
#     driver.close()
def login(url, username, password):
    chrome_options = webdriver.ChromeOptions()
    
    # Disable password saving, password breach warnings, safety check popups
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-features=PasswordManagerEnforcement,PasswordChange,SafeBrowsingProtection")
    chrome_options.add_argument("--safebrowsing-disable-download-protection")
    chrome_options.add_argument("--safebrowsing-disable-extension-blacklist")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation", "load-extension"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # Initialize Chrome driver with options
    driver = webdriver.Chrome(
        service=ChromeService(executable_path=r"Drivers\chromedriver-win64\chromedriver.exe"),
        options=chrome_options
    )

    wait = WebDriverWait(driver, 10)  # Explicit wait up to 10 seconds

    def retry_find(by, locator, retries=3):
        """Helper to find an element with retries"""
        for attempt in range(retries):
            try:
                element = wait.until(EC.visibility_of_element_located((by, locator)))
                return element
            except (TimeoutException, NoSuchElementException):
                if attempt == retries - 1:
                    raise
                time.sleep(1)  # Short wait before retry

    try:
        driver.get(url)
        driver.maximize_window()

        retry_find(By.ID, "loginId").send_keys(username)
        retry_find(By.ID, "password").send_keys(password)
        retry_find(By.XPATH, "//div[@class='mt-2']").click()

        driver.implicitly_wait(5)

        yield driver

    finally:
        driver.quit()




@pytest.fixture()
def con_login(url):

    driver = webdriver.Chrome(
        service=ChromeService(
            executable_path=r"Drivers\chromedriver-win64\chromedriver.exe"
        )
    )
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    yield driver


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
    email = f"{first_name}{test_mail}"
    print(email)
    return [first_name, last_name, phonenumber, email]

def create_business_detail():
    fake = Faker()
    bs_name = fake.bs()
    print(bs_name)
    vendors_id = "".join(random.choices(string.ascii_letters + string.digits, k=3))
    print(vendors_id)
    return [bs_name, vendors_id]
 


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
        
def scroll_to_window(login):
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def scroll_to_element(login, element):
    login.execute_script("arguments[0].scrollIntoView(true);", element)


# Generate a random billing address
# def generate_random_billing_address():
#     fake = Faker()
#     street_address = fake.street_address()  # e.g., '1234 Elm St.'
#     city = fake.city()  # e.g., 'Springfield'
#     state = fake.state()  # e.g., 'Illinois'
#     zip_code = fake.zipcode()  # e.g., '62704'
#     country = fake.country()  # e.g., 'United States'
    
#     # Combine to form a full billing address
#     # billing_address = f"{street_address}, {city}, {state} {zip_code}, {country}"
    
#     # return billing_address
#     return {street_address}, {city}, {state}, {zip_code}, {country}
def generate_random_billing_address():
    fake = Faker()
    street_address = fake.street_address()
    city = fake.city()
    state = fake.state()
    zip_code = fake.zipcode()
    country = fake.country()

    billing_address = f"{street_address}, {city}, {state} {zip_code}, {country}"
    return billing_address


def generate_random_billing_india_address():
    fake = Faker("en_IN")
    street_address = fake.street_address()  # e.g., '12 MG Road'
    city = fake.city()  # e.g., 'Mumbai'
    state = fake.state()  # e.g., 'Maharashtra'
    zip_code = fake.postcode()  # e.g., '400001'
    country = "India"  # Fixed for Indian addresses
    
    return street_address, city, state, zip_code, country
