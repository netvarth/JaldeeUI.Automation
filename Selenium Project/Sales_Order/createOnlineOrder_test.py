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
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Dessert')]"))
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", Dessert)
        time.sleep(2)    
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

        time.sleep(10)


        main_window_handle = consumer_login.current_window_handle

        # Wait for the new window (popup) to appear
        WebDriverWait(consumer_login, 10).until(EC.new_window_is_opened)

        # Get all window handles and find the new window handle
        all_window_handles = consumer_login.window_handles
        new_window_handle = next(
            handle for handle in all_window_handles if handle != main_window_handle
        )

        # Switch to the new window
        consumer_login.switch_to.window(new_window_handle)

        # Interact with elements in the Razorpay popup window
        try:
            # Select the bank (e.g., HDFC Bank)
            select_bank = WebDriverWait(consumer_login, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@data-value='HDFC']"))
            )
            consumer_login.execute_script("arguments[0].click();", select_bank)

            # Click the Pay button or proceed further based on the flow
            pay_button = WebDriverWait(consumer_login, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Success')]"))
            )
            pay_button.click()

        except Exception as e:
            print(f"Error occurred: {e}")

        finally:
            # Optionally, switch back to the main window
            consumer_login.switch_to.window(main_window_handle)






        # Switch to the Razorpay iframe
        # iframe = WebDriverWait(consumer_login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'razorpay')]"))
        # )
        # consumer_login.switch_to.frame(iframe)

        # # Interact with elements inside the iframe
        # time.sleep(2)
        # WebDriverWait(consumer_login, 10).until(
        # EC.presence_of_element_located(
        #     (By.XPATH, "//p[contains(@class,'ptm-paymode-name ptm-lightbold')]")
        # )
        # ).click()
        # time.sleep(2)
        # WebDriverWait(consumer_login, 10).until(
        # EC.visibility_of_element_located((By.XPATH, "(//label[.//div[@data-value='SBIN']])[1]"))
        # ).click()
        # # WebDriverWait(consumer_login, 10).until(
        # # EC.presence_of_element_located(
        # #     (By.XPATH,"//div[contains(@class,'ptm-overlay-wrapper btn-enabled')]//img[contains(@class,'ptm-lock-img')]"))
        # # ).click()
        #  # Handle the popup window
        # main_window_handle = consumer_login.current_window_handle
        # WebDriverWait(consumer_login, 10).until(EC.new_window_is_opened)
        # all_window_handles = consumer_login.window_handles
        # new_window_handle = None
        # for handle in all_window_handles:
        #     if handle != main_window_handle:
        #         new_window_handle = handle
        #         break
        #  # Switch to the new window
        # consumer_login.switch_to.window(new_window_handle)
        # time.sleep(3)

        # WebDriverWait(consumer_login, 10).until(
        # EC.visibility_of_element_located((By.XPATH, "(//label[.//div[@data-value='SBIN']])[1]"))
        # ).click()
        # time.sleep(5)
        # WebDriverWait(consumer_login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Successful']"))
        # ).click()
        # time.sleep(5)
        # # Optionally, switch back to the main window
        # consumer_login.switch_to.window(main_window_handle)
        time.sleep(5)
        ordernumber = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='order-id']"))
        )
        order_id = ordernumber.text
        confirmed_order_id = order_id.split("#")[-1].strip()
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
        wait_and_locate_click(consumer_login, By.XPATH, "//i[@class='fa fa-arrow-left']")
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//button[normalize-space()='Home']")
        time.sleep(2)
        consumer_login.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "//button[@class='mat-mdc-menu-trigger mdc-icon-button mat-mdc-icon-button mat-unthemed mat-mdc-button-base']")
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//span[contains(text(),'Dashboard')]")
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//div[normalize-space()='My Orders']")
        time.sleep(5)
        order_element = consumer_login.find_element(By.XPATH, "(//div[@class = 'orderNumber'])[1]")
        dashboard_order_id = order_element.text
        print("Dashboard Order ID :", dashboard_order_id)
        print(f"Expected Order ID : '{dashboard_order_id}', Actual Order ID : '{confirmed_order_id}'")
        assert confirmed_order_id == dashboard_order_id, f"Expected Order ID '{dashboard_order_id} but got Order ID '{confirmed_order_id}'"
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "//i[@class='fa fa-arrow-left']")
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "//span[normalize-space()='Home']")
        time.sleep(2)
    except Exception as e:
        allure.attach(
            consumer_login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e  
    

from Framework.consumer_common_utils import *
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Online_Order_Itemsearch")
def test_create_Online_order_itemsearch(consumer_login):
    try:
        time.sleep(5)
        consumer_data = create_consumer_data()
        itemsearch =WebDriverWait(consumer_login,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='what are you looking for?']"))
        )
        itemsearch.send_keys('G')
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Sweets']")
        )
        ).click()
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add to cart']")
        )
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
    

