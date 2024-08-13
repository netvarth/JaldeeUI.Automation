from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.common import TimeoutException,JavascriptException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


# New invoice from dashboard and Newinvoice from viewdetails
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_token_newinvoice(login):
    try:
        time.sleep(5)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
                )
            )
        ).click()
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Token']"))
        ).click()
        time.sleep(5)
        lucenesearch = login.find_element(By.XPATH, "//input[@placeholder='Enter name or phone or id']"
                                        )
        lucenesearch.send_keys("5550004454")
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 29']"))
        ).click()
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Select Location']"))
        ).click()
        dropdownelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel='place']"))
        )
        dropdownelement.click()
        time.sleep(5)
        droplocation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Ashok Nagar']"))
        )
        droplocation.click()
        print("Select Location:", droplocation.text)
        userelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='mt-2 col-lg-8 col-xxl-6'])[2]"))
        )
        userelement.click()
        time.sleep(3)
        dropgeneralservice = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@aria-label='General Services']"))
        )
        dropgeneralservice.click()
        print("Select User:", dropgeneralservice.text)
        assignto = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@optionlabel='fullName']//div[@class='text-left p-dropdown p-component']"))
        )
        assignto.click()
        time.sleep(3)
        assigntounassigneduser = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@id='p-highlighted-option']"))
        )
        assigntounassigneduser.click()
        print("Assignto:", assigntounassigneduser.text)
        consultation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@optionlabel='name']//div[@class='text-left p-dropdown p-component']"))
        )
        consultation.click()
        time.sleep(3)
        dropconsultation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@aria-label='Consultation']"))
        )
        dropconsultation.click()
        print("Select service:", dropconsultation.text)
        time.sleep(3)
        # today = datetime.date.today()
        today_xpath = ("//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected "
                    "mat-calendar-body-today']")
        # today_xpath = "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected']"
        today_element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, today_xpath))
        )
        today_element.click()
        print("Today's Date:", today_element.text)
        queueelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='col-lg-12 col-xxl-12 p-2']//div[@class='p-inputgroup']"))
        )
        queueelement.click()
        time.sleep(3)
        dropqueue = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@class='p-ripple p-element p-dropdown-item p-highlight']["
                                                    "@id='p-highlighted-option']"))
        )
        dropqueue.click()
        print("Selected Queue", dropqueue.text)
        time.sleep(3)
        confirmed = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm']"))
        )
        confirmed.click()
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
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']"))
                )
                cancelbutton.click()
            except TimeoutException:
                cancelbutton = WebDriverWait(login, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']"))
                )
                cancelbutton.click()
                print("Cancelled Successfully")
            time.sleep(1)
        while True:
            try:
                print("Before in the loop")
                time.sleep(3)
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//angledoublerighticon[@class='p-element p-icon-wrapper "
                                                            "ng-star-inserted']"))
                )
                next_button.click()
            except:
                print("EC Caught:Next button not found or clicked.")
                break
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))

        )
        last_element_in_accordian.click()
        time.sleep(5)
        login.execute_script("arguments[0].scrollIntoView(true);", last_element_in_accordian)
        print("Accordion expanded")
        # # *****NewInvoice from dashboard  and share the payment link*****************
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='New Invoice']"))
        ).click()
        print("New Invoice Clicked")
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'CheckupHalfprepayOn')]"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder "
                                                        "ng-star-inserted']"))
        ).click()
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Share Payment Link']"))
        ).click()
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='cs-btn bt1 btn btn-primary mdc-button "
                                                    "mat-mdc-button mat-unthemed mat-mdc-button-base']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-arrow-left']"))
        ).click()
        time.sleep(3)
        while True:
            try:
                print("Before in the loop")
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//angledoublerighticon[@class='p-element p-icon-wrapper "
                                                            "ng-star-inserted']"))
                )
                next_button.click()
            except:
                print("EC Caught:Next button not found or clicked.")
                break
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
            )
        last_element_in_accordian.click()
        time.sleep(3)
        print("Recent booking element clicked")
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Details']"))
        ).click()
        time.sleep(5)
        print("ViewDetails Button Clicked")
        # # *** New Invoice in View Details for subservice and paybycash and settled the invoice***
        Newinvoice = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='New Invoice']"))
            )
        login.execute_script("arguments[0].scrollIntoView();", Newinvoice)
        Newinvoice.click()
        print("Newinvoice Clicked")
        time.sleep(5)
        additem = WebDriverWait(login, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='card inv-card Item-Details']//div[@class='d-flex justify-content-start']//button[normalize-space()='Add Procedure/Item']"))
            )
        login.execute_script("arguments[0].scrollIntoView();", additem)
        login.execute_script("arguments[0].click();", additem)
        print("Additem Clicked")
        time.sleep(5)   
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Cleaning subservice']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='p-multiselect-label p-placeholder']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Manikandan']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space() = 'Save']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "// span[ @class ='p-dropdown-label p-inputtext p-placeholder "
                                                    "ng-star-inserted']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Pay by Cash']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Pay']"))
        ).click()
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='text-center img-container']"))
        )
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Settle Invoice']"))
        ).click()
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(5)
        WebDriverWait(login, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//i[@class='fa fa-arrow-left']"))
        ).click()
        time.sleep(5)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e  
    
 # NewInvoice from dashboard and paybyothers and cancel the invoice
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_token_createinvoice_pay_cancel(login):
    try:
        time.sleep(5)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
                )
            )
        ).click()
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Token']"))
        ).click()
        time.sleep(5)
        lucenesearch = login.find_element(By.XPATH, "//input[@placeholder='Enter name or phone or id']"
                                        )
        lucenesearch.send_keys("5550004454")
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 29']"))
        ).click()
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Select Location']"))
        ).click()
        dropdownelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel='place']"))
        )
        dropdownelement.click()
        time.sleep(5)
        droplocation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Ashok Nagar']"))
        )
        droplocation.click()
        print("Select Location:", droplocation.text)
        userelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='mt-2 col-lg-8 col-xxl-6'])[2]"))
        )
        userelement.click()
        time.sleep(3)
        dropgeneralservice = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@aria-label='General Services']"))
        )
        dropgeneralservice.click()
        print("Select User:", dropgeneralservice.text)
        assignto = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@optionlabel='fullName']//div[@class='text-left p-dropdown p-component']"))
        )
        assignto.click()
        time.sleep(3)
        assigntounassigneduser = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@id='p-highlighted-option']"))
        )
        assigntounassigneduser.click()
        print("Assignto:", assigntounassigneduser.text)
        consultation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@optionlabel='name']//div[@class='text-left p-dropdown p-component']"))
        )
        consultation.click()
        time.sleep(3)
        dropconsultation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@aria-label='Consultation']"))
        )
        dropconsultation.click()
        print("Select service:", dropconsultation.text)
        time.sleep(3)
        # today = datetime.date.today()
        today_xpath = ("//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected "
                    "mat-calendar-body-today']")
        # today_xpath = "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected']"
        today_element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, today_xpath))
        )
        today_element.click()
        print("Today's Date:", today_element.text)
        queueelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='col-lg-12 col-xxl-12 p-2']//div[@class='p-inputgroup']"))
        )
        queueelement.click()
        time.sleep(3)
        dropqueue = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@class='p-ripple p-element p-dropdown-item p-highlight']["
                                                    "@id='p-highlighted-option']"))
        )
        dropqueue.click()
        print("Selected Queue", dropqueue.text)
        time.sleep(3)
        confirmed = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm']"))
        )
        confirmed.click()
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
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']"))
                )
                cancelbutton.click()
            except TimeoutException:
                cancelbutton = WebDriverWait(login, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']"))
                )
                cancelbutton.click()
                print("Cancelled Successfully")
            time.sleep(1)
        while True:
            try:
                print("Before in the loop")
                time.sleep(3)
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//angledoublerighticon[@class='p-element p-icon-wrapper "
                                                            "ng-star-inserted']"))
                )
                next_button.click()
            except:
                print("EC Caught:Next button not found or clicked.")
                break
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))

        )
        last_element_in_accordian.click()
        time.sleep(5)
        login.execute_script("arguments[0].scrollIntoView(true);", last_element_in_accordian)
        print("Accordion expanded")
        # # *****NewInvoice and paybyothers and cancel the invoice*****************
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='New Invoice']"))
        ).click()
        print("New Invoice Clicked")
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'CheckupHalfprepayOn')]"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder "
                                                        "ng-star-inserted']"))
        ).click()
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Pay by Others']"))
        ).click()
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Pay']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
        ).click()
        time.sleep(3)
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Cancel Invoice']"))
        ).click()
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter any notes for your future reference']"))
        ).send_keys("Invoice Cancelled")
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        WebDriverWait(login, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//i[@class='fa fa-arrow-left']"))
        ).click()
        time.sleep(5)
    except Exception as e:
            allure.attach(  # use Allure package, .attach() method, pass 3 params
                login.get_screenshot_as_png(),  # param1
                # login.screenshot()
                name="full_page",  # param2
                attachment_type=AttachmentType.PNG,
            )
            raise e  


