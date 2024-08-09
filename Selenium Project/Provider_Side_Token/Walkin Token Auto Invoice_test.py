from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.common import TimeoutException,JavascriptException
from selenium.webdriver.support.ui import Select
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_token_viewinvoice(login):
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
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 140']"))
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
        startbutton = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Start']"))
        )
        startbutton.click()
        print("Token status changed to Started ")
        time.sleep(5)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))

        )
        last_element_in_accordian.click()
        time.sleep(3)
        completebutton = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Complete']"))
        )
        completebutton.click()
        time.sleep(5)
        completed = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
        )
        completed.click()
        print("Token status changed to Completed")
        time.sleep(3)
        completed_checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@type='checkbox'])[3]"))
        )
        completed_checkbox.click()
        print("Completed Tab is clicked")
        time.sleep(5)
        activetab_unclicked = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@type='checkbox'])[2]"))
        )
        activetab_unclicked.click()
        print("Active Tab is Unclicked")
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
        print("Recent booking element clicked")
        # ***********Autoinvoice and sharepayment link*******************
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Invoice']"))
        ).click()
        time.sleep(3)
        print("Clicked view invoice")
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder "
                                                    "ng-star-inserted']"))
        ).click()
        time.sleep(3)
        print("Clicked Get payment")
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Share Payment Link']"))
        ).click()
        time.sleep(3)
        send_payment = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='cs-btn bt1 btn btn-primary mdc-button mat-mdc-button "
                                                "mat-unthemed mat-mdc-button-base']"))
        )
        send_payment.click()
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
        time.sleep(3)
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
        time.sleep(3)
        # *****viewinvoice in the details page and cancel the invoice*****
        viewinvoice = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Invoice']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", viewinvoice)
        viewinvoice.click()
        print("viewinvoice clicked")
        time.sleep(3)
        WebDriverWait(login, 10).until(
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
def test_token_autoinvoice_print(login):
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
        # WebDriverWait(login, 20).until(
        #     EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Token']"))
        # ).click()
        # time.sleep(5)
        # lucenesearch = login.find_element(By.XPATH, "//input[@placeholder='Enter name or phone or id']"
        #                                 )
        # lucenesearch.send_keys("5550008854")
        # time.sleep(5)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 105']"))
        # ).click()
        # time.sleep(5)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Select Location']"))
        # ).click()
        # dropdownelement = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel='place']"))
        # )
        # dropdownelement.click()
        # time.sleep(5)
        # droplocation = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Ashok Nagar']"))
        # )
        # droplocation.click()
        # print("Select Location:", droplocation.text)
        # userelement = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "(//div[@class='mt-2 col-lg-8 col-xxl-6'])[2]"))
        # )
        # userelement.click()
        # time.sleep(3)
        # dropgeneralservice = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//li[@aria-label='General Services']"))
        # )
        # dropgeneralservice.click()
        # print("Select User:", dropgeneralservice.text)
        # assignto = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//p-dropdown[@optionlabel='fullName']//div[@class='text-left p-dropdown p-component']"))
        # )
        # assignto.click()
        # time.sleep(3)
        # assigntounassigneduser = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//li[@id='p-highlighted-option']"))
        # )
        # assigntounassigneduser.click()
        # print("Assignto:", assigntounassigneduser.text)
        # consultation = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//p-dropdown[@optionlabel='name']//div[@class='text-left p-dropdown p-component']"))
        # )
        # consultation.click()
        # time.sleep(3)
        # dropconsultation = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//li[@aria-label='Consultation']"))
        # )
        # dropconsultation.click()
        # print("Select service:", dropconsultation.text)
        # time.sleep(3)
        # # today = datetime.date.today()
        # today_xpath = ("//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected "
        #             "mat-calendar-body-today']")
        # # today_xpath = "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected']"
        # today_element = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, today_xpath))
        # )
        # today_element.click()
        # print("Today's Date:", today_element.text)
        # queueelement = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//div[@class='col-lg-12 col-xxl-12 p-2']//div[@class='p-inputgroup']"))
        # )
        # queueelement.click()
        # time.sleep(3)
        # dropqueue = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//li[@class='p-ripple p-element p-dropdown-item p-highlight']["
        #                                             "@id='p-highlighted-option']"))
        # )
        # dropqueue.click()
        # print("Selected Queue", dropqueue.text)
        # time.sleep(3)
        # confirmed = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm']"))
        # )
        # confirmed.click()
        # try:
        #     snack_bar = WebDriverWait(login, 20).until(
        #         EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        #     )
        #     print("Snackbar Message :", snack_bar.text)
        # except TimeoutException:
        #     try:
        #         snackbarerror = WebDriverWait(login, 10).until(
        #             EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
        #         )
        #         print("Snackbar Message : ", snackbarerror.text)
        #         cancelbutton = WebDriverWait(login, 10).until(
        #             EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']"))
        #         )
        #         cancelbutton.click()
        #     except TimeoutException:
        #         cancelbutton = WebDriverWait(login, 10).until(
        #             EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']"))
        #         )
        #         cancelbutton.click()
        #         print("Cancelled Successfully")
        #     time.sleep(1)
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
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='View Invoice']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Print']"))
        ).click()
        time.sleep(3)
        try:
            dropdown_script = """
                return document.querySelector('print-preview-app').shadowRoot
                    .querySelector('print-preview-sidebar').shadowRoot
                    .querySelector('print-preview-destination-settings').shadowRoot
                    .querySelector('print-preview-destination-select').shadowRoot
                    .querySelector('select.md-select');
                """
            dropdown = login.execute_script(dropdown_script)
            select = Select(dropdown)
            select.select_by_visible_text("Save as PDF")
            time.sleep(3)
        except JavascriptException as e:
            login.switch_to.window(login.window_handles[0])
    except Exception as e:
            allure.attach(  # use Allure package, .attach() method, pass 3 params
                login.get_screenshot_as_png(),  # param1
                # login.screenshot()
                name="full_page",  # param2
                attachment_type=AttachmentType.PNG,
            )
            raise e   
        