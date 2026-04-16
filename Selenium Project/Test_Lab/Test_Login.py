import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import random
import string
test_mail = "@jaldee.com"

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def create_user_data():
    fake = Faker()
    first_name = fake.first_name()
    # print(first_name)
    last_name = fake.last_name()
    # print(last_name)
    # cons_manual_id = "".join(random.choices(string.ascii_letters + string.digits, k=3))
    # # print(cons_manual_id)
    random_digits = fake.numerify(text="#######")
    # random_digits = ''.join(random.choices(string.digits, k=7))
    phonenumber = f"{555}{random_digits}"
    # print(phonenumber)
    email = f"{first_name}.{last_name}{test_mail}"
    # print(email)
    return [first_name, last_name, phonenumber, email]


def test_appointment_newcustomer(driver):

    wait=WebDriverWait(driver, 30)

    
    driver.get("https://scale.jaldee.com/business/")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='loginId']").send_keys("5558881790")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Jaldee12")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[contains(@class,'p-card-body')]//div[contains(text(),'Appointments')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@id='actionCreate_BUS_bookList']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[@id='btnCreateCust_BUS_appt']").click()
    time.sleep(2)

    first_name, last_name, phonenumber, email = create_user_data()

    driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    driver.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    driver.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)

    driver.find_element(By.XPATH, "//button[span[contains(text(),'Save')]]").click()
    time.sleep(5)

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//p-dropdown[@id='selectUser_BUS_apptForm']"))
    ).click()
    time.sleep(2)
    options = driver.find_elements(By.XPATH, "//ul[@role='listbox']//li[@role='option']")

    # Pick a random option
    random_option = random.choice(options)

    # Click it
    random_option.click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//a[@id='actnAddNote_BUS_notAttch']"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']"))
    ).send_keys("Appointment Notes")
    time.sleep(1)
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[@id='btnSave_BUS_addNote']"))
    ).click()

    time.sleep(2)

    Confirm_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@id='btnConfirm_BUS_apptForm']")))
    driver.execute_script("arguments[0].scrollIntoView();", Confirm_element)

    time.sleep(2)

    Confirm_element.click()

    time.sleep(5)
    