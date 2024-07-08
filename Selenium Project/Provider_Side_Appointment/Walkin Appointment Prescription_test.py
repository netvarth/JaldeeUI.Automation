from Framework.common_utils import *
import allure
from allure_commons.types import AttachmentType
import os



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Prescription Sharing")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_Prescription(login):
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
        # File pat
        file_path = r"C:\Users\Archana\PycharmProjects\JaldeeUI.Automation\Selenium Project\Data\number.txt"
        
        # Open the file in 'w' mode (create the file if it doesn't exist, overwrite it if it does)
        print("value to be written to file", phonenumber)
        with open(file_path, 'w') as file:
            # Write the value to the file
            file.write(phonenumber)
        print("value written to file", phonenumber)
        print("value written to file", phonenumber)
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

        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        element = login.find_element(By.XPATH, service_dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        service_option_xpath = ("(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
                                "Consultation'])[2]")
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

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Notes')]"))
        ).click()

        login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("Note for the walkin appointment")

        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
        ).click()
        print("Note added for walkin appointment")

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
        print("Successfully upload the file")

        time.sleep(6)
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

        time.sleep(2)
        WebDriverWait(login,10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Prescriptions']"))
        ).click()

        for i in range(5):
            login.find_element(By.XPATH, "//div[@class='add']").click()
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




        dropdown_locator_xpath = "/html[1]/body[1]/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-provider-appointment-detail[1]/div[1]/div[1]/div[1]/div[1]/app-booking-details[1]/div[2]/app-customer-record[1]/div[1]/div[2]/div[1]/app-prescriptions[1]/div[1]/div[1]/div[2]/div[1]/app-create[1]/div[1]/div[3]/div[1]/span[1]/mat-select[1]"
        dropdown_element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, dropdown_locator_xpath)))

    # Click on the dropdown to open options
        dropdown_element.click()

    # Wait for the option to be clickable
        option_locator_xpath = "//div[normalize-space()='Naveen KP']"
        option_element = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, option_locator_xpath)))

    # Click on the desired option
        option_element.click()

        login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(5)
        print("prescription created successfully")

        login.find_element(By.XPATH, "//img[@alt='share']").click()
        
        time.sleep(2)
        login.find_element(By.XPATH, "//textarea[@placeholder='Enter message description']").send_keys(
            "prescription message")

        login.find_element(By.XPATH, "//span[normalize-space()='Whatsapp']").click()
        login.find_element(By.XPATH, "//button[@type='button'][normalize-space()='Share']").click()
        print("Prescription Shared Successfully")

        time.sleep(3)
    except Exception as e:
        allure.attach(      # use Allure package, .attach() method, pass 3 params
        login.get_screenshot_as_png(),    # param1
        # login.screenshot()
        name="full_page",                 # param2
        attachment_type=AttachmentType.PNG)
        raise e
    

