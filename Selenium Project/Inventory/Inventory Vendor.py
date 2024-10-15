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
@allure.title("Vendors Creation")
def test_vendor_creation(login):

    try:

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
        ).click()

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
                (By.XPATH, "//input[@id='vendorID']"))
        ).send_keys(vendor_id)

        print("Vendor_ID : ", vendor_id)

        



    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e 