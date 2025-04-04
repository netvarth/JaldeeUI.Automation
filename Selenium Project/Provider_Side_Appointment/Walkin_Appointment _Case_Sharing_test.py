from Framework.common_utils import *
import allure
from allure_commons.types import AttachmentType
import os

# first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Case Sharing")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_without_prescription(login):
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

        time.sleep(2)
        service_option_xpath = ("//li[@aria-label='Naveen Consultation']//div[1]")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
        print("Select Service : Naveen Consultation")
        time.sleep(3)
        Today_Date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
        Today_Date.click()
        print("Today Date:", Today_Date.text)
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
        login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
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

            # print("Appointment confirm successfully")

        time.sleep(4)

        while True:
                try:
                    next_button = WebDriverWait(login, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
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
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Patient Record')]"))
        ).click()

        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='+ Create Case']"))
            ).click()

        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Case Description']"))
            ).send_keys("test case for case")

        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
            ).click()

        toast_message = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
            )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder = 'Enter Chief Complaint']"))
        ).send_keys("Fever")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Save')]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='History']"))
        ).click()

        login.find_element(By.XPATH, "//input[@placeholder ='Enter History']").send_keys("viral fever")
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='viral fever']"))
        ).click()

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
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Medication']"))
        ).click()

        login.find_element(By.XPATH, "//input[@placeholder='Enter Medication'] ").send_keys("no medication")
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-list-item__primary-text'][normalize-space()='no medication']"))
        ).click()

        time.sleep(3)
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
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Vital Signs']"))
        ).click()

        login.find_element(By.XPATH, "//input[@placeholder='Enter Pulse Rate , Max : 999']").send_keys("560")
        login.find_element(By.XPATH, "//input[@placeholder='Enter Respiration , Max : 90']").send_keys("62")
        login.find_element(By.XPATH, "//input[@placeholder='Enter Temperature in °F , Max : 200']").send_keys("123")
        login.find_element(By.XPATH, "//input[@placeholder='Enter Systolic , Max : 500']").send_keys("264")
        login.find_element(By.XPATH, "//input[@placeholder='Enter Diastolic , Max : 500']").send_keys("287")

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
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Immunization History']"))
        # ).click()
        # login.find_element(By.XPATH, "//input[@placeholder='Enter Immunization History']").send_keys(
        #     "No History of Immunization History")
        # time.sleep(2)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH,
        #                                     "//span[@class='mdc-list-item__primary-text'][normalize-space()='no history of immunization history']"))
        # ).click()

        # element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        # login.execute_script("arguments[0].scrollIntoView();", element)
        # element.click()

        # login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        # toast_message = WebDriverWait(login, 10).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        # )
        # message = toast_message.text
        # print("Toast Message:", message)

        # time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Observations']"))
        ).click()

        observation_data = login.find_element(By.XPATH, "//input[@placeholder='Enter Observations']")
        observation_data.send_keys("Minor fever")
        observation_data.send_keys(Keys.ENTER)
        time.sleep(2)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Minor fever']"))
        # ).click()

        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        # login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Share']"))
        ).click()

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
        login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

        # time.sleep(3)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Upload File']"))
        # ).click()

        # time.sleep(4)
        # # Get the current working directory
        # current_working_directory = os.getcwd()

        # # Construct the absolute path
        # absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))
        # pyautogui.write(absolute_path)
        # pyautogui.press('enter')

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

            # print("Appointment confirm successfully")

        time.sleep(4)

        while True:
                try:
                    next_button = WebDriverWait(login, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
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
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Patient Record')]"))
        ).click()

        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='+ Create Case']"))
            ).click()

        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Case Description']"))
            ).send_keys("test case for case")

        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
            ).click()

        toast_message = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
            )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder = 'Enter Chief Complaint']"))
        ).send_keys("Fever")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Save')]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='History']"))
        ).click()

        login.find_element(By.XPATH, "//input[@placeholder ='Enter History']").send_keys("viral fever")
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='viral fever']"))
        ).click()

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
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Medication']"))
        ).click()

        login.find_element(By.XPATH, "//input[@placeholder='Enter Medication'] ").send_keys("no medication")
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-list-item__primary-text'][normalize-space()='no medication']"))
        ).click()

        time.sleep(3)
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
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Vital Signs']"))
        ).click()

        login.find_element(By.XPATH, "//input[@placeholder='Enter Pulse Rate , Max : 999']").send_keys("560")
        login.find_element(By.XPATH, "//input[@placeholder='Enter Respiration , Max : 90']").send_keys("62")
        login.find_element(By.XPATH, "//input[@placeholder='Enter Temperature in °F , Max : 200']").send_keys("123")
        login.find_element(By.XPATH, "//input[@placeholder='Enter Systolic , Max : 500']").send_keys("264")
        login.find_element(By.XPATH, "//input[@placeholder='Enter Diastolic , Max : 500']").send_keys("287")

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
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Immunization History']"))
        ).click()
        immu_history = login.find_element(By.XPATH, "//input[@placeholder='Enter Immunization History']")
        immu_history.send_keys("No History of Immunization History")
        immu_history.send_keys(Keys.ENTER)

        # time.sleep(2)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH,
        #                                     "//span[@class='mdc-list-item__primary-text'][normalize-space()='no history of immunization history']"))
        # ).click()

        time.sleep(2)
        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].click();", element)
        

        # login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Observations']"))
        ).click()
        time.sleep(2)
        observation_data = login.find_element(By.XPATH, "//input[@placeholder='Enter Observations']")
        observation_data.send_keys("Minor fever")
        observation_data.send_keys(Keys.ENTER)  
        
        
        time.sleep(3)
        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        # login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Diagnosis']"))
        ).click()

        login.find_element(By.XPATH, "//input[@placeholder='Enter Diagnosis']").send_keys("High temperature")
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='high temperature']"))
        ).click()
        
        time.sleep(2)
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
            (By.XPATH, "//button[normalize-space()='Prescription']"))
        ).click()

        for i in range(5):
                login.find_element(By.XPATH, "//button[normalize-space()='+ Add Medicine']").click()
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

        dropdown_locator_xpath = "//div[contains(@class, 'mat-mdc-select-arrow-wrapper ')]"
        dropdown_element = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, dropdown_locator_xpath)))

        dropdown_element.click()

        option_locator_xpath = "//div[normalize-space()='Naveen KP']"
        option_element = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, option_locator_xpath)))

        option_element.click()

        login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Share']"))
        ).click()

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
        time.sleep(3) 
        WebDriverWait(login, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]"))
        ).click()
        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]"))
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

        WebDriverWait(login, 10).until(
             EC.presence_of_element_located(
                  (By.XPATH, "//input[@placeholder='Enter name or phone or id']"))
        ).send_keys("5556211480")

        time.sleep(3)
        WebDriverWait(login, 10).until(
             EC.presence_of_element_located(
                  (By.XPATH, "//span[normalize-space()='Id : f6p']"))
        ).click()

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
        wait = WebDriverWait(login, 10)
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
        login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
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

            # print("Appointment confirm successfully")

        time.sleep(4)

        while True:
                try:
                    next_button = WebDriverWait(login, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
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
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Patient Record')]"))
        ).click()

        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='+ Create Case']"))
            ).click()

        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Case Description']"))
            ).send_keys("test case for case")

        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
            ).click()
        
    

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder = 'Enter Chief Complaint']"))
        ).send_keys("Fever")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Save')]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='History']"))
        ).click()

        login.find_element(By.XPATH, "//input[@placeholder ='Enter History']").send_keys("viral fever")
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='viral fever']"))
        ).click()

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
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Medication']"))
        ).click()

        login.find_element(By.XPATH, "//input[@placeholder='Enter Medication'] ").send_keys("no medication")
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-list-item__primary-text'][normalize-space()='no medication']"))
        ).click()

        time.sleep(3)
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
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Vital Signs']"))
        ).click()

        login.find_element(By.XPATH, "//input[@placeholder='Enter Pulse Rate , Max : 999']").send_keys("560")
        login.find_element(By.XPATH, "//input[@placeholder='Enter Respiration , Max : 90']").send_keys("62")
        login.find_element(By.XPATH, "//input[@placeholder='Enter Temperature in °F , Max : 200']").send_keys("123")
        login.find_element(By.XPATH, "//input[@placeholder='Enter Systolic , Max : 500']").send_keys("264")
        login.find_element(By.XPATH, "//input[@placeholder='Enter Diastolic , Max : 500']").send_keys("287")

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
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Immunization History']"))
        ).click()
        login.find_element(By.XPATH, "//input[@placeholder='Enter Immunization History']").send_keys(
            "No History of Immunization History")
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//span[@class='mdc-list-item__primary-text'][normalize-space()='no history of immunization history']"))
        ).click()

        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        # login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Observations']"))
        ).click()

        login.find_element(By.XPATH, "//input[@placeholder='Enter Observations']").send_keys("Minor fever")
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='minor fever']"))
        ).click()

        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        # login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Diagnosis']"))
        ).click()

        login.find_element(By.XPATH, "//input[@placeholder='Enter Diagnosis']").send_keys("High temperature")
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='high temperature']"))
        ).click()

        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        # login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Share']"))
        ).click()

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
@allure.title("Treatment plan in case Sharing")    
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
        login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
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

            # print("Appointment confirm successfully")

        time.sleep(4)

        while True:
                try:
                    next_button = WebDriverWait(login, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
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
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Patient Record')]"))
        ).click()

        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='+ Create Case']"))
            ).click()

        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Case Description']"))
            ).send_keys("test case for case")

        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
            ).click()

        toast_message = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
            )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder = 'Enter Chief Complaint']"))
        ).send_keys("Fever")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Save')]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='History']"))
        ).click()

        login.find_element(By.XPATH, "//input[@placeholder ='Enter History']").send_keys("viral fever")
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='viral fever']"))
        ).click()

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
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Medication']"))
        ).click()

        login.find_element(By.XPATH, "//input[@placeholder='Enter Medication'] ").send_keys("no medication")
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-list-item__primary-text'][normalize-space()='no medication']"))
        ).click()

        time.sleep(3)
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
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Vital Signs']"))
        ).click()

        login.find_element(By.XPATH, "//input[@placeholder='Enter Pulse Rate , Max : 999']").send_keys("560")
        login.find_element(By.XPATH, "//input[@placeholder='Enter Respiration , Max : 90']").send_keys("62")
        login.find_element(By.XPATH, "//input[@placeholder='Enter Temperature in °F , Max : 200']").send_keys("123")
        login.find_element(By.XPATH, "//input[@placeholder='Enter Systolic , Max : 500']").send_keys("264")
        login.find_element(By.XPATH, "//input[@placeholder='Enter Diastolic , Max : 500']").send_keys("287")

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
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Immunization History']"))
        ).click()
        login.find_element(By.XPATH, "//input[@placeholder='Enter Immunization History']").send_keys(
            "No History of Immunization History")
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//span[@class='mdc-list-item__primary-text'][normalize-space()='no history of immunization history']"))
        ).click()

        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        # login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Observations']"))
        ).click()

        login.find_element(By.XPATH, "//input[@placeholder='Enter Observations']").send_keys("Minor fever")
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='minor fever']"))
        ).click()

        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        # login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Diagnosis']"))
        ).click()

        login.find_element(By.XPATH, "//input[@placeholder='Enter Diagnosis']").send_keys("High temperature")
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='high temperature']"))
        ).click()

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

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Share']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Enter message description']"))
        ).send_keys("case sharing testing")

        login.find_element(By.XPATH, "//span[contains(text(),'Email')]").click()
        # login.find_element(By.XPATH, "//span[contains(text(),'Whatsapp')]").click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Share')]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        # print("Case file Shared successfully")

    except Exception as e:
        allure.attach(      # use Allure package, .attach() method, pass 3 params
        login.get_screenshot_as_png(),    # param1
        # login.screenshot()
        name="full_page",                 # param2
        attachment_type=AttachmentType.PNG)
        raise e







    