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
    cons_manual_id = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
    print(cons_manual_id)
    random_digits = fake.numerify(text='#######')
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

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)

    # 5550005540  Netvarth123  5555556030  Jaldee01
    driver.find_element(By.ID, "phone").send_keys("5555556030")
    driver.find_element(By.ID, "password").send_keys("Jaldee01")
    driver.find_element(By.XPATH, "//div[@class='mt-2']").click()
    # time.sleep(10)
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()


# def fill_prescription_details(login, row, dose, frequency, duration, notes):
#     # Base XPath for the specified row
#     base_xpath = f"//table[@id='pr_id_19-table']/tbody/tr[{row}]"
    
#     # XPaths for each cell in the row
#     cells = ["/td[2]", "/td[3]", "/td[4]", "/td[5]"]
#     details = [dose, frequency, duration, notes]
    
#     # Iterate over each cell and detail to enter
#     for cell, detail in zip(cells, details):
#         cell_xpath = base_xpath + cell  # XPath for the cell
#         textarea_xpath = cell_xpath + "/p-celleditor/textarea"  # XPath for the textarea within the cell
        
#         # Find the cell element and click to activate it
#         cell_element = login.find_element(By.XPATH, cell_xpath)
#         cell_element.click()
        
#         # Find the textarea element and enter the detail
#         textarea_element = login.find_element(By.XPATH, textarea_xpath)
#         textarea_element.clear()  # Clear any existing text
#         textarea_element.send_keys(detail)


def fill_prescription_details(login, row_num, dose, frequency, duration, notes):
    base_xpath = f"//table[@id='pr_id_19-table']/tbody/tr[{row_num}]"
    dose_xpath = base_xpath + "/td[2]"
    frequency_xpath = base_xpath + "/td[3]"
    duration_xpath = base_xpath + "/td[4]"
    notes_xpath = base_xpath + "/td[5]"
    
    def fill_cell(cell_xpath, value):
        cell = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, cell_xpath)))
        cell.click()
        input_field = cell.find_element(By.TAG_NAME, "input")
        input_field.clear()
        input_field.send_keys(value)
    
    fill_cell(dose_xpath, dose)
    fill_cell(frequency_xpath, frequency)
    fill_cell(duration_xpath, duration)
    fill_cell(notes_xpath, notes)