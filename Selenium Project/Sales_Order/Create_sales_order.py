import time
import allure

from Framework.common_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating sales order")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order(login):

    time.sleep(5)
    wait = WebDriverWait(login, 20)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[contains(text(),'Create Order')])[1]"))
    ).click()
    
    first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
    
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='New customer'])[1]"))
    ).click()

    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
    login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

    # time.sleep(3)

    # wait.until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
    # ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='Next'])[1]"))
    ).click()

    time.sleep(3)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//input[@placeholder='Search items'])[1]"))
    ).send_keys("sales")
    time.sleep(3)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[contains(text(),'Sales_order_item_184a')])[1]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Black'])[1]"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//i[@class='pi pi-check'])[1]"))
    ).click()


    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='Add Item'])[1]"))
    ).click()

    time.sleep(2)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//input[@type='checkbox' and contains(@id, 'mat-mdc-checkbox')])[1]"))
     ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Green'])[1]"))
    ).click()


    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//i[@class='pi pi-check'])[2]"))
    ).click()
    
    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[1]"))
    ).click()


    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='Confirm Order'])[1]"))
    ).click()

     

