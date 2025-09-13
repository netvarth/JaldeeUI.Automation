from Framework.common_utils import *
from Framework.common_dates_utils import *
import random

from faker import Faker

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Basic workflow of IP Mangement")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_workflow_New_IP_Patient(login):

    wait = WebDriverWait(login, 20)
    try:
        time.sleep(5)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='dashboard-card-image'])[6]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        ).click()

        # time.sleep(1)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        # ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        drop_downlist = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal Room'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", drop_downlist)
        time.sleep(1)   
        drop_downlist.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Private Room'])[1]"))
        ).click()


        room_name = get_next_room_name()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Room Name'])[1]")
            )
        ).send_keys(room_name)

        print(f"🏨 Room created: {room_name}")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[5]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Room'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()
    
        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='Room Details'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()
        
        time.sleep(1)
        bed_type = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_type)
        time.sleep(1)
        bed_type.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Observation Beds'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        bed_price = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Manual Hospital Bed'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_price)
        time.sleep(1)
        bed_price.click()


        bed_name  = f'Bed{room_name}'
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Bed Name'])[1]"))
        ).send_keys(bed_name)   

        time.sleep(1)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()   

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)



        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(5)  
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'New Admission')])[1]"))
        ).click()

        time.sleep(3)
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

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Last Name'])[1]"))
        ).send_keys(last_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Email Id'])[1]"))
        ).send_keys(email)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[1]"))
        ).send_keys(phonenumber)

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

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save & Next'])[1]"))
        ).click()

        
        time.sleep(2)
        admission_dropdown = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        )
        admission_dropdown.click()

        # Wait and fetch all options in the dropdown
        dropdown_options = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@role='listbox' and contains(@class, 'p-dropdown-items')]/p-dropdownitem/li")
            )
        )

        # Randomly choose and click one option
        random_option = random.choice(dropdown_options)
        random_option_text = random_option.text.strip()
        random_option.click()

        print(f"✅ Randomly selected admission type: {random_option_text}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        time.sleep(2)

        today_element = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
        (By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")
                )
        )          

        # Click using JavaScript in case normal click doesn't work
        login.execute_script("arguments[0].click();", today_element)

        print("Clicked today's date:", today_element.text)


        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]"))
        ).click()

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=3)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        print("future day: ", future_day)
        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 10  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
        else:
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # ✅ Click the future day but only inside the correct month/year panel
        date_xpath = (
        f"//td[not(contains(@class,'p-disabled')) "
        f"and not(contains(@class,'p-datepicker-other-month'))]"
        f"//span[normalize-space()='{future_day}']"
        )

        target_date = wait.until(EC.element_to_be_clickable((By.XPATH, date_xpath)))
        login.execute_script("arguments[0].click();", target_date)
        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")
            )
        ).click()                                                                                                                                            
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Second Floor B'])[1]"))
        ).click()
 

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"))
        ).click()

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space(.)='Admit Now'])[1]")
            )
        ).click()

        
        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
       
        time.sleep(5)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Medical Record')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='+ Add New Visit'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()   

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Visit'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)    
        
        time.sleep(5)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Services'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-plus'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Search Service'])[1]"))
        ).send_keys("Doc")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//li[@role='option'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[3]")
        time.sleep(1)
        # Locate the minute up arrow
        minute_up_button = login.find_element(By.XPATH, "//div[contains(@class,'p-minute-picker')]//button[1]")

        # Click it 10 times
        for _ in range(3):
            minute_up_button.click()
            time.sleep(0.5)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]", "2")
      
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Service'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Medical Records'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Vital Signs'])[1]"))
        ).click()

        # Generate vitals
        temp = generate_temperature_f()
        pulse = generate_pulse_rate()
        resp = generate_respiration_rate()
        systolic, diastolic = generate_blood_pressure()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Temperature in °F , Max : 200'])[1]"))
        ).send_keys(str(temp))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Pulse Rate , Max : 999'])[1]"))
        ).send_keys(str(pulse))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Respiration , Max : 90'])[1]"))
        ).send_keys(str(resp))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Systolic , Max : 500'])[1]"))
        ).send_keys(str(systolic))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Diastolic , Max : 500'])[1]"))
        ).send_keys(str(diastolic))

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save'])[1]"))
            
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'p-toast-message')]"))
        ).text
        print("Toast Message:", toast_message)


        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Prescription'])[1]"))
        ).click()

        time.sleep(2)
        for i in range(5):
            login.find_element(
                By.XPATH, "//button[normalize-space()='+ Add Medicine']"
            ).click()
            login.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(
                "Medicine"
            )

            # Scope to the prescription modal dialog
            
            before_XPath = "//mat-dialog-container[@role='dialog' and contains(@class, 'mat-mdc-dialog-container')]//table[contains(@class, 'p-datatable-table')]//tbody/tr"
            aftertd_XPath_1 = "/td[2]"
            aftertd_XPath_2 = "/td[3]"
            aftertd_XPath_3 = "/td[4]"
            aftertd_XPath_4 = "/td[5]"
            textarea_xpath = "//input[@role='searchbox']"
            row = i + 1
            if i > 0:
                trXPath = before_XPath + str([row])
            else:
                trXPath = before_XPath

            PreFinalXPath = trXPath + aftertd_XPath_1
            FinalXPath = PreFinalXPath + textarea_xpath

            Dose = login.find_element(By.XPATH, PreFinalXPath)
            Dose.click()
            Dose1 = login.find_element(By.XPATH, FinalXPath)
            Dose1.send_keys("650 mg")

            PreFinalXPath = trXPath + aftertd_XPath_2
            FinalXPath = PreFinalXPath + textarea_xpath

            Frequency = login.find_element(By.XPATH, PreFinalXPath)
            Frequency.click()
            Frequency1 = login.find_element(By.XPATH, FinalXPath)
            Frequency1.send_keys("1-1-1")

            PreFinalXPath = trXPath + aftertd_XPath_3
            FinalXPath = PreFinalXPath + textarea_xpath
            Duration = login.find_element(By.XPATH, PreFinalXPath)
            Duration.click()
            Duration1 = login.find_element(By.XPATH, FinalXPath)
            Duration1.send_keys("5 Days")

            PreFinalXPath = trXPath + aftertd_XPath_4
            FinalXPath = PreFinalXPath + textarea_xpath
            Notes = login.find_element(By.XPATH, PreFinalXPath)
            Notes.click()
            Notes1 = login.find_element(By.XPATH, FinalXPath)
            Notes1.send_keys("After Food")

        time.sleep(5)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save'])[1]"))
        ).click()

        
        
        time.sleep(3)
        share_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'Share')])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", share_button)
        time.sleep(2)
        share_button.click()
        
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@placeholder='Enter message description'])[1]"))
        ).send_keys("This is a test message.")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Email'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Whatsapp'])[1]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@type='button'][normalize-space()='Share'])[1]"))
        ).click()

        time.sleep(3) 
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Transfer Bed')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='First Floor B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal ICU'])[1]"))
        ).click()

        time.sleep(2)          

        # Find all bed cards
        bed_cards = login.find_elements(By.XPATH, "//div[contains(@class, 'bed-card')]")

        # Randomly choose one bed
        random_bed = random.choice(bed_cards)

        # Click the "Select Bed" button inside that bed-card
        select_button = random_bed.find_element(By.XPATH, ".//button[contains(text(), 'Select Bed')]")
        select_button.click()

        # (Optional) Print which bed was selected
        bed_name = random_bed.find_element(By.XPATH, ".//span[contains(@class, 'bed-title')]").text
        print(f"Selected Bed: {bed_name}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        today_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        today_date.click()
        print("Clicked today's date:", today_date.text)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save & Transfer'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)    

        time.sleep(3)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]"))
        # ).click()

        # time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Transfer Bed')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Select Bed'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        today_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        today_date.click()
        print("Clicked today's date:", today_date.text)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[normalize-space()='No'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save & Transfer'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)
       

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='my-1 font-small fw-bold text-capitalize ng-star-inserted'][normalize-space(.)='Discharge'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Use Template'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Use template'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        discharge_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space(.)='Discharge'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", discharge_button)

        time.sleep(2)
        discharge_button.click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        # Wait for the discharge status to appear
        discharge_status_xpath = "//div[contains(@class, 'status-discharged') and normalize-space()='Discharged']"
        WebDriverWait(login, 10).until(EC.visibility_of_element_located((By.XPATH, discharge_status_xpath)))

        # Assert that the "Discharged" status is displayed
        discharge_status_element = login.find_element(By.XPATH, discharge_status_xpath)
        assert discharge_status_element.is_displayed(), "Discharge status is not visible after discharge."

        print("✅ Discharge status is visible after discharge.")

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Invoices')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-plus'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[1]"))
        ).click()

        time.sleep(2)  
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space(.)='Generate'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space(.)='Generate Invoice'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Pay by Others'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Pay'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
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
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()
    
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Checkout'])[1]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@type='button'][normalize-space()='Checkout'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)
 
        time.sleep(3)
        # XPath for "Checked Out" status
        checkout_xpath = "//div[contains(@class, 'status-checkout') and normalize-space()='Checked Out']"

        # Wait for the element to be visible
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, checkout_xpath))
        )

        # Assert the element is displayed
        checkout_status = login.find_element(By.XPATH, checkout_xpath)
        assert checkout_status.is_displayed(), "'Checked Out' status is not visible."

        print("✅ Checked Out status is visible after checkout.")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Checked Out'])[1]"))
        ).click()

    


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
@allure.title("Test Case: Basic workflow of IP Mangement with Reservations")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_workflow_Reservations(login):


    wait = WebDriverWait(login, 20)
    try:
        time.sleep(5)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()


        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='dashboard-card-image'])[6]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1] "))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        drop_downlist = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal Room'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", drop_downlist)
        time.sleep(1)   
        drop_downlist.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Private Room'])[1]"))
        ).click()


        room_name = get_next_room_name()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Room Name'])[1]")
            )
        ).send_keys(room_name)

        print(f"🏨 Room created: {room_name}")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[5]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Room'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()
    
        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='Room Details'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Yes'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()
        
        time.sleep(1)
        bed_type = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_type)
        time.sleep(1)
        bed_type.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Observation Beds'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        bed_price = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Manual Hospital Bed'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_price)
        time.sleep(1)
        bed_price.click()


        bed_name  = f'Bed{room_name}'
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Bed Name'])[1]"))
        ).send_keys(bed_name)   

        time.sleep(1)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()   

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)



        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(5)  
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'New Admission')])[1]"))
        ).click()

        time.sleep(3)
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

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Last Name'])[1]"))
        ).send_keys(last_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Email Id'])[1]"))
        ).send_keys(email)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[1]"))
        ).send_keys(phonenumber)

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

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save & Next'])[1]"))
        ).click()


        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[normalize-space()='Reserve'])[1]"))
        ).click()

        time.sleep(2)
        admission_dropdown = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        )
        admission_dropdown.click()

        # Wait and fetch all options in the dropdown
        dropdown_options = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@role='listbox' and contains(@class, 'p-dropdown-items')]/p-dropdownitem/li")
            )
        )

        # Randomly choose and click one option
        random_option = random.choice(dropdown_options)
        random_option_text = random_option.text.strip()
        random_option.click()

        print(f"✅ Randomly selected admission type: {random_option_text}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        time.sleep(2)

        today_element = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
        (By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")
                )
        )          

        # Click using JavaScript in case normal click doesn't work
        login.execute_script("arguments[0].click();", today_element)

        print("Clicked today's date:", today_element.text)


        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]"))
        ).click()

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=3)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
        else:
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")
            )
        ).click()





        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"))
        ).click()

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()
        
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Reserve Now'])[1]"))
        ).click()


        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(5)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'Admit')])[1]"))
        ).click()

        time.sleep(2)
        admit_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Admit'])[1]"))
        )
        login.execute_script("arguments[0].click();", admit_button)

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(5)
        view_button = wait.until(
             EC.presence_of_element_located((By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]"))
        )
        login.execute_script("arguments[0].click();", view_button)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Medical Record')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='+ Add New Visit'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()   

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Visit'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)    
        
        time.sleep(5)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Services'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-plus'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Search Service'])[1]"))
        ).send_keys("Doc")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//li[@role='option'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[3]")
        time.sleep(1)
        # Locate the minute up arrow
        minute_up_button = login.find_element(By.XPATH, "//div[contains(@class,'p-minute-picker')]//button[1]")

        # Click it 10 times
        for _ in range(3):
            minute_up_button.click()
            time.sleep(0.5)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]", "2")
      
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Service'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Medical Records'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Vital Signs'])[1]"))
        ).click()

        # Generate vitals
        temp = generate_temperature_f()
        pulse = generate_pulse_rate()
        resp = generate_respiration_rate()
        systolic, diastolic = generate_blood_pressure()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Temperature in °F , Max : 200'])[1]"))
        ).send_keys(str(temp))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Pulse Rate , Max : 999'])[1]"))
        ).send_keys(str(pulse))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Respiration , Max : 90'])[1]"))
        ).send_keys(str(resp))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Systolic , Max : 500'])[1]"))
        ).send_keys(str(systolic))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Diastolic , Max : 500'])[1]"))
        ).send_keys(str(diastolic))

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save'])[1]"))
            
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(5)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Prescription'])[1]"))
        ).click()

        time.sleep(2)
        for i in range(5):
            login.find_element(
                By.XPATH, "//button[normalize-space()='+ Add Medicine']"
            ).click()
            login.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(
                "Medicine"
            )

            # Scope to the prescription modal dialog
            
            before_XPath = "//mat-dialog-container[@role='dialog' and contains(@class, 'mat-mdc-dialog-container')]//table[contains(@class, 'p-datatable-table')]//tbody/tr"
            aftertd_XPath_1 = "/td[2]"
            aftertd_XPath_2 = "/td[3]"
            aftertd_XPath_3 = "/td[4]"
            aftertd_XPath_4 = "/td[5]"
            textarea_xpath = "//input[@role='searchbox']"
            row = i + 1
            if i > 0:
                trXPath = before_XPath + str([row])
            else:
                trXPath = before_XPath

            PreFinalXPath = trXPath + aftertd_XPath_1
            FinalXPath = PreFinalXPath + textarea_xpath

            Dose = login.find_element(By.XPATH, PreFinalXPath)
            Dose.click()
            Dose1 = login.find_element(By.XPATH, FinalXPath)
            Dose1.send_keys("650 mg")

            PreFinalXPath = trXPath + aftertd_XPath_2
            FinalXPath = PreFinalXPath + textarea_xpath

            Frequency = login.find_element(By.XPATH, PreFinalXPath)
            Frequency.click()
            Frequency1 = login.find_element(By.XPATH, FinalXPath)
            Frequency1.send_keys("1-1-1")

            PreFinalXPath = trXPath + aftertd_XPath_3
            FinalXPath = PreFinalXPath + textarea_xpath
            Duration = login.find_element(By.XPATH, PreFinalXPath)
            Duration.click()
            Duration1 = login.find_element(By.XPATH, FinalXPath)
            Duration1.send_keys("5 Days")

            PreFinalXPath = trXPath + aftertd_XPath_4
            FinalXPath = PreFinalXPath + textarea_xpath
            Notes = login.find_element(By.XPATH, PreFinalXPath)
            Notes.click()
            Notes1 = login.find_element(By.XPATH, FinalXPath)
            Notes1.send_keys("After Food")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save'])[1]"))
        ).click()
        
        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'Share')])[1]"))
        ).click()
        
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@placeholder='Enter message description'])[1]"))
        ).send_keys("This is a test message.")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Email'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Whatsapp'])[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@type='button'][normalize-space()='Share'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)


        time.sleep(3)
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Transfer Bed')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='First Floor B'])[1]"))
        ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//button[@type='button'])[2]"))
        # ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal ICU'])[1]"))
        ).click()

        time.sleep(2)          

        # Find all bed cards
        bed_cards = login.find_elements(By.XPATH, "//div[contains(@class, 'bed-card')]")

        # Randomly choose one bed
        random_bed = random.choice(bed_cards)

        # Click the "Select Bed" button inside that bed-card
        select_button = random_bed.find_element(By.XPATH, ".//button[contains(text(), 'Select Bed')]")
        select_button.click()

        # (Optional) Print which bed was selected
        bed_name = random_bed.find_element(By.XPATH, ".//span[contains(@class, 'bed-title')]").text
        print(f"Selected Bed: {bed_name}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        today_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        today_date.click()
        print("Clicked today's date:", today_date.text)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save & Transfer'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)    

        # time.sleep(3)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]"))
        # ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Transfer Bed')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Select Bed'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        today_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        today_date.click()
        print("Clicked today's date:", today_date.text)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[normalize-space()='No'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save & Transfer'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)


        # time.sleep(3)
        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'View')])[1]"))
        # ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Discharge')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Use Template'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Use template'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Discharge'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        # Wait for the discharge status to appear
        discharge_status_xpath = "//div[contains(@class, 'status-discharged') and normalize-space()='Discharged']"
        WebDriverWait(login, 10).until(EC.visibility_of_element_located((By.XPATH, discharge_status_xpath)))

        # Assert that the "Discharged" status is displayed
        discharge_status_element = login.find_element(By.XPATH, discharge_status_xpath)
        assert discharge_status_element.is_displayed(), "Discharge status is not visible after discharge."

        print("✅ Discharge status is visible after discharge.")

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Invoices')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-plus'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[1]"))
        ).click()

        time.sleep(2)  
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space(.)='Generate'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space(.)='Generate Invoice'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Pay by Others'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Pay'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
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
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()


        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Checkout'])[1]"))
        ).click()

        

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@type='button'][normalize-space()='Checkout'])[1]"))
        ).click()

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Yes'])[1]")

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        # XPath for "Checked Out" status
        checkout_xpath = "//div[contains(@class, 'status-checkout') and normalize-space()='Checked Out']"

        # Wait for the element to be visible
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, checkout_xpath))
        )

        # Assert the element is displayed
        checkout_status = login.find_element(By.XPATH, checkout_xpath)
        assert checkout_status.is_displayed(), "'Checked Out' status is not visible."

        print("✅ Checked Out status is visible after checkout.")



        time.sleep(10)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Basic workflow of IP Mangement to Convert Patient to IP Patient")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)]) 