@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_token_createinvoice(login):
    try:
        time.sleep(5)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
                )
            )
        ).click()
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Token']"))
        ).click()
        time.sleep(5)
        lucenesearch = login.find_element(By.XPATH, "//input[@placeholder='Enter name or phone or id']"
                                        )
        lucenesearch.send_keys("5550004454")
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 29']"))
        ).click()
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Select Location']"))
        ).click()
        dropdownelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel='place']"))
        )
        dropdownelement.click()
        time.sleep(5)
        droplocation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Ashok Nagar']"))
        )
        droplocation.click()
        print("Select Location:", droplocation.text)
        userelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='mt-2 col-lg-8 col-xxl-6'])[2]"))
        )
        userelement.click()
        time.sleep(3)
        dropgeneralservice = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@aria-label='General Services']"))
        )
        dropgeneralservice.click()
        print("Select User:", dropgeneralservice.text)
        assignto = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@optionlabel='fullName']//div[@class='text-left p-dropdown p-component']"))
        )
        assignto.click()
        time.sleep(3)
        assigntounassigneduser = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@id='p-highlighted-option']"))
        )
        assigntounassigneduser.click()
        print("Assignto:", assigntounassigneduser.text)
        consultation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@optionlabel='name']//div[@class='text-left p-dropdown p-component']"))
        )
        consultation.click()
        time.sleep(3)
        dropconsultation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@aria-label='Consultation']"))
        )
        dropconsultation.click()
        print("Select service:", dropconsultation.text)
        time.sleep(3)
        # today = datetime.date.today()
        today_xpath = ("//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected "
                    "mat-calendar-body-today']")
        # today_xpath = "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected']"
        today_element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, today_xpath))
        )
        today_element.click()
        print("Today's Date:", today_element.text)
        queueelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='col-lg-12 col-xxl-12 p-2']//div[@class='p-inputgroup']"))
        )
        queueelement.click()
        time.sleep(3)
        dropqueue = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@class='p-ripple p-element p-dropdown-item p-highlight']["
                                                    "@id='p-highlighted-option']"))
        )
        dropqueue.click()
        print("Selected Queue", dropqueue.text)
        time.sleep(3)
        confirmed = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm']"))
        )
        confirmed.click()
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
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']"))
                )
                cancelbutton.click()
            except TimeoutException:
                cancelbutton = WebDriverWait(login, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']"))
                )
                cancelbutton.click()
                print("Cancelled Successfully")
            time.sleep(1)
        while True:
            try:
                print("Before in the loop")
                time.sleep(3)
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//angledoublerighticon[@class='p-element p-icon-wrapper "
                                                            "ng-star-inserted']"))
                )
                next_button.click()
            except:
                print("EC Caught:Next button not found or clicked.")
                break
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))

        )
        last_element_in_accordian.click()
        time.sleep(5)
        login.execute_script("arguments[0].scrollIntoView(true);", last_element_in_accordian)
        print("Accordion expanded")
        # # *****NewInvoice and paybyothers and cancel the invoice*****************
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='New Invoice']"))
        ).click()
        print("New Invoice Clicked")
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'CheckupHalfprepayOn')]"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(5)

        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder "
                                                        "ng-star-inserted']"))
        ).click()
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Pay by Others']"))
        ).click()
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Pay']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
        ).click()
        time.sleep(3)
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Cancel Invoice']"))
        ).click()
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter any notes for your future reference']"))
        ).send_keys("Invoice Cancelled")
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        WebDriverWait(login, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//i[@class='fa fa-arrow-left']"))
        ).click()
        time.sleep(5)
    except Exception as e:
            allure.attach(  # use Allure package, .attach() method, pass 3 params
                login.get_screenshot_as_png(),  # param1
                # login.screenshot()
                name="full_page",  # param2
                attachment_type=AttachmentType.PNG,
            )
            raise e  

