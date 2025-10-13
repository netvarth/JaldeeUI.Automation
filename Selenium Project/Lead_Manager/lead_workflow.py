from Framework.common_utils import *



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: lead work flow")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_lead_workflow(login):

    try:
        wait = WebDriverWait(login, 10)

        time.sleep(5)
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

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Product/Service')]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']"))
        ).click()

        prod_service = "Appointment" + str(uuid.uuid4())[:4]

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

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located( 
                (By.XPATH, "(//div[@aria-label='dropdown trigger'])[2]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Appointment Template'])[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Create'])[1]"))
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
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Whatsapp']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
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
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Chavakkad'])[1]"))
        ).click()

        time.sleep(3)

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

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Search prospect with name,email or phone']"))
        ).send_keys(phonenumber)

        time.sleep(3)
        wait.until(
             EC.presence_of_element_located(
                (By.XPATH, "//span[@class='p-button-icon pi pi-search']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='d-flex justify-content-between'])[2]"))
        ).click()

        time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[normalize-space()='Select Location']"))
        # ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Chavakkad']"))
        # ).click()

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

        treet_address, city, state, zip_code, country = generate_random_billing_india_address()



        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Address']"))
        ).send_keys(treet_address, city, state, zip_code, country)


        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        checkbox = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='p-checkbox-box'])[5]"))
        )
        checkbox.click()

        # login.send_keys(checkbox,Keys.ENTER)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='If Yes, Mention them']"))
        ).send_keys("No")

        time.sleep(2)

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

        time.sleep(5)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Assign']"))
        ).click()

        time.sleep(5)
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

        wait_and_locate_click(login, By.XPATH, "//*[@id='pbtnchngestats_leadmgr_leadsgrid_dtls']")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='btncnvrtlead_leadmgr_leadsgrid_dtls']"))
        ).click()

        time.sleep(2)
        wait_and_click(login, By.CSS_SELECTOR, "p-dropdown[optionlabel='place']")
        wait_and_visible_click (login, By.XPATH, "(//li[@id='p-highlighted-option'])[1]")
        
        print("location : Chavakkad")
        login.implicitly_wait(5)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")

        login.implicitly_wait(5)
        wait_and_visible_click(login, By.XPATH, "(//li[@aria-label='ENT'])[1]")
    
        print("Department : ENT")
        user_dropdown_xpath = (
            "(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
            "ng-dirty'])[1]"
        )

        wait_and_click(login, By.XPATH, user_dropdown_xpath)
        
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        wait_and_click(login, By.XPATH, user_option_xpath)
        print("Select user : Naveen")

        time.sleep(3)
        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        element= login.find_element(By.XPATH, service_dropdown_xpath)
        scroll_to_element(login, element)
        # login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        service_option_xpath = ("//li[@aria-label='Naveen Consultation']//div[1]")
        
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, service_option_xpath)
        
        print("Select Service : Naveen Consultation")
        
        time.sleep(5)

        Today_Date = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']",
                )    
            )
        )

        click_to_element(login, Today_Date)
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']"))
        )
        click_to_element(login, time_slot)

        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Confirm']")
        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(2)




        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[8]"))
        ).click()

        wait_and_locate_click(login, By.XPATH, "(//*[@id='pcrdactn_leadmgr_dash'])[2]")

        time.sleep(2)
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
@allure.title("Test Case: Create a Product and Service ")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_create_product_service(login):

    try:
        wait = WebDriverWait(login, 10)

        time.sleep(5)
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
        wait_and_locate_click(login, By.XPATH, "(//div[contains(text(),'Product/Service')])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btncrte_leadmgr_leadsgrid_prdttypegrid']")
        
        prod_service = "Appointment" + str(uuid.uuid4())[:4]
        
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@id='txtprdnme_leadmgr_leadsgrid_prdtypes_crte']", prod_service)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Select Product']"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Appointment']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located( 
                (By.XPATH, "(//div[@aria-label='dropdown trigger'])[2]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Appointment Template'])[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Create'])[1]"))
        ).click()

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]")

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
@allure.title("Test Case: Update the product and service")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_create_product_service_update(login):

    try:
        wait = WebDriverWait(login, 10)

        time.sleep(5)
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
        wait_and_locate_click(login, By.XPATH, "(//div[contains(text(),'Product/Service')])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnupdate_leadmgr_leadsgrid_prdtypes'])[1]")

        time.sleep(2)
        prod_service = "RenameAppointment" + str(uuid.uuid4())[:4]
        servicename_element =  wait_and_locate_click(login, By.XPATH,"//input[@id='txtprdnme_leadmgr_leadsgrid_prdtypes_crte']")
        servicename_element.clear()
        servicename_element.send_keys(prod_service)

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnsubmit_leadmgr_leadsgrid_prdtypes_crte']")

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
@allure.title("Test Case: create the channel in Lead Manager")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_create_channel(login):

    try:
        wait = WebDriverWait(login, 10)

        time.sleep(5)
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
        wait_and_locate_click(login, By.XPATH, "(//div[contains(text(),'Channels')])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btncrte_leadmgr_chnlgrd']")

        channel_name = "WhatsAPP" + str(uuid.uuid4())[:4]
        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='txtchnlnme_leadmgr_chnl_create']"))
        ).send_keys(channel_name)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@id='pddplatform_leadmgr_chnl_create']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Whatsapp']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@id='pddproduct_leadmgr_chnl_create']"))
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
                (By.XPATH, "//p-dropdown[@id='pddlocation_leadmgr_chnl_create']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Chavakkad'])[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Create Channel']"))
        ).click()

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//button[@id= 'btnviewchnl_leadmgr_chnlgrd_chnls'])[1]")

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
@allure.title("Test Case: Update the channel")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_update_channel(login):

    try:
        wait = WebDriverWait(login, 10)

        time.sleep(5)
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
        wait_and_locate_click(login, By.XPATH, "(//div[contains(text(),'Channels')])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnupdchnl_leadmgr_chnlgrd_chnls'])[1]")

        time.sleep(1)
        channel_name = "RenameWhatsAPP" + str(uuid.uuid4())[:4]
        channel_element = wait_and_locate_click(login, By.XPATH, "//input[@id='txtchnlnme_leadmgr_chnl_create']")
        channel_element.clear()
        channel_element.send_keys(channel_name)

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnsubmit_leadmgr_chnl_create']")
        msg = get_toast_message(login)
        print("Toast Message :", msg)

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
@allure.title("Test Case: Disable and enable the first channel")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_disable_enable_channel(login):

    driver = login
    wait = WebDriverWait(login, 15)

    try:
        # --- Navigate to Lead Suite > Channels ---
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//img[@src='./assets/images/menu/home-color.png']"))
        ).click()

        time.sleep(3)
        lead_card = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Lead Suite')]"))
        )
        login.execute_script("arguments[0].click();", lead_card)

        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//div[contains(text(),'Channels')])[1]"))
        ).click()

        # --- Wait for the table and first row to load ---
        wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "tbody.p-datatable-tbody tr"))
        )
        first_row = driver.find_element(By.CSS_SELECTOR, "tbody.p-datatable-tbody tr")

        # --- Capture channel name for reporting ---
        name = first_row.find_element(By.CSS_SELECTOR, "td div.fw-bold div").text.strip()
        print(f"Processing first channel: {name}")

        # --- Locate the toggle switch and input ---
        slider = first_row.find_element(By.CSS_SELECTOR, "p-inputswitch span.p-inputswitch-slider")
        input_elem = first_row.find_element(By.CSS_SELECTOR, "p-inputswitch input[type='checkbox']")

        # --- Scroll into view ---
        login.execute_script("arguments[0].scrollIntoView({block: 'center'});", slider)
        time.sleep(0.5)

        # --- Disable if currently enabled ---
        current_state = input_elem.get_attribute("aria-checked")
        if current_state == "true":
            slider.click()
            time.sleep(1)
            disabled_state = input_elem.get_attribute("aria-checked")
            allure.attach(f"{name} disabled state: {disabled_state}",
                          "Disable Verification", allure.attachment_type.TEXT)
            assert disabled_state == "false", f"{name} not disabled properly"
            print(f"{name} disabled ✅")

        # --- Enable again ---
        slider.click()
        time.sleep(1)
        enabled_state = input_elem.get_attribute("aria-checked")
        allure.attach(f"{name} enabled state: {enabled_state}",
                      "Enable Verification", allure.attachment_type.TEXT)
        assert enabled_state == "true", f"{name} not enabled properly"
        print(f"{name} enabled ✅")

    except Exception as e:
        allure.attach(login.get_screenshot_as_png(),
                      name="full_page",
                      attachment_type=AttachmentType.PNG)
        raise e




