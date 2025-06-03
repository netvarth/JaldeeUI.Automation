from Framework.common_utils import *
from Framework.common_dates_utils import *
import random

from faker import Faker




@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Basic lab order work flow")
@pytest.mark.parametrize("url, username, password", [(scale_url, Lab_order_user, password)])
def test_lab_order(login):

    try:
        
        time.sleep(5)
        wait = WebDriverWait(login, 30)

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
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Pirme Clinic'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", clinic_option)

        clinic_option.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[5]"))
        ).click()

        store_option = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Aster Dental'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", store_option)
        store_option.click()

        time.sleep(1)
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
                (By.XPATH, "(//input[@class='mdc-checkbox__native-control'])[1]"))
        ).click()

        time.sleep(3)
        checkbox = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//mat-checkbox[contains(@class, 'mat-mdc-checkbox')]//input[@type='checkbox'])[1]"))
        )
        login.execute_script("arguments[0].click()", checkbox)


        time.sleep(3)
        # Questionnaire

        random_form_number = random.randint(100, 9999)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter form number'])[1]"))
        ).send_keys(str(random_form_number))

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)

        today_element = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
        (By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")
                )
        )          

        # Click using JavaScript in case normal click doesn't work
        login.execute_script("arguments[0].click();", today_element)

        print("Clicked today's date:", today_element.text)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Please enter the doctor’s name'])[1]"))
        ).send_keys("Naveen P")

        time.sleep(2)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Please enter the patient name'])[1]"))
        ).send_keys(f"{first_name} {last_name}")

        time.sleep(1)

        random_age = random.randint(23, 65)
        print("Random Age:", random_age)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Age'])[1]"))
        ).send_keys(str(random_age)) 

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Male'])[1]"))
        ).click()

        prosthesis_types = [
        "Complete Denture",
        "Partial Denture",
        "Fixed Bridge",
        "Crown",
        "Implant",
        "Implant-Supported Denture",
        "Veneer",
        "Inlay",
        "Onlay",
        "Orthodontic Appliance"
        ]

        random_type = random.choice(prosthesis_types)
        print("Random Prosthesis Type:", random_type)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Prosthesis Type'])[1]"))
        ).send_keys(random_type)

        time.sleep(2)

        # Locate all the circle elements inside the quadrant-container
        circles = login.find_elements(By.CSS_SELECTOR, ".quadrant-container .circle")

        # Randomly choose 4 or 5 distinct circles
        num_to_select = random.choice([4, 5])
        selected_circles = random.sample(circles, num_to_select)

        # Click on each selected circle
        for circle in selected_circles:
            print(f"Clicking on: {circle.text.strip()}")
            login.execute_script("arguments[0].scrollIntoView(true);", circle)
            circle.click()


        time.sleep(2)
        Pontic_types = [
        "Saddle Pontic",
        "Modified Ridge Lap Pontic",
        "Conical Pontic",
        "Ovate Pontic",
        "Prefabricated Pontics"
         ]

        random_pontic_type = random.choice(prosthesis_types)
        print("Random Pontic types:", random_pontic_type)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Type Of Ponti'])[1]"))
        ).send_keys(random_pontic_type)


        time.sleep(2)
        Shade_types = [
        "Reddish-Brownish",
        "Reddish-Yellowish",
        "Greyish",
        "Reddish-Grey"
       	]

        random_Shade_types = random.choice(Shade_types)
        print("Random Pontic types:", random_Shade_types)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Shade'])[1]"))
        ).send_keys(random_Shade_types)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Yes'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]"))
        ).click()

        time.sleep(2)
        
        future_date = datetime.now() + timedelta(days=4)
        future_day = str(future_date.day)

        # XPath to locate the cell containing the desired date
        date_xpath = f"//td[not(contains(@class,'p-datepicker-other-month'))]//span[text()='{future_day}']"

        # Wait for and click the date
        future_date_element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        login.execute_script("arguments[0].click();", future_date_element)

        print("Clicked future date (+4):", future_date_element.text)


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Yes'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[3]"))
        ).click()
        time.sleep(2)
        
        future_date = datetime.now() + timedelta(days=6)
        future_day = str(future_date.day)

        # XPath to locate the cell containing the desired date
        date_xpath = f"//td[not(contains(@class,'p-datepicker-other-month'))]//span[text()='{future_day}']"

        # Wait for and click the date
        future_date_element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        login.execute_script("arguments[0].click();", future_date_element)

        print("Clicked future date (+6):", future_date_element.text)


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Final Finish'])[1]"))
        ).send_keys("Final Finish")
        
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[4]"))
        ).click()

        time.sleep(2)
        
        future_date = datetime.now() + timedelta(days=10)
        future_day = str(future_date.day)

        # XPath to locate the cell containing the desired date
        date_xpath = f"//td[not(contains(@class,'p-datepicker-other-month'))]//span[text()='{future_day}']"

        # Wait for and click the date
        future_date_element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        login.execute_script("arguments[0].click();", future_date_element)

        print("Clicked future date (+10):", future_date_element.text)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter your notes'])[1]"))
        ).send_keys("Some notes")   

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Confirm Order'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Create Invoice'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='View Invoice'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Share Payment Link'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
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

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Complete Order'])[1]"))
        ).click()

        toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_detail.text
        print("toast_Message:", message)

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Pass To Delivery'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@name='radioBtn'])[1]"))
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
                (By.XPATH, "//span[@class='mdc-list-item__primary-text'][normalize-space()='Dispatched']"))
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
                (By.XPATH, "(//span[normalize-space(.)='Dispatched'])[1]"))
        )
        pickup_status_text = pickup_status_element.text
        print(f"Status: {pickup_status_text}")
        assert pickup_status_text == "Dispatched", f"Expected 'Dispatched' status, but got {pickup_status_text}"

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Change Status'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='mdc-list-item__primary-text'][normalize-space()='Delivered'])[1]"))
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
@allure.title("Test Case: Create Clinic")
@pytest.mark.parametrize("url, username, password", [(scale_url, Lab_order_user, password)])
def test_lab_order_1(login):

    time.sleep(3)
    try:
        
        wait = WebDriverWait(login, 20)
        # order_element = wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//img)[3]"))
        # )
        # order_element.click()

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

        fake_india = Faker('en_IN')

        # Generate individual components
        street_address = fake_india.street_address()
        city = fake_india.city()
        state = fake_india.state()
        country = fake_india.country()

        # Combine into full address
        full_address = f"{street_address}, {city}, {state}, {country}"
        print(full_address)


        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[1]"))
        ).send_keys(phonenumber)

        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[contains(text(),'Verify')])[1]"))
        # ).click()

        # otp_digits = "55555"
        # # Wait for the OTP input fields to be present
        # otp_inputs = WebDriverWait(login, 10).until(
        #     EC.presence_of_all_elements_located(
        #         (By.XPATH, "//input[contains(@id, 'otp_')]")
        #     )
        # )

        # # print("Number of OTP input fields:", len(otp_inputs))
        # # print(otp_inputs)

        # for i, otp_input in enumerate(otp_inputs):

        #     # print(i)
        #     # print(otp_input)
        #     otp_input.send_keys(otp_digits[i])

        # snack_bar = WebDriverWait(login, 10).until(
        #         EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        # )
        # message = snack_bar.text
        # print("Snack bar message:", message)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[2]"))
        ).send_keys(phonenumber)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[3]"))
        ).send_keys(phonenumber)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Clinic Email'])[1]"))
        ).send_keys(email)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Location'])[1]"))
        ).click()

        time.sleep(1)

        try:
            # Locate the input field using XPath
            input_field = login.find_element(By.XPATH, "//input[@id='pac-input']")

            # Input "Thrissur" into the text field
            input_field.send_keys("Thrissur")
            time.sleep(3)

            # Wait for the suggestions to appear and select the appropriate one
            wait = WebDriverWait(login, 10)
            suggestions = wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='pac-item']"))
            )

            time.sleep(3)

            # Iterate through the suggestions and select the one that matches "Thrissur, Kerala, India"
            for suggestion in suggestions:
                if "Thrissur, Kerala, India" in suggestion.text:
                    suggestion.click()
                    break

        finally:
            print("Loaction : Thrissur, Kerala, India")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='mdc-button__label'])[1]"))
        ).click()

        time.sleep(5)
        Address_1 = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Address 1'])[1]"))
        )
        Address_1.send_keys(full_address)

        time.sleep(3)
        Address_2 = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Address 2'])[1]"))
        )
        Address_2.send_keys(full_address)
 
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Area'])[1]"))
        ).send_keys("Thrissur")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter City'])[1]"))
        ).send_keys("Thrissur")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter District'])[1]"))
        ).send_keys("Thrissur")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@class='p-dropdown-filter p-inputtext p-component'])[1]"))
        ).send_keys("Ker") 

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Kerala'])[1]"))
        ).click()

        time.sleep(1)   
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Pincode'])[1]"))
        ).send_keys("680505")

        # time.sleep(1)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        # ).click()

        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Clinic'])[1]"))
        # ).click()

        time.sleep(1)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create Clinic'])[1]"))
        ).click()

        toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_detail.text
        print("toast_Message:", message)

        time.sleep(3)
        
    
        Assigned_status_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space(.)='Approval Pending'])[1]"))
        )
        Assigned_status_text = Assigned_status_element.text
        print(f"Status: {Assigned_status_text}")
        assert Assigned_status_text == "Approval Pending", f"Expected 'Approval Pending' status, but got {Assigned_status_text}"

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[contains(text(),'Update')])[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Send for Approval'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element btn fw-bold p-button-light p-button p-component ng-star-inserted'][normalize-space()='View'])[1]"))
        ).click() 

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space(.)='Approve']"))
        ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//div[@class='btn-sanctioned mr-2 pointer-cursor'])[1]"))
        # ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@placeholder='Enter Remarks'])[1]"))
        ).send_keys("Approve the clinic")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='btn btn-primary'][normalize-space()='Approve'])[1]"))
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

        time.sleep(3)

        status_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//tr[contains(@class, 'mobile-card')])[1]/td[4]/span[2]"))
        )

        # Get the text and assert
        status_text = status_element.text.strip()
        assert status_text == "Approved", f"Expected status to be 'Approved' but got '{status_text}'"

        print("Status is correctly set to 'Approved'.")


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
@allure.title("Test Case: Create Lab Order Item")
@pytest.mark.parametrize("url, username, password", [(scale_url, Lab_order_user, password)])
def test_lab_order_2(login):

    time.sleep(5)
    try:
        
        wait = WebDriverWait(login, 20)
        # order_element = wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//img)[3]"))
        # )
        # order_element.click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Items'])[1]"))
        ).click()


        time.sleep(2)   
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Create'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Item Name'])[1]"))
        ).send_keys("Item" + str(uuid.uuid4())[:4])

        time.sleep(1)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        # ).click()

        # time.sleep(1)   
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[normalize-space()='Lab Items'])[1]"))
        # ).click()

        # time.sleep(1)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "   (//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        # ).click()

        # time.sleep(1)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[normalize-space()='Lab Items'])[1]"))
        # ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@placeholder='Enter Item Description'])[1]"))
        ).send_keys("Lab order Item description")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Create Item'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        


    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Create Lab Order Store")
