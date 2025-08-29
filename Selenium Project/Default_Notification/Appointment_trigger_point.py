import time

from Framework.common_utils import *
from Framework.consumer_common_utils import *
from Framework.common_dates_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Confirmation, Send_message, Send_Attachment, Prescription_Sharing, Case_Sharing, Auto and Manual Invoice, Reschedule, Cancellation")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_create_patient(login):
    try:

        time.sleep(5)
        print("New patient create")
        
        WebDriverWait(login, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]",
                )
            )
        ).click()
        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]",
                )
            )
        )
        element.click()
        
        
        time.sleep(3)

        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//b[normalize-space()='Create New Patient']")
            )
        )
        element_appoint.click()
        login.implicitly_wait(3)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(
            str(first_name)
        )
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(
            str(last_name)
        )
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(
            By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
        ).send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
        
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "p-dropdown[optionlabel='place']")
            )
        ).click()

        
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        login.implicitly_wait(5)

        login.find_element(
            By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']"
        ).click()
        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
        print("Department : ENT")
        user_dropdown_xpath = (
            "(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
            "ng-dirty'])[1]"
        )
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))
        ).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, user_option_xpath))
        ).click()
        print("Select user : Naveen")

        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        element= login.find_element(By.XPATH, service_dropdown_xpath)
        scroll_to_element(login, element)
        # login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        service_option_xpath = ("//li[@aria-label='Naveen Consultation']//div[1]")
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, service_option_xpath))
        ).click()
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
        login.implicitly_wait(10)
        Today_Date.click()
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']"))
        )
        time_slot.click()
        
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm']"))
        ).click()
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/app-sidebar-menu[1]/div[1]/div[2]/div[1]/ul[1]/li[2]/a[1]/div[1]/span[1]/span[1]/img[1]"))
        ).click()  
        
        time.sleep(2)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]",
                )
            )
        )
        element.click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
            )
        ).send_keys("9207206005")
        time.sleep(2)
        login.implicitly_wait(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Id : 2']")
            )
        ).click()
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "p-dropdown[optionlabel='place']")
            )
        ).click()

        
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        login.implicitly_wait(5)

        login.find_element(
            By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']"
        ).click()
        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
        print("Department : ENT")
        user_dropdown_xpath = (
            "(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
            "ng-dirty'])[1]"
        )
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))
        ).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, user_option_xpath))
        ).click()
        print("Select user : Naveen")

        time.sleep(3)
        element = login.find_element(By.XPATH, "//p-dropdown[@optionlabel='name']")
        scroll_to_element(login, element)
        time.sleep(2)
        element.click()

        time.sleep(3)
        service_option = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, ("//li[@aria-label='Naveen Consultation']//div[1]")))
        )
        click_to_element(login, service_option)
      
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
        login.implicitly_wait(10)
        Today_Date.click()
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Notes')]"))
        ).click()

        login.find_element(By.XPATH, "//textarea[@id='message']").send_keys(
            "Note for the walkin appointment"
        )

        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[normalize-space()='Save']")
            )
        ).click()
        print("Note added for walkin appointment")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Upload File']")
            )
        ).click()

        time.sleep(4)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        time.sleep(2)
        pyautogui.write(absolute_path)
        time.sleep(2)
        pyautogui.press("enter")
        print("Successfully upload the file")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Confirm')]")
            )
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

        # print("Appointment confirm successfully")

        time.sleep(3)

        while True:
            try:
                # Attempt to locate the "Next" button using the button's class
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                # Check if the button is enabled (i.e., not disabled)
                if next_button.is_enabled():
                    # print("Next button found and clickable.")
                    # Click using JavaScript to avoid interception issues
                    login.execute_script("arguments[0].click();", next_button)
                else:
                    # print("Next button is disabled. Reached the last page.")
                    break

            except Exception as e:
                # # If no next button is found or any other exception occurs, exit the loop
                # print("End of pages or error encountered:", e)
                break

        # After clicking through all pages, locate and click the last accordion
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
        click_to_element(login, View_Detail_button)

        time.sleep(3)
        more_actions_button = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[normalize-space()='More Actions']")
            )
        )
        click_to_element(login, more_actions_button)
       
          
        # ****************************** Send Message **********************************************
    
        time.sleep(3)
        message_button = WebDriverWait(login, 15).until(
        EC.presence_of_element_located(
        (By.XPATH, "//button[normalize-space()='Send Message']"))
        )
        click_to_element(login, message_button)

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//textarea[@id='messageData']", "Send Message to the Patient")

        time.sleep(3)
        wait_and_click(login, By.XPATH, "//label[normalize-space()='Click here to select the files']")
        
        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(4)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'send')]")

        get_snack_bar_message(login)
        print("Snack bar message:", get_snack_bar_message(login))

        # ******************* Send Attachment ************************
        time.sleep(5)
        wait_and_visible_click(login, By.XPATH, "//button[normalize-space()='Send Attachments']")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "//label[normalize-space()='Click here to select the files']")

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()
        time.sleep(2)
        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        time.sleep(1)
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'send')]")

        get_snack_bar_message(login)
        print("Snack bar message:", get_snack_bar_message(login))
        
        # ********************* Create the Prescription and Sharing ******************************

        time.sleep(5)
        WebDriverWait(login, 10)

        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Prescriptions']")

        for i in range(5):
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='+ Add Medicine']")
            wait_and_send_keys( login, By.XPATH, "//input[@role='searchbox']", "Medicine")

            before_XPath = "//*[contains(@id, 'pr_id')]/tbody/tr"
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

        wait_and_locate_click(login, By.XPATH, "//mat-select[@aria-haspopup='listbox']")
        
        time.sleep(3)
        element3 = login.find_element(By.XPATH, "//span[@class='mdc-list-item__primary-text']//div[contains(text(),'Naveen KP')]")
        click_to_element(login, element3)
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
        
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        # print("prescription created successfully")
        time.sleep(2)

        login.find_element(By.XPATH, "//img[@alt='share']").click()

        time.sleep(2)
        login.find_element(
            By.XPATH, "//textarea[@placeholder='Enter message description']"
        ).send_keys("prescription message")

        login.find_element(
            By.XPATH, "(//input[@class='mdc-checkbox__native-control'])[1]"
        ).click()
        login.find_element(By.XPATH, "//span[normalize-space()='Whatsapp']").click()
        login.find_element(By.XPATH, "//button[@type='button'][normalize-space()='Share']").click()

        print("Prescription Shared Successfully")

        # ************************* Case Creation and Sharing *********************

        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Patient Record']")
        
        login.implicitly_wait(5)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='+ Create Case']")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Case Description']", "test case for case")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']")
            )
        ).click()

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder = 'Enter Chief Complaint']")
            )
        ).send_keys("Fever")

        element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']"))
        )
        login.execute_script("arguments[0].click();", element)
        
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='History']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder ='Enter History']"))
        ).send_keys("viral fever",Keys.RETURN)
        
        element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']"))
        )
        login.execute_script("arguments[0].click();", element)

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Medication']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Medication']"))
        ).send_keys("no medication",Keys.RETURN)
        
        time.sleep(1)
        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].click();", element)
        

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Vital Signs']")
            )
        ).click()

        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Pulse Rate , Max : 999']"
        ).send_keys("560")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Respiration , Max : 90']"
        ).send_keys("62")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Temperature in °F , Max : 200']"
        ).send_keys("123")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Systolic , Max : 500']"
        ).send_keys("264")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Diastolic , Max : 500']"
        ).send_keys("287")

        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        # login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Treatment Plan']"))
        ).click()
        
    
        treat_name = "Treatment" + str(uuid.uuid4())[:4]
        treat_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@role='searchbox']"))
        )
        treat_namebox.clear()
        treat_namebox.send_keys(treat_name)
        
        
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='p-multiselect-label p-placeholder']"))
        ).click()
        
        
        dropdown_xpath = "//span[normalize-space()='Naveen KP']"
        element = login.find_element(By.XPATH, dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        
        time.sleep(3)
        
        
        WebDriverWait(login, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@class='btn btn-white shadow fw-bold']"))
        ).click()
        
        step_name = "Step" + str(uuid.uuid1())[:1]
        step_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Name']"))
        )
        step_namebox.clear()
        step_namebox.send_keys(step_name)
        
        
        WebDriverWait(login, 10).until(
           EC.presence_of_element_located(
               (By.XPATH, "//p-multiselect[@optionlabel='firstName']//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted']"))
       ).click()
        
        time.sleep(2)
        element1 = login.find_element(By.XPATH, dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element1)
        element1.click()
        
        time.sleep(3)
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='d-flex']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']")
            )
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='In Progress']"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Step Notes']"))
        ).send_keys("Steps for notes")
        
        WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//label[@for='treatmentPlanAattachments']")
        )
        ).click()

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Treatment Notes']"))
        ).send_keys("Note for the treatment")
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']"))
        ).click()
        
        element2 = login.find_element(By.XPATH, "//span[normalize-space()='Add the sections you need for this medical record']")
        login.execute_script("arguments[0].scrollIntoView();", element2)
        element2.click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Prescription']")
            )
        ).click()

        for i in range(5):
            login.find_element(
                By.XPATH, "//button[normalize-space()='+ Add Medicine']"
            ).click()
            login.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(
                "Medicine"
            )

            before_XPath = "//*[contains(@id, 'pr_id')]/tbody/tr"
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

        
       
        dropdown_element= WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//mat-select[@aria-haspopup='listbox']"))
        )
        dropdown_element.click()
        
        time.sleep(3)
        element3 = login.find_element(By.XPATH, "//span[@class='mdc-list-item__primary-text']//div[contains(text(),'Naveen KP')]")
        login.execute_script("arguments[0].click();", element3)
        
        
    
        time.sleep(2)
        login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        time.sleep(2)
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[@class='add-action-btn']"))
        ).click()
        
        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Share')]")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter message description']")
            )
        ).send_keys("case sharing testing")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Email')]"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Whatsapp')]"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(),'Share')]")
            )
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        # print("Case file Shared successfully")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//i[@class='pi pi-arrow-left back-btn-arrow']")
            )
        ).click()

        WebDriverWait(login, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
            )
        ).click()

        while True:
            try:
                # Attempt to locate the "Next" button using the button's class
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                # Check if the button is enabled (i.e., not disabled)
                if next_button.is_enabled():
                    # print("Next button found and clickable.")
                    # Click using JavaScript to avoid interception issues
                    login.execute_script("arguments[0].click();", next_button)
                else:
                    # print("Next button is disabled. Reached the last page.")
                    break

            except Exception as e:
                # # If no next button is found or any other exception occurs, exit the loop
                # print("End of pages or error encountered:", e)
                break

        # After clicking through all pages, locate and click the last accordion
        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        # ************************* Auto Invoice and Sharing ************************

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='View Invoice']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Send']")
            )
        ).click()
        print("Auto Invoice")
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
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Edit']"))
        ).click()
        
        time.sleep(2)
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        ).click()
        
        time.sleep(2)    
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='Naveen Consultation 1']"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        print("Added Sub Service to the Invoice")
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        ).click()
        
        item_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Choose Procedure/Item']"))
        )
        item_button.click()
        item_button.send_keys("item1234")
          
        time.sleep(3)
        price = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='mat-input-4'])[2]"))
        )
        price.clear()
        price.click()
        price.send_keys("1")
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        print("Added ADHOC item to the Invoice")
        
        time.sleep(3)
        update_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", update_button)
        update_button.click()
        
          
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
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Send']")
            )
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

        time.sleep(4)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Pay by Cash']"))
        ).click()

        pay_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Pay']"))
        )
        login.execute_script("arguments[0].click();", pay_button)

        time.sleep(3)
        yes_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space(.)='Yes']"))
        )
        login.execute_script("arguments[0].click();", yes_button)
                     
        time.sleep(3)

        login.find_element(By.XPATH, "//i[@class='fa fa-arrow-left']").click()

        while True:
            try:
                # Attempt to locate the "Next" button using the button's class
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                # Check if the button is enabled (i.e., not disabled)
                if next_button.is_enabled():
                    # print("Next button found and clickable.")
                    # Click using JavaScript to avoid interception issues
                    login.execute_script("arguments[0].click();", next_button)
                else:
                    # print("Next button is disabled. Reached the last page.")
                    break

            except Exception as e:
                # # If no next button is found or any other exception occurs, exit the loop
                # print("End of pages or error encountered:", e)
                break

        # After clicking through all pages, locate and click the last accordion
        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        # ********************** Manual Invoice and Sharing ***********************

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='New Invoice']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']")
            )
        ).click()

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Choose Procedure/Item']")
            )
        ).click()

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@class='item-name'][normalize-space()='Naveen Consultation']",
                )
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//button[@class='cs-btn bt1 ml-0'][normalize-space()='Add']",
                )
            )
        ).click()

        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Update']")
            )
        ).click()

        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Send']")
            )
        ).click()
        print("Manual Invoice")

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
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Edit']"))
        ).click()
        
        time.sleep(2)
        
        add_service = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        )
        login.execute_script("arguments[0].click();", add_service)
        
        time.sleep(3)    
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='Naveen Consultation 1']"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        print("Added Sub Service to the Invoice")
        
        time.sleep(2)
        login.execute_script("arguments[0].click();", add_service)
        item_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Choose Procedure/Item']"))
        )
        item_button.click()
        item_button.send_keys("item1234")
        
        time.sleep(3)
        price = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='mat-input-4'])[2]"))
        )
        price.clear()
        price.click()
        price.send_keys("102")
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        print("Added ADHOC item to the Invoice")
        
        time.sleep(3)
        update_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", update_button)
        update_button.click()
        
        
        
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
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Send']")
            )
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
    #     # print("Successfully send the Payment Link to the patient")

        login.find_element(By.XPATH, "//i[@class='fa fa-arrow-left']").click()

        while True:
            try:
                # Attempt to locate the "Next" button using the button's class
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                # Check if the button is enabled (i.e., not disabled)
                if next_button.is_enabled():
                    # print("Next button found and clickable.")
                    # Click using JavaScript to avoid interception issues
                    login.execute_script("arguments[0].click();", next_button)
                else:
                    # print("Next button is disabled. Reached the last page.")
                    break

            except Exception as e:
                # # If no next button is found or any other exception occurs, exit the loop
                # print("End of pages or error encountered:", e)
                break

        # After clicking through all pages, locate and click the last accordion
        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(3)
        # print("Before clicking View Details button")
        View_Detail_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(), 'View Details')]")
            )
        )
        View_Detail_button.click()

        # *************************** Reschedule **********************

        time.sleep(3)
        login.find_element(By.XPATH, "//button[contains(text(),'Reschedule')]").click()
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='reschedule-date-picker']")
            )
        ).click()

        today_date = datetime.now()
        print(today_date.day)
        today_xpath_expression = "//span[@class='example-custom-date-class d-pad-15 ng-star-inserted'][normalize-space()='{}']".format(
            today_date.day
        )
        print(today_xpath_expression)
        tomorrow_date = today_date + timedelta(days=1)
        print(tomorrow_date.day)

        # current_month = WebDriverWait(login, 10).until(
        # EC.presence_of_element_located(
        #     (By.XPATH, "//button[contains(@class, 'p-datepicker-month')]"))
        # )

        # current_year = WebDriverWait(login, 10).until(
        # EC.presence_of_element_located(
        #     (By.XPATH, "//button[contains(@class, 'p-datepicker-year')]"))
        # )

        # if current_month.text.lower() != tomorrow_date.strftime("%b").lower() or current_year.text.lower() != tomorrow_date.strftime("%Y").lower():

        #     login.find_element(By.XPATH, "//button[contains(@class, 'p-datepicker-next')]").click()

        tomorrow_xpath_expression = "//span[@class='example-custom-date-class d-pad-15 ng-star-inserted'][normalize-space()='{}']".format(
            tomorrow_date.day
        )
        print(tomorrow_xpath_expression)

        Tomorrow_Date = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, tomorrow_xpath_expression))
        )
        Tomorrow_Date.click()
        print("Tomorrow Date:", Tomorrow_Date.text)

        wait = WebDriverWait(login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected= 'false']"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)

        reschedule_button = WebDriverWait(login, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='btn btn-primary reschedule-btn']")
            )
        )
        reschedule_button.click()

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
        # print("Reschedule Successfully")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Today')]")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Future']")
            )
        ).click()

        time.sleep(3)
        last_accordian = WebDriverWait(login, 15).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
                )
            )
        )
        last_accordian.click()

        # *******************Cancellation **********************

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Change Status']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Cancel')]")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'No Show Up')]")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Ok']"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message) 

        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    


