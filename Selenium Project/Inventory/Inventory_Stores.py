
import time
import allure

from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException






@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_store_creation(login):
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
    ).click()

    time.sleep(5)

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Stores']"))
    ).click()

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Store']"))
    ).click()


    dropdown = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Type']"))  
    )
    dropdown.click() 

    dropdown_item = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Pharmacy']"))
    )

    dropdown_item.click()

    store_name = "Store_" + str(uuid.uuid4())[:6]
    print(store_name)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='storeName']"))
    ).send_keys(store_name)

    email = f"{store_name}{test_mail}"
    random_number = str(random.randint(1111111, 9999999))
    phonenumber = f"{555}{random_number}"

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
    ).send_keys(phonenumber)

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
    ).send_keys(email)


    invoice_prefix = "K_" + str(uuid.uuid4())[:1]
    print(invoice_prefix)
    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Invoice prefix']"))
    ).send_keys(invoice_prefix)
    

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Location']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Chavakkad']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create']"))
    ).click()

    try:

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

    except:

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)
    time.sleep(3)


