from Framework.common_utils import *
import allure
from allure_commons.types import AttachmentType
from Framework.common_dates_utils import *
from selenium.common import TimeoutException , JavascriptException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

####### ENABLE NEW MR SETTING #######

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


    except Exception as e:
            allure.attach(      # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),    # param1
            # login.screenshot()
            name="full_page",                 # param2
            attachment_type=AttachmentType.PNG)
            raise e


####### CREATE CASE FROM PATIENT RECORD IN THE TOKEN DETAILS PAGE #######


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("New MR sharing with only case from patient record")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_NewMR_withonly_case_from_patient_record(login):
    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH,
        "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
                )
        
        time.sleep(5)
        wait_and_locate_click(login, 
                    By.XPATH,
                    "//span[normalize-space()='Token']"
                )
        
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//b[normalize-space()='Create New Patient']")

        login.implicitly_wait(3)
        wait_and_locate_click(login, By.XPATH, "//mat-select[@placeholder='Select']")

        time.sleep(3)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        wait_and_locate_click(login, By.XPATH, salutation_option_xpath)

        time.sleep(3)
        first_name, last_name, phonenumber, email = create_users_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(
            By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
        ).send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[normalize-space()='Save']").click()

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")

        msg=get_snack_bar_message(login)
        print("Snackbar Message:", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        time.sleep(1)
        
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Chavakkad']")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='ENT'])")
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen KP'])")
        
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon ng-star-inserted fa fa-caret-down'])[1]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen service prepayment'])")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, 
        "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today'] "
            )
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "//a[@id='actnAddNote_BUS_notAttch']")
        time.sleep(2)

        wait_and_send_keys(login, By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']", "Walkintoken booking")
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnSave_BUS_addNote']")
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "//a[@id='actnImg_BUS_notAttch']")
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

        wait_and_locate_click(login, By.XPATH, "//button[contains(@class, 'confirmBtn')]")

        msg = get_snack_bar_message(login)
        print("Snackbar Message:", msg)
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

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='+ Create Case']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@type='button'][normalize-space()='Create Case']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_description_edit_btn']")

        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, 
        "//textarea[@placeholder='Add description...']", "Case description added for testing")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='newcase_upload_file_btn'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)

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
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Treatment Notes']"))
        ).send_keys("Note for the treatment")
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']"))
        ).click()

        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-share-alt']")

        wait_and_send_keys(
                login, By.XPATH, "//textarea[@placeholder='Enter message description']", "Case sharing without prescription in new MR"
        )

        time.sleep(2)

        wait_and_locate_click(
             login, By.XPATH, "//span[contains(text(),'Email')]"   
        )

        time.sleep(1)
        wait_and_locate_click(
             login, By.XPATH, "//button[normalize-space()='Share']"
        )

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)
        
        
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("New MR sharing with only Prescription from patient record")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_NewMR_withonly_prescription_from_patient_record(login):
    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)

        wait_and_locate_click(login, 
                    By.XPATH,
                    "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
                )
        
        time.sleep(5)
        wait_and_locate_click(login, 
                    By.XPATH,
                    "//span[normalize-space()='Token']"
                )
        
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//b[normalize-space()='Create New Patient']")

        # login.implicitly_wait(3)
        # wait_and_locate_click(login, By.XPATH, "//mat-select[@placeholder='Select']")

        # time.sleep(3)
        # salutation = generate_random_salutation()
        # salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        # wait_and_locate_click(login, By.XPATH, salutation_option_xpath)

        time.sleep(3)
        first_name, last_name, phonenumber, email = create_users_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(
            By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
        ).send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[normalize-space()='Save']").click()

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")

        msg=get_snack_bar_message(login)
        print("Snackbar Message:", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        time.sleep(1)
        
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Chavakkad']")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='ENT'])")
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen KP'])")
        
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon ng-star-inserted fa fa-caret-down'])[1]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen service prepayment'])")
        time.sleep(3)

        wait_and_locate_click(
            login, By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today'] "
            )
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "//a[@id='actnAddNote_BUS_notAttch']")
        time.sleep(2)

        wait_and_send_keys(login, By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']", "Walkintoken booking")
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnSave_BUS_addNote']")
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "//a[@id='actnImg_BUS_notAttch']")
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

        wait_and_locate_click(login, By.XPATH, "//button[contains(@class, 'confirmBtn')]")

        msg = get_snack_bar_message(login)
        print("Snackbar Message:", msg)
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

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='+ Create Case']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@type='button'][normalize-space()='Create Case']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_description_edit_btn']")

        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, 
        "//textarea[@placeholder='Add description...']", "Case description added for testing")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='newcase_upload_file_btn'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)

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
        wait_and_locate_click(login, By.XPATH, "(//i[@class='fa fa-edit pointer-cursor ng-star-inserted'])[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen KP'])")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//textarea[@placeholder='Add visit summary...'])[1]")

        time.sleep(4)
        wait_and_send_keys(
             login, By.XPATH, "(//textarea[@placeholder='Add visit summary...'])[1]", "visit summary of the patient"
        )

        # Click Create Rx button
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_visit_create_rx_btn']")

        time.sleep(2)
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

        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//button[@ptooltip='Share' and .//img[@alt='share']])[1]")

        time.sleep(2)
        wait_and_send_keys(
                login, By.XPATH, "//textarea[@placeholder='Enter message description']", "Case sharing with only prescription in new MR"
        )

        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'Email')]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Share']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)

        # EDIT PRESCRIPTION

        # Click 3 dots against the prescription
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@ptooltip='More actions' "
        "and .//i[contains(@class,'fa-ellipsis-h')]])[1]")

        # Select Edit from the 3 dots
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Edit'])[1]")

        # Delete the last medicine added in the prescription
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[contains(@class,'rx-danger-link') "
        "and .//i[contains(@class,'pi-trash')]])[last()]")

        time.sleep(3)
        # click top-right + Add button to open Add Medicine section again to add a medicine
        wait_and_locate_click(
                    login,
                    By.XPATH,
                    "//button[contains(@class,'rx-link-btn') and .//i[contains(@class,'pi-plus')] and contains(., 'Add')]"
                )
        
        medicines = [
            ["Ibuprofen", "200MG", "0-0-1", "6 DAYS", "AFTER FOOD"]
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
       
        # Click SAVE button to save the prescription
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[contains(@class,'rx-primary-btn') and contains(normalize-space(), 'Save')]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        # CLONE RX

        # Click 3 dots against the prescription
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "(//button[@ptooltip='More actions' "
        "and .//i[contains(@class,'fa-ellipsis-h')]])[1]")

        # Select Clone Rx from the 3 dots
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[contains(@class,'mat-mdc-menu-item') and contains(normalize-space(.),'Clone Rx')]")

        time.sleep(3)
        # click top-right + Add button to open Add Medicine section again to add a medicine
        wait_and_locate_click(
                    login,
                    By.XPATH,
                    "//button[contains(@class,'rx-link-btn') and .//i[contains(@class,'pi-plus')] and contains(., 'Add')]"
                )
        
        medicines = [
            ["Cetirizine", "10MG", "0-1-0", "10 DAYS", "BEFOR OR AFTER FOOD"]
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
       
        # Click SAVE button to save the prescription
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[contains(@class,'rx-primary-btn') and contains(normalize-space(), 'Save')]")


    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("New MR sharing with only uploaded Prescription from patient record")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_NewMR_withonly_uploadedprescription_from_patient_record(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)

        wait_and_locate_click(login, 
                    By.XPATH,
                    "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
                )
        
        time.sleep(5)
        wait_and_locate_click(login, 
                    By.XPATH,
                    "//span[normalize-space()='Token']"
                )
        
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//b[normalize-space()='Create New Patient']")

        login.implicitly_wait(3)
        wait_and_locate_click(login, By.XPATH, "//mat-select[@placeholder='Select']")

        time.sleep(3)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        wait_and_locate_click(login, By.XPATH, salutation_option_xpath)

        time.sleep(3)
        first_name, last_name, phonenumber, email = create_users_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(
            By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
        ).send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[normalize-space()='Save']").click()

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")

        msg=get_snack_bar_message(login)
        print("Snackbar Message:", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        time.sleep(1)
        
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Chavakkad']")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='ENT'])")
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen KP'])")
        
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon ng-star-inserted fa fa-caret-down'])[1]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen service prepayment'])")
        time.sleep(3)

        wait_and_locate_click(
            login, By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today'] "
            )
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "//a[@id='actnAddNote_BUS_notAttch']")
        time.sleep(2)

        wait_and_send_keys(login, By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']", "Walkintoken booking")
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnSave_BUS_addNote']")
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "//a[@id='actnImg_BUS_notAttch']")
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

        wait_and_locate_click(login, By.XPATH, "//button[contains(@class, 'confirmBtn')]")

        msg = get_snack_bar_message(login)
        print("Snackbar Message:", msg)
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
        wait_and_locate_click(login, By.XPATH, "(//i[@class='fa fa-edit pointer-cursor ng-star-inserted'])[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen KP'])")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//textarea[@placeholder='Add visit summary...'])[1]")

        time.sleep(4)
        wait_and_send_keys(
             login, By.XPATH, "(//textarea[@placeholder='Add visit summary...'])[1]", "visit summary of the patient"
        )

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_visit_create_rx_btn']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//mat-select[@role='combobox' and .//span[normalize-space()='Amber Gordon']]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//mat-option[contains(@class,'mat-mdc-option') "
        "and contains(normalize-space(.),'Naveen KP')]")

        time.sleep(3)
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
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[@ptooltip='Share' and .//img[@alt='share']]")

        time.sleep(2)
        wait_and_send_keys(
                login, By.XPATH, "//textarea[@placeholder='Enter message description']", "Case sharing with only uploaded prescription in new MR"
        )

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'Email')]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Share']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)

        # Test case of Cancel the uploaded prescription of different doctor

        time.sleep(1)
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

        # Catching the 3 dot against the prescription
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[@ptooltip='More actions' and .//i[contains(@class,'fa-ellipsis-h')]]")

        # Selecting CANCEL from the 3 dots
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@role='menuitem' and contains(@class,'mat-mdc-menu-item') "
        "and .//i[contains(@class,'fa-close')] and contains(normalize-space(.),'Cancel')]")

        # Catch / wait for the confirmation popup
        time.sleep(1)
        popup_xpath = ("//mat-dialog-container[@role='dialog' "
        "and .//p[contains(normalize-space(), " "'Are you sure you want to cancel this prescription')]]")

        popup = WebDriverWait(login, 10).until(EC.visibility_of_element_located((By.XPATH, popup_xpath)))

        # Click YES button inside the caught popup
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//mat-dialog-container[@role='dialog']//button[contains(@class,'checkavailabilitybutton') " \
        "and normalize-space()='Yes']")
        time.sleep(2)

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("New MR sharing with case and Prescription from patient record")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_NewMR_with_caseandprescriptions_from_patient_record(login):
    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH,
        "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
                )
        
        time.sleep(5)
        wait_and_locate_click(login, 
                    By.XPATH,
                    "//span[normalize-space()='Token']"
                )
        
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//b[normalize-space()='Create New Patient']")

        # login.implicitly_wait(3)
        # wait_and_locate_click(login, By.XPATH, "//mat-select[@placeholder='Select']")

        # time.sleep(3)
        # salutation = generate_random_salutation()
        # salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        # wait_and_locate_click(login, By.XPATH, salutation_option_xpath)

        time.sleep(3)
        first_name, last_name, phonenumber, email = create_users_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(
            By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
        ).send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[normalize-space()='Save']").click()

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")

        msg=get_snack_bar_message(login)
        print("Snackbar Message:", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        time.sleep(1)
        
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Chavakkad']")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='ENT'])")
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen KP'])")
        
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon ng-star-inserted fa fa-caret-down'])[1]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen service prepayment'])")
        time.sleep(3)

        wait_and_locate_click(
            login, By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today'] "
            )
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "//a[@id='actnAddNote_BUS_notAttch']")
        time.sleep(2)

        wait_and_send_keys(login, By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']", "Walkintoken booking")
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnSave_BUS_addNote']")
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "//a[@id='actnImg_BUS_notAttch']")
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

        wait_and_locate_click(login, By.XPATH, "//button[contains(@class, 'confirmBtn')]")

        msg = get_snack_bar_message(login)
        print("Snackbar Message:", msg)
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


    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e



