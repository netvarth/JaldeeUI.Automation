from selenium.webdriver.chrome.webdriver import WebDriver
import webdriver_manager
from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import allure
from allure_commons.types import AttachmentType
import os
first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoice test cases for paid invoice")
@pytest.mark.parametrize("iteration", range(5))  # Adjust the range to set the number of iterations
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Invoice_appointment(login, iteration): 

    
    """
    Test invoice creation with multiple iterations.
    """
    print(f"Running iteration: {iteration + 1}")
    first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
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

    con_name = login.find_element(By.XPATH, "//input[@id='first_name']")
    con_name.send_keys(first_name)
    con_name = first_name
    con_lastname = login.find_element(By.XPATH, "//input[@id='last_name']")
    con_lastname.send_keys(last_name)
    con_lastname = last_name
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
    
    time.sleep(3)
    wait = WebDriverWait(login, 30) 

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//p-dropdown[@optionlabel='departmentName']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='ENT'])[1]"))
    ).click()

    wait.until(
       EC.presence_of_element_located(
           (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")) 
    ).click()

    time.sleep(2)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Venu Gopal']"))    
    ).click()

    # time.sleep(2)
    # Today_Date = wait.until(EC.presence_of_element_located(
    #     (By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today']"))
    # )
    # Today_Date.click()
    # print("Today Date:", Today_Date.text)


    time.sleep(3)
    [year,month,day] = sub_days(27)
    print(year)
    print(month)
    print(day)
    time.sleep(2)
    
    year_month = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-label='Choose month and year']//span[@class='mat-mdc-button-touch-target']"))
    )
    login.execute_script("arguments[0].click();", year_month)
    
    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']"))
    # ).click()
    time.sleep(2)

    year_xpath = f"//span[normalize-space()='{year}']"
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, year_xpath))
    ).click()
    print(year_xpath)
    time.sleep(2)
    month_xpath = f"//span[contains(text(),'{month.upper()}')]" 
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, month_xpath))
    ).click()
    print(month_xpath)
    time.sleep(5)
    day_xpath = (
        f"//span[normalize-space()='{day}']"
    )
    print(day_xpath)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, day_xpath))
    ).click()


    time.sleep(3)
    # wait = WebDriverWait(login, 10)
    # time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
    # time_slot.click()
    # print("Time Slot:", time_slot.text)
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
    WebDriverWait(login, 10).until(
         EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

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

    time.sleep(3)

    dropdown1 = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
    )
    dropdown1.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='History'])[1]"))
    ).click()

    time.sleep(2)

    filter = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//i[@class='pi pi-filter-fill'])[1]"))
    )
    login.execute_script("arguments[0].click();", filter)

    time.sleep(3)
    name_option = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Name')]"))
    )
    login.execute_script("arguments[0].click();", name_option)

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='firstName']"))
    ).send_keys(con_name)

    time.sleep(1)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='lastName']"))
    ).send_keys(con_lastname)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Apply']"))
    ).click()

    time.sleep(5)

    # while True:
    #     try:
    #         print("before in loop")
    #         next_button = WebDriverWait(login, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
    #         )

    #         next_button.click()

    #     except:
    #         print("EC caught:")
    #         break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create Invoice']"))
    ).click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Edit Procedure/Item']"))
    ).click()

    price_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Price']"))
    )
    price_button.clear()
    price_button.send_keys("500")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()

    time.sleep(3)
    Add_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    )

    login.execute_script("arguments[0].click();", Add_button)

    fee_service = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Registration fee')]"))
    )
    login.execute_script("arguments[0].scrollIntoView();", fee_service)
    fee_service.click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()

    time.sleep(3)
    update_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']"))
    )
    update_button.click()


    time.sleep(3)
    pay_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
    )
    login.execute_script("arguments[0].click();", pay_button)

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
    print(f"Iteration {iteration + 1} completed")

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoice test cases unpaid")
@pytest.mark.parametrize("iteration", range(5))  # Adjust the range to set the number of iterations
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Invoice_appointment1(login, iteration):

    
    """
    Test invoice creation with multiple iterations.
    """
    print(f"Running iteration: {iteration + 1}")
    first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
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

    con_name = login.find_element(By.XPATH, "//input[@id='first_name']")
    con_name.send_keys(first_name)
    con_name = first_name
    con_lastname = login.find_element(By.XPATH, "//input[@id='last_name']")
    con_lastname.send_keys(last_name)
    con_lastname = last_name
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
    
    time.sleep(3)
    wait = WebDriverWait(login, 30) 

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//p-dropdown[@optionlabel='departmentName']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='ENT'])[1]"))
    ).click()

    wait.until(
       EC.presence_of_element_located(
           (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")) 
    ).click()

    time.sleep(2)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Venu Gopal']"))    
    ).click()

    # time.sleep(2)
    # Today_Date = wait.until(EC.presence_of_element_located(
    #     (By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today']"))
    # )
    # Today_Date.click()
    # print("Today Date:", Today_Date.text)


    time.sleep(3)
    [year,month,day] = sub_days(27)
    print(year)
    print(month)
    print(day)
    time.sleep(2)
    
    year_month = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-label='Choose month and year']//span[@class='mat-mdc-button-touch-target']"))
    )
    login.execute_script("arguments[0].click();", year_month)
    
    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']"))
    # ).click()
    time.sleep(2)

    year_xpath = f"//span[normalize-space()='{year}']"
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, year_xpath))
    ).click()
    print(year_xpath)
    time.sleep(2)
    month_xpath = f"//span[contains(text(),'{month.upper()}')]" 
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, month_xpath))
    ).click()
    print(month_xpath)
    time.sleep(5)
    day_xpath = (
        f"//span[normalize-space()='{day}']"
    )
    print(day_xpath)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, day_xpath))
    ).click()


    time.sleep(3)
    # wait = WebDriverWait(login, 10)
    # time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
    # time_slot.click()
    # print("Time Slot:", time_slot.text)
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
    WebDriverWait(login, 10).until(
         EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

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

    time.sleep(3)

    dropdown1 = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
    )
    dropdown1.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='History'])[1]"))
    ).click()

    time.sleep(2)

    filter = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//i[@class='pi pi-filter-fill'])[1]"))
    )
    login.execute_script("arguments[0].click();", filter)

    time.sleep(3)
    name_option = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Name')]"))
    )
    login.execute_script("arguments[0].click();", name_option)

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='firstName']"))
    ).send_keys(con_name)

    time.sleep(1)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='lastName']"))
    ).send_keys(con_lastname)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Apply']"))
    ).click()


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
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create Invoice']"))
    ).click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Edit Procedure/Item']"))
    ).click()

    price_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Price']"))
    )
    price_button.clear()
    price_button.send_keys("500")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()

    time.sleep(3)
    Add_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    )

    login.execute_script("arguments[0].click();", Add_button)

    fee_service = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Registration fee')]"))
    )
    login.execute_script("arguments[0].scrollIntoView();", fee_service)
    fee_service.click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()

    time.sleep(3)
    update_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']"))
    )
    update_button.click()


    time.sleep(3)
    pay_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
    )
    login.execute_script("arguments[0].click();", pay_button)

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']"))
    ).click()

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mdc-button__label'])[1]"))
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

    print(f"Iteration {iteration + 1} completed")

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoice test cases sub-service assigned unpaid ")
@pytest.mark.parametrize("iteration", range(5))  # Adjust the range to set the number of iterations
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Invoice_appointment2(login, iteration):

    
    """
    Test invoice creation with multiple iterations.
    """
    print(f"Running iteration: {iteration + 1}")
    first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
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

    con_name = login.find_element(By.XPATH, "//input[@id='first_name']")
    con_name.send_keys(first_name)
    con_name = first_name
    con_lastname = login.find_element(By.XPATH, "//input[@id='last_name']")
    con_lastname.send_keys(last_name)
    con_lastname = last_name
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
    
    time.sleep(3)
    wait = WebDriverWait(login, 30) 

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//p-dropdown[@optionlabel='departmentName']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='ENT'])[1]"))
    ).click()

    wait.until(
       EC.presence_of_element_located(
           (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")) 
    ).click()

    time.sleep(2)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Venu Gopal']"))    
    ).click()

    # time.sleep(2)
    # Today_Date = wait.until(EC.presence_of_element_located(
    #     (By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today']"))
    # )
    # Today_Date.click()
    # print("Today Date:", Today_Date.text)

    time.sleep(3)
    [year,month,day] = sub_days(27)
    print(year)
    print(month)
    print(day)
    time.sleep(2)
    
    year_month = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-label='Choose month and year']//span[@class='mat-mdc-button-touch-target']"))
    )
    login.execute_script("arguments[0].click();", year_month)
    
    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']"))
    # ).click()
    time.sleep(2)

    year_xpath = f"//span[normalize-space()='{year}']"
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, year_xpath))
    ).click()
    print(year_xpath)
    time.sleep(2)
    month_xpath = f"//span[contains(text(),'{month.upper()}')]" 
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, month_xpath))
    ).click()
    print(month_xpath)
    time.sleep(5)
    day_xpath = (
        f"//span[normalize-space()='{day}']"
    )
    print(day_xpath)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, day_xpath))
    ).click()


    time.sleep(3)
    # wait = WebDriverWait(login, 10)
    # time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
    # time_slot.click()
    # print("Time Slot:", time_slot.text)
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
    WebDriverWait(login, 10).until(
         EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

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

    time.sleep(3)

    dropdown1 = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
    )
    dropdown1.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='History'])[1]"))
    ).click()

    time.sleep(2)

    filter = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//i[@class='pi pi-filter-fill'])[1]"))
    )
    login.execute_script("arguments[0].click();", filter)

    time.sleep(3)
    name_option = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Name')]"))
    )
    login.execute_script("arguments[0].click();", name_option)

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='firstName']"))
    ).send_keys(con_name)

    time.sleep(1)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='lastName']"))
    ).send_keys(con_lastname)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Apply']"))
    ).click()


    time.sleep(5)

    # while True:
    #     try:
    #         print("before in loop")
    #         next_button = WebDriverWait(login, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
    #         )

    #         next_button.click()

    #     except:
    #         print("EC caught:")
    #         break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create Invoice']"))
    ).click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Edit Procedure/Item']"))
    ).click()

    price_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Price']"))
    )
    price_button.clear()
    price_button.send_keys("500")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()

    time.sleep(3)
    Add_button = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    )

    login.execute_script("arguments[0].scrollIntoView();", Add_button)

    Add_button.click()

    select_subservice = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Sub_Service']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", select_subservice)
    select_subservice.click()

    price = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Price']"))
    )
    price.clear()
    price.send_keys("350")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@class='p-multiselect-label p-placeholder'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Swathy']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add']"))
    ).click()

    time.sleep(3)
    Add_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    )

    login.execute_script("arguments[0].click();", Add_button)

    fee_service = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Registration fee')]"))
    )
    login.execute_script("arguments[0].scrollIntoView();", fee_service)
    fee_service.click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()

    time.sleep(3)

    update_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']"))
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

    
    time.sleep(3)
    pay_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
    )
    login.execute_script("arguments[0].click();", pay_button)

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']"))
    ).click()

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mdc-button__label'])[1]"))
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

    print(f"Iteration {iteration + 1} completed")

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoice test cases sub-service unassigned unpaid ")
@pytest.mark.parametrize("iteration", range(5))  # Adjust the range to set the number of iterations
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Invoice_appointment3(login, iteration):

    
    """
    Test invoice creation with multiple iterations.
    """
    print(f"Running iteration: {iteration + 1}")
    first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
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

    con_name = login.find_element(By.XPATH, "//input[@id='first_name']")
    con_name.send_keys(first_name)
    con_name = first_name
    con_lastname = login.find_element(By.XPATH, "//input[@id='last_name']")
    con_lastname.send_keys(last_name)
    con_lastname = last_name
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
    
    time.sleep(3)
    wait = WebDriverWait(login, 30) 

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//p-dropdown[@optionlabel='departmentName']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Neurology']"))
    ).click()

    wait.until(
       EC.presence_of_element_located(
           (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")) 
    ).click()

    time.sleep(2)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Fabin JJ']"))    
    ).click()

    # time.sleep(2)
    # Today_Date = wait.until(EC.presence_of_element_located(
    #     (By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today']"))
    # )
    # Today_Date.click()
    # print("Today Date:", Today_Date.text)



    time.sleep(3)
    [year,month,day] = sub_days(27)
    print(year)
    print(month)
    print(day)
    time.sleep(2)
    
    year_month = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-label='Choose month and year']//span[@class='mat-mdc-button-touch-target']"))
    )
    login.execute_script("arguments[0].click();", year_month)
    
    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']"))
    # ).click()
    time.sleep(2)

    year_xpath = f"//span[normalize-space()='{year}']"
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, year_xpath))
    ).click()
    print(year_xpath)
    time.sleep(2)
    month_xpath = f"//span[contains(text(),'{month.upper()}')]" 
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, month_xpath))
    ).click()
    print(month_xpath)
    time.sleep(5)
    day_xpath = (
        f"//span[normalize-space()='{day}']"
    )
    print(day_xpath)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, day_xpath))
    ).click()


    time.sleep(3)
    # wait = WebDriverWait(login, 10)
    # time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
    # time_slot.click()
    # print("Time Slot:", time_slot.text)
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
    WebDriverWait(login, 10).until(
         EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

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

    time.sleep(3)

    dropdown1 = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
    )
    dropdown1.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='History'])[1]"))
    ).click()

    time.sleep(2)

    filter = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//i[@class='pi pi-filter-fill'])[1]"))
    )
    login.execute_script("arguments[0].click();", filter)

    time.sleep(3)
    name_option = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Name')]"))
    )
    login.execute_script("arguments[0].click();", name_option)

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='firstName']"))
    ).send_keys(con_name)

    time.sleep(1)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='lastName']"))
    ).send_keys(con_lastname)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Apply']"))
    ).click()

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
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create Invoice']"))
    ).click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Edit Procedure/Item']"))
    ).click()

    price_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Price']"))
    )
    price_button.clear()
    price_button.send_keys("500")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()
    time.sleep(2)
    Add_button = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    )
    login.execute_script("arguments[0].click();", Add_button)

    time.sleep(2)
    select_subservice = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Sub_Service']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", select_subservice)
    select_subservice.click()

    price = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Price']"))
    )
    price.clear()
    price.send_keys("350")

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add']"))
    ).click()

    time.sleep(3)
    Add_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    )

    login.execute_script("arguments[0].click();", Add_button)

    fee_service = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Registration fee')]"))
    )
    login.execute_script("arguments[0].scrollIntoView();", fee_service)
    fee_service.click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()

    time.sleep(3)

    update_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']"))
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

    
    time.sleep(3)
    pay_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
    )
    login.execute_script("arguments[0].click();", pay_button)

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']"))
    ).click()

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mdc-button__label'])[1]"))
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

    print(f"Iteration {iteration + 1} completed")

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoice test cases sub-service assigned paid ")
@pytest.mark.parametrize("iteration", range(5))  # Adjust the range to set the number of iterations
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Invoice_appointment4(login, iteration):

    
    """
    Test invoice creation with multiple iterations.
    """
    print(f"Running iteration: {iteration + 1}")
    first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
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

    con_name = login.find_element(By.XPATH, "//input[@id='first_name']")
    con_name.send_keys(first_name)
    con_name = first_name
    con_lastname = login.find_element(By.XPATH, "//input[@id='last_name']")
    con_lastname.send_keys(last_name)
    con_lastname = last_name
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
    
    time.sleep(3)
    wait = WebDriverWait(login, 30) 

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//p-dropdown[@optionlabel='departmentName']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='ENT'])[1]"))
    ).click()

    wait.until(
       EC.presence_of_element_located(
           (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")) 
    ).click()

    time.sleep(2)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Venu Gopal']"))    
    ).click()

    time.sleep(2)
    # Today_Date = wait.until(EC.presence_of_element_located(
    #     (By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today']"))
    # )
    # Today_Date.click()
    # print("Today Date:", Today_Date.text)



    time.sleep(3)
    [year,month,day] = sub_days(27)
    print(year)
    print(month)
    print(day)
    time.sleep(2)
    
    year_month = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-label='Choose month and year']//span[@class='mat-mdc-button-touch-target']"))
    )
    login.execute_script("arguments[0].click();", year_month)
    
    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']"))
    # ).click()
    time.sleep(2)

    year_xpath = f"//span[normalize-space()='{year}']"
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, year_xpath))
    ).click()
    print(year_xpath)
    time.sleep(2)
    month_xpath = f"//span[contains(text(),'{month.upper()}')]" 
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, month_xpath))
    ).click()
    print(month_xpath)
    time.sleep(5)
    day_xpath = (
        f"//span[normalize-space()='{day}']"
    )
    print(day_xpath)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, day_xpath))
    ).click()


    time.sleep(3)
    # wait = WebDriverWait(login, 10)
    # time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
    # time_slot.click()
    # print("Time Slot:", time_slot.text)
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
    WebDriverWait(login, 10).until(
         EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

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

    time.sleep(3)

    dropdown1 = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
    )
    dropdown1.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='History'])[1]"))
    ).click()

    time.sleep(2)

    filter = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//i[@class='pi pi-filter-fill'])[1]"))
    )
    login.execute_script("arguments[0].click();", filter)

    time.sleep(3)
    name_option = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Name')]"))
    )
    login.execute_script("arguments[0].click();", name_option)

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='firstName']"))
    ).send_keys(con_name)

    time.sleep(1)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='lastName']"))
    ).send_keys(con_lastname)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Apply']"))
    ).click()

    time.sleep(5)

    # while True:
    #     try:
    #         print("before in loop")
    #         next_button = WebDriverWait(login, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
    #         )

    #         next_button.click()

    #     except:
    #         print("EC caught:")
    #         break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create Invoice']"))
    ).click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Edit Procedure/Item']"))
    ).click()

    price_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Price']"))
    )
    price_button.clear()
    price_button.send_keys("500")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()

    time.sleep(2)
    Add_button = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    )

    Add_button.click()

    time.sleep(2)
    select_subservice = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Sub_Service']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", select_subservice)
    select_subservice.click()

    price = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Price']"))
    )
    price.clear()
    price.send_keys("350")

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@class='p-multiselect-label p-placeholder'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Swathy']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add']"))
    ).click()

    time.sleep(3)
    Add_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    )

    login.execute_script("arguments[0].click();", Add_button)

    fee_service = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Registration fee')]"))
    )
    login.execute_script("arguments[0].scrollIntoView();", fee_service)
    fee_service.click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()

    time.sleep(3)
    update_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']"))
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

    
    time.sleep(3)
    pay_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
    )
    login.execute_script("arguments[0].click();", pay_button)

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

    print(f"Iteration {iteration + 1} completed")

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoice test cases sub-service unassigned unpaid ")
@pytest.mark.parametrize("iteration", range(5))  # Adjust the range to set the number of iterations
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Invoice_appointment5(login, iteration):

    
    """
    Test invoice creation with multiple iterations.
    """
    print(f"Running iteration: {iteration + 1}")
    first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
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

    con_name = login.find_element(By.XPATH, "//input[@id='first_name']")
    con_name.send_keys(first_name)
    con_name = first_name
    con_lastname = login.find_element(By.XPATH, "//input[@id='last_name']")
    con_lastname.send_keys(last_name)
    con_lastname = last_name
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
    
    time.sleep(3)
    wait = WebDriverWait(login, 30) 

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//p-dropdown[@optionlabel='departmentName']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Neurology']"))
    ).click()

    wait.until(
       EC.presence_of_element_located(
           (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")) 
    ).click()

    time.sleep(2)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Fabin JJ']"))    
    ).click()

    # time.sleep(2)
    # Today_Date = wait.until(EC.presence_of_element_located(
    #     (By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today']"))
    # )
    # Today_Date.click()
    # print("Today Date:", Today_Date.text)



    time.sleep(3)
    [year,month,day] = sub_days(27)
    print(year)
    print(month)
    print(day)
    time.sleep(2)
    
    year_month = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-label='Choose month and year']//span[@class='mat-mdc-button-touch-target']"))
    )
    login.execute_script("arguments[0].click();", year_month)
    
    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']"))
    # ).click()
    time.sleep(2)

    year_xpath = f"//span[normalize-space()='{year}']"
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, year_xpath))
    ).click()
    print(year_xpath)
    time.sleep(2)
    month_xpath = f"//span[contains(text(),'{month.upper()}')]" 
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, month_xpath))
    ).click()
    print(month_xpath)
    time.sleep(5)
    day_xpath = (
        f"//span[normalize-space()='{day}']"
    )
    print(day_xpath)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, day_xpath))
    ).click()


    time.sleep(3)
    # wait = WebDriverWait(login, 10)
    # time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
    # time_slot.click()
    # print("Time Slot:", time_slot.text)
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
    WebDriverWait(login, 10).until(
         EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

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

    time.sleep(3)

    dropdown1 = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
    )
    dropdown1.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='History'])[1]"))
    ).click()

    time.sleep(2)

    filter = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//i[@class='pi pi-filter-fill'])[1]"))
    )
    login.execute_script("arguments[0].click();", filter)

    time.sleep(3)
    name_option = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Name')]"))
    )
    login.execute_script("arguments[0].click();", name_option)

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='firstName']"))
    ).send_keys(con_name)

    time.sleep(1)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='lastName']"))
    ).send_keys(con_lastname)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Apply']"))
    ).click()

    time.sleep(5)

    # while True:
    #     try:
    #         print("before in loop")
    #         next_button = WebDriverWait(login, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
    #         )

    #         next_button.click()

    #     except:
    #         print("EC caught:")
    #         break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create Invoice']"))
    ).click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Edit Procedure/Item']"))
    ).click()

    price_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Price']"))
    )
    price_button.clear()
    price_button.send_keys("500")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()

    time.sleep(3)
    Add_button = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    )

    Add_button.click()

    time.sleep(3)
    select_subservice = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Sub_Service']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", select_subservice)
    select_subservice.click()


    price = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Price']"))
    )
    price.clear()
    price.send_keys("350")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add']"))
    ).click()

    time.sleep(3)
    Add_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    )

    login.execute_script("arguments[0].click();", Add_button)

    fee_service = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Registration fee')]"))
    )
    login.execute_script("arguments[0].scrollIntoView();", fee_service)
    fee_service.click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()

    time.sleep(3)

    update_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']"))
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

    
    time.sleep(3)


    pay_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
    )
    login.execute_script("arguments[0].click();", pay_button)

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']"))
    ).click()

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mdc-button__label'])[1]"))
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

    print(f"Iteration {iteration + 1} completed")

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoice test cases for invoice level discount paid Invoice ")
@pytest.mark.parametrize("iteration", range(5))  # Adjust the range to set the number of iterations
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Invoice_appointment6(login, iteration):

    
    """
    Test invoice creation with multiple iterations.
    """
    print(f"Running iteration: {iteration + 1}")
    first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
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

    con_name = login.find_element(By.XPATH, "//input[@id='first_name']")
    con_name.send_keys(first_name)
    con_name = first_name
    con_lastname = login.find_element(By.XPATH, "//input[@id='last_name']")
    con_lastname.send_keys(last_name)
    con_lastname = last_name
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
    
    time.sleep(3)
    wait = WebDriverWait(login, 30) 

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//p-dropdown[@optionlabel='departmentName']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='ENT'])[1]"))
    ).click()

    wait.until(
       EC.presence_of_element_located(
           (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")) 
    ).click()

    time.sleep(2)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Venu Gopal']"))    
    ).click()

    # time.sleep(2)
    # Today_Date = wait.until(EC.presence_of_element_located(
    #     (By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today']"))
    # )
    # Today_Date.click()
    # print("Today Date:", Today_Date.text)


    time.sleep(3)
    [year,month,day] = sub_days(27)
    print(year)
    print(month)
    print(day)
    time.sleep(2)
    
    year_month = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-label='Choose month and year']//span[@class='mat-mdc-button-touch-target']"))
    )
    login.execute_script("arguments[0].click();", year_month)
    
    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']"))
    # ).click()
    time.sleep(2)

    year_xpath = f"//span[normalize-space()='{year}']"
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, year_xpath))
    ).click()
    print(year_xpath)
    time.sleep(2)
    month_xpath = f"//span[contains(text(),'{month.upper()}')]" 
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, month_xpath))
    ).click()
    print(month_xpath)
    time.sleep(5)
    day_xpath = (
        f"//span[normalize-space()='{day}']"
    )
    print(day_xpath)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, day_xpath))
    ).click()


    time.sleep(3)
    # wait = WebDriverWait(login, 10)
    # time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
    # time_slot.click()
    # print("Time Slot:", time_slot.text)
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
    WebDriverWait(login, 10).until(
         EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

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

    time.sleep(3)

    dropdown1 = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
    )
    dropdown1.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='History'])[1]"))
    ).click()

    time.sleep(2)

    filter = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//i[@class='pi pi-filter-fill'])[1]"))
    )
    login.execute_script("arguments[0].click();", filter)

    time.sleep(3)
    name_option = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Name')]"))
    )
    login.execute_script("arguments[0].click();", name_option)

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='firstName']"))
    ).send_keys(con_name)

    time.sleep(1)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='lastName']"))
    ).send_keys(con_lastname)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Apply']"))
    ).click()

    time.sleep(5)

    # while True:
    #     try:
    #         print("before in loop")
    #         next_button = WebDriverWait(login, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
    #         )

    #         next_button.click()

    #     except:
    #         print("EC caught:")
    #         break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create Invoice']"))
    ).click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Edit Procedure/Item']"))
    ).click()

    price_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Price']"))
    )
    price_button.clear()
    price_button.send_keys("500")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()

    time.sleep(3)
    add_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    )
    add_button.click()

    time.sleep(3)
    select_subservice = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Sub_Service']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", select_subservice)
    select_subservice.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@class='p-multiselect-label p-placeholder'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Swathy']"))
    ).click()

    price = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Price']"))
    )
    price.clear()
    price.send_keys("350")
    

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add']"))
    ).click()

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='svg-icon svg-icon-lg svg-icon-success']//*[name()='svg']"))
    ).click()

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mdc-list-item__primary-text'][normalize-space()='Apply Discount'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//select[./option[text()='Select Discount']])[3]"))
        ).click()
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//option[normalize-space()='On Demand Discount'])[3]"))
        ).click()
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter Amount']"))
        ).send_keys("50")
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Apply'])[3]"))
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
    Add_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    )

    login.execute_script("arguments[0].click();", Add_button)

    fee_service = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Registration fee')]"))
    )
    login.execute_script("arguments[0].scrollIntoView();", fee_service)
    fee_service.click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()

    time.sleep(3)

    update_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']"))
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
    pay_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
    )
    login.execute_script("arguments[0].click();", pay_button)

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
    print(f"Iteration {iteration + 1} completed")

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoice test cases for Service level discount paid Invoice ")
@pytest.mark.parametrize("iteration", range(5))  # Adjust the range to set the number of iterations
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Invoice_appointment7(login, iteration):

    
    """
    Test invoice creation with multiple iterations.
    """
    print(f"Running iteration: {iteration + 1}")
    first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
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

    con_name = login.find_element(By.XPATH, "//input[@id='first_name']")
    con_name.send_keys(first_name)
    con_name = first_name
    con_lastname = login.find_element(By.XPATH, "//input[@id='last_name']")
    con_lastname.send_keys(last_name)
    con_lastname = last_name
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
    
    time.sleep(3)
    wait = WebDriverWait(login, 30) 

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//p-dropdown[@optionlabel='departmentName']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='ENT'])[1]"))
    ).click()

    wait.until(
       EC.presence_of_element_located(
           (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")) 
    ).click()

    time.sleep(2)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Venu Gopal']"))    
    ).click()

    # time.sleep(2)
    # Today_Date = wait.until(EC.presence_of_element_located(
    #     (By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today']"))
    # )
    # Today_Date.click()
    # print("Today Date:", Today_Date.text)

    time.sleep(3)
    [year,month,day] = sub_days(27)
    print(year)
    print(month)
    print(day)
    time.sleep(2)
    
    year_month = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-label='Choose month and year']//span[@class='mat-mdc-button-touch-target']"))
    )
    login.execute_script("arguments[0].click();", year_month)
    
    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']"))
    # ).click()
    time.sleep(2)

    year_xpath = f"//span[normalize-space()='{year}']"
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, year_xpath))
    ).click()
    print(year_xpath)
    time.sleep(2)
    month_xpath = f"//span[contains(text(),'{month.upper()}')]" 
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, month_xpath))
    ).click()
    print(month_xpath)
    time.sleep(5)
    day_xpath = (
        f"//span[normalize-space()='{day}']"
    )
    print(day_xpath)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, day_xpath))
    ).click()


    time.sleep(3)
    # wait = WebDriverWait(login, 10)
    # time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
    # time_slot.click()
    # print("Time Slot:", time_slot.text)
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
    WebDriverWait(login, 10).until(
         EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

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

    time.sleep(3)

    dropdown1 = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
    )
    dropdown1.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='History'])[1]"))
    ).click()

    time.sleep(2)

    filter = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//i[@class='pi pi-filter-fill'])[1]"))
    )
    login.execute_script("arguments[0].click();", filter)

    time.sleep(3)
    name_option = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Name')]"))
    )
    login.execute_script("arguments[0].click();", name_option)

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='firstName']"))
    ).send_keys(con_name)

    time.sleep(1)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='lastName']"))
    ).send_keys(con_lastname)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Apply']"))
    ).click()

    time.sleep(5)

    # while True:
    #     try:
    #         print("before in loop")
    #         next_button = WebDriverWait(login, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
    #         )

    #         next_button.click()

    #     except:
    #         print("EC caught:")
    #         break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create Invoice']"))
    ).click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Edit Procedure/Item']"))
    ).click()

    price_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Price']"))
    )
    price_button.clear()
    price_button.send_keys("500")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()

    time.sleep(3)
    add_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    )
    add_button.click()

    time.sleep(3)
    select_subservice = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Sub_Service']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", select_subservice)
    select_subservice.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@class='p-multiselect-label p-placeholder'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Swathy']"))
    ).click()

    price = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Price']"))
    )
    price.clear()
    price.send_keys("350")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add']"))
    ).click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[1]"))
    ).click()


    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mdc-list-item__primary-text'][normalize-space()='Apply Discount'])[1]"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//select[./option[text()='Select Discount']])[1]"))
        ).click()
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//option[normalize-space()='On Demand Discount'])[1]"))
        ).click()
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter Amount']"))
        ).send_keys("50")
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Apply'])[1]"))
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
    Add_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    )

    login.execute_script("arguments[0].click();", Add_button)

    fee_service = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Registration fee')]"))
    )
    login.execute_script("arguments[0].scrollIntoView();", fee_service)
    fee_service.click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()

    time.sleep(3)

    update_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']"))
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
    pay_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
    )
    login.execute_script("arguments[0].click();", pay_button)

    time.sleep()
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
    print(f"Iteration {iteration + 1} completed")

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoice test cases for invoice level discount unpaid Invoice ")
@pytest.mark.parametrize("iteration", range(5))  # Adjust the range to set the number of iterations
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Invoice_appointment8(login, iteration):

    
    """
    Test invoice creation with multiple iterations.
    """
    print(f"Running iteration: {iteration + 1}")
    first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
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

    con_name = login.find_element(By.XPATH, "//input[@id='first_name']")
    con_name.send_keys(first_name)
    con_name = first_name
    con_lastname = login.find_element(By.XPATH, "//input[@id='last_name']")
    con_lastname.send_keys(last_name)
    con_lastname = last_name
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
    
    time.sleep(3)
    wait = WebDriverWait(login, 30) 

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//p-dropdown[@optionlabel='departmentName']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='ENT'])[1]"))
    ).click()

    wait.until(
       EC.presence_of_element_located(
           (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")) 
    ).click()

    time.sleep(2)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Venu Gopal']"))    
    ).click()

    # time.sleep(2)
    # Today_Date = wait.until(EC.presence_of_element_located(
    #     (By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today']"))
    # )
    # Today_Date.click()
    # print("Today Date:", Today_Date.text)
    
    time.sleep(3)
    [year,month,day] = sub_days(27)
    print(year)
    print(month)
    print(day)
    time.sleep(2)
    
    year_month = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-label='Choose month and year']//span[@class='mat-mdc-button-touch-target']"))
    )
    login.execute_script("arguments[0].click();", year_month)
    
    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']"))
    # ).click()
    time.sleep(2)

    year_xpath = f"//span[normalize-space()='{year}']"
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, year_xpath))
    ).click()
    print(year_xpath)
    time.sleep(2)
    month_xpath = f"//span[contains(text(),'{month.upper()}')]" 
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, month_xpath))
    ).click()
    print(month_xpath)
    time.sleep(5)
    day_xpath = (
        f"//span[normalize-space()='{day}']"
    )
    print(day_xpath)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, day_xpath))
    ).click()
    time.sleep(2)
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
    WebDriverWait(login, 10).until(
         EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

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

    time.sleep(3)

    dropdown1 = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
    )
    dropdown1.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='History'])[1]"))
    ).click()

    time.sleep(2)

    filter = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//i[@class='pi pi-filter-fill'])[1]"))
    )
    login.execute_script("arguments[0].click();", filter)

    time.sleep(3)
    name_option = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Name')]"))
    )
    login.execute_script("arguments[0].click();", name_option)

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='firstName']"))
    ).send_keys(con_name)

    time.sleep(1)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='lastName']"))
    ).send_keys(con_lastname)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Apply']"))
    ).click()

    time.sleep(5)

    # while True:
    #     try:
    #         print("before in loop")
    #         next_button = WebDriverWait(login, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
    #         )

    #         next_button.click()

    #     except:
    #         print("EC caught:")
    #         break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create Invoice']"))
    ).click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Edit Procedure/Item']"))
    ).click()

    price_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Price']"))
    )
    price_button.clear()
    price_button.send_keys("500")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()

    time.sleep(3)
    add_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    )
    add_button.click()

    time.sleep(3)
    select_subservice = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Sub_Service']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", select_subservice)
    select_subservice.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@class='p-multiselect-label p-placeholder'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Swathy']"))
    ).click()

    price = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Price']"))
    )
    price.clear()
    price.send_keys("350")
    

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add']"))
    ).click()

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='svg-icon svg-icon-lg svg-icon-success']//*[name()='svg']"))
    ).click()

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mdc-list-item__primary-text'][normalize-space()='Apply Discount'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//select[./option[text()='Select Discount']])[3]"))
        ).click()
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//option[normalize-space()='On Demand Discount'])[3]"))
        ).click()
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter Amount']"))
        ).send_keys("50")
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Apply'])[3]"))
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
    Add_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    )

    login.execute_script("arguments[0].click();", Add_button)

    fee_service = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Registration fee')]"))
    )
    login.execute_script("arguments[0].scrollIntoView();", fee_service)
    fee_service.click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()

    time.sleep(3)
    update_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']"))
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
    pay_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
    )
    login.execute_script("arguments[0].click();", pay_button)

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']"))
    ).click()

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mdc-button__label'])[1]"))
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
    print(f"Iteration {iteration + 1} completed")


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoice test cases for Service level discount unpaid Invoice ")
@pytest.mark.parametrize("iteration", range(5))  # Adjust the range to set the number of iterations
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Invoice_appointment9(login, iteration):

    
    """
    Test invoice creation with multiple iterations.
    """
    print(f"Running iteration: {iteration + 1}")
    first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
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

    con_name = login.find_element(By.XPATH, "//input[@id='first_name']")
    con_name.send_keys(first_name)
    con_name = first_name
    con_lastname = login.find_element(By.XPATH, "//input[@id='last_name']")
    con_lastname.send_keys(last_name)
    con_lastname = last_name
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
    
    time.sleep(3)
    wait = WebDriverWait(login, 30) 

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//p-dropdown[@optionlabel='departmentName']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='ENT'])[1]"))
    ).click()

    wait.until(
       EC.presence_of_element_located(
           (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")) 
    ).click()

    time.sleep(2)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Venu Gopal']"))    
    ).click()

    # time.sleep(2)
    # Today_Date = wait.until(EC.presence_of_element_located(
    #     (By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today']"))
    # )
    # Today_Date.click()
    # print("Today Date:", Today_Date.text)

    time.sleep(3)
    [year,month,day] = sub_days(27)
    print(year)
    print(month)
    print(day)
    time.sleep(2)
    
    year_month = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-label='Choose month and year']//span[@class='mat-mdc-button-touch-target']"))
    )
    login.execute_script("arguments[0].click();", year_month)
    
    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']"))
    # ).click()
    time.sleep(2)

    year_xpath = f"//span[normalize-space()='{year}']"
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, year_xpath))
    ).click()
    print(year_xpath)
    time.sleep(2)
    month_xpath = f"//span[contains(text(),'{month.upper()}')]" 
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, month_xpath))
    ).click()
    print(month_xpath)
    time.sleep(5)
    day_xpath = (
        f"//span[normalize-space()='{day}']"
    )
    print(day_xpath)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, day_xpath))
    ).click()


    time.sleep(3)
    # wait = WebDriverWait(login, 10)
    # time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
    # time_slot.click()
    # print("Time Slot:", time_slot.text)
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
    WebDriverWait(login, 10).until(
         EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

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

    time.sleep(3)

    dropdown1 = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
    )
    dropdown1.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='History'])[1]"))
    ).click()

    time.sleep(2)

    filter = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//i[@class='pi pi-filter-fill'])[1]"))
    )
    login.execute_script("arguments[0].click();", filter)

    time.sleep(3)
    name_option = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Name')]"))
    )
    login.execute_script("arguments[0].click();", name_option)

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='firstName']"))
    ).send_keys(con_name)

    time.sleep(1)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='lastName']"))
    ).send_keys(con_lastname)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Apply']"))
    ).click()

    time.sleep(5)

    # while True:
    #     try:
    #         print("before in loop")
    #         next_button = WebDriverWait(login, 10).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
    #         )

    #         next_button.click()

    #     except:
    #         print("EC caught:")
    #         break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create Invoice']"))
    ).click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Edit Procedure/Item']"))
    ).click()

    price_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Price']"))
    )
    price_button.clear()
    price_button.send_keys("500")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()

    time.sleep(3)
    add_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    )
    add_button.click()

    time.sleep(3)
    select_subservice = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Sub_Service']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", select_subservice)
    select_subservice.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@class='p-multiselect-label p-placeholder'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Swathy']"))
    ).click()

    price = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Price']"))
    )
    price.clear()
    price.send_keys("350")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add']"))
    ).click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[1]"))
    ).click()


    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mdc-list-item__primary-text'][normalize-space()='Apply Discount'])[1]"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//select[./option[text()='Select Discount']])[1]"))
        ).click()
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//option[normalize-space()='On Demand Discount'])[1]"))
        ).click()
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter Amount']"))
        ).send_keys("50")
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Apply'])[1]"))
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
    Add_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
    )

    login.execute_script("arguments[0].click();", Add_button)

    fee_service = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Registration fee')]"))
    )
    login.execute_script("arguments[0].scrollIntoView();", fee_service)
    fee_service.click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Add'])[1]"))
    ).click()

    time.sleep(3)
    update_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']"))
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
    pay_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
    )
    login.execute_script("arguments[0].click();", pay_button)

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']"))
    ).click()

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mdc-button__label'])[1]"))
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
    print(f"Iteration {iteration + 1} completed")