# ######################################################################################################

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Confirmation, Send_message, Send_Attachment, Prescription_Sharing, Case_Sharing, Auto and Manual Invoice, Reschedule, Cancellation")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale_1, password)])
def test_notification_single_location(login):
    try:

        time.sleep(5)
        
        WebDriverWait(login, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]",
                )
            )
        ).click()
        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]",
                )
            )
        )
        element.click()

        time.sleep(2)
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
            )
        ).send_keys("9207206005")

        login.implicitly_wait(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Id : 2'])[1]"))
        ).click()
        
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "p-dropdown[optionlabel='place']")
            )
        ).click()

        
        login.find_element(By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Poothole'])[1]").click()
        print("location : Poothole")
        login.implicitly_wait(5)

        login.find_element(By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]").click()
        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//span[normalize-space()='General Services'])[1]").click()
        print("Department : General Services")
        user_dropdown_xpath = "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))
        ).click()
        user_option_xpath = "(//span[normalize-space()='Varun CP'])[1]"
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, user_option_xpath))
        ).click()
        print("Select user : Dr.Varun CP")

        # service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        # element= login.find_element(By.XPATH, service_dropdown_xpath)
        # scroll_to_element(login, element)
        # # login.execute_script("arguments[0].scrollIntoView();", element)
        # element.click()

        # service_option_xpath = ("//li[@aria-label='Naveen Consultation']//div[1]")
        # time.sleep(2)
        # WebDriverWait(login, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, service_option_xpath))
        # ).click()
        print("Select Service :Consultation")
        time.sleep(5)
        Today_Date = WebDriverWait(login, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(@class,'mat-calendar-body-today')]")
            )
        )
        Today_Date.click()
        print("Today Date:", Today_Date.text)

        wait = WebDriverWait(login, 30)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']"))
        )
        time_slot.click()
        
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Confirm')]")
            )
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

        # print("Appointment confirm successfully")

        time.sleep(3)

        while True:
            try:
                # Attempt to locate the "Next" button using the button's class
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                # Check if the button is enabled (i.e., not disabled)
                if next_button.is_enabled():
                    # print("Next button found and clickable.")
                    # Click using JavaScript to avoid interception issues
                    login.execute_script("arguments[0].click();", next_button)
                else:
                    # print("Next button is disabled. Reached the last page.")
                    break

            except Exception as e:
                # # If no next button is found or any other exception occurs, exit the loop
                # print("End of pages or error encountered:", e)
                break

        # After clicking through all pages, locate and click the last accordion
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
        click_to_element(login, View_Detail_button)

        time.sleep(3)
        more_actions_button = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[normalize-space()='More Actions']")
            )
        )
        click_to_element(login, more_actions_button)
       
          
        # ****************************** Send Message **********************************************
    
        time.sleep(3)
        message_button = WebDriverWait(login, 15).until(
        EC.presence_of_element_located(
        (By.XPATH, "//button[normalize-space()='Send Message']"))
        )
        click_to_element(login, message_button)

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//textarea[@id='messageData']", "Send Message to the Patient")

        time.sleep(3)
        wait_and_click(login, By.XPATH, "//label[normalize-space()='Click here to select the files']")
        
        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(4)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'send')]")

        get_snack_bar_message(login)
        print("Snack bar message:", get_snack_bar_message(login))

        # ******************* Send Attachment ************************
        time.sleep(5)
        wait_and_visible_click(login, By.XPATH, "//button[normalize-space()='Send Attachments']")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "//label[normalize-space()='Click here to select the files']")

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()
        time.sleep(2)
        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        time.sleep(1)
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'send')]")

        get_snack_bar_message(login)
        print("Snack bar message:", get_snack_bar_message(login))
        
        # ********************* Create the Prescription and Sharing ******************************

        time.sleep(5)
        WebDriverWait(login, 10)

        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Prescriptions']")

        for i in range(5):
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='+ Add Medicine']")
            wait_and_send_keys( login, By.XPATH, "//input[@role='searchbox']", "Medicine")

            before_XPath = "//*[contains(@id, 'pr_id')]/tbody/tr"
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

        # wait_and_locate_click(login, By.XPATH, "//mat-select[@aria-haspopup='listbox']")
        
        # time.sleep(3)
        # element3 = login.find_element(By.XPATH, "//span[@class='mdc-list-item__primary-text']//div[contains(text(),'Naveen KP')]")
        # click_to_element(login, element3)
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
        
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        # print("prescription created successfully")
        time.sleep(2)

        login.find_element(By.XPATH, "//img[@alt='share']").click()

        time.sleep(2)
        login.find_element(
            By.XPATH, "//textarea[@placeholder='Enter message description']"
        ).send_keys("prescription message")

        login.find_element(
            By.XPATH, "(//input[@class='mdc-checkbox__native-control'])[1]"
        ).click()
        login.find_element(By.XPATH, "//span[normalize-space()='Whatsapp']").click()
        login.find_element(By.XPATH, "//button[@type='button'][normalize-space()='Share']").click()

        print("Prescription Shared Successfully")

        # ************************* Case Creation and Sharing *********************

        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Patient Record']")
        
        login.implicitly_wait(5)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='+ Create Case']")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Case Description']", "test case for case")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']")
            )
        ).click()

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder = 'Enter Chief Complaint']")
            )
        ).send_keys("Fever")

        element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']"))
        )
        login.execute_script("arguments[0].click();", element)
        
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='History']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder ='Enter History']"))
        ).send_keys("viral fever",Keys.RETURN)
        
        element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']"))
        )
        login.execute_script("arguments[0].click();", element)

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Medication']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Medication']"))
        ).send_keys("no medication",Keys.RETURN)
        
        time.sleep(1)
        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].click();", element)
        

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Vital Signs']")
            )
        ).click()

        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Pulse Rate , Max : 999']"
        ).send_keys("560")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Respiration , Max : 90']"
        ).send_keys("62")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Temperature in °F , Max : 200']"
        ).send_keys("123")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Systolic , Max : 500']"
        ).send_keys("264")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Diastolic , Max : 500']"
        ).send_keys("287")

        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        # login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Treatment Plan']"))
        ).click()
        
    
        treat_name = "Treatment" + str(uuid.uuid4())[:4]
        treat_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@role='searchbox']"))
        )
        treat_namebox.clear()
        treat_namebox.send_keys(treat_name)
        
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()
        
        
        dropdown_xpath = "(//span[normalize-space()='Varun CP'])[1]"
        element = login.find_element(By.XPATH, dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        
        time.sleep(3)
        
        
        WebDriverWait(login, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@class='btn btn-white shadow fw-bold']"))
        ).click()
        
        step_name = "Step" + str(uuid.uuid1())[:1]
        step_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Name']"))
        )
        step_namebox.clear()
        step_namebox.send_keys(step_name)
        
        
        WebDriverWait(login, 10).until(
           EC.presence_of_element_located(
               (By.XPATH, "//p-multiselect[@optionlabel='firstName']//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted']"))
       ).click()
        
        time.sleep(2)
        element1 = login.find_element(By.XPATH, dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element1)
        element1.click()
        
        time.sleep(3)
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='d-flex']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']")
            )
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='In Progress']"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Step Notes']"))
        ).send_keys("Steps for notes")
        
        WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//label[@for='treatmentPlanAattachments']")
        )
        ).click()

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Treatment Notes']"))
        ).send_keys("Note for the treatment")
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']"))
        ).click()
        
        element2 = login.find_element(By.XPATH, "//span[normalize-space()='Add the sections you need for this medical record']")
        login.execute_script("arguments[0].scrollIntoView();", element2)
        element2.click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Prescription']")
            )
        ).click()

        for i in range(5):
            login.find_element(
                By.XPATH, "//button[normalize-space()='+ Add Medicine']"
            ).click()
            login.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(
                "Medicine"
            )

            before_XPath = "//*[contains(@id, 'pr_id')]/tbody/tr"
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
        login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        time.sleep(2)
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[@class='add-action-btn']"))
        ).click()
        
        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Share')]")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter message description']")
            )
        ).send_keys("case sharing testing")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Email')]"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Whatsapp')]"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(),'Share')]")
            )
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        # print("Case file Shared successfully")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//i[@class='pi pi-arrow-left back-btn-arrow']")
            )
        ).click()

        WebDriverWait(login, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
            )
        ).click()

        while True:
            try:
                # Attempt to locate the "Next" button using the button's class
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                # Check if the button is enabled (i.e., not disabled)
                if next_button.is_enabled():
                    # print("Next button found and clickable.")
                    # Click using JavaScript to avoid interception issues
                    login.execute_script("arguments[0].click();", next_button)
                else:
                    # print("Next button is disabled. Reached the last page.")
                    break

            except Exception as e:
                # # If no next button is found or any other exception occurs, exit the loop
                # print("End of pages or error encountered:", e)
                break

        # After clicking through all pages, locate and click the last accordion
        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        # ************************* Auto Invoice and Sharing ************************

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='View Invoice']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Send']")
            )
        ).click()
        print("Auto Invoice")
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
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Edit']"))
        ).click()
        
        time.sleep(2)
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        ).click()
        
        time.sleep(2)    
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='Naveen Consultation 1']"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        print("Added Sub Service to the Invoice")
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        ).click()
        
        item_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Choose Procedure/Item']"))
        )
        item_button.click()
        item_button.send_keys("item1234")
          
        time.sleep(3)
        price = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='mat-input-4'])[2]"))
        )
        price.clear()
        price.click()
        price.send_keys("1")
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        print("Added ADHOC item to the Invoice")
        
        time.sleep(3)
        update_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", update_button)
        update_button.click()
        
          
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
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Send']")
            )
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

        time.sleep(4)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Pay by Cash']"))
        ).click()

        pay_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Pay']"))
        )
        login.execute_script("arguments[0].click();", pay_button)

        time.sleep(3)
        yes_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space(.)='Yes']"))
        )
        login.execute_script("arguments[0].click();", yes_button)
                     
        time.sleep(3)

        login.find_element(By.XPATH, "//i[@class='fa fa-arrow-left']").click()

        while True:
            try:
                # Attempt to locate the "Next" button using the button's class
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                # Check if the button is enabled (i.e., not disabled)
                if next_button.is_enabled():
                    # print("Next button found and clickable.")
                    # Click using JavaScript to avoid interception issues
                    login.execute_script("arguments[0].click();", next_button)
                else:
                    # print("Next button is disabled. Reached the last page.")
                    break

            except Exception as e:
                # # If no next button is found or any other exception occurs, exit the loop
                # print("End of pages or error encountered:", e)
                break

        # After clicking through all pages, locate and click the last accordion
        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        # ********************** Manual Invoice and Sharing ***********************

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='New Invoice']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']")
            )
        ).click()

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Choose Procedure/Item']")
            )
        ).click()

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@class='item-name'][normalize-space()='Naveen Consultation']",
                )
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//button[@class='cs-btn bt1 ml-0'][normalize-space()='Add']",
                )
            )
        ).click()

        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Update']")
            )
        ).click()

        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Send']")
            )
        ).click()
        print("Manual Invoice")

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
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Edit']"))
        ).click()
        
        time.sleep(2)
        
        add_service = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        )
        login.execute_script("arguments[0].click();", add_service)
        
        time.sleep(3)    
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='Naveen Consultation 1']"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        print("Added Sub Service to the Invoice")
        
        time.sleep(2)
        login.execute_script("arguments[0].click();", add_service)
        item_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Choose Procedure/Item']"))
        )
        item_button.click()
        item_button.send_keys("item1234")
        
        time.sleep(3)
        price = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='mat-input-4'])[2]"))
        )
        price.clear()
        price.click()
        price.send_keys("102")
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        print("Added ADHOC item to the Invoice")
        
        time.sleep(3)
        update_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", update_button)
        update_button.click()
        
        
        
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
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Send']")
            )
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
    #     # print("Successfully send the Payment Link to the patient")

        login.find_element(By.XPATH, "//i[@class='fa fa-arrow-left']").click()

        while True:
            try:
                # Attempt to locate the "Next" button using the button's class
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                # Check if the button is enabled (i.e., not disabled)
                if next_button.is_enabled():
                    # print("Next button found and clickable.")
                    # Click using JavaScript to avoid interception issues
                    login.execute_script("arguments[0].click();", next_button)
                else:
                    # print("Next button is disabled. Reached the last page.")
                    break

            except Exception as e:
                # # If no next button is found or any other exception occurs, exit the loop
                # print("End of pages or error encountered:", e)
                break

        # After clicking through all pages, locate and click the last accordion
        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(3)
        # print("Before clicking View Details button")
        View_Detail_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(), 'View Details')]")
            )
        )
        View_Detail_button.click()

        # *************************** Reschedule **********************

        time.sleep(3)
        login.find_element(By.XPATH, "//button[contains(text(),'Reschedule')]").click()
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='reschedule-date-picker']")
            )
        ).click()

        today_date = datetime.now()
        print(today_date.day)
        today_xpath_expression = "//span[@class='example-custom-date-class d-pad-15 ng-star-inserted'][normalize-space()='{}']".format(
            today_date.day
        )
        print(today_xpath_expression)
        tomorrow_date = today_date + timedelta(days=1)
        print(tomorrow_date.day)

        # current_month = WebDriverWait(login, 10).until(
        # EC.presence_of_element_located(
        #     (By.XPATH, "//button[contains(@class, 'p-datepicker-month')]"))
        # )

        # current_year = WebDriverWait(login, 10).until(
        # EC.presence_of_element_located(
        #     (By.XPATH, "//button[contains(@class, 'p-datepicker-year')]"))
        # )

        # if current_month.text.lower() != tomorrow_date.strftime("%b").lower() or current_year.text.lower() != tomorrow_date.strftime("%Y").lower():

        #     login.find_element(By.XPATH, "//button[contains(@class, 'p-datepicker-next')]").click()

        tomorrow_xpath_expression = "//span[@class='example-custom-date-class d-pad-15 ng-star-inserted'][normalize-space()='{}']".format(
            tomorrow_date.day
        )
        print(tomorrow_xpath_expression)

        Tomorrow_Date = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, tomorrow_xpath_expression))
        )
        Tomorrow_Date.click()
        print("Tomorrow Date:", Tomorrow_Date.text)

        wait = WebDriverWait(login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected= 'false']"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)

        reschedule_button = WebDriverWait(login, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='btn btn-primary reschedule-btn']")
            )
        )
        reschedule_button.click()

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
        # print("Reschedule Successfully")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Today')]")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Future']")
            )
        ).click()

        time.sleep(3)
        last_accordian = WebDriverWait(login, 15).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
                )
            )
        )
        last_accordian.click()

        # *******************Cancellation **********************

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Change Status']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Cancel')]")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'No Show Up')]")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Ok']"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message) 

        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

