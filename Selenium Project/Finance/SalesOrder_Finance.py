from Framework.common_utils import *
from Framework.common_dates_utils import *
import re

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_WalkinOrder_confirmed and completed_order")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_walkin_Order(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search customers']", "9400553615")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 131']")
        time.sleep(2)
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
    