import time
import uuid

from pyautogui import click

from Framework.common_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Framework.common_dates_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Stock Ajustment")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_stock_adjustment(login):
    time.sleep(3)
    wait = WebDriverWait(login, 20)

    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "overlay")))

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Inv.Adjust')]"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Create']"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//p-dropdown[@placeholder='Select Store']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']"))
    ).click()

    element_geetha = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[normalize-space()='Geetha']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", element_geetha)

    element_geetha.click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//p-dropdown[@placeholder='Select Catalog']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']"))
    ).click()

    element_invcatalog = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[normalize-space()='Inventory_catalog']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", element_invcatalog)
    element_invcatalog.click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//p-dropdown[@placeholder='Select Remark']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Adjustment']"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Add Items']"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//input[@type='checkbox'])[5]"))
    ).click()


    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[2]"))
    ).click()

    

    time.sleep(3)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='fw-bold shadow p-1 pointer-cursor ng-star-inserted'])[1]"))
    ).click()


    # Capture the initial stock before adding the quantity
    initial_stock_element = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Item3')]/ancestor::tr/td[contains(@class, 'fw-bold')]")
        )
    )

    initial_stock = int(initial_stock_element.text.strip())
    print(f"Initial stock: {initial_stock}")


    time.sleep(3)
    qty_element = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@type='number']"))
    )
    qty_element.clear()
    qty_element.send_keys("10")  

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Save']"))
    ).click()
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Yes']"))
    ).click()

    toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_detail.text
    print("toast_Message:", message)

    time.sleep(3)
    # Wait for the table to be present
    table_body = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
    )

    # Locate the first table row
    first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")

    # Find the status element within the first row
    status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
    status_text = status_element.text
    expected_status = "DRAFT"

    print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

    # Assert that the status is "IN REVIEW"
    assert status_text == "DRAFT", f"Expected status to be 'DRAFT', but got '{status_text}'"

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='Update'])[1]"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Submit']"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Yes']"))
    ).click()

    toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_detail.text
    print("toast_Message:", message)

    time.sleep(3)
    # Wait for the table to be present
    table_body = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
    )

    # Locate the first table row
    first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")

    # Find the status element within the first row
    status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
    status_text = status_element.text
    expected_status = "SUBMITTED"

    print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

    # Assert that the status is "IN REVIEW"
    assert status_text == "SUBMITTED", f"Expected status to be 'SUBMITTED', but got '{status_text}'"

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]"))
    ).click()

    time.sleep(3)

    click_approve = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Approve']"))
    )
    try:
        click_approve.click()
    except:
        login.execute_script("arguments[0].click();", click_approve)
    
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Yes']"))
    ).click()

    toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_detail.text
    print("toast_Message:", message)
    

    time.sleep(3)
    # Wait for the table to be present
    table_body = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
    )

    # Locate the first table row
    first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")

    # Find the status element within the first row
    status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
    status_text = status_element.text
    expected_status = "PROCESSED"

    print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

    # Assert that the status is "IN REVIEW"
    assert status_text == "PROCESSED", f"Expected status to be 'PROCESSED', but got '{status_text}'"

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='fw-bold card shadow p-1 pointer-cursor'])[1]"))
    ).click()


    # Click to see the current stock
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//td[@class='fw-bold'])[1]"))
    ).click()

    # Capture the updated stock after clicking "View"
    updated_stock_element = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Item3')]/ancestor::tr/td[contains(@class, 'fw-bold')]")
        )
    )
    updated_stock = int(updated_stock_element.text.strip())
    print(f"Updated stock: {updated_stock}")

     # Calculate the expected stock after adding 10
    expected_stock = initial_stock + 10

    # Assert that the stock increased correctly
    assert updated_stock == expected_stock, f"Expected stock to be {expected_stock}, but got {updated_stock}"
    print(f"Stock updated successfully: {updated_stock}")

    
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//i[@class='pi pi-arrow-left']"))
    ).click() 

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//i[@class='pi pi-arrow-left']"))
    ).click()



    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[contains(text(),'Stocks')])[1]"))
    ).click()

    time.sleep(3)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    element_geetha = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[normalize-space()='Geetha']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", element_geetha)

    element_geetha.click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
    ).click()

    element_invcatalog = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[normalize-space()='Inventory_catalog']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", element_invcatalog)
    element_invcatalog.click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Search items']"))
    ).send_keys("item")

    click_item = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Item3')]"))
    )

    try:
        click_item.click()
    except:
        login.execute_script("arguments[0].click();", click_item)


    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Check Stock']"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='Batch Wise Stock'])[1]"))
    ).click()

    

    # Capture the updated stock after clicking "View"
    updated_stock_element = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//tr[td[1]//div[contains(text(),'69')]]/td[3]//div[contains(@class, 'text-nowrap')]")
        )
    )
    updated_stock = int(updated_stock_element.text.strip())
    print(f"Updated stock: {updated_stock}")

     # Calculate the expected stock after adding 10
    expected_stock = initial_stock + 10

    # Assert that the stock increased correctly
    assert updated_stock == expected_stock, f"Expected stock to be {expected_stock}, but got {updated_stock}"
    print(f"Stock updated successfully: {updated_stock}")