######################################################################################################################################################################################
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Reconfirmation")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])  
def test_patient_Reconfirmation(login):
    try:
        time.sleep(5)
        WebDriverWait(login, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]",
                )
            )
        ).click()
        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]",
                )
            )
        )
        element.click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
            )
        ).send_keys("920720600")

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Id : 2')]"))
        ).click()

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "p-dropdown[optionlabel='place']")
            )
        ).click()

        
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        login.implicitly_wait(5)

        login.find_element(
            By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']"
        ).click()
        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
        print("Department : ENT")
        user_dropdown_xpath = (
            "(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
            "ng-dirty'])[1]"
        )
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))
        ).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, user_option_xpath))
        ).click()
        print("Select user : Naveen")

        time.sleep(2)
        element = login.find_element(By.XPATH, "//p-dropdown[@optionlabel='name']")
        scroll_to_element(login, element)
        element.click()

        time.sleep(3)
        service_option = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, ("//li[@aria-label='Naveen Consultation']//div[1]")))
        )
        click_to_element(login, service_option)
        print("Select Service : Naveen Consultation")

        time.sleep(3)
        Today_Date = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']",
                )
            )
        )
        Today_Date.click()
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Notes')]"))
        ).click()

        login.find_element(By.XPATH, "//textarea[@id='message']").send_keys(
            "Note for the walkin appointment"
        )

        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
        ).click()

        print("Note added for walkin appointment")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Upload File']")
            )
        ).click()

        time.sleep(8)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(4)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
        ).click()

        print("Appointment confirm successfully")

        time.sleep(5)

        while True:
                try:
                    # Attempt to locate the "Next" button using the button's class
                    next_button = WebDriverWait(login, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                        )
                    )

                    # Check if the button is enabled (i.e., not disabled)
                    if next_button.is_enabled():
                        # print("Next button found and clickable.")
                        # Click using JavaScript to avoid interception issues
                        login.execute_script("arguments[0].click();", next_button)
                    else:
                        # print("Next button is disabled. Reached the last page.")
                        break

                except Exception as e:
                    # # If no next button is found or any other exception occurs, exit the loop
                    # print("End of pages or error encountered:", e)
                    break

            # After clicking through all pages, locate and click the last accordion
        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Change Status']")
            )
        ).click()

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Cancel')]"))
        ).click()

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'No Show Up')]")
            )
        ).click()

        login.find_element(By.XPATH, "//span[@class='mdc-button__label']").click()

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@type='checkbox'])[4]"))
        ).click()

        while True:
                try:
                    # Attempt to locate the "Next" button using the button's class
                    next_button = WebDriverWait(login, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                        )
                    )

                    # Check if the button is enabled (i.e., not disabled)
                    if next_button.is_enabled():
                        # print("Next button found and clickable.")
                        # Click using JavaScript to avoid interception issues
                        login.execute_script("arguments[0].click();", next_button)
                    else:
                        # print("Next button is disabled. Reached the last page.")
                        break

                except Exception as e:
                    # # If no next button is found or any other exception occurs, exit the loop
                    # print("End of pages or error encountered:", e)
                    break

            # After clicking through all pages, locate and click the last accordion
        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Change Status']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='status status-box']"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

