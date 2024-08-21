from Framework.common_utils import *

first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("After creatng appointment provider create invoice manually")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_appt_manualinvoice(login):
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
    login.execute_script("arguments[0].click();", element)

    service_option_xpath = (
        "(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
        "Consultation'])[2]"
    )
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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys(
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
            print("before in loop")
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
            print("EC caught:")
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
@allure.title("Apply the discount in the Invoice and Share the payment link")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_appt_manualinvoice1(login):
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
        "(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
        "Consultation'])[2]"
    )
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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys(
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
            print("before in loop")
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
            print("EC caught:")
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
            (By.XPATH, "//span[normalize-space()='Apply Discount']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//option[normalize-space()='Select Discount']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//option[normalize-space()='On Demand Discount']")
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
            (By.XPATH, "//button[normalize-space()='Apply']")
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
@allure.title("Add the item in the Invoice and Share the payment link")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
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
        "(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
        "Consultation'])[2]"
    )
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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys(
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
            print("before in loop")
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
            print("EC caught:")
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

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='item-name'][normalize-space()='Consultation']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='cs-btn bt1 ml-0'][normalize-space()='Add']")
        )
    ).click()

    time.sleep(2)
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
@allure.title("Add the item and apply the discount in the Invoice and Share the payment link")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
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
        "(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
        "Consultation'])[2]"
    )
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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys(
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
            print("before in loop")
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
            print("EC caught:")
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
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Create Invoice']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Service/Item']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Item']"))
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
            (By.XPATH, "//span[normalize-space()='Apply Discount']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//option[normalize-space()='Select Discount']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//option[normalize-space()='On Demand Discount']")
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
            (By.XPATH, "//button[normalize-space()='Apply']")
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
@allure.title("Add the sub service in the invoice")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_appt_manualinvoice4(login):
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
        "(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
        "Consultation'])[2]"
    )
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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys(
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
            print("before in loop")
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
            print("EC caught:")
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
            (By.XPATH, "//span[normalize-space()='Apply Discount']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//option[normalize-space()='Select Discount']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//option[normalize-space()='On Demand Discount']")
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
            (By.XPATH, "//button[normalize-space()='Apply']")
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
@allure.title("Settled the Manual Invoice ")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
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
        "(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
        "Consultation'])[2]"
    )
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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys(
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
            print("before in loop")
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
            print("EC caught:")
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
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
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
@allure.title("Apply coupon in manual Invoice")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_appt_manualinvoice6(login):

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
        "(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
        "Consultation'])[2]"
    )
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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys(
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
            print("before in loop")
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
            print("EC caught:")
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
                "//option[@value='SSCP']",
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
@allure.title("Update bill status as canceled")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
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
        "(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
        "Consultation'])[2]"
    )
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
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys(
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
            print("before in loop")
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
            print("EC caught:")
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
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
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

#####################################################################################################################################

@pytest.fixture()
def con_login():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://scale.jaldee.com/visionhospital/")
    driver.maximize_window()
    yield driver


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Consumer take prepayment booking")
def test_prepaymentbooking(con_login):
    try:

        time.sleep(5)

        book_now_button = WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Book Now']")
            )
        )
        con_login.execute_script("arguments[0].scrollIntoView();", book_now_button)

        # Wait for the element to be clickable
        clickable_book_now_button = WebDriverWait(con_login, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[normalize-space()='Book Now']")
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
                    "//div[contains(text(),'Naveen Consultation')]",
                )
            )
        ).click()
        time.sleep(4)
        Today_Date = WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@aria-pressed='true'] [@aria-current='date']")
            )
        )

        con_login.execute_script("arguments[0].click();", Today_Date)

        print("Today Date:", Today_Date.text)

        wait = WebDriverWait(con_login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//mat-chip[@aria-selected='true']"))
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
            EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        ).send_keys("9207206005")

        con_login.find_element(
            By.XPATH, "//span[@class='continue ng-star-inserted']"
        ).click()

        time.sleep(5)

        otp_digits = "5555"

        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(con_login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )

        # print("Number of OTP input fields:", len(otp_inputs))
        # print(otp_inputs)

        for i, otp_input in enumerate(otp_inputs):

            # print(i)
            # print(otp_input)
            otp_input.send_keys(otp_digits[i])

        con_login.find_element(
            By.XPATH,
            "//div[@class='form-group otp text-center']//button[@type='button']",
        ).click()

        WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'NET BANKING')]")
            )
        ).click()

        time.sleep(3)
        makepayment = WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='text-center mgn-up-10']//button[@type='button']",
                )
            )
        )
        con_login.execute_script("arguments[0].click();", makepayment)
        WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[contains(@class,'ptm-paymode-name ptm-lightbold')]")
            )
        ).click()

        time.sleep(1)

        WebDriverWait(con_login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'SBI')]"))
        ).click()

        WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class,'ptm-emi-overlay')]//div[contains(@class,'')]//div[@id='checkout-button']//button[contains(@class,'ptm-nav-selectable')][contains(text(),'Pay ₹149')]",
                )
            )
        ).click()

        # Handle the popup window
        # Save the current window handle
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
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btnd']"))
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

        time.sleep(3)
        # confirm_button = WebDriverWait(con_login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[contains(text(),'Confirm')]")
        #     )
        # )
        # con_login.execute_script("arguments[0].click();", confirm_button)
        # time.sleep(3)

        ok_button = WebDriverWait(con_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Ok']")
            )
        )

        con_login.execute_script("arguments[0].click();", ok_button)

        time.sleep(3)
        # con_login.quit()

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
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
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

    while True:
        try:
            print("before in loop")
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
            print("EC caught:")
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
            (By.XPATH, "//button[normalize-space()='Refund']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@type='button' and contains(@class, 'btn btn-primary btn-square lh-p4 font-weight-bold font-size-xs') and normalize-space(text())='Refund']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Pay Online']"))
    ).click()
    time.sleep(1)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Yes']"))
    ).click()

    time.sleep(5)

######################################################################################################################################


