import time
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
    time.sleep(5)
    # print("Select Store:", store.text)

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
    input_field = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@class='p-inputtext p-component p-element ng-valid p-filled ng-touched ng-dirty']"))
    )

    # Clear the existing text from the input field
    input_field.clear()

    # Enter a new value into the input field
    new_value = "10"
    input_field.send_keys(new_value)

    # Confirm the new value is entered by retrieving the input field value
    entered_value = input_field.get_attribute('value')
    print(f"Entered Qty value: {entered_value}")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Add']"))
    ).click()

    batch_no = login.find_element(By.XPATH, "//input[@class='p-inputtext p-component p-element"
                                            "ng-pristine ng-valid ng-star-inserted ng-touched']").click()

    random_number = str(random.randint(100, 999))
    batch_no.send_keys(random_number)
    print("Batch No:", random_number)

    login.find_element(By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']").click()
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Box of 10']"))
    ).click()

    login.find_element(By.XPATH, "(//span[@class='ng-tns-c83-347 p-calendar'])[1]").click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='2024']"))
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



