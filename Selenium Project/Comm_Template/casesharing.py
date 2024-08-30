from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.common import TimeoutException

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Case_Sharing")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_case_sharing(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//img[contains(@src, 'settings.gif')]//following::div[contains(text(),'Settings')]")
        time.sleep(3)
        commun = wait_and_locate_click(login, By.XPATH, "//div[normalize-space()='Communications And Notifications']")
        login.execute_script("window.scrollTo(0, document.body.scrollHeight);", commun)
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Notifications']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//h2[normalize-space()='Custom Templates']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create New']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='context']//div[@aria-label='dropdown trigger']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[@id='p-highlighted-option']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='displayName']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Share CasePdf']")
        time.sleep(3)
        uniquename = f"Case{''.join(random.choices(string.ascii_letters + string.digits, k=8))}"
        wait_and_send_keys(login, By.XPATH, "//div[@class='form-group']//input[contains(@class, 'p-inputtext')]", uniquename)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//input[@id='mat-mdc-checkbox-1-input']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//input[@id='mat-mdc-checkbox-2-input']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted']")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save & Next']")
        time.sleep(2)
        editors = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']//p"))
        )
        editors.click()
        wait_and_locate_click(login, By.XPATH, "//div[@class='form-group text-ceditor pointer-cursor']//span[@class='mgn-lt-5'][normalize-space()='Add Variables']")
        time.sleep(2)
        consumer_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Consumer name']")) 
        )
        consumer_name.click()
        editors.send_keys(Keys.SPACE)  
        editors.send_keys("Doctor's Note:")
        wait_and_locate_click(login, By.XPATH, "//div[@class='form-group text-ceditor pointer-cursor']//span[@class='mgn-lt-5'][normalize-space()='Add Variables']")
        # time.sleep(2)
        doctor_note = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Message']")) 
        )
        doctor_note.click()
        editors.send_keys(Keys.ENTER)  
        wait_and_locate_click(login, By.XPATH, "//div[@class='form-group text-ceditor pointer-cursor']//span[@class='mgn-lt-5'][normalize-space()='Add Variables']")
        # time.sleep(2)
        case_file_link = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Prescription Link']")) 
        )
        case_file_link.click()
        time.sleep(2)
        email_subject_line = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[1]/input[1]"))
        )
        email_subject_line.click()
        email_subject_line.send_keys("CaseFile from")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[2]")
        time.sleep(2)
        business_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Business Name']")) 
        )
        business_name.click()
        time.sleep(2)
        header_notes = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[2]/input[1]"))
        )
        header_notes.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[3]")
        consumer_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Consumer name']")) 
        )
        consumer_name.click()
        time.sleep(2)
        salutation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[3]/input[1]"))
        )
        salutation.click()
        salutation.send_keys("Greetings!!")
        time.sleep(2)
        Signature = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[4]/input[1]"))
        )
        Signature.click()
        Signature.send_keys("Thank you for using Jaldee")
        time.sleep(2)
        Footer = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[5]/input[1]"))
        )
        Footer.click()
        Footer.send_keys("Powered by Jaldee business")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='actiondiv mgn-lt-10 desktop-only']//button[@type='submit'][normalize-space()='Update']")
        time.sleep(2)
        wait_and_visible_click(login, By.XPATH, "(//span[contains(text(),'Inactive')])[1]")
        time.sleep(2)
        WebDriverWait(login,20).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='pi pi-bars text-light']")
        )
        ).click()
        time.sleep(3)
        WebDriverWait(login,20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Patients')]")
        )
        ).click()
        time.sleep(3)
        patientsearch =WebDriverWait(login,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter name or phone or id']"))
        )
        patientsearch.send_keys('9400553615')
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 13']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create Case']"))
        ).click()
        time.sleep(3)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Case Description']", 'Automation Test Case')
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder ='Enter Chief Complaint']", 'Fever')
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='History']")
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder ='Enter History']", 'Cold')
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-list-item__primary-text']")
        wait_and_click(login, By.XPATH, "//button[normalize-space()='Save']")
        # login.execute_script("arguments[0].scrollIntoView();", History_save)
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//div[@class='col-md-8 order-2 order-md-1']//button[2]")
        time.sleep(3)
        wait_and_send_keys(login, By.XPATH, "//textarea[@placeholder='Enter message description']", 'Casesharing')
        time.sleep(1)
        login.find_element(By.XPATH, "//span[contains(text(),'Email')]").click()
        login.find_element(By.XPATH, "//span[contains(text(),'Whatsapp')]").click()
        time.sleep(3)
        wait_and_click(login, By.XPATH, "//button[contains(text(),'Share')]")
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  