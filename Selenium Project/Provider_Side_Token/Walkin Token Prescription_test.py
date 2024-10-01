
from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.common import TimeoutException , JavascriptException
from selenium.webdriver.support.ui import Select

@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_patient_Manage_Template(login):
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
        manage_template = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//img[@src='./assets/images/customer-record/rx-templates.png']"))
        )
        manage_template.click()
        time.sleep(3)
        classic = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Classic']"))
        )
        classic.click()
        save = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='button'][normalize-space()='Save']"))
        )
        save.click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        time.sleep(3)
    except Exception as e:
            allure.attach(  
            login.get_screenshot_as_png(), 
            name="full_page",  
            attachment_type=AttachmentType.PNG,
            )
            raise e  
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_patient_MR_Sharing(login):
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
        allure.attach( 
            login.get_screenshot_as_png(),  
            name="full_page", 
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
        allure.attach( 
            login.get_screenshot_as_png(),  
            name="full_page",
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
        allure.attach(  
            login.get_screenshot_as_png(), 
            name="full_page",  
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
        allure.attach( 
            login.get_screenshot_as_png(), 
            name="full_page", 
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
        # dropdown = WebDriverWait(login, 20).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, 'print-preview-app'))
        # )
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
        allure.attach( 
            login.get_screenshot_as_png(), 
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        )
        raise e
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"]) 
def test_patient_MR_Templatesaving(login):
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
        patientsearch.send_keys('5552080585')
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 167']"))
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
                if suffix == 0:save_as_template = template_name 
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
                if 'Template Data Saved Successfully' in message:
                    break
                else:
                    suffix += 1
                    save_as_template = f"{template_name} {suffix}"
        except Exception as e:
            print(f"An error occurred:{str(e)}")
    except Exception as e:
        allure.attach( 
            login.get_screenshot_as_png(),
            name="full_page",  
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
        allure.attach(  
            login.get_screenshot_as_png(), 
            name="full_page", 
            attachment_type=AttachmentType.PNG,
        )
        raise e


@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"]) 
def test_patient_MR_createTemplate(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//img[contains(@src, 'customers.gif')]//following::div[contains(text(),'Patients')]")
        time.sleep(3)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter name or phone or id']", '5556328484')
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 151']")
        time.sleep(3)
        prescription = wait_and_click(login, By.XPATH, "//span[normalize-space()='Prescriptions']")
        login.execute_script("arguments[0].scrollIntoView();", prescription)
        time.sleep(3)
        # Create Template
        wait_and_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component ng-star-inserted']")
        basetemplatename = 'Temp'
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        uniquename = f"{basetemplatename}_{random_string}"
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Template Name']", 
                                          uniquename)
        wait_and_click(login, By.XPATH, "//div[@class='add']")
        time.sleep(3)
        # Fill in the template details
        medicine = wait_and_send_keys(login, By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[contains(@class, 'medicine-name')]//p-celleditor//textarea", 'Furosemide')
        medicine.send_keys(Keys.TAB)
        dose = wait_and_send_keys(login, By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[contains(@class, 'first-cell')][1]//p-celleditor//textarea", '2mg')
        dose.send_keys(Keys.TAB)
        frequency = wait_and_send_keys(login, By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[not(contains(@class, 'first-cell'))][2]//p-celleditor//textarea", 'Twice a day')
        frequency.send_keys(Keys.TAB)
        duration = wait_and_send_keys(login, By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[not(contains(@class, 'first-cell'))][3]//p-celleditor//textarea", '2 Weeks')
        duration.send_keys(Keys.TAB)
        wait_and_send_keys(login, By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[not(contains(@class, 'first-cell'))][4]//p-celleditor//textarea", 'Before food')
        time.sleep(3)
        wait_and_click(login, By.XPATH, "//button[normalize-space()='Save Template']")
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(3)
        # Search and Edit Template
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search Template']", uniquename)  # Adjust search term if necessary
        wait_and_click(login, By.XPATH, "//span[@class='p-button-icon pi pi-search']")
        time.sleep(3)
        wait_and_click(login, By.XPATH, "//span[normalize-space()='Edit']")
        time.sleep(3)
        wait_and_click(login, By.XPATH, "//button[normalize-space()='Update Template']")
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(3)
        # View and Delete Template
        wait_and_click(login, By.XPATH, "//span[@class='p-button-icon pi pi-search']")
        wait_and_click(login, By.XPATH, "//span[normalize-space()='View']")
        time.sleep(3)
        wait_and_click(login, By.XPATH, "//i[@class='fa fa-times']")
        print("Template viewed successfully")
        time.sleep(3)
        wait_and_click(login, By.XPATH, "//span[normalize-space()='Delete']")
        time.sleep(3)
        wait_and_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(3)
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(3)
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e

@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"]) 
def test_patient_MR_usetemplate(login):
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
        search_template = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search Template']"))
            )
        search_template.click()
        search_template.send_keys('pressure')
        search_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[@class='p-button-icon pi pi-search']"))
            )
        search_button.click()
        try:
            search_result = WebDriverWait(login, 10).until(
                            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'pressure')]"))
                            )
            if search_result.is_displayed():
                WebDriverWait(login, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Use']"))
                    ).click()
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
        except TimeoutException:
            WebDriverWait(login, 20).until(
                        EC.presence_of_element_located((By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']"))
                    ).click()
            time.sleep(3)
            WebDriverWait(login, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Template Name']"))
                    ).click()
            time.sleep(3)
            templatename = WebDriverWait(login, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Template Name']"))
                    )
            templatename.click()
            templatename.send_keys('abc')
            time.sleep(3)
            WebDriverWait(login, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//div[@class='add']"))
                    ).click()
            time.sleep(3)
            medicine = WebDriverWait(login, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[contains(@class, 'medicine-name')]//p-celleditor//textarea"))
                    )
            medicine.click()
            medicine.send_keys('Furosemide')
            time.sleep(1)
            medicine.send_keys(Keys.TAB)
            dose = WebDriverWait(login, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[contains(@class, 'first-cell')][1]//p-celleditor//textarea"))
                    )
            dose.click()
            dose.send_keys('2mg')
            time.sleep(1)
            dose.send_keys(Keys.TAB)
            frequency = WebDriverWait(login, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[not(contains(@class, 'first-cell'))][2]//p-celleditor//textarea"))
                    )
            frequency.click()
            frequency.send_keys('ab')
            time.sleep(1)
            frequency.send_keys(Keys.TAB)
            Duration = WebDriverWait(login, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[not(contains(@class, 'first-cell'))][3]//p-celleditor//textarea"))
                    )
            Duration.click()
            Duration.send_keys('ab')
            time.sleep(1)
            Duration.send_keys(Keys.TAB)
            Instrn = WebDriverWait(login, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[not(contains(@class, 'first-cell'))][4]//p-celleditor//textarea"))
                    )
            Instrn.click()
            Instrn.send_keys('ab')
            time.sleep(3)
            WebDriverWait(login, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save Template']"))
                    ).click()
            toast_message = WebDriverWait(login, 10).until(
                            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
                        )
            message = toast_message.text
            print("Toast Message:", message)
            time.sleep(3)
    except Exception as e:
        allure.attach( 
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"] )
def test_patient_prescriptionslist(login):
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
        medicinename.send_keys('chlorpheniramine')
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[@class='p-element first-cell p-editable-column']"))
            ).click()
        time.sleep(1)
        dose = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][2]//input[@type='text']"))
            )
        dose.send_keys('100 mg')
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[3]"))
            ).click()
        time.sleep(1)
        frequency = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][3]//input[@type='text']"))
            )
        frequency.send_keys('twice daily')
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[4]"))
            ).click()
        time.sleep(1)
        duration = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][4]//input[@type='text']"))
            )
        duration.send_keys('1 week')
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@class='mobile-card ng-star-inserted']//td[5]"))
            ).click()
        time.sleep(1)
        pre_notes = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-editable-column')][5]//input[@type='text']"))
            )
        pre_notes.send_keys('Take before food')
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
        login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        latest_row_xpath = "(//tr[@class='ng-star-inserted'])[2]"
        latest_row = WebDriverWait(login, 10).until(EC.presence_of_element_located((By.XPATH, latest_row_xpath)))
        print(latest_row.text.strip())
        sharebutton_xpath= ".//span[contains(@class, 'more-actions-btn')]/img[@alt='share']"
        sharebutton = latest_row.find_element(By.XPATH, sharebutton_xpath)
        sharebutton.click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Enter message description']"))
            ).send_keys('Sharing Prescription')
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Email']"))
            ).click()
        time.sleep(1)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Whatsapp']"))
            ).click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='button'][normalize-space()='Share']"))
            ).click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(5)
        # download_xpath = "//span[contains(text(), 'Download')]"
        downloadbutton = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(((By.XPATH, "//span[contains(text(), 'Download')]")))
        )
        downloadbutton.click() #//span[@class='mat-mdc-menu-trigger more-actions-btn mt-2 pointer-cursor ng-star-inserted']
        time.sleep(3)
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  # param1
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        )
        raise e  
    
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"] )
def test_patient_cancel_prescriptionslist(login):
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
                EC.presence_of_element_located((By.XPATH, "(//img[@alt='dropdown'])[1]"))
            ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Cancel']"))
            ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
            ).click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        time.sleep(3)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//img[@alt='dropdown'])[1]"))
            ).click()
        time.sleep(3)
        view = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[@class='mdc-list-item__primary-text'][normalize-space()='View']"))
            )
        view.click()
        # login.execute_script("window.scrollTo(0, 0);")
        time.sleep(3)
    except Exception as e:
        allure.attach( 
            login.get_screenshot_as_png(),  
            name="full_page", 
            attachment_type=AttachmentType.PNG,
        )
        raise e  
    
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Medical_History(login):
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
        medical_history = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//img[@src='./assets/images/customer-record/personal-medical-history.png']"))
        )
        medical_history.click()
        time.sleep(2)
        add_record = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Add')]"))
        )
        add_record.click()
        time.sleep(2)
        medical_history_title =WebDriverWait(login,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Medical History Title']"))
        )
        medical_history_title.send_keys('OP Booking INFO')
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Upload File']"))
        ).click()
        time.sleep(5)
        current_working_directory = os.getcwd()
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\prescription.pdf")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        time.sleep(3)
        add_medical_history = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted']//span[@class='ng-star-inserted'][normalize-space()='Medical History']"))
        )
        add_medical_history.click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='pi pi-times']"))
        ).click()
        time.sleep(3)
        medical_history = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//img[@src='./assets/images/customer-record/personal-medical-history.png']"))
        )
        medical_history.click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='pi pi-paperclip']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='cdk-overlay-container']//div[@class='text-center']//div[1]"))
        ).click()
        time.sleep(3)
        handles = login.window_handles
        login.switch_to.window(handles[1])
        login.close()
        login.switch_to.window(handles[0])
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-times']"))
        ).click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='pi pi-pencil']"))
        ).click()
        time.sleep(3)
        medical_history_title =WebDriverWait(login,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Medical History Title']"))
        )
        medical_history_title.clear()
        medical_history_title.send_keys('OP Booking Number')
        update_medical_history = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='update']"))
        )
        update_medical_history.click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        time.sleep(3)
        delete_medical_history = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='pi pi-trash']"))
        )
        delete_medical_history.click()
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
        ).click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        )
        raise e 