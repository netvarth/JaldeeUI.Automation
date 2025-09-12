# from xml.etree.ElementPath import xpath_tokenizer
from Framework.common_utils import *
import allure
from allure_commons.types import AttachmentType
import os


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Prescription Sharing")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_Prescription(login):
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
        time.sleep(3)
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//b[contains(text(),'Create New Patient')]")
            )
        )
        element_appoint.click() 
        login.implicitly_wait(3)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        # # File pat
        # file_path = r"F:\UI Automation\JaldeeUI.Automation\Selenium Project\Data"

        # # Open the file in 'w' mode (create the file if it doesn't exist, overwrite it if it does)
        # print("value to be written to file", phonenumber)
        # with open(file_path, "w") as file:
        #     # Write the value to the file
        #     file.write(phonenumber)
        # print("value written to file", phonenumber)
        # print("value written to file", phonenumber)
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
        login.implicitly_wait(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "p-dropdown[optionlabel='place']")
            )
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

        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        element = login.find_element(By.XPATH, service_dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        service_option_xpath = ("//li[@aria-label='Naveen Consultation']//div[1]")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, service_option_xpath))
        ).click()
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
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        print("Successfully upload the file")

        time.sleep(6)
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

        time.sleep(4)

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
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Prescriptions']")
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

        dropdown_locator_xpath = "/html[1]/body[1]/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-provider-appointment-detail[1]/div[1]/div[1]/div[1]/div[1]/app-booking-details[1]/div[2]/app-customer-record[1]/div[1]/div[2]/div[1]/app-prescriptions[1]/div[1]/div[1]/div[2]/div[1]/app-create[1]/div[1]/div[3]/div[1]/span[1]/mat-select[1]"
        dropdown_element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, dropdown_locator_xpath))
        )

        # Click on the dropdown to open options
        dropdown_element.click()

        # Wait for the option to be clickable
        option_locator_xpath = "//div[normalize-space()='Naveen KP']"
        option_element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_locator_xpath))
        )

        # Click on the desired option
        option_element.click()

        login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(5)
        print("prescription created successfully")

        login.find_element(By.XPATH, "//img[@alt='share']").click()

        time.sleep(2)
        login.find_element(
            By.XPATH, "//textarea[@placeholder='Enter message description']"
        ).send_keys("prescription message")

        login.find_element(By.XPATH, "//span[normalize-space()='Whatsapp']").click()
        login.find_element(
            By.XPATH, "//button[@type='button'][normalize-space()='Share']"
        ).click()

        toast_detail = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_detail.text
        print("toast_Message:", message)
        # print("Prescription Shared Successfully")

        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Download')]")
            )
        ).click()

        toast_detail = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_detail.text
        print("toast_Message:", message)

        time.sleep(3)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Prescription upload Sharing")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_Prescription_1(login):

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
        login.execute_script("arguments[0].click();", element)
        time.sleep(3)
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//b[contains(text(),'Create New Patient')]")
            )
        )
        element_appoint.click()
        login.implicitly_wait(3)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        # # File path
        # file_path = r"C:\Users\Archana\PycharmProjects\JaldeeUI.Automation\Selenium Project\Data\number.txt""

        # # Open the file in 'w' mode (create the file if it doesn't exist, overwrite it if it does)
        # print("value to be written to file", phonenumber)
        # with open(file_path, 'w') as file:
        #     # Write the value to the file
        #     file.write(phonenumber)
        # print("value written to file", phonenumber)
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
        login.implicitly_wait(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "p-dropdown[optionlabel='place']")
            )
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

        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        element = login.find_element(By.XPATH, service_dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        service_option_xpath = ("//li[@aria-label='Naveen Consultation']//div[1]")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, service_option_xpath))
        ).click()
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

        print("Absolute path:", absolute_path)
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        print("Successfully upload the file")

        time.sleep(6)
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

        time.sleep(4)

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

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Prescriptions']")
            )
        ).click()

        time.sleep(3)
        dropdown_element= WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//mat-select[@aria-haspopup='listbox']"))
        )
        dropdown_element.click()
        
        time.sleep(3)
        element3 = login.find_element(By.XPATH, "//span[@class='mdc-list-item__primary-text']//div[contains(text(),'Naveen KP')]")
        login.execute_script("arguments[0].click();", element3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Upload Prescription']")
            )
        ).click()

        time.sleep(2)
        login.find_element(By.XPATH, "//a[normalize-space()='Upload']").click()

        time.sleep(2)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(2)
        login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
  
        time.sleep(5)
        print("prescription created successfully")
        
        time.sleep(2)
        login.find_element(By.XPATH, "(//img[@alt='share'])[1]").click()

        time.sleep(2)
        login.find_element(
            By.XPATH, "//textarea[@placeholder='Enter message description']"
        ).send_keys("prescription message")

        login.find_element(By.XPATH, "//span[normalize-space()='Whatsapp']").click()
        login.find_element(
            By.XPATH, "//button[@type='button'][normalize-space()='Share']"
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


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Prescription using Template")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_Prescription_2(login):

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
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//span[normalize-space(.)='Appointment']",
                )
            )
        )
        element.click()
        time.sleep(3)
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//b[contains(text(),'Create New Patient')]")
            )
        )
        element_appoint.click()
        login.implicitly_wait(3)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        # # File path
        # file_path = r"C:\Users\Archana\PycharmProjects\JaldeeUI.Automation\Selenium Project\Data\number.txt""

        # # Open the file in 'w' mode (create the file if it doesn't exist, overwrite it if it does)
        # print("value to be written to file", phonenumber)
        # with open(file_path, 'w') as file:
        #     # Write the value to the file
        #     file.write(phonenumber)
        # print("value written to file", phonenumber)
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
        login.implicitly_wait(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "p-dropdown[optionlabel='place']")
            )
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

        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        element = login.find_element(By.XPATH, service_dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        service_option_xpath = ("//li[@aria-label='Naveen Consultation']//div[1]")


        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, service_option_xpath))
        ).click()
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
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        print("Successfully upload the file")

        time.sleep(6)
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

        time.sleep(4)

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

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Prescriptions']")
            )
        ).click()

        login.find_element(
            By.XPATH,
            "//div[@class='temp ng-star-inserted']//div[1]//div[1]//div[2]//div[1]//button[1]",
        ).click()

        dropdown_element= WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//mat-select[@aria-haspopup='listbox']"))
        )
        dropdown_element.click()
        
        time.sleep(3)
        element3 = login.find_element(By.XPATH, "//span[@class='mdc-list-item__primary-text']//div[contains(text(),'Naveen KP')]")
        login.execute_script("arguments[0].click();", element3)

        time.sleep(3)

        login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(5)
        print("prescription created successfully")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Print']")
            )
        ).click()

        time.sleep(2)
        # Wait until the shadow host element is present
        shadow_host = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#shadow-host"))
        )

        # Execute JavaScript to access the shadow root
        shadow_root = login.execute_script(
            "return arguments[0].shadowRoot", shadow_host
        )

        # Locate the button inside the shadow root
        print_button = shadow_root.find_element(
            By.CSS_SELECTOR, "cr-button.action-button"
        )

        # Click the button
        print_button.click()

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

        # login.find_element(By.XPATH, "//img[@alt='share']").click()

        # time.sleep(2)
        # login.find_element(By.XPATH, "//textarea[@placeholder='Enter message description']").send_keys(
        #     "prescription message")

        # login.find_element(By.XPATH, "//span[normalize-space()='Email']").click()
        # login.find_element(By.XPATH, "//div[@class='coupon-outer']").click()

        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='Share']"))
        # ).click()

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RX Push Complete Order")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_Prescription_3(login):

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
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Appointment']",)
            )
        )
        element.click()
        time.sleep(3)
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//b[contains(text(),'Create New Patient')]")
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

        # time.sleep(2)
        # toast_message = WebDriverWait(login, 10).until(
        # EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        # )
        # message = toast_message.text
        # print("Toast Message:", message)

        time.sleep(3)


        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        wait = WebDriverWait(login, 10)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='ENT']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Naveen KP']"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm']"))
        ).click()

        time.sleep(5)
        # scroll = wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[@class='p-paginator-current ng-star-inserted']"))
        # )
        # login.execute_script("arguments[0].scrollIntoView();", scroll)

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
        login.execute_script("arguments[0].click();", View_Detail_button)
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Prescriptions']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        select_doc = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Naveen KP']"))
        )

        login.execute_script("arguments[0].scrollIntoView();", select_doc)

        select_doc.click()

        # Loop through rows and interact with each row
        # # Loop through rows and interact with each row
        # for index in range(3):  # Assuming you're iterating through 2 rows
        #     # Click the "+ Add Medicine" button
        #     wait.until(
        #         EC.presence_of_element_located(
        #             (By.XPATH, "//button[normalize-space()='+ Add Medicine']")
        #         )
        #     ).click()

        #     # Find the search box and clear it
        #     search_box = login.find_element(By.CSS_SELECTOR, "input[role='searchbox']")
        #     search_box.clear()

        #     # Type 'item' into the search box (you can replace with dynamic name)
        #     search_box.send_keys('item')
        #     time.sleep(1)  # Wait for suggestions to load

        #     # Get the list of suggestions
        #     suggestions = login.find_elements(By.CSS_SELECTOR, ".p-autocomplete-item")

        #     # Select a suggestion based on the index or randomly
        #     if suggestions:
        #         suggestions[index].click()
        #         time.sleep(1)

        #         # Locate the current row
        #         row = wait.until(
        #             EC.presence_of_element_located((By.XPATH, f"//tbody/tr[{index + 1}]"))
        #         )

        #         # Enter Duration
        #         duration = row.find_element(By.XPATH, ".//td[3]/input[@type='number']")
        #         duration.clear()
        #         duration.send_keys("5")

        #         # ✅ Updated Frequency Dropdown Selection
        #         dropdown_trigger = row.find_element(
        #             By.XPATH, ".//td[4]//div[contains(@class, 'p-dropdown-trigger')]"
        #         )
        #         dropdown_trigger.click()

        #         dropdown_options = WebDriverWait(login, 10).until(
        #             EC.presence_of_all_elements_located(
        #                 (By.XPATH, "//div[contains(@class,'p-dropdown-items-wrapper')]//li")
        #             )
        #         )

        #         if dropdown_options:
        #             option_to_click = random.choice(dropdown_options)
        #             login.execute_script("arguments[0].scrollIntoView(true);", option_to_click)
        #             time.sleep(0.5)
        #             login.execute_script("arguments[0].click();", option_to_click)
        #         # Qty
        #         qty_input = row.find_element(By.XPATH, ".//td[5]/input[@type='number']")
        #         qty_input.clear()
        #         qty_input.send_keys("1")

        #         # Remarks (Notes / Instructions)
        #         row.find_element(By.XPATH, ".//td[6]").click()
        #         remarks = row.find_element(By.XPATH, "//input[@role='searchbox']")
        #         remarks.clear()
        #         remarks.send_keys("After food")

        #         time.sleep(1)  # Pause before moving to the next row


        # # Finally, submit the prescription by clicking the "Create Prescription" button
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='Create Prescription']")
        #     )
        # ).click()

        # Medicines: first is manual, rest are normal
        medicines_to_add = [
            {"name": "Paracetamol", "manual": True},  # manual entry
            {"name": "items", "manual": False},
            {"name": "Item4", "manual": False}
        ]
        for index, med in enumerate(medicines_to_add):
            # Click the "+ Add Medicine" button
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[normalize-space()='+ Add Medicine']")
                )
            ).click()

            # Find the search box
            search_box = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[role='searchbox']"))
            )
            search_box.clear()
            search_box.send_keys(med["name"])
            time.sleep(1)

            if not med["manual"]:
                # Normal item → pick from autocomplete
                suggestions = login.find_elements(By.CSS_SELECTOR, ".p-autocomplete-item")
                if suggestions:
                    suggestions[0].click()
            else:
                # Manual (ADOCH) item → confirm typed entry
                search_box.send_keys(Keys.ENTER)

            time.sleep(1)

            # Locate the current row
            row = wait.until(
                EC.presence_of_element_located((By.XPATH, f"//tbody/tr[{index + 1}]"))
            )

            # Duration
            duration = row.find_element(By.XPATH, ".//td[3]/input[@type='number']")
            duration.clear()
            duration.send_keys("5")

            # Frequency dropdown
            dropdown_trigger = row.find_element(
                By.XPATH, ".//td[4]//div[contains(@class, 'p-dropdown-trigger')]"
            )
            dropdown_trigger.click()

            dropdown_options = WebDriverWait(login, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//div[contains(@class,'p-dropdown-items-wrapper')]//li")
                )
            )
            if dropdown_options:
                option_to_click = random.choice(dropdown_options)
                login.execute_script("arguments[0].scrollIntoView(true);", option_to_click)
                time.sleep(0.5)
                login.execute_script("arguments[0].click();", option_to_click)

            # Qty
            qty_input = row.find_element(By.XPATH, ".//td[5]/input[@type='number']")
            qty_input.clear()
            qty_input.send_keys("1")

            # Remarks
            row.find_element(By.XPATH, ".//td[6]").click()
            remarks = row.find_element(By.XPATH, "//input[@role='searchbox']")
            remarks.clear()
            remarks.send_keys(f"Notes for {med['name']}")

            time.sleep(1)

        # Finally submit
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Create Prescription']")
            )
        ).click()

        time.sleep(3)  # Wait for the prescription to be processed
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Push RX']"))
        ).click()

        store = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='Geetha']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", store)
        store.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Push']"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[5]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-pristine ng-valid']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']"))
        ).click()

        stores = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Geetha']"))
        )

        login.execute_script("arguments[0].scrollIntoView();", stores)
        stores.click()

        time.sleep(2)
        
        RX_request_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Rx Requests']"))
        )

        scroll_to_element(login, RX_request_element) 
        time.sleep(1)
        RX_request_element.click()

        time.sleep(2)
        # Wait for the table to be present
        table_body = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody"))
        )

        # Locate the first table row
        first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")
                                                                    
        # Find the status element within the first row
        status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
        status_text = status_element.text
        expected_status = "Pushed"

        print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

        # Assert that the status is "Pushed"
        assert status_text == "Pushed", f"Expected status to be 'Pushed', but got '{status_text}'"

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//tbody/tr[1]/td[7]/div[1]/div[1]/button[1]/span[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm Order']"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        # Assertion to check if the order status is "Confirmed"
        time.sleep(3)
        
        # Locate the status element within the page (update XPATH as per actual structure)
        status_complete = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )

        # Extract the text to validate it shows "Confirmed"
        status_text = status_complete.text
        expected_status = "Confirmed"

        print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

        # Assert that the status is "Confirmed"
        assert status_text == expected_status, f"Expected status to be '{expected_status}', but got '{status_text}'"

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Create Invoice']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Complete Order']"))
        ).click()
        

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='View Invoice']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-button__label']"))
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
                (By.XPATH, "//i[@class='pi pi-arrow-left']"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Complete Order']"))  
        ).click()

        toast_detail = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_detail.text
        print("toast_Message:", message)
        
        
        # Assertion to check if the order status is "Completed"
        time.sleep(3)
        
        # Locate the status element within the page (update XPATH as per actual structure)
        status_complete = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )

        # Extract the text to validate it shows "Completed"
        status_text = status_complete.text
        expected_status = "Completed"

        print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

        # Assert that the status is "Completed"
        assert status_text == expected_status, f"Expected status to be '{expected_status}', but got '{status_text}'"


        time.sleep(5)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="Error_Screenshot",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RX Push Decline Order")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_Prescription_4(login):

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
                    "//span[normalize-space()='Appointment']",
                )
            )
        )
        element.click()
        time.sleep(3)
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//b[contains(text(),'Create New Patient')]")
            )
        )
        element_appoint.click()
        login.implicitly_wait(3)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        time.sleep(3)
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

        # time.sleep(2)
        # toast_message = WebDriverWait(login, 10).until(
        # EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        # )
        # message = toast_message.text
        # print("Toast Message:", message)

        time.sleep(3)


        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        wait = WebDriverWait(login, 10)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='ENT']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Naveen KP']"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm']"))
        ).click()

        time.sleep(5)
        scroll = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='p-paginator-current ng-star-inserted']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", scroll)

        
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
        View_Detail_button.click()
        login.execute_script("arguments[0].click();", View_Detail_button)
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Prescriptions']"))
        ).click()


        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        select_doc = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Naveen KP']"))
        )

        login.execute_script("arguments[0].scrollIntoView();", select_doc)

        select_doc.click()

        # Loop through rows and interact with each row
        for index in range(2):  # Assuming you're iterating through 3 rows
            # Click the "+ Add Medicine" button
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[normalize-space()='+ Add Medicine']")
                )
            ).click()

            # Find the search box and clear it
            search_box = login.find_element(By.CSS_SELECTOR, "input[role='searchbox']")
            search_box.clear()

            # Type 'item' into the search box (you might want to replace 'item' with actual item names if needed)
            search_box.send_keys('item')
            time.sleep(1)  # Wait for suggestions to load

            # Get the list of suggestions
            suggestions = login.find_elements(By.CSS_SELECTOR, ".p-autocomplete-item")

            # Select a suggestion based on the index or randomly
            if suggestions:
                suggestions[index].click()  # Click the current suggestion
                time.sleep(1)  # Wait briefly before interacting with other fields

                # Locate the current row (each row is a tr element in tbody)
                row = wait.until(
                    EC.presence_of_element_located((By.XPATH, f"//tbody/tr[{index + 1}]"))  # Adjust this if needed
                )

                # Find the duration input field inside the current row and send the value
                duration = row.find_element(By.XPATH, ".//td[3]/input[@type='number']")  # Adjust if necessary
                duration.clear()
                duration.send_keys("5")  # Send the duration value

                time.sleep(1)  # Pause before interacting with the frequency dropdown

                # Find and select a random frequency from the dropdown in the current row
                frequency_dropdown_label = row.find_element(By.CSS_SELECTOR, ".p-dropdown-label")
                frequency_dropdown_label.click()  # Click to open the dropdown

                # Get the frequency options within the dropdown for this row
                frequency_options = login.find_elements(By.CSS_SELECTOR, ".p-dropdown-item")  # Adjust if necessary
                if frequency_options:
                    random_frequency = random.choice(frequency_options)
                    random_frequency.click()  # Select the random frequency

                time.sleep(1)  # Pause before interacting with the quantity field

                # Optionally, send remarks (e.g., "After food")
                row.find_element(By.XPATH, ".//td[6]").click()
                remarks = row.find_element(By.XPATH, ".//textarea")  # Adjust if necessary
                remarks.clear()
                remarks.send_keys("After food")

            time.sleep(1)  # Pause before moving to the next row

        # Finally, submit the prescription by clicking the "Create Prescription" button
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Create Prescription']")
            )
        ).click()

        time.sleep(3)  # Wait for the prescription to be processed
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Push RX']"))
        ).click()

        store = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='Geetha']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", store)
        store.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Push']"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[5]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        stores = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Geetha']"))
        )

        login.execute_script("arguments[0].scrollIntoView();", stores)
        stores.click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Rx Requests']"))
        ).click()

        # Wait for the table to be present
        table_body = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody"))
        )

        # Locate the first table row
        first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")
                                                                    
        # Find the status element within the first row
        status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
        status_text = status_element.text
        expected_status = "PUSHED"

        print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

        # Assert that the status is "PUSHED"
        assert status_text == "PUSHED", f"Expected status to be 'PUSHED', but got '{status_text}'"

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//tbody/tr[1]/td[7]/div[1]/div[1]/button[1]/span[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Decline Order']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Yes']"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        # Wait for the table to be present
        table_body = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody"))
        )

        # Locate the first table row
        first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")
                                                                    
        # Find the status element within the first row
        status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
        status_text = status_element.text
        expected_status = "DECLINED"

        print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

        # Assert that the status is "DECLINED"
        assert status_text == "DECLINED", f"Expected status to be 'DECLINED', but got '{status_text}'"

        

        time.sleep(5)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="Error_Screenshot",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RX Push Draft Order")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_Prescription_5(login):

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
                    "//span[normalize-space()='Appointment']",
                )
            )
        )
        element.click()
        time.sleep(3)
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//b[contains(text(),'Create New Patient')]")
            )
        )
        element_appoint.click()
        login.implicitly_wait(3)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        time.sleep(3)
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

        # time.sleep(2)
        # toast_message = WebDriverWait(login, 10).until(
        # EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        # )
        # message = toast_message.text
        # print("Toast Message:", message)

        time.sleep(3)


        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        wait = WebDriverWait(login, 10)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='ENT']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Naveen KP']"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm']"))
        ).click()

        time.sleep(5)
        scroll = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='p-paginator-current ng-star-inserted']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", scroll)

        
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
        View_Detail_button.click()
        login.execute_script("arguments[0].click();", View_Detail_button)
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Prescriptions']"))
        ).click()


        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        select_doc = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Naveen KP']"))
        )

        login.execute_script("arguments[0].scrollIntoView();", select_doc)

        select_doc.click()

        # Loop through rows and interact with each row
        for index in range(2):  # Assuming you're iterating through 3 rows
            # Click the "+ Add Medicine" button
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[normalize-space()='+ Add Medicine']")
                )
            ).click()

            # Find the search box and clear it
            search_box = login.find_element(By.CSS_SELECTOR, "input[role='searchbox']")
            search_box.clear()

            # Type 'item' into the search box (you might want to replace 'item' with actual item names if needed)
            search_box.send_keys('item')
            time.sleep(1)  # Wait for suggestions to load

            # Get the list of suggestions
            suggestions = login.find_elements(By.CSS_SELECTOR, ".p-autocomplete-item")

            # Select a suggestion based on the index or randomly
            if suggestions:
                suggestions[index].click()  # Click the current suggestion
                time.sleep(1)  # Wait briefly before interacting with other fields

                # Locate the current row (each row is a tr element in tbody)
                row = wait.until(
                    EC.presence_of_element_located((By.XPATH, f"//tbody/tr[{index + 1}]"))  # Adjust this if needed
                )

                # Find the duration input field inside the current row and send the value
                duration = row.find_element(By.XPATH, ".//td[3]/input[@type='number']")  # Adjust if necessary
                duration.clear()
                duration.send_keys("5")  # Send the duration value

                time.sleep(1)  # Pause before interacting with the frequency dropdown

                # Find and select a random frequency from the dropdown in the current row
                frequency_dropdown_label = row.find_element(By.CSS_SELECTOR, ".p-dropdown-label")
                frequency_dropdown_label.click()  # Click to open the dropdown

                # Get the frequency options within the dropdown for this row
                frequency_options = login.find_elements(By.CSS_SELECTOR, ".p-dropdown-item")  # Adjust if necessary
                if frequency_options:
                    random_frequency = random.choice(frequency_options)
                    random_frequency.click()  # Select the random frequency

                time.sleep(1)  # Pause before interacting with the quantity field

                # Optionally, send remarks (e.g., "After food")
                row.find_element(By.XPATH, ".//td[6]").click()
                remarks = row.find_element(By.XPATH, ".//textarea")  # Adjust if necessary
                remarks.clear()
                remarks.send_keys("After food")

            time.sleep(1)  # Pause before moving to the next row

        # Finally, submit the prescription by clicking the "Create Prescription" button
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Create Prescription']")
            )
        ).click()

        time.sleep(3)  # Wait for the prescription to be processed
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Push RX']"))
        ).click()

        store = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='Geetha']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", store)
        store.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Push']"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[4]//a[1]//div[1]//span[1]//span[1]//img[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        stores = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Geetha']"))
        )

        login.execute_script("arguments[0].scrollIntoView();", stores)
        stores.click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Rx Requests']"))
        ).click()

        # Wait for the table to be present
        table_body = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody"))
        )

        # Locate the first table row
        first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")
                                                                    
        # Find the status element within the first row
        status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
        status_text = status_element.text
        expected_status = "PUSHED"

        print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

        # Assert that the status is "PUSHED"
        assert status_text == "PUSHED", f"Expected status to be 'PUSHED', but got '{status_text}'"

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//tbody/tr[1]/td[7]/div[1]/div[1]/button[1]/span[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Draft Order']"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        # Wait for the table to be present
        table_body = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody"))
        )

        # Locate the first table row
        first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")
                                                                    
        # Find the status element within the first row
        status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
        status_text = status_element.text
        expected_status = "Draft"

        print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

        # Assert that the status is "Draft"
        assert status_text == "Draft", f"Expected status to be 'Draft', but got '{status_text}'"

        

        time.sleep(5)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="Error_Screenshot",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e