####################################################### uplaod prescription #####################################################

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Prescription upload Sharing")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_Prescription_1(login):
    
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
        # # File path
        # file_path = r"C:\Users\Archana\PycharmProjects\JaldeeUI.Automation\Selenium Project\Data\number.txt""
        
        # # Open the file in 'w' mode (create the file if it doesn't exist, overwrite it if it does)
        # print("value to be written to file", phonenumber)
        # with open(file_path, 'w') as file:
        #     # Write the value to the file
        #     file.write(phonenumber)
        # print("value written to file", phonenumber)
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

        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        element = login.find_element(By.XPATH, service_dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        service_option_xpath = ("(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
                                "Consultation'])[2]")
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

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Notes')]"))
        ).click()

        login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("Note for the walkin appointment")

        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
        ).click()
        print("Note added for walkin appointment")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Upload File']"))
        ).click()

        time.sleep(4)
        
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))

        print("Absolute path:", absolute_path)
        pyautogui.write(absolute_path)
        pyautogui.press('enter')
        print("Successfully upload the file")

        time.sleep(6)
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

        time.sleep(2)
        WebDriverWait(login,10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Prescriptions']"))
        ).click()   

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Upload Prescription']"))
        ).click()

        login.find_element(By.XPATH, "//a[normalize-space()='Upload']").click()

        time.sleep(2)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))
        pyautogui.write(absolute_path)
        pyautogui.press('enter')

        time.sleep(2)
        login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        dropdown_locator_xpath = "/html[1]/body[1]/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-provider-appointment-detail[1]/div[1]/div[1]/div[1]/div[1]/app-booking-details[1]/div[2]/app-customer-record[1]/div[1]/div[2]/div[1]/app-prescriptions[1]/div[1]/div[1]/div[2]/div[1]/app-create[1]/div[1]/div[3]/div[1]/span[1]/mat-select[1]"
        dropdown_element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, dropdown_locator_xpath)))

    # Click on the dropdown to open options
        dropdown_element.click()

    # Wait for the option to be clickable
        option_locator_xpath = "//div[normalize-space()='Naveen KP']"
        option_element = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, option_locator_xpath)))

    # Click on the desired option
        option_element.click()

        login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(5)
        print("prescription created successfully")

        login.find_element(By.XPATH, "//img[@alt='share']").click()
        
        time.sleep(2)
        login.find_element(By.XPATH, "//textarea[@placeholder='Enter message description']").send_keys(
            "prescription message")

        login.find_element(By.XPATH, "//span[normalize-space()='Whatsapp']").click()
        login.find_element(By.XPATH, "//button[@type='button'][normalize-space()='Share']").click()


        time.sleep(3)
    except Exception as e:
        allure.attach(      # use Allure package, .attach() method, pass 3 params
        login.get_screenshot_as_png(),    # param1
        # login.screenshot()
        name="full_page",                 # param2
        attachment_type=AttachmentType.PNG)
        raise e
    
     
############################################## Prescription Using Template #########################################      


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Prescription using Template")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_Prescription_2(login):

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
        # # File path
        # file_path = r"C:\Users\Archana\PycharmProjects\JaldeeUI.Automation\Selenium Project\Data\number.txt""
        
        # # Open the file in 'w' mode (create the file if it doesn't exist, overwrite it if it does)
        # print("value to be written to file", phonenumber)
        # with open(file_path, 'w') as file:
        #     # Write the value to the file
        #     file.write(phonenumber)
        # print("value written to file", phonenumber)
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

        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        element = login.find_element(By.XPATH, service_dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        service_option_xpath = ("(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
                                "Consultation'])[2]")
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

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Notes')]"))
        ).click()

        login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("Note for the walkin appointment")

        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
        ).click()
        print("Note added for walkin appointment")

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
        print("Successfully upload the file")

        time.sleep(6)
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

        time.sleep(2)
        WebDriverWait(login,10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Prescriptions']"))
        ).click() 

        login.find_element(By.XPATH, "//div[@class='temp ng-star-inserted']//div[1]//div[1]//div[2]//div[1]//button[1]").click()

        dropdown_locator_xpath = "/html[1]/body[1]/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-provider-appointment-detail[1]/div[1]/div[1]/div[1]/div[1]/app-booking-details[1]/div[2]/app-customer-record[1]/div[1]/div[2]/div[1]/app-prescriptions[1]/div[1]/div[1]/div[2]/div[1]/app-create[1]/div[1]/div[3]/div[1]/span[1]/mat-select[1]"
        dropdown_element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, dropdown_locator_xpath)))

    # Click on the dropdown to open options
        dropdown_element.click()

    # Wait for the option to be clickable
        option_locator_xpath = "//div[normalize-space()='Naveen KP']"
        option_element = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, option_locator_xpath)))

    # Click on the desired option
        option_element.click()

        login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(5)
        print("prescription created successfully")

        login.find_element(By.XPATH, "//img[@alt='share']").click()
        
        time.sleep(2)
        login.find_element(By.XPATH, "//textarea[@placeholder='Enter message description']").send_keys(
            "prescription message")

        login.find_element(By.XPATH, "//span[normalize-space()='Whatsapp']").click()
        login.find_element(By.XPATH, "//button[@type='button'][normalize-space()='Share']").click()


    except Exception as e:
        allure.attach(      # use Allure package, .attach() method, pass 3 params
        login.get_screenshot_as_png(),    # param1
        # login.screenshot()
        name="full_page",                 # param2
        attachment_type=AttachmentType.PNG)
        raise e 



#######################################









    






