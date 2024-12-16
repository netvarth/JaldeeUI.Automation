from Framework.common_utils import *
from Framework.common_dates_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_WalkinOrder_completed")
@pytest.mark.parametrize("url", ["https://www.jaldee.com/business/"])
def test_create_walkin_Order(login):
    current_date = datetime.now().strftime("%d-%m-%Y")
    print("Post-Deployment Walkin Order via Payment Link",current_date)
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search customers']", "9400553615")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 4']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[3]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        time.sleep(2)
        confirmorder.click()
        time.sleep(5)
        confirm_order_id = login.find_element(By.XPATH, "//span[@class='order-id ng-star-inserted']")
        confirmed_order = confirm_order_id.text
        Order_Confirmed_Id = '#' + confirmed_order.split('#')[-1] 
        print("Confirmed_order_Id :", Order_Confirmed_Id )
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )
        actual_message = confirmorder.text
        expected_message = "Confirmed"
        print(f"Expected status: '{expected_message}', Actual status: '{confirmorder.text}'")
        assert actual_message == expected_message, f"Expected message '{expected_message} but got Message '{actual_message}'"
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
        expected_message = "Order Completed Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{toast_message.text}'")
        assert toast_message.text == expected_message, f"Expected toast message '{expected_message}', but got '{toast_message.text}'"
        time.sleep(5)
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
        paymentlink = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        scroll_to_element(login, paymentlink)
        paymentlink.click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[@aria-label='Share Payment Link']")
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "The invoice has been sent to the customer"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Orders'])[1]") 
        time.sleep(3)
        Order_first_row = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[2]"))
        ).text
        View_Orders_first_value = '#' + Order_first_row.split('#')[-1]  
        print(f"View_Order_first_value : {View_Orders_first_value}")
        time.sleep(3)
        print(f"Expected View Order ID: '{View_Orders_first_value}', Actual Confirmed Order ID: '{Order_Confirmed_Id}'")
        assert Order_Confirmed_Id == View_Orders_first_value, f"Expected View Order ID '{View_Orders_first_value} but got Confirmed Order ID '{Order_Confirmed_Id}'"
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

from Framework.common_utils import *
from Framework.common_dates_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_WalkinOrder_completed")
@pytest.mark.parametrize("url", ["https://www.jaldee.com/business/"])
def test_create_walkin_Order(login):
    current_date = datetime.now().strftime("%d-%m-%Y")
    print("Post-Deployment Walkin Order via Pay By Cash",current_date)
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search customers']", "9400553615")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 4']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[3]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        time.sleep(2)
        confirmorder.click()
        time.sleep(5)
        confirm_order_id = login.find_element(By.XPATH, "//span[@class='order-id ng-star-inserted']")
        confirmed_order = confirm_order_id.text
        Order_Confirmed_Id = '#' + confirmed_order.split('#')[-1] 
        print("Confirmed_order_Id :", Order_Confirmed_Id )
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )
        actual_message = confirmorder.text
        expected_message = "Confirmed"
        print(f"Expected status: '{expected_message}', Actual status: '{confirmorder.text}'")
        assert actual_message == expected_message, f"Expected message '{expected_message} but got Message '{actual_message}'"
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
        expected_message = "Order Completed Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{toast_message.text}'")
        assert toast_message.text == expected_message, f"Expected toast message '{expected_message}', but got '{toast_message.text}'"
        time.sleep(5)
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
        paymentlink = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        scroll_to_element(login, paymentlink)
        paymentlink.click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[@aria-label='Share Payment Link']")
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "The invoice has been sent to the customer"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Orders'])[1]") 
        time.sleep(3)
        Order_first_row = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[2]"))
        ).text
        View_Orders_first_value = '#' + Order_first_row.split('#')[-1]  
        print(f"View_Order_first_value : {View_Orders_first_value}")
        time.sleep(3)
        print(f"Expected View Order ID: '{View_Orders_first_value}', Actual Confirmed Order ID: '{Order_Confirmed_Id}'")
        assert Order_Confirmed_Id == View_Orders_first_value, f"Expected View Order ID '{View_Orders_first_value} but got Confirmed Order ID '{Order_Confirmed_Id}'"
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    


