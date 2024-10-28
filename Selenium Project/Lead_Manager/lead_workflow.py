from Framework.common_utils import *



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: lead work flow")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_lead_workflow(login):

    try:
        wait = WebDriverWait(login, 10)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Settings')]"))
        ).click()

        lead_suite = login.find_element(By.XPATH, "//div[normalize-space()='Lead Suite']")
        login.execute_script("arguments[0].scrollIntoView();", lead_suite)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[normalize-space()='Manage Leads']"))
        ).click()
        time.sleep(1)


        switch_icon = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='mdc-switch__ripple']"))
        )
        login.execute_script("arguments[0].click();", switch_icon)

        time.sleep(1)

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


        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//img[@src='./assets/images/menu/home-color.png']"))
        ).click()

        time.sleep(3)
        lead_card = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Lead Suite')]"))
        )
        login.execute_script("arguments[0].click();", lead_card)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Product/Service')]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']"))
        ).click()

        prod_service = "Appointment_" + str(uuid.uuid4())[:4]

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Product/Service']"))
        ).send_keys(prod_service)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Select Product']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Appointment']"))
        ).click()


        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@placeholder='Select Lead Template']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Default Template']"))
        ).click()

        time.sleep(1)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Create Product Type']"))
        ).click()

        toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_detail.text
        print("toast_Message:", message)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//i[@class='pi pi-arrow-left']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Channels')]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']"))
                ).click()

        channel_name = "WhatsAPP" + str(uuid.uuid4())[:4]
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Channel']"))
        ).send_keys(channel_name)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Select Platform Type']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Whatsapp']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Select Product Type']"))
        ).click()

        time.sleep(2)
        option = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-dropdownitem[@class='p-element ng-star-inserted'])[1]"))
        )
        login.execute_script("arguments[0].click();", option)
        option.click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='p-multiselect-label p-placeholder'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[@aria-label='Chavakkad']//div[@class='p-checkbox-box']"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Create Channel']"))
        ).click()


        toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_detail.text
        print("toast_Message:", message)

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//i[@class='pi pi-arrow-left']"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//i[@class='pi pi-arrow-left']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Prospects')]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']"))
        ).click()

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        time.sleep(2)
        login.find_element(By.XPATH, "//input[@placeholder='Enter First Name']").send_keys(str(first_name))
        time.sleep(1)
        login.find_element(By.XPATH, "//input[@placeholder='Enter Last Name']").send_keys(str(last_name))
        time.sleep(1)
        login.find_element(By.XPATH, "//input[@id='phone']").send_keys(phonenumber)
        time.sleep(1)
        login.find_element(By.XPATH, "//input[@placeholder='Enter Email Id']").send_keys(email)


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Create Prospect']"))
        ).click()

        toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_detail.text
        print("toast_Message:", message)

        time.sleep(5)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//i[@class='pi pi-arrow-left']"))
        ).click()

 ####################   Create Lead  #######################
        
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Create Lead')]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Search prospect with name,email or phone']"))
        ).send_keys(phonenumber)

        wait.until(
             EC.presence_of_element_located(
                (By.XPATH, "//span[@class='p-button-icon pi pi-search']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='d-flex justify-content-between'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Select Location']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Chavakkad']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Select Channel']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-dropdownitem[@class = 'p-element ng-star-inserted'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Select Lead Owner']"))
        ).click()

        time.sleep(1)
        lead_owner = login.find_element(By.XPATH, "//span[normalize-space()='Sanu AS']")
        login.execute_script("arguments[0].scrollIntoView();", lead_owner)
        lead_owner.click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter City']"))
        ).send_keys("Chavakad")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Notes']"))
        ).send_keys("Note for crate lead")

        wait.until(
            EC.presence_of_element_located(
                
                (By.XPATH, "//span[normalize-space()='Create Lead']"))
        ).click()

        toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_detail.text
        print("toast_Message:", message)

        prospect_name = f"{first_name} {last_name}"
        print(prospect_name)
        owner_name = "Sanu AS"

        time.sleep(3)
        # Wait for table to load and locate the table wrapper
        table = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody"))
        )

        # Locate the first row of the table
        first_row = table.find_element(By.XPATH, "//tbody/tr[1]")

        
        # Verify that the first row contains the prospect name and owner name
        row_text = first_row.text
        assert (prospect_name in row_text) and (owner_name in row_text), (
            f"Expected lead with Prospect Name '{prospect_name}' and Owner '{owner_name}' "
            f"not found in the first row. Found: '{row_text}'"
        )

        print(f"Lead with Prospect Name '{prospect_name}' and Owner '{owner_name}' is correctly found in the first row.")


        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Assign']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@name='Checkboxes4'])[1]"))
        ).click()

        time.sleep(5)

        done_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(@class, 'p-button-primary') and .//i[contains(@class, 'pi pi-check')]]"))
        )

        login.execute_script("arguments[0].click();", done_button)


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

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Convert Lead']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm']"))
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
                (By.XPATH, "//li[8]//a[1]//div[1]//span[1]//span[1]//img[1]"))
        ).click()

        lead = login.find_element(By.XPATH, "//div[@class='heading']")
        login.execute_script("arguments[0].scrollIntoView();", lead)


        # Wait for table to load and locate the table wrapper
        table = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody"))
        )

        # Locate the first row of the table
        first_row = table.find_element(By.XPATH, "//tbody/tr[1]")

        
        # Verify that the first row contains the prospect name and owner name
        row_text = first_row.text
        assert (prospect_name in row_text) and (owner_name in row_text), (
            f"Expected lead with Prospect Name '{prospect_name}' and Owner '{owner_name}' "
            f"not found in the first row. Found: '{row_text}'"
        )
        print(f"Lead with Prospect Name '{prospect_name}' and Owner '{owner_name}' is correctly found in the first row.")


        # Locate the first table row
        first_row = login.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")

        # Find the status element within the first row
        status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
        status_text = status_element.text
        expected_status = "Converted"

        print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

        # Assert that the status is "Converted"
        assert status_text == "Converted", f"Expected status to be 'Converted', but got '{status_text}'"

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]"))
        ).click()

        
        message_element = WebDriverWait(login, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='p-button-label ng-star-inserted']"))
        )

        # Retrieve the text and print it for verification
        message_text = message_element.text
        print(f"Message found: '{message_text}'")

        # Assert that the text matches "Converted to Appointment"
        assert message_text == "Converted to Appointment", "Expected message 'Converted to Appointment' not found on the page."

        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e