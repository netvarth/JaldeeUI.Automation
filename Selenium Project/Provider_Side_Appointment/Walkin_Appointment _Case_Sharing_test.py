from Framework.common_utils import *
import allure
from allure_commons.types import AttachmentType



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Case Sharing")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_without_prescription(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "(//img)[3]")
        
        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//div[@id='actionCreate_BUS_bookList'])[1]",
                )
            )
        )
        element.click()
        time.sleep(3)
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='btnCreateCust_BUS_appt']")
            )
        )
        element_appoint.click()
        time.sleep(2)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
        login.implicitly_wait(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
        ).click()

        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        login.implicitly_wait(5)

        login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
        print("Department : ENT")
        user_dropdown_xpath = ("(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
                            "ng-dirty'])[1]")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_option_xpath))).click()
        print("Select user : Naveen")
        # time.sleep(3)
        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        # WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_dropdown_xpath))).click()
        element = login.find_element(By.XPATH, service_dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        time.sleep(2)
        service_option_xpath = ("//li[@aria-label='Naveen Consultation']//div[1]")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
        print("Select Service : Naveen Consultation")
        time.sleep(3)

        Today_Date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
        Today_Date.click()
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(login, 10)
        time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
        time_slot.click()
        print("Time Slot:", time_slot.text)
        note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
        note_input.click()
        login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys("test_selenium project")
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Upload File']"))
        ).click()

        time.sleep(4)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))
        pyautogui.write(absolute_path)
        pyautogui.press('enter')

        time.sleep(4)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='btnConfirm_BUS_apptForm']"))
        ).click()


        msg = get_snack_bar_message(login)
        print("Snack Bar message :", msg)
        
        time.sleep(3)

        while True:
                try:
                    next_button = WebDriverWait(login, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//button[@class='p-ripple p-element p-paginator-last p-paginator-element p-link ng-star-inserted']"))
                    )                   

                    next_button.click()

                except:
                    break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(3)
        View_Detail_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'View Details')]"))
        )
        View_Detail_button.click()

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Patient Record']")
        
        login.implicitly_wait(5)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='+ Create Case']")
    
        time.sleep(3)
        wait_and_send_keys(login, By.XPATH, "//textarea[@placeholder='Add any initial observations or background information...']", "test case for case")
        

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//button[@type='button'][normalize-space()='Create Case'])[1]"
        )
        

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
        
        msg = get_toast_message(login)
        print("Toast Message :", msg)

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

        msg = get_toast_message(login)
        print("Toast Message :", msg)

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

        msg = get_toast_message(login)
        print("Toast Message :", msg)

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
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='Prescription']")
        #     )
        # ).click()

        # for i in range(5):
        #     login.find_element(
        #         By.XPATH, "//button[normalize-space()='+ Add Medicine']"
        #     ).click()
        #     login.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(
        #         "Medicine"
        #     )

        #     before_XPath = "//*[contains(@id, 'pr_id')]/tbody/tr"
        #     aftertd_XPath_1 = "/td[2]"
        #     aftertd_XPath_2 = "/td[3]"
        #     aftertd_XPath_3 = "/td[4]"
        #     aftertd_XPath_4 = "/td[5]"
        #     textarea_xpath = "//input[@role='searchbox']"
        #     row = i + 1
        #     if i > 0:
        #         trXPath = before_XPath + str([row])
        #     else:
        #         trXPath = before_XPath

        #     PreFinalXPath = trXPath + aftertd_XPath_1
        #     FinalXPath = PreFinalXPath + textarea_xpath

        #     Dose = login.find_element(By.XPATH, PreFinalXPath)
        #     Dose.click()
        #     Dose1 = login.find_element(By.XPATH, FinalXPath)
        #     Dose1.send_keys("650 mg")

        #     PreFinalXPath = trXPath + aftertd_XPath_2
        #     FinalXPath = PreFinalXPath + textarea_xpath

        #     Frequency = login.find_element(By.XPATH, PreFinalXPath)
        #     Frequency.click()
        #     Frequency1 = login.find_element(By.XPATH, FinalXPath)
        #     Frequency1.send_keys("1-1-1")

        #     PreFinalXPath = trXPath + aftertd_XPath_3
        #     FinalXPath = PreFinalXPath + textarea_xpath
        #     Duration = login.find_element(By.XPATH, PreFinalXPath)
        #     Duration.click()
        #     Duration1 = login.find_element(By.XPATH, FinalXPath)
        #     Duration1.send_keys("5 Days")

        #     PreFinalXPath = trXPath + aftertd_XPath_4
        #     FinalXPath = PreFinalXPath + textarea_xpath
        #     Notes = login.find_element(By.XPATH, PreFinalXPath)
        #     Notes.click()
        #     Notes1 = login.find_element(By.XPATH, FinalXPath)
        #     Notes1.send_keys("After Food")

        
       
        # dropdown_element= WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//mat-select[@aria-haspopup='listbox']"))
        # )
        # dropdown_element.click()
        
        # time.sleep(3)
        # element3 = login.find_element(By.XPATH, "//span[@class='mdc-list-item__primary-text']//div[contains(text(),'Naveen KP')]")
        # login.execute_script("arguments[0].click();", element3)
        
        
    
        # time.sleep(2)
        # login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        # time.sleep(2)
        # msg = get_toast_message(login)
        # print("Toast Message :", msg)
        
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

        time.sleep(1)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Email')]"))
        ).click()
        
        # time.sleep(2)

        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[contains(text(),'Whatsapp')]"))
        # ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(),'Share')]")
            )
        ).click()

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(3)
    except Exception as e:
        allure.attach(      # use Allure package, .attach() method, pass 3 params
        login.get_screenshot_as_png(),    # param1
        # login.screenshot()
        name="full_page",                 # param2
        attachment_type=AttachmentType.PNG)
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Prescription in case Sharing")    
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_with_prescription(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "(//img)[3]")
        
        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//div[@id='actionCreate_BUS_bookList'])[1]",
                )
            )
        )
        element.click()
        time.sleep(3)
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='btnCreateCust_BUS_appt']")
            )
        )
        element_appoint.click()
        time.sleep(2)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
        login.implicitly_wait(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
        ).click()

        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        login.implicitly_wait(5)

        login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
        print("Department : ENT")
        user_dropdown_xpath = ("(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
                            "ng-dirty'])[1]")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_option_xpath))).click()
        print("Select user : Naveen")
        # time.sleep(3)
        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        # WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_dropdown_xpath))).click()
        element = login.find_element(By.XPATH, service_dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        time.sleep(2)
        service_option_xpath = ("//li[@aria-label='Naveen Consultation']//div[1]")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
        print("Select Service : Naveen Consultation")
        time.sleep(3)

        Today_Date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
        Today_Date.click()
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(login, 10)
        time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
        time_slot.click()
        print("Time Slot:", time_slot.text)
        note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
        note_input.click()
        login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys("test_selenium project")
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Upload File']"))
        ).click()

        time.sleep(4)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))
        pyautogui.write(absolute_path)
        pyautogui.press('enter')

        time.sleep(4)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='btnConfirm_BUS_apptForm']"))
        ).click()


        msg = get_snack_bar_message(login)
        print("Snack Bar message :", msg)
        
        time.sleep(3)

        while True:
                try:
                    next_button = WebDriverWait(login, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//button[@class='p-ripple p-element p-paginator-last p-paginator-element p-link ng-star-inserted']"))
                    )

                    next_button.click()

                except:
                    break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(3)
        View_Detail_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'View Details')]"))
        )
        View_Detail_button.click()

        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Patient Record']")
        
        login.implicitly_wait(5)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='+ Create Case']")
    
        time.sleep(3)
        wait_and_send_keys(login, By.XPATH, "//textarea[@placeholder='Add any initial observations or background information...']", "test case for case")
        

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//button[@type='button'][normalize-space()='Create Case'])[1]"
        )

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
        
        msg = get_toast_message(login)
        print("Toast Message :", msg)

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

        msg = get_toast_message(login)
        print("Toast Message :", msg)

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

        msg = get_toast_message(login)
        print("Toast Message :", msg)

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
        msg = get_toast_message(login)
        print("Toast Message :", msg)
        
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

        time.sleep(1)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Email')]"))
        ).click()
        
        # time.sleep(2)

        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[contains(text(),'Whatsapp')]"))
        # ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(),'Share')]")
            )
        ).click()

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(3)
    except Exception as e:
        allure.attach(      # use Allure package, .attach() method, pass 3 params
        login.get_screenshot_as_png(),    # param1
        # login.screenshot()
        name="full_page",                 # param2
        attachment_type=AttachmentType.PNG)
        raise e

