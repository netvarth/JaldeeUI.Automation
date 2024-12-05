from selenium.webdriver.chrome.webdriver import WebDriver
from Framework.common_utils import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import allure
from allure_commons.types import AttachmentType
import os
first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoice test cases")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Invoice_appointment(login):

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
    # login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
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
    Today_Date = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today']"))
    )
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




@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoice test cases2")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Invoice_appointment2(login):

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
    # login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
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

    time.sleep(2)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//p-dropdown[@optionlabel='departmentName']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Dental']"))
    ).click()






@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoice test cases")
@pytest.mark.parametrize("iteration", range(3))  # Adjust the range to set the number of iterations
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Invoice_appointment3(login, iteration):

    

    """
    Test invoice creation with multiple iterations.
    """
    print(f"Running iteration: {iteration + 1}")
    
    # Step 1: Navigate to the appointments page
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//b[contains(text(),'Create New Patient')]"))
    ).click()

    # Fill patient details
    login.implicitly_wait(3)
    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
    login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

    # Handle snack bar notifications
    try:
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snack bar message:", snack_bar.text)
    except:
        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
        )
        print("Snack bar error message:", snack_bar.text)

    # Continue with rest of the test logic (e.g., appointment scheduling, invoice generation)
    # ... (rest of the test logic from original code)

    print(f"Iteration {iteration + 1} completed")
