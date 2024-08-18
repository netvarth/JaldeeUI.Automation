from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.common import TimeoutException,JavascriptException
from selenium.webdriver.support.ui import Select
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])

####autoinvoice and share payment link in the dashboard and auto invoice from details page and cancel the invoice ####
def test_token_autoinvoice(login):
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
        # *****autoinvoice in the view details page and cancel the invoice*****
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
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//button[@class='view-bookings-btn'][normalize-space()='View'])[1]"))
        # ).click()
        # time.sleep(3)
        window_before = login.window_handles[0]
        print(f"Original window handle: {window_before}")
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Print']"))
        ).click()
        # login.execute_script('''window.open('{}');'''.format("about:blank"))
        # window_after = login.window_handles[1]
        # print(f"New window handle: {window_after}")
        # login.switch_to.window(window_after)
        # print(f"Switched to new window handle: {window_after}")
        try:
            # Wait for the new window to be available
            # WebDriverWait(login, 10).until(EC.number_of_windows_to_be(2))

            # Switch to the new window
            # for window_handle in login.window_handles:
            #     if window_handle != window_before:
            #         window_after = window_handle
            #         login.switch_to.window(window_after)
            #         break

            # print(f"New window handle: {window_after}")
            # Find and interact with the print preview app element
            pyautogui.hotkey('ctrl', 'tab')
            print('next tab')


            # window_after = login.switch_to.window(login.window_handles[1])
            # print(f"New window handle: {window_after}")
            # WebDriverWait(login, 20).until(
            #     EC.presence_of_element_located((By.CSS_SELECTOR, 'print-preview-app'))
            # ).click()             

            # dropdown_script = """
            #     return document.querySelector('print-preview-app').shadowRoot
            #         .querySelector('print-preview-sidebar').shadowRoot
            #         .querySelector('print-preview-destination-settings').shadowRoot
            #         .querySelector('print-preview-destination-select').shadowRoot
            #         .querySelector('select.md-select');
            #     """
            # print(dropdown_script)
            # dropdown = login.execute_script(dropdown_script)
            # select = Select(dropdown)
            # select.select_by_visible_text("Save as PDF")
            # time.sleep(3)
            # save_button_script = """
            #     return document.querySelector('print-preview-app').shadowRoot
            #     .querySelector('print-preview-sidebar').shadowRoot
            #     .querySelector('print-preview-button-strip').shadowRoot
            #     .querySelector('cr-button.action-button').click();
            #     """
            # login.execute_script(save_button_script)
            # time.sleep(3)
            pyautogui.click()
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(3)
            # Example for locating and clicking a button by image
# print_button_location = pyautogui.locateCenterOnScreen('print_button_image.png')
# if print_button_location:
#     pyautogui.click(print_button_location)
# else:
#     print("Print button not found!")
        except JavascriptException as e:
            login.switch_to.window(login.window_handles[0])
            print('element not found')

        # finally:
        #     # Switch back to the original window
        #     login.switch_to.window(window_before)
        #     print(f"Switched back to original window handle: {window_before}")
    except Exception as e:
            allure.attach(  # use Allure package, .attach() method, pass 3 params
                login.get_screenshot_as_png(),  # param1
                # login.screenshot()
                name="full_page",  # param2
                attachment_type=AttachmentType.PNG,
            )
            raise e   
    
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])   
def test_token_autoinvoice_paybycash_settled(login):
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
        print("Recent booking element clicked")
        # ***********Autoinvoice and paybycash and settled invoice*******************
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
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Pay by Cash']"))
        ).click()
        time.sleep(3)
        paybycash = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Pay']"))
        )
        paybycash.click()
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Yes']"))
        ).click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        settledinvoice = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Settle Invoice']"))
        )
        settledinvoice.click()
        sendnotes = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Enter any notes for your future reference']"))
        )
        sendnotes.send_keys("Settled invoice after pay by cash")
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
        ).click()
        time.sleep(3)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-arrow-left']"))
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
def test_token_autoinvoice_paybyothers_cancel(login):
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
        print("Recent booking element clicked")
        # ***********Autoinvoice and paybycash and settled invoice*******************
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
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Pay by Others']"))
        ).click()
        time.sleep(3)
        paybycash = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Pay']"))
        )
        paybycash.click()
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Yes']"))
        ).click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        settledinvoice = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel Invoice']"))
        )
        settledinvoice.click()
        sendnotes = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Enter any notes for your future reference']"))
        )
        sendnotes.send_keys("Cancelled invoice after pay by other method")
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
        ).click()
        time.sleep(3)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-arrow-left']"))
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
def test_token_autoinvoice_sharedpdf(login):
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
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))

        )
        last_element_in_accordian.click()
        time.sleep(5)
        login.execute_script("arguments[0].scrollIntoView(true);", last_element_in_accordian)
        print("Accordion expanded")
        print("Recent booking element clicked")
        # ***********Autoinvoice shared invoice*******************
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Invoice']"))
        ).click()
        time.sleep(3)
        print("Clicked view invoice")
        sharepdf =WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Share PDF']"))
        )
        sharepdf.click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-arrow-left']"))
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

# ######### Edit and add adhoc item in the invoice  
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])   
def test_token_autoinvoice_edit(login):
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
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))

        )
        last_element_in_accordian.click()
        time.sleep(5)
        login.execute_script("arguments[0].scrollIntoView(true);", last_element_in_accordian)
        print("Accordion expanded")
        print("Recent booking element clicked")
        # ***********Autoinvoice shared invoice*******************
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Invoice']"))
        ).click()
        time.sleep(3)
        print("Clicked view invoice")
        edit =WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Edit']"))
        )
        edit.click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='symbol-label']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Add Procedure/']"))
        ).click()
        time.sleep(3)
        adhocitem = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Choose Procedure/Item']"))
        )
        adhocitem.click()
        time.sleep(3)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        adhocitem.send_keys(random_string)
        adhocitem.send_keys(Keys.TAB)
        adhocitemqty = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-input-4'])[1]"))
        )
        adhocitemqty.click()
        time.sleep(3)
        adhocitemqty.send_keys(Keys.TAB)
        adhocitemprice = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-input-4'])[2]"))
        )
        adhocitemprice.click()
        adhocitemprice.clear()
        adhocitemprice.send_keys("500")
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Update']"))
        ).click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-arrow-left']"))
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
    

    


        