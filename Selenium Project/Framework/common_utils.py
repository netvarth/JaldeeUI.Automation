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





scale_url = "https://scale.jaldee.com/business/"
prod_url = "https://www.jaldee.com/business/"
localhost_url = "https://localhost:4200/business/"
test_scale_url = "https://test.jaldee.com/business/"
test_mail = ".test@jaldee.com"
consumer_url = "https://scale.jaldee.com/visionhospital/"
test_consumer_url = "https://test.jaldee.com/53b6eu1/"


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
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--ignore-ssl-errors=yes")
    # chrome_options.add_argument("--ignore-certificate-errors")
    # chrome_options.add_argument("--lang=en-US")

    # driver = webdriver.Chrome(
    #     service=ChromeService(ChromeDriverManager().install()), options=chrome_options
    # )
    

    driver = webdriver.Chrome(
        service=ChromeService(
            # executable_path=r"D:\ChromeDriver\chromedriver-win64\chromedriver.exe"
            executable_path=r"Drivers\chromedriver-win64\chromedriver.exe"
        )
    )
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)

    # 5550005540  Netvarth123  5555556030 Jaldee01 5555998877 Jaldee01
    # driver.find_element(By.ID, "loginId").send_keys("5550005540")
    # driver.find_element(By.ID, "password").send_keys("Netvarth123")
    # 5550005540  Netvarth123  5555556030  Jaldee01 

    # driver.find_element(By.ID, "loginId").send_keys("5550005540")#Production
    # driver.find_element(By.ID, "password").send_keys("Jaldee01")

    # driver.find_element(By.ID, "loginId").send_keys("5555523479")
    # driver.find_element(By.ID, "password").send_keys("Jaldee123")
    # driver.find_element(By.ID, "loginId").send_keys("5551111557")
    # driver.find_element(By.ID, "password").send_keys("Jaldee123")
    # driver.find_element(By.ID, "loginId").send_keys("6030")#Test
    # driver.find_element(By.ID, "password").send_keys("Jaldee01")
    # driver.find_element(By.ID, "loginId").send_keys("5555550603")#Scal
    # driver.find_element(By.ID, "password").send_keys("Jaldee01")
    driver.find_element(By.ID, "loginId").send_keys("5555556030")#Scale
    driver.find_element(By.ID, "password").send_keys("Jaldee01")
    # driver.find_element(By.ID, "loginId").send_keys("5555557799")#Whole
    # driver.find_element(By.ID, "password").send_keys("Jaldee01")
    # driver.find_element(By.ID, "loginId").send_keys("5555998844")#salesorder
    # driver.find_element(By.ID, "password").send_keys("Jaldee123")
    # driver.find_element(By.ID, "loginId").send_keys("login12347")#Production sales order
    # driver.find_element(By.ID, "password").send_keys("Jaldee123")
  
    # driver.find_element(By.ID, "loginId").send_keys("5555523479")
    # driver.find_element(By.ID, "password").send_keys("Jaldee123")
    driver.find_element(By.XPATH, "//div[@class='mt-2']").click()
    
    # time.sleep(10)
    driver.implicitly_wait(5)
    yield driver
    driver.close()
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
def generate_random_billing_address():
    fake = Faker()
    street_address = fake.street_address()  # e.g., '1234 Elm St.'
    city = fake.city()  # e.g., 'Springfield'
    state = fake.state()  # e.g., 'Illinois'
    zip_code = fake.zipcode()  # e.g., '62704'
    country = fake.country()  # e.g., 'United States'
    
    # Combine to form a full billing address
    billing_address = f"{street_address}, {city}, {state} {zip_code}, {country}"
    
    return billing_address