####################################################################################################################################################################
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Start")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)]) 
def test_patient_start(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]",
            )
        )
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]",
            )
        )
    )
    element.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
        )
    ).send_keys("920720600")

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Id : 2')]"))
    ).click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "p-dropdown[optionlabel='place']")
            )
        ).click()

        
    login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
    print("location : Chavakkad")
    login.implicitly_wait(5)

    login.find_element(
        By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']"
    ).click()
    login.implicitly_wait(5)
    login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
    print("Department : ENT")
    user_dropdown_xpath = (
        "(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
        "ng-dirty'])[1]"
    )
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))
    ).click()
    user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, user_option_xpath))
    ).click()
    print("Select user : Naveen")

    time.sleep(2)
    element = login.find_element(By.XPATH, "//p-dropdown[@optionlabel='name']")
    scroll_to_element(login, element)
    element.click()

    time.sleep(3)
    service_option = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, ("//li[@aria-label='Naveen Consultation']//div[1]")))
    )
    click_to_element(login, service_option)
    print("Select Service : Naveen Consultation")

    time.sleep(3)
    Today_Date = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']",
            )
        )
    )
    Today_Date.click()
    print("Today Date:", Today_Date.text)
    wait = WebDriverWait(login, 10)
    time_slot = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']"))
    )
    time_slot.click()
    print("Time Slot:", time_slot.text)

    time.sleep(4)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
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
    while True:
            try:
                # Attempt to locate the "Next" button using the button's class
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                # Check if the button is enabled (i.e., not disabled)
                if next_button.is_enabled():
                    # print("Next button found and clickable.")
                    # Click using JavaScript to avoid interception issues
                    login.execute_script("arguments[0].click();", next_button)
                else:
                    # print("Next button is disabled. Reached the last page.")
                    break

            except Exception as e:
                # # If no next button is found or any other exception occurs, exit the loop
                # print("End of pages or error encountered:", e)
                break

        # After clicking through all pages, locate and click the last accordion
    time.sleep(1)
    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Change Status']")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Start')]"))
    ).click()

    toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_message.text
    print("Toast Message:", message)