@allure.severity(allure.severity_level.NORMAL)
@allure.title("Preview, Print, Download")   
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_Case_Status(login):  
        
    try:
        wait = WebDriverWait(login, 30)
        time.sleep(3) 
        wait_and_locate_click(login, By.XPATH, "(//img)[3]")
        
        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//div[@id='actionCreate_BUS_bookList'])[1]",
                )
            )
        )
        element.click()

        # time.sleep(3)
        # wait = WebDriverWait(login, 10)
        # element_appoint = wait.until(EC.presence_of_element_located(
        #     (By.XPATH, "//b[contains(text(),'Create New Patient')]")))
        # element_appoint.click()
        # login.implicitly_wait(3)
        # first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        # login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        # login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        # login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        # login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        # login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        # login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        # login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
        # login.implicitly_wait(3)

        wait_and_send_keys(login, By.XPATH, "//*[@placeholder='Enter name or phone or id']", "5556211480")
        time.sleep(3)

        # WebDriverWait(login, 10).until(
        #      EC.presence_of_element_located(
        #           (By.XPATH, "//*[normalize-space()='Id : f6p']"))
        # ).click()
        wait_and_locate_click(
             login, By.XPATH, "//*[normalize-space()='Id : f6p']"
             )

        wait_and_locate_click(
            login, By.XPATH, "//*[@id='selctLoc_BUS_apptForm']"
            )

        time.sleep(2)
        login.find_element(By.XPATH, "//*[@class='ng-star-inserted'][normalize-space()='Chavakkad']").click()
        print("location : Chavakkad")
        
        time.sleep(2)

        login.find_element(
            By.XPATH, "//*[@id='selectDept_BUS_apptForm']"
        ).click()
        
        time.sleep(2)

        login.find_element(
            By.XPATH, "//*[@class='ng-star-inserted'][normalize-space()='ENT']"
            ).click()
        
        print("Department : ENT")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//*[@id='selectUser_BUS_apptForm']")

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "//*[@class='ng-star-inserted'][normalize-space()='Naveen KP']"
        )

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//*[@id='selectService_BUS_apptForm']")

        service_element = WebDriverWait(login, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@aria-label='Naveen Consultation']"))
        )
        scroll_to_element(login, service_element)

        service_element.click()

        print("Select Service : Naveen Consultation")

        time.sleep(3)
        Today_Date = wait.until(
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
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnConfirm_BUS_apptForm']")
            )
        ).click()


        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(4)

        while True:
                try:
                    next_button = WebDriverWait(login, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//button[@class='p-ripple p-element p-paginator-last p-paginator-element p-link ng-star-inserted']"))
                    )

                    next_button.click()

                except:
                    break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(3)
        View_Detail_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'View Details')]"))
        )
        View_Detail_button.click()

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Patient Record']")
        
        login.implicitly_wait(5)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='+ Create Case']")
    
        time.sleep(3)
        wait_and_send_keys(login, By.XPATH, "//textarea[@placeholder='Add any initial observations or background information...']", "test case for case")
        

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//button[@type='button'][normalize-space()='Create Case'])[1]"
        )
        
        time.sleep(2)

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

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(3)

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

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(3)
        wait_and_locate_click(
             login, By.XPATH, "//span[normalize-space()='Share']" 
        )
        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Enter message description']"))
        ).send_keys("case sharing testing")

        login.find_element(By.XPATH, "//span[contains(text(),'Email')]").click()
        # login.find_element(By.XPATH, "//span[contains(text(),'Whatsapp')]").click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Share')]"))
        ).click()

        print("Case file Shared successfully")

        time.sleep(3)
        WebDriverWait(login, 10).until(
             EC.presence_of_element_located(
                  (By.XPATH, "//span[normalize-space()='Preview']"))
        ).click()
        time.sleep(5)

        WebDriverWait(login, 10).until(
             EC.presence_of_element_located(
                  (By.XPATH, "//i[@class='pi pi-times']"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
             EC.presence_of_element_located(
                  (By.XPATH, "//span[normalize-space()='Download']"))
        ).click()
        
        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(3)
        WebDriverWait(login, 10).until(
             EC.presence_of_element_located(
                  (By.XPATH, "//span[normalize-space()='Print']"))
        ).click()
        
        time.sleep(5)


        time.sleep(3)
    except Exception as e:
        allure.attach(      # use Allure package, .attach() method, pass 3 params
        login.get_screenshot_as_png(),    # param1
        # login.screenshot()
        name="full_page",                 # param2
        attachment_type=AttachmentType.PNG)
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Treatment plan with prescription in case Sharing")    
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_treatment_plan(login):
    try:
        time.sleep(5)
        WebDriverWait(login, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]"))
        ).click()
        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]"))
        )
        element.click()
        time.sleep(3)
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//b[contains(text(),'Create New Patient')]")))
        element_appoint.click()
        login.implicitly_wait(3)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
        login.implicitly_wait(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
        ).click()

        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        login.implicitly_wait(5)

        login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
        print("Department : ENT")
        user_dropdown_xpath = ("(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
                            "ng-dirty'])[1]")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_option_xpath))).click()
        print("Select user : Naveen")
        # time.sleep(3)
        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        # WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_dropdown_xpath))).click()
        element = login.find_element(By.XPATH, service_dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        service_option_xpath = ("//li[@aria-label='Naveen Consultation']//div[1]")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
        print("Select Service : Naveen Consultation")
        time.sleep(3)
        Today_Date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
        Today_Date.click()
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(login, 10)
        time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
        time_slot.click()
        print("Time Slot:", time_slot.text)
        note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
        note_input.click()
        login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys("test_selenium project")
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Upload File']"))
        ).click()

        time.sleep(4)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))
        pyautogui.write(absolute_path)
        pyautogui.press('enter')

        time.sleep(4)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='btnConfirm_BUS_apptForm']"))
        ).click()

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

            # print("Appointment confirm successfully")

        time.sleep(4)

        while True:
                try:
                    next_button = WebDriverWait(login, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//button[@class='p-ripple p-element p-paginator-last p-paginator-element p-link ng-star-inserted']"))
                    )

                    next_button.click()

                except:
                    break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(3)
        View_Detail_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'View Details')]"))
        )
        View_Detail_button.click()

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Patient Record']")
        
        login.implicitly_wait(5)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='+ Create Case']")
    
        time.sleep(3)
        wait_and_send_keys(login, By.XPATH, "//textarea[@placeholder='Add any initial observations or background information...']", "test case for case")
        

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//button[@type='button'][normalize-space()='Create Case'])[1]"
        )

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder = 'Enter Chief Complaint']"))
        ).send_keys("Fever")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Save')]"))
        ).click()

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(3)

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

        msg = get_toast_message(login)
        print("Toast Message :", msg)

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
        msg = get_toast_message(login)
        print("Toast Message :", msg)
        
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
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[contains(text(),'Whatsapp')]"))
        # ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(),'Share')]")
            )
        ).click()

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(3)

    except Exception as e:
        allure.attach(      # use Allure package, .attach() method, pass 3 params
        login.get_screenshot_as_png(),    # param1
        # login.screenshot()
        name="full_page",                 # param2
        attachment_type=AttachmentType.PNG)
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Treatment plan without prescription in case Sharing")    
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_treatment_plan_1(login):
    try:
        time.sleep(5)
        WebDriverWait(login, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]"))
        ).click()
        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]"))
        )
        element.click()
        time.sleep(3)
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//b[contains(text(),'Create New Patient')]")))
        element_appoint.click()
        login.implicitly_wait(3)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
        login.implicitly_wait(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
        ).click()

        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        login.implicitly_wait(5)

        login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
        print("Department : ENT")
        user_dropdown_xpath = ("(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
                            "ng-dirty'])[1]")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_option_xpath))).click()
        print("Select user : Naveen")
        # time.sleep(3)
        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        # WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_dropdown_xpath))).click()
        element = login.find_element(By.XPATH, service_dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        service_option_xpath = ("//li[@aria-label='Naveen Consultation']//div[1]")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
        print("Select Service : Naveen Consultation")
        time.sleep(3)
        Today_Date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
        Today_Date.click()
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(login, 10)
        time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
        time_slot.click()
        print("Time Slot:", time_slot.text)
        note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
        note_input.click()
        login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys("test_selenium project")
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Upload File']"))
        ).click()

        time.sleep(4)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))
        pyautogui.write(absolute_path)
        pyautogui.press('enter')

        time.sleep(4)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='btnConfirm_BUS_apptForm']"))
        ).click()

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

            # print("Appointment confirm successfully")

        time.sleep(4)

        while True:
                try:
                    next_button = WebDriverWait(login, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//button[@class='p-ripple p-element p-paginator-last p-paginator-element p-link ng-star-inserted']"))
                    )

                    next_button.click()

                except:
                    break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(3)
        View_Detail_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'View Details')]"))
        )
        View_Detail_button.click()

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Patient Record']")
        
        login.implicitly_wait(5)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='+ Create Case']")
    
        time.sleep(3)
        wait_and_send_keys(login, By.XPATH, "//textarea[@placeholder='Add any initial observations or background information...']", "test case for case")
        

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//button[@type='button'][normalize-space()='Create Case'])[1]"
        )

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder = 'Enter Chief Complaint']"))
        ).send_keys("Fever")

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Save')]"))
        ).click()

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(3)

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

        msg = get_toast_message(login)
        print("Toast Message :", msg)

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
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[contains(text(),'Whatsapp')]"))
        # ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(),'Share')]")
            )
        ).click()

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(3)

    except Exception as e:
        allure.attach(      # use Allure package, .attach() method, pass 3 params
        login.get_screenshot_as_png(),    # param1
        # login.screenshot()
        name="full_page",                 # param2
        attachment_type=AttachmentType.PNG)
        raise e
    
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Share the case from patient record tab menu")   
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_share_case_from_patientrecord(login):

    try:
        time.sleep(3)
        wait_and_locate_click(
            login, By.XPATH, "(//img)[9]"
        )
        
        time.sleep(2)
        wait_and_send_keys(
             login, By.XPATH, "//*[@placeholder='Enter name or phone or id']", "9207206005"
        )
        
        wait_and_locate_click(
             login, By.XPATH, "//span[normalize-space()='Id : 2']"
        )
        
        time.sleep(1)
        wait_and_locate_click(
             login, By.XPATH, "//*[normalize-space()='Patient Record']"
        )
        
        time.sleep(1)
        wait_and_locate_click(
             login, By.XPATH, "(//*[normalize-space()='Share'])[1]"
        )

        time.sleep(1)

        wait_and_send_keys(
             login, By.XPATH, "//textarea[@placeholder='Enter message description']", "Message for the patient"
        )

        wait_and_locate_click(
             login, By.XPATH, "//*[normalize-space()='Email']"
        )

        wait_and_locate_click(
             login, By.XPATH, "//*[normalize-space()='Whatsapp']"
        )

        time.sleep(1)
        wait_and_locate_click(
             login, By.XPATH, "//button[@class='btn btn-primary font-weight-bold confirmBtn']"
        )

        msg = get_toast_message(login)
        print("Toast Message :", msg)        

        time.sleep(3)
    except Exception as e:
            allure.attach(      # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),    # param1
            # login.screenshot()
            name="full_page",                 # param2
            attachment_type=AttachmentType.PNG)
            raise e 
       
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Share multiple case from patient record tab menu")   
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_multiple_share_case(login):

    try:
        time.sleep(3)
        wait_and_locate_click(
            login, By.XPATH, "(//img)[9]"
        )
        
        time.sleep(2)
        wait_and_send_keys(
             login, By.XPATH, "//*[@placeholder='Enter name or phone or id']", "9207206005"
        )
        time.sleep(2)
        wait_and_locate_click(
             login, By.XPATH, "//span[normalize-space()='Id : 2']"
        )
        
        time.sleep(1)
        wait_and_locate_click(
             login, By.XPATH, "//*[normalize-space()='Patient Record']"
        )
        
        time.sleep(1)
        wait_and_locate_click(
             login, By.XPATH, "(//input[@class='pointer-cursor ng-star-inserted'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
             login, By.XPATH, "//button[@class='p-element p-button-raised p-button-primary p-button-rounded p-button p-component ng-star-inserted']"
        )

        time.sleep(1)
        wait_and_send_keys(
             login, By.XPATH, "//textarea[@placeholder='Enter message description']", "Message to Patient"
        )

        wait_and_locate_click(
             login, By.XPATH, "//*[normalize-space()='Email']"
        )

        wait_and_locate_click(
             login, By.XPATH, "//*[normalize-space()='Whatsapp']"
        )

        time.sleep(1)
        wait_and_locate_click(
             login, By.XPATH, "//button[@class='btn btn-primary font-weight-bold confirmBtn']"
        )

        msg = get_toast_message(login)
        print("Toast Message :", msg)        

        time.sleep(3)
    except Exception as e:
            allure.attach(      # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),    # param1
            # login.screenshot()
            name="full_page",                 # param2
            attachment_type=AttachmentType.PNG)
            raise e


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Enabling MR setting")   
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_MR_setting_enable(login):

    try:
        driver = login
        time.sleep(3)
        wait = WebDriverWait(login, 30)
        
        wait_and_locate_click(login, By.XPATH, "(//img[@src='./assets/images/menu/settings.png'])[1]")

        time.sleep(2)
        setting_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Features and Customization']"))
        )

        driver.execute_script("arguments[0].scrollIntoView();", setting_element)

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//p[normalize-space()='Manage MR Settings']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='mdc-switch__icon mdc-switch__icon--off'])[1]")

        msg = get_snack_bar_message(login)
        print("Snack bar message:", msg)

        time.sleep(3)

    except Exception as e:
            allure.attach(      # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),    # param1
            # login.screenshot()
            name="full_page",                 # param2
            attachment_type=AttachmentType.PNG)
            raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Case Sharing without prescription in New MR")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_without_prescription_NewMR(login):
    try:
        driver = login
        wait= WebDriverWait(login, 30)
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "(//img)[3]")
        
        # time.sleep(3)
        # element = driver.find_element(By.XPATH, "(//div[@id='actionCreate_BUS_bookList'])[1]")
        # element.click()

        # time.sleep(3)
        # wait = WebDriverWait(login, 10)
        # element_appoint = driver.find_element(By.XPATH, "//*[@id='btnCreateCust_BUS_appt']")
        # element_appoint.click()

        # time.sleep(2)
        # first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        # driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        # driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        # driver.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        # driver.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        # driver.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        # driver.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        # driver.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
        # driver.implicitly_wait(3)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
        # ).click()

        # driver.implicitly_wait(5)
        # driver.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        # print("location : Chavakkad")
        # driver.implicitly_wait(5)

        # driver.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
        # driver.implicitly_wait(5)
        # driver.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
        # print("Department : ENT")
        # user_dropdown_xpath = ("(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
        #                     "ng-dirty'])[1]")
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))).click()
        # user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, user_option_xpath))).click()
        # print("Select user : Naveen")
        # # time.sleep(3)
        # service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        # # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, service_dropdown_xpath))).click()
        # element = driver.find_element(By.XPATH, service_dropdown_xpath)
        # driver.execute_script("arguments[0].scrollIntoView();", element)
        # element.click()

        # time.sleep(2)
        # service_option_xpath = ("//li[@aria-label='Naveen Consultation']//div[1]")
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
        # print("Select Service : Naveen Consultation")
        # time.sleep(3)

        # Today_Date = wait.until(EC.presence_of_element_located((By.XPATH,
        #                                                         "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
        # Today_Date.click()
        # print("Today Date:", Today_Date.text)
        # wait = WebDriverWait(driver, 10)
        # time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
        # time_slot.click()
        # print("Time Slot:", time_slot.text)
        # note_input = driver.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
        # note_input.click()
        # driver.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys("test_selenium project New MR")
        # WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

        # time.sleep(4)
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//button[@id='btnConfirm_BUS_apptForm']"))
        # ).click()


        # msg = get_snack_bar_message(driver)
        # print("Snack Bar message :", msg)
        
        # time.sleep(3)

        while True:
                try:
                    next_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//button[@class='p-ripple p-element p-paginator-last p-paginator-element p-link ng-star-inserted']"))
                    )                   

                    next_button.click()

                except:
                    break

        last_element_in_accordian = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(3)
        View_Detail_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'View Details')]"))
        )
        View_Detail_button.click()

        time.sleep(3)
        wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='Patient Record']")

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//button[normalize-space()='+ Create Case']")

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//button[@type='button'][normalize-space()='Create Case']")

        # time.sleep(2)
        # wait_and_locate_click(driver, By.XPATH, "//button[@type='button'][normalize-space()='Create Case']")

        # msg = get_snack_bar_message(driver)
        # print("Snack Bar message :", msg)
        time.sleep(3)

        wait_and_locate_click(driver, By.XPATH, "//button[normalize-space()='New Visit']")
        time.sleep(2)


        # Assert vt-card appears
        vt_card = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'vt-card')]")
            )
        )

        assert vt_card.is_displayed(), "VT Card did not appear after clicking New Visit"

        wait_and_locate_click(driver, By.XPATH, "//button[@class='new-visit-doc-card new-visit-doc-card--blue']")
        time.sleep(2)

        wait_and_locate_click(driver, By.XPATH, "//button[normalize-space()='Add Section']")
        time.sleep(2)

        wait_and_locate_click(driver, By.XPATH, "(//a[@role='menuitem'])[2]")

        time.sleep(1)
        wait_and_send_keys(driver,By.XPATH, "//input[@placeholder = 'Enter Chief Complaint']", "Fever" + Keys.ENTER)

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//button[normalize-space()='Save']")

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(3)

        wait_and_locate_click(driver, By.XPATH, "//button[normalize-space()='Add Section']")
        time.sleep(2)

        wait_and_locate_click(driver, By.XPATH, "(//a[@role='menuitem'])[3]")
        time.sleep(1)

        wait_and_send_keys(driver, By.XPATH, "//input[@placeholder='Enter History']", "viral fever" + Keys.ENTER)
       
        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//button[normalize-space()='Save']")

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(3)

        wait_and_locate_click(driver, By.XPATH, "//button[normalize-space()='Add Section']")
        time.sleep(2)

        wait_and_locate_click(driver, By.XPATH, "(//a[@role='menuitem'])[4]")
        time.sleep(1)

        wait_and_send_keys(driver, By.XPATH, "//input[@placeholder='Enter Medication']", "no medication" + Keys.ENTER)

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//button[normalize-space()='Save']")

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(3)

        wait_and_locate_click(driver, By.XPATH, "//button[normalize-space()='Add Section']")
        time.sleep(2)

        wait_and_locate_click(driver, By.XPATH, "(//a[@role='menuitem'])[5]")
        time.sleep(1)

        wait_and_send_keys(driver, By.XPATH, "//input[@placeholder='Enter Pulse Rate , Max : 999']", "560")
        wait_and_send_keys(driver, By.XPATH, "//input[@placeholder='Enter Respiration , Max : 90']", "62")
        wait_and_send_keys(driver, By.XPATH, "//input[@placeholder='Enter Temperature in °F , Max : 200']", "123")
        wait_and_send_keys(driver, By.XPATH, "//input[@placeholder='Enter Systolic , Max : 500']", "264")
        wait_and_send_keys(driver, By.XPATH, "//input[@placeholder='Enter Diastolic , Max : 500']", "287")
        
        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//button[normalize-space()='Save'] ")

        msg = get_toast_message(driver)
        print("Toast Message :", msg)   
        time.sleep(3)   

        wait_and_locate_click(driver, By.XPATH, "//button[normalize-space()='Add Section']")
        time.sleep(2)

        wait_and_locate_click(driver, By.XPATH, "(//a[@role='menuitem'])[9]")
        time.sleep(1)   

        treat_name = "Treatment" + str(uuid.uuid4())[:4]
        treat_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@role='searchbox']"))
        )
        treat_namebox.clear()
        treat_namebox.send_keys(treat_name)

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//div[@class='p-multiselect-label p-placeholder']")

        time.sleep(2)
        dropdown_xpath = wait.until(
             EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Naveen KP']")
        ))
        driver.execute_script("arguments[0].scrollIntoView();", dropdown_xpath)
        time.sleep(1)
        dropdown_xpath.click()

        time.sleep(2)

        wait_and_locate_click(driver, By.XPATH, "//button[@class='btn btn-white shadow fw-bold']")
        
        step_name = "Step" + str(uuid.uuid1())[:1]
        step_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Name']"))
        )
        step_namebox.clear()
        step_namebox.send_keys(step_name)

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")   
        
        time.sleep(2)
        element1 = login.find_element(By.XPATH, "//span[normalize-space()='Naveen KP']")
        login.execute_script("arguments[0].scrollIntoView();", element1)
        time.sleep(1)
        element1.click()
    
        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//button[@class='p-ripple p-element p-multiselect-close p-link p-button-icon-only ng-star-inserted']"
        )
        time.sleep(3)
        
        wait_and_locate_click(
             driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"
        )
        
        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "//li[@aria-label='In Progress']"
        )


        time.sleep(2)
        upload_element = wait.until(
             EC.presence_of_element_located(((By. XPATH, "//label[@for='treatmentPlanAattachments']"))
        ))
        driver.execute_script("arguments[0].click();", upload_element)

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

        wait_and_send_keys(
             driver, By.XPATH, "//textarea[@placeholder='Enter Treatment Notes']", "Note for the treatment"
        )
         
        time.sleep(3)
        wait_and_locate_click(
             driver, By.XPATH, "//button[normalize-space()='Save']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(5)

        upload_element = wait.until(
             EC.presence_of_element_located(((By. XPATH, "//button[@class='btn btn--outline']"))
        ))
        driver.execute_script("arguments[0].scrollIntoView();", upload_element)
        time.sleep(2)
        upload_element.click()

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()
        time.sleep(2)
        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        time.sleep(1)
        pyautogui.press("enter")

        time.sleep(3)
        share_element = wait.until(
             EC.element_to_be_clickable((By.XPATH, "//button[@ptooltip='Share Case']"))
        )
        driver.execute_script("arguments[0].click();", share_element)

        time.sleep(2)
        wait_and_send_keys(
                driver, By.XPATH, "//textarea[@placeholder='Enter message description']", "Case sharing without prescription in new MR"
        )

        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "//span[contains(text(),'Email')]"   
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//button[normalize-space()='Share']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(3)
        

    except Exception as e:
                allure.attach(      # use Allure package, .attach() method, pass 3 params
                login.get_screenshot_as_png(),    # param1
                # login.screenshot()
                name="full_page",                 # param2
                attachment_type=AttachmentType.PNG)
                raise e