# Newinvoice created ,shared,edited to add new procedure,further edited to remove the procedure.

@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_token_createinvoice_sharepdf(login):
    try:
        time.sleep(5)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
                )
            )
        ).click()
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Token']"))
        ).click()
        time.sleep(5)
        lucenesearch = login.find_element(By.XPATH, "//input[@placeholder='Enter name or phone or id']"
                                        )
        lucenesearch.send_keys("5550004454")
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 29']"))
        ).click()
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Select Location']"))
        ).click()
        dropdownelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel='place']"))
        )
        dropdownelement.click()
        time.sleep(5)
        droplocation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Ashok Nagar']"))
        )
        droplocation.click()
        print("Select Location:", droplocation.text)
        userelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='mt-2 col-lg-8 col-xxl-6'])[2]"))
        )
        userelement.click()
        time.sleep(3)
        dropgeneralservice = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@aria-label='General Services']"))
        )
        dropgeneralservice.click()
        print("Select User:", dropgeneralservice.text)
        assignto = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@optionlabel='fullName']//div[@class='text-left p-dropdown p-component']"))
        )
        assignto.click()
        time.sleep(3)
        assigntounassigneduser = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@id='p-highlighted-option']"))
        )
        assigntounassigneduser.click()
        print("Assignto:", assigntounassigneduser.text)
        consultation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@optionlabel='name']//div[@class='text-left p-dropdown p-component']"))
        )
        consultation.click()
        time.sleep(3)
        dropconsultation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@aria-label='Consultation']"))
        )
        dropconsultation.click()
        print("Select service:", dropconsultation.text)
        time.sleep(3)
        # today = datetime.date.today()
        today_xpath = ("//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected "
                    "mat-calendar-body-today']")
        # today_xpath = "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected']"
        today_element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, today_xpath))
        )
        today_element.click()
        print("Today's Date:", today_element.text)
        queueelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='col-lg-12 col-xxl-12 p-2']//div[@class='p-inputgroup']"))
        )
        queueelement.click()
        time.sleep(3)
        dropqueue = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@class='p-ripple p-element p-dropdown-item p-highlight']["
                                                    "@id='p-highlighted-option']"))
        )
        dropqueue.click()
        print("Selected Queue", dropqueue.text)
        time.sleep(3)
        confirmed = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm']"))
        )
        confirmed.click()
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
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']"))
                )
                cancelbutton.click()
            except TimeoutException:
                cancelbutton = WebDriverWait(login, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']"))
                )
                cancelbutton.click()
                print("Cancelled Successfully")
            time.sleep(1)
        while True:
            try:
                print("Before in the loop")
                time.sleep(3)
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//angledoublerighticon[@class='p-element p-icon-wrapper "
                                                            "ng-star-inserted']"))
                )
                next_button.click()
            except:
                print("EC Caught:Next button not found or clicked.")
                break
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))

        )
        last_element_in_accordian.click()
        time.sleep(5)
        login.execute_script("arguments[0].scrollIntoView(true);", last_element_in_accordian)
        print("Accordion expanded")
        # # *****NewInvoice and sharepdf*****************
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='New Invoice']"))
        ).click()
        print("New Invoice Clicked")
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'CheckupHalfprepayOn')]"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(5)
        sharepdf =WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Share PDF']"))
        )
        sharepdf.click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(3)
        Edit = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Edit']"))
        )
        Edit.click()
        time.sleep(3)
        add_item =WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        )
        add_item.click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'ConsultFullPrepayON')]"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Update']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(3)
        Edit_again = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Edit']"))
        )
        Edit_again.click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='mat-mdc-button-touch-target']"))
        ).click()
        time.sleep(3)
        remove_item = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Remove Procedure']"))
        )
        remove_item.click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Update']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//i[@class='fa fa-arrow-left']"))
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
       # Change quantiy of the procedure of Invoice using Edit
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_token_createinvoice_editqty(login):
    try:
        time.sleep(5)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
                )
            )
        ).click()
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Token']"))
        ).click()
        time.sleep(5)
        lucenesearch = login.find_element(By.XPATH, "//input[@placeholder='Enter name or phone or id']"
                                        )
        lucenesearch.send_keys("5550004454")
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 29']"))
        ).click()
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Select Location']"))
        ).click()
        dropdownelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel='place']"))
        )
        dropdownelement.click()
        time.sleep(5)
        droplocation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Ashok Nagar']"))
        )
        droplocation.click()
        print("Select Location:", droplocation.text)
        userelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='mt-2 col-lg-8 col-xxl-6'])[2]"))
        )
        userelement.click()
        time.sleep(3)
        dropgeneralservice = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@aria-label='General Services']"))
        )
        dropgeneralservice.click()
        print("Select User:", dropgeneralservice.text)
        assignto = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@optionlabel='fullName']//div[@class='text-left p-dropdown p-component']"))
        )
        assignto.click()
        time.sleep(3)
        assigntounassigneduser = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@id='p-highlighted-option']"))
        )
        assigntounassigneduser.click()
        print("Assignto:", assigntounassigneduser.text)
        consultation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@optionlabel='name']//div[@class='text-left p-dropdown p-component']"))
        )
        consultation.click()
        time.sleep(3)
        dropconsultation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@aria-label='Consultation']"))
        )
        dropconsultation.click()
        print("Select service:", dropconsultation.text)
        time.sleep(3)
        # today = datetime.date.today()
        today_xpath = ("//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected "
                    "mat-calendar-body-today']")
        # today_xpath = "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected']"
        today_element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, today_xpath))
        )
        today_element.click()
        print("Today's Date:", today_element.text)
        queueelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='col-lg-12 col-xxl-12 p-2']//div[@class='p-inputgroup']"))
        )
        queueelement.click()
        time.sleep(3)
        dropqueue = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@class='p-ripple p-element p-dropdown-item p-highlight']["
                                                    "@id='p-highlighted-option']"))
        )
        dropqueue.click()
        print("Selected Queue", dropqueue.text)
        time.sleep(3)
        confirmed = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm']"))
        )
        confirmed.click()
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
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']"))
                )
                cancelbutton.click()
            except TimeoutException:
                cancelbutton = WebDriverWait(login, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']"))
                )
                cancelbutton.click()
                print("Cancelled Successfully")
            time.sleep(1)
        while True:
            try:
                print("Before in the loop")
                time.sleep(3)
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//angledoublerighticon[@class='p-element p-icon-wrapper "
                                                            "ng-star-inserted']"))
                )
                next_button.click()
            except:
                print("EC Caught:Next button not found or clicked.")
                break
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))

        )
        last_element_in_accordian.click()
        time.sleep(5)
        login.execute_script("arguments[0].scrollIntoView(true);", last_element_in_accordian)
        print("Accordion expanded")
        # # *****NewInvoice and sharepdf*****************
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='New Invoice']"))
        ).click()
        print("New Invoice Clicked")
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'CheckupHalfprepayOn')]"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(5)
        Edit = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Edit']"))
        )
        Edit.click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='mat-mdc-button-touch-target']"))
        ).click()
        editprocedure = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Edit Procedure/Item']"))
        )
        editprocedure.click()
        time.sleep(3)
        changeqty = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-input-4'])[1]"))
        )
        changeqty.click()
        changeqty.clear()
        changeqty.send_keys(3)
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Update']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(3)
        sharepdf =WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Share PDF']"))
        )
        sharepdf.click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//i[@class='fa fa-arrow-left']"))
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
    
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_token_createinvoice_editapplydiscount(login):
    try:
        time.sleep(5)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
                )
            )
        ).click()
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Token']"))
        ).click()
        time.sleep(5)
        lucenesearch = login.find_element(By.XPATH, "//input[@placeholder='Enter name or phone or id']"
                                        )
        lucenesearch.send_keys("5550004454")
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 29']"))
        ).click()
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Select Location']"))
        ).click()
        dropdownelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel='place']"))
        )
        dropdownelement.click()
        time.sleep(5)
        droplocation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Ashok Nagar']"))
        )
        droplocation.click()
        print("Select Location:", droplocation.text)
        userelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='mt-2 col-lg-8 col-xxl-6'])[2]"))
        )
        userelement.click()
        time.sleep(3)
        dropgeneralservice = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@aria-label='General Services']"))
        )
        dropgeneralservice.click()
        print("Select User:", dropgeneralservice.text)
        assignto = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@optionlabel='fullName']//div[@class='text-left p-dropdown p-component']"))
        )
        assignto.click()
        time.sleep(3)
        assigntounassigneduser = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@id='p-highlighted-option']"))
        )
        assigntounassigneduser.click()
        print("Assignto:", assigntounassigneduser.text)
        consultation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@optionlabel='name']//div[@class='text-left p-dropdown p-component']"))
        )
        consultation.click()
        time.sleep(3)
        dropconsultation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@aria-label='Consultation']"))
        )
        dropconsultation.click()
        print("Select service:", dropconsultation.text)
        time.sleep(3)
        # today = datetime.date.today()
        today_xpath = ("//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected "
                    "mat-calendar-body-today']")
        # today_xpath = "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected']"
        today_element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, today_xpath))
        )
        today_element.click()
        print("Today's Date:", today_element.text)
        queueelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='col-lg-12 col-xxl-12 p-2']//div[@class='p-inputgroup']"))
        )
        queueelement.click()
        time.sleep(3)
        dropqueue = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@class='p-ripple p-element p-dropdown-item p-highlight']["
                                                    "@id='p-highlighted-option']"))
        )
        dropqueue.click()
        print("Selected Queue", dropqueue.text)
        time.sleep(3)
        confirmed = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm']"))
        )
        confirmed.click()
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
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']"))
                )
                cancelbutton.click()
            except TimeoutException:
                cancelbutton = WebDriverWait(login, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']"))
                )
                cancelbutton.click()
                print("Cancelled Successfully")
            time.sleep(1)
        while True:
            try:
                print("Before in the loop")
                time.sleep(3)
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//angledoublerighticon[@class='p-element p-icon-wrapper "
                                                            "ng-star-inserted']"))
                )
                next_button.click()
            except:
                print("EC Caught:Next button not found or clicked.")
                break
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))

        )
        last_element_in_accordian.click()
        time.sleep(5)
        login.execute_script("arguments[0].scrollIntoView(true);", last_element_in_accordian)
        print("Accordion expanded")
        # # *****NewInvoice and sharepdf*****************
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='New Invoice']"))
        ).click()
        print("New Invoice Clicked")
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'CheckupHalfprepayOn')]"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(5)
        Edit = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Edit']"))
        )
        Edit.click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='mat-mdc-button-touch-target']"))
        ).click()
        time.sleep(3)
        apply_discount = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='mdc-list-item__primary-text'][normalize-space()='Apply Discount']"))
        )
        apply_discount.click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//option[normalize-space()='Select Discount']"))
            ).click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//option[normalize-space()='On Demand Discount']"))
        ).click()
        time.sleep(2)
        amount = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Amount']"))
        )
        amount.click()
        amount.send_keys(50)
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='exampleModalSizeDefault']//button[@type='button'][normalize-space()='Apply']"))
        ).click()
        time.sleep(3)
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Update']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(3)
        sharepdf =WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Share PDF']"))
        )
        sharepdf.click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//i[@class='fa fa-arrow-left']"))
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

