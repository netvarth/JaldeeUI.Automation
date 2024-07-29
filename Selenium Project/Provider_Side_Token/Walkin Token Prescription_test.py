from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.common import TimeoutException , JavascriptException
from selenium.webdriver.support.ui import Select
from pywinauto import Desktop , Application # type: ignore


@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_patient_MR_Sharing(login, ):
    try:
        time.sleep(5)
        WebDriverWait(login,20).until(
            EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'customers.gif')]//following::div[contains(text(),'Patients')]")
        )
        ).click()
        time.sleep(3)
        patientsearch =WebDriverWait(login,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter name or phone or id']"))
        )
        patientsearch.send_keys('5553310348')
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 153']"))
        ).click()
        time.sleep(3)
        prescription = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Prescriptions']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", prescription)
        prescription.click()
        time.sleep(3)
        addmedicine = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='+ Add Medicine']"))
            )
        addmedicine.click()
        time.sleep(1)
        medicinename = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[@class= 'p-element medicine-name p-editable-column p-cell-editing']//input[@type='text']"))
            )
        medicinename.send_keys('p')
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'paracetamol')]"))
            ).click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[@class='p-element first-cell p-editable-column']"))
            ).click()
        time.sleep(1)
        dose = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][2]//input[@type='text']"))
            )
        dose.send_keys('650 mg')
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[3]"))
            ).click()
        time.sleep(1)
        frequency = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][3]//input[@type='text']"))
            )
        frequency.send_keys('Once daily')
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[4]"))
            ).click()
        time.sleep(1)
        duration = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][4]//input[@type='text']"))
            )
        duration.send_keys('2 weeks')
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[5]"))
            ).click()
        time.sleep(1)
        pre_notes = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][5]//input[@type='text']"))
            )
        pre_notes.send_keys('Take with food')
        time.sleep(3)
        Notesif_any = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']"))
            )
        Notesif_any.send_keys('Please schedule a follow-up consultation after two weeks if the condition does not improve.')
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
            ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Share']"))
            ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Enter message description']"))
            ).send_keys('Sharing Prescription')
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Email']"))
            ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Whatsapp']"))
            ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='button'][normalize-space()='Share']"))
            ).click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        time.sleep(3)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e  
       
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_patient_MR_Sharing_Others(login):
    try:
        time.sleep(5)
        WebDriverWait(login,20).until(
            EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'customers.gif')]//following::div[contains(text(),'Patients')]")
        )
        ).click()
        time.sleep(3)
        patientsearch =WebDriverWait(login,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter name or phone or id']"))
        )
        patientsearch.send_keys('5553310348')
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 153']"))
        ).click()
        time.sleep(3)
        prescription = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Prescriptions']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", prescription)
        prescription.click()
        time.sleep(3)
        addmedicine = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='+ Add Medicine']"))
            )
        addmedicine.click()
        time.sleep(1)
        medicinename = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[@class= 'p-element medicine-name p-editable-column p-cell-editing']//input[@type='text']"))
            )
        medicinename.send_keys('p')
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'paracetamol')]"))
            ).click()
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[@class='p-element first-cell p-editable-column']"))
            ).click()
        time.sleep(1)
        dose = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][2]//input[@type='text']"))
            )
        dose.send_keys('650 mg')
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[3]"))
            ).click()
        time.sleep(1)
        frequency = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][3]//input[@type='text']"))
            )
        frequency.send_keys('Once daily')
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[4]"))
            ).click()
        time.sleep(1)
        duration = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][4]//input[@type='text']"))
            )
        duration.send_keys('2 weeks')
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[5]"))
            ).click()
        time.sleep(1)
        pre_notes = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][5]//input[@type='text']"))
            )
        pre_notes.send_keys('Take with food')
        time.sleep(1)
        Notesif_any = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']"))
            )
        Notesif_any.send_keys('Please schedule a follow-up consultation after two weeks if the condition does not improve.')
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
            ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Share']"))
            ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//mat-select[@placeholder = 'Share with whom']"))
            ).click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Others']"))
            ).click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Enter message description']"))
            ).send_keys('Sharing Prescription')
        time.sleep(2)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Email']"))
            ).click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='thirdpartyemail']"))
            ).send_keys('priya.test@jaldee.com')
        time.sleep(2)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Whatsapp']"))
            ).click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='mobile_number']"))
            ).send_keys('5550001536')
        time.sleep(2)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='button'][normalize-space()='Share']"))
            ).click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        time.sleep(3)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    