def test_IP_workflow_Patient_to_IP_Patient(login):


    wait = WebDriverWait(login, 20)
    try: 
        time.sleep(5)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='dashboard-card-image'])[6]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(., 'Create Room')]"))
        ).click()           

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        ).click()

        # time.sleep(1)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        # ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        drop_downlist = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal Room'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", drop_downlist)
        time.sleep(1)   
        drop_downlist.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Private Room'])[1]"))
        ).click()


        room_name = get_next_room_name()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Room Name'])[1]")
            )
        ).send_keys(room_name)

        print(f"🏨 Room created: {room_name}")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[5]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Room'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()
    
        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='Room Details'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Yes'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()
        
        time.sleep(1)
        bed_type = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_type)
        time.sleep(1)
        bed_type.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Observation Beds'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        bed_price = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Manual Hospital Bed'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_price)
        time.sleep(1)
        bed_price.click()


        bed_name  = f'Bed{room_name}'
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Bed Name'])[1]"))
        ).send_keys(bed_name)   

        time.sleep(1)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()   

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)



        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[7]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img[@src='assets/images/add-cust.svg'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img[@alt='add Patient'])[1]"))
        ).click()

        time.sleep(2)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='first_name'])[1]"))
        ).send_keys(first_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='last_name'])[1]"))
        ).send_keys(last_name)


        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='email_id'])[1]"))
        ).send_keys(email)

        time.sleep(1)   
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[1]"))
        ).send_keys(phonenumber)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[normalize-space()='Male'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)   
        # Click on the "2025" button
        login.find_element(By.XPATH, "//button[normalize-space()='2025']").click()

        # Wait until the backward arrow is clickable before clicking it
        backward_arrow = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'p-ripple') and contains(@class, 'p-element') and contains(@class, 'p-datepicker-prev') and contains(@class, 'p-link') and contains(@class, 'ng-star-inserted')]")
            )
        )

        # Clicking backward arrows 4 times to navigate to the correct year
        for _ in range(4):
            backward_arrow.click()

        # Generate Date of Birth (DOB)
        [year, month, day] = Generate_dob()
        print(f"Year: {year}, Month: {month}, Day: {day}")
        time.sleep(1)
        # Select Year
        year_xpath = f"//span[normalize-space()='{year}']"
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, year_xpath))
        ).click()
        time.sleep(1)
        # Select Month
        month_xpath = f"//span[normalize-space()='{month}']"
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, month_xpath))
        ).click()

        time.sleep(2)
        # Select Day
        day = str(int(day))  # Ensuring day is in integer form
        day_xpath = f"//span[normalize-space()='{day}']"
        select_day = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, day_xpath))
        )
        select_day.click()

        print(f"Selected Date of Birth: {day}-{month}-{year}")
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Save'])[1]"))
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
                (By.XPATH, "(//img)[19]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Create IP Admission'])[1]"))
        ).click()


        time.sleep(2)
        admission_dropdown = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        )
        admission_dropdown.click()

        # Wait and fetch all options in the dropdown
        dropdown_options = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@role='listbox' and contains(@class, 'p-dropdown-items')]/p-dropdownitem/li")
            )
        )

        # Randomly choose and click one option
        random_option = random.choice(dropdown_options)
        random_option_text = random_option.text.strip()
        random_option.click()

        print(f"✅ Randomly selected admission type: {random_option_text}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        time.sleep(2)

        today_element = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
        (By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")
                )
        )          

        # Click using JavaScript in case normal click doesn't work
        login.execute_script("arguments[0].click();", today_element)

        print("Clicked today's date:", today_element.text)


        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]"))
        ).click()

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=3)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
        else:
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='p-checkbox-box'])[3]")
            )
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))
        ).click() 

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"))
        ).click()

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()                                                                                                                                       
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space(.)='Admit Now'])[1]")
            )
        ).click()

        
        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)


        time.sleep(5)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Medical Record')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='+ Add New Visit'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()   

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Visit'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)    
        
        time.sleep(5)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Services'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-plus'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Search Service'])[1]"))
        ).send_keys("Doc")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//li[@role='option'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[3]")
        time.sleep(1)
        # Locate the minute up arrow
        minute_up_button = login.find_element(By.XPATH, "//div[contains(@class,'p-minute-picker')]//button[1]")

        # Click it 10 times
        for _ in range(3):
            minute_up_button.click()
            time.sleep(0.5)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]", "2")
      
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Service'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Medical Records'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Vital Signs'])[1]"))
        ).click()

        # Generate vitals
        temp = generate_temperature_f()
        pulse = generate_pulse_rate()
        resp = generate_respiration_rate()
        systolic, diastolic = generate_blood_pressure()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Temperature in °F , Max : 200'])[1]"))
        ).send_keys(str(temp))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Pulse Rate , Max : 999'])[1]"))
        ).send_keys(str(pulse))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Respiration , Max : 90'])[1]"))
        ).send_keys(str(resp))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Systolic , Max : 500'])[1]"))
        ).send_keys(str(systolic))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Diastolic , Max : 500'])[1]"))
        ).send_keys(str(diastolic))

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save'])[1]"))
            
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'p-toast-message')]"))
        ).text
        print("Toast Message:", toast_message)


        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Prescription'])[1]"))
        ).click()

        time.sleep(2)
        for i in range(5):
            login.find_element(
                By.XPATH, "//button[normalize-space()='+ Add Medicine']"
            ).click()
            login.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(
                "Medicine"
            )

            # Scope to the prescription modal dialog
            
            before_XPath = "//mat-dialog-container[@role='dialog' and contains(@class, 'mat-mdc-dialog-container')]//table[contains(@class, 'p-datatable-table')]//tbody/tr"
            aftertd_XPath_1 = "/td[2]"
            aftertd_XPath_2 = "/td[3]"
            aftertd_XPath_3 = "/td[4]"
            aftertd_XPath_4 = "/td[5]"
            textarea_xpath = "//input[@role='searchbox']"
            row = i + 1
            if i > 0:
                trXPath = before_XPath + str([row])
            else:
                trXPath = before_XPath

            PreFinalXPath = trXPath + aftertd_XPath_1
            FinalXPath = PreFinalXPath + textarea_xpath

            Dose = login.find_element(By.XPATH, PreFinalXPath)
            Dose.click()
            Dose1 = login.find_element(By.XPATH, FinalXPath)
            Dose1.send_keys("650 mg")

            PreFinalXPath = trXPath + aftertd_XPath_2
            FinalXPath = PreFinalXPath + textarea_xpath

            Frequency = login.find_element(By.XPATH, PreFinalXPath)
            Frequency.click()
            Frequency1 = login.find_element(By.XPATH, FinalXPath)
            Frequency1.send_keys("1-1-1")

            PreFinalXPath = trXPath + aftertd_XPath_3
            FinalXPath = PreFinalXPath + textarea_xpath
            Duration = login.find_element(By.XPATH, PreFinalXPath)
            Duration.click()
            Duration1 = login.find_element(By.XPATH, FinalXPath)
            Duration1.send_keys("5 Days")

            PreFinalXPath = trXPath + aftertd_XPath_4
            FinalXPath = PreFinalXPath + textarea_xpath
            Notes = login.find_element(By.XPATH, PreFinalXPath)
            Notes.click()
            Notes1 = login.find_element(By.XPATH, FinalXPath)
            Notes1.send_keys("After Food")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save'])[1]"))
        ).click()

        
        
        time.sleep(2)
        share_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'Share')])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", share_button)
        time.sleep(2)
        share_button.click()
        
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@placeholder='Enter message description'])[1]"))
        ).send_keys("This is a test message.")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Email'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Whatsapp'])[1]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@type='button'][normalize-space()='Share'])[1]"))
        ).click()


        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Transfer Bed')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='First Floor B'])[1]"))
        ).click()


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal ICU'])[1]"))
        ).click()

        time.sleep(2)          

        # Find all bed cards
        bed_cards = login.find_elements(By.XPATH, "//div[contains(@class, 'bed-card')]")

        # Randomly choose one bed
        random_bed = random.choice(bed_cards)

        # Click the "Select Bed" button inside that bed-card
        select_button = random_bed.find_element(By.XPATH, ".//button[contains(text(), 'Select Bed')]")
        select_button.click()

        # (Optional) Print which bed was selected
        bed_name = random_bed.find_element(By.XPATH, ".//span[contains(@class, 'bed-title')]").text
        print(f"Selected Bed: {bed_name}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        today_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        today_date.click()
        print("Clicked today's date:", today_date.text)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save & Transfer'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)    

        # time.sleep(3)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]"))
        # ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Transfer Bed')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Select Bed'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        today_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        today_date.click()
        print("Clicked today's date:", today_date.text)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[normalize-space()='No'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save & Transfer'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)

        # time.sleep(3)
        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'View')])[1]"))
        # ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='my-1 font-small fw-bold text-capitalize ng-star-inserted'][normalize-space(.)='Discharge'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Use Template'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Use template'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        discharge_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space(.)='Discharge'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", discharge_button)

        time.sleep(2)
        discharge_button.click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        # Wait for the discharge status to appear
        discharge_status_xpath = "//div[contains(@class, 'status-discharged') and normalize-space()='Discharged']"
        WebDriverWait(login, 10).until(EC.visibility_of_element_located((By.XPATH, discharge_status_xpath)))

        # Assert that the "Discharged" status is displayed
        discharge_status_element = login.find_element(By.XPATH, discharge_status_xpath)
        assert discharge_status_element.is_displayed(), "Discharge status is not visible after discharge."

        print("✅ Discharge status is visible after discharge.")

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Invoices')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-plus'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space(.)='Generate'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space(.)='Generate Invoice'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Pay by Others'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Pay'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
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
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

    
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Checkout'])[1]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@type='button'][normalize-space()='Checkout'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)
 
        time.sleep(3)
        # XPath for "Checked Out" status
        checkout_xpath = "//div[contains(@class, 'status-checkout') and normalize-space()='Checked Out']"

        # Wait for the element to be visible
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, checkout_xpath))
        )

        # Assert the element is displayed
        checkout_status = login.find_element(By.XPATH, checkout_xpath)
        assert checkout_status.is_displayed(), "'Checked Out' status is not visible."

        print("✅ Checked Out status is visible after checkout.")

        

        
        
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Basic workflow of IP Mangement to Convert OP Patient to IP Patient")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)]) 
def  test_OP_Converted_to_IP_Patient(login):


    wait = WebDriverWait(login, 20)
    try: 
        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='dashboard-card-image'])[6]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(., 'Create Room')]"))  
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        drop_downlist = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal Room'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", drop_downlist)
        time.sleep(1)   
        drop_downlist.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Private Room'])[1]"))
        ).click()


        room_name = get_next_room_name()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Room Name'])[1]")
            )
        ).send_keys(room_name)

        print(f"🏨 Room created: {room_name}")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[5]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Room'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()
    
        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='Room Details'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()
        
        time.sleep(1)
        bed_type = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_type)
        time.sleep(1)
        bed_type.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Observation Beds'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        bed_price = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Manual Hospital Bed'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_price)
        time.sleep(1)
        bed_price.click()


        bed_name  = f'Bed{room_name}'
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Bed Name'])[1]"))
        ).send_keys(bed_name)   

        time.sleep(1)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()   

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Appointment'])[1]"))
        ).click()

        time.sleep(2)
        time.sleep(3)
        print("Create new patient")
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//b[normalize-space()='Create New Patient']")
            )
        )
        element_appoint.click()
        login.implicitly_wait(3)
        time.sleep(2)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='first_name'])[1]"))
        ).send_keys(first_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='last_name'])[1]"))
        ).send_keys(last_name)


        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='email_id'])[1]"))
        ).send_keys(email)

        time.sleep(1)   
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[1]"))
        ).send_keys(phonenumber)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[normalize-space()='Male'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)   
        # Click on the "2025" button
        login.find_element(By.XPATH, "//button[normalize-space()='2025']").click()

        # Wait until the backward arrow is clickable before clicking it
        backward_arrow = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'p-ripple') and contains(@class, 'p-element') and contains(@class, 'p-datepicker-prev') and contains(@class, 'p-link') and contains(@class, 'ng-star-inserted')]")
            )
        )

        # Clicking backward arrows 4 times to navigate to the correct year
        for _ in range(4):
            backward_arrow.click()
        time.sleep(2)
        # Generate Date of Birth (DOB)
        [year, month, day] = Generate_dob()
        print(f"Year: {year}, Month: {month}, Day: {day}")
        time.sleep(2)
        # Select Year
        year_xpath = f"//span[normalize-space()='{year}']"
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, year_xpath))
        ).click()
        time.sleep(2)
        # Select Month
        month_xpath = f"//span[normalize-space()='{month}']"
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, month_xpath))
        ).click()

        time.sleep(2)
        # Select Day
        day = str(int(day))  # Ensuring day is in integer form
        day_xpath = f"//span[normalize-space()='{day}']"
        select_day = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, day_xpath))
        )
        select_day.click()

        print(f"Selected Date of Birth: {day}-{month}-{year}")
        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Save'])[1]"))
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
       
        
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm']"))
        ).click()

        time.sleep(3)
        while True:
            try:
                
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                
                if next_button.is_enabled():
                   
                    login.execute_script("arguments[0].click();", next_button)
                else:
                  
                    break

            except Exception as e:
                
                break

        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(3)
        View_Detail_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(), 'View Details')]")
            )
        )
        View_Detail_button.click()


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Convert to IP'])[1]"))
        ).click()

        time.sleep(2)


        admission_dropdown = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        )
        admission_dropdown.click()

        # Wait and fetch all options in the dropdown
        dropdown_options = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@role='listbox' and contains(@class, 'p-dropdown-items')]/p-dropdownitem/li")
            )
        )

        # Randomly choose and click one option
        random_option = random.choice(dropdown_options)
        random_option_text = random_option.text.strip()
        random_option.click()

        print(f"✅ Randomly selected admission type: {random_option_text}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        time.sleep(2)

        today_element = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
        (By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")
                )
        )          

        # Click using JavaScript in case normal click doesn't work
        login.execute_script("arguments[0].click();", today_element)

        print("Clicked today's date:", today_element.text)


        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]"))
        ).click()

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=3)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
        else:
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")
            )
        ).click()                                                                                                                                            
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"))
        ).click()

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space(.)='Admit Now'])[1]")
            )
        ).click()

        
        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//button[normalize-space()='Assign Bed'])[1]"))
        # ).click()

        # toast_message = WebDriverWait(login, 10).until(
        # EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        # )
        # message = toast_message.text
        # print("Toast Message:", message)
        time.sleep(5)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Medical Record')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='+ Add New Visit'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()   

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Visit'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)    
        
        time.sleep(5)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Services'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-plus'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Search Service'])[1]"))
        ).send_keys("Doc")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//li[@role='option'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[3]")
        time.sleep(1)
        # Locate the minute up arrow
        minute_up_button = login.find_element(By.XPATH, "//div[contains(@class,'p-minute-picker')]//button[1]")

        # Click it 10 times
        for _ in range(3):
            minute_up_button.click()
            time.sleep(0.5)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]", "2")
      
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Service'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Medical Records'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Vital Signs'])[1]"))
        ).click()

        # Generate vitals
        temp = generate_temperature_f()
        pulse = generate_pulse_rate()
        resp = generate_respiration_rate()
        systolic, diastolic = generate_blood_pressure()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Temperature in °F , Max : 200'])[1]"))
        ).send_keys(str(temp))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Pulse Rate , Max : 999'])[1]"))
        ).send_keys(str(pulse))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Respiration , Max : 90'])[1]"))
        ).send_keys(str(resp))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Systolic , Max : 500'])[1]"))
        ).send_keys(str(systolic))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Diastolic , Max : 500'])[1]"))
        ).send_keys(str(diastolic))

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save'])[1]"))
            
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'p-toast-message')]"))
        ).text
        print("Toast Message:", toast_message)


        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Prescription'])[1]"))
        ).click()

        time.sleep(2)
        for i in range(5):
            login.find_element(
                By.XPATH, "//button[normalize-space()='+ Add Medicine']"
            ).click()
            login.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(
                "Medicine"
            )

            # Scope to the prescription modal dialog
            
            before_XPath = "//mat-dialog-container[@role='dialog' and contains(@class, 'mat-mdc-dialog-container')]//table[contains(@class, 'p-datatable-table')]//tbody/tr"
            aftertd_XPath_1 = "/td[2]"
            aftertd_XPath_2 = "/td[3]"
            aftertd_XPath_3 = "/td[4]"
            aftertd_XPath_4 = "/td[5]"
            textarea_xpath = "//input[@role='searchbox']"
            row = i + 1
            if i > 0:
                trXPath = before_XPath + str([row])
            else:
                trXPath = before_XPath

            PreFinalXPath = trXPath + aftertd_XPath_1
            FinalXPath = PreFinalXPath + textarea_xpath

            Dose = login.find_element(By.XPATH, PreFinalXPath)
            Dose.click()
            Dose1 = login.find_element(By.XPATH, FinalXPath)
            Dose1.send_keys("650 mg")

            PreFinalXPath = trXPath + aftertd_XPath_2
            FinalXPath = PreFinalXPath + textarea_xpath

            Frequency = login.find_element(By.XPATH, PreFinalXPath)
            Frequency.click()
            Frequency1 = login.find_element(By.XPATH, FinalXPath)
            Frequency1.send_keys("1-1-1")

            PreFinalXPath = trXPath + aftertd_XPath_3
            FinalXPath = PreFinalXPath + textarea_xpath
            Duration = login.find_element(By.XPATH, PreFinalXPath)
            Duration.click()
            Duration1 = login.find_element(By.XPATH, FinalXPath)
            Duration1.send_keys("5 Days")

            PreFinalXPath = trXPath + aftertd_XPath_4
            FinalXPath = PreFinalXPath + textarea_xpath
            Notes = login.find_element(By.XPATH, PreFinalXPath)
            Notes.click()
            Notes1 = login.find_element(By.XPATH, FinalXPath)
            Notes1.send_keys("After Food")

        time.sleep(5)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save'])[1]"))
        ).click()

        
        
        time.sleep(3)
        share_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'Share')])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", share_button)
        time.sleep(2)
        share_button.click()
        
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@placeholder='Enter message description'])[1]"))
        ).send_keys("This is a test message.")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Email'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Whatsapp'])[1]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@type='button'][normalize-space()='Share'])[1]"))
        ).click()

        time.sleep(3) 
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Transfer Bed')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='First Floor B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal ICU'])[1]"))
        ).click()

        time.sleep(2)          

        # Find all bed cards
        bed_cards = login.find_elements(By.XPATH, "//div[contains(@class, 'bed-card')]")

        # Randomly choose one bed
        random_bed = random.choice(bed_cards)

        # Click the "Select Bed" button inside that bed-card
        select_button = random_bed.find_element(By.XPATH, ".//button[contains(text(), 'Select Bed')]")
        select_button.click()

        # (Optional) Print which bed was selected
        bed_name = random_bed.find_element(By.XPATH, ".//span[contains(@class, 'bed-title')]").text
        print(f"Selected Bed: {bed_name}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        today_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        today_date.click()
        print("Clicked today's date:", today_date.text)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save & Transfer'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)    

        # time.sleep(3)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]"))
        # ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Transfer Bed')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Select Bed'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        today_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        today_date.click()
        print("Clicked today's date:", today_date.text)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[normalize-space()='No'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save & Transfer'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)

        # time.sleep(3)
        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'View')])[1]"))
        # ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='my-1 font-small fw-bold text-capitalize ng-star-inserted'][normalize-space(.)='Discharge'])[1]"))
        ).click()

        time.sleep(3) 
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Use Template'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Use template'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        discharge_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space(.)='Discharge'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", discharge_button)

        time.sleep(2)
        discharge_button.click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        # Wait for the discharge status to appear
        discharge_status_xpath = "//div[contains(@class, 'status-discharged') and normalize-space()='Discharged']"
        WebDriverWait(login, 10).until(EC.visibility_of_element_located((By.XPATH, discharge_status_xpath)))

        # Assert that the "Discharged" status is displayed
        discharge_status_element = login.find_element(By.XPATH, discharge_status_xpath)
        assert discharge_status_element.is_displayed(), "Discharge status is not visible after discharge."

        print("✅ Discharge status is visible after discharge.")

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Billing / Invoices')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-plus'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space(.)='Generate'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space(.)='Generate Invoice'])[1]"))
        ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Save Invoice'])[1]"))
        # ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Pay by Others'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Pay'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
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
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()
    
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Checkout'])[1]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@type='button'][normalize-space()='Checkout'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)
 
        time.sleep(3)
        # XPath for "Checked Out" status
        checkout_xpath = "//div[contains(@class, 'status-checkout') and normalize-space()='Checked Out']"

        # Wait for the element to be visible
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, checkout_xpath))
        )

        # Assert the element is displayed
        checkout_status = login.find_element(By.XPATH, checkout_xpath)
        assert checkout_status.is_displayed(), "'Checked Out' status is not visible."

        print("✅ Checked Out status is visible after checkout.")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Checked Out'])[1]"))
        ).click()



    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e