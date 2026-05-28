from concurrent.futures import wait
from ast import arguments
from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("After creating an appointment,create aninvoice manually")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_appt_manualinvoice1(login):
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
                    "//div[@id='actionCreate_BUS_bookList']",
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
        time.sleep(3)

        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(
            By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
        ).send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        save_button= login.find_element(By.XPATH, "//span[contains(text(),'Save')]")
        login.execute_script("arguments[0].click();", save_button)
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
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
        ).click()

        time.sleep(3)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        time.sleep(2)

        login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
        time.sleep(3)
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

        service_option_xpath = ("//div[normalize-space()='Video call Services']")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
        print("Select Service : Video call Services")
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
        note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
        note_input.click()
        login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
            "test_selenium project"
        )
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm']")
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

        time.sleep(3)

        while True:
            try:
                
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "test_confirmation_label_message_attachment")
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

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Create Invoice']")
            )
        ).click()

        time.sleep(3)
        update_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Update']")
            )
        )
        update_button.click()
        

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

        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
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

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

    time.sleep(5)

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Apply the discount in the Invoice and Share the payment link")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_appt_manualinvoice2(login):
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
                "//div[@id='actionCreate_BUS_bookList']",
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

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
    login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

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

    login.implicitly_wait(3)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

    service_option_xpath = "//div[normalize-space()='Video call Services']"
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
    ).click()
    print("Select Service : Video call Services")
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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
        "test_selenium project"
    )
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()

    login.find_element(By.XPATH, "//span[normalize-space()='Confirm']").click()
    time.sleep(4)

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

    time.sleep(1)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Create Invoice']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@aria-haspopup='menu']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mdc-list-item__primary-text'][normalize-space()='Apply Discount'])[1]")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//select[./option[text()='Select Discount']])[3]")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//option[normalize-space()='On Demand Discount'])[3]")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter Amount']")
        )
    ).send_keys("50")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Apply'])[3]")
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

    time.sleep(5)

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']"))
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

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Get Payment']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
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

    time.sleep(5)

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Add a service in the Invoice and Share the payment link")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_appt_manualinvoice3(login):
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
                "//div[@id='actionCreate_BUS_bookList']",
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

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
    login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
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

    login.implicitly_wait(3)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

    service_option_xpath = "//div[normalize-space()='Video call Services']"
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
    ).click()
    print("Select Service : Video call Services")
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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
        "test_selenium project"
    )
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()

    login.find_element(By.XPATH, "//span[normalize-space()='Confirm']").click()
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

    # Click on view details
    time.sleep(1)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Create Invoice']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Choose Procedure/Item']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='item-name'][normalize-space()='Consultation']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='cs-btn bt1 ml-0'][normalize-space()='Add']")
        )
    ).click()

    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Update']")
   
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

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Get Payment']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
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

    time.sleep(5)

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Add an item and apply the discount in the Invoice level and Share the payment link")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_appt_manualinvoice4(login):

    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]",
            )
        )
    ).click()

    # Click on + Appointment button in the appointment dashboard
    time.sleep(3)
    wait_and_locate_click(login, By.XPATH, "//div[@id='actionCreate_BUS_bookList']"
    )

    time.sleep(3)
    wait = WebDriverWait(login, 10)
    element_appoint = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//b[contains(text(),'Create New Patient')]")
        )
    )
    element_appoint.click()
    login.implicitly_wait(3)

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
    login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
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

    login.implicitly_wait(3)

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

    service_option_xpath = ("//div[normalize-space()='Video call Services']")
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
    ).click()
    print("Select Service : Video call Services")

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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
        "test_selenium project"
    )
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()

    login.find_element(By.XPATH, "//span[normalize-space()='Confirm']").click()

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

    time.sleep(5)
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

    # Click on view details
    time.sleep(1)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Create Invoice']")
        )
    ).click()

    # Locate Add Procedure/Item / Add Service/Item button
    add_item_btn = wait.until(
    EC.presence_of_element_located(
        (By.XPATH,
            "//button[contains(normalize-space(), 'Add Procedure/Item') "
            "or contains(normalize-space(), 'Add Service/Item') "
            "or .//span[contains(normalize-space(), 'Add Procedure/Item')]]")
         )
    )

    # Scroll down until the button is visible
    login.execute_script(
    "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
    add_item_btn
    )
    
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add Procedure/Item']")  

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'item-name') and normalize-space()='item3']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='cs-btn bt1 ml-0'][normalize-space()='Add']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@aria-haspopup='menu']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@role='menuitem' and contains(normalize-space(), 'Apply Discount')]")
        )
    ).click()

    # Click on the select discount dropdown in the pop up
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//select[./option[text()='Select Discount']])[3]")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//option[normalize-space()='On Demand Discount'])[3]")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter Amount']")
        )
    ).send_keys("50")

    time.sleep(3)
    wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Apply'])[3]")

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

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']"))
    ).click()

    snack_bar = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    )
    message = snack_bar.text
    print("Snack bar message:", message)

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Get Payment']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
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

    time.sleep(5)


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Add an item in the invoice and apply discount in item level and Share the payment link")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_appt_manualinvoice5(login):

    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]",
            )
        )
    ).click()

    # Click on + Appointment button in the appointment dashboard
    time.sleep(3)
    wait_and_locate_click(login, By.XPATH, "//div[@id='actionCreate_BUS_bookList']"
    )

    time.sleep(3)
    wait = WebDriverWait(login, 10)
    element_appoint = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//b[contains(text(),'Create New Patient')]")
        )
    )
    element_appoint.click()
    login.implicitly_wait(3)

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
    login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
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

    login.implicitly_wait(3)

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

    service_option_xpath = ("//div[normalize-space()='Video call Services']")
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
    ).click()
    print("Select Service : Video call Services")

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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
        "test_selenium project"
    )
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()

    login.find_element(By.XPATH, "//span[normalize-space()='Confirm']").click()

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

    time.sleep(5)
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

    # Click on view details
    time.sleep(1)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Create Invoice']")
        )
    ).click()

    # Locate Add Procedure/Item / Add Service/Item button
    add_item_btn = wait.until(
    EC.presence_of_element_located(
        (By.XPATH,
            "//button[contains(normalize-space(), 'Add Procedure/Item') "
            "or contains(normalize-space(), 'Add Service/Item') "
            "or .//span[contains(normalize-space(), 'Add Procedure/Item')]]")
         )
    )

    # Scroll down until the button is visible
    login.execute_script(
    "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
    add_item_btn
    )
    
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add Procedure/Item']")  

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'item-name') and normalize-space()='item3']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='cs-btn bt1 ml-0'][normalize-space()='Add']")
        )
    ).click()

    # Click on the three dots against the added item
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
        (By.XPATH, "//tr[.//span[normalize-space()='Item3']]//td[contains(@class,'more-class')]//button[.//mat-icon[normalize-space()='more_horiz']]"))
    ).click()


    # Select Apply Discount option from the menu
    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@role='menuitem' and .//span[normalize-space()='Apply Discount']]")
        )
    ).click()
  


    # Catch Apply Discount popup
    time.sleep(2)

    popup_xpath = "//div[contains(@class,'modal-content') and ancestor::div[contains(@class,'modal') and contains(@class,'show')]][.//h5[@id='discountModalLabel' and normalize-space()='Apply Discount']]"
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, popup_xpath))
    )


    # Locate Select Discount dropdown
    discount_dropdown = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, popup_xpath + "//select[.//option[@value='33636']]")
        )
    )


    # Select On Demand Discount
    login.execute_script("""
        arguments[0].value = '33636';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
    """, discount_dropdown)


    # Enter Amount
    time.sleep(2)

    amount_field = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, popup_xpath + "//input[@placeholder='Enter Amount']")
        )
    )

    amount_field.clear()
    amount_field.send_keys("12")

    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//div[@id='exampleModaItemDiscount']//button[@type='button'][normalize-space()='Apply']")  


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

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']"))
    ).click()

    snack_bar = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    )
    message = snack_bar.text
    print("Snack bar message:", message)

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Get Payment']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
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

    time.sleep(5)

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Add a sub service in the manual invoice")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_appt_manualinvoice6(login):
    # Add the sub service in the invoice

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
                "//div[@id='actionCreate_BUS_bookList']",
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

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
    login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

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

    login.implicitly_wait(3)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

    service_option_xpath = (
        "//div[normalize-space()='Video call Services']"
    )
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
    ).click()
    print("Select Service : Video call Services")
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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
        "test_selenium project"
    )
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()

    login.find_element(By.XPATH, "//span[normalize-space()='Confirm']").click()
    time.sleep(4)

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

    # Click on view details
    time.sleep(1)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")

    # Click on create invoice button
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Create Invoice']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    ).click()

    # Click on service/item dropdown
    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Choose Procedure/Item']")
        )
    ).click()

    # Click on the sub service to be added
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Scanning']")
        )
    ).click()

    # Click on select user dropdown
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class,'p-multiselect') and .//div[normalize-space()='Select User']]")
        )
    ).click()

    # select user from the dropdown
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[contains(@class,'p-multiselect-item') and @aria-label='Naveen']")
        )
    ).click()

    # Click on Add button to add the sub service in the invoice
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add']")
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

    time.sleep(5)

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']"))
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

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Get Payment']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
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

    time.sleep(5)

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Update the bill status to SETTLED")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_appt_manualinvoice7(login):

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
                "//div[@id='actionCreate_BUS_bookList']",
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

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
    login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
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

    login.implicitly_wait(3)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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
    # time.sleep(3)
    service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
    # WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_dropdown_xpath))).click()
    element = login.find_element(By.XPATH, service_dropdown_xpath)
    login.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    service_option_xpath = (
        "//div[normalize-space()='Video call Services']"
    )
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
    ).click()
    print("Select Service : Video call Services")
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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
        "test_selenium project"
    )
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Confirm']")
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

    time.sleep(3)

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

    # Click on view details
    time.sleep(1)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")


    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Create Invoice']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']")
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

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Settle Invoice']")
        )
    ).click()

    time.sleep(3)
    wait_and_locate_click(login, By.XPATH, "//textarea[@placeholder='Enter any notes for your future reference']")

    time.sleep(2)
    wait_and_send_keys(login, By.XPATH, "//textarea[@placeholder='Enter any notes for your future reference']", "Settling the invoice")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Confirm & Settle Invoice']"))
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

    time.sleep(5)

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Apply Fixed amount coupon in the invoice and share the payment link")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_appt_manualinvoice8(login):

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
                "//div[@id='actionCreate_BUS_bookList']",
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

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
    login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

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

    login.implicitly_wait(3)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

    service_option_xpath = (
        "//div[normalize-space()='Video call Services']"
    )
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
    ).click()
    print("Select Service : Video call Services")
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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
        "test_selenium project"
    )
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()

    login.find_element(By.XPATH, "//span[normalize-space()='Confirm']").click()
    time.sleep(4)

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

    # Click on view details
    time.sleep(1)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")


    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Create Invoice']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@aria-haspopup='menu']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[@class='mdc-list-item__primary-text'][normalize-space()='Apply Coupon']",
            )
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//option[normalize-space()='Select Coupon']")
        )
    ).click()

    dropdown_element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//option[@value='VISION']",
            )
        )
    )
    dropdown_element.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                " //button[contains(@class, 'btn btn-primary') and text()='Apply']",
            )
        )
    ).click()

    # time.sleep(3)
    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Amount']"))
    # ).send_keys("50")

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

    time.sleep(5)

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']"))
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

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Get Payment']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
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

    time.sleep(5)


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Apply percentage amount coupon and share the payment link")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_appt_manualinvoice9(login):

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
                "//div[@id='actionCreate_BUS_bookList']",
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

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
    login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

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

    login.implicitly_wait(3)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

    service_option_xpath = (
        "//div[normalize-space()='Video call Services']"
    )
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
    ).click()
    print("Select Service : Video call Services")
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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
        "test_selenium project"
    )
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()

    login.find_element(By.XPATH, "//span[normalize-space()='Confirm']").click()
    time.sleep(4)

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

    # Click on view details
    time.sleep(1)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")


    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Create Invoice']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@aria-haspopup='menu']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[@class='mdc-list-item__primary-text'][normalize-space()='Apply Coupon']",
            )
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//option[normalize-space()='Select Coupon']")
        )
    ).click()

    dropdown_element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//option[@value='SPECIAL']",
            )
        )
    )
    dropdown_element.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                " //button[contains(@class, 'btn btn-primary') and text()='Apply']",
            )
        )
    ).click()

    # time.sleep(3)
    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Amount']"))
    # ).send_keys("50")

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

    time.sleep(5)

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']"))
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

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Get Payment']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
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

    time.sleep(5)


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Update bill status as CANCELLED")    
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_appt_manualinvoice10(login):

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
                "//div[@id='actionCreate_BUS_bookList']",
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

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
    login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
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

    login.implicitly_wait(3)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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
    # time.sleep(3)
    service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
    # WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_dropdown_xpath))).click()
    element = login.find_element(By.XPATH, service_dropdown_xpath)
    login.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    service_option_xpath = (
        "//div[normalize-space()='Video call Services']"
    )
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
    ).click()
    print("Select Service : Video call Services")

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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
        "test_selenium project"
    )
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Confirm']")
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

    time.sleep(3)

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


    # Click on view details
    time.sleep(1)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")


    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Create Invoice']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']")
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

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Cancel Invoice']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Enter any notes for your future reference']"))
    ).click()

    time.sleep(1)
    wait_and_send_keys(login, By.XPATH, "//textarea[@placeholder='Enter any notes for your future reference']", "Canceling the invoice")

    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//button[@class='cs-btn btn btn-primary settle-button']") 

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

    time.sleep(5)
   
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Consumer take prepayment booking")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/visionhospital/"])
def test_prepaymentbooking(con_login):

    try:
 
        time.sleep(5)

        book_now_button = WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnBookNow']")
            )
        )
        con_login.execute_script("arguments[0].scrollIntoView();", book_now_button)

        # Wait for the element to be clickable
        clickable_book_now_button = WebDriverWait(con_login, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@id='btnBookNow']")
            )
        )

        # Attempt to click the element
        try:
            clickable_book_now_button.click()
        except:
            # If click is intercepted, click using JavaScript
            con_login.execute_script("arguments[0].click();", clickable_book_now_button)

        wait = WebDriverWait(con_login, 10)
        location_button = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='deptName ng-star-inserted'][contains(text(),'Chavakkad')]",
                )
            )
        )
        location_button.click()

        wait = WebDriverWait(con_login, 10)
        depart_button = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='deptName ng-star-inserted'][normalize-space()='ENT']",
                )
            )
        )
        depart_button.click()

        wait = WebDriverWait(con_login, 10)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Dr.Naveen KP')]")
            )
        ).click()

        WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//app-appointment-card[.//div[contains(@class,'serviceName') and normalize-space()='Naveen Consultation']]",
                )
            )
        ).click()

        time.sleep(4)
        Today_Date = WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' is-selected ')]")
            )
        )
        print("Today Date:", Today_Date.text)
        con_login.execute_script("arguments[0].click();", Today_Date)


        wait = WebDriverWait(con_login, 10)
        time_slot = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='mdc-evolution-chip__action mat-mdc-chip-action mdc-evolution-chip__action--primary mdc-evolution-chip__action--presentational'])[1]"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)

        time.sleep(2)
        clickable_next_button = WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(),'Next')]")
            )
        )

        con_login.execute_script("arguments[0].click();", clickable_next_button)

        time.sleep(2)
        WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='81234 56789'])[1]"))
        ).send_keys("8281276241")

        time.sleep(1)
        wait_and_locate_click(
            con_login, By.XPATH, "//button[@id='btnSendOTP']"
        )

        time.sleep(3)

        otp_digits = "5555"

        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(con_login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )

    
        for i, otp_input in enumerate(otp_inputs):

            # print(i)
            # print(otp_input)
            otp_input.send_keys(otp_digits[i])

        con_login.find_element(
            By.XPATH,
            "//button[@id='btnVerifyOTP']").click()
        
        time.sleep(2)
        wait_and_locate_click(
            con_login, By.XPATH, "//mat-radio-button//div[contains(text(),'NET BANKING')]"
        )

        time.sleep(2)
        wait_and_locate_click(
            con_login, By.XPATH, "//button[@id='btnConfirm']"
        )

        time.sleep(3)
        # Store main window
        main_window = con_login.current_window_handle


        # ************ PAYTM WORKFLOW *****************
        # print("Using Paytm checkout DOM")
        # # Click Net Banking option
        # netbanking = wait.until(
        #     EC.element_to_be_clickable(
        #         (By.CSS_SELECTOR, "#checkout-nb label.ptm-lbl")
        #     )
        # )

        # con_login.execute_script(
        #     "arguments[0].scrollIntoView({block: 'center'});",
        #     netbanking
        # )

        # try:
        #     netbanking.click()
        # except Exception:
        #     con_login.execute_script("arguments[0].click();", netbanking)

        # print("Netbanking selected")

        # bank_name = "Kotak"  # Options visible in HTML: HDFC, SBI, ICICI, AXIS, Kotak, Canara, PNB, IOB

        # bank = wait.until(
        #     EC.element_to_be_clickable(
        #         (
        #             By.XPATH,
        #             f"//div[@id='ptm-nb-inner']//p[contains(@class,'ptm-bank-name') and normalize-space()='{bank_name}']"
        #             "/ancestor::div[contains(@class,'ptm-nb-list-item')][1]"
        #         )
        #     )
        # )

        # con_login.execute_script(
        #     "arguments[0].scrollIntoView({block: 'center'});",
        #     bank
        # )

        # try:
        #     bank.click()
        # except Exception:
        #     con_login.execute_script("arguments[0].click();", bank)

        # print("Bank selected")
        
        # # Stay in main page DOM for Paytm checkout
        # con_login.switch_to.default_content()

        # time.sleep(2)

        # # Store main window before clicking Pay
        # main_window = con_login.current_window_handle
        # existing_windows = set(con_login.window_handles)

        # print("Main window:", main_window)

        # # Click Pay / Make Payment button
        # pay_btn = wait.until(
        #     EC.element_to_be_clickable(
        #         (
        #             By.XPATH,
        #             "//button[contains(@class,'ptm-custom-btn') and .//img[contains(@class,'ptm-lock-img')]]"
        #         )
        #     )
        # )

        # con_login.execute_script(
        #     "arguments[0].scrollIntoView({block: 'center'});",
        #     pay_btn
        # )

        # try:
        #     pay_btn.click()
        # except Exception:
        #     con_login.execute_script("arguments[0].click();", pay_btn)

        # print("Pay button clicked")

        # # Paytm may open mock bank either in same window or new window.
        # # First check if a new window opens.
        # try:
        #     wait.until(lambda d: len(d.window_handles) > len(existing_windows))

        #     new_window = list(set(con_login.window_handles) - existing_windows)[0]
        #     con_login.switch_to.window(new_window)

        #     print("Switched to Paytm mock bank window:", con_login.current_url)

        # except Exception:
        #     # If no new window opens, Paytm likely navigated in the same window
        #     print("Paytm mock bank opened in same window:", con_login.current_url)

        # # Wait for Successful button on Paytm demo bank page
        # success_btn = wait.until(
        #     EC.element_to_be_clickable(
        #         (
        #             By.XPATH,
        #             "//button[contains(@class,'btn') and .//span[normalize-space()='Successful']]"
        #         )
        #     )
        # )

        # con_login.execute_script("arguments[0].click();", success_btn)
        # time.sleep(2)
        # print("Successful button clicked")

        # # If Paytm opened a separate window, switch back to main window
        # if main_window in con_login.window_handles:
        #     con_login.switch_to.window(main_window)
        #     print("Returned to main window")

        # time.sleep(5)


         # ************ RAZORPAY WORKFLOW *****************
         
        # Switch to the iframe containing the Razorpay modal
        razorpay_iframe = WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "razorpay-checkout-frame"))
        )
        con_login.switch_to.frame(razorpay_iframe)
        print("Switched to Razorpay iframe")

        # Click on Netbanking from the Razorpay gateway
        time.sleep(2)
        wait_and_locate_click(
            con_login, By.XPATH, "//span[@data-testid='Netbanking' and normalize-space()='Netbanking']"
        )
        print("Clicked Netbanking option in Razorpay")

        # Select bank option (e.g., State Bank of India)
        bank_option = WebDriverWait(con_login, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(@class,'font-medium') and normalize-space()='Kotak Mahindra Bank']")
            )
        )
        con_login.execute_script("arguments[0].click();", bank_option)
        print("Selected bank option")


        main_window_handle = con_login.current_window_handle
        WebDriverWait(con_login, 10).until(EC.new_window_is_opened)
        all_window_handles = con_login.window_handles

        new_window_handle = None
        for handle in all_window_handles:
            if handle != main_window_handle:
                new_window_handle = handle
                break

        if new_window_handle:
            con_login.switch_to.window(new_window_handle)

            time.sleep(3)
            WebDriverWait(con_login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Success']"))
            ).click()

            con_login.switch_to.window(main_window_handle)
        
        print("success")
        time.sleep(5)


        # Click on OK button in the booking confirmation page after payment
        time.sleep(3)
        ok_button = WebDriverWait(con_login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[@id='btnOK']")
                )
            )
        con_login.execute_script("arguments[0].click();", ok_button)

        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            con_login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Payment Refund")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_appt_manualinvoice11(login):

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

     # Click on view details
    time.sleep(1)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")

    # Click on view invoice
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Invoice']")
        )
    ).click()

    # Click on Refund button in invoice
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Refund']")
        )
    ).click()

    # Click on Refund button in the pop up
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'modal-content')]//button[normalize-space()='Refund']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Pay Online']"))
    ).click()
    
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Yes']"))
    ).click()
    print("Refund successful with online payment")
    time.sleep(5)



