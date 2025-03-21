import time
import uuid

from Framework.common_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Framework.common_dates_utils import *


@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_stock_transfer(login):
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//img)[6]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Stock Transfer')]"))
    ).click()

    login.implicitly_wait(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//i[@class='pi pi-plus']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    element_scroll = login.find_element(By.XPATH, "//span[normalize-space()='Geetha']")
    login.execute_script("arguments[0].scrollIntoView();", element_scroll)
    element_scroll.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
    ).click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Inventory_catalog']"))
    ).click()

    time.sleep(1)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
    ).click()

    element_scroll_1 = login.find_element(By.XPATH, "//span[normalize-space()='Swathy Pharmacy']")
    login.execute_script("arguments[0].scrollIntoView();", element_scroll_1)
    element_scroll_1.click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
             
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Inventory Catalog2']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Search items']"))
    ).send_keys("item")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='d-flex justify-content-between fw-bold']//div[@class='ng-star-inserted'][normalize-space()='Items']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Select Batch')]"))
    ).click()
    
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='69']"))
    ).click()

    qty= WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@type='number']"))
    )
    qty.click()
    qty.clear()
    qty.send_keys("25")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Add']"))
    ).click()

    time.sleep(1)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Transfer Request']"))
    ).click()

    toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_message.text
    print("Toast Message:", message)

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='DISPATCH']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    time.sleep(3)
    store = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Geetha'])[1]"))
    )
    login.execute_script("arguments[0].scrollIntoView();", store)

    store.click()

    time.sleep(5)



     # Wait for the table to be present
    table_body = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
    )

    # Locate the first table row
    first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")

    # Find the status element within the first row
    status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
    status_text = status_element.text
    expected_status = "DISPATCHED"

    print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

    # Assert that the status is "DISPATCHED"
    assert status_text == "DISPATCHED", f"Expected status to be 'DISPATCHED', but got '{status_text}'"

    
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    time.sleep(3)
    store1 = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='Swathy Pharmacy'])[1]"))
    )
    login.execute_script("arguments[0].scrollIntoView();", store1)

    store1.click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Received'])[1]"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//i)[5]"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='RECEIVED']"))
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

    time.sleep(2)
     # Wait for the table to be present
    table_body = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
    )

    # Locate the first table row
    first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")

    # Find the status element within the first row
    status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
    status_text = status_element.text
    expected_status = "RECEIVED"

    print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

    # Assert that the status is "RECEIVED"
    assert status_text == "RECEIVED", f"Expected status to be 'RECEIVED', but got '{status_text}'"

    