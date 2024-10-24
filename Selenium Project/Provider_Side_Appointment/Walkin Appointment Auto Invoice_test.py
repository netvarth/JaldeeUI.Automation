from Framework.common_utils import *
import allure
from allure_commons.types import AttachmentType
import os
first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Auto Invoice")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appt_autoinvoice(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]"))
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]"))
    )
    element.click()
    time.sleep(3)
    wait = WebDriverWait(login, 10)
    element_appoint = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[contains(text(),'Create New Patient')]")))
    element_appoint.click()
    login.implicitly_wait(3)

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
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

    login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
    login.implicitly_wait(5)
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

    service_option_xpath = ("(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
                            "Consultation'])[2]")
    WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
    print("Select Service : Naveen Consultation")
    time.sleep(3)
    Today_Date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                            "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
    Today_Date.click()
    print("Today Date:", Today_Date.text)
    wait = WebDriverWait(login, 10)
    time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
    time_slot.click()
    print("Time Slot:", time_slot.text)
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

    login.find_element(By.XPATH,
                       "//span[normalize-space()='Confirm']").click()
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
                    (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
            )

            next_button.click()

        except:
            print("EC caught:")
            break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Invoice']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Get Payment']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Share Payment Link']"))
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

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Get Payment']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Pay by Cash']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Pay']"))
    ).click()

    time.sleep(1)
    login.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()


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


# Apply the discount in the Invoice and Share the payment link
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Apply the discount in the Invoice")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appt_autoinvoice1(login):
    print("Apply discount and share the payment link")

    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]"))
    ).click()
    time.sleep(2)
    while True:
        try:
            print("before in loop")
            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
            )

            next_button.click()

        except:
            print("EC caught:")
            break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Invoice']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Edit']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@aria-haspopup='menu']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Apply Discount']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//option[normalize-space()='Select Discount']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//option[normalize-space()='On Demand Discount']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Amount']"))
    ).send_keys("50")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Apply']"))
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
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Get Payment']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Share Payment Link']"))
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


# Add the item in the Invoice and Share the payment link
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Add the item in the Invoice")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appt_autoinvoice2(login):
    print("Add item and Share the payment link")

    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]"))
    ).click()

    while True:
        try:

            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
            )

            next_button.click()

        except:
            print("EC caught:")
            break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    last_element_in_accordian.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Invoice']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Edit']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Choose Procedure/Item']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='cs-btn bt1 ml-0'][normalize-space()='Add']"))
    ).click()

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
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Get Payment']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Share Payment Link']"))
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


# Add the item and apply the discount in the Invoice and Share the payment link
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Add the item and apply the discount")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appt_autoinvoice3(login):
    # Add the item and apply the discount in the Invoice and Share the payment link
    print("Add item, Apply the discount and Share the payment link")
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]"))
    ).click()

    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]"))
    )
    element.click()
    time.sleep(3)
    wait = WebDriverWait(login, 10)
    element_appoint = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[contains(text(),'Create New Patient')]")))
    element_appoint.click()
    login.implicitly_wait(3)

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
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

    login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
    login.implicitly_wait(5)
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

    service_option_xpath = ("(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
                            "Consultation'])[2]")
    WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
    print("Select Service : Naveen Consultation")
    time.sleep(3)
    Today_Date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                            "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
    Today_Date.click()
    print("Today Date:", Today_Date.text)
    wait = WebDriverWait(login, 10)
    time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
    time_slot.click()
    print("Time Slot:", time_slot.text)
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

    login.find_element(By.XPATH,
                       "//span[normalize-space()='Confirm']").click()

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

            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
            )

            next_button.click()

        except:
            print("EC caught:")
            break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    last_element_in_accordian.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Invoice']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Edit']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Choose Procedure/Item']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='cs-btn bt1 ml-0'][normalize-space()='Add']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@aria-haspopup='menu']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Apply Discount']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//option[normalize-space()='Select Discount']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//option[normalize-space()='On Demand Discount']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Amount']"))
    ).send_keys("50")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Apply']"))
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
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Get Payment']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Share Payment Link']"))
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


# Change the Qty/Price of the Service in the invoice and share the payment link
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Change the Qty/Price of the Service and share the payment link")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appt_autoinvoice4(login):
    # Change the Qty/Price of the Service in the invoice and share the payment link
    print("Change the Qty/Price in the invoice and Share the payment link")

    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]"))
    ).click()

    while True:
        try:

            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
            )

            next_button.click()

        except:
            print("EC caught:")
            break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    last_element_in_accordian.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Invoice']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Edit']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='mat-mdc-button-touch-target']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Change Qty/Price']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Quantity']"))
    ).send_keys("2")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add Service/Item']"))
    ).click()

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
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Get Payment']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Share Payment Link']"))
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


