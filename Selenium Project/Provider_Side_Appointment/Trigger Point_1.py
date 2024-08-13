from Framework.common_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Signup")
def test_signup():
    login = webdriver.Chrome(
        service=ChromeService(
            executable_path=r"Drivers\chromedriver-win64\chromedriver.exe"
        )
    )
    login.get("https://test.jaldee.com/business/")
    login.maximize_window()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Sign Up']"))
    ).click()

    time.sleep(3)
    first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='Firstname']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='Lastname']").send_keys(str(last_name))

    time.sleep(3)
    signup_button = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='signup']"))
    )

    # Scroll into view if needed
    login.execute_script("arguments[0].scrollIntoView(true);", signup_button)

    # Additional wait to ensure the element is not covered by any other element
    time.sleep(1)

    signup_button.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//h6[normalize-space()='Healthcare']")
        )
    ).click()

    next_button = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@class='form-submit']"))
    )

    login.execute_script("arguments[0].scrollIntoView(true);", next_button)

    time.sleep(1)

    next_button.click()

    # login.find_element(By.XPATH,"//h6[normalize-space()='Doctor / Clinic']").click()

    next_button1 = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@value='Next']"))
    )

    login.execute_script("arguments[0].scrollIntoView(true);", next_button1)

    time.sleep(1)

    next_button1.click()

    time.sleep(2)

    next_button2 = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='signup']"))
    )
    login.execute_script("arguments[0].scrollIntoView(true);", next_button2)
    time.sleep(1)
    next_button2.click()

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

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter OTP']"))
    ).send_keys("55555")

    confirm_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Confirm OTP']")
        )
    )

    login.execute_script("arguments[0].scrollIntoView(true);", confirm_button)

    time.sleep(1)
    confirm_button.click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='loginId']"))
    ).send_keys(phonenumber)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='newpassfield']"))
    ).send_keys("Jaldee01")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Re-enter Password']")
        )
    ).send_keys("Jaldee01")

    join_button = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='signup']"))
    )

    join_button.click()

    time.sleep(2)

    ###############################################################################################################################


#############################################################################################################################################
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Reconfirmation")
@pytest.mark.parametrize("url", ["https://test.jaldee.com/business/"])
def test_patient_Reconfirmation(login):
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

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
        )
    ).send_keys("9207206005")

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Id : 1')]"))
    ).click()

    time.sleep(3)

    print("Select Service :  Consultation ")

    time.sleep(3)
    Today_Date = WebDriverWait(login, 10).until(
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
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()

    print("Note added for walkin appointment")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Upload File']")
        )
    ).click()

    time.sleep(8)
    # Get the current working directory
    current_working_directory = os.getcwd()

    # Construct the absolute path
    absolute_path = os.path.abspath(
        os.path.join(current_working_directory, r"Extras\test.png")
    )
    pyautogui.write(absolute_path)
    pyautogui.press("enter")

    time.sleep(4)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
    ).click()

    print("Appointment confirm successfully")

    time.sleep(5)

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

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Change Status']")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Cancel')]"))
    ).click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'No Show Up')]")
        )
    ).click()

    login.find_element(By.XPATH, "//span[@class='mdc-button__label']").click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@type='checkbox'])[4]"))
    ).click()

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

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Change Status']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='status status-box']"))
    ).click()

    toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_message.text
    print("Toast Message:", message)


##################################################################################################################################
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Start")
@pytest.mark.parametrize("url", ["https://test.jaldee.com/business/"])
def test_patient_start(login):
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

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
        )
    ).send_keys("9207206005")

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Id : 1')]"))
    ).click()

    time.sleep(3)

    print("Select Service :  Consultation ")

    time.sleep(3)
    Today_Date = WebDriverWait(login, 10).until(
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
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()

    print("Note added for walkin appointment")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Upload File']")
        )
    ).click()

    time.sleep(8)
    # Get the current working directory
    current_working_directory = os.getcwd()

    # Construct the absolute path
    absolute_path = os.path.abspath(
        os.path.join(current_working_directory, r"Extras\test.png")
    )
    pyautogui.write(absolute_path)
    pyautogui.press("enter")

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

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Change Status']")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Start')]"))
    ).click()

    toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_message.text
    print("Toast Message:", message)