#####################################################################################################################################################
    
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Stock adjustment with Batch disable Item")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_stock_adjustment_1(login):

    time.sleep(5)
    wait = WebDriverWait(login, 10)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
    ).click()

    time.sleep(3)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Inv.Adjust')]"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Create']"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//p-dropdown[@placeholder='Select Store']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']"))
    ).click()

    element_geetha = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[normalize-space()='Geetha']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", element_geetha)

    element_geetha.click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//p-dropdown[@placeholder='Select Catalog']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']"))
    ).click()

    element_invcatalog = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[normalize-space()='Inventory_catalog']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", element_invcatalog)
    element_invcatalog.click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//p-dropdown[@placeholder='Select Remark']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Adjustment']"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Add Items']"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//input[@type='checkbox'])[2]"))
    ).click()


    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[2]"))
    ).click()
    time.sleep(3)

    # wait.until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "(//span[@class='fw-bold shadow p-1 pointer-cursor ng-star-inserted'])[1]"))
    # ).click()


    # # Capture the initial stock before adding the quantity
    # initial_stock_element = wait.until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "//div[contains(text(),'Item_batchdisable')]/ancestor::tr/td[contains(@class, 'fw-bold')]")
    #     )
    # )

    # print(initial_stock_element.text)
    # initial_stock = int(initial_stock_element.text.strip())
    # print(f"Initial stock: {initial_stock}")


    # time.sleep(3)
    # qty_element = wait.until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "//input[@type='number']"))
    # )
    # qty_element.clear()
    # qty_element.send_keys("10")
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//td[@class='fw-bold']//div[@class='ng-star-inserted']"))
    ).click()
    time.sleep(1)
    # Capture the initial stock before adding the quantity
    initial_stock_element = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Item_batchdisable')]/ancestor::tr/td[contains(@class, 'fw-bold')]")
        )
    )
    initial_stock = int(initial_stock_element.text.strip())
    print(f"Initial stock: {initial_stock}")


    time.sleep(3)
    qty_element = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@type='number']"))
    )
    qty_element.clear()
    qty_element.send_keys("10")  

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Save']"))
    ).click()
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Yes']"))
    ).click()

    toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_detail.text
    print("toast_Message:", message)

    time.sleep(3)
    # Wait for the table to be present
    table_body = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
    )

    # Locate the first table row
    first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")

    # Find the status element within the first row
    status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
    status_text = status_element.text
    expected_status = "DRAFT"

    print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

    # Assert that the status is "IN REVIEW"
    assert status_text == "DRAFT", f"Expected status to be 'DRAFT', but got '{status_text}'"

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='Update'])[1]"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Submit']"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Yes']"))
    ).click()

    toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_detail.text
    print("toast_Message:", message)

    time.sleep(3)
    # Wait for the table to be present
    table_body = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
    )

    # Locate the first table row
    first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")

    # Find the status element within the first row
    status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
    status_text = status_element.text
    expected_status = "SUBMITTED"

    print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

    # Assert that the status is "IN REVIEW"
    assert status_text == "SUBMITTED", f"Expected status to be 'SUBMITTED', but got '{status_text}'"

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]"))
    ).click()

    time.sleep(3)

    click_approve = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Approve']"))
    )
    try:
        click_approve.click()
    except:
        login.execute_script("arguments[0].click();", click_approve)
    
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Yes']"))
    ).click()

    toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_detail.text
    print("toast_Message:", message)
    

    time.sleep(3)
    # Wait for the table to be present
    table_body = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
    )

    # Locate the first table row
    first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")

    # Find the status element within the first row
    status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
    status_text = status_element.text
    expected_status = "PROCESSED"

    print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

    # Assert that the status is "IN REVIEW"
    assert status_text == "PROCESSED", f"Expected status to be 'PROCESSED', but got '{status_text}'"

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='fw-bold card shadow p-1 pointer-cursor'])[1]"))
    ).click()


    # Click to see the current stock
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//td[@class='fw-bold'])[1]"))
    ).click()

    # Capture the updated stock after clicking "View"
    updated_stock_element = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Item_batchdisable')]/ancestor::tr/td[contains(@class, 'fw-bold')]")
        )
    )
    updated_stock = int(updated_stock_element.text.strip())
    print(f"Updated stock: {updated_stock}")

     # Calculate the expected stock after adding 10
    expected_stock = initial_stock + 10

    # Assert that the stock increased correctly
    assert updated_stock == expected_stock, f"Expected stock to be {expected_stock}, but got {updated_stock}"
    print(f"Stock updated successfully: {updated_stock}")


    
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//i[@class='pi pi-arrow-left']"))
    ).click() 

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//i[@class='pi pi-arrow-left']"))
    ).click()



    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[contains(text(),'Stocks')])[1]"))
    ).click()

    time.sleep(3)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    element_geetha = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[normalize-space()='Geetha']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", element_geetha)

    element_geetha.click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
    ).click()

    element_invcatalog = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[normalize-space()='Inventory_catalog']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", element_invcatalog)
    element_invcatalog.click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Search items']"))
    ).send_keys("item")

    click_item = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Item_batchdisable')]"))
    )

    try:
        click_item.click()
    except:
        login.execute_script("arguments[0].click();", click_item)


    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Check Stock']"))
    ).click()

    time.sleep(2)
# Capture the updated stock after clicking "View"
    updated_stock_element = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//tbody/tr[@class='ng-star-inserted']/td[2]/div[1]")
        )
    )
    updated_stock = int(updated_stock_element.text.strip())
    print(f"Updated stock: {updated_stock}")

     # Calculate the expected stock after adding 10
    expected_stock = initial_stock + 10

    # Assert that the stock increased correctly
    assert updated_stock == expected_stock, f"Expected stock to be {expected_stock}, but got {updated_stock}"
    print(f"Stock updated successfully: {updated_stock}")
    
