import time
import uuid

from Framework.common_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Framework.common_dates_utils import *


@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Inventory Stock Transfer")
def test_stock_transfer(login):
    driver = login
    try:
        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "(//img)[3]" 
        )

        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionNav_ORD_Inventory'])[8]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCreateTrf_ORD_StockTtans']"
        )

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='selectStore_ORD_StKTrafCrt']"
        )

        element_scroll = driver.find_element(By.XPATH, "(//span[normalize-space()='B&B Stores'])[1]")
        scroll_to_element(driver, element_scroll)
        element_scroll.click()

        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='selectCat_ORD_StKTrafCrt']"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//span[normalize-space()='Catalog_Inventory']"
        )

        time.sleep(1)

        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='selectDstore_ORD_StKTrafCrt']"
        )

        element_scroll_1 = login.find_element(By.XPATH, "//span[normalize-space()='B&B Store 2']")
        scroll_to_element(driver, element_scroll_1)
        element_scroll_1.click()

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='selectDCat_ORD_StKTrafCrt']"
        )

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "//span[normalize-space()='Catalog_Inventory_2']"
        )

        time.sleep(2)
        wait_and_send_keys(
            driver, By.XPATH, "(//input[@placeholder='Search items'])[1]", "item"
        )

        

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Item_8')])[1]"))
        ).click()

        

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='selectBatch_ORD_StKTrafCrt']"
        )
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='501'])[1]")

        qty= driver.find_element(By.XPATH, "//input[@id='InputQty_ORD_StKTrafCrt']")

        qty.click()
        qty.clear()
        qty.send_keys("10")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnUpdtItem_ORD_StKTrafCrt']"))
        ).click()

        time.sleep(1)

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCrtStkTtran_ORD_StKTrafCrt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)


        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnDispth_ORD_StKView']"))
        ).click()
        
        msg = get_snack_bar_message(driver)
        print("Snack Bar MEssage :", msg)
        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(3)
        store = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]"))
        )
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
                (By.XPATH, "//span[normalize-space()='B&B Store 2']"))
        )
        store1.click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnshStatus_ORD_StKTrafList']"))
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnViewStk_ORD_StKTrafList'])[1]"))
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnRcvd_ORD_StKView']"))
        ).click()

        msg = get_snack_bar_message(driver)
        print("Snack Bar Message :", msg)

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

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e
    



@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Draft stock transfer and Update")
def test_stock_transfer_1(login):
    driver = login
    try:
        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "(//img)[3]" 
        )

        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionNav_ORD_Inventory'])[8]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCreateTrf_ORD_StockTtans']"
        )

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='selectStore_ORD_StKTrafCrt']"
        )

        element_scroll = driver.find_element(By.XPATH, "(//span[normalize-space()='B&B Stores'])[1]")
        scroll_to_element(driver, element_scroll)
        element_scroll.click()

        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='selectCat_ORD_StKTrafCrt']"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//span[normalize-space()='Catalog_Inventory']"
        )

        time.sleep(1)

        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='selectDstore_ORD_StKTrafCrt']"
        )

        element_scroll_1 = login.find_element(By.XPATH, "//span[normalize-space()='B&B Store 2']")
        scroll_to_element(driver, element_scroll_1)
        element_scroll_1.click()

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='selectDCat_ORD_StKTrafCrt']"
        )

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "//span[normalize-space()='Catalog_Inventory_2']"
        )

        time.sleep(2)
        wait_and_send_keys(
            driver, By.XPATH, "(//input[@placeholder='Search items'])[1]", "item"
        )

        

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Item_8')])[1]"))
        ).click()

        

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='selectBatch_ORD_StKTrafCrt']"
        )
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='501'])[1]")

        qty= driver.find_element(By.XPATH, "//input[@id='InputQty_ORD_StKTrafCrt']")

        qty.click()
        qty.clear()
        qty.send_keys("10")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnUpdtItem_ORD_StKTrafCrt']"))
        ).click()

        time.sleep(1)

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCrtStkTtran_ORD_StKTrafCrt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//div[@id='actionBack_ORD_StKView']"
        )

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

        # Assert that the status is "DRAFT"
        assert status_text == "DRAFT", f"Expected status to be 'DRAFT', but got '{status_text}'"

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnEdtStk_ORD_StKTrafList'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCrtStkTtran_ORD_StKTrafCrt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']"
        )

        store_element = driver.find_element(By.XPATH, "//li[@aria-label='B&B Store 2']")
        scroll_to_element(driver, store_element)
        store_element.click()

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnshStatus_ORD_StKTrafList']"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnViewStk_ORD_StKTrafList'])[1]"
        )


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

        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e