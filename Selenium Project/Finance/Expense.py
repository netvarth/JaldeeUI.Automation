import pytest
from Framework.common_utils import *




@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Create Expense")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_create_expense(login):
    time.sleep(3)
    try:
       
        wait = WebDriverWait(login, 10)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Create Expense']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@aria-label='dropdown trigger'])[1]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Purchase']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Chavakkad']"))
        ).click()

        login.find_element(By.XPATH, "//input[@id='expenseFor']").send_keys("Office Expense")

        Refer_no = "".join(random.choices(string.ascii_letters + string.digits, k=3))
        login.find_element(By.XPATH, "//input[@id='referenceNo']").send_keys(Refer_no)

        random_amount = str(random.randint(100, 999))
        login.find_element(By.XPATH, "//input[@id='amount']").send_keys(random_amount)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(2)
        
        vendor = wait.until(
             EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='MedCC']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", vendor)
        vendor.click()

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

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Expenses'])[1]"))
        ).click()

        time.sleep(2)

        table_body = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
        )

        # Locate the first table row
        first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[2]")

        # Find the status element within the first row
        status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
        status_text = status_element.text
        expected_status = "New"

        print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

        # Assert that the status is "IN REVIEW"
        assert status_text == "New", f"Expected status to be 'New', but got '{status_text}'"

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@type='button'])[3]"))
        ).click()

        time.sleep(1)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Change Status']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Pending')]"))
        ).click()

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

        table_body = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
        )

        # Locate the first table row
        first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[2]")

        # Find the status element within the first row
        status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
        status_text = status_element.text
        expected_status = "Pending"

        print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

        # Assert that the status is "IN REVIEW"
        assert status_text == "Pending", f"Expected status to be 'Pending', but got '{status_text}'"
        

        time.sleep(3)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Expense Converted to Pay")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_expense_converted(login):
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
                (By.XPATH, "(//span[normalize-space()='Expenses'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@type='button'])[3]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Convert to Payout']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Approved']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Convert to Payout')]"))
        ).click()


        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

        table_body = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
        )

        # Locate the first table row
        first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[2]")

        # Find the status element within the first row
        status_element = first_row.find_element(By.XPATH, "(//span[@class='table-column-data'][normalize-space()='Converted'])[1]")
        status_text = status_element.text
        expected_status = "Converted"

        print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

        # Assert that the status is "Converted"
        assert status_text == "Converted", f"Expected status to be 'Converted', but got '{status_text}'" 

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//i[@class='fa fa-arrow-left']"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Payouts']"))
        ).click()

        time.sleep(2)
        table_body = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
        )

        # Locate the first table row
        first_row = table_body.find_element(By.XPATH, "(//tr[@class='pointer-cursor ng-star-inserted'])[1]")

        # Find the status element within the first row
        status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
        status_text = status_element.text
        expected_status = "Approved"

        print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

        # Assert that the status is "Approved"
        assert status_text == "Approved", f"Expected status to be 'Approved', but got '{status_text}'"
        
        time.sleep(3)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e