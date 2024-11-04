import pytest
from Framework.common_utils import *

# global bs_name, vendors_id, first_name, last_name, phonenumber, email
bs_name, vendors_id = create_business_detail()

first_name, last_name, phonenumber, email = create_users_data()
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Create Vendors")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_create_vendors(login):
    time.sleep(3)

    try:
       
        wait = WebDriverWait(login, 10)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Create Vendor']"))
        ).click()

        # bs_name, vendors_id = create_business_detail()
        # first_name, last_name, phonenumber, email = create_users_data()
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='vendorName']"))
        ).send_keys(str(bs_name))
        print(str(bs_name))
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='vendorID']"))
        ).send_keys(vendors_id)
        print(vendors_id)
        owner_name = first_name
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='ownerName']"))
        ).send_keys(first_name)
        print(first_name)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='phone']"))
        ).send_keys(phonenumber)
        print(phonenumber)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='email']"))
        ).send_keys(email)
        print(email)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='state']"))
        ).send_keys("Kerala")
        print("kerala")
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='pincode']"))
        ).send_keys("680505")
        print("680505")
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-button__label']"))
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

        time.sleep(5)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Create same Vendors with same vendor id")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_create_same_vendors(login):
    time.sleep(3)
    try:

        # global business_name, vendors_id, first_name, phonenumber, email
        # # bs_name, vendors_id = create_business_detail()
        # # first_name, last_name, phonenumber, email = create_users_data()
        
        wait = WebDriverWait(login, 10)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Create Vendor']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='vendorName']"))
        ).send_keys(str(bs_name))
        print(str(bs_name))
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='vendorID']"))
        ).send_keys(vendors_id)
        print(vendors_id)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='ownerName']"))
        ).send_keys(first_name)
        print(first_name)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='phone']"))
        ).send_keys(phonenumber)
        print(phonenumber)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='email']"))
        ).send_keys(email)
        print(email)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='state']"))
        ).send_keys("Kerala")
        print("kerala")
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='pincode']"))
        ).send_keys("680505")
        print("680505")
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-button__label']"))
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
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: ")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_(login):