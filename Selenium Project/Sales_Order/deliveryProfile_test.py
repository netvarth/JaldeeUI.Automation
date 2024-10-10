from Framework.common_utils import *
from Framework.common_dates_utils import *
import re


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Home_Delivery_Profile")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_home_deliveryProfile(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Delivery Profile')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Delivery Profile']")
        time.sleep(2)
        Delivery_profile = "Delivery_profile_" + str(uuid.uuid4())[:8]
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Delivery Profile 1']", Delivery_profile)
        time.sleep(2)
        min_price = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@type='number'])[1]"))
        )
        min_price.clear()
        min_price.send_keys("50")
        time.sleep(3)
        max_price = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@type='number'])[2]"))
        )
        max_price.clear()
        max_price.send_keys("5000")
        time.sleep(3)
        wait_and_send_keys(login, By.XPATH, "(//input[@type='number'])[3]", 50)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Create']") 
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='name']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Sweets']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='displayname']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Home Delivery']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']") 
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Store_Pickup_Profile")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_Store_Pickup_deliveryProfile(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Delivery Profile')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Delivery Profile']")
        time.sleep(2)
        Delivery_profile = "Delivery_profile_" + str(uuid.uuid4())[:8]
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Delivery Profile 1']", Delivery_profile)
        time.sleep(2)
        min_price = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@type='number'])[1]"))
        )
        min_price.clear()
        min_price.send_keys("50")
        time.sleep(3)
        max_price = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@type='number'])[2]"))
        )
        max_price.clear()
        max_price.send_keys("5000")
        time.sleep(3)
        wait_and_send_keys(login, By.XPATH, "(//input[@type='number'])[3]", 50)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Create']") 
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='name']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Sweets']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='displayname']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Store Pickup']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']") 
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_WalkinOrder_completed")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_walkin_Order(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search customers']", "5550004454")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 1']")
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
        time.sleep(5)
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
        time.sleep(5)
        delivery_charge_element = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='d-flex space-between mb-1 align-items-center ng-star-inserted'])[4]"))
        )
        scroll_to_element(login, delivery_charge_element)
        time.sleep(2)
        # Retrieve the text
        delivery_charge_text = delivery_charge_element.text.strip()  # This removes leading/trailing whitespace
        print(f"Delivery Charge Text: '{delivery_charge_text}'")  # Debugging line

        # Use regex to extract the numeric value
        match = re.search(r'\d+\.\d{2}', delivery_charge_text)
        if match:
            delivery_charge = match.group(0)  # This will give you '50.00'
            print(f"Extracted Delivery Charge: {delivery_charge}")
        else:
            print("Delivery charge not found.")
        expected_delivery_charge = "50.00"  
        print(f"Expected delivery_charge: '{expected_delivery_charge}', Actual delivery_charge: '{delivery_charge}'")
        assert delivery_charge == expected_delivery_charge, f"Expected delivery charge '{expected_delivery_charge}' but got '{delivery_charge}'"
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
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("View_Delivery_Profile")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_View_deliveryProfile(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Delivery Profile')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@type='submit'][normalize-space()='View'])[2]")
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='View Store']")
        time.sleep(5)
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
def test_create_Online_order(consumer_login):
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
        WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
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
        WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='cart-count ng-star-inserted']"))
        ).click()
        time.sleep(3)
        WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Checkout']"))
        ).click()
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
        delivery_charge_element = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '(+)₹50.00')]"))
        )

        # Retrieve the text
        delivery_charge_text = delivery_charge_element.text.strip()  # Remove leading/trailing whitespace
        print(f"Delivery Charge Text: '{delivery_charge_text}'")  # Debugging line

        # Use regex to extract the numeric value
        match = re.search(r'[\d,]+(?:\.\d{2})?', delivery_charge_text)
        if match:
            delivery_charge = match.group(0)  # This will give you '50.00'
            print(f"Extracted Delivery Charge: {delivery_charge}")
            return delivery_charge
        else:
            print("Delivery charge not found.")
        expected_delivery_charge = "50.00"  
        print(f"Expected delivery_charge: '{expected_delivery_charge}', Actual delivery_charge: '{delivery_charge}'")
        assert delivery_charge == expected_delivery_charge, f"Expected delivery charge '{expected_delivery_charge}' but got '{delivery_charge}'"
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
        time.sleep(3)
        # Optionally, switch back to the main window
        consumer_login.switch_to.window(main_window_handle)
        time.sleep(5)
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
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-arrow-left']"))
        ).click()
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Home']"))
        ).click()
        time.sleep(3)
    except Exception as e:
        allure.attach(  
            consumer_login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  