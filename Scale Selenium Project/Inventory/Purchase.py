import time
from datetime import datetime, date
import uuid

from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_create_catalogs(login):
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@class='menu-item menu-item-submenu mt-2 ng-star-inserted'][7]"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Purchase']"))
    ).click()
    login.implicitly_wait(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='p-element create-purchase-button me-1 p-button p-component']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select Store']"))
    ).click()

    time.sleep(3)
    store = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Swathy Pharmacy')]"))
    )
    store.click()

    login.find_element(By.XPATH, "//span[normalize-space()='Select Supplier']").click()

    Select_supplier = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='MedCC']"))
    )
    Select_supplier.click()
    print("Select Supplier:", Select_supplier.text)

    login.find_element(By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']").click()

    Inventory_Catalog = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Inventory Catalog2']"))
    )
    Inventory_Catalog.click()
    print("Inventory Selected:", Inventory_Catalog.text)

    Bill_no = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Purchase Bill#']"))
    )
    Bill_no.click()

    random_number = str(random.randint(10000, 99999))
    Bill_no.send_keys(random_number)
    print("Bill no:", random_number)

    login.find_element(By.XPATH, "//p-calendar//input[@type='text']").click()

    Today_Date = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]"))
    )
    Today_Date.click()
    print("Date:", Today_Date.text)

    login.find_element(By.XPATH, "//textarea[@placeholder='Notes to supplier']").send_keys("Medcc  Supplied item ")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Add Items']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-radio']//input[@type='radio'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']"))
    ).click()
    time.sleep(3)
    try:
        # Wait for the input field to be visible and interactable
        input_field = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@type='number'])[1]"))
        )

        # Clear any existing value in the input field (optional)
        input_field.clear()

        # Enter a new value into the input field
        input_value = 10
        input_field.send_keys(str(input_value))  # Convert to string before sending keys

        # For example, to verify the min attribute:
        min_value = int(input_field.get_attribute("min"))
        assert input_value >= min_value, f"Value {input_value} should be >= {min_value}"
    except Exception as e:
        print("Exception:", e)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Add']"))
    ).click()

    time.sleep(3)
    batch_no = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@type='text'])[5]"))
    )
    batch_no.click()

    random_number = str(random.randint(100, 999))
    batch_no.send_keys(random_number)
    print("Batch No:", random_number)

    login.find_element(By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']").click()
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Box of 10']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@type='text'])[7]"))
    ).click()

    current_year = datetime.now().strftime("%Y")
    current_year_xpath = f"//button[normalize-space()='{current_year}']"
    print(current_year_xpath)
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, current_year_xpath))
    ).click()

    [year, month, day] = add_date(2)
    print(year)
    year_xpath = f"//span[normalize-space()='{year}']"
    print(year_xpath)
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, year_xpath))
    ).click()
    time.sleep(2)
    month_xpath = f"//span[normalize-space()='{month}']"

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, month_xpath))
    ).click()
    time.sleep(2)
    day_xpath = f"//span[normalize-space()='{day}']"
    print(day_xpath)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, day_xpath))
    ).click()


