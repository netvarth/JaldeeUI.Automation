from Framework.common_utils import *
from Framework.common_dates_utils import *
import re

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_WalkinOrder_confirmed and completed_order")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_create_walkin_Order(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "/html[1]/body[1]/app-root[1]/app-business[1]/div[1]/app-sidebar-menu[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]/div[1]/span[1]/span[1]/img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search customers']", "9207206005")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 2']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[5]")
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[2]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        time.sleep(2)
        confirmorder.click()
        print("Order Confirmed")
        time.sleep(3)
        complete_Order = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Complete Order']"))
        )
        scroll_to_element(login, complete_Order)
        time.sleep(2)
        complete_Order.click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        print("Toast Message:", toast_message.text)
        order_id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='order-id ng-star-inserted']"))
        )
        full_order_id = order_id.text  
        actual_order_formatid = full_order_id.replace('#', '').strip()  
        parts = actual_order_formatid.split()  
        actual_order_id = f"{parts[0]} '{parts[1]}'"  
        print("Actual_OrderID:",actual_order_id) 
        time.sleep(3)
        create_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Invoice']"))
        )
        create_Invoice.click()
        time.sleep(3)
        view_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='View Invoice']"))
        )
        scroll_to_element(login, view_Invoice)
        view_Invoice.click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[4]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        orderinvoices = WebDriverWait(login, 15).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Order Invoices']"))
        )
        scroll_to_element(login,orderinvoices)
        time.sleep(2) 
        orderinvoices.click()
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]") 
        time.sleep(2)
        order_invoice_Id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'font-small') and contains(text(), 'Order No# :')]"))
        )
        order_text = order_invoice_Id.text

        # Use regex to extract the order number (i.e., the digits after "Order No# :")
        match = re.search(r'Order No# : (\d+)', order_text)

        if match:
            # Extracted order number
            order_number = match.group(1)
            formatted_order = f"Order '{order_number}'"
    
            print(f"Formatted Order: {formatted_order}")
        else:
            print("Order number not found")

        expected_order_invoice_Id = formatted_order
        print("Expected_OrderId:",expected_order_invoice_Id)
        print(f"Expected_OrderId: '{expected_order_invoice_Id}', Actual_OrderId: '{actual_order_id}'")
        assert actual_order_id == expected_order_invoice_Id, f"Expected_OrderId: '{expected_order_invoice_Id}', but got Actual_OrderId: '{actual_order_id}'"
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Share Invoice']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "The invoice has been sent to the customer"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(3)
    except Exception as e:
        
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    



from Framework.consumer_common_utils import *
from Framework.common_dates_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Online_Order")
@pytest.fixture()

