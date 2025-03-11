from Framework.common_utils import *
from Framework.common_dates_utils import *



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Basic Member Ship flow")
@pytest.mark.parametrize("url, username, password", [(scale_url, membership_scale, password)])
def test_los_workflow(login):

    try:

        wait = WebDriverWait(login, 20)
        print("Create the Subscription Type")

        login.implicitly_wait(10)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Subscription Types')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Create'])[1]"))
        ).click()

        Subscription_Name = "Monthly_" + str(uuid.uuid4())[:4]

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Name'])[1]"))
        ).send_keys(Subscription_Name)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='mdc-switch__icon mdc-switch__icon--off'])[1]"))
        ).click()

        Fee_Amount = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Registration Fee'])[1]"))
        )
        Fee_Amount.clear()
        Fee_Amount.send_keys("150")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[normalize-space()='Renewal'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        login.implicitly_wait(5)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Months'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='mdc-switch__icon mdc-switch__icon--off'])[2]"))
        ).click()

        Enter_renewal_fee = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Renewal Fee'])[1]"))
        )
        Enter_renewal_fee.clear()
        Enter_renewal_fee.send_keys("50")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Grace Period'])[1]"))
        ).send_keys("10")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save'])[1]"))
        ).click()

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

        time.sleep(3)

          # Validate the newly added subscription in the table
        table_xpath = "(//tbody)[1]"
        subscription_xpath = f"{table_xpath}//td/span[normalize-space()='{Subscription_Name}']"
        status_xpath = f"{table_xpath}//td[span[normalize-space()='{Subscription_Name}']]/following-sibling::td[4]//button"

        # Check if subscription name exists in the table
        saved_name_element = wait.until(
            EC.presence_of_element_located((By.XPATH, subscription_xpath))
        )
        saved_name = saved_name_element.text
        print(f"Saved Subscription Name: {saved_name}")  # Debugging print

        assert saved_name == Subscription_Name, f"Expected Subscription Name: {Subscription_Name}, but got {saved_name}"

        # Check if status is "Active"
        status_element = wait.until(
            EC.presence_of_element_located((By.XPATH, status_xpath))
        )
        status = status_element.text
        print(f"Subscription Status: {status}")  # Debugging print

        assert status == "Active", f"Expected status: 'Active', but got {status}"

        print("Subscription successfully created and verified!")

        print("Create the Member")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()  

        login.implicitly_wait(10)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Create Members')])[1]"))
        ).click()

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                ((By.XPATH, "(//input[@placeholder='First Name'])[1]"))) 
        ).send_keys(first_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Last Name'])[1]"))
        ).send_keys(last_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Member ID'])[1]"))
        ).send_keys(cons_manual_id)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[1]"))
        ).send_keys(phonenumber)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[2]"))
        ).send_keys(phonenumber)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Email'])[1]"))
        ).send_keys(email)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(1)
        sub_type = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Quarterly'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", sub_type)
        login.implicitly_wait(10)
        sub_type.click()

        # time.sleep(1)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        # ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Register'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Generate Fee'])[1]"))
        ).click()

        login.implicitly_wait(10)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'][normalize-space()='Get Payment'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Pay by Cash'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Pay'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()
        
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)
        time.sleep(3)
        # Define Table XPath
        table_xpath = "(//tbody)[1]"
        member_full_name = f"{first_name} {last_name}"
        print(member_full_name)
        # Construct XPaths for Validation
        member_xpath = f"{table_xpath}//td//span[normalize-space()='{member_full_name}']"
  
        subscription_xpath = f"{table_xpath}//td[span[normalize-space()='{member_full_name}']]/following-sibling::td[1]"
        status_xpath = f"{table_xpath}//td[span[normalize-space()='{member_full_name}']]/following-sibling::td[3]//button"

        # Assert if the member name exists in the table
        saved_name = wait.until(EC.presence_of_element_located((By.XPATH, member_xpath))).text
        assert saved_name == member_full_name, f"Member Name '{saved_name}' does not match expected '{member_full_name}'"

        # Assert Subscription Type
        saved_subscription = wait.until(EC.presence_of_element_located((By.XPATH, subscription_xpath))).text.strip()
        assert saved_subscription == "Quarterly", f"Subscription Type '{saved_subscription}' is incorrect"

        # Assert Active Status
        saved_status = wait.until(EC.presence_of_element_located((By.XPATH, status_xpath))).text.strip()
        assert saved_status == "Active", f"Status '{saved_status}' is not 'Active'"

        print(f"Member '{member_full_name}' successfully created with 'Quarterly' subscription and 'Active' status!")


    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="error_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        print(f"Test Failed: {e}")  # Ensure failure reason is visible in logs
        raise e