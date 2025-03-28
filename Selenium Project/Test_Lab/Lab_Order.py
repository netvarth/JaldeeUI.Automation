from Framework.common_utils import *
from Framework.common_dates_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Basic lab order work flow")
@pytest.mark.parametrize("url, username, password", [(test_url, test_user, password_1)])
def test_lab_order(login):

    try:
        
        time.sleep(5)
        wait = WebDriverWait(login, 30)

        order_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[3]"))
        )
        # login.refresh()
        login.execute_script("arguments[0].click();", order_element)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Create Order')])[1]"))
        ).click()
 
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        clinic_option = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='ASTRAL CLINIC'])[1]"))
        )
        clinic_option.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[6]"))
        ).click()

        delivery_type = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Home Delivery'])[1]"))
        )
        delivery_type.click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Next'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Add Item'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='mat-mdc-checkbox-4-input'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-check'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Confirm Order'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Complete Order'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Pass To Delivery'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@name='radioBtn'])[3]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Assign Agent'])[1]"))
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

        Assigned_status_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='ASSIGNED'])[1]"))
        )
        Assigned_status_text = Assigned_status_element.text
        print(f"Status: {Assigned_status_text}")
        assert Assigned_status_text == "ASSIGNED", f"Expected 'ASSIGNED' status, but got {Assigned_status_text}"

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Change Status'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='mdc-list-item__primary-text'][normalize-space()='Accepted'])[1]"))
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

        Accepted_status_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='ACCEPTED'])[1]"))
        )
        Accepted_status_text = Accepted_status_element.text
        print(f"Status: {Accepted_status_text}")
        assert Accepted_status_text == "ACCEPTED", f"Expected 'ACCEPTED' status, but got {Accepted_status_text}"

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Change Status'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[1]"))
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

        pickup_status_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='PICK UP'])[1]"))
        )
        pickup_status_text = pickup_status_element.text
        print(f"Status: {pickup_status_text}")
        assert pickup_status_text == "PICK UP", f"Expected 'PICK UP' status, but got {pickup_status_text}"

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Change Status'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[1]"))
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

        In_Transist_status_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='IN TRANSIST'])[1]"))
        )
        In_Transist_status_text = In_Transist_status_element.text
        print(f"Status: {In_Transist_status_text}")
        assert In_Transist_status_text == "IN TRANSIST", f"Expected 'IN TRANSIST' status, but got {In_Transist_status_text}"

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Change Status'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[1]"))
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
        
        delivered_status_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='DELIVERED'])[1]"))
        )
        delivered_status_text = delivered_status_element.text
        print(f"Status: {delivered_status_text}")
        assert delivered_status_text == "DELIVERED", f"Expected 'DELIVERED' status, but got {delivered_status_text}"


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
@allure.title("Test Case: Create Clinic")
@pytest.mark.parametrize("url, username, password", [(test_url, test_user, password_1)])
def test_lab_order_1(login):


    try:
        
        wait = WebDriverWait(login, 20)
        order_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[3]"))
        )
        order_element.click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Clinics')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-plus'])[1]"))
        ).click()

        Clinic_Name = "Clinicname" + str(uuid.uuid4())[:4]
        Clinic_Nickname = "ClinicNickname" + str(uuid.uuid4())[:4]

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Clinic Name'])[1]"))
        ).send_keys(Clinic_Name)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Clinic Alias Name'])[1]"))
        ).send_keys(Clinic_Nickname)

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        fake_india= Faker('en_IN')
        fake_india_address= fake_india.address()
        print(fake_india_address)


    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