# Share PDF to the consumer 
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Share PDF to the consumer")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appt_autoinvoice5(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]"))
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]"))
    )
    element.click()
    time.sleep(3)
    wait = WebDriverWait(login, 10)
    element_appoint = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[contains(text(),'Create New Patient')]")))
    element_appoint.click()
    login.implicitly_wait(3)

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
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

    login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
    login.implicitly_wait(5)
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

    service_option_xpath = ("(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
                            "Consultation'])[2]")
    WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
    print("Select Service : Naveen Consultation")
    time.sleep(3)
    Today_Date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                            "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
    Today_Date.click()
    print("Today Date:", Today_Date.text)
    wait = WebDriverWait(login, 10)
    time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
    time_slot.click()
    print("Time Slot:", time_slot.text)
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

    login.find_element(By.XPATH,
                       "//span[normalize-space()='Confirm']").click()
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
                    (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
            )

            next_button.click()

        except:
            print("EC caught:")
            break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Invoice']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Share PDF']"))
    ).click()

    login.implicitly_wait(5)
    login.find_element(By.XPATH, "//span[@class='mdc-button__label']").click()

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


# Settle the auto Invoice 
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Settle the auto Invoice")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appt_autoinvoice6(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]"))
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]"))
    )
    element.click()
    time.sleep(3)
    wait = WebDriverWait(login, 10)
    element_appoint = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[contains(text(),'Create New Patient')]")))
    element_appoint.click()
    login.implicitly_wait(3)

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
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

    login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
    login.implicitly_wait(5)
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

    service_option_xpath = ("(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
                            "Consultation'])[2]")
    WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
    print("Select Service : Naveen Consultation")
    time.sleep(3)
    Today_Date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                            "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
    Today_Date.click()
    print("Today Date:", Today_Date.text)
    wait = WebDriverWait(login, 10)
    time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
    time_slot.click()
    print("Time Slot:", time_slot.text)
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

    login.find_element(By.XPATH,
                       "//span[normalize-space()='Confirm']").click()
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
                    (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
            )

            next_button.click()

        except:
            print("EC caught:")
            break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Invoice']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Settle Invoice']"))
    ).click()

    time.sleep(2)
    login.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()


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



@allure.severity(allure.severity_level.NORMAL)
@allure.title("Pay by cash in Auto Invoice")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appt_autoinvoice7(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]"))
    ).click()

    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]"))
    )
    element.click()
    time.sleep(3)
    wait = WebDriverWait(login, 10)
    element_appoint = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[contains(text(),'Create New Patient')]")))
    element_appoint.click()
    login.implicitly_wait(3)

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
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

    login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
    login.implicitly_wait(5)
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

    service_option_xpath = ("(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
                            "Consultation'])[2]")
    WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
    print("Select Service : Naveen Consultation")
    time.sleep(3)
    Today_Date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                            "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
    Today_Date.click()
    print("Today Date:", Today_Date.text)
    wait = WebDriverWait(login, 10)
    time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
    time_slot.click()
    print("Time Slot:", time_slot.text)
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

    time.sleep(2)
    login.find_element(By.XPATH,
                       "//span[normalize-space()='Confirm']").click()
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
                    (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
            )

            next_button.click()

        except:
            print("EC caught:")
            break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Invoice']"))
    ).click()
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Get Payment']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Pay by Cash']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Pay']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Yes']"))
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



@allure.severity(allure.severity_level.NORMAL)
@allure.title("Pay by other with Credit Card (CC)")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appt_autoinvoice9(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]"))
    ).click()

    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]"))
    )
    element.click()
    time.sleep(3)
    wait = WebDriverWait(login, 10)
    element_appoint = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[contains(text(),'Create New Patient')]")))
    element_appoint.click()
    login.implicitly_wait(3)

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
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

    login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
    login.implicitly_wait(5)
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

    service_option_xpath = ("(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
                            "Consultation'])[2]")
    WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
    print("Select Service : Naveen Consultation")
    time.sleep(3)
    Today_Date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                            "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
    Today_Date.click()
    print("Today Date:", Today_Date.text)
    wait = WebDriverWait(login, 10)
    time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
    time_slot.click()
    print("Time Slot:", time_slot.text)
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

    time.sleep(2)
    login.find_element(By.XPATH,
                       "//span[normalize-space()='Confirm']").click()
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
                    (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
            )

            next_button.click()

        except:
            print("EC caught:")
            break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Invoice']"))
    ).click()


    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Get Payment']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Pay by Others']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Pay']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Yes']"))
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




@allure.severity(allure.severity_level.NORMAL)
@allure.title("Pay by other with UPI")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appt_autoinvoice8(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]"))
    ).click()

    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]"))
    )
    element.click()
    time.sleep(3)
    wait = WebDriverWait(login, 10)
    element_appoint = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[contains(text(),'Create New Patient')]")))
    element_appoint.click()
    login.implicitly_wait(3)

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
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

    login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
    login.implicitly_wait(5)
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

    service_option_xpath = ("(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
                            "Consultation'])[2]")
    WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
    print("Select Service : Naveen Consultation")
    time.sleep(3)
    Today_Date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                            "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
    Today_Date.click()
    print("Today Date:", Today_Date.text)
    wait = WebDriverWait(login, 10)
    time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
    time_slot.click()
    print("Time Slot:", time_slot.text)
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

    time.sleep(2)
    login.find_element(By.XPATH,
                       "//span[normalize-space()='Confirm']").click()
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
                    (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
            )

            next_button.click()

        except:
            print("EC caught:")
            break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Invoice']"))
    ).click()


    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Get Payment']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Pay by Others']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='CC'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Pay']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Yes']"))
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