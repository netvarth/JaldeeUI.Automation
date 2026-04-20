from Framework.common_utils import *
import allure
from allure_commons.types import AttachmentType
from Framework.common_dates_utils import *
from selenium.common import TimeoutException , JavascriptException
from selenium.webdriver.support.ui import Select


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
@allure.title("New MR sharing without Prescription")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_NewMR_without_prescription(login):
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

        # msg = get_snack_bar_message(login)
        # print("Snack Bar message :", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='New Visit']")
        time.sleep(2)

        # Assert vt-card appears
        vt_card = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'vt-card')]")
            )
        )

        assert vt_card.is_displayed(), "VT Card did not appear after clicking New Visit"

        wait_and_locate_click(login, By.XPATH, "//button[@class='new-visit-doc-card new-visit-doc-card--blue']")
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add Section']")
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//a[@role='menuitem'])[2]")

        time.sleep(1)
        wait_and_send_keys(login,By.XPATH, "//input[@placeholder = 'Enter Chief Complaint']", "Fever" + Keys.ENTER)

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add Section']")
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//a[@role='menuitem'])[3]")
        time.sleep(1)

        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter History']", "viral fever")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add Section']")
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//a[@role='menuitem'])[4]")
        time.sleep(1)

        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Medication']", "no medication")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add Section']")
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

        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add Section']")
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//a[@role='menuitem'])[6]")
        time.sleep(1)   

        wait_and_send_keys(login, By.XPATH, "//input[@role='searchbox']", "Treatment" )
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(@class,'p-multiselect')"
        " and .//div[contains(@class,'p-multiselect-label') and contains(text(),'Select User')]]")

        time.sleep(2)
        dropdown_xpath = "//span[normalize-space()='Naveen KP']"
        element = login.find_element(By.XPATH, dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        element.click()
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "//button[@class='btn btn-white shadow fw-bold']")
        
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

        upload_element = wait.until(
             EC.presence_of_element_located(((By. XPATH, "//span[normalize-space()='Upload File']"))
        ))
        login.execute_script("arguments[0].scrollIntoView();", upload_element)
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

        wait_and_locate_click(
             By.XPATH, "//i[@class='pi pi-share-alt']"
        )

        wait_and_send_keys(
                By.XPATH, "//textarea[@placeholder='Enter message description']", "Case sharing without prescription in new MR"
        )

        time.sleep(2)

        wait_and_locate_click(
             By.XPATH, "//span[contains(text(),'Email')]"   
        )

        time.sleep(1)
        wait_and_locate_click(
             By.XPATH, "//button[normalize-space()='Share']"
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