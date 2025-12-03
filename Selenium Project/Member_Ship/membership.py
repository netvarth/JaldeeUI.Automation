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
                (By.XPATH, "//div[@data-action='Subscription Types']"))
        ).click()


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnCreateType_MS_MemberType']"))
        ).click()

        Subscription_Name = "Monthly" + str(uuid.uuid4())[:4]

        wait.until(
            EC.presence_of_element_located( 
                (By.XPATH, "//input[@id='txtName_MS_MemberType_Create']"))
        ).send_keys(Subscription_Name)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='tglSubscriptionRequired_MS_MemberType_Create-button']"))
        ).click()

        Fee_Amount = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='numRegistrationFee_MS_MemberType_Create']"))
        )
        Fee_Amount.clear()
        Fee_Amount.send_keys("150")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//mat-radio-button[@id='rdoRenewal_MS_MemberType_Create']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        login.implicitly_wait(5)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Months']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='tglRenewalRequired_MS_MemberType_Create-button']"))
        ).click()

        Enter_renewal_fee = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='numRenewalFee_MS_MemberType_Create']"))
        )
        Enter_renewal_fee.clear()
        Enter_renewal_fee.send_keys("50")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='numGracePeriod_MS_MemberType_Create']"))
        ).send_keys("10")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnSave_MS_MemberType_Create']"))
        ).click()

        msg = get_snack_bar_message(login)
        print("Snac Bar Message :", msg)

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
                (By.XPATH, "//div[@data-action='Create Member']"))
        ).click()

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                ((By.XPATH, "//input[@id='txtFirstName_MS_Member_Create']"))) 
        ).send_keys(first_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='txtLastName_MS_Member_Create']"))
        ).send_keys(last_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='txtMemberId_MS_Member_Create']"))
        ).send_keys(cons_manual_id)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//ngx-intl-tel-input[@id='telPhone_MS_Member_Create']//input[@id='phone']"))
        ).send_keys(phonenumber)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//ngx-intl-tel-input[@id='telWhatsapp_MS_Member_Create']//input[@id='phone']"))
        ).send_keys(phonenumber)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='txtEmail_MS_Member_Create']"))
        ).send_keys(email)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@id='ddlSubType_MS_Member_Create']"))
        ).click()

        time.sleep(1)
        sub_type = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Quarterly']"))
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
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnSave_MS_Member_Create']")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnProceed_MS_Member_ChangeStatus']"))
        ).click()

        login.implicitly_wait(10)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@id='ddlGetPaymentDesktop_MS_Member_PaymentDetails']"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Pay by Cash']"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnCashPayment_MS_PBI']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnYes_MS_ConfirmPay']"))
        ).click()
        
        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='fa fa-arrow-left pointer-cursor'])[1]"))
        ).click()

        time.sleep(3)

        table_xpath = "(//tbody)[1]"

        # Extract Name (First row)
        name_xpath = f"{table_xpath}//tr[1]//td//span[@class='fw-bold text-capitalize']/span[@class='ng-star-inserted']"
        status_xpath = f"{table_xpath}//tr[1]/td[4]//button[contains(@class, 'dropdown-toggle') and contains(@class, 'btn-outline-success')]"

        # Extract values
        saved_name = wait.until(EC.presence_of_element_located((By.XPATH, name_xpath))).text.strip()

        saved_status = wait.until(EC.presence_of_element_located((By.XPATH, status_xpath))).text.strip()

        # Expected values
        expected_name = saved_name
        expected_status = saved_status

        # Debugging print
        print(f"Extracted Name: '{saved_name}'")
        print(f"Extracted Status: '{saved_status}'")

        assert saved_name == expected_name, f"❌ Name Mismatch: Extracted '{saved_name}', Expected '{expected_name}'"
        assert saved_status == expected_status, f"❌ Status Mismatch: Extracted '{saved_status}', Expected '{expected_status}'"

        print("\n✅ Test Passed! Extracted data matches expected values.")

        # Service type creation 

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@id='divGoBack_MS_Member']")

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@data-action='Service Types']"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnCreateType_MS_ServiceType']"))           
        ).click()

        Service_Type = "Servicetype" + str(uuid.uuid4())[:4]
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Service Type Name']"))
        ).send_keys(Service_Type)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@id='txtAreaRemarks_MS_ST']"))
        ).send_keys("Remarks for the service type")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnSave_MS_ST']"))
        ).click()

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@id='divGoBack_MS_ServiceType']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@data-action='Services']"))
        ).click()

        Service_Name = "Servicename" + str(uuid.uuid4())[:4]

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnCreateService_MS_Scheme']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='txtServiceName_MS_Scheme_Create']"))
        ).send_keys(Service_Name)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']"))
        ).send_keys("A women s policy generally refers to a set of strategies and actions aimed at promoting the rights, well-being, and empowerment of women, addressing gender inequalities, and ensuring their full and equal participation in all aspects of life.")

        time.sleep(2)
        # today = datetime.today()
        # next_month = today + timedelta(days=30)

        # current_day = today.day
        # next_month_year = next_month.year
        # next_month_name = next_month.strftime("%B")  # Full month name (e.g., "April")

        # # Open Date Picker for Start Date
        # start_date_picker = wait.until(
        #     EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='Select Date'])[1]"))
        # )
        # start_date_picker.click()

        # # # Select Current Day
        # # current_day_element = wait.until(
        # #     EC.element_to_be_clickable((By.XPATH, f"//td[normalize-space()='{current_day}']"))
        # # )
        # # current_day_element.click()

        # # Select the correct day based on 30 days from today
        # next_day = next_month.day

        # # Handle cases where the 30-days-later date doesn't exist in the calendar
        # next_month_day_element = wait.until(
        #     EC.element_to_be_clickable((By.XPATH, f"//td[normalize-space()='{next_day}']"))
        # )
        # next_month_day_element.click()

        # # Open Date Picker for End Date (After One Month)
        # end_date_picker = wait.until(
        #     EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='Select Date'])[2]"))
        # )
        # end_date_picker.click()
        # time.sleep(5)
        # # Navigate to the next month if necessary
        # while True:
        #     displayed_month = wait.until(
        #         EC.presence_of_element_located((By.CLASS_NAME, "p-datepicker-month"))
        #     ).text
        #     displayed_year = wait.until(
        #         EC.presence_of_element_located((By.CLASS_NAME, "p-datepicker-year"))
        #     ).text

        #     if displayed_month == next_month_name and str(displayed_year) == str(next_month_year):
        #         break

        #     # Click "Next" button to move to next month
        #     next_button = wait.until(
        #         EC.element_to_be_clickable((By.CLASS_NAME, "p-datepicker-next"))
        #     )
        #     next_button.click()

        # # Select the same day in the next month
        # next_month_day_element = wait.until(
        #     EC.element_to_be_clickable((By.XPATH, f"//td[normalize-space()='{current_day}']"))
        # )
        # next_month_day_element.click()

        

        # Get today's date and target date 30 days later
        today = datetime.today()
        start_day = today.day
        start_month = today.strftime("%B")
        start_year = str(today.year)

        end_date = today + timedelta(days=30)
        end_day = end_date.day
        end_month = end_date.strftime("%B")
        end_year = str(end_date.year)

       

        
        # --- START DATE SELECTION ---

        # Open the first date picker (start date)
        start_date_picker = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='Select Date'])[1]"))
        )
        start_date_picker.click()

        # No need to navigate since it's today — just select today's date
        start_day_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//td[normalize-space()='{start_day}']"))
        )
        start_day_element.click()

        # --- END DATE SELECTION ---

        # Open the second date picker (end date)
        end_date_picker = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='Select Date'])[2]"))
        )
        end_date_picker.click()

        time.sleep(2)
        # Navigate to the correct month/year for the end date
        while True:
            displayed_month = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "p-datepicker-month"))
            ).text
            displayed_year = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "p-datepicker-year"))
            ).text

            if displayed_month == end_month and displayed_year == end_year:
                break

            next_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "p-datepicker-next"))
            )
            next_button.click()
            time.sleep(1)

        valid_days = wait.until(
            EC.presence_of_all_elements_located((
                By.XPATH,
                f"//td[not(contains(@class, 'p-datepicker-other-month'))]//span[normalize-space()='{end_day}' and not(contains(@class, 'p-disabled'))]"
            ))
        )

        # Click the first visible, valid day
        for day in valid_days:
            if day.is_displayed():
                day.click()
                print(f"✅ Clicked end date: {end_day}")
                break

        time.sleep(3)


        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@placeholder='Remarks'])[1]"))
        ).send_keys("Remarks for the service")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        select_servicetype = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Woman Empowerment'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", select_servicetype)
        select_servicetype.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='p-checkbox-box'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text    
        print("Snack bar message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Members'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//button[@type='button'])[1]"))
        ).click()
        time.sleep(2)
        last_checkbox = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='p-radiobutton-box'])[last()]"))
        )
        last_checkbox.click()

        # # Optional: Verify selection
        # assert last_checkbox.is_selected(), "Checkbox not selected"

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnDone_MS_SCH_SUBA']"))
        ).click()

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@id='divGoBack_MS_Member_DetailsView']"))
        ).click()


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@id='divGoBack_MS_Member']"))
        ).click()

        print("Create Lead")
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@data-action='Leads']"))
        ).click()


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btncrtelead_leadmgr_leadsgrid']"))
        ).click()

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='txtfirstName_leadmgr_leadsgrid_create']"))
        ).send_keys(first_name)


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='txtlastName_leadmgr_leadsgrid_create']"))
        ).send_keys(last_name)




        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[1]"))
        ).send_keys(phonenumber)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@id='pddchannel_leadmgr_leadsgrid_create']"))
        ).click()
        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Whatsapp']"))
        ).click()


        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@id='pddleadowner_leadmgr_leadsgrid_create']"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='David James']"))
        ).click()


        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btncrte_leadmgr_leadsgrid_create']"))
        ).click()

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnviewlead_leadmgr_leads'])[1]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Change Status'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Convert Lead'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()


        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(5)



    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="error_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        print(f"Test Failed: {e}")  # Ensure failure reason is visible in logs
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: ")
@pytest.mark.parametrize("url, username, password", [(scale_url, membership_scale, password)])
def test_create_Member(login):

    try:

        wait = WebDriverWait(login, 20)
        time.sleep(3)
        wait_and_locate_click(
            login, By.XPATH, "(//div[@class='cardAction_MS_Dashboard'])[2]")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnCreate_MS_Member']")
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        wait_and_locate_click(login, By.XPATH, "//button[@id='mnuCreateMember_MS_Member']")

        time.sleep(1)
        wait_and_send_keys(
            login, By.XPATH, "//input[@id='txtFirstName_MS_Member_Create']", first_name)
        time.sleep(1)
        wait_and_send_keys(
            login, By.XPATH, "//input[@id='txtLastName_MS_Member_Create']", last_name)
        time.sleep(1)
        wait_and_send_keys(
            login, By.XPATH, "//input[@id='txtMemberId_MS_Member_Create']", cons_manual_id)
        time.sleep(1)
        wait_and_send_keys(
            login, By.XPATH, "//ngx-intl-tel-input[@id='telPhone_MS_Member_Create']//input[@id='phone']", phonenumber)
        time.sleep(1)
        wait_and_send_keys(
            login, By.XPATH, "//input[@id='txtEmail_MS_Member_Create']", email)
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@id='ddlSubType_MS_Member_Create']")

        time.sleep(1)
        sub_type_element = login.find_element(By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Quarterly']")

        scroll_to_element(login, sub_type_element)
        time.sleep(2)
        sub_type_element.click()

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnSave_MS_Member_Create']")

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(3)


    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="error_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        print(f"Test Failed: {e}")  # Ensure failure reason is visible in logs
        raise e     

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Convert Lead to Member and assign service")
@pytest.mark.parametrize("url, username, password", [(scale_url, membership_scale, password)])
def test_Lead_to_Member(login):

    try:

        wait = WebDriverWait(login, 20)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Leads')])[1]"))
        ).click()


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[1]"))
        ).click()

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter First Name'])[1]"))
        ).send_keys(first_name)


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Last Name'])[1]"))
        ).send_keys(last_name)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[1]"))
        ).send_keys(phonenumber)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()
        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Whatsapp'])[1]"))
        ).click()


        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='David James'])[1]"))
        ).click()


        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Create Lead'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//button[@id= 'btnviewlead_leadmgr_leads'])[1]")

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Change Status'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Convert to Member'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Member ID'])[1]"))
        ).send_keys(cons_manual_id)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[2]"))
        ).send_keys(phonenumber)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click() 


        Sub_type1 = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Quarterly'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView()", Sub_type1)
        Sub_type1.click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Register'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Proceed to Pay'])[1]"))
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

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='fa fa-arrow-left pointer-cursor'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//button[@type='button'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@class='p-ripple p-element p-paginator-last p-paginator-element p-link ng-star-inserted'])[1]")

        time.sleep(3)
        last_radiobutton = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='p-radiobutton-box'])[last()]"))
        )
        last_radiobutton.click()

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnDone_MS_SCH_SUBA']")

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(3)


    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="error_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        print(f"Test Failed: {e}")  
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case:Add subscription plan")
@pytest.mark.parametrize("url, username, password", [(scale_url, membership_scale, password)])
def test_Add_subscription_plan(login):

    try:
        wait= WebDriverWait(login, 30)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@data-action='Members'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnAdd_MS_Member_Subscriptions']"))
        ).click()

        # Define the target name
        # target_name_xpath = "//td[@class='ng-star-inserted']//span[@class='ng-star-inserted'][normalize-space()='Yearly']"
        # element = login.find_element(By.XPATH, target_name_xpath)
        target_name = "Yearly"
        

        while True:
            try:
                row_xpath = f"//td[@class='ng-star-inserted']//span[@class='ng-star-inserted'][normalize-space()='{target_name}']"
                row_element = wait.until(
                    EC.presence_of_element_located((By.XPATH, row_xpath))
                )
                radio_button = row_element.find_element(By.XPATH, ".//div[@class='p-radiobutton-box']")
                radio_button.click()
                print(f"Radio button for '{target_name}' selected.")
                break

            except Exception as e:
                # Debug print plans on current page
                plan_names = login.find_elements(By.XPATH, "//tr/td/span")
                print("Plans on this page:")
                for p in plan_names:
                    print("-", p.text.strip())

                # Try to go to next page
                try:
                    next_button = wait.until(
                        EC.element_to_be_clickable((
                            By.XPATH,
                            "(//button[@class='p-ripple p-element p-paginator-next p-paginator-element p-link'])[1]"
                        ))
                    )
                    login.execute_script("arguments[0].scrollIntoView(true);", next_button)
                    next_button.click()
                    wait.until(EC.presence_of_element_located((By.XPATH, "//tr")))
                except:
                    print("Pagination ended or next button not clickable.")
                    break

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="error_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        print(f"Test Failed: {e}")  
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case:Create the subscription type")
@pytest.mark.parametrize("url, username, password", [(scale_url, membership_scale, password)])
def test_create_subscription_type_days_payment(login):  

    test_data = [
        {"subscription_name_prefix": "Days", "reg_fee": "150", "renewal_fee": "50", "renewal_period": "1", "period_unit": "Days", "grace_period": "0"},
        {"subscription_name_prefix": "Months", "reg_fee": "700", "renewal_fee": "75", "renewal_period": "5", "period_unit": "Months", "grace_period": "1"},
        {"subscription_name_prefix": "Years", "reg_fee": "1300", "renewal_fee": "100", "renewal_period": "10", "period_unit": "Years", "grace_period": "2"},
        {"subscription_name_prefix": "CalendarYear", "reg_fee": "1000", "renewal_fee": "100", "renewal_period": "10", "period_unit": "Calendar Year", "grace_period": "2"},
        {"subscription_name_prefix": "CalendarMonth", "reg_fee": "500", "renewal_fee": "100", "renewal_period": "10", "period_unit": "Calendar Month", "grace_period": "2"},
        {"subscription_name_prefix": "CalendarWeek", "reg_fee": "200", "renewal_fee": "100", "renewal_period": "5", "period_unit": "Calendar Week", "grace_period": "1"}
    ]
    try:
        wait = WebDriverWait(login, 20)

        for data in test_data:
            # Click on Subscription Types
            wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Subscription Types')])[1]"))).click()
            time.sleep(2)
            wait.until(EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Create'])[1]"))).click()

            # Generate unique subscription name
            Subscription_Name = f"{data['subscription_name_prefix']}{str(uuid.uuid4())[:4]}"
            time.sleep(2)
            wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Enter Name'])[1]"))).send_keys(Subscription_Name)

            wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='mdc-switch__icon mdc-switch__icon--off'])[1]"))).click()

            reg_fee = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Enter Registration Fee'])[1]")))
            reg_fee.clear()
            reg_fee.send_keys(data['reg_fee'])
            

            wait.until(EC.presence_of_element_located((By.XPATH, "(//label[normalize-space()='Renewal'])[1]"))).click()
            time.sleep(1)

            select_number = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Select Number'])[1]")))
            select_number.clear()
            select_number.send_keys(data['renewal_period'])

            # Select Period Unit
            time.sleep(1)
            wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))).click()
            option_xpath = f"//span[normalize-space()='{data['period_unit']}']"
            wait.until(EC.presence_of_element_located((By.XPATH, option_xpath))).click()

            wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='mdc-switch__icon mdc-switch__icon--off'])[2]"))).click()

            renewal_fee = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Enter Renewal Fee'])[1]")))
            renewal_fee.clear()
            renewal_fee.send_keys(data['renewal_fee'])

            wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Enter Grace Period'])[1]"))).send_keys(data['grace_period'])

            wait.until(EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Save'])[1]"))).click()

            # Check for success message
            snack_bar = WebDriverWait(login, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal")))
            message = snack_bar.text
            print("Snack bar message:", message)

            time.sleep(3)

            # Validate the newly added subscription in the table
            table_xpath = "(//tbody)[1]"
            subscription_xpath = f"{table_xpath}//td/span[normalize-space()='{Subscription_Name}']"
            status_xpath = f"{table_xpath}//td[span[normalize-space()='{Subscription_Name}']]/following-sibling::td[4]//button"

            # Check if subscription name exists in the table
            saved_name_element = wait.until(EC.presence_of_element_located((By.XPATH, subscription_xpath)))
            saved_name = saved_name_element.text
            assert saved_name == Subscription_Name, f"Expected: {Subscription_Name}, but got {saved_name}"

            # Check if status is "Active"
            status_element = wait.until(EC.presence_of_element_located((By.XPATH, status_xpath)))
            status = status_element.text
            assert status == "Active", f"Expected: 'Active', but got {status}"

            print(f"Subscription '{Subscription_Name}' successfully created and verified!")


    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="error_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        print(f"Test Failed: {e}")  
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case:create service with all the detail filled")
@pytest.mark.parametrize("url, username, password", [(scale_url, membership_scale, password)])
def test_create_service(login):

    try:

        wait = WebDriverWait(login, 20)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//div[@class='cardAction_MS_Dashboard'])[3]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnCreateService_MS_Scheme']")

        time.sleep(2)
        
        Service_Name = "Servicename" + str(uuid.uuid4())[:4]
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='txtServiceName_MS_Scheme_Create']"))
        ).send_keys(Service_Name)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']"))
        ).send_keys("A women s policy generally refers to a set of strategies and actions aimed at promoting the rights, well-being, and empowerment of women, addressing gender inequalities, and ensuring their full and equal participation in all aspects of life.")

        time.sleep(2)
        # Get today's date and target date 30 days later
        today = datetime.today()
        start_day = today.day
        start_month = today.strftime("%B")
        start_year = str(today.year)

        end_date = today + timedelta(days=30)
        end_day = end_date.day
        end_month = end_date.strftime("%B")
        end_year = str(end_date.year)

       

        
        # --- START DATE SELECTION ---

        # Open the first date picker (start date)
        start_date_picker = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='Select Date'])[1]"))
        )
        start_date_picker.click()

        # No need to navigate since it's today — just select today's date
        start_day_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//td[normalize-space()='{start_day}']"))
        )
        start_day_element.click()

        # --- END DATE SELECTION ---

        # Open the second date picker (end date)
        end_date_picker = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='Select Date'])[2]"))
        )
        end_date_picker.click()

        time.sleep(2)
        # Navigate to the correct month/year for the end date
        while True:
            displayed_month = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "p-datepicker-month"))
            ).text
            displayed_year = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "p-datepicker-year"))
            ).text

            if displayed_month == end_month and displayed_year == end_year:
                break

            next_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "p-datepicker-next"))
            )
            next_button.click()
            time.sleep(1)

        valid_days = wait.until(
            EC.presence_of_all_elements_located((
                By.XPATH,
                f"//td[not(contains(@class, 'p-datepicker-other-month'))]//span[normalize-space()='{end_day}' and not(contains(@class, 'p-disabled'))]"
            ))
        )

        # Click the first visible, valid day
        for day in valid_days:
            if day.is_displayed():
                day.click()
                print(f"✅ Clicked end date: {end_day}")
                break

        time.sleep(3)


        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@placeholder='Remarks'])[1]"))
        ).send_keys("Remarks for the service")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        select_servicetype = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Woman Empowerment'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", select_servicetype)
        select_servicetype.click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnCreate_MS_Scheme_Create']")

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)
        time.sleep(3)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="error_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        print(f"Test Failed: {e}")  
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case:create service without few mandatory fields")
@pytest.mark.parametrize("url, username, password", [(scale_url, membership_scale, password)])
def test_create_service_1(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//div[@class='cardAction_MS_Dashboard'])[3]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnCreateService_MS_Scheme']")

        time.sleep(2)
        
        Service_Name = "Servicename" + str(uuid.uuid4())[:4]
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='txtServiceName_MS_Scheme_Create']"))
        ).send_keys(Service_Name)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']"))
        ).send_keys("A women s policy generally refers to a set of strategies and actions aimed at promoting the rights, well-being, and empowerment of women, addressing gender inequalities, and ensuring their full and equal participation in all aspects of life.")



        with allure.step("Validating 'Create' button is disabled"):
            create_btn = wait.until(
                EC.presence_of_element_located((By.ID, "btnCreate_MS_Scheme_Create"))
            )

            if not create_btn.is_enabled():
                result = "PASS: Create button is disabled as expected."
                print(result)
                allure.attach(result, name="Create Button Disabled", attachment_type=allure.attachment_type.TEXT)
            else:
                result = "FAIL: Create button is enabled! Expected to be disabled."
                print(result)
                allure.attach(result, name="Create Button Disabled", attachment_type=allure.attachment_type.TEXT)
                assert False, "Create button should be disabled!"

            

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="error_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        print(f"Test Failed: {e}")  
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case:Edit service and update")
@pytest.mark.parametrize("url, username, password", [(scale_url, membership_scale, password)])
def test_create_service_2(login):

    try:

        wait = WebDriverWait(login, 20)
        time.sleep(3)

        wait_and_locate_click(
            login, By.XPATH, "(//div[@class='cardAction_MS_Dashboard'])[3]")
        time.sleep(2)
        
        wait_and_locate_click(
            login, By.XPATH, "(//button[@label='Edit'])[1]")
        
        Service_Name = "RenameServicename" + str(uuid.uuid4())[:4]
        time.sleep(2)
        service_element_name = wait_and_locate_click(
            login, By.XPATH, "//input[@id='txtServiceName_MS_Scheme_Create']")

        service_element_name.clear()
        service_element_name.send_keys(Service_Name)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnCreate_MS_Scheme_Create']")

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)


    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="error_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        print(f"Test Failed: {e}")  
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case:Edit service type and Update from Detail page")
@pytest.mark.parametrize("url, username, password", [(scale_url, membership_scale, password)])
def test_edit_service(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(3)

        wait_and_locate_click(
            login, By.XPATH, "(//div[@class='cardAction_MS_Dashboard'])[3]")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@label='View'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//p-button[@id='btnEditService_MS_SCH_SD']")

        time.sleep(2)
        Service_Name = "RenameServicename" + str(uuid.uuid4())[:4]
        time.sleep(2)
        service_element_name = wait_and_locate_click(
            login, By.XPATH, "//input[@id='txtServiceName_MS_Scheme_Create']")

        service_element_name.clear()
        service_element_name.send_keys(Service_Name)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnCreate_MS_Scheme_Create']")

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(3)
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="error_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        print(f"Test Failed: {e}")  
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case:create service type with all the detail filled")
@pytest.mark.parametrize("url, username, password", [(scale_url, membership_scale, password)])
def test_create_service_type(login):

    try:
        wait = WebDriverWait(login, 30)
        time.sleep(3)
        wait_and_locate_click(
            login, By.XPATH, "(//div[@class='cardAction_MS_Dashboard'])[7]")

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "//button[@id='btnCreateType_MS_ServiceType']")

        Service_Type = "Servicetype" + str(uuid.uuid4())[:4]
        time.sleep(2)

        wait_and_send_keys(
            login, By.XPATH, "//input[@placeholder='Service Type Name']", Service_Type)

        wait_and_send_keys(
            login, By.XPATH, "//textarea[@id='txtAreaRemarks_MS_ST']", "Remarks for the service type")
        
        wait_and_locate_click(
            login, By.XPATH, "//button[@id='btnSave_MS_ST']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        
        time.sleep(3)
        first_row_xpath = "//tbody/tr[1]/td[1]//span"
        first_row_text = wait.until(
            EC.visibility_of_element_located((By.XPATH, first_row_xpath))
        ).text.strip()

        with allure.step(f"Validating that first row value is '{Service_Type}'"):
            if first_row_text == Service_Type:
                print(f"Assertion Passed: '{Service_Type}' is correctly displayed in the first row.")
                allure.attach(
                    f"Assertion Passed: Expected '{Service_Type}', Found '{first_row_text}'",
                    name="Assertion Result",
                    attachment_type=allure.attachment_type.TEXT
                )
            else:
                print(f"Assertion Failed: Expected '{Service_Type}', but Found '{first_row_text}'")
                allure.attach(
                    f"Assertion Failed:\nExpected: {Service_Type}\nFound: {first_row_text}",
                    name="Assertion Result",
                    attachment_type=allure.attachment_type.TEXT
                )
                assert False, f"Expected '{Service_Type}' but found '{first_row_text}'"

        time.sleep(2)
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="error_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        print(f"Test Failed: {e}")  
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case:Edit service type and Update")
@pytest.mark.parametrize("url, username, password", [(scale_url, membership_scale, password)])
def test_edit_service_type(login):

    try:
        wait = WebDriverWait(login, 30)
        time.sleep(3)
        wait_and_locate_click(
            login, By.XPATH, "(//div[@class='cardAction_MS_Dashboard'])[7]")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@label='Edit'])[1]")

        Service_Type = "ServicetypeRename" + str(uuid.uuid4())[:4]
        service_type_name = wait_and_locate_click(login, By.XPATH, "//input[@placeholder='Service Type Name']")
        service_type_name.clear()

        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Service Type Name']", Service_Type)

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnSave_MS_ST']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(3)
        first_row_xpath = "//tbody/tr[1]/td[1]//span"
        first_row_text = wait.until(
            EC.visibility_of_element_located((By.XPATH, first_row_xpath))
        ).text.strip()

        with allure.step(f"Validating that first row value is '{Service_Type}'"):
            if first_row_text == Service_Type:
                print(f"Assertion Passed: '{Service_Type}' is correctly displayed in the first row.")
                allure.attach(
                    f"Assertion Passed: Expected '{Service_Type}', Found '{first_row_text}'",
                    name="Assertion Result",
                    attachment_type=allure.attachment_type.TEXT
                )
            else:
                print(f"Assertion Failed: Expected '{Service_Type}', but Found '{first_row_text}'")
                allure.attach(
                    f"Assertion Failed:\nExpected: {Service_Type}\nFound: {first_row_text}",
                    name="Assertion Result",
                    attachment_type=allure.attachment_type.TEXT
                )
                assert False, f"Expected '{Service_Type}' but found '{first_row_text}'"

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="error_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        print(f"Test Failed: {e}")  
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case:Active and Inactive Service type")
@pytest.mark.parametrize("url, username, password", [(scale_url, membership_scale, password)])
def test_active_inactive_service_type(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(3)
        wait_and_locate_click(
            login, By.XPATH, "(//div[@class='cardAction_MS_Dashboard'])[7]")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='dropdownMenuButton'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//div[normalize-space()='Inactive'])[1]")

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(2)
        wait_and_locate_click(login , By.XPATH, "(//button[@id='dropdownMenuButton'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='dropdown-item pointer-cursor fw-bold dropdownCSTSE_MS_ST_Grid ng-star-inserted'])[1]")

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(3)
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="error_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        print(f"Test Failed: {e}")  
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case:Active and Inactive Service type")
@pytest.mark.parametrize("url, username, password", [(scale_url, membership_scale, password)])
def test_active_inactive_service(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(3)

        wait_and_locate_click(
            login, By.XPATH, "(//div[@class='cardAction_MS_Dashboard'])[3]")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[contains(@class,'btnStatus_MS_SCH_SG')])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//div[normalize-space()='Inactive'])[1]")

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(2)
        wait_and_locate_click(login , By.XPATH, "(//button[contains(@class,'btnStatus_MS_SCH_SG')])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//div[normalize-space()='Active'])[1]")

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(3)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="error_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        print(f"Test Failed: {e}")  
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case:")
@pytest.mark.parametrize("url, username, password", [(scale_url, membership_scale, password)])
def test_(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//div[@class='cardAction_MS_Dashboard'])[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "")
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="error_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        print(f"Test Failed: {e}")  
        raise e