#######################################################################################################################################
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Reminder Message")
@pytest.mark.parametrize("url", ["https://test.jaldee.com/business/"])
def test_reminder_message(login):

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

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
        )
    ).send_keys("9207206005")

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Id : 1')]"))
    ).click()

    time.sleep(3)

    print("Select Service :  Consultation ")

    time.sleep(3)
    Today_Date = WebDriverWait(login, 10).until(
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
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()

    print("Note added for walkin appointment")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Upload File']")
        )
    ).click()

    time.sleep(8)
    # Get the current working directory
    current_working_directory = os.getcwd()

    # Construct the absolute path
    absolute_path = os.path.abspath(
        os.path.join(current_working_directory, r"Extras\test.png")
    )
    pyautogui.write(absolute_path)
    pyautogui.press("enter")

    time.sleep(4)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
    ).click()

    print("Appointment confirm successfully")

    time.sleep(3)

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
    more_actions_button = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[normalize-space()='More Actions']")
        )
    )
    more_actions_button.click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Share Info']")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='mdc-button__label']"))
    ).click()


#######################################################################################################################################
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Completed Messages")
@pytest.mark.parametrize("url", ["https://test.jaldee.com/business/"])
def test_completed_messages(login):

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

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
        )
    ).send_keys("9207206005")

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Id : 1')]"))
    ).click()

    time.sleep(3)

    print("Select Service :  Consultation ")

    time.sleep(3)
    Today_Date = WebDriverWait(login, 10).until(
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

    print("Appointment confirm successfully")

    time.sleep(3)

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

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Change Status']")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Complete')]"))
    ).click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
    ).click()

    toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_message.text
    print("Toast Message:", message)


