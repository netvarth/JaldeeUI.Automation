from Framework.common_utils import *
from Framework.common_dates_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Followup for Sameday")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_followup_sameday(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//img)[3]",
            )
        )
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@id='actionCreate_BUS_bookList'])[1]",
            )
        )
    )
    element.click()
    time.sleep(3)
    wait = WebDriverWait(login, 10)
    element_appoint = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='btnCreateCust_BUS_appt']")
        )
    )
    element_appoint.click()
    login.implicitly_wait(3)
    first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
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

    service_option_xpath = ("//li[@aria-label='Naveen Consultation']//div[1]")
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
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
    note_input = login.find_element(By.XPATH, "//a[normalize-space()='Notes']")
    note_input.click()
    wait_and_send_keys(login, By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']", "Note for the patient")

    wait_and_locate_click(login, By.XPATH, "//button[@id='btnSave_BUS_addNote']")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[@id='actnImg_BUS_notAttch']")
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

    time.sleep(3)

    time.sleep(3)
    wait_and_locate_click(login, By.XPATH, "(//button[@id='btnConfirm_BUS_apptForm'])[1]")
    message = get_snack_bar_message(login)
    print("Snack bar message:", message)

    time.sleep(3)

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
    View_Detail_button = WebDriverWait(login, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")
            )
        )
    View_Detail_button.click()

    time.sleep(3)
    wait_and_locate_click(login, By.XPATH, "//*[@id='btnFollowp_BUS_bookAction']")

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
    login.find_element(By.XPATH, "//*[@id='actnAddNote_BUS_notAttch']").click()
    wait_and_send_keys(login, By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']", "Note for the patient")

    login.find_element(By.XPATH, "//span[normalize-space()='Save']").click()
    uploadfile = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Upload File']")
        )
    )
    uploadfile.click()
    time.sleep(3)
    # Get the current working directory
    current_working_directory = os.getcwd()

    # Construct the absolute path
    absolute_path = os.path.abspath(
        os.path.join(current_working_directory, r"Extras\prescription.pdf")
    )
    pyautogui.write(absolute_path)
    pyautogui.press("enter")
    time.sleep(3)
    uploadfileaccordion = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[contains(text(),'Files selected')]")
        )
    )
    uploadfileaccordion.click()
    print("Uploaded File Successfully")
    time.sleep(3)
    # WebDriverWait(login, 10).until(
    #     EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()
    # WebDriverWait(login, 10).until(
    #     EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Confirm']"))).click()
    time.sleep(3)
    login.find_element(By.XPATH, "//span[normalize-space()='Confirm']").click()
    print("Followup Complete Successful")

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Followup for nextday")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_followup_nextday(login):

    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//img)[3]",
            )
        )
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@id='actionCreate_BUS_bookList'])[1]",
            )
        )
    )
    element.click()
    time.sleep(3)
    wait = WebDriverWait(login, 10)
    element_appoint = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='btnCreateCust_BUS_appt']")
        )
    )
    element_appoint.click()
    login.implicitly_wait(3)
    first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
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
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
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

    time.sleep(3)
    wait_and_locate_click(login, By.XPATH, "(//button[@id='btnConfirm_BUS_apptForm'])[1]")
    message = get_snack_bar_message(login)
    print("Snack bar message:", message)

    time.sleep(2)
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
    time.sleep(2)
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

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Follow Up']")
        )
    ).click()

    today_date = datetime.now()
    print(today_date.day)
    today_xpath_expression = "//span[@class='mat-calendar-body-cell-content mat-focus-indicator'][normalize-space()='{}']".format(
        today_date.day
    )
    print(today_xpath_expression)
    tomorrow_date = today_date + timedelta(days=1)
    print(tomorrow_date.day)
    tomorrow_xpath_expression = "//span[@class='mat-calendar-body-cell-content mat-focus-indicator'][normalize-space()='{}']".format(
        tomorrow_date.day
    )
    print(tomorrow_xpath_expression)

    time.sleep(3)
    Tomorrow_Date = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, tomorrow_xpath_expression))
    )
    Tomorrow_Date.click()
    print("Tomorrow Date:", Tomorrow_Date.text)

    wait = WebDriverWait(login, 10)
    time_slot = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected= 'false']"))
    )
    time_slot.click()
    print("Time Slot:", time_slot.text)
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
        os.path.join(current_working_directory, r"Extras\prescription.pdf")
    )
    pyautogui.write(absolute_path)
    pyautogui.press("enter")

    time.sleep(4)

    time.sleep(3)
    wait_and_locate_click(login, By.XPATH, "(//button[@id='btnConfirm_BUS_apptForm'])[1]")
    message = get_snack_bar_message(login)
    print("Snack bar message:", message)

    time.sleep(5)

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Followup for 180day")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_followup_180day(login):

    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//img)[3]",
            )
        )
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//div[@id='actionCreate_BUS_bookList'])[1]",
            )
        )
    )
    element.click()
    time.sleep(3)
    wait = WebDriverWait(login, 10)
    element_appoint = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='btnCreateCust_BUS_appt']")
        )
    )
    element_appoint.click()
    login.implicitly_wait(3)
    first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
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

    service_option_xpath = ("//li[@aria-label='Naveen Consultation']//div[1]")
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
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
    note_input = login.find_element(By.XPATH, "//a[normalize-space()='Notes']")
    note_input.click()
    wait_and_send_keys(login, By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']", "Note for the patient")

    wait_and_locate_click(login, By.XPATH, "//button[@id='btnSave_BUS_addNote']")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[@id='actnImg_BUS_notAttch']")
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

    time.sleep(3)

    time.sleep(3)
    wait_and_locate_click(login, By.XPATH, "(//button[@id='btnConfirm_BUS_apptForm'])[1]")
    message = get_snack_bar_message(login)
    print("Snack bar message:", message)

    time.sleep(3)

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
    View_Detail_button = WebDriverWait(login, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")
            )
        )
    View_Detail_button.click()

    time.sleep(3)
    wait_and_locate_click(login, By.XPATH, "//*[@id='btnFollowp_BUS_bookAction']")


    time.sleep(5)

    element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-label='Choose month and year']")
        )
    )
    login.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()

    [year, month, day] = add_days(180)
    print(month, year)
    year_xpath = f"//span[normalize-space()='{year}']"
    print(year_xpath)
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, year_xpath))
    ).click()
    time.sleep(2)
    month_xpath = f"//span[normalize-space()='{month.upper()}']"
    print(month_xpath)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, month_xpath))
    ).click()
    time.sleep(2)
    day_xpath = (
        f"//span[normalize-space()='{int(day)}' and not(contains(@class,'p-disabled'))]"
    )
    print(day_xpath)
    time.sleep(2)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, day_xpath))
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

        time.sleep(5)