###############################################################################################################################################################
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Reminder Message")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])  
def test_reminder_message(login):

    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]",
            )
        )
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]",
            )
        )
    )
    element.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
        )
    ).send_keys("920720600")

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Id : 2')]"))
    ).click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "p-dropdown[optionlabel='place']")
            )
        ).click()

        
    login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
    print("location : Chavakkad")
    login.implicitly_wait(5)

    login.find_element(
        By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']"
    ).click()
    login.implicitly_wait(5)
    login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
    print("Department : ENT")
    user_dropdown_xpath = (
        "(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
        "ng-dirty'])[1]"
    )
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))
    ).click()
    user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, user_option_xpath))
    ).click()
    print("Select user : Naveen")

    time.sleep(2)
    element = login.find_element(By.XPATH, "//p-dropdown[@optionlabel='name']")
    scroll_to_element(login, element)
    element.click()

    time.sleep(3)
    service_option = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, ("//li[@aria-label='Naveen Consultation']//div[1]")))
    )
    click_to_element(login, service_option)
    print("Select Service : Naveen Consultation")

    time.sleep(3)
    Today_Date = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']",
            )
        )
    )
    Today_Date.click()
    print("Today Date:", Today_Date.text)
    wait = WebDriverWait(login, 10)
    time_slot = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']"))
    )
    time_slot.click()
    print("Time Slot:", time_slot.text)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Notes')]"))
    ).click()

    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys(
        "Note for the walkin appointment"
    )

    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()

    print("Note added for walkin appointment")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Upload File']")
        )
    ).click()

    time.sleep(8)
    # Get the current working directory
    current_working_directory = os.getcwd()

    # Construct the absolute path
    absolute_path = os.path.abspath(
        os.path.join(current_working_directory, r"Extras\test.png")
    )
    pyautogui.write(absolute_path)
    pyautogui.press("enter")

    time.sleep(4)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
    ).click()

    print("Appointment confirm successfully")

    time.sleep(3)

    while True:
        try:

            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                    )
                )
            )

            next_button.click()

        except:

            break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
            )
        )
    )
    last_element_in_accordian.click()

    time.sleep(3)
    View_Detail_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[contains(text(), 'View Details')]")
        )
    )
    View_Detail_button.click()

    time.sleep(3)
    more_actions_button = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[normalize-space()='More Actions']")
        )
    )
    more_actions_button.click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Share Info']")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='mdc-button__label']"))
    ).click()


