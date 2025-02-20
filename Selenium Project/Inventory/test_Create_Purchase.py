import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from datetime import datetime
from Create_Purchase import test_create_purchase

@pytest.fixture
def login():
    driver = webdriver.Chrome()
    driver.get("https://scale.jaldee.com/business/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_create_purchase_workflow(login):
    test_create_purchase(login)

def test_create_purchase_elements(login):
    login.get("https://scale.jaldee.com/business/")
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//img)[6]"))
    ).click()

    time.sleep(5)
    purchase_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Purchase']"))
    )
    assert purchase_button is not None, "Purchase button not found"
    purchase_button.click()

    store_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select Store']"))
    )
    assert store_button is not None, "Store button not found"
    store_button.click()

    store = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Geetha']"))
    )
    assert store is not None, "Store 'Geetha' not found"
    store.click()

    vendor_dropdown = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p-dropdown[@placeholder='Select Vendor']//div[@aria-label='dropdown trigger']"))
    )
    assert vendor_dropdown is not None, "Vendor dropdown not found"
    vendor_dropdown.click()

    supplier = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='MedCC']"))
    )
    assert supplier is not None, "Supplier 'MedCC' not found"
    supplier.click()

def test_create_purchase_add_items(login):
    login.get("https://scale.jaldee.com/business/")
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//img)[6]"))
    ).click()

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Purchase']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select Store']"))
    ).click()

    store = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Geetha']"))
    )
    store.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p-dropdown[@placeholder='Select Vendor']//div[@aria-label='dropdown trigger']"))
    ).click()

    supplier = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='MedCC']"))
    )
    supplier.click()

    login.find_element(By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']").click()

    time.sleep(2)
    inventory_catalog = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='catalog1']"))
    )
    inventory_catalog.click()

    bill_no = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Purchase Bill#']"))
    )
    bill_no.click()

    random_number = str(random.randint(10000, 99999))
    bill_no.send_keys(random_number)

    login.find_element(By.XPATH, "//p-calendar//input[@type='text']").click()

    today_date = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]"))
    )
    today_date.click()

    login.find_element(By.XPATH, "//textarea[@placeholder='Notes to Vendor']").send_keys("Medcc Supplied item")

    element1 = login.find_element(By.XPATH, "//span[normalize-space()='Add Items']")
    login.execute_script("arguments[0].scrollIntoView();", element1)

    item_list = ["Items,Item3"]
    random_batch_number = str(random.randint(100, 1000))
    time.sleep(3)
    for i in range(len(item_list)):
        item_xpath = f"//div[@class='d-flex justify-content-between fw-bold']//div[@class='ng-star-inserted'][normalize-space()='{item_list[i]}']"
        time.sleep(2)
        WebDriverWait(login, 30).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search items']"))
        ).send_keys("it")

        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, item_xpath))
        ).click()

        time.sleep(5)
        batch_number = WebDriverWait(login, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//td//div[@class='ng-star-inserted']//input[@type='text' and contains(@class, 'p-inputtext')]")
            )
        )
        batch_number.click()
        batch_number.send_keys(random_batch_number)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@placeholder='Item Units']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']"))
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Box of 10']"))
        ).click()

        time.sleep(2)
        item_exp = f"//p-calendar[contains(@class, 'exp-date') and contains(@class, 'ng-tns-c')]"
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, item_exp))
        ).click()

        time.sleep(2)
        current_year = datetime.now().strftime("%Y")
        current_year_xpath = f"//button[normalize-space()='{current_year}']"
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, current_year_xpath))
        ).click()

        [year, month, day] = add_date(2)
        year_xpath = f"//span[normalize-space()='{year}']"
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, year_xpath))
        ).click()
        time.sleep(1)
        month_xpath = f"//span[normalize-space()='{month}']"
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, month_xpath))
        ).click()
        time.sleep(2)
        day_xpath = f"//span[normalize-space()='{day}' and not(contains(@class,'p-disabled'))]"
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, day_xpath))
        ).click()

        qty = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@min='1']"))
        )
        qty.click()
        qty.clear()
        qty_random_number = str(random.randint(10, 50))
        qty.send_keys(qty_random_number)

        free_qty = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@class,'free-quantity')]"))
        )
        free_qty.click()
        free_qty.clear()
        free_qty_random_number = str(random.randint(1, 5))
        free_qty.send_keys(free_qty_random_number)

        mrpprice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//input[contains(@class,'item-price')])[1]"))
        )
        mrpprice.click()
        mrpprice.clear()
        mrpprice_random_number = str(random.randint(100, 200))
        mrpprice.send_keys(mrpprice_random_number)

        time.sleep(2)
        price = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[contains(@class,'item-price')])[2]"))
        )
        price.click()
        price.clear()
        price_random_number = str(random.randint(40, 90))
        price.send_keys(price_random_number)

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Add']"))
        ).click()
        time.sleep(3)

def add_date(years_to_add):
    future_date = datetime.now().replace(year=datetime.now().year + years_to_add)
    return [future_date.year, future_date.strftime("%b"), future_date.day]