def orderinvoiceid(consumer_login):
    try:
        time.sleep(5)
        consumer_data = create_consumer_data()
        # consumer_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        Dessert = WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='category-name d-flex justify-content-between'][normalize-space()='Dessert']"))
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", Dessert)
        time.sleep(5)
        Dessert.click()
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//button[normalize-space()='Add']")
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        ).send_keys(consumer_data['phonenumber'])
        print("New Consumer Phone Number:", consumer_data['phonenumber'])
        consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        time.sleep(5)
        otp_inputs = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )
        for i, otp_input in enumerate(otp_inputs):
            otp_input.send_keys(consumer_data['otp'][i])
        consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@id='first_name'])[1]"))
        ).send_keys(consumer_data['first_name'])
        print("New Consumer Firstname:", consumer_data['first_name'])
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='first_name'])[2]"))
        ).send_keys(consumer_data['last_name'])
        print("New Consumer Lastname:", consumer_data['last_name'])
        consumer_login.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        time.sleep(5)
        print("Toast Message: Item added to cart")
        wait_and_locate_click(consumer_login, By.XPATH, "//span[@class='cart-count ng-star-inserted']")
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//button[normalize-space()='Checkout']")
        time.sleep(3)
        WebDriverWait(consumer_login, 15).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@id='ownerName'])[1]"))
        ).send_keys(consumer_data['first_name'])
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='ownerName'])[2]"))
        ).send_keys(consumer_data['last_name'])
        email = consumer_data['email']
        email_input = WebDriverWait(consumer_login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='email']")) 
        )
        email_input.send_keys(email)
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        ).send_keys(consumer_data['phonenumber'])
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname='address']"))
        ).send_keys("Jaldee Soft PVT LTD")
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='pinCode']"))
        ).send_keys("680305")
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='landMark']"))
        ).send_keys("CrownTower")
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='city']"))
        ).send_keys("Thrissur")
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='state']"))
        ).send_keys("Kerala")
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='country']"))
        ).send_keys("India")
        save_address = WebDriverWait(consumer_login, 15).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save & Proceed']"))
        )
        scroll_to_element(consumer_login, save_address)
        time.sleep(2)
        save_address.click()
        time.sleep(3)
        confirm = WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Confirm']"))
        )
        scroll_to_element(consumer_login, confirm)
        time.sleep(2)
        confirm.click()
        time.sleep(3)
        NB = WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'NET BANKING')]"))
        )
        scroll_to_element(consumer_login, NB)
        time.sleep(2)
        NB.click()
        time.sleep(2)
        WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Pay']"))
        ).click()
        time.sleep(2)
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[contains(@class,'ptm-paymode-name ptm-lightbold')]")
        )
        ).click()
        time.sleep(2)
        WebDriverWait(consumer_login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='SBI']"))
        ).click()
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH,"//div[contains(@class,'ptm-overlay-wrapper btn-enabled')]//img[contains(@class,'ptm-lock-img')]"))
        ).click()
         # Handle the popup window
        main_window_handle = consumer_login.current_window_handle
        WebDriverWait(consumer_login, 10).until(EC.new_window_is_opened)
        all_window_handles = consumer_login.window_handles
        new_window_handle = None
        for handle in all_window_handles:
            if handle != main_window_handle:
                new_window_handle = handle
                break
         # Switch to the new window
        consumer_login.switch_to.window(new_window_handle)
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Successful']"))
        ).click()
        time.sleep(5)
        # Optionally, switch back to the main window
        consumer_login.switch_to.window(main_window_handle)
        time.sleep(5)
        ordernumber = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='order-id']"))
        )
        order_id = ordernumber.text
        confirmed_order_id= order_id.split("#")[-1].strip()
        print("Confirmed Order ID :", confirmed_order_id)
        confirmation_text = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-confirmed ng-star-inserted']"))
        )
        message = confirmation_text.text
        expected_message = "ORDER CONFIRMED"
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        print("Test passed:", message)
        invoice = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Invoice']"))
        )
        scroll_to_element(consumer_login, invoice)
        time.sleep(2)
        invoice.click()
        time.sleep(3)
        invoiceid = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.columns.ng-star-inserted span.dynamic.fw-bold"))
        )
        orderinvoiceid = invoiceid.text
        print("orderinvoiceid:", orderinvoiceid)
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "//i[@class='fa fa-arrow-left']")
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//button[normalize-space()='Home']")
        time.sleep(2)
        return orderinvoiceid
    finally:
            consumer_login.quit()


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Online order invoice and provider side order invoice on Finance Dashboard")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_provider_orderinvoice(orderinvoiceid,login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[4]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        orderinvoices = WebDriverWait(login, 15).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Order Invoices']"))
        )
        scroll_to_element(login,orderinvoices)
        time.sleep(2) 
        orderinvoices.click()
        time.sleep(2)
        invoiceid = WebDriverWait(login, 15).until(
            EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[1]"))
        )
        expected_orderinvoiceid = invoiceid.text
        print("Expected_orderinvoiceid:",expected_orderinvoiceid )
        print(f"Expected_orderinvoiceid: '{expected_orderinvoiceid}', Actual_OrderId: '{orderinvoiceid}'")
        assert orderinvoiceid == expected_orderinvoiceid, f"Expected_orderinvoiceid: '{expected_orderinvoiceid}', but got Actual_OrderId: '{orderinvoiceid}'"
        time.sleep(3)
        view_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]"))
        )
        scroll_to_element(login, view_Invoice)
        view_Invoice.click()
        time.sleep(3)
        scroll_to_window(login)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Settle Invoice']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "Invoice Settled Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(2)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e
    
from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.common import TimeoutException , JavascriptException
from selenium.webdriver.support.ui import Select
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Print Order Invoice")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_print_order_invoice(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[4]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        orderinvoices = WebDriverWait(login, 15).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Order Invoices']"))
        )
        scroll_to_element(login,orderinvoices)
        time.sleep(2) 
        orderinvoices.click()
        time.sleep(2)
        view_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]"))
        )
        scroll_to_element(login, view_Invoice)
        view_Invoice.click()
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='for-xs']"))
        ).click()
        
        login.switch_to.window(login.window_handles[-1])
        dropdown = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'print-preview-app'))
        )
        try:
            dropdown = WebDriverWait(login, 20).until(
                EC.presence_of_element_located((By.XPATH, "//print-preview-app//print-preview-sidebar//print-preview-destination-settings//print-preview-destination-select//select[@class='md-select']"))
            )

            # JavaScript to find the dropdown element within nested shadow DOMs
            dropdown_script = """
                return document.querySelector('print-preview-app').shadowRoot
                    .querySelector('print-preview-sidebar').shadowRoot
                    .querySelector('print-preview-destination-settings').shadowRoot
                    .querySelector('print-preview-destination-select').shadowRoot
                    .querySelector('select.md-select');
                """

            # Executing the script to find the dropdown element
            dropdown = login.execute_script(dropdown_script)
            select = Select(dropdown)
            select.select_by_visible_text("Save as PDF")
            time.sleep(3)
            save_button_script = """
                return document.querySelector('print-preview-app').shadowRoot
                .querySelector('print-preview-sidebar').shadowRoot
                .querySelector('print-preview-button-strip').shadowRoot
                .querySelector('cr-button.action-button').click();
                """
            login.execute_script(save_button_script)
            time.sleep(3)
            pyautogui.click()
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(3)
            login.switch_to.window(login.window_handles[0])
        except JavascriptException as e:
            print('element not found')
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e
    