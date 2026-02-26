import random
import time
import uuid

import allure
import pytest

from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException



@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Store Creation")
def test_store_creation(login):
    try:
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[2]"))
        ).click()

        time.sleep(5)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[normalize-space()='Stores']"))
        ).click()

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='Create Store']"))
        ).click()                                   


        dropdown = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[normalize-space()='Type']"))  
        )
        dropdown.click() 

        time.sleep(2)
        dropdown_item = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[normalize-space()='OTHERS']"))
        )

        dropdown_item.click()

        store_name = "Store_" + str(uuid.uuid4())[:6]
        print("Store Nmae : ", store_name)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='storeName']"))
        ).send_keys(store_name)

        email = f"{store_name}{test_mail}"
        random_number = str(random.randint(1111111, 9999999))
        phonenumber = f"{555}{random_number}"

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        ).send_keys(phonenumber)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
        ).send_keys(email)


        invoice_prefix = "KT_" + str(uuid.uuid4())[:6]
        print(invoice_prefix)
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Invoice prefix']"))  
        ).send_keys(invoice_prefix)
        

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Location']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[normalize-space()='West Nada'])[1]"))
        ).click()

        create_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create']"))
        )
        login.execute_script("arguments[0].click();", create_button)

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
        time.sleep(3)


    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e

@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@pytest.mark.xfail(reason="Create button incorrectly enabled without selecting Location")
@allure.title("Store Creation without location")
def test_store_creation_without_location(login):
    try:
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[2]"))
        ).click()

        time.sleep(5)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[normalize-space()='Stores']"))
        ).click()

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='Create Store']"))
        ).click()                                   


        dropdown = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[normalize-space()='Type']"))  
        )
        dropdown.click() 

        time.sleep(2)
        dropdown_item = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[normalize-space()='OTHERS']"))
        )

        dropdown_item.click()

        store_name = "Store_" + str(uuid.uuid4())[:6]
        print("Store Nmae : ", store_name)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='storeName']"))
        ).send_keys(store_name)

        email = f"{store_name}{test_mail}"
        random_number = str(random.randint(1111111, 9999999))
        phonenumber = f"{555}{random_number}"

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        ).send_keys(phonenumber)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
        ).send_keys(email)


        invoice_prefix = "KT_" + str(uuid.uuid4())[:6]
        print(invoice_prefix)
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Invoice prefix']"))  
        ).send_keys(invoice_prefix)
        
         # Assert Create button is still disabled
        create_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create']"))
        )
        is_disabled_after = create_button.get_attribute("disabled")
        btn_class_after = create_button.get_attribute("class")

        assert (is_disabled_after is not None) or ("p-disabled" in btn_class_after), \
            "❌ Create button is enabled even though Type was not selected!"
        print("✅ Create button remained disabled when mandatory field 'Type' was skipped")                                   




    except Exception as e: 
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e 
    
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@pytest.mark.xfail(reason="Create button incorrectly enabled without selecting Type")
@allure.title("Store Creation without Type")
def test_store_creation_without_type(login):
    try:
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//img)[2]"))
        ).click()

        time.sleep(5)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Stores']"))
        ).click()

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Store']"))
        ).click()

        time.sleep(2)
        store_name = "Store_" + str(uuid.uuid4())[:6]
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='storeName']"))
        ).send_keys(store_name)

        time.sleep(2)
        email = f"{store_name}{test_mail}"
        random_number = str(random.randint(1111111, 9999999))
        phonenumber = f"{555}{random_number}"

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        ).send_keys(phonenumber)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
        ).send_keys(email)

        invoice_prefix = "KT_" + str(uuid.uuid4())[:6]
        print(invoice_prefix)
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Invoice prefix']"))  
        ).send_keys(invoice_prefix)

        time.sleep(2)
        # Select Location
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Location']"))
        ).click()
        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[normalize-space()='West Nada'])[1]"))
        ).click()

        time.sleep(2)

        # Assert Create button is still disabled
        create_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create']"))
        )
        is_disabled_after = create_button.get_attribute("disabled")
        btn_class_after = create_button.get_attribute("class")

        assert (is_disabled_after is not None) or ("p-disabled" in btn_class_after), \
            "❌ Create button is enabled even though Type was not selected!"
        print("✅ Create button remained disabled when mandatory field 'Type' was skipped")                                   




    except Exception as e: 
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e

@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Update the store name")
def test_rename_store(login):
    try:
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//img)[2]"))
        ).click()

        time.sleep(5)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Stores']"))
        ).click()

        time.sleep(2)
        # Click on Edit for the first store
        wait_and_click(login, By.XPATH, "(//span[@class='p-button-label ng-star-inserted'][normalize-space()='Edit'])[1]")

        time.sleep(2)

        # Locate store name field
        store_name_input = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='storeName']"))
        )

        # Clear old name
        store_name_input.clear()

        # Enter new store name
        new_store_name = "Renamed_" + str(uuid.uuid4())[:6]
        store_name_input.send_keys(new_store_name)
        print("New Store Name:", new_store_name)

        time.sleep(2)

        # Click Update button
        update_button = WebDriverWait(login, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']"))
        )
        login.execute_script("arguments[0].click();", update_button)

        # Validate snackbar message
        try:
            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
            )
            message = snack_bar.text
            print("✅ Snackbar (success):", message)

        except:
            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            print("❌ Snackbar (error):", message)

        time.sleep(3)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Disable and Enable the Store")
