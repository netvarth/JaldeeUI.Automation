import random
import time
import uuid
import allure
import pytest

from Framework.common_utils import *




@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Vendors Creation")
def test_vendor_creation(login):

    try:

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[3]"))
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
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e 