##############################################################################################################
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Donation")
@pytest.mark.parametrize("url", ["https://test.jaldee.com/53b6eu1/"])
def test_donation(con_login):
    time.sleep(5)

    donation = (
        WebDriverWait(con_login, 10)
        .until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Donate')]")
            )
        )
        .click()
    )

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
    ).send_keys("9207206005")

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='continue ng-star-inserted']")
        )
    ).click()

    time.sleep(2)
    otp_digits = "5555"

    # Wait for the OTP input fields to be present
    otp_inputs = WebDriverWait(con_login, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//input[contains(@id, 'otp_')]")
        )
    )

    for i, otp_input in enumerate(otp_inputs):
        otp_input.send_keys(otp_digits[i])

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='continue ng-star-inserted']")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='number']"))
    ).send_keys("400")

    # WebDriverWait(con_login, 10).until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "//textarea[contains(@class,'form-control mgn-bt-20 ng-pristine ng-valid ng-touched')]",
    #         )
    #     )
    # ).send_keys("Donation")

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'NET BANKING')]")
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[contains(text(),'Proceed')]")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[contains(@class,'ptm-paymode-name ptm-lightbold')]")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'SBI')]"))
    ).click()

    paybutton = WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'ptm-emi-overlay')]//div[contains(@class,'')]//div[@id='checkout-button']//button[contains(@class,'ptm-nav-selectable')][contains(text(),'Pay ₹400')]",
            )
        )
    )
    paybutton.click()

    main_window_handle = con_login.current_window_handle

    # Wait until the new window is present
    WebDriverWait(con_login, 10).until(EC.new_window_is_opened)

    # Get all window handles
    all_window_handles = con_login.window_handles

    # Find the new window handle (the popup window)
    new_window_handle = None
    for handle in all_window_handles:
        if handle != main_window_handle:
            new_window_handle = handle
            break

    # Switch to the new window
    con_login.switch_to.window(new_window_handle)

    # Now interact with elements in the new window
    # For example, clicking the success button
    time.sleep(3)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Successful')]")
        )
    ).click()

    # Optionally, switch back to the main window

    con_login.switch_to.window(main_window_handle)
    # time.sleep(15)

    try:
        snack_bar = WebDriverWait(con_login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

    except:

        snack_bar = WebDriverWait(con_login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

    # book_now_button = WebDriverWait(con_login, 10).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "//span[normalize-space()='Book Now']")
    #     )
    # )
    # con_login.execute_script("arguments[0].scrollIntoView();", book_now_button)

    # # Wait for the element to be clickable
    # clickable_book_now_button = WebDriverWait(con_login, 10).until(
    #     EC.element_to_be_clickable(
    #         (By.XPATH, "//span[normalize-space()='Book Now']")
    #     )
    # )

    # # Attempt to click the element
    # try:
    #     clickable_book_now_button.click()
    # except:
    #     # If click is intercepted, click using JavaScript
    #     con_login.execute_script("arguments[0].click();", clickable_book_now_button)


###########################################################################################################
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Confirmation,Reschedule,Send Message, Send attachment")
@pytest.mark.parametrize("url", ["https://test.jaldee.com/53b6eu1/"])
def test_confirmation(con_login):
    time.sleep(3)
    book_now_button = WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Book Now']")
        )
    )
    con_login.execute_script("arguments[0].scrollIntoView();", book_now_button)

    # Wait for the element to be clickable
    clickable_book_now_button = WebDriverWait(con_login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Book Now']"))
    )

    # Attempt to click the element
    try:
        clickable_book_now_button.click()
    except:
        # If click is intercepted, click using JavaScript
        con_login.execute_script("arguments[0].click();", clickable_book_now_button)

    time.sleep(2)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class,'serviceName ng-star-inserted')]")
        )
    ).click()

    time.sleep(2)
    Today_Date = WebDriverWait(con_login, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[@aria-pressed='true'] [@aria-current='date']",
            )
        )
    )

    Today_Date.click()

    print("Today Date:", Today_Date.text)

    wait = WebDriverWait(con_login, 10)
    time_slot = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//mat-chip[@aria-selected='true']"))
    )
    time_slot.click()
    print("Time Slot:", time_slot.text)

    con_login.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
    ).send_keys("9207206005")

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='continue ng-star-inserted']")
        )
    ).click()

    time.sleep(2)
    otp_digits = "5555"

    # Wait for the OTP input fields to be present
    otp_inputs = WebDriverWait(con_login, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//input[contains(@id, 'otp_')]")
        )
    )

    for i, otp_input in enumerate(otp_inputs):
        otp_input.send_keys(otp_digits[i])

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='continue ng-star-inserted']")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
    ).click()

    time.sleep(3)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Ok')]"))
    ).click()

    time.sleep(3)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'My Bookings')]")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span//mat-icon[@class='mat-icon notranslate material-icons mat-ligature-font mat-icon-no-color']",
            )
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Reschedule']")
        )
    ).click()

    today_date = datetime.now()
    print(today_date.day)
    today_xpath_expression = "//div[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today'][normalize-space()='{}']".format(
        today_date.day
    )
    print(today_xpath_expression)
    tomorrow_date = today_date + timedelta(days=1)
    print(tomorrow_date.day)

    time.sleep(3)
    tomorrow_xpath_expression = "//div[@class='mat-calendar-body-cell-content mat-focus-indicator'][normalize-space()='{}']".format(
        tomorrow_date.day
    )
    print(tomorrow_xpath_expression)

    Tomorrow_Date = WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, tomorrow_xpath_expression))
    )
    Tomorrow_Date.click()

    print("Tomorrow Date:", Tomorrow_Date.text)

    wait = WebDriverWait(con_login, 10)
    time_slot = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//mat-chip[@class='mat-chip mat-focus-indicator text-center mat-primary mat-standard-chip mat-chip-selected ng-star-inserted']",
            )
        )
    )
    time_slot.click()
    print("Time Slot:", time_slot.text)

    time.sleep(2)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Next']"))
    ).click()

    time.sleep(2)

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Reschedule']")
        )
    ).click()

    time.sleep(3)

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
    ).click()

    print("Appointment Rescheduled successfully")

    # time.sleep(3)
    # WebDriverWait(con_login, 10).until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "//div[@class='cdk-overlay-backdrop cdk-overlay-transparent-backdrop cdk-overlay-backdrop-showing']",
    #         )
    #     )
    # ).click()

    # WebDriverWait(con_login, 10).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "//span[normalize-space()='Dashboard']")
    #     )
    # ).click()

    time.sleep(2)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='My Bookings']")
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span//mat-icon[@class='mat-icon notranslate material-icons mat-ligature-font mat-icon-no-color']",
            )
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Send Message']")
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@id='message']"))
    ).send_keys(" Message to the provider ")

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//button[@type='button']//i[@class='material-icons'][normalize-space()='attach_file']",
            )
        )
    ).click()

    time.sleep(8)
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
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Send']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Send Attachments']")
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Click here to select the files']")
        )
    ).click()

    time.sleep(8)
    # Get the current working directory
    current_working_directory = os.getcwd()

    # Construct the absolute path
    absolute_path = os.path.abspath(
        os.path.join(current_working_directory, r"Extras\test.png")
    )
    pyautogui.write(absolute_path)
    pyautogui.press("enter")
    print("Successfully upload the file")

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='send']"))
    ).click()

    time.sleep(2)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//mat-select[@role='combobox']"))
    ).click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Upcoming Bookings')]")
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span//mat-icon[@class='mat-icon notranslate material-icons mat-ligature-font mat-icon-no-color']",
            )
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Cancel']"))
    ).click()

    con_login.find_element(
        By.XPATH, "//mat-chip[normalize-space()='Change of Plans']"
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Confirm']")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-arrow-left']"))
    ).click()

    time.sleep(3)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[@alt='Home']"))
    ).click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-commenting-o']"))
    ).click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@id='message']"))
    ).send_keys("Message to provider")

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted']"))
    ).click()

    time.sleep(3)