from Framework.common_utils import *
from Framework.common_dates_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_WalkinOrder_completed")
@pytest.mark.parametrize("url", ["https://www.jaldee.com/business/"])
def test_create_walkin_Order(login):
    current_date = datetime.now().strftime("%d-%m-%Y")
    print("Post-Deployment Walkin Order via Pay By Others",current_date)
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search customers']", "9400553615")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 4']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[3]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        time.sleep(2)
        confirmorder.click()
        time.sleep(5)
        confirm_order_id = login.find_element(By.XPATH, "//span[@class='order-id ng-star-inserted']")
        confirmed_order = confirm_order_id.text
        Order_Confirmed_Id = '#' + confirmed_order.split('#')[-1] 
        print("Confirmed_order_Id :", Order_Confirmed_Id )
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )
        actual_message = confirmorder.text
        expected_message = "Confirmed"
        print(f"Expected status: '{expected_message}', Actual status: '{confirmorder.text}'")
        assert actual_message == expected_message, f"Expected message '{expected_message} but got Message '{actual_message}'"
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
        expected_message = "Order Completed Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{toast_message.text}'")
        assert toast_message.text == expected_message, f"Expected toast message '{expected_message}', but got '{toast_message.text}'"
        time.sleep(5)
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
        paymentlink = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        scroll_to_element(login, paymentlink)
        paymentlink.click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[@aria-label='Share Payment Link']")
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "The invoice has been sent to the customer"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Orders'])[1]") 
        time.sleep(3)
        Order_first_row = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[2]"))
        ).text
        View_Orders_first_value = '#' + Order_first_row.split('#')[-1]  
        print(f"View_Order_first_value : {View_Orders_first_value}")
        time.sleep(3)
        print(f"Expected View Order ID: '{View_Orders_first_value}', Actual Confirmed Order ID: '{Order_Confirmed_Id}'")
        assert Order_Confirmed_Id == View_Orders_first_value, f"Expected View Order ID '{View_Orders_first_value} but got Confirmed Order ID '{Order_Confirmed_Id}'"
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    





    


from Framework.common_utils import *
from Framework.common_dates_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_WalkinOrder_completed_Paybycash")
@pytest.mark.parametrize("url", ["https://www.jaldee.com/business/"])
def test_create_walkin_Order_paybycash(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search customers']", "9400553615")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 4']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[3]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        time.sleep(2)
        confirmorder.click()
        time.sleep(5)
        confirm_order_id = login.find_element(By.XPATH, "//span[@class='order-id ng-star-inserted']")
        confirmed_order = confirm_order_id.text
        Order_Confirmed_Id = '#' + confirmed_order.split('#')[-1] 
        print("Confirmed_order_Id :", Order_Confirmed_Id )
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )
        actual_message = confirmorder.text
        expected_message = "Confirmed"
        print(f"Expected status: '{expected_message}', Actual status: '{confirmorder.text}'")
        assert actual_message == expected_message, f"Expected message '{expected_message} but got Message '{actual_message}'"
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
        expected_message = "Order Completed Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{toast_message.text}'")
        assert toast_message.text == expected_message, f"Expected toast message '{expected_message}', but got '{toast_message.text}'"
        time.sleep(5)
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
        paymentlink = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        scroll_to_element(login, paymentlink)
        paymentlink.click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Pay by Cash']")
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Pay']")
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "Payment completed successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(5)
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
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Orders'])[1]") 
        time.sleep(3)
        Order_first_row = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[2]"))
        ).text
        View_Orders_first_value = '#' + Order_first_row.split('#')[-1]  
        print(f"View_Order_first_value : {View_Orders_first_value}")
        time.sleep(3)
        print(f"Expected View Order ID: '{View_Orders_first_value}', Actual Confirmed Order ID: '{Order_Confirmed_Id}'")
        assert Order_Confirmed_Id == View_Orders_first_value, f"Expected View Order ID '{View_Orders_first_value} but got Confirmed Order ID '{Order_Confirmed_Id}'"
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_WalkinOrder_completed_Paybyothers")
@pytest.mark.parametrize("url", ["https://www.jaldee.com/business/"])
def test_create_walkin_Order_paybyothers(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search customers']", "9400553615")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 4']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[3]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        time.sleep(2)
        confirmorder.click()
        time.sleep(5)
        confirm_order_id = login.find_element(By.XPATH, "//span[@class='order-id ng-star-inserted']")
        confirmed_order = confirm_order_id.text
        Order_Confirmed_Id = '#' + confirmed_order.split('#')[-1] 
        print("Confirmed_order_Id :", Order_Confirmed_Id )
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )
        actual_message = confirmorder.text
        expected_message = "Confirmed"
        print(f"Expected status: '{expected_message}', Actual status: '{confirmorder.text}'")
        assert actual_message == expected_message, f"Expected message '{expected_message} but got Message '{actual_message}'"
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
        expected_message = "Order Completed Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{toast_message.text}'")
        assert toast_message.text == expected_message, f"Expected toast message '{expected_message}', but got '{toast_message.text}'"
        time.sleep(5)
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
        paymentlink = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        scroll_to_element(login, paymentlink)
        paymentlink.click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Pay by Others']")
        time.sleep(5)
        pay = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Pay']"))
        ) 
        scroll_to_element(login, pay)
        time.sleep(2)
        pay.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "Payment completed successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Orders'])[1]") 
        time.sleep(3)
        Order_first_row = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]/td[2]"))
        ).text
        View_Orders_first_value = '#' + Order_first_row.split('#')[-1]  
        print(f"View_Order_first_value : {View_Orders_first_value}")
        time.sleep(3)
        print(f"Expected View Order ID: '{View_Orders_first_value}', Actual Confirmed Order ID: '{Order_Confirmed_Id}'")
        assert Order_Confirmed_Id == View_Orders_first_value, f"Expected View Order ID '{View_Orders_first_value} but got Confirmed Order ID '{Order_Confirmed_Id}'"
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  