from Framework.consumer_common_utils import *
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Online_Order_OurProducts")
def test_create_Online_order_products(consumer_login):
    try:
        time.sleep(5)
        consumer_data = create_consumer_data()
        Dessert2 = WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='d-flex item-grid2 align-items-center justify-content-between'])[2]"))
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", Dessert2)
        time.sleep(5)
        Dessert2.click()
        time.sleep(3)
        WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add to cart']"))
        ).click()
        time.sleep(2)
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
    

from Framework.consumer_common_utils import *
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Online_Order_ViewAll")
def test_create_Online_order_Viewall(consumer_login):
    try:
        time.sleep(5)
        consumer_data = create_consumer_data()
        Viewall = WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View All Products']"))
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", Viewall)
        time.sleep(5)
        Viewall.click()
        time.sleep(3)
        WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[2]"))
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
    
from Framework.consumer_common_utils import *
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Online_Order_login")
def test_create_Online_order_login(consumer_login):
    try:
        time.sleep(5)
        consumer_data = create_consumer_data()
        login = WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='fa fa-user-circle-o ms-1'])[1]"))
        )
        login.click()
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
        Home = WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Home']"))
        )
        Home.click()
        time.sleep(3)
        itemsearch =WebDriverWait(consumer_login,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='what are you looking for?']"))
        )
        itemsearch.send_keys('G')
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Sweets']")
        )
        ).click()
        time.sleep(3)
        # print("Toast Message: Item added to cart")
        WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Buy it now']"))
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
    
from Framework.consumer_common_utils import *
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Online_Order_Existinglogin with quantity increment and decrement")
def test_create_Online_order_existlogin(consumer_login):
    try:
        time.sleep(5)
        consumer_data = create_consumer_data()
        login = WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='fa fa-user-circle-o ms-1'])[1]"))
        )
        login.click()
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        ).send_keys(5550004454)
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
        Home = WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Home']"))
        )
        Home.click()
        time.sleep(3)
        itemsearch =WebDriverWait(consumer_login,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='what are you looking for?']"))
        )
        itemsearch.send_keys('G')
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Sweets']")
        )
        ).click()
        time.sleep(3)
       
        for i in range(3):
            WebDriverWait(consumer_login, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add to cart']"))
            ).click()
        time.sleep(3)
        print("Toast Message: Item added to cart")
        WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='cart-count ng-star-inserted']"))
        ).click()
        time.sleep(3)
        for i in range(3):
            WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='pi pi-plus ng-star-inserted']"))
            ).click()
        time.sleep(3) 
        for i in range(2):
            WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='pi pi-minus ng-star-inserted']"))
            ).click()
        time.sleep(3)
        WebDriverWait(consumer_login, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Checkout']"))
            ).click()
        time.sleep(3)
        WebDriverWait(consumer_login, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Proceed to payment']"))
            ).click()
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
    
from Framework.consumer_common_utils import *
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Online_Order_login_shopnow")
def test_create_Online_order_login_shopnow(consumer_login):
    try:
        time.sleep(5)
        consumer_data = create_consumer_data()
        login = WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='fa fa-user-circle-o ms-1'])[1]"))
        )
        login.click()
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
        Home = WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Home']"))
        )
        Home.click()
        time.sleep(3)
        WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='ms-1 display-large']"))
        ).click()
        time.sleep(3)
        shop_now = WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Shop Now']"))
        )
        time.sleep(2)
        scroll_to_element(consumer_login, shop_now)
        time.sleep(2)
        shop_now.click()
        time.sleep(3)
        itemsearch =WebDriverWait(consumer_login,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='what are you looking for?']"))
        )
        itemsearch.send_keys('G')
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Sweets']")
        )
        ).click()
        time.sleep(3)
        # print("Toast Message: Item added to cart")
        WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Buy it now']"))
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
    
