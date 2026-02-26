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
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import Select


import os
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException


test_url = "https://test.jaldee.com/business/"
scale_url = "https://scale.jaldee.com/business/"
prod_url = "https://www.jaldee.com/business/"
localhost_url = "https://localhost:4200/business/"
test_scale_url = "https://scale.jaldeetest.in/business/"
test_mail = ".test@jaldee.com"
consumer_url = "https://scale.jaldee.com/visionhospital/"
test_consumer_url = "https://scale.jaldeetest.in/visionhospital/"
test_prod_url = "https://beta.jaldee.com/business/"
lead_scale_url = "https://scale.jaldee.com/visionhospital/lead/create/ch-73b91u7-55"


sales_officer = "001920"
credit_head = "001921"
branch_manager = "001922"
password = "Jaldee01"
main_scale = "5555556030" 
main_scale_2 = "151225"
main_scale_1 = "5554646777"
main_prod = "5550005540"
scale_consumer = "9207206005"
prod_sales_officer = "001921"
prod_credit_head = "001922"
prod_branch_manager = "001923" 
sales_order_scale = "556131"
sales_order_scale_1 = "55789"
membership_scale = "556232"
test_user = "Krishnadas"
password_1 = "Netvarth1"
Lab_order_user = "556333"
IP_Management = "5555556633"
IP_Management_1 = "40251"




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






# @pytest.fixture()
# def login(request, url, username, password):
#     chrome_options = webdriver.ChromeOptions()

#     # ✅ ADD THIS FOR HEADLESS
#     chrome_options.add_argument("--headless=new")
#     chrome_options.add_argument("--window-size=1920,1080")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--no-sandbox")

#     chrome_options.add_experimental_option("prefs", {
#         "credentials_enable_service": False,
#         "profile.password_manager_enabled": False
#     })

#     prefs = {
#         "credentials_enable_service": False,
#         "profile.password_manager_enabled": False,
#         "profile.password_manager_leak_detection_enabled": False,
#         "password_manager_enabled": False,
#     }

#     chrome_options.add_experimental_option("prefs", prefs)

#     chrome_options.add_argument("--disable-notifications")
#     chrome_options.add_argument("--disable-infobars")
#     chrome_options.add_argument("--disable-save-password-bubble")
#     chrome_options.add_argument("--disable-password-manager-reauthentication")
#     chrome_options.add_argument("--no-first-run")
#     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
#     chrome_options.add_argument("--incognito")

#     driver = webdriver.Chrome(
#         service=ChromeService(executable_path=r"Drivers\chromedriver-win64\chromedriver.exe"),
#         options=chrome_options
#     )









@pytest.fixture()
def login(url, username, password):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    chrome_options.add_argument("--disable-notifications")

    prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection_enabled": False,
    "password_manager_enabled": False,  # extra precaution
    }

    chrome_options.add_experimental_option("prefs", prefs)

    # Disable Chrome popups, notifications, infobars, safe browsing
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-password-manager-reauthentication")
    chrome_options.add_argument("--no-first-run")  # skips first run popups
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # optional
    chrome_options.add_argument("--incognito")  # optional
   

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


# @pytest.fixture()
# def login(url, username, password):
#     options = FirefoxOptions()
#     options.set_preference("dom.webnotifications.enabled", False)
#     options.set_preference("signon.rememberSignons", False)
#     options.set_preference("network.cookie.cookieBehavior", 0)
#     options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

#     driver = webdriver.Firefox(
#         service=FirefoxService(executable_path=r"Drivers\geckodriver-win64\geckodriver.exe"),
#         options=options
#     )

#     wait = WebDriverWait(driver, 5)  # Shorter explicit wait

#     try:
#         driver.get(url)

#         # Fast login
#         wait.until(EC.visibility_of_element_located((By.ID, "loginId"))).send_keys(username)
#         wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
#         wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mt-2']"))).click()

#         yield driver

#     finally:
#         driver.quit()

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

@pytest.fixture()
def open_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=ChromeService(executable_path=r"Drivers\\chromedriver-win64\\chromedriver.exe"),
        options=chrome_options
    )

    yield driver
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
 


