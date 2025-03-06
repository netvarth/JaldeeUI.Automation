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
                (By.XPATH, "//input[@id='vendorID']"))
        ).send_keys(vendor_id)

        print("Vendor_ID : ", vendor_id)

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='ownerName']"))
        ).send_keys(first_name)
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='phone']"))
        ).send_keys(phonenumber)
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='email']"))
        ).send_keys(email)

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='mdc-button__label'])[1]"))
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

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e 