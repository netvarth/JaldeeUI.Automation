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

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating the item")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_item_creation(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "(//img)[6]"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Items']"))
    ).click()           

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create']"))
    ).click()

    item_name = "Item_" + str(uuid.uuid4())[:4]

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Item Name']"))
    ).send_keys(item_name)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Select Item Source']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='General']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Enter Item Description']"))
    ).send_keys("A Item name is required and recommended to be unique.")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select Category']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Antibacterials']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Select Group')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Medicine']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select Type']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Tablet']"))
    ).click()

    login.implicitly_wait(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select Manufacturer']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='ALPHA DRUGS']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Select Unit')]"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Box of 10'] "))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p-dropdown[@placeholder='Track Inventory or Not']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Yes']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select HSN Code']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='33215478']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Select Item Compositions')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'starch, hydroxypropyl methylcellulose, propylene g')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Select Item Tax')]"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='GST 12%']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Item']"))
    ).click()

    toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_detail.text
    print("toast_Message:", message)

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//i[@class='pi pi-arrow-left']"))
    ).click()


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test for item filter item id ")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_item_filter(login):

    time.sleep(3)
    wait = WebDriverWait(login, 20)
    wait.until(
        EC.presence_of_element_located((By.XPATH, "(//img)[6]"))
    ).click()

    time.sleep(3)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Items']"))
    ).click()  

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//i[@class='pi pi-filter-fill'])[1]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(), 'Item ID')]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//input[@id='spCode'])[1]"))
    ).send_keys("sprx-73b91u7-b")

    time.sleep(3)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='Apply'])[1]"))
    ).click()

    print("Apply the the filter")
    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Actions'])[1]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[1]"))
    ).click()
    print("Enter into the item detail page")
    time.sleep(3)
    # Assert that the ID is present on the page
    element = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, f"//*[contains(text(), 'sprx-73b91u7-b')]")
        )
    )
    assert element is not None, "The ID 'sprx-73b91u7-b' was not found on the page"
    print("Assertion passed: The ID 'sprx-73b91u7-b' is present on the page")
    
      
    scroll_down = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(), 'Item Consumption History')]"))
    )
    login.execute_script("arguments[0].scrollIntoView();", scroll_down)

    time.sleep(3)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//i[@class='pi pi-filter-fill'])[1]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(), 'Transaction Type')]"))
    ).click()

    time.sleep(2)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Select transactionTypeEnum')]"))
    ).click()

    select_sales = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='Sales'])[1]"))
    )
    login.execute_script("arguments[0].click();", select_sales)

    time.sleep(3)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='Apply'])[1]"))
    ).click()


    print("Applied filter for Transaction Type: Sales")

    # Assert the table only contains rows with Transaction Type as "Sales"
    time.sleep(3)
    table = wait.until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
    )
    rows = table.find_elements(By.XPATH, "//tbody/tr")

    for row in rows:
        transaction_type = row.find_element(By.XPATH, "./td[5]/span").text.strip()
        assert transaction_type == "SALES", f"Found non-SALES transaction type: {transaction_type}"

    print("Assertion passed: All rows in the table have Transaction Type as 'SALES'.")




