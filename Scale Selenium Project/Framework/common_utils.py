import pytest
import random
import string
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

scale_url = "https://scale.jaldee.com/business/"
prod_url = "https://www.jaldee.com/business/"
test_mail = "test@jaldee.com"


def create_user_data():
    fake = Faker()
    first_name = fake.first_name()
    print(first_name)
    last_name = fake.last_name()
    print(last_name)
    cons_manual_id = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
    print(cons_manual_id)
    random_digits = ''.join(random.choices(string.digits, k=7))
    phonenumber = f"{555}{random_digits}"
    print(phonenumber)
    email = f"{phonenumber}.{first_name}.{test_mail}"
    print(email)
    return [first_name, last_name, cons_manual_id, phonenumber, email]


@pytest.fixture()
def login(url):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url)
    driver.maximize_window()

    driver.find_element(By.ID, "phone").send_keys("5555556030")
    driver.find_element(By.ID, "password").send_keys("Jaldee01")
    driver.find_element(By.XPATH, "//div[@class='mt-2']").click()
    # time.sleep(10)
    driver.implicitly_wait(5)
    yield driver
    # driver.close()
    # driver.quit()