def test_store_disable_enable(login):
    try:
        wait = WebDriverWait(login, 15)

        # Step 1: Go to Store module
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//img)[2]"))).click()

        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[normalize-space()='Stores']"))).click()

        # Step 2: Click "View" for the first store
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[normalize-space()='View'])[1]"))).click()

        # Step 3: Disable the store (if active)
        time.sleep(2)
        disable_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='p-button-label ng-star-inserted'])[1]")))
        disable_text = disable_btn.text.strip()

        if disable_text.lower() == "disable":
            disable_btn.click()
            print("Action: Store Disabled")
        else:
            print("Store already disabled, skipping disable action.")

        # Capture snack bar message after disable
        msg = get_snack_bar_message(login)
        print("Snack Bar Message:", msg)

        # Step 4: Go back to Store list
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))).click()

        # Step 5: Verify store status is Inactive
        time.sleep(3)
        status = wait.until(EC.presence_of_element_located((By.XPATH, "(//tbody//tr[1]//td)[4]//div"))).text.strip()
        print(f"Store Status after Disable: {status}")
        assert status == "Inactive", f"Expected Inactive, but got {status}"

        # Step 6: Enable the store again
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[normalize-space()='View'])[1]"))).click()

        time.sleep(2)
        enable_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='p-button-label ng-star-inserted'])[1]")))
        enable_text = enable_btn.text.strip()

        if enable_text.lower() == "enable":
            enable_btn.click()
            print("Action: Store Enabled")
        else:
            print("Store already enabled, skipping enable action.")

        # Capture snack bar message after enable
        msg = get_snack_bar_message(login)
        print("Snack Bar Message:", msg)

        # Step 7: Go back and verify store is Active
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))).click()

        time.sleep(3)
        final_status = wait.until(EC.presence_of_element_located((By.XPATH, "(//tbody//tr[1]//td)[4]//div"))).text.strip()
        print(f"Store Status after Enable: {final_status}")
        assert final_status == "Active", f"Expected Active, but got {final_status}"
        
        time.sleep(3)
    except Exception as e:
        # Capture full-page screenshot only if something fails
        allure.attach(login.get_screenshot_as_png(), name="Error_Screenshot", attachment_type=AttachmentType.PNG)
        raise e
   
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Store Filter Location")
def test_store_filter_location(login):

    try:

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[2]"))
        ).click()

        time.sleep(5)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Stores']"))
        ).click()

        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//i[@class='pi pi-filter-fill']"))
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Location']"))
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='West Nada'])[1]"))
        ).click()    


        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Apply']"))
        ).click()

        # Wait for the table to load after applying the filter
        time.sleep(5)

        # Locate the table body containing the filtered results
        table_body = WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//tbody")
            )
        )

        # Get all rows in the table
        table_rows = table_body.find_elements(By.XPATH, ".//tr")

        # Check if all store locations in the rows match the filter 'Round North'
        for row in table_rows:
            # Locate the cell containing the store location (adjust column index based on actual table structure)
            store_location = row.find_element(By.XPATH, "//tbody/tr/td[@class='desktop-only'][1]").text
            
            # Assert that the store location is 'Round North'
            assert store_location == "West Nada", f"Store location '{store_location}' does not match the filter 'West Nada'"

            

    except Exception as e: 
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e 
    
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Store Filter_Status")
def test_store_filter_storestatus(login):

    try:

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[2]"))
        ).click()

        time.sleep(5)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Stores']"))
        ).click()

        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//i[@class='pi pi-filter-fill']"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Status']"))
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(3)   
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Active']"))
        ).click()
          
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Apply']"))
        ).click()

        # Wait for the table to load after applying the filter
        time.sleep(5)

        # Locate the table body containing the filtered results
        table_body = WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//tbody")
            )
        )

        # Get all rows in the table
        table_rows = table_body.find_elements(By.XPATH, ".//tr")

        # Check if all store status
        for row in table_rows:
            # Locate the cell containing the store location (adjust column index based on actual table structure)
            store_status = row.find_element(By.XPATH, "//tbody/tr/td[@class='desktop-only'][3]").text
            
            # Assert that the store status
            assert store_status == "Active", f"Store Status '{store_status}' does not match the filter 'Active'"

        

        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//i[@class='pi pi-filter-fill']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()


        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Inactive']"))
        ).click()


        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Apply']"))
        ).click()

        # Wait for the table to load after applying the filter
        time.sleep(3)

        # Locate the table body containing the filtered results
        table_body = WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//tbody")
            )
        )

        # Get all rows in the table
        table_rows = table_body.find_elements(By.XPATH, ".//tr")

        # Check if all store status
        for row in table_rows:
            # Locate the cell containing the store location (adjust column index based on actual table structure)
            store_status = row.find_element(By.XPATH, "//tbody/tr/td[@class='desktop-only'][3]").text
            
            # Assert that the store status
            assert store_status == "Inactive", f"Store Status '{store_status}' does not match the filter 'Inactive'"

        print ("test result")
    except Exception as e: 
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e 
    