####### CREATE CASE FROM TOKEN DETAILS PAGE #######

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("New MR sharing with only case from token details")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_NewMR_withonly_case_from_token_details(login):
    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH,
        "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
                )
        
        time.sleep(5)
        wait_and_locate_click(login, 
                    By.XPATH,
                    "//span[normalize-space()='Token']"
                )
        
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//b[normalize-space()='Create New Patient']")

        login.implicitly_wait(3)
        wait_and_locate_click(login, By.XPATH, "//mat-select[@placeholder='Select']")

        time.sleep(3)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        wait_and_locate_click(login, By.XPATH, salutation_option_xpath)

        time.sleep(3)
        first_name, last_name, phonenumber, email = create_users_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(
            By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
        ).send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[normalize-space()='Save']").click()

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")

        msg=get_snack_bar_message(login)
        print("Snackbar Message:", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        time.sleep(1)
        
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Chavakkad']")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='ENT'])")
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen KP'])")
        
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon ng-star-inserted fa fa-caret-down'])[1]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen service prepayment'])")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, 
        "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today'] "
            )
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "//a[@id='actnAddNote_BUS_notAttch']")
        time.sleep(2)

        wait_and_send_keys(login, By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']", "Walkintoken booking")
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnSave_BUS_addNote']")
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "//a[@id='actnImg_BUS_notAttch']")
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

        wait_and_locate_click(login, By.XPATH, "//button[contains(@class, 'confirmBtn')]")

        msg = get_snack_bar_message(login)
        print("Snackbar Message:", msg)
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
    

        # Click Create Case button from token details page
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnCreateCase_BUS_bookAction']")

        # Click Create Case button from the pop up
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@type='button'][normalize-space()='Create Case']")

        # Add case description
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_description_edit_btn']")

        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, 
        "//textarea[@placeholder='Add description...']", "Case description added for testing")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='newcase_upload_file_btn'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)


        # time.sleep(2)
        # wait_and_locate_click(login, By.XPATH, "(//button[@id='newcase_upload_file_btn'])[1]")

        # Upload case files
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

        # Click New Visit button
        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_new_visit_btn']")
        time.sleep(2)

        # Assert vt-card appears
        vt_card = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'vt-card')]")
            )
        )

        assert vt_card.is_displayed(), "VT Card did not appear after clicking New Visit"

        # Click on Add Clinical Notes button in the visit card
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_add_clinical_notes_btn']")
        

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
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Treatment Notes']"))
        ).send_keys("Note for the treatment")
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']"))
        ).click()

        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-share-alt']")

        wait_and_send_keys(
                login, By.XPATH, "//textarea[@placeholder='Enter message description']", "Case sharing without prescription in new MR"
        )

        time.sleep(2)

        wait_and_locate_click(
             login, By.XPATH, "//span[contains(text(),'Email')]"   
        )

        time.sleep(1)
        wait_and_locate_click(
             login, By.XPATH, "//button[normalize-space()='Share']"
        )

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)
        
        
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("New MR sharing with only Prescription from token details")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_NewMR_withonly_prescription_from_token_details(login):
    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)

        wait_and_locate_click(login, 
                    By.XPATH,
                    "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
                )
        
        time.sleep(5)
        wait_and_locate_click(login, 
                    By.XPATH,
                    "//span[normalize-space()='Token']"
                )
        
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//b[normalize-space()='Create New Patient']")

        login.implicitly_wait(3)
        wait_and_locate_click(login, By.XPATH, "//mat-select[@placeholder='Select']")

        time.sleep(3)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        wait_and_locate_click(login, By.XPATH, salutation_option_xpath)

        time.sleep(3)
        first_name, last_name, phonenumber, email = create_users_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(
            By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
        ).send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[normalize-space()='Save']").click()

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")

        msg=get_snack_bar_message(login)
        print("Snackbar Message:", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        time.sleep(1)
        
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Chavakkad']")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='ENT'])")
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen KP'])")
        
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon ng-star-inserted fa fa-caret-down'])[1]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen service prepayment'])")
        time.sleep(3)

        wait_and_locate_click(
            login, By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today'] "
            )
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "//a[@id='actnAddNote_BUS_notAttch']")
        time.sleep(2)

        wait_and_send_keys(login, By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']", "Walkintoken booking")
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnSave_BUS_addNote']")
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "//a[@id='actnImg_BUS_notAttch']")
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

        wait_and_locate_click(login, By.XPATH, "//button[contains(@class, 'confirmBtn')]")

        msg = get_snack_bar_message(login)
        print("Snackbar Message:", msg)
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
      
        # Click Create Case button from token details page
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnCreateCase_BUS_bookAction']")

        
        # Click Create Case button from the pop up
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@type='button'][normalize-space()='Create Case']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_description_edit_btn']")

        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, 
        "//textarea[@placeholder='Add description...']", "Case description added for testing")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='newcase_upload_file_btn'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)

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

        # Click on Add Clinical Notes button in the visit card
        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_add_clinical_notes_btn']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='fa fa-edit pointer-cursor ng-star-inserted'])[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen KP'])")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//textarea[@placeholder='Add visit summary...'])[1]")

        time.sleep(4)
        wait_and_send_keys(
             login, By.XPATH, "(//textarea[@placeholder='Add visit summary...'])[1]", "visit summary of the patient"
        )

        # Click Create Rx button
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_visit_create_rx_btn']")

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
            wait_and_locate_click(login, By.XPATH, "//section[contains(@class,'rx-composer-card')]//button[contains(@class,'rx-primary-btn') "
            "and not(contains(@class,'disabled')) and contains(., 'Add')]"
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

        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//button[@ptooltip='Share' and .//img[@alt='share']])[1]")

        time.sleep(2)
        wait_and_send_keys(
                login, By.XPATH, "//textarea[@placeholder='Enter message description']", "Case sharing with only prescription in new MR"
        )

        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'Email')]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Share']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)

        # EDIT PRESCRIPTION

        # Click 3 dots against the prescription
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@ptooltip='More actions' "
        "and .//i[contains(@class,'fa-ellipsis-h')]])[1]")

        # Select Edit from the 3 dots
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Edit'])[1]")

        # Delete the last medicine added in the prescription
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[contains(@class,'rx-danger-link') "
        "and .//i[contains(@class,'pi-trash')]])[last()]")

        time.sleep(3)
        # click top-right + Add button to open Add Medicine section again to add a medicine
        wait_and_locate_click(
                    login,
                    By.XPATH,
                    "//button[contains(@class,'rx-link-btn') and .//i[contains(@class,'pi-plus')] and contains(., 'Add')]"
                )
        
        medicines = [
            ["Ibuprofen", "200MG", "0-0-1", "6 DAYS", "AFTER FOOD"]
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
       
        # Click SAVE button to save the prescription
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[contains(@class,'rx-primary-btn') and contains(normalize-space(), 'Save')]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        # CLONE RX

        # Click 3 dots against the prescription
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "(//button[@ptooltip='More actions' "
        "and .//i[contains(@class,'fa-ellipsis-h')]])[1]")

        # Select Clone Rx from the 3 dots
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[contains(@class,'mat-mdc-menu-item') and contains(normalize-space(.),'Clone Rx')]")

        time.sleep(3)
        # click top-right + Add button to open Add Medicine section again to add a medicine
        wait_and_locate_click(
                    login,
                    By.XPATH,
                    "//button[contains(@class,'rx-link-btn') and .//i[contains(@class,'pi-plus')] and contains(., 'Add')]"
                )
        
        medicines = [
            ["Cetirizine", "10MG", "0-1-0", "10 DAYS", "BEFOR OR AFTER FOOD"]
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
       
        # Click SAVE button to save the prescription
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[contains(@class,'rx-primary-btn') and contains(normalize-space(), 'Save')]")


    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("New MR sharing with only uploaded Prescription from token details")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_NewMR_withonly_uploadedprescription_from_token_details(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)

        wait_and_locate_click(login, 
                    By.XPATH,
                    "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
                )
        
        time.sleep(5)
        wait_and_locate_click(login, 
                    By.XPATH,
                    "//span[normalize-space()='Token']"
                )
        
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//b[normalize-space()='Create New Patient']")

        login.implicitly_wait(3)
        wait_and_locate_click(login, By.XPATH, "//mat-select[@placeholder='Select']")

        time.sleep(3)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        wait_and_locate_click(login, By.XPATH, salutation_option_xpath)

        time.sleep(3)
        first_name, last_name, phonenumber, email = create_users_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(
            By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
        ).send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[normalize-space()='Save']").click()

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")

        msg=get_snack_bar_message(login)
        print("Snackbar Message:", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        time.sleep(1)
        
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Chavakkad']")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='ENT'])")
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen KP'])")
        
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon ng-star-inserted fa fa-caret-down'])[1]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen service prepayment'])")
        time.sleep(3)

        wait_and_locate_click(
            login, By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today'] "
            )
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "//a[@id='actnAddNote_BUS_notAttch']")
        time.sleep(2)

        wait_and_send_keys(login, By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']", "Walkintoken booking")
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnSave_BUS_addNote']")
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "//a[@id='actnImg_BUS_notAttch']")
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

        wait_and_locate_click(login, By.XPATH, "//button[contains(@class, 'confirmBtn')]")

        msg = get_snack_bar_message(login)
        print("Snackbar Message:", msg)
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
      
        # Click Create Case button from token details page
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnCreateCase_BUS_bookAction']")
        
        # Click Create Case button from the pop up
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
        wait_and_locate_click(login, By.XPATH, "(//i[@class='fa fa-edit pointer-cursor ng-star-inserted'])[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen KP'])")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//textarea[@placeholder='Add visit summary...'])[1]")

        time.sleep(4)
        wait_and_send_keys(
             login, By.XPATH, "(//textarea[@placeholder='Add visit summary...'])[1]", "visit summary of the patient"
        )

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[@id='newcase_visit_create_rx_btn']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//mat-select[@role='combobox' and .//span[normalize-space()='Amber Gordon']]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//mat-option[contains(@class,'mat-mdc-option') "
        "and contains(normalize-space(.),'Naveen KP')]")

        time.sleep(3)
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
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[@ptooltip='Share' and .//img[@alt='share']]")

        time.sleep(2)
        wait_and_send_keys(
                login, By.XPATH, "//textarea[@placeholder='Enter message description']", "Case sharing with only uploaded prescription in new MR"
        )

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'Email')]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Share']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)

        # Test case of Cancel the uploaded prescription of different doctor

        time.sleep(1)
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

        # Catching the 3 dot against the prescription
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[@ptooltip='More actions' and .//i[contains(@class,'fa-ellipsis-h')]]")

        # Selecting CANCEL from the 3 dots
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@role='menuitem' and contains(@class,'mat-mdc-menu-item') "
        "and .//i[contains(@class,'fa-close')] and contains(normalize-space(.),'Cancel')]")

        # Catch / wait for the confirmation popup
        time.sleep(1)
        popup_xpath = ("//mat-dialog-container[@role='dialog' "
        "and .//p[contains(normalize-space(), " "'Are you sure you want to cancel this prescription')]]")

        popup = WebDriverWait(login, 10).until(EC.visibility_of_element_located((By.XPATH, popup_xpath)))

        # Click YES button inside the caught popup
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//mat-dialog-container[@role='dialog']//button[contains(@class,'checkavailabilitybutton') " \
        "and normalize-space()='Yes']")
        time.sleep(2)

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e
    


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("New MR sharing with case and Prescription from token details")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_NewMR_with_caseandprescriptions_from_token_details(login):
    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH,
        "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
                )
        
        time.sleep(5)
        wait_and_locate_click(login, 
                    By.XPATH,
                    "//span[normalize-space()='Token']"
                )
        
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//b[normalize-space()='Create New Patient']")

        login.implicitly_wait(3)
        wait_and_locate_click(login, By.XPATH, "//mat-select[@placeholder='Select']")

        time.sleep(3)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        wait_and_locate_click(login, By.XPATH, salutation_option_xpath)

        time.sleep(3)
        first_name, last_name, phonenumber, email = create_users_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(
            By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
        ).send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[normalize-space()='Save']").click()

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")

        msg=get_snack_bar_message(login)
        print("Snackbar Message:", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        time.sleep(1)
        
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Chavakkad']")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='ENT'])")
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen KP'])")
        
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon ng-star-inserted fa fa-caret-down'])[1]")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Naveen service prepayment'])")
        time.sleep(3)

        wait_and_locate_click(
            login, By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today'] "
            )
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "//a[@id='actnAddNote_BUS_notAttch']")
        time.sleep(2)

        wait_and_send_keys(login, By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']", "Walkintoken booking")
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnSave_BUS_addNote']")
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "//a[@id='actnImg_BUS_notAttch']")
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

        wait_and_locate_click(login, By.XPATH, "//button[contains(@class, 'confirmBtn')]")

        msg = get_snack_bar_message(login)
        print("Snackbar Message:", msg)
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
      
        # Click Create Case button from token details page
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnCreateCase_BUS_bookAction']")

        # Click Create Case button from the pop up
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

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Step Notes']"))
        ).send_keys("Steps for notes")

        time.sleep(2)
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
        "//textarea[@placeholder='Enter message description']", "MR sharing with case and prescription in new MR")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'Email')]")

        time.sleep(1)
        wait_and_locate_click(
             login, By.XPATH, "//button[normalize-space()='Share']"
        )

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)


    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e







##########  DISABLING THE NEW MR SETTINGS ##########

@allure.severity(allure.severity_level.NORMAL)
@allure.title("Disabling MR settings")   
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_MR_setting_disable(login):

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

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e

