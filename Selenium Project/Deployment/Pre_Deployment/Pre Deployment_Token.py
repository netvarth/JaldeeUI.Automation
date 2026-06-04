from ast import arguments
import time
from Framework.common_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Token Pre deployment testing")
@pytest.mark.parametrize("url, username, password", [( scale_url, main_scale, password)])
def test_walkin_token(login):
    try:
        time.sleep(5)
        current_date = datetime.now().strftime("%Y-%m-%d")
        print("Pre-Deployment Provider Token",current_date)

        wait = WebDriverWait(login, 30)
        # WebDriverWait(login, 15).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//img[@src='./assets/images/menu/settings.png']"))
        # ).click()
        
        # time.sleep(3)
        # fea_cust = login.find_element(By.XPATH, "//div[normalize-space(.)='Features and Customization']")
        # login.execute_script("arguments[0].scrollIntoView();", fea_cust)
        
        # time.sleep(3)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[normalize-space()='Custom Fields']"))
        # ).click()
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[normalize-space()='Label']"))
        # ).click()
        
        # label_name1 = "Label" + str(uuid.uuid1())[:3]
        # label_namebox1 = WebDriverWait(login, 10).until(
        # EC.presence_of_element_located((By.XPATH, "//input[@id='displayName']"))
        # )
        # label_namebox1.clear()
        # label_namebox1.send_keys(label_name1)
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[@class='mdc-button__label']"))
        # ).click()
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']"))
        # ).click()
        
        
        # time.sleep(3)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/app-sidebar-menu[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]/div[1]/span[1]/span[1]/span[1]/img[1]"))
        # ).click()

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//span[contains(text(),'Tokens')])[1]")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@id='actionCreate_BUS_bookList']")
        

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
            )
        ).send_keys("8281276241")

        time.sleep(3)
        


        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Id : 456547']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
        ).click()

        login.implicitly_wait(5)
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
        wait = WebDriverWait(login, 10)
        Today_Date = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")   
            )
        )
      
        Today_Date.click()
        print("Today Date:", Today_Date.text)

        print("Time Slot: 00:00 AM - 11:59 PM")


        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Notes')]"))
        ).click()

        login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
            "Note for the walkin Token"
        )

        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
        ).click()
        print("Note added for walkin token")

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
        time.sleep(3)
        pyautogui.write(absolute_path)
        time.sleep(2)
        pyautogui.press("enter")
        print("Successfully upload the file")

        time.sleep(3)
        WebDriverWait(login, 30).until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space(.)='Confirm'])[1]"))
        ).click()
        time.sleep(2)
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


        time.sleep(3)
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


        #************************************** Apply Label ***********************************************

        # time.sleep(3)
        # more_actions_button = WebDriverWait(login, 10).until(
        #     EC.visibility_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='More Actions']")
        #     )
        # )
        # more_actions_button.click()
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='Apply Labels']"))
        # ).click()
        
        # login.implicitly_wait(5)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='Create New']"))
        # ).click()
        
        # label_name = "Label" + str(uuid.uuid1())[:3]
        # label_namebox = WebDriverWait(login, 10).until(
        # EC.presence_of_element_located((By.XPATH, "//input[@id='displayName']"))
        # )
        # label_namebox.clear()
        # label_namebox.send_keys(label_name)
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='Create']"))
        # ).click()
        
        # label_xpath = f"//label[normalize-space()='{label_name}']"

        # # Wait for the label to appear and click on it
        # label = WebDriverWait(login, 10).until(
        # EC.presence_of_element_located((By.XPATH, label_xpath))
        # ).click()
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='Apply']"))
        # ).click()
        
        # Selected_label = WebDriverWait(login, 10).until(
        # EC.presence_of_element_located(
        #         (By.XPATH, label_xpath))
        # )

        # # Get the text of the confirmation message
        # actual_label = Selected_label.text
        # print("Selected Label:", actual_label)

        # # Assert the expected text
        # expected_label = Selected_label.text
        # assert (
        #     actual_label == expected_label
        # ), f"Expected '{expected_label}', but got '{actual_label}'"
        
        # # Applying Filter
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']"))
        # ).click()
        
        # login.implicitly_wait(5)
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//i[@class='pi pi-filter-fill']"))
        # ).click()
        
        # time.sleep(3)
        # Label_filter = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[contains(text(),'Labels')]"))
        # )
        # login.execute_script("arguments[0].scrollIntoView();", Label_filter)
        # Label_filter.click()
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//div[contains(text(),'Select Labels')]"))
        # ).click()

        # time.sleep(3)
        
        #     # Wait for the list to be visible
        # WebDriverWait(login, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, "//ul[@role='listbox']"))
        # )
        
        # # Locate all the list items
        # list_items = WebDriverWait(login, 10).until(
        #     EC.presence_of_all_elements_located((By.XPATH, "//ul[@role='listbox']//li"))
        # )

        # # Get the last item in the list
        # last_item = list_items[-1]

        # # Initialize ActionChains
        # actions = ActionChains(login)

        # # Move to the last item and click it
        # actions.move_to_element(last_item).click().perform()
        
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//timesicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']//*[name()='path' and contains(@d,'M8.01186 7')]"))
        # ).click()
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[contains(text(),'Apply')]"))
        # ).click()
        
        # time.sleep(3)
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')]"))
        #     ).click()
        
        # time.sleep(3)
        # assert (
        #     actual_label == expected_label
        # ), f"Expected '{expected_label}', but got '{actual_label}'"
        
        # time.sleep(2)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//i[@class='pi pi-filter-fill']"))
        # ).click()
        
        # time.sleep(3)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[normalize-space()='Reset']"))
        # ).click()
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//timesicon[contains(@class, 'p-element') and contains(@class, 'p-icon-wrapper') and contains(@class, 'ng-star-inserted')]//*[contains(@class, 'p-icon')]"))
        # ).click()
        
        # time.sleep(2)
        # login.refresh()
        
        # time.sleep(5)
        # while True:
        #     try:
        #         next_button = WebDriverWait(login, 10).until(
        #         EC.presence_of_element_located(
        #             (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']"))
        #         )

        #         next_button.click()

        #     except:
        #         print("error")
        #         break

        # last_element_in_accordian = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (
        #             By.XPATH,
        #             "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
        #         )
        #     )
        # )
        # last_element_in_accordian.click()

        # time.sleep(3)
        # View_Detail_button = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[contains(text(), 'View Details')]")
        #     )
        # )
        # View_Detail_button.click()
        
        time.sleep(3)
        more_actions_button = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[normalize-space()='More Actions']")
            )
        )
        more_actions_button.click()
        # ****************************** Send Message ****************************
        
        time.sleep(4)
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[normalize-space()='Send Message']")
            )
        ).click()

        time.sleep(2)
        login.find_element(By.XPATH, " //textarea[@id='messageData']").send_keys(
            "Send Message to the Patient"
        )

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[normalize-space()='Click here to select the files']")
            )
        ).click()

        time.sleep(4)
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
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'send')]"))
        ).click()

        print("Send Message Successfully")

        # ******************* Send Attachment ************************
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[normalize-space()='Send Attachments']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[normalize-space()='Click here to select the files']")
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

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'send')]"))
        ).click()

        print("Attachment Send Successfully")

        # ********************* Create the Prescription and Sharing *************************

        time.sleep(5)
        WebDriverWait(login, 10)
        login.find_element(By.XPATH, "//span[normalize-space()='Prescriptions']").click()

        for i in range(2):
            login.find_element(
                By.XPATH, "//button[normalize-space()='+ Add Medicine']"
            ).click()
            login.find_element(By.XPATH, "//input[@role='searchbox']").send_keys("Medicine")

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

        dropdown_locator_xpath = "//mat-select[@aria-haspopup='listbox']"
        dropdown_element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, dropdown_locator_xpath))
        )

        dropdown_element.click()

        option_locator_xpath = "//div[normalize-space()='Naveen KP']"
        option_element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_locator_xpath))
        )

        option_element.click()


        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']"))
        ).click()
        
        time.sleep(5)
        print("prescription created successfully")

        login.find_element(By.XPATH, "//img[@alt='share']").click()
        time.sleep(2)
        login.find_element(
            By.XPATH, "//textarea[@placeholder='Enter message description']"
        ).send_keys("prescription message")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Email']"))
        ).click()
        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Whatsapp']"))
        ).click()

        login.find_element(
            By.XPATH, "//button[@type='button'][normalize-space()='Share']"
        ).click()
        print("Prescription Shared Successfully")

        # ************************* Case Creation and Sharing *********************

        time.sleep(5)
        WebDriverWait(login, 10).until(

                EC.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Patient Record']")
                )
            ).click()

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
        
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
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
        

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-multiselectitem//li[contains(@class,'p-multiselect-item') "
        "and @aria-label='Naveen KP']")
        
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

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-multiselect[.//div[contains(@class,'p-multiselect-label') and normalize-space()='Select User']]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-multiselectitem//li[contains(@class,'p-multiselect-item') and @aria-label='Naveen KP']")
        
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

        dropdown_locator_xpath = (
            "//div[contains(@class, 'mat-mdc-select-arrow-wrapper ')]"
        )
        dropdown_element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, dropdown_locator_xpath))
        )

        dropdown_element.click()
        
        time.sleep(3)
        doctor_name = "//span[@class='mdc-list-item__primary-text']//div[contains(text(),'Naveen KP')]"
        element3 = login.find_element(By.XPATH, doctor_name)
        login.execute_script("arguments[0].scrollIntoView();", element3)
        element3.click()

        login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        
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
                (By.XPATH, "//span[contains(text(),'Share')]"))

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

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(),'Share')]"))
        ).click()
    

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        # time.sleep(2)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//i[@class='pi pi-arrow-left back-btn-arrow']")
        #     )
        # ).click()

        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
        #     )
        # ).click()
            
        # while True:
        #     try:
        #         next_button = WebDriverWait(login, 10).until(
        #             EC.presence_of_element_located(
        #                 (
        #                     By.XPATH,
        #                     "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
        #                 )
        #             )
        #         )

        #         next_button.click()

        #     except:
        #         break

        # time.sleep(3)
        # last_element_in_accordian = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (
        #             By.XPATH,
        #             "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
        #         )
        #     )
        # )
        # last_element_in_accordian.click()


        # *********************** Enable New MR Setting ************************

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
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='MR and Diet Settings']")

        time.sleep(2)

        # Wait until MR Settings page opens
        wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(normalize-space(), 'MR Settings')]")))

        # Locate the toggle button
        toggle_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@role='switch']")
            )
        )

        # Get current state
        toggle_state = toggle_button.get_attribute("aria-checked")

        print("Current Toggle State :", toggle_state)

        # If toggle is OFF (false), click and make it ON
        if toggle_state == "false":
            toggle_button.click()
            print("Toggle turned ON")

        # If already ON
        else:
            print("Toggle is already ON")
        time.sleep(3)

        # *************************** Create and share New MR ***********************

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='p-element svg-icon menu-icon ng-star-inserted']//img")
            )
        ).click()

        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
        #     )
        # ).click()
            
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

        time.sleep(3)
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
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'View Details')]"))
        )
        View_Detail_button.click()
      
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Patient Record']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='+ Create Case']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@type='button'][normalize-space()='Create Case']")

        # Adding case description
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_description_edit_btn']")

        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, 
        "//textarea[@placeholder='Add description...']", "Case description added for testing")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='newcase_upload_file_btn'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        # Uploading case files
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='newcase_upload_file_btn'])[1]")

        time.sleep(2)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        print("Successfully upload the file")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_new_visit_btn']")

        time.sleep(2)

        # Assert vt-card appears
        vt_card = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'vt-card')]")
            )
        )

        assert vt_card.is_displayed(), "VT Card did not appear after clicking New Visit"

        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_add_clinical_notes_btn']")
        time.sleep(2)

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='fa fa-edit pointer-cursor ng-star-inserted'])[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen KP'])")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//textarea[@placeholder='Add visit summary...'])[1]")

        time.sleep(2)
        wait_and_send_keys(
             login, By.XPATH, "(//textarea[@placeholder='Add visit summary...'])[1]", "visit summary of the patient"
        )

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_visit_add_section_menu_btn']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//a[@role='menuitem'])[2]")

        time.sleep(1)
        wait_and_send_keys(login,By.XPATH, "//input[@placeholder = 'Enter Chief Complaint']", "Fever" + Keys.ENTER)

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_visit_add_section_menu_btn']")
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//a[@role='menuitem'])[3]")
        time.sleep(1)

        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter History']", "viral fever" + Keys.ENTER)

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_visit_add_section_menu_btn']")
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//a[@role='menuitem'])[4]")
        time.sleep(1)

        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Medication']", "no medication" + Keys.ENTER)

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_visit_add_section_menu_btn']")
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//a[@role='menuitem'])[5]")
        time.sleep(1)

        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Pulse Rate , Max : 999']", "560")
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Respiration , Max : 90']", "62")
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Temperature in °F , Max : 200']", "123")
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Systolic , Max : 500']", "264")
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Diastolic , Max : 500']", "287")
        
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save'] ")

        msg = get_toast_message(login)
        print("Toast Message :", msg)   
        time.sleep(3)   

        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_visit_add_section_menu_btn']")
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//a[@role='menuitem'])[9]")
        time.sleep(1)   

        treat_name = "Treatment" + str(uuid.uuid4())[:4]
        treat_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@role='searchbox']"))
        )
        treat_namebox.clear()
        treat_namebox.send_keys(treat_name)

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='p-multiselect-label p-placeholder']")

        time.sleep(2)
        dropdown_xpath = wait.until(
             EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Naveen KP']")
        ))
        login.execute_script("arguments[0].scrollIntoView();", dropdown_xpath)
        time.sleep(1)
        dropdown_xpath.click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='btn btn-white shadow fw-bold']")
        
        step_name = "Step" + str(uuid.uuid1())[:1]
        step_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Name']"))
        )
        step_namebox.clear()
        step_namebox.send_keys(step_name)

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")
        
        time.sleep(2)
        element1 = login.find_element(By.XPATH, "//span[normalize-space()='Naveen KP']")
        login.execute_script("arguments[0].scrollIntoView();", element1)
        time.sleep(1)
        element1.click()
        
        time.sleep(1)
        wait_and_locate_click(
             login, By.XPATH, "//button[@class='p-ripple p-element p-multiselect-close p-link p-button-icon-only ng-star-inserted']"
        )
        
        time.sleep(3)
        wait_and_locate_click(
             login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"
        )
        
        time.sleep(2)
        wait_and_locate_click(
             login, By.XPATH, "//li[@aria-label='In Progress']"
        )

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
        wait_and_send_keys(login, By.XPATH, "//textarea[@placeholder='Enter Treatment Notes']", "Note for the treatment")

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")

        # Wait for the section/treatment plan to save
        time.sleep(3)

        # Scroll back to top because Create Rx button is at the top of the page
        login.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)

        # Click Create Rx button
        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_visit_create_rx_btn']")

        # Add medicine section

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//mat-select[@role='combobox' and .//span[normalize-space()='Amber Gordon']]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//mat-option[contains(@class,'mat-mdc-option') "
        "and contains(normalize-space(.),'Naveen KP')]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Add Medicine'])[1]")

        medicines = [
            ["Dolo", "500MG", "1-1-1", "5 DAYS", "AFTER FOOD"],
            ["Azithromycin", "250MG", "1-0-1", "3 DAYS", "AFTER FOOD"],
            ["Pantop", "40MG", "1-0-0", "5 DAYS", "BEFORE FOOD"]
        ]

        for i in range(len(medicines)):

            # Add medicine details in Add Medicine section
            time.sleep(2)
            wait_and_send_keys(
                login,
                By.XPATH,
                "//section[contains(@class,'rx-composer-card')]//label[normalize-space()='Select Medicine']/following::input[1]",
                medicines[i][0]
            )

            time.sleep(1)
            wait_and_send_keys(
                login,
                By.XPATH,
                "//section[contains(@class,'rx-composer-card')]//label[normalize-space()='Strength/Dosage']/following::input[1]",
                medicines[i][1]
            )

            time.sleep(1)
            wait_and_send_keys(
                login,
                By.XPATH,
                "//section[contains(@class,'rx-composer-card')]//label[normalize-space()='Frequency']/following::input[1]",
                medicines[i][2]
            )

            time.sleep(1)
            wait_and_send_keys(
                login,
                By.XPATH,
                "//section[contains(@class,'rx-composer-card')]//label[normalize-space()='Duration']/following::input[1]",
                medicines[i][3]
            )

            time.sleep(1)
            wait_and_send_keys(
                login,
                By.XPATH,
                "//section[contains(@class,'rx-composer-card')]//label[normalize-space()='Instructions']/following::input[1]",
                medicines[i][4]
            )

            # Click purple Add button to add medicine into prescription table
            time.sleep(2)
            wait_and_locate_click(
                login,
                By.XPATH,
                "//section[contains(@class,'rx-composer-card')]//button[contains(@class,'rx-primary-btn') and not(contains(@class,'disabled')) and contains(., 'Add')]"
            )

            time.sleep(2)

            # After 1st and 2nd medicine, click top-right + Add button to open Add Medicine section again
            if i < len(medicines) - 1:
                wait_and_locate_click(
                    login,
                    By.XPATH,
                    "//button[contains(@class,'rx-link-btn') and .//i[contains(@class,'pi-plus')] and contains(., 'Add')]"
                )
                
                time.sleep(2)
        wait_and_locate_click(login, By.XPATH,
            "//*[normalize-space()='Prescription Notes']/following::div[@role='textbox' and @contenteditable='true'][1]")

        time.sleep(1)
        wait_and_send_keys(login, By.XPATH,
            "//*[normalize-space()='Prescription Notes']/following::div[@role='textbox' and @contenteditable='true'][1]",
            "Prescription notes for the patient")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[contains(@class,'rx-primary-btn') and contains(normalize-space(), 'Save')]")

        # Upload prescription section

        # Scroll back to top because Create Rx button is at the top of the page
        login.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)

        # Click Create Rx button
        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_visit_create_rx_btn']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
        "//mat-select[@role='combobox' and .//span[normalize-space()='Amber Gordon']]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//mat-option[contains(@class,'mat-mdc-option') "
        "and contains(normalize-space(.),'Naveen KP')]")   

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[contains(@class,'rx-ghost-btn') "
        "and contains(normalize-space(.),'Upload Prescription')]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//a[contains(@class,'cursor-pointer') and normalize-space()='Upload']")   

        time.sleep(4)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        print("Successfully upload the file")
        time.sleep(3)

        # Click SAVE button to save the prescription
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[contains(@class,'rx-primary-btn') and contains(normalize-space(), 'Save')]")
        
        msg = get_toast_message(login)
        print("Toast Message :", msg)


        # Share the prescription
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-share-alt']")

        wait_and_send_keys(login, By.XPATH, 
        "//textarea[@placeholder='Enter message description']", "Case sharing without prescription in new MR")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'Email')]")

        time.sleep(1)
        wait_and_locate_click(
             login, By.XPATH, "//button[normalize-space()='Share']"
        )

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)




        # ******************************** Disable New MR Setting ***********************

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
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='MR and Diet Settings'] ")

        time.sleep(2)

        # Wait until MR Settings page opens
        wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(normalize-space(), 'MR Settings')]")))

        # Locate the toggle button
        toggle_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@role='switch']")
            )
        )

        # Get current state
        toggle_state = toggle_button.get_attribute("aria-checked")

        print("Current Toggle State :", toggle_state)

        # If toggle is ON (true), click and make it OFF
        if toggle_state == "true":
            toggle_button.click()
            print("Toggle turned OFF")

        # If already OFF
        else:
            print("Toggle is already OFF")
        time.sleep(3)



        # # ************************* Auto Invoice and Sharing ****************************

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='p-element svg-icon menu-icon ng-star-inserted']//img")
            )
        ).click()

        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
        #     )
        # ).click()
            
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

        time.sleep(3)
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
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
        ).click()

        time.sleep(5)
        print("Auto Invoice")
        print("Successfully send the Payment Link to the patient")
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
        element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        )

        scroll_to_element(login, element)

        element.click()
        
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
        
        
        time.sleep(2)
        login.find_element(By.XPATH, "//i[@class='fa fa-arrow-left']").click()

        while True:
            try:
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']",
                        )
                    )
                )

                next_button.click()
  
            except:

                break

        time.sleep(3)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
                )
            )
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
        add_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']")
            )
        )
        login.execute_script("arguments[0].scrollIntoView();", add_button)
        login.execute_script("arguments[0].click();", add_button)
        # login.execute_script("arguments[0].click();", view_details_button)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Choose Procedure/Item']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='service']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@class='cs-btn bt1 ml-0'][normalize-space()='Add']")
            )
        ).click()

        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Update']"))
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
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
        ).click()

        time.sleep(5)
        print("Successfully send the Payment Link to the patient")

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
        
        # Adding subservice into the invoice
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
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add Procedure/Item']")
        
        # Adding ADHOC item into the invoice
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Choose Procedure/Item']", "Item1234")

        
        time.sleep(3)
        price = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[contains(@class,'item-price') and @placeholder='Price']"))
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
         
        msg = get_snack_bar_message(login)
        print("Snack Bar Message:", msg)
            
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
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']",
                        )
                    )
                )

                next_button.click()

            except:
                break

        time.sleep(3)
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


        tomorrow_xpath_expression = "//span[@class='example-custom-date-class d-pad-15 ng-star-inserted'][normalize-space()='{}']".format(
            tomorrow_date.day
        )
        print(tomorrow_xpath_expression)

        Tomorrow_Date = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, tomorrow_xpath_expression))
        )
        time.sleep(3)
        Tomorrow_Date.click()
        print("Tomorrow Date:", Tomorrow_Date.text)

        print("Time slot = 00:00AM - 11:59 PM")
        reschedule_button = WebDriverWait(login, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='btn btn-primary reschedule-btn']")
            )
        )
        reschedule_button.click()
        print("Reschedule Successfully")

        time.sleep(3)
        WebDriverWait(login, 10).until( 
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
            )
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@id='selectTime_BUS_bookList']")

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Future']"))
        ).click()

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

        time.sleep(3)

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
                )
            )
        )
        last_element_in_accordian.click()

        # *******************Cancellation **********************

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Change Status']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Cancel')]")) 
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
        
        time.sleep(5)
        
        print("Successfully Cancel Token")
    


    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    


    



