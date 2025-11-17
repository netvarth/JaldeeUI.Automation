import time
import allure
import sys
import os
import allure
import pytest
from ast import arguments
from tkinter import Label
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Framework.common_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
from selenium.webdriver.common.action_chains import ActionChains




@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Inventory Pre deployment testing")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_Inventory_work_flow(login): 
    current_date = datetime.now().strftime("%Y-%m-%d")
    print("Pre-Deployment Inventory : ",current_date)
    try:
        time.sleep(5)
        driver = login
        wait = WebDriverWait(driver, 30)
        wait_and_locate_click(driver, By.XPATH, "(//div[@id= 'actionRouteTo_ORD_Dashbrd'])[5]")
        
        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//button[@id='btnCrtItem_ORD_Items']")

        item_name = "Item_" + str(uuid.uuid4())[:4] 

        time.sleep(3)
        name_element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='inpItemName_ORD_INV_ItemCreate']")))
        name_element.click()
        time.sleep(2)
        name_element.send_keys(item_name)

        time.sleep(2)
        wait_and_send_keys(driver, By.XPATH, "//textarea[@id='txtaShortDesc_ORD_INV_ItemCreate']", "A Item name is required and recommended to be unique.")

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//p-dropdown[@id='ddCategory_ORD_INV_ItemCreate']")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='Stationary']")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//p-multiselect[@id='msGroup_ORD_INV_ItemCreate']")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='Stationary_Item']")

        time.sleep(1)
        wait_and_locate_click(driver,By.XPATH, "//p-dropdown[@id='ddType_ORD_INV_ItemCreate']")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//li[@aria-label='Office_Item']")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//p-dropdown[@id='ddManufacturer_ORD_INV_ItemCreate']")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='SC.PVT.Limited']")

        time.sleep(1)
        dropdown = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//p-multiselect[@id='msUnits_ORD_INV_ItemCreate']"))
        )
        dropdown.click()

        time.sleep(2)
        options = dropdown.find_elements(By.XPATH, "//ul[@role='listbox']")

        # Select a random option
        if options:
            random_option = random.choice(options)
            random_option.click()
        else:
            print("No options found in the dropdown.")

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//p-dropdown[@id='ddHSN_ORD_INV_ItemCreate']")

        time.sleep(1)
        dropdown = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//p-dropdown[@id='ddHSN_ORD_INV_ItemCreate']"))
        )
        dropdown.click()

        time.sleep(2)
        options = dropdown.find_elements(By.XPATH, "//div[@class='p-dropdown-panel p-component ng-star-inserted']")

        # Select a random option
        if options:
            random_option = random.choice(options)
            random_option.click()
        else:
            print("No options found in the dropdown.")

            time.sleep(2)

    except Exception as e:
            allure.attach(  # use Allure package, .attach() method, pass 3 params
                login.get_screenshot_as_png(),  # param1
                # login.screenshot()
                name="full_page",  # param2
                attachment_type=AttachmentType.PNG,
            )
            raise e
       