from Framework.consumer_common_utils import *
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Online_Order_login_Delete")
def test_create_Online_order_login_delete(consumer_login):
    try:
        time.sleep(5)
        consumer_data = create_consumer_data()
        login = WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='fa fa-user-circle-o ms-1'])[1]"))
        )
        login.click()
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
        Home = WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Home']"))
        )
        Home.click()
        time.sleep(3)
        itemsearch =WebDriverWait(consumer_login,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='what are you looking for?']"))
        )
        itemsearch.send_keys('G')
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Sweets']")
        )
        ).click()
        time.sleep(3)
        for i in range(3):
            WebDriverWait(consumer_login, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add to cart']"))
            ).click()
        time.sleep(3)
        WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//img[@class='ms-1'])[1]"))
        ).click()
        time.sleep(3)
        WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-trash']"))
        ).click()
        time.sleep(3)
        WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Confirm']"))
        ).click()
        time.sleep(3)
        shop_now = WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Shop Now']"))
        )
        time.sleep(2)
        scroll_to_element(consumer_login, shop_now)
        time.sleep(2)
        shop_now.click()
        time.sleep(3)
        itemsearch =WebDriverWait(consumer_login,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='what are you looking for?']"))
        )
        itemsearch.send_keys('G')
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Sweets']")
        )
        ).click()
        time.sleep(3)
        # print("Toast Message: Item added to cart")
        WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Buy it now']"))
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
        print(message)
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
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Online_Order with Applying Coupon")
def test_create_Online_order_Coupon(consumer_login):
    try:
        time.sleep(5)
        consumer_data = create_consumer_data()
        # consumer_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        Dessert = WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Dessert')]"))
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", Dessert)
        time.sleep(2)    
        Dessert.click()
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//button[normalize-space()='Add']")
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        ).send_keys(consumer_data['phonenumber'])
        print("New ConsuDessertmer Phone Number:", consumer_data['phonenumber'])
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
        wait_and_locate_click(consumer_login, By.XPATH, "//div[@class='coupons-icon pointer-cursor']")
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "//i[@class='fa fa-clone']")
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "//i[@class='fa fa-window-close']")
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "//input[@type='checkbox']")
        time.sleep(2)
        coupon_input = consumer_login.find_element(By.XPATH, "//input[@placeholder='Enter coupon code']")
        coupon_input.click()
        time.sleep(2)
        coupon_input.send_keys(Keys.CONTROL, 'v')
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "//button[normalize-space()='Add']")
        message = get_snack_bar_message(consumer_login)
        print("Snack bar message:", message)
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
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Pay']"))
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
        wait_and_locate_click(consumer_login, By.XPATH, "//i[@class='fa fa-arrow-left']")
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//button[normalize-space()='Home']")
        time.sleep(2)
        consumer_login.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "//button[@class='mat-mdc-menu-trigger mdc-icon-button mat-mdc-icon-button mat-unthemed mat-mdc-button-base']")
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//span[contains(text(),'Dashboard')]")
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//div[normalize-space()='My Orders']")
        time.sleep(5)
        order_element = consumer_login.find_element(By.XPATH, "(//div[@class = 'orderNumber'])[1]")
        dashboard_order_id = order_element.text
        print("Dashboard Order ID :", dashboard_order_id)
        print(f"Expected Order ID : '{dashboard_order_id}', Actual Order ID : '{confirmed_order_id}'")
        assert confirmed_order_id == dashboard_order_id, f"Expected Order ID '{dashboard_order_id} but got Order ID '{confirmed_order_id}'"
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "//i[@class='fa fa-arrow-left']")
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "//span[normalize-space()='Home']")
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            consumer_login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    