lead_scale_url = "https://scale.jaldee.com/visionhospital/lead/create/ch-73b91u7-55"

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Fill and Submit Questionnaire Form (Public Link)")
def test_fill_questionnaire(open_browser):
    driver = open_browser 
    wait = WebDriverWait(driver, 20)

    try:
        driver.get(lead_scale_url)
        time.sleep(10)

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        driver.find_element(By.XPATH, "//input[@placeholder='Enter First Name']").send_keys(first_name)
        driver.find_element(By.XPATH, "//input[@placeholder='Enter Last Name']").send_keys(last_name)
        driver.find_element(By.XPATH, "//input[@placeholder='81234 56789']").send_keys(phonenumber)
        driver.find_element(By.XPATH, "//input[@placeholder='Enter Email Id']").send_keys(email)

        time.sleep(2)
        fake_india= Faker('en_IN')
        fake_india_address= fake_india.address().replace("\n", " ").strip()
        print(fake_india_address)
        driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Address']").send_keys(fake_india_address)

        time.sleep(2)
        driver.find_element(By.XPATH, "//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted']").click()
        
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[normalize-space()='Other']").click()
        driver.find_element(By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]").click()

        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='If Yes, Mention them']").send_keys("NO")

        time.sleep(2)
        driver.find_element(By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]").click()

        time.sleep(2)
        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        time.sleep(2)
        wait_and_locate_click(driver,By.XPATH, "//button[@type='submit']")

        time.sleep(2)
        # otp_digits = "5555"
        otp_digits = "55555"
        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )

        # print("Number of OTP input fields:", len(otp_inputs))
        # print(otp_inputs)

        for i, otp_input in enumerate(otp_inputs):

            # print(i)
            # print(otp_input)
            otp_input.send_keys(otp_digits[i])

        time.sleep(5)
        

    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(),
                      name="full_page",
                      attachment_type=AttachmentType.PNG)
        raise e
    



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Reject the lead and reconfirm the lead")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_reject_reconfirm(login):

    try:
        wait = WebDriverWait(login, 10)

        time.sleep(5)
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

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Product/Service')]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']"))
        ).click()

        prod_service = "Appointment" + str(uuid.uuid4())[:4]

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

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located( 
                (By.XPATH, "(//div[@aria-label='dropdown trigger'])[2]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Appointment Template'])[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Create'])[1]"))
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
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Whatsapp']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
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
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Chavakkad'])[1]"))
        ).click()

        time.sleep(3)

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

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Search prospect with name,email or phone']"))
        ).send_keys(phonenumber)

        time.sleep(3)
        wait.until(
             EC.presence_of_element_located(
                (By.XPATH, "//span[@class='p-button-icon pi pi-search']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='d-flex justify-content-between'])[2]"))
        ).click()

        time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[normalize-space()='Select Location']"))
        # ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Chavakkad']"))
        # ).click()

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

        treet_address, city, state, zip_code, country = generate_random_billing_india_address()



        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Address']"))
        ).send_keys(treet_address, city, state, zip_code, country)


        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        checkbox = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='p-checkbox-box'])[5]"))
        )
        checkbox.click()

        # login.send_keys(checkbox,Keys.ENTER)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='If Yes, Mention them']"))
        ).send_keys("No")

        time.sleep(2)

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

        time.sleep(5)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Assign']"))
        ).click()

        time.sleep(5)
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

        wait_and_locate_click(login, By.XPATH, "//*[@id='pbtnchngestats_leadmgr_leadsgrid_dtls']")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='btnleadrjct_leadmgr_leadsgrid_dtls']"))
        ).click()

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(2)
        # Wait until the table body is visible
        table_body = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "tbody.p-element.p-datatable-tbody"))
        )

        # Locate the first row
        first_row = table_body.find_element(By.TAG_NAME, "tr")

        # Get the status cell (8th td, index 7)
        status_cell = first_row.find_elements(By.TAG_NAME, "td")[7]

        # Get the text
        status_text = status_cell.text.strip()

        # Assert it is "Rejected"
        assert status_text == "Rejected", f"Expected 'Rejected' but got '{status_text}'"
        print("First row status is:", status_text)

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id= 'btnviewlead_leadmgr_leads'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-button[@id='pbtnchngestats_leadmgr_leadsgrid_dtls']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnleadactv_leadmgr_leadsgrid_dtls']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Yes'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(2)
        # Wait until the table body is visible
        table_body = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "tbody.p-element.p-datatable-tbody"))
        )

        # Locate the first row
        first_row = table_body.find_element(By.TAG_NAME, "tr")

        # Get the status cell (8th td, index 7)
        status_cell = first_row.find_elements(By.TAG_NAME, "td")[7]

        # Get the text
        status_text = status_cell.text.strip()

        # Assert it is "Rejected"
        assert status_text == "Active", f"Expected 'Active' but got '{status_text}'"
        print("First row status is:", status_text)

        time.sleep(3)
    except Exception as e:
        allure.attach(login.get_screenshot_as_png(),
                      name="full_page",
                      attachment_type=AttachmentType.PNG)
        raise e
    