# def wait_and_click(login, by, value, timeout=30):
    element = WebDriverWait(login, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()
    return element


def wait_and_click(login, by, value, timeout=30):
    wait = WebDriverWait(login, timeout)
    element = wait.until(EC.presence_of_element_located((by, value)))
    wait.until(EC.visibility_of(element))
    wait.until(EC.element_to_be_clickable((by, value)))
    element.click()
    return element
# def wait_and_click(login, by, value, timeout=30):
#     wait = WebDriverWait(login, timeout)
#     last_err = None
#     for _ in range(3):  # small retry for Angular re-render
#         try:
#             # Don't cache an earlier element; get a FRESH clickable element now
#             el = wait.until(EC.element_to_be_clickable((by, value)))
#             el.click()
#             return el
#         except StaleElementReferenceException as e:
#             last_err = e
#     # If we still fail after retries, raise the last error
#     if last_err:
#         raise last_err

def wait_and_locate_click(login, by, value, timeout=30):
    element = WebDriverWait(login, timeout).until(EC.presence_of_element_located((by, value)))
    element.click()
    return element

def wait_and_locate_all_click(login, by, value, timeout=30):
    elements = WebDriverWait(login, timeout).until(EC.presence_of_all_elements_located((by, value)))
    for element in elements:
        element.click()
    return elements

def wait_and_visible_click(login, by, value, timeout=30):
    element = WebDriverWait(login, timeout).until(EC.visibility_of_element_located((by, value)))
    element.click()
    return element

def wait_and_send_keys(login, by, value, keys, timeout=30):
    element = WebDriverWait(login, timeout).until(EC.presence_of_element_located((by, value)))
    element.send_keys(keys)
    return element

def wait_for_text(login, by, value, timeout=30):
    element = WebDriverWait(login, timeout).until(EC.presence_of_element_located((by, value)))
    return element.text





# def get_snack_bar_message(login, timeout=30):
#     try:
#         # Try to get the normal snack bar message
#         snack_bar = WebDriverWait(login, timeout).until(
#             EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
#         )
#         message = snack_bar.text
#         return message

#     except:
#         # If not found, try to get the error snack bar message
#         try:
#             snack_bar = WebDriverWait(login, timeout).until(
#                 EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
#             )
#             message = snack_bar.text
#             return message
#         except Exception as e:
#             return None

def get_snack_bar_message(login, timeout=5):
    """
    Captures the snackbar message (normal or error) from Angular Material.
    Returns the message text if found, else None.
    """
    selectors = [
        ".cdk-overlay-container mat-snack-bar-container .mat-mdc-snack-bar-label.mdc-snackbar__label",
        ".cdk-overlay-container .mat-mdc-snack-bar-label.mdc-snackbar__label",
        "mat-snack-bar-container .mat-mdc-snack-bar-label.mdc-snackbar__label"
    ]

    for selector in selectors:
        try:
            # Wait for snackbar presence (not just visible)
            element = WebDriverWait(login, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )

            # Capture text before it disappears
            msg = element.text.strip()
            if msg:
                # allure.attach(msg, "Snackbar Message", allure.attachment_type.TEXT)
                return msg

        except Exception as e:
            continue

    return None


def get_toast_message(login, timeout=10):
    """
    Wait for a PrimeNG toast message and return its text.

    :param driver: Selenium WebDriver instance
    :param timeout: Maximum wait time in seconds
    :return: Toast message text or None if not found
    """
    try:
        toast_message = WebDriverWait(login, timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        return toast_message.text.strip()
    except:
        return None
    
def scroll_to_window(login):
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def scroll_to_element(login, element):
    login.execute_script("arguments[0].scrollIntoView();", element)

def click_to_element(login, element):
    login.execute_script("arguments[0].click();", element)


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


def get_next_room_name(file_path='room_counter.txt', prefix='B', start=101):
    try:
        with open(file_path, 'r') as f:
            last_number = int(f.read().strip())
    except FileNotFoundError:
        last_number = start - 1  # If file doesn't exist, start from 305

    next_number = last_number + 1

    with open(file_path, 'w') as f:
        f.write(str(next_number))

    return f"{next_number}{prefix}"





# ---------- Random Generators ----------
def generate_temperature_f():
    return round(random.uniform(96.0, 104.0), 2)

def generate_pulse_rate():
    return random.randint(60, 200)

def generate_respiration_rate():
    return random.randint(12, 40)

def generate_blood_pressure():
    systolic = random.randint(90, 140)
    diastolic = random.randint(60, 90)
    return systolic, diastolic


def create_room_and_bed(driver, wait, room_name):

    # Click Create Room
    wait_and_locate_click(driver, By.XPATH, "//*[@id='btnCreate_IP_RO_RO']")

    # Select Building
    wait_and_locate_click(driver, By.XPATH, "//*[@formcontrolname='building']")
    wait_and_locate_click(driver, By.XPATH, "//*[normalize-space()='Block D']")

    # Select Type
    wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='Select Type']")
    wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='Private']")

    # Select Category
    wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='Select Category']")
    wait_and_locate_click(driver, By.XPATH, "(//span[normalize-space()='Private'])[1]")

    # Enter Room Name
    room_input = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Room Name']")
    ))
    room_input.clear()
    room_input.send_keys(room_name)

    print(f"🏨 Room Created: {room_name}")

    # Select Nature
    wait_and_locate_click(driver, By.XPATH, "//p-dropdown[@formcontrolname='roomNature']")
    wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='Room']")

    # Create Room
    wait_and_locate_click(driver, By.XPATH, "//button[normalize-space()='Create']")
    get_toast_message(driver)

    # Open Room Details
    wait_and_locate_click(driver, By.XPATH, "(//*[contains(@class,'btnView_IP_RmGrd')])[last()]")

    # =========================
    # CREATE BED
    # =========================
    wait_and_locate_click(driver, By.XPATH, "//*[@id='btnCreateBed_IP_RmDet']")

    wait_and_locate_click(driver, By.XPATH, "//p-dropdown[@id='selectResrv_IP_BedCrt']")
    wait_and_locate_click(driver, By.XPATH, "//li[@aria-label='Yes']")

    wait_and_locate_click(driver, By.XPATH, "//p-dropdown[@id='selectBed_IP_BedCrt']")
    wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='Normal']")

    wait_and_locate_click(driver, By.XPATH, "//*[@id='selectBedCat_IP_BedCrt']")
    wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='Observation']")

    wait_and_locate_click(driver, By.XPATH, "//*[@id='selectBedPrice_IP_BedCrt']")
    wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='Normal Bed']")

    bed_name = f"Bed{room_name}"

    bed_input = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@id='inputBed_IP_BedCrt']")
    ))
    bed_input.send_keys(bed_name)

    wait_and_locate_click(driver, By.XPATH, "//*[@id='btnCrt_IP_BedCrt']")
    get_toast_message(driver)

    print(f"🛏️ Bed Created: {bed_name}")

    # Go back to dashboard
    for _ in range(4):
        wait_and_locate_click(driver, By.XPATH, "//i[@class='pi pi-arrow-left']")

    return bed_name

