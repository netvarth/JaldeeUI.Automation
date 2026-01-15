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

        wait_and_locate_click(
             login, By.XPATH, "(//img)[3]"
        )

        wait_and_locate_click(driver, By.XPATH, "(//div[@id='actionNav_ORD_Inventory'])[3]")
        
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
        dropdown = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//p-dropdown[@id='ddHSN_ORD_INV_ItemCreate']"))
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
        wait_and_locate_click(driver, By.XPATH, "//p-dropdown[@id='ddBatchApplicable_ORD_INV_ItemCreate']")

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Yes']")

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//button[@id='btnSubmit_ORD_INV_ItemCreate']")

        msg = get_toast_message(driver)
        print("Toast Message :", msg )

        time.sleep(3)

        wait_and_locate_click(driver, By.XPATH, "//*[@id='actionBack__ORD_Items']")

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//*[normalize-space()='B&B Stores']")
        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//*[@id='actionNav_ORD_Inventory'])[2]")

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//*[normalize-space()='Create Store']")

        time.sleep(2)
       
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//p-dropdown[@id='strType_ORD_storeCre']")
        )).click()

        options = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//ul[@role='listbox']//li[@role='option']")
        ))

        random.choice(options).click()


        store_name = "Store_" + str(uuid.uuid4())[:6]
        time.sleep(2)
        wait_and_send_keys(driver, By.XPATH, "//input[@placeholder='Name']", store_name)

        email = f"{store_name}{test_mail}"
        random_number = str(random.randint(1111111, 9999999))
        phonenumber = f"{555}{random_number}"
        time.sleep(2)
        wait_and_send_keys(driver, By.XPATH, "//input[@id='phone']", phonenumber)

        time.sleep(1)
        wait_and_send_keys(driver, By.XPATH, "//input[@id='email']", email)

        invoice_prefix = "KT_" + str(uuid.uuid4())[:6]
        print(invoice_prefix)

        wait_and_send_keys(driver, By.XPATH, "//input[@placeholder='Invoice prefix']", invoice_prefix)

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//p-dropdown[@placeholder='Location']")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='West Nada']")

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//button[normalize-space()='Create']")

        msg = get_snack_bar_message(driver)
        print("Snack Bar Message :", msg)

        time.sleep(2)
        
        wait_and_locate_click(
             login, By.XPATH, "//i[@class='fa fa-arrow-left']"
        )

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='Vendors']"))
        ).click()  

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Create Vendor']"))
        ).click()
        
        vendor_name = "vendor_"+ str(uuid.uuid4())[:4]

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='vendorName']"))
        ).send_keys(vendor_name)

        print("Vendor Name: ", vendor_name)

        vendor_id = "ven_id"+ str(uuid.uuid4())[:8]
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='inputId_FIN_VendorDet'])[1]"))
        ).send_keys(vendor_id)

        print("Vendor_ID : ", vendor_id)

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='ownerName'])[1]"))
        ).send_keys(first_name)
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='phone']"))
        ).send_keys(phonenumber)
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='inputEmail_FIN_VendorDet']"))
        ).send_keys(email)

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnSave_FIN_VendorDet']"))
        ).click()

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
             login, By.XPATH, "//span[@id='goback_FIN_Vendr']"
        )

        time.sleep(2)
        

    except Exception as e:
            allure.attach(  # use Allure package, .attach() method, pass 3 params
                login.get_screenshot_as_png(),  # param1
                # login.screenshot()
                name="full_page",  # param2
                attachment_type=AttachmentType.PNG,
            )
            raise e
       