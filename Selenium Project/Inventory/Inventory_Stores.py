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






@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
@allure.title("Store Creation")
def test_store_creation(login):
    try:
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
        ).click()

        time.sleep(5)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Stores']"))
        ).click()

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Store']"))
        ).click()                                   


        dropdown = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Type']"))  
        )
        dropdown.click() 

        time.sleep(2)
        dropdown_item = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Pharmacy']"))
        )

        dropdown_item.click()

        store_name = "Store_" + str(uuid.uuid4())[:6]
        print(store_name)
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


        invoice_prefix = "KT_" + str(uuid.uuid4())[:1]
        print(invoice_prefix)
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Invoice prefix']"))  
        ).send_keys(invoice_prefix)
        

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Location']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Chavakkad']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create']"))
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
        time.sleep(3)


    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
@allure.title("Store Filter Location")
def test_store_filter_location(login):

    try:

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
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
                (By.XPATH, "//span[normalize-space()='Round North']"))
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
            assert store_location == "Round North", f"Store location '{store_location}' does not match the filter 'Round North'"

            

    except Exception as e: 
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e 
    


@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
@allure.title("Store Filter_Status")
def test_store_filter_storestatus(login):

    try:

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
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
        )
          
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
    