################################################################################################################################################
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Reschedule")
@pytest.mark.parametrize("url", ["https://test.jaldee.com/53b6eu1/"])
def test_reschedule(con_login):
    time.sleep(3)
    book_now_button = WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Book Now']")
        )
    )
    con_login.execute_script("arguments[0].scrollIntoView();", book_now_button)

    # Wait for the element to be clickable
    clickable_book_now_button = WebDriverWait(con_login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Book Now']"))
    )

    # Attempt to click the element
    try:
        clickable_book_now_button.click()
    except:
        # If click is intercepted, click using JavaScript
        con_login.execute_script("arguments[0].click();", clickable_book_now_button)

    time.sleep(2)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class,'serviceName ng-star-inserted')]")
        )
    ).click()

    time.sleep(2)
    Today_Date = WebDriverWait(con_login, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[@aria-pressed='true'] [@aria-current='date']",
            )
        )
    )

    Today_Date.click()

    print("Today Date:", Today_Date.text)

    wait = WebDriverWait(con_login, 10)
    time_slot = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//mat-chip[@aria-selected='true']"))
    )
    time_slot.click()
    print("Time Slot:", time_slot.text)

    con_login.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
    ).send_keys("9207206005")

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='continue ng-star-inserted']")
        )
    ).click()

    time.sleep(2)
    otp_digits = "5555"

    # Wait for the OTP input fields to be present
    otp_inputs = WebDriverWait(con_login, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//input[contains(@id, 'otp_')]")
        )
    )

    for i, otp_input in enumerate(otp_inputs):
        otp_input.send_keys(otp_digits[i])

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='continue ng-star-inserted']")
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Confirm']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
    ).click()

    time.sleep(3)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'My Bookings')]")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span//mat-icon[@class='mat-icon notranslate material-icons mat-ligature-font mat-icon-no-color']",
            )
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Reschedule']")
        )
    ).click()

    today_date = datetime.now()
    print(today_date.day)
    today_xpath_expression = "//div[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today'][normalize-space()='{}']".format(
        today_date.day
    )
    print(today_xpath_expression)
    tomorrow_date = today_date + timedelta(days=1)
    print(tomorrow_date.day)

    # current_month_year = WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "//button[@aria-label='Choose month and year']//span[@class='mat-button-wrapper']",
    #         )
    #     )
    # )
    # print(current_month_year.text)
    # print(current_month_year.text.lower())
    # print(tomorrow_date.strftime("%b %Y").lower())
    # if current_month_year.text.lower() != tomorrow_date.strftime("%b %Y").lower():
    #     login.find_element(By.XPATH, "//button[@aria-label='Next month']").click()
    time.sleep(3)
    tomorrow_xpath_expression = "//div[@class='mat-calendar-body-cell-content mat-focus-indicator'][normalize-space()='{}']".format(
        tomorrow_date.day
    )
    print(tomorrow_xpath_expression)

    Tomorrow_Date = WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, tomorrow_xpath_expression))
    )
    Tomorrow_Date.click()

    print("Tomorrow Date:", Tomorrow_Date.text)

    wait = WebDriverWait(con_login, 10)
    time_slot = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//mat-chip[@class='mat-chip mat-focus-indicator text-center mat-primary mat-standard-chip mat-chip-selected ng-star-inserted']",
            )
        )
    )
    time_slot.click()
    print("Time Slot:", time_slot.text)

    time.sleep(2)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Next']"))
    ).click()

    time.sleep(2)

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Reschedule']")
        )
    ).click()

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
    ).click()

    print("Appointment Rescheduled successfully")


###################################################################################################################