@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_patient_Upload_MR_Sharing(login):
    try:
        time.sleep(5)
        WebDriverWait(login,20).until(
            EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'customers.gif')]//following::div[contains(text(),'Patients')]")
        )
        ).click()
        time.sleep(3)
        patientsearch =WebDriverWait(login,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter name or phone or id']"))
        )
        patientsearch.send_keys('5552826546')
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 155']"))
        ).click()
        time.sleep(3)
        prescription = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Prescriptions']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", prescription)
        prescription.click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Upload Prescription']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Upload']"))
        ).click()
        time.sleep(8)
        current_working_directory = os.getcwd()
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\prescription.pdf")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        time.sleep(3)
        
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
            ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Share']"))
            ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Enter message description']"))
            ).send_keys('Sharing Prescription')
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Email']"))
            ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Whatsapp']"))
            ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='button'][normalize-space()='Share']"))
            ).click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        time.sleep(3)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_patient_Upload_MR_Sharing_others(login):
    try:
        time.sleep(5)
        WebDriverWait(login,20).until(
            EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'customers.gif')]//following::div[contains(text(),'Patients')]")
        )
        ).click()
        time.sleep(3)
        patientsearch =WebDriverWait(login,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter name or phone or id']"))
        )
        patientsearch.send_keys('5552826546')
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 155']"))
        ).click()
        time.sleep(3)
        prescription = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Prescriptions']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", prescription)
        prescription.click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Upload Prescription']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Upload']"))
        ).click()
        time.sleep(8)
        current_working_directory = os.getcwd()
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\prescription.pdf")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
            ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Share']"))
            ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//mat-select[@placeholder = 'Share with whom']"))
            ).click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Others']"))
            ).click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Enter message description']"))
            ).send_keys('Sharing Prescription')
        time.sleep(2)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Email']"))
            ).click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='thirdpartyemail']"))
            ).send_keys('priya.test@jaldee.com')
        time.sleep(2)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Whatsapp']"))
            ).click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='mobile_number']"))
            ).send_keys('5550001536')
        time.sleep(2)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='button'][normalize-space()='Share']"))
            ).click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        time.sleep(3)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e