@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_token_createinvoice_editapplycoupon(login):
    try:
        time.sleep(5)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
                )
            )
        ).click()
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Token']"))
        ).click()
        time.sleep(5)
        lucenesearch = login.find_element(By.XPATH, "//input[@placeholder='Enter name or phone or id']"
                                        )
        lucenesearch.send_keys("5550004454")
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 29']"))
        ).click()
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Select Location']"))
        ).click()
        dropdownelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel='place']"))
        )
        dropdownelement.click()
        time.sleep(5)
        droplocation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Ashok Nagar']"))
        )
        droplocation.click()
        print("Select Location:", droplocation.text)
        userelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='mt-2 col-lg-8 col-xxl-6'])[2]"))
        )
        userelement.click()
        time.sleep(3)
        dropgeneralservice = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@aria-label='General Services']"))
        )
        dropgeneralservice.click()
        print("Select User:", dropgeneralservice.text)
        assignto = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@optionlabel='fullName']//div[@class='text-left p-dropdown p-component']"))
        )
        assignto.click()
        time.sleep(3)
        assigntounassigneduser = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@id='p-highlighted-option']"))
        )
        assigntounassigneduser.click()
        print("Assignto:", assigntounassigneduser.text)
        consultation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@optionlabel='name']//div[@class='text-left p-dropdown p-component']"))
        )
        consultation.click()
        time.sleep(3)
        dropconsultation = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@aria-label='Consultation']"))
        )
        dropconsultation.click()
        print("Select service:", dropconsultation.text)
        time.sleep(3)
        # today = datetime.date.today()
        today_xpath = ("//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected "
                    "mat-calendar-body-today']")
        # today_xpath = "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected']"
        today_element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, today_xpath))
        )
        today_element.click()
        print("Today's Date:", today_element.text)
        queueelement = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='col-lg-12 col-xxl-12 p-2']//div[@class='p-inputgroup']"))
        )
        queueelement.click()
        time.sleep(3)
        dropqueue = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@class='p-ripple p-element p-dropdown-item p-highlight']["
                                                    "@id='p-highlighted-option']"))
        )
        dropqueue.click()
        print("Selected Queue", dropqueue.text)
        time.sleep(3)
        confirmed = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm']"))
        )
        confirmed.click()
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
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']"))
                )
                cancelbutton.click()
            except TimeoutException:
                cancelbutton = WebDriverWait(login, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']"))
                )
                cancelbutton.click()
                print("Cancelled Successfully")
            time.sleep(1)
        while True:
            try:
                print("Before in the loop")
                time.sleep(3)
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//angledoublerighticon[@class='p-element p-icon-wrapper "
                                                            "ng-star-inserted']"))
                )
                next_button.click()
            except:
                print("EC Caught:Next button not found or clicked.")
                break
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))

        )
        last_element_in_accordian.click()
        time.sleep(5)
        login.execute_script("arguments[0].scrollIntoView(true);", last_element_in_accordian)
        print("Accordion expanded")
        # # *****NewInvoice and sharepdf*****************
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='New Invoice']"))
        ).click()
        print("New Invoice Clicked")
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'CheckupHalfprepayOn')]"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(5)
        Edit = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Edit']"))
        )
        Edit.click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='symbol-label']"))
        ).click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Apply Coupon']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//option[normalize-space()='Select Coupon']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//option[@value='NEWC1']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary lh-p6 rounded-0 font-weight-bold ng-star-inserted']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Update']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(3)
        sharepdf =WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Share PDF']"))
        )
        sharepdf.click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//i[@class='fa fa-arrow-left']"))
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