# *********** MANUAL INVOICE WITH TAXABLE SERVICE **********

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create appointment with manual invoice having taxable service")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_appt_manualinvoice_with_taxable_service1(login):
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
                    "//div[@id='actionCreate_BUS_bookList']",
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
        time.sleep(3)

        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(
            By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
        ).send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        save_button= login.find_element(By.XPATH, "//span[contains(text(),'Save')]")
        login.execute_script("arguments[0].click();", save_button)
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
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
        ).click()

        time.sleep(3)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        time.sleep(2)

        login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
        time.sleep(3)
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

        service_option_xpath = ("//li[@role='option' and @aria-label='WhatsApp Service(Taxable)']")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
        print("Select Service : WhatsApp Service(Taxable)")
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
        note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
        note_input.click()
        login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
            "Walk-in appointment"
        )
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm']")
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

        time.sleep(3)

        while True:
            try:
                
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "test_confirmation_label_message_attachment")
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

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnCraeteInv_BUS_bookAction']")
            )
        ).click()

        time.sleep(3)
        update_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Update']")
            )
        )
        update_button.click()
        

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

        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
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

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

    time.sleep(5)   


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Apply the discount in the Invoice")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_appt_manualinvoice_with_taxable_service2(login):
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
                "//div[@id='actionCreate_BUS_bookList']",
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

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
    login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

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

    login.implicitly_wait(3)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

    service_option_xpath = "//li[@role='option' and @aria-label='WhatsApp Service(Taxable)']"
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
    ).click()
    print("Select Service : WhatsApp Service(Taxable)")
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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
        "test_selenium project"
    )
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()

    login.find_element(By.XPATH, "//span[normalize-space()='Confirm']").click()
    time.sleep(4)

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

    time.sleep(1)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@id='btnCraeteInv_BUS_bookAction']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@aria-haspopup='menu']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mdc-list-item__primary-text'][normalize-space()='Apply Discount'])[1]")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//select[./option[text()='Select Discount']])[3]")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//option[normalize-space()='On Demand Discount'])[3]")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter Amount']")
        )
    ).send_keys("50")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Apply'])[3]")
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

    time.sleep(5)

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']"))
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

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Get Payment']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
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

    time.sleep(5)


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Add a service in the Invoice and Share the payment link")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_appt_manualinvoice_with_taxable_service3(login):
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
                "//div[@id='actionCreate_BUS_bookList']",
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

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
    login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
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

    login.implicitly_wait(3)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

    service_option_xpath = "//li[@role='option' and @aria-label='WhatsApp Service(Taxable)']"
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
    ).click()
    print("Select Service : WhatsApp Service(Taxable)")
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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
        "test_selenium project"
    )
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()

    login.find_element(By.XPATH, "//span[normalize-space()='Confirm']").click()
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

    # Click on view details
    time.sleep(1)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@id='btnCraeteInv_BUS_bookAction']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Choose Procedure/Item']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='item-name'][normalize-space()='Consultation']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='cs-btn bt1 ml-0'][normalize-space()='Add']")
        )
    ).click()

    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Update']")
   
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

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Get Payment']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
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

    time.sleep(5)


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Add an item and apply the discount in the Invoice level and Share the payment link")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_appt_manualinvoice_with_taxable_service4(login):

    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]",
            )
        )
    ).click()

    # Click on + Appointment button in the appointment dashboard
    time.sleep(3)
    wait_and_locate_click(login, By.XPATH, "//div[@id='actionCreate_BUS_bookList']"
    )

    time.sleep(3)
    wait = WebDriverWait(login, 10)
    element_appoint = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//b[contains(text(),'Create New Patient')]")
        )
    )
    element_appoint.click()
    login.implicitly_wait(3)

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
    login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
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

    login.implicitly_wait(3)

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

    service_option_xpath = ("//li[@role='option' and @aria-label='WhatsApp Service(Taxable)']")
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
    ).click()
    print("Select Service : WhatsApp Service(Taxable)")

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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
        "test_selenium project"
    )
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()

    login.find_element(By.XPATH, "//span[normalize-space()='Confirm']").click()

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

    time.sleep(5)
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

    # Click on view details
    time.sleep(1)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@id='btnCraeteInv_BUS_bookAction']")
        )
    ).click()

    # Locate Add Procedure/Item / Add Service/Item button
    add_item_btn = wait.until(
    EC.presence_of_element_located(
        (By.XPATH,
            "//button[contains(normalize-space(), 'Add Procedure/Item') "
            "or contains(normalize-space(), 'Add Service/Item') "
            "or .//span[contains(normalize-space(), 'Add Procedure/Item')]]")
         )
    )

    # Scroll down until the button is visible
    login.execute_script(
    "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
    add_item_btn
    )
    
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add Procedure/Item']")  

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'item3')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='cs-btn bt1 ml-0'][normalize-space()='Add']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@aria-haspopup='menu']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@role='menuitem' and contains(normalize-space(), 'Apply Discount')]")
        )
    ).click()

    # Click on the select discount dropdown in the pop up
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//select[./option[text()='Select Discount']])[3]")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//option[normalize-space()='On Demand Discount'])[3]")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter Amount']")
        )
    ).send_keys("50")

    time.sleep(3)
    wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Apply'])[3]")

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

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']"))
    ).click()

    snack_bar = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    )
    message = snack_bar.text
    print("Snack bar message:", message)

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Get Payment']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
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

    time.sleep(5)



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Add an item in the invoice and apply discount in item level and Share the payment link")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_appt_manualinvoice_with_taxable_service5(login):

    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]",
            )
        )
    ).click()

    # Click on + Appointment button in the appointment dashboard
    time.sleep(3)
    wait_and_locate_click(login, By.XPATH, "//div[@id='actionCreate_BUS_bookList']"
    )

    time.sleep(3)
    wait = WebDriverWait(login, 10)
    element_appoint = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//b[contains(text(),'Create New Patient')]")
        )
    )
    element_appoint.click()
    login.implicitly_wait(3)

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
    login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
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

    login.implicitly_wait(3)

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

    service_option_xpath = ("//li[@role='option' and @aria-label='WhatsApp Service(Taxable)']")
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
    ).click()
    print("Select Service : WhatsApp Service(Taxable)")

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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
        "test_selenium project"
    )
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()

    login.find_element(By.XPATH, "//span[normalize-space()='Confirm']").click()

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

    time.sleep(5)
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

    # Click on view details
    time.sleep(1)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Create Invoice']")
        )
    ).click()

    # Locate Add Procedure/Item / Add Service/Item button
    add_item_btn = wait.until(
    EC.presence_of_element_located(
        (By.XPATH,
            "//button[contains(normalize-space(), 'Add Procedure/Item') "
            "or contains(normalize-space(), 'Add Service/Item') "
            "or .//span[contains(normalize-space(), 'Add Procedure/Item')]]")
         )
    )

    # Scroll down until the button is visible
    login.execute_script(
    "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
    add_item_btn
    )
    
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add Procedure/Item']")  

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'item-name') and normalize-space()='item3']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='cs-btn bt1 ml-0'][normalize-space()='Add']")
        )
    ).click()

    # Click on the three dots against the added item
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
        (By.XPATH, "//tr[.//span[normalize-space()='Item3']]//td[contains(@class,'more-class')]//button[.//mat-icon[normalize-space()='more_horiz']]"))
    ).click()


    # Select Apply Discount option from the menu
    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@role='menuitem' and .//span[normalize-space()='Apply Discount']]")
        )
    ).click()
  


    # Catch Apply Discount popup
    time.sleep(2)

    popup_xpath = "//div[contains(@class,'modal-content') and ancestor::div[contains(@class,'modal') and contains(@class,'show')]][.//h5[@id='discountModalLabel' and normalize-space()='Apply Discount']]"
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, popup_xpath))
    )


    # Locate Select Discount dropdown
    discount_dropdown = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, popup_xpath + "//select[.//option[@value='33636']]")
        )
    )


    # Select On Demand Discount
    login.execute_script("""
        arguments[0].value = '33636';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
    """, discount_dropdown)


    # Enter Amount
    time.sleep(2)

    amount_field = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, popup_xpath + "//input[@placeholder='Enter Amount']")
        )
    )

    amount_field.clear()
    amount_field.send_keys("12")

    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//div[@id='exampleModaItemDiscount']//button[@type='button'][normalize-space()='Apply']")  


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

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']"))
    ).click()

    snack_bar = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    )
    message = snack_bar.text
    print("Snack bar message:", message)

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Get Payment']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
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

    time.sleep(5)



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Add a sub service in the manual invoice")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_appt_manualinvoice_with_taxable_service6(login):
    # Add the sub service in the invoice

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
                "//div[@id='actionCreate_BUS_bookList']",
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

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
    login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

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

    login.implicitly_wait(3)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

    service_option_xpath = (
        "//li[@role='option' and @aria-label='WhatsApp Service(Taxable)']"
    )
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
    ).click()
    print("Select Service : WhatsApp Service(Taxable)")

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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
        "test_selenium project"
    )
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()

    login.find_element(By.XPATH, "//span[normalize-space()='Confirm']").click()
    time.sleep(4)

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

    # Click on view details
    time.sleep(1)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")

    # Click on create invoice button
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Create Invoice']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    ).click()

    # Click on service/item dropdown
    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Choose Procedure/Item']")
        )
    ).click()

    # Click on the sub service to be added
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Scanning']")
        )
    ).click()

    # Click on select user dropdown
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class,'p-multiselect') and .//div[normalize-space()='Select User']]")
        )
    ).click()

    # select user from the dropdown
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[contains(@class,'p-multiselect-item') and @aria-label='Naveen']")
        )
    ).click()

    # Click on Add button to add the sub service in the invoice
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add']")
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

    time.sleep(5)

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']"))
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

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Get Payment']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
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

    time.sleep(5)



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Apply Fixed amount coupon in the invoice and share the payment link")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_appt_manualinvoice_with_taxable_service7(login):

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
                "//div[@id='actionCreate_BUS_bookList']",
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

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
    login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

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

    login.implicitly_wait(3)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

    service_option_xpath = (
        "//li[@role='option' and @aria-label='WhatsApp Service(Taxable)']"
    )
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
    ).click()
    print("Select Service : WhatsApp Service(Taxable)")
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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
        "test_selenium project"
    )
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()

    login.find_element(By.XPATH, "//span[normalize-space()='Confirm']").click()
    time.sleep(4)

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

    # Click on view details
    time.sleep(1)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")


    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Create Invoice']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@aria-haspopup='menu']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[@class='mdc-list-item__primary-text'][normalize-space()='Apply Coupon']",
            )
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//option[normalize-space()='Select Coupon']")
        )
    ).click()

    dropdown_element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//option[@value='VISION']",
            )
        )
    )
    dropdown_element.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                " //button[contains(@class, 'btn btn-primary') and text()='Apply']",
            )
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

    time.sleep(5)

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']"))
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

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Get Payment']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
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

    time.sleep(5)



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Apply percentage amount coupon and share the payment link")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_appt_manualinvoice_with_taxable_service8(login):

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
                "//div[@id='actionCreate_BUS_bookList']",
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

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
    login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

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

    login.implicitly_wait(3)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

    service_option_xpath = (
        "//li[@role='option' and @aria-label='WhatsApp Service(Taxable)']"
    )
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
    ).click()
    print("Select Service : WhatsApp Service(Taxable)")

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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
        "test_selenium project"
    )
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()

    login.find_element(By.XPATH, "//span[normalize-space()='Confirm']").click()
    time.sleep(4)

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

    # Click on view details
    time.sleep(1)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")


    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Create Invoice']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@aria-haspopup='menu']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[@class='mdc-list-item__primary-text'][normalize-space()='Apply Coupon']",
            )
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//option[normalize-space()='Select Coupon']")
        )
    ).click()

    dropdown_element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//option[@value='SPECIAL']",
            )
        )
    )
    dropdown_element.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                " //button[contains(@class, 'btn btn-primary') and text()='Apply']",
            )
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

    time.sleep(5)

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']"))
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

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Get Payment']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
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

    time.sleep(5)



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Consumer take prepayment booking")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/visionhospital/"])
def test_prepaymentbooking_with_taxable_service(con_login):

    try:
 
        time.sleep(5)

        book_now_button = WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnBookNow']")
            )
        )
        con_login.execute_script("arguments[0].scrollIntoView();", book_now_button)

        # Wait for the element to be clickable
        clickable_book_now_button = WebDriverWait(con_login, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@id='btnBookNow']")
            )
        )

        # Attempt to click the element
        try:
            clickable_book_now_button.click()
        except:
            # If click is intercepted, click using JavaScript
            con_login.execute_script("arguments[0].click();", clickable_book_now_button)

        wait = WebDriverWait(con_login, 10)
        location_button = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='deptName ng-star-inserted'][contains(text(),'Chavakkad')]",
                )
            )
        )
        location_button.click()

        wait = WebDriverWait(con_login, 10)
        depart_button = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='deptName ng-star-inserted'][normalize-space()='ENT']",
                )
            )
        )
        depart_button.click()

        wait = WebDriverWait(con_login, 10)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Dr.Naveen KP')]")
            )
        ).click()

        WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//app-appointment-card[.//div[contains(@class,'serviceName') and normalize-space()='WhatsApp Service(Taxable)']]",
                )
            )
        ).click()

        time.sleep(4)
        Today_Date = WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' is-selected ')]")
            )
        )
        print("Today Date:", Today_Date.text)
        con_login.execute_script("arguments[0].click();", Today_Date)


        wait = WebDriverWait(con_login, 10)
        time_slot = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='mdc-evolution-chip__action mat-mdc-chip-action mdc-evolution-chip__action--primary mdc-evolution-chip__action--presentational'])[1]"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)

        time.sleep(2)
        clickable_next_button = WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(),'Next')]")
            )
        )

        con_login.execute_script("arguments[0].click();", clickable_next_button)

        time.sleep(2)
        WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='81234 56789'])[1]"))
        ).send_keys("8281276241")

        time.sleep(1)
        wait_and_locate_click(
            con_login, By.XPATH, "//button[@id='btnSendOTP']"
        )

        time.sleep(3)

        otp_digits = "5555"

        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(con_login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )

    
        for i, otp_input in enumerate(otp_inputs):

            # print(i)
            # print(otp_input)
            otp_input.send_keys(otp_digits[i])

        con_login.find_element(
            By.XPATH,
            "//button[@id='btnVerifyOTP']").click()
        
        time.sleep(2)
        wait_and_locate_click(
            con_login, By.XPATH, "//mat-radio-button//div[contains(text(),'NET BANKING')]"
        )

        time.sleep(2)
        wait_and_locate_click(
            con_login, By.XPATH, "//button[@id='btnConfirm']"
        )

        time.sleep(3)
        # Store main window
        main_window = con_login.current_window_handle


        # ************ PAYTM WORKFLOW *****************
        # print("Using Paytm checkout DOM")
        # # Click Net Banking option
        # netbanking = wait.until(
        #     EC.element_to_be_clickable(
        #         (By.CSS_SELECTOR, "#checkout-nb label.ptm-lbl")
        #     )
        # )

        # con_login.execute_script(
        #     "arguments[0].scrollIntoView({block: 'center'});",
        #     netbanking
        # )

        # try:
        #     netbanking.click()
        # except Exception:
        #     con_login.execute_script("arguments[0].click();", netbanking)

        # print("Netbanking selected")

        # bank_name = "Kotak"  # Options visible in HTML: HDFC, SBI, ICICI, AXIS, Kotak, Canara, PNB, IOB

        # bank = wait.until(
        #     EC.element_to_be_clickable(
        #         (
        #             By.XPATH,
        #             f"//div[@id='ptm-nb-inner']//p[contains(@class,'ptm-bank-name') and normalize-space()='{bank_name}']"
        #             "/ancestor::div[contains(@class,'ptm-nb-list-item')][1]"
        #         )
        #     )
        # )

        # con_login.execute_script(
        #     "arguments[0].scrollIntoView({block: 'center'});",
        #     bank
        # )

        # try:
        #     bank.click()
        # except Exception:
        #     con_login.execute_script("arguments[0].click();", bank)

        # print("Bank selected")
        
        # # Stay in main page DOM for Paytm checkout
        # con_login.switch_to.default_content()

        # time.sleep(2)

        # # Store main window before clicking Pay
        # main_window = con_login.current_window_handle
        # existing_windows = set(con_login.window_handles)

        # print("Main window:", main_window)

        # # Click Pay / Make Payment button
        # pay_btn = wait.until(
        #     EC.element_to_be_clickable(
        #         (
        #             By.XPATH,
        #             "//button[contains(@class,'ptm-custom-btn') and .//img[contains(@class,'ptm-lock-img')]]"
        #         )
        #     )
        # )

        # con_login.execute_script(
        #     "arguments[0].scrollIntoView({block: 'center'});",
        #     pay_btn
        # )

        # try:
        #     pay_btn.click()
        # except Exception:
        #     con_login.execute_script("arguments[0].click();", pay_btn)

        # print("Pay button clicked")

        # # Paytm may open mock bank either in same window or new window.
        # # First check if a new window opens.
        # try:
        #     wait.until(lambda d: len(d.window_handles) > len(existing_windows))

        #     new_window = list(set(con_login.window_handles) - existing_windows)[0]
        #     con_login.switch_to.window(new_window)

        #     print("Switched to Paytm mock bank window:", con_login.current_url)

        # except Exception:
        #     # If no new window opens, Paytm likely navigated in the same window
        #     print("Paytm mock bank opened in same window:", con_login.current_url)

        # # Wait for Successful button on Paytm demo bank page
        # success_btn = wait.until(
        #     EC.element_to_be_clickable(
        #         (
        #             By.XPATH,
        #             "//button[contains(@class,'btn') and .//span[normalize-space()='Successful']]"
        #         )
        #     )
        # )

        # con_login.execute_script("arguments[0].click();", success_btn)
        # time.sleep(2)
        # print("Successful button clicked")

        # # If Paytm opened a separate window, switch back to main window
        # if main_window in con_login.window_handles:
        #     con_login.switch_to.window(main_window)
        #     print("Returned to main window")

        # time.sleep(5)


         # ************ RAZORPAY WORKFLOW *****************
         
        # Switch to the iframe containing the Razorpay modal
        razorpay_iframe = WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "razorpay-checkout-frame"))
        )
        con_login.switch_to.frame(razorpay_iframe)
        print("Switched to Razorpay iframe")

        # Click on Netbanking from the Razorpay gateway
        time.sleep(2)
        wait_and_locate_click(
            con_login, By.XPATH, "//span[@data-testid='Netbanking' and normalize-space()='Netbanking']"
        )
        print("Clicked Netbanking option in Razorpay")

        # Select bank option (e.g., State Bank of India)
        bank_option = WebDriverWait(con_login, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(@class,'font-medium') and normalize-space()='Kotak Mahindra Bank']")
            )
        )
        con_login.execute_script("arguments[0].click();", bank_option)
        print("Selected bank option")


        main_window_handle = con_login.current_window_handle
        WebDriverWait(con_login, 10).until(EC.new_window_is_opened)
        all_window_handles = con_login.window_handles

        new_window_handle = None
        for handle in all_window_handles:
            if handle != main_window_handle:
                new_window_handle = handle
                break

        if new_window_handle:
            con_login.switch_to.window(new_window_handle)

            time.sleep(3)
            WebDriverWait(con_login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Success']"))
            ).click()

            con_login.switch_to.window(main_window_handle)
        
        print("success")
        time.sleep(5)


        # Click on OK button in the booking confirmation page after payment
        time.sleep(3)
        ok_button = WebDriverWait(con_login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[@id='btnOK']")
                )
            )
        con_login.execute_script("arguments[0].click();", ok_button)

        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            con_login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Payment Refund")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_prepayment_refund_of_taxable_service(login):

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

     # Click on view details
    time.sleep(1)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")

    # Click on create invoice
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@id='btnCraeteInv_BUS_bookAction']")
        )
    ).click()

    time.sleep(2)
     # Locate Update button
    update_button = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']")
        )
    )

    # Scroll down until Update button is visible
    login.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        update_button
    )

    time.sleep(2)

    # Click on Update button in invoice
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']")
        )
    ).click()

    msg = get_snack_bar_message(login)
    print("Sanck Bar Message :", msg)

    # Click on Refund button in invoice
    time.sleep(4)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Refund']")
        )
    ).click()

    # Click on Refund button in the pop up
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'modal-content')]//button[normalize-space()='Refund']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Pay Online']"))
    ).click()
    
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Yes']"))
    ).click()
    print("Refund successful with online payment")
    time.sleep(5)



