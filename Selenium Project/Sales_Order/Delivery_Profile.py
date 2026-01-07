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


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create Delivery Profile from Sales Order Module")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_delivery_profile(login):
    try:
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//img)[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH,  
                              "(//div[@id='actionRouteTo_ORD_Dashbrd'])[10]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//p-button[@id='btnCretDprofile_ORD_DProfille'])[1]")
        
        delivery_profile = "Delivery_Profile" + str(uuid.uuid4())[:6]
        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, 
                              "(//input[@id='inputDPName_ORD_CreateDP'])[1]", delivery_profile)
        

        minimum_amount = WebDriverWait(login, 20).until(
                EC.presence_of_element_located((By.XPATH,
                                                "(//input[@type='number'])[1]"))
            )
        minimum_amount.click()
        minimum_amount.clear()
        minimum_amount_random_number = str(random.randint(150, 299))  # Setting MRP
        minimum_amount.send_keys(minimum_amount_random_number)
        print("minimum amount of the item:",minimum_amount_random_number)

        time.sleep(2)

        maximum_amount = WebDriverWait(login, 20).until(
                EC.presence_of_element_located((By.XPATH,
                                                "(//input[@type='number'])[2]"))
            )
        maximum_amount.click()
        maximum_amount.clear()
        maximum_amount_random_number = str(random.randint(300, 599))  # Setting MRP
        maximum_amount.send_keys(maximum_amount_random_number)
        print("minimum amount of the item:",maximum_amount_random_number)

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@type='number'])[3]", "35")

        
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnAdPrice_ORD_CreateDP']")


        minimum_amount = WebDriverWait(login, 20).until(
                EC.presence_of_element_located((By.XPATH,
                                                "(//input[@type='number'])[4]"))
            )
        minimum_amount.click()
        minimum_amount.clear()
        minimum_amount_random_number = str(random.randint(600, 999))  # Setting MRP
        minimum_amount.send_keys(minimum_amount_random_number)
        print("minimum amount of the item:",minimum_amount_random_number)

        time.sleep(2)

        maximum_amount = WebDriverWait(login, 20).until(
                EC.presence_of_element_located((By.XPATH,
                                                "(//input[@type='number'])[5]"))
            )
        maximum_amount.click()
        maximum_amount.clear()
        maximum_amount_random_number = str(random.randint(1000, 1499))  # Setting MRP
        maximum_amount.send_keys(maximum_amount_random_number)
        print("maximum amount of the item:",maximum_amount_random_number)

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@type='number'])[6]", "15")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnCreate_ORD_CreateDP']")

        msg = get_snack_bar_message(login)
        print("Toast Message :",msg)

        time.sleep(3)


    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create the Delivery Profile with Empty Fields")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_delivery_profile_with_empty_fields(login):
    try:
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//img)[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//div[@id='actionRouteTo_ORD_Dashbrd'])[10]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//p-button[@id='btnCretDprofile_ORD_DProfille'])[1]")
        
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnCreate_ORD_CreateDP']")

        msg = get_snack_bar_message(login)
        print("Snack bar Message :", msg)

        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create a Delivery Profile with Empty Price Range")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_delivery_profile_with_empty_price_range(login):
    try:
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//img)[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//div[@id='actionRouteTo_ORD_Dashbrd'])[10]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//p-button[@id='btnCretDprofile_ORD_DProfille'])[1]")
        
        delivery_profile = "Delivery_Profile" + str(uuid.uuid4())[:6]
        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, 
                              "(//input[@id='inputDPName_ORD_CreateDP'])[1]", delivery_profile)
        
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnCreate_ORD_CreateDP']")

        msg = get_snack_bar_message(login, timeout=5)
        print("Snack bar Message :", msg)

        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Edit delivery profile and Update")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_edit_delivery_profile_and_update(login):
    try:
        wait = WebDriverWait(login, 10)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//img)[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//*[contains(text(),'Delivery Profile')])[1]")

        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//button[@type='submit'][normalize-space()='View'])[2]")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='fa fa-pencil'])[1]")

        time.sleep(2)
    
        delivery_charge = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//input[@type='number'])[3]"))
        )
        delivery_charge.clear()
        delivery_charge.send_keys("40")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//*[normalize-space()='Update']")

        msg = get_snack_bar_message(login)
        print("Snack bar Message :", msg)

        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Assign delivery profile to the store")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_assign_delivery_profile_to_store(login):
    try:
        wait = WebDriverWait(login, 10)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//img)[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//*[contains(text(),'Delivery Profile')])[1]")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[contains(text(),'Assign')])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@aria-label='dropdown trigger'])[2]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='B&B Stores'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//div[@aria-label='dropdown trigger'])[3]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Home Delivery'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Save'])[1]")

        msg = get_snack_bar_message(login)
        print("Snack bar Message :", msg)

        time.sleep(2)
        
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Assign delivery profile to the store from detail page")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_assign_delivery_profile_to_store_from_detail_page(login):
    try:
        wait = WebDriverWait(login, 10)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//img)[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//*[contains(text(),'Delivery Profile')])[1]")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@type='submit'][normalize-space()='View'])[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[contains(text(),'Assign')])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@aria-label='dropdown trigger'])[2]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='B&B Stores'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//div[@aria-label='dropdown trigger'])[3]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Store Pickup'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Save'])[1]")

        msg = get_snack_bar_message(login)
        print("Snack bar Message :", msg)

        time.sleep(2)
        
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e