@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_patient_MR_Print(login):
    try:
        time.sleep(5)
        WebDriverWait(login,20).until(
            EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'customers.gif')]//following::div[contains(text(),'Patients')]")
        )
        ).click()
        time.sleep(3)
        patientsearch =WebDriverWait(login,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter name or phone or id']"))
        )
        patientsearch.send_keys('5558615251')
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 149']"))
        ).click()
        time.sleep(3)
        prescription = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Prescriptions']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", prescription)
        prescription.click()
        time.sleep(3)
        addmedicine = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='+ Add Medicine']"))
            )
        addmedicine.click()
        time.sleep(1)
        medicinename = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[@class= 'p-element medicine-name p-editable-column p-cell-editing']//input[@type='text']"))
            )
        medicinename.send_keys('p')
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'paracetamol')]"))
            ).click()
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[@class='p-element first-cell p-editable-column']"))
            ).click()
        time.sleep(1)
        dose = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][2]//input[@type='text']"))
            )
        dose.send_keys('650 mg')
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[3]"))
            ).click()
        time.sleep(1)
        frequency = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][3]//input[@type='text']"))
            )
        frequency.send_keys('Once daily')
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[4]"))
            ).click()
        time.sleep(1)
        duration = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][4]//input[@type='text']"))
            )
        duration.send_keys('2 weeks')
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[5]"))
            ).click()
        time.sleep(1)
        pre_notes = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][5]//input[@type='text']"))
            )
        pre_notes.send_keys('Take with food')
        time.sleep(1)
        Notesif_any = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']"))
            )
        Notesif_any.send_keys('Please schedule a follow-up consultation .')
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
            ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Print']"))
            ).click()
        time.sleep(3)
        login.switch_to.window(login.window_handles[-1])
        dropdown = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'print-preview-app'))
        )
        try:
            # JavaScript to find the dropdown element within nested shadow DOMs
            dropdown_script = """
                return document.querySelector('print-preview-app').shadowRoot
                    .querySelector('print-preview-sidebar').shadowRoot
                    .querySelector('print-preview-destination-settings').shadowRoot
                    .querySelector('print-preview-destination-select').shadowRoot
                    .querySelector('select.md-select');
                """

            # Executing the script to find the dropdown element
            dropdown = login.execute_script(dropdown_script)
            select = Select(dropdown)
            select.select_by_visible_text("Save as PDF")
            time.sleep(3)
            save_button_script = """
                return document.querySelector('print-preview-app').shadowRoot
                .querySelector('print-preview-sidebar').shadowRoot
                .querySelector('print-preview-button-strip').shadowRoot
                .querySelector('cr-button.action-button').click();
                """
            login.execute_script(save_button_script)
            time.sleep(3)
            pyautogui.click()
            # current_working_directory = os.getcwd()
            # print(f"Current working directory: {current_working_directory}")
            # download_dir  = os.path.abspath(
            #        os.path.join(current_working_directory, r'Extras')
            #   )
            # print(f"Download directory: {download_dir}")
            # pyautogui.typewrite(download_dir)
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(3)
            login.switch_to.window(login.window_handles[0])
        except JavascriptException as e:
            print('element not found')
    except Exception as e:
        allure.attach(  # use Allure package, .attach() met hod, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"]) 
def test_patient_MR_Template(login):
    try:
        time.sleep(5)
        WebDriverWait(login,20).until(
            EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'customers.gif')]//following::div[contains(text(),'Patients')]")
        )
        ).click()
        time.sleep(3)
        patientsearch =WebDriverWait(login,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter name or phone or id']"))
        )
        patientsearch.send_keys('5556328484')
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 151']"))
        ).click()
        time.sleep(3)
        prescription = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Prescriptions']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", prescription)
        prescription.click()
        time.sleep(3)
        addmedicine = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='+ Add Medicine']"))
            )
        addmedicine.click()
        time.sleep(1)
        medicinename = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[@class= 'p-element medicine-name p-editable-column p-cell-editing']//input[@type='text']"))
            )
        medicinename.send_keys('p')
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'paracetamol')]"))
            ).click()
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[@class='p-element first-cell p-editable-column']"))
            ).click()
        time.sleep(1)
        dose = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][2]//input[@type='text']"))
            )
        dose.send_keys('650 mg')
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[3]"))
            ).click()
        time.sleep(1)
        frequency = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][3]//input[@type='text']"))
            )
        frequency.send_keys('Once daily')
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[4]"))
            ).click()
        time.sleep(1)
        duration = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][4]//input[@type='text']"))
            )
        duration.send_keys('2 weeks')
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[5]"))
            ).click()
        time.sleep(1)
        pre_notes = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][5]//input[@type='text']"))
            )
        pre_notes.send_keys('Take with food')
        time.sleep(1)
        Notesif_any = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']"))
            )
        Notesif_any.send_keys('Please schedule a follow-up consultation after two weeks if the condition does not improve.')
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
            ).click()
        time.sleep(3)
        try:
            template_name = "Temperature"
            suffix = 0
            while True:  
                if suffix == 0:
                    save_as_template = template_name
                else:
                    save_as_template = f"{template_name} {suffix}"
                WebDriverWait(login, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Actions']"))
                    ).click()
                WebDriverWait(login, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Save as Template']"))
                    ).click()
                time.sleep(2)
                WebDriverWait(login, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Template Name to Save']"))
                    ).send_keys(save_as_template)
                time.sleep(2)
                WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Save']"))
                ).click()
                toast_message = WebDriverWait(login, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
                )
                message = toast_message.text
                print("Toast Message:", message)
                time.sleep(3)
                if 'Template Data Saved Succesfully' in message:
                    break
                else:
                    suffix += 1
        except Exception as e:
            print(f"An error occurred:{str(e)}")
    except Exception as e:
        allure.attach(  # use Allure package, .attach() met hod, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

    
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"]) 
def test_patient_MR_Edit(login):
    try:
        time.sleep(5)
        WebDriverWait(login,20).until(
            EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'customers.gif')]//following::div[contains(text(),'Patients')]")
        )
        ).click()
        time.sleep(3)
        patientsearch =WebDriverWait(login,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter name or phone or id']"))
        )
        patientsearch.send_keys('5556328484')
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 151']"))
        ).click()
        time.sleep(3)
        prescription = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Prescriptions']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", prescription)
        prescription.click()
        time.sleep(3)
        addmedicine = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='+ Add Medicine']"))
            )
        addmedicine.click()
        time.sleep(1)
        medicinename = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[@class= 'p-element medicine-name p-editable-column p-cell-editing']//input[@type='text']"))
            )
        medicinename.send_keys('p')
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'paracetamol')]"))
            ).click()
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[@class='p-element first-cell p-editable-column']"))
            ).click()
        time.sleep(1)
        dose = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][2]//input[@type='text']"))
            )
        dose.send_keys('650 mg')
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[3]"))
            ).click()
        time.sleep(1)
        frequency = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][3]//input[@type='text']"))
            )
        frequency.send_keys('Once daily')
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[4]"))
            ).click()
        time.sleep(1)
        duration = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][4]//input[@type='text']"))
            )
        duration.send_keys('2 weeks')
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[5]"))
            ).click()
        time.sleep(1)
        pre_notes = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][5]//input[@type='text']"))
            )
        pre_notes.send_keys('Take with food')
        time.sleep(1)
        Notesif_any = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']"))
            )
        Notesif_any.send_keys('Please schedule a follow-up consultation after two weeks if the condition does not improve.')
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
            ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Actions']"))
                    ).click()
        time.sleep(2)
        Edit_button =WebDriverWait(login, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//span[@class='mdc-list-item__primary-text'][normalize-space()='Edit']"))
                    )
        Edit_button.click()
        login.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -150);", prescription)
        time.sleep(5)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[4]"))
            ).click()
        time.sleep(3)
        duration = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][4]//input[@type='text']"))
            )
        duration.clear()
        duration.send_keys('3 weeks')
        time.sleep(1)
        Notesif_any = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']"))
            )
        Notesif_any.click()
        Notesif_any.send_keys(Keys.CONTROL + 'a')
        Notesif_any.send_keys(Keys.DELETE)
        Notesif_any.send_keys('Please schedule a follow-up consultation after three weeks .')
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
            ).click()
        toast_message = WebDriverWait(login, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
                )
        message = toast_message.text
        print("Toast Message:", message)
        time.sleep(3)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() met hod, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