@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_followup_history(login):

    time.sleep(5)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Appointments']")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-pristine ng-valid']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']",
            )
        )
    ).click()

    login.find_element(By.XPATH, "//span[normalize-space()='History']").click()

    time.sleep(4)


  #locate and click the last accordion
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

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Follow Up']")
        )
    ).click()

    time.sleep(5)

    element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-label='Choose month and year']")
        )
    )
    login.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()

    [year, month, day] = add_days(180)
    print(month, year)
    year_xpath = f"//span[normalize-space()='{year}']"
    print(year_xpath)
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, year_xpath))
    ).click()
    time.sleep(2)
    month_xpath = f"//span[normalize-space()='{month.upper()}']"
    print(month_xpath)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, month_xpath))
    ).click()
    time.sleep(2)
    day_xpath = (
        f"//span[normalize-space()='{int(day)}' and not(contains(@class,'p-disabled'))]"
    )
    print(day_xpath)
    time.sleep(2)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, day_xpath))
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

        time.sleep(5)

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Followup to nextmonth")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_followup_nextmonth(login):

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
    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
    ).send_keys(phonenumber)
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
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
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
            (By.XPATH, "//button[normalize-space()='Follow Up']")
        )
    ).click()

    time.sleep(5)

    element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-label='Choose month and year']")
        )
    )
    login.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()

    [year, month, day] = add_month(1)
    print(month, year)
    year_xpath = f"//span[normalize-space()='{year}']"
    print(year_xpath)
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, year_xpath))
    ).click()
    time.sleep(2)
    month_xpath = f"//span[normalize-space()='{month.upper()}']"
    print(month_xpath)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, month_xpath))
    ).click()
    time.sleep(2)
    day_xpath = (
        f"//span[normalize-space()='{int(day)}' and not(contains(@class,'p-disabled'))]"
    )
    print(day_xpath)
    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, day_xpath))
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

        time.sleep(5)