@pytest.mark.parametrize("url, username, password", [(scale_url, Lab_order_user, password)])
def test_lab_order_3(login):

    time.sleep(5)
    try:
 
        wait = WebDriverWait(login, 20)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Stores')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Create Store'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        select_option_1 = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='OTHERS'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", select_option_1)
        select_option_1.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Name'])[1]"))
        ).send_keys("Store" + str(uuid.uuid4())[:4])

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[1]"))
        ).send_keys(phonenumber)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='email'])[1]"))
        ).send_keys(email)

        time.sleep(1)   
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Invoice prefix'])[1]"))
        ).send_keys("INV" + str(uuid.uuid1())[:2])

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        location_option = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Round North'])[1]"))
        )
        location_option.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()

    
        # snack_bar = WebDriverWait(login, 10).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        # )
        # message = snack_bar.text
        # print("Snack bar message:", message)

       
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
@allure.title("Test Case: Delivery failed order")
@pytest.mark.parametrize("url, username, password", [(scale_url, Lab_order_user, password)])
def test_lab_order_4(login):

    time.sleep(5)
    try:
        
        time.sleep(5)
        wait = WebDriverWait(login, 30)

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
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Pirme Clinic'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", clinic_option)

        clinic_option.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[5]"))
        ).click()

        store_option = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Aster Dental'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", store_option)
        store_option.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Next'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Add Item'])[1]"))
        ).click()

        time.sleep(3)
        checkbox = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//mat-checkbox[contains(@class, 'mat-mdc-checkbox')]//input[@type='checkbox'])[1]"))
        )
        login.execute_script("arguments[0].click()", checkbox)

        time.sleep(2)

        time.sleep(3)
        # Questionnaire

        random_form_number = random.randint(100, 9999)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter form number'])[1]"))
        ).send_keys(str(random_form_number))

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)

        today_element = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
        (By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")
                )
        )          

        # Click using JavaScript in case normal click doesn't work
        login.execute_script("arguments[0].click();", today_element)

        print("Clicked today's date:", today_element.text)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Please enter the doctor’s name'])[1]"))
        ).send_keys("Naveen P")

        time.sleep(2)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Please enter the patient name'])[1]"))
        ).send_keys(f"{first_name} {last_name}")

        time.sleep(1)

        random_age = random.randint(23, 65)
        print("Random Age:", random_age)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Age'])[1]"))
        ).send_keys(str(random_age)) 

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Male'])[1]"))
        ).click()

        prosthesis_types = [
        "Complete Denture",
        "Partial Denture",
        "Fixed Bridge",
        "Crown",
        "Implant",
        "Implant-Supported Denture",
        "Veneer",
        "Inlay",
        "Onlay",
        "Orthodontic Appliance"
        ]

        random_type = random.choice(prosthesis_types)
        print("Random Prosthesis Type:", random_type)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Prosthesis Type'])[1]"))
        ).send_keys(random_type)

        time.sleep(2)

        # Locate all the circle elements inside the quadrant-container
        circles = login.find_elements(By.CSS_SELECTOR, ".quadrant-container .circle")

        # Randomly choose 4 or 5 distinct circles
        num_to_select = random.choice([4, 5])
        selected_circles = random.sample(circles, num_to_select)

        # Click on each selected circle
        for circle in selected_circles:
            print(f"Clicking on: {circle.text.strip()}")
            login.execute_script("arguments[0].scrollIntoView(true);", circle)
            circle.click()


        time.sleep(2)
        Pontic_types = [
        "Saddle Pontic",
        "Modified Ridge Lap Pontic",
        "Conical Pontic",
        "Ovate Pontic",
        "Prefabricated Pontics"
         ]

        random_pontic_type = random.choice(prosthesis_types)
        print("Random Pontic types:", random_pontic_type)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Type Of Ponti'])[1]"))
        ).send_keys(random_pontic_type)


        time.sleep(2)
        Shade_types = [
        "Reddish-Brownish",
        "Reddish-Yellowish",
        "Greyish",
        "Reddish-Grey"
       	]

        random_Shade_types = random.choice(Shade_types)
        print("Random Pontic types:", random_Shade_types)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Shade'])[1]"))
        ).send_keys(random_Shade_types)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Yes'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]"))
        ).click()

        time.sleep(2)
        
        future_date = datetime.now() + timedelta(days=4)
        future_day = str(future_date.day)

        # XPath to locate the cell containing the desired date
        date_xpath = f"//td[not(contains(@class,'p-datepicker-other-month'))]//span[text()='{future_day}']"

        # Wait for and click the date
        future_date_element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        login.execute_script("arguments[0].click();", future_date_element)

        print("Clicked future date (+4):", future_date_element.text)


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Yes'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[3]"))
        ).click()
        time.sleep(2)
        
        future_date = datetime.now() + timedelta(days=6)
        future_day = str(future_date.day)

        # XPath to locate the cell containing the desired date
        date_xpath = f"//td[not(contains(@class,'p-datepicker-other-month'))]//span[text()='{future_day}']"

        # Wait for and click the date
        future_date_element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        login.execute_script("arguments[0].click();", future_date_element)

        print("Clicked future date (+6):", future_date_element.text)


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Final Finish'])[1]"))
        ).send_keys("Final Finish")
        
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[4]"))
        ).click()

        time.sleep(2)
        
        future_date = datetime.now() + timedelta(days=10)
        future_day = str(future_date.day)

        # XPath to locate the cell containing the desired date
        date_xpath = f"//td[not(contains(@class,'p-datepicker-other-month'))]//span[text()='{future_day}']"

        # Wait for and click the date
        future_date_element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        login.execute_script("arguments[0].click();", future_date_element)

        print("Clicked future date (+10):", future_date_element.text)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter your notes'])[1]"))
        ).send_keys("Some notes")   

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Confirm Order'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Create Invoice'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='View Invoice'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Share Payment Link'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
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

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Complete Order'])[1]"))
        ).click()

        toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_detail.text
        print("toast_Message:", message)

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Pass To Delivery'])[1]"))
        ).click()


        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@name='radioBtn'])[1]"))
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
                (By.XPATH, "//span[@class='mdc-list-item__primary-text'][normalize-space()='Dispatched']"))
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
                (By.XPATH, "(//span[normalize-space(.)='Dispatched'])[1]"))
        )
        pickup_status_text = pickup_status_element.text
        print(f"Status: {pickup_status_text}")
        assert pickup_status_text == "Dispatched", f"Expected 'Dispatched' status, but got {pickup_status_text}"

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Change Status'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='mdc-list-item__primary-text'][normalize-space()='Delivery Failed'])[1]"))
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
                (By.XPATH, "(//span[normalize-space(.)='DELIVERY FAILED'])[1]"))
        )
        In_Transist_status_text = In_Transist_status_element.text
        print(f"Status: {In_Transist_status_text}")
        assert In_Transist_status_text == "DELIVERY FAILED", f"Expected 'DELIVERY FAILED' status, but got {In_Transist_status_text}"
        

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
@allure.title("Test Case: Delivery failed order")
@pytest.mark.parametrize("url, username, password", [(scale_url, Lab_order_user, password)])
def test_lab_order_5(login):

    try:  
        time.sleep(5)
        wait = WebDriverWait(login, 30)

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
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Pirme Clinic'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", clinic_option)

        clinic_option.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[5]"))
        ).click()

        store_option = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Aster Dental'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", store_option)
        store_option.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Next'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Add Item'])[1]"))
        ).click()

        time.sleep(3)
        checkbox = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//mat-checkbox[contains(@class, 'mat-mdc-checkbox')]//input[@type='checkbox'])[1]"))
        )
        login.execute_script("arguments[0].click()", checkbox)

        time.sleep(2)

        time.sleep(3)
        # Questionnaire

        random_form_number = random.randint(100, 9999)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter form number'])[1]"))
        ).send_keys(str(random_form_number))

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)

        today_element = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
        (By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")
                )
        )          

        # Click using JavaScript in case normal click doesn't work
        login.execute_script("arguments[0].click();", today_element)

        print("Clicked today's date:", today_element.text)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Please enter the doctor’s name'])[1]"))
        ).send_keys("Naveen P")

        time.sleep(2)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Please enter the patient name'])[1]"))
        ).send_keys(f"{first_name} {last_name}")

        time.sleep(1)

        random_age = random.randint(23, 65)
        print("Random Age:", random_age)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Age'])[1]"))
        ).send_keys(str(random_age)) 

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Male'])[1]"))
        ).click()

        prosthesis_types = [
        "Complete Denture",
        "Partial Denture",
        "Fixed Bridge",
        "Crown",
        "Implant",
        "Implant-Supported Denture",
        "Veneer",
        "Inlay",
        "Onlay",
        "Orthodontic Appliance"
        ]

        random_type = random.choice(prosthesis_types)
        print("Random Prosthesis Type:", random_type)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Prosthesis Type'])[1]"))
        ).send_keys(random_type)

        time.sleep(2)

        # Locate all the circle elements inside the quadrant-container
        circles = login.find_elements(By.CSS_SELECTOR, ".quadrant-container .circle")

        # Randomly choose 4 or 5 distinct circles
        num_to_select = random.choice([4, 5])
        selected_circles = random.sample(circles, num_to_select)

        # Click on each selected circle
        for circle in selected_circles:
            print(f"Clicking on: {circle.text.strip()}")
            login.execute_script("arguments[0].scrollIntoView(true);", circle)
            circle.click()


        time.sleep(2)
        Pontic_types = [
        "Saddle Pontic",
        "Modified Ridge Lap Pontic",
        "Conical Pontic",
        "Ovate Pontic",
        "Prefabricated Pontics"
         ]

        random_pontic_type = random.choice(prosthesis_types)
        print("Random Pontic types:", random_pontic_type)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Type Of Ponti'])[1]"))
        ).send_keys(random_pontic_type)


        time.sleep(2)
        Shade_types = [
        "Reddish-Brownish",
        "Reddish-Yellowish",
        "Greyish",
        "Reddish-Grey"
       	]

        random_Shade_types = random.choice(Shade_types)
        print("Random Pontic types:", random_Shade_types)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Shade'])[1]"))
        ).send_keys(random_Shade_types)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Yes'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]"))
        ).click()

        time.sleep(2)
        
        future_date = datetime.now() + timedelta(days=4)
        future_day = str(future_date.day)

        # XPath to locate the cell containing the desired date
        date_xpath = f"//td[not(contains(@class,'p-datepicker-other-month'))]//span[text()='{future_day}']"

        # Wait for and click the date
        future_date_element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        login.execute_script("arguments[0].click();", future_date_element)

        print("Clicked future date (+4):", future_date_element.text)


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Yes'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[3]"))
        ).click()
        time.sleep(2)
        
        future_date = datetime.now() + timedelta(days=6)
        future_day = str(future_date.day)

        # XPath to locate the cell containing the desired date
        date_xpath = f"//td[not(contains(@class,'p-datepicker-other-month'))]//span[text()='{future_day}']"

        # Wait for and click the date
        future_date_element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        login.execute_script("arguments[0].click();", future_date_element)

        print("Clicked future date (+6):", future_date_element.text)


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Final Finish'])[1]"))
        ).send_keys("Final Finish")
        
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[4]"))
        ).click()

        time.sleep(2)
        
        future_date = datetime.now() + timedelta(days=10)
        future_day = str(future_date.day)

        # XPath to locate the cell containing the desired date
        date_xpath = f"//td[not(contains(@class,'p-datepicker-other-month'))]//span[text()='{future_day}']"

        # Wait for and click the date
        future_date_element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        login.execute_script("arguments[0].click();", future_date_element)

        print("Clicked future date (+10):", future_date_element.text)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter your notes'])[1]"))
        ).send_keys("Some notes")   

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Confirm Order'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Create Invoice'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='View Invoice'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Share Payment Link'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
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

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Complete Order'])[1]"))
        ).click()

        toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_detail.text
        print("toast_Message:", message)

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Pass To Delivery'])[1]"))
        ).click()
        

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@name='radioBtn'])[1]"))
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

        # Assigned_status_element = wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[normalize-space()='ASSIGNED'])[1]"))
        # )
        # Assigned_status_text = Assigned_status_element.text
        # print(f"Status: {Assigned_status_text}")
        # assert Assigned_status_text == "ASSIGNED", f"Expected 'ASSIGNED' status, but got {Assigned_status_text}"

        # time.sleep(1)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//button[normalize-space()='Change Status'])[1]"))
        # ).click()

        # time.sleep(1)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[normalize-space()='Rejected'])[1]"))
        # ).click()

        # try:

        #     snack_bar = WebDriverWait(login, 10).until(
        #         EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        #     )
        #     message = snack_bar.text
        #     print("Snack bar message:", message)

        # except:

        #     snack_bar = WebDriverWait(login, 10).until(
        #         EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
        #     )
        #     message = snack_bar.text
        #     print("Snack bar message:", message)

        # Accepted_status_element = wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[normalize-space()='ACCEPTED'])[1]"))
        # )
        # Accepted_status_text = Accepted_status_element.text
        # print(f"Status: {Accepted_status_text}")
        # assert Accepted_status_text == "ACCEPTED", f"Expected 'ACCEPTED' status, but got {Accepted_status_text}"

        time.sleep(3)
        home_button = WebDriverWait(login, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@id='kt_quick_user_toggle']//span[contains(@class, 'bname')]")
        )
        )
        login.execute_script("arguments[0].click();", home_button)

        time.sleep(3)
        signout_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Sign Out']"))
        )
        login.execute_script("arguments[0].click();", signout_button)

        # Re-login to verify options
        print("Login with Sales officer")
        login_id = login.find_element(By.XPATH, "//input[@id='loginId']")
        login_id.clear()
        login_id.send_keys("ArchanaS")

        password = login.find_element(By.XPATH, "//input[@id='password']")
        password.clear()
        password.send_keys("Jaldee01")

        login.find_element(By.XPATH, "//button[@type='submit']").click()


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@aria-haspopup='menu'][normalize-space()='Status'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Rejected'])[1]"))
        ).click()

       

        time.sleep(3)



    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    