####################################################################################################################################################
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Completed Messages")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])  
def test_completed_messages(login):

    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]",
            )
        )
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]",
            )
        )
    )
    element.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
        )
    ).send_keys("920720600")

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Id : 2')]"))
    ).click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "p-dropdown[optionlabel='place']")
            )
        ).click()

        
    login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
    print("location : Chavakkad")
    login.implicitly_wait(5)

    login.find_element(
        By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']"
    ).click()
    login.implicitly_wait(5)
    login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
    print("Department : ENT")
    user_dropdown_xpath = (
        "(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
        "ng-dirty'])[1]"
    )
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))
    ).click()
    user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, user_option_xpath))
    ).click()
    print("Select user : Naveen")

    time.sleep(2)
    element = login.find_element(By.XPATH, "//p-dropdown[@optionlabel='name']")
    scroll_to_element(login, element)
    element.click()

    time.sleep(3)
    service_option = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, ("//li[@aria-label='Naveen Consultation']//div[1]")))
    )
    click_to_element(login, service_option)
    print("Select Service : Naveen Consultation")

    time.sleep(3)
    Today_Date = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']",
            )
        )
    )
    Today_Date.click()
    print("Today Date:", Today_Date.text)
    wait = WebDriverWait(login, 10)
    time_slot = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']"))
    )
    time_slot.click()
    print("Time Slot:", time_slot.text)

    time.sleep(4)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
    ).click()

    print("Appointment confirm successfully")

    time.sleep(3)

    while True:
        try:

            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                    )
                )
            )

            next_button.click()

        except:

            break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
            )
        )
    )
    last_element_in_accordian.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Change Status']")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Complete')]"))
    ).click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
    ).click()

    toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_message.text
    print("Toast Message:", message)


#################################################################################################################################################
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Donation")
@pytest.mark.parametrize("url", [consumer_login_url_1])
def test_donation(con_login):
    time.sleep(5)

    donation = WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Donate Now'])[1]")
            )
        )
    donation.click()
    

    time.sleep(2)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='81234 56789'])[1]"))
    ).send_keys("9207206005")
    
    time.sleep(2)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='continue ng-star-inserted']")
        )
    ).click()

    time.sleep(2)
    otp_digits = "5555"

    # Wait for the OTP input fields to be present
    otp_inputs = WebDriverWait(con_login, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//input[contains(@id, 'otp_')]")
        )
    )

    for i, otp_input in enumerate(otp_inputs):
        otp_input.send_keys(otp_digits[i])

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='continue ng-star-inserted']")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='number']"))
    ).send_keys("400")

    # WebDriverWait(con_login, 10).until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "//textarea[contains(@class,'form-control mgn-bt-20 ng-pristine ng-valid ng-touched')]",
    #         )
    #     )
    # ).send_keys("Donation")

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[contains(text(),'NET BANKING')])[1]")
        )
    ).click()
    
    time.sleep(3)
    proceed_button = WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Proceed'])[1]")
        )
    )

    con_login.execute_script("arguments[0].scrollIntoView();", proceed_button)
    time.sleep(1)
    proceed_button.click()

    time.sleep(2)
    WebDriverWait(con_login, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@src,'razorpay.com')]")))
    time.sleep(5)
    
    netbank_button =  WebDriverWait(con_login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(), 'Netbanking')]"))
        )
    con_login.execute_script("arguments[0].click();", netbank_button)



    time.sleep(2)
    WebDriverWait(con_login, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'State Bank of India')]"))
    ).click()
    
    
    time.sleep(2)
    # WebDriverWait(consumer_login, 10).until(
    # EC.presence_of_element_located(
    #     (By.XPATH,"//div[contains(@class,'ptm-overlay-wrapper btn-enabled')]//img[contains(@class,'ptm-lock-img')]"))
    # ).click()
    # Handle the popup window
    main_window_handle = con_login.current_window_handle
    WebDriverWait(con_login, 10).until(EC.new_window_is_opened)
    all_window_handles = con_login.window_handles
    new_window_handle = None
    for handle in all_window_handles:
        if handle != main_window_handle:
            new_window_handle = handle
            break
        # Switch to the new window
    con_login.switch_to.window(new_window_handle)
    time.sleep(3)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-val='S' and contains(@class, 'success')]"))
    ).click()
    time.sleep(5)
    # Optionally, switch back to the main window
    con_login.switch_to.window(main_window_handle)

    

   
    time.sleep(3)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//strong[normalize-space()='OK'])[1]")
        )
    ).click()

    time.sleep(5)

    
########################################################################################################################################################
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Confirmation,Reschedule,Send Message, Send attachment")
@pytest.mark.parametrize("url", [consumer_login_url_1])
def test_confirmation(consumer_login):
    try:    
        time.sleep(5)
        # Scroll to the element
        consultation = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//h3[normalize-space()='GET YOUR CONSULTATION TODAY'])[1]")
            )
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", consultation)
        
        time.sleep(3)
        wait = WebDriverWait(consumer_login, 30)

        book_now_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//button[@id='btnBookNow'])[3]")
            )
        )
        book_now_button.click()


        time.sleep(3)
        
        location_button = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='deptName ng-star-inserted'][contains(text(),'Chavakkad')]",
                )
            )
        )
        location_button.click()

        wait = WebDriverWait(consumer_login, 10)
        depart_button = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='deptName ng-star-inserted'][normalize-space()='ENT']",
                )
            )
        )
        depart_button.click()

        wait = WebDriverWait(consumer_login, 10)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Dr.Naveen KP')]")
            )
        ).click()

        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//app-appointment-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][contains(text(),'service')]",
                )
            )
        ).click()
        time.sleep(3)
        Today_Date = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@aria-pressed='true'] [@aria-current='date']")
            )
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", Today_Date)
        time.sleep(3) 
        Today_Date.click()
        time.sleep(3)  
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(consumer_login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='mdc-evolution-chip__cell mdc-evolution-chip__cell--primary'])[1]"))
        )
        consumer_login.execute_script("arguments[0].scrollIntoView();", time_slot)
        time.sleep(2)
        time_slot.click()
        
        print("Time Slot:", time_slot.text)
        
        consumer_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Next']")
            )
        ).click()
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='81234 56789'])[1]"))
        ).send_keys("9207206005")
        
        consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

        time.sleep(5)

        otp_digits = "5555"
        # otp_digits = "55555"
        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(consumer_login, 10).until(
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

        consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

        # time.sleep(3)

        time.sleep(3)
        consumer_notes = WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//textarea[@placeholder='Add Notes you may have...']")
        )
        )
        consumer_notes.send_keys("Notes added from consumer side")
        time.sleep(5)
        consumer_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='uploadFileTxt']"))
        ).click()
        time.sleep(2)
        
        current_working_directory = os.getcwd()
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        time.sleep(2)
        pyautogui.write(absolute_path)
        time.sleep(2)
        pyautogui.press("enter")

        consumer_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        confirmbutton = WebDriverWait(consumer_login, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm']")
            )
        )
        confirmbutton.click()

        print("Clicked Confirm button")
        time.sleep(5)
        # Step 1: Extract Booking ID
        booking_id_element = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='bookingIdFlex']/div"))
        )
        booking_id = booking_id_element[1].text.strip()
        print(f"Booking ID: {booking_id}")

        # Step 2: Click OK
        WebDriverWait(consumer_login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Ok']"))
        ).click()

        print("Clicked OK button")

        time.sleep(3)

        # Step 3: Go to My Bookings
        bookings = WebDriverWait(consumer_login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'My Bookings')]"))
        )
        bookings.click()
        time.sleep(3)

        # Step 1: Click "Show more" once (if present)
        try:
            show_more = WebDriverWait(consumer_login, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Show more']"))
            )
            consumer_login.execute_script("arguments[0].scrollIntoView(true);", show_more)
            time.sleep(1)
            show_more.click()
            print("Clicked 'Show more'")
            time.sleep(2)  # Wait for new content to begin loading

            # Scroll to bottom to ensure all lazy-loaded cards are loaded
            last_height = consumer_login.execute_script("return document.body.scrollHeight")
            while True:
                consumer_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                new_height = consumer_login.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            print("Scrolled to bottom to load all cards.")
        except:
            print("No 'Show more' button found or it's already fully expanded.")

        # Step 2: Loop through all loaded cards to find the booking ID
        found = False
        cards = consumer_login.find_elements(By.XPATH, "//app-appt-card")
        print(f"Total cards found: {len(cards)}")

        for card in cards:
            try:
                # card_booking_id_elem = card.find_element(By.XPATH, ".//div[@class='cstmTxt field-head' and text()='Booking Id']/following-sibling::div")
                card_booking_id_elem = card.find_element(
                    By.XPATH,
                    ".//div[normalize-space(text())='Booking Id']/following-sibling::div"
                )

                card_booking_id = card_booking_id_elem.text.strip()
                print(f"Found booking ID in card: '{card_booking_id}'")  # <--- Debug print

                if card_booking_id == booking_id:
                    consumer_login.execute_script("arguments[0].scrollIntoView(true);", card)
                    print(f"Found matching booking ID card: {card_booking_id}")

                    # Click the 3-dot menu inside this card
                    three_dot = card.find_element(By.XPATH, ".//button[contains(@class, 'menu') and i[contains(@class, 'fa-ellipsis-h')]]")
                    WebDriverWait(consumer_login, 5).until(EC.element_to_be_clickable(three_dot))
                    consumer_login.execute_script("arguments[0].scrollIntoView(true);", three_dot)
                    time.sleep(2)
                    three_dot.click()
                    print("Clicked 3-dot menu.")
                    found = True
                    break
            except Exception as e:
                print(f"Error processing a card: {e}")

        if not found:
            print("Booking card not found.")

        time.sleep(3)

        wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//span[contains(text(),'Send Message')])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@id='message'])[1]")
            )
        ).send_keys("Test message from consumer side")

        wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//i[@class='material-icons'])[1]"))
        ).click()

        time.sleep(3)

        current_working_directory = os.getcwd()
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        time.sleep(3)
        pyautogui.press("enter")

        time.sleep(3)
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Send'])[1]"))
        ).click()

        toast_message = WebDriverWait(consumer_login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Send Attachments')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='select-wrapper'])[1]")
            )
        ).click()
        time.sleep(2)
        current_working_directory = os.getcwd()
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        time.sleep(3)
        pyautogui.press("enter")

        time.sleep(2)
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='mdc-button__label'])[1]"))
        ).click()

        toast_message = WebDriverWait(consumer_login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'View Attachments')])[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='fa fa-window-close'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Reschedule')])[1]"))
        ).click()

        time.sleep(3)
        consumer_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        # Calculate tomorrow's date
        tomorrow_date = datetime.now() + timedelta(days=2)
        # Get the day as an integer to avoid leading zeros
        day = tomorrow_date.day  # e.g., 1 for October 1
        # Format for the XPath
        tomorrow_xpath_expression = f"//span[@class='mat-calendar-body-cell-content mat-focus-indicator'][normalize-space()='{day}']"

        print("Tomorrow's XPath Expression:", tomorrow_xpath_expression)

        # Get current month/year element
        current_month_year = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//button[@aria-label='Choose month and year']//span[@class='mat-mdc-button-persistent-ripple mdc-button__ripple']",
                )
            )
        )

        consumer_login.execute_script("arguments[0].scrollIntoView(true);", current_month_year)

        # Click next month if needed
        if current_month_year.text.lower() != tomorrow_date.strftime('%B %Y').lower():
            consumer_login.find_element(By.XPATH, "//button[@aria-label='Next month']").click()
        time.sleep(3)

        # Wait for tomorrow's date element to be clickable
        Tomorrow_Date = WebDriverWait(consumer_login, 10).until(
            EC.element_to_be_clickable((By.XPATH, tomorrow_xpath_expression))
        )
        # Click on tomorrow's date
        Tomorrow_Date.click()
        print("Clicked on Tomorrow Date:", day)
        time.sleep(2)
        wait = WebDriverWait(consumer_login, 20)
        time_slot = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//span[@class='mdc-evolution-chip__action mat-mdc-chip-action mdc-evolution-chip__action--primary mdc-evolution-chip__action--presentational'])[1]"
                )
            )
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Next']"))
        ).click()
        time.sleep(2)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Reschedule']")
            )
        ).click()
        time.sleep(3)

        # Step 1: Extract Booking ID
        booking_id_element = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='bookingIdFlex']/div"))
        )
        booking_id = booking_id_element[1].text.strip()
        print(f"Booking ID: {booking_id}")

        consumer_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        confirmation_button = WebDriverWait(consumer_login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Ok']"))
        )
        confirmation_button.click()

        # toast_message = WebDriverWait(consumer_login, 10).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        # )
        # message = toast_message.text
        # print("Toast Message:", message)

        time.sleep(3)

        bookings = WebDriverWait(consumer_login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'My Bookings')]"))
        )
        bookings.click()
        time.sleep(3)
       
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(), \"Today's Booking\")]")
            )
        ).click()

        time.sleep(2)

        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(), \"Upcoming Bookings\")])[1]")
            )
        ).click()

        time.sleep(5)


        try:
            show_more = WebDriverWait(consumer_login, 30).until(
                EC.presence_of_element_located((By.XPATH, "(//a[normalize-space(.)='Show more'])[1]"))
            )
            consumer_login.execute_script("arguments[0].scrollIntoView(true);", show_more)
            time.sleep(1)
            show_more.click()
            print("Clicked 'Show more'")
            time.sleep(3)  # Wait for new content to begin loading

            # Scroll to bottom to ensure all lazy-loaded cards are loaded
            last_height = consumer_login.execute_script("return document.body.scrollHeight")
            while True:
                consumer_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                new_height = consumer_login.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            print("Scrolled to bottom to load all cards.")
        except:
            print("No 'Show more' button found or it's already fully expanded.")

        # Step 2: Loop through all loaded cards to find the booking ID
        found = False
        cards = consumer_login.find_elements(By.XPATH, "//app-appt-card")
        print(f"Total cards found: {len(cards)}")

        for card in cards:
            try:
                # card_booking_id_elem = card.find_element(By.XPATH, ".//div[@class='cstmTxt field-head' and text()='Booking Id']/following-sibling::div")
                card_booking_id_elem = card.find_element(
                    By.XPATH,
                    ".//div[normalize-space(text())='Booking Id']/following-sibling::div"
                )

                card_booking_id = card_booking_id_elem.text.strip()
                print(f"Found booking ID in card: '{card_booking_id}'")  # <--- Debug print

                if card_booking_id == booking_id:
                    consumer_login.execute_script("arguments[0].scrollIntoView(true);", card)
                    print(f"Found matching booking ID card: {card_booking_id}")
                    time.sleep(2)

                    # Click the 3-dot menu inside this card
                    three_dot = card.find_element(By.XPATH, ".//button[contains(@class, 'menu') and i[contains(@class, 'fa-ellipsis-h')]]")
                    WebDriverWait(consumer_login, 5).until(EC.element_to_be_clickable(three_dot))
                    consumer_login.execute_script("arguments[0].scrollIntoView(true);", three_dot)
                    three_dot.click()
                    print("Clicked 3-dot menu.")
                    found = True
                    break
            except Exception as e:
                print(f"Error processing a card: {e}")

        if not found:
            print("Booking card not found.")

        

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='menuInfo'][normalize-space()='Cancel'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'Change of Plans')])[1]")
            )
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='mdc-button__label'])[1]")
            )
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[@id='btnUser'])[1]"))
        ).click()

        print("Appointment Cancelled Successfully")

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'Dashboard')])[1]")
            )
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='fa fa-home'])[1]")
            )
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='fa fa-commenting-o'])[1]")
            )
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@id='message'])[1]")
            )
        ).send_keys("consumer send the enquriy to the provider")

        time.sleep(1)
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//i[@class='material-icons'])[1]"))
        ).click() 

        time.sleep(2)
        current_working_directory = os.getcwd()
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        time.sleep(3)
        pyautogui.press("enter")

        time.sleep(3)
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Send')])[1]"))
        ).click()

        toast_message = WebDriverWait(consumer_login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)


        time.sleep(5)

   
    
    except Exception as e:
            allure.attach(  # use Allure package, .attach() method, pass 3 params
            consumer_login.get_screenshot_as_png(),  # param1
            # consumer_login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
            )
            raise e


##################################################################################################################################################
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Reschedule")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/visionhospital/"])
def test_reschedule(con_login):
    time.sleep(3)
    book_now_button = WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Book Now']")
        )
    )
    con_login.execute_script("arguments[0].scrollIntoView();", book_now_button)

    # Wait for the element to be clickable
    clickable_book_now_button = WebDriverWait(con_login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Book Now']"))
    )

    # Attempt to click the element
    try:
        clickable_book_now_button.click()
    except:
        # If click is intercepted, click using JavaScript
        con_login.execute_script("arguments[0].click();", clickable_book_now_button)

    time.sleep(2)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class,'serviceName ng-star-inserted')]")
        )
    ).click()

    time.sleep(2)
    Today_Date = WebDriverWait(con_login, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[@aria-pressed='true'] [@aria-current='date']",
            )
        )
    )

    Today_Date.click()

    print("Today Date:", Today_Date.text)

    wait = WebDriverWait(con_login, 10)
    time_slot = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//mat-chip[@aria-selected='true']"))
    )
    time_slot.click()
    print("Time Slot:", time_slot.text)

    con_login.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
    ).send_keys("9207206005")

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='continue ng-star-inserted']")
        )
    ).click()

    time.sleep(2)
    otp_digits = "5555"

    # Wait for the OTP input fields to be present
    otp_inputs = WebDriverWait(con_login, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//input[contains(@id, 'otp_')]")
        )
    )

    for i, otp_input in enumerate(otp_inputs):
        otp_input.send_keys(otp_digits[i])

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='continue ng-star-inserted']")
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Confirm']")
        )
    ).click()

    time.sleep(4)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
    ).click()

    time.sleep(3)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'My Bookings')]")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span//mat-icon[@class='mat-icon notranslate material-icons mat-ligature-font mat-icon-no-color']",
            )
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Reschedule']")
        )
    ).click()

    today_date = datetime.now()
    print(today_date.day)
    today_xpath_expression = "//div[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today'][normalize-space()='{}']".format(
        today_date.day
    )
    print(today_xpath_expression)
    tomorrow_date = today_date + timedelta(days=1)
    print(tomorrow_date.day)

    # current_month_year = WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "//button[@aria-label='Choose month and year']//span[@class='mat-button-wrapper']",
    #         )
    #     )
    # )
    # print(current_month_year.text)
    # print(current_month_year.text.lower())
    # print(tomorrow_date.strftime("%b %Y").lower())
    # if current_month_year.text.lower() != tomorrow_date.strftime("%b %Y").lower():
    #     login.find_element(By.XPATH, "//button[@aria-label='Next month']").click()
    time.sleep(3)
    tomorrow_xpath_expression = "//div[@class='mat-calendar-body-cell-content mat-focus-indicator'][normalize-space()='{}']".format(
        tomorrow_date.day
    )
    print(tomorrow_xpath_expression)

    Tomorrow_Date = WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, tomorrow_xpath_expression))
    )
    Tomorrow_Date.click()

    print("Tomorrow Date:", Tomorrow_Date.text)

    wait = WebDriverWait(con_login, 10)
    time_slot = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//mat-chip[@class='mat-chip mat-focus-indicator text-center mat-primary mat-standard-chip mat-chip-selected ng-star-inserted']",
            )
        )
    )
    time_slot.click()
    print("Time Slot:", time_slot.text)

    time.sleep(3)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Next']"))
    ).click()

    time.sleep(2)

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Reschedule']")
        )
    ).click()

    time.sleep(2)

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
    ).click()

    print("Appointment Rescheduled successfully")


######################################################################################################################################################
