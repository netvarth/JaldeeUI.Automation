from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.common import TimeoutException

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Reschedules  to tomorrow date")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_reschedule_create_patient(login):
    try:
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
        wait_and_click(login, By.XPATH, salutation_option_xpath)
        time.sleep(3)
        first_name, last_name, phonenumber, email = create_users_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(
            By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
        ).send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//label[normalize-space()='Select Location']")
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='place']")
        time.sleep(3)
        user_location =wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Ashok Nagar']")
        print("Select Location:", user_location.text)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mt-2 col-lg-8 col-xxl-6'])[2]")
        time.sleep(3)
        generalservice = wait_and_locate_click(login, By.XPATH, "//li[@aria-label='General Services']")
        print("Select User:", generalservice.text)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='fullName']//div[@class='text-left p-dropdown p-component']")
        assigntounassigneduser = wait_and_locate_click(login, By.XPATH, "//li[@id='p-highlighted-option']")
        print("Assignto:", assigntounassigneduser.text)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='name']//div[@class='text-left p-dropdown p-component']")
        time.sleep(3)
        consultation = wait_and_locate_click(login, By.XPATH, "//li[@aria-label='Consultation']")
        print("Select service:", consultation.text)
        time.sleep(3)
        today_xpath = (
            "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected "
            "mat-calendar-body-today']"
        )
        todayqueue = wait_and_locate_click(login, By.XPATH, today_xpath)
        print("Today's Date:", todayqueue.text)
        wait_and_locate_click(login, By.XPATH, "//div[@class='col-lg-12 col-xxl-12 p-2']//div[@class='p-inputgroup']")
        time.sleep(3)
        selectqueue = wait_and_locate_click(login, By.XPATH, "//li[@class='p-ripple p-element p-dropdown-item p-highlight']["
                    "@id='p-highlighted-option']")
        print("Selected Queue", selectqueue.text)
        time.sleep(3)
        notes = wait_and_locate_click(login, By.XPATH, "//label[normalize-space()='Please upload Notes/Files related to "
                    "your service']")
        login.execute_script("arguments[0].scrollIntoView();", notes)
        wait_and_locate_click(login, By.XPATH, "//div[@class='chip-group']//div[1]//a[1]")
        time.sleep(3)
        wait_and_send_keys(login, By.XPATH, "//textarea[@placeholder='Add Note']", "Walkintoken booking")
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Save']")
        time.sleep(3)
        login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        noteaccordions = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//label[normalize-space()='Notes Added']")
            )
        )
        noteaccordions.click()
        login.execute_script("arguments[0].scrollIntoView();", noteaccordions)
        time.sleep(5)
        added_notes = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='customerNoteDetails mt-2']")
            )
        )
        print("Input Added Notes", added_notes.text)
        noteaccordions.click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Upload File']")
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
        wait_and_locate_click(login, By.XPATH, "//label[contains(text(),'Files selected')]")
        print("Uploaded File Successfully")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Confirm']")
        try:
            snack_bar = WebDriverWait(login, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
            )
            print("Snackbar Message :", snack_bar.text)
        except TimeoutException:
            try:
                snackbarerror = WebDriverWait(login, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
                )
                print("Snackbar Message : ", snackbarerror.text)
                cancelbutton = WebDriverWait(login, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[normalize-space()='Cancel']")
                    )
                )
                cancelbutton.click()
            except TimeoutException:
                cancelbutton = WebDriverWait(login, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[normalize-space()='Cancel']")
                    )
                )
                cancelbutton.click()
                print("Cancelled Successfully")
            time.sleep(1)
        while True:
            try:
                print("Before in the loop")
                time.sleep(3)
                wait_and_locate_click(login, By.XPATH, "//angledoublerighticon[@class='p-element p-icon-wrapper "
                            "ng-star-inserted']")
            except:
                print("EC Caught:Next button not found or clicked.")
                break
        wait_and_locate_click(login, By.XPATH,  "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]")
        time.sleep(5)
        print("Accordion expanded")
        wait_and_locate_click(login, By.XPATH,  "//button[normalize-space()='View Details']")
        time.sleep(5)
        print("ViewDetails Button Clicked")
        #**********Reschedule token to the Next day***********#
        wait_and_click(login, By.XPATH, "//button[normalize-space()='Reschedule']")
        time.sleep(3)
        wait_and_click(login, By.XPATH, "//div[@class='reschedule-date-picker']")
        time.sleep(3)
        today = datetime.now().date()
        tomorrow = today + timedelta(days=1)
        xpath_tomorrow = "//span[contains(text(),{})]".format(tomorrow.day)
        tomorrow_date = wait_and_locate_click(login, By.XPATH, xpath_tomorrow)
        print("Tomorrow Date:", tomorrow_date.text)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[@class='btn btn-primary reschedule-btn']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
        time.sleep(3)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  






    
