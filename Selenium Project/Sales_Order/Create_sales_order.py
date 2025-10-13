import time
import allure

from Framework.common_utils import *
from Framework.consumer_common_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating a walk-in sales order and invoice, and Share payment link")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_1(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        
        
        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))).click()

        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
    
        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Create Order')])[1]"))
        ).click()
        
        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='New customer'])[1]"))
        ).click()

        
        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='p-multiselect-label p-placeholder'])[1]"))
        ).click()
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Next'])[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Search items'])[1]"))
        ).send_keys("item")
        time.sleep(3)

        element = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Item_1')])[1]")))
        click_to_element(login, element)

        # time.sleep(3)
        # # Re-locate to avoid stale reference
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(text(),'Item_1')])[1]")))
        # element.click()


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Blue'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[.//span[normalize-space(text())='Select Item']])[1]"))
        ).click()

        

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Add Item'])[1]")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@type='checkbox' and contains(@class,'mdc-checkbox__native-control')])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[span[normalize-space()='Select Item']]"))
        ).click()

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//i[@class='pi pi-check'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='fa fa-caret-down'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Confirm Order'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Create Invoice'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='View Invoice'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Share Payment Link'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='mdc-button__label'])[1]")

        message = get_snack_bar_message(login)
        print("Snack bar message:", message)

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Complete Order'])[1]")

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Orders'])[1]")

        time.sleep(2)
        # Locate the first row of the orders table
        first_row = wait.until(
            EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]"))
        )

        # Get consumer name from the first row
        first_row_consumer = first_row.find_element(
            By.XPATH, "./td[1]//span[@class='fw-bold text-capitalize']"
        ).text.strip()

        # Get order status from the first row
        first_row_status = first_row.find_element(
            By.XPATH, "./td[4]//span"
        ).text.strip()

        print(f"First row -> Consumer: {first_row_consumer}, Status: {first_row_status}")

        # Assertions
        assert first_row_consumer == consumer_name, f"Expected consumer {consumer_name}, but found {first_row_consumer}"
        assert first_row_status == "Completed", f"Expected status Completed, but found {first_row_status}"

        time.sleep(5)
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating a walk-in sales order and invoice, and pay now.")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_2(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)


        
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
    
        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Create Order')])[1]"))
        ).click()
        
        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='New customer'])[1]"))
        ).click()

        
        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='p-multiselect-label p-placeholder'])[1]"))
        ).click()
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='p-checkbox-box'])[2]"))
        ).click()

        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Next'])[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Search items'])[1]"))
        ).send_keys("item")
        time.sleep(3)

        element = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Item_1')])[1]")))
        click_to_element(login, element)


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Blue'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[.//span[normalize-space(text())='Select Item']])[1]"))
        ).click()

        

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Add Item'])[1]")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@type='checkbox' and contains(@class,'mdc-checkbox__native-control')])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[span[normalize-space()='Select Item']]"))
        ).click()
       
        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//i[@class='pi pi-check'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='fa fa-caret-down'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Confirm Order'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Create Invoice'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='View Invoice'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Pay by Cash'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Pay'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Yes'])[1]")

        message = get_snack_bar_message(login)
        print("Snack bar message:", message)

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Complete Order'])[1]")

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Orders'])[1]")

        time.sleep(2)
        # Locate the first row of the orders table
        first_row = wait.until(
            EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]"))
        )

        # Get consumer name from the first row
        first_row_consumer = first_row.find_element(
            By.XPATH, "./td[1]//span[@class='fw-bold text-capitalize']"
        ).text.strip()

        # Get order status from the first row
        first_row_status = first_row.find_element(
            By.XPATH, "./td[4]//span"
        ).text.strip()

        print(f"First row -> Consumer: {first_row_consumer}, Status: {first_row_status}")

        # Assertions
        assert first_row_consumer == consumer_name, f"Expected consumer {consumer_name}, but found {first_row_consumer}"
        assert first_row_status == "Completed", f"Expected status Completed, but found {first_row_status}"
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating a walk-in sales order and invoice, and Settle Invoice.")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_3(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)


        
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
    
        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Create Order')])[1]"))
        ).click()
        
        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='New customer'])[1]"))
        ).click()

        
        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='p-multiselect-label p-placeholder'])[1]"))
        ).click()
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='p-checkbox-box'])[2]"))
        ).click()

        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Next'])[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Search items'])[1]"))
        ).send_keys("item")
        time.sleep(3)

        element = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Item_1')])[1]")))
        click_to_element(login, element)


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Blue'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[.//span[normalize-space(text())='Select Item']])[1]"))
        ).click()

        

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Add Item'])[1]")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@type='checkbox' and contains(@class,'mdc-checkbox__native-control')])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[span[normalize-space()='Select Item']]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-check'])[2]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='fa fa-caret-down'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Confirm Order'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Create Invoice'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='View Invoice'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Settle Invoice'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Confirm & Settle Invoice'])[1]")


        message = get_snack_bar_message(login)
        print("Snack bar message:", message)

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Complete Order'])[1]")

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Orders'])[1]")

        time.sleep(2)
        # Locate the first row of the orders table
        first_row = wait.until(
            EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]"))
        )

        # Get consumer name from the first row
        first_row_consumer = first_row.find_element(
            By.XPATH, "./td[1]//span[@class='fw-bold text-capitalize']"
        ).text.strip()

        # Get order status from the first row
        first_row_status = first_row.find_element(
            By.XPATH, "./td[4]//span"
        ).text.strip()

        print(f"First row -> Consumer: {first_row_consumer}, Status: {first_row_status}")

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating a walk-in sales order and invoice, and cancel Invoice.")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_4(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)


        
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
    
        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Create Order')])[1]"))
        ).click()
        
        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='New customer'])[1]"))
        ).click()

        
        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='p-multiselect-label p-placeholder'])[1]"))
        ).click()
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='p-checkbox-box'])[2]"))
        ).click()

        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Next'])[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Search items'])[1]"))
        ).send_keys("item")
        time.sleep(3)

        element = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Item_1')])[1]")))
        click_to_element(login, element)


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Blue'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[.//span[normalize-space(text())='Select Item']])[1]"))
        ).click()

        

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Add Item'])[1]")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@type='checkbox' and contains(@class,'mdc-checkbox__native-control')])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[span[normalize-space()='Select Item']]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-check'])[2]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='fa fa-caret-down'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Confirm Order'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Create Invoice'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='View Invoice'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Cancel Invoice'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[@class='cs-btn btn btn-primary settle-button'])[1]")

        message = get_snack_bar_message(login)
        print("Snack bar message:", message)

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Complete Order'])[1]")

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Orders'])[1]")

        time.sleep(2)
        # Locate the first row of the orders table
        first_row = wait.until(
            EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]"))
        )

        # Get consumer name from the first row
        first_row_consumer = first_row.find_element(
            By.XPATH, "./td[1]//span[@class='fw-bold text-capitalize']"
        ).text.strip()

        # Get order status from the first row
        first_row_status = first_row.find_element(
            By.XPATH, "./td[4]//span"
        ).text.strip()

        print(f"First row -> Consumer: {first_row_consumer}, Status: {first_row_status}")

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating a online sales order and invoice, and cancel Invoice.")
@pytest.mark.parametrize("url" , [(sales_order_consumer_scale_url)])
def test_create_sales_order_5(consumer_login):

    try:

        time.sleep(5)
        wait_and_locate_click(consumer_login, By.XPATH, "(//div[normalize-space()='Item_1'])[1]")

        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "(//button[normalize-space()='Blue'])[1]")

        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "(//button[normalize-space()='Add to cart'])[1]")

        get_toast_message(consumer_login)
        print("Toast message:", get_toast_message(consumer_login))

        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "(//button[normalize-space()='Buy it now'])[1]")

        first_name, last_name, phonenumber, email, otp = create_consumer_data()

        time.sleep(2)
        wait_and_send_keys(consumer_login, By.XPATH, "(//input[@placeholder='81234 56789'])[1]", phonenumber)

        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "(//button[normalize-space()='Continue'])[1]")

        # time.sleep(2)
        # consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

        time.sleep(5)

        otp_digits = "55555"
       
        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@class,'otp-input')]")
            )
        )
        # print("Number of OTP input fields:", len(otp_inputs))
        # print(otp_inputs)

        for i, otp_input in enumerate(otp_inputs):

            # print(i)
            # print(otp_input)
            otp_input.send_keys(otp_digits[i])

        consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

        wait_and_locate_click(consumer_login, By.XPATH, "(//*[name()='svg'][@class='p-dropdown-trigger-icon p-icon'])[1]")

        time.sleep(1)
        options = consumer_login.find_elements(By.XPATH, "//ul[@role='listbox']//li[@role='option']")

        # Pick one randomly
        random_option = random.choice(options)

        # Click on it
        random_option.click()

        print("Selected option:", random_option.text.strip())

        wait_and_send_keys(consumer_login, By.XPATH, "(//input[@id='first_name'])[1]", first_name)

        wait_and_send_keys(consumer_login, By.XPATH, "(//input[@id='first_name'])[2]", last_name)

        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "(//span[normalize-space()='Next'])[1]")

        time.sleep(3)
        wait_and_send_keys(consumer_login, By.XPATH, "(//input[@id='ownerName'])[1]", first_name)
        wait_and_send_keys(consumer_login, By.XPATH, "(//input[@id='ownerName'])[2]", last_name)
        wait_and_send_keys(consumer_login, By.XPATH, "(//input[@id='email'])[1]", email)
        wait_and_send_keys(consumer_login, By.XPATH, "(//input[@placeholder='81234 56789'])[1]", phonenumber)



        time.sleep(5)

    except Exception as e:
        allure.attach(
            consumer_login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e