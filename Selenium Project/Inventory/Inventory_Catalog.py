import time
import uuid

from Framework.common_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_inventory_catalog(login):
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//img)[6]"))
    ).click()

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Inv.Catalogs')]"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='p-ripple p-element p-button p-component']"))
    ).click()

    catalog_name = "Inventory_Catalog_" + str(uuid.uuid4())[:8]

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Catalog Name']"))
    ).send_keys(catalog_name)

    login.find_element(By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']").click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Geetha']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create Catalog']"))
    ).click()

    time.sleep(5)

    checkboxes = WebDriverWait(login, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//input[contains(@id, 'mat-mdc-checkbox')]"))
    )

    # Click the first three checkboxes
    for i in range(1, min(6, len(checkboxes))):
        checkboxes[i].click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']"))
    ).click()

    time.sleep(3)
    toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_detail.text
    print("toast_Message:", message)

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    time.sleep(2)
    store_dropdown = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Geetha']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", store_dropdown)

    store_dropdown.click()

    time.sleep(5)


@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_inventory_catalog_filter(login):
    time.sleep(5)
    wait = WebDriverWait(login, 20)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//img)[5]"))
    ).click()

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Catalogs')])[1]"))
    ).click()

    time.sleep(3)


    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Actions'])[1]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[1]"))
    ).click()

 