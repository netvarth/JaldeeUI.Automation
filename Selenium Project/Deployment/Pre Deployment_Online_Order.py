from Framework.consumer_common_utils import *
from Framework.common_dates_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Online_Order")
def test_create_Online_order(consumer_login):
    try:
        time.sleep(5)
        consumer_data = create_consumer_data()
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
        time.sleep(2)
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@aria-label='Select']"))
        ).click()
        time.sleep(2)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//li[@aria-label='{salutation}']"
        salutation_option_element = WebDriverWait(consumer_login, 15).until(
            EC.element_to_be_clickable((By.XPATH, salutation_option_xpath))
        )
        salutation_option_element.click()
        time.sleep(2)
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
        ####################### SearchItems ####################################
        itemsearch =WebDriverWait(consumer_login,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='what are you looking for?']"))
        )
        itemsearch.send_keys('G')
        time.sleep(3)
        itemname = WebDriverWait(consumer_login,10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='fw-bold ng-star-inserted'][normalize-space()='Gulab jamun'])[1]"))
        )
        Search_Itemname = itemname.text
        print("Looking For Item :", Search_Itemname)
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Sweets']")
        )
        ).click()
        time.sleep(3)
        ViewItemname = consumer_login.find_element(By.XPATH, "//h2[normalize-space()='Gulab jamun']")
        Viewable_Itemname = ViewItemname.text
        print("Viewable Item :", Viewable_Itemname)
        print(f"Expected Item_name : '{Viewable_Itemname}', Actual Item_name : '{Search_Itemname}'")
        assert Search_Itemname == Viewable_Itemname, f"Expected Item Name '{Viewable_Itemname} but got Item Name '{Search_Itemname}'"
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//i[@class='fa fa-arrow-left clrChangeHeader pointer-cursor']")
        time.sleep(2)
        ############################## View All ###############################################
        viewall = consumer_login.find_element(By.XPATH, "//button[normalize-space()='View All']")
        scroll_to_element(consumer_login, viewall)
        time.sleep(3)
        AllItems = consumer_login.find_elements(By.XPATH, "//div[@class='items-grid-card pointer-cursor']")
        AllItemscount = len(AllItems)
        print(f"Count of All Items  with class 'items-grid-card pointer-cursor': {AllItemscount}")
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//button[normalize-space()='View All']")
        time.sleep(3)
        Itemscount = consumer_login.find_elements(By.XPATH, "//div[@class='items-card pointer-cursor']")
        ViewItemscount = len(Itemscount)
        print(f"Count of All Items  with class 'items-card pointer-cursor': {ViewItemscount}")
        time.sleep(3)
        print(f"Expected Item_name_count : '{ViewItemscount}', Actual Item_name_count : '{AllItemscount}'")
        assert AllItemscount == ViewItemscount, f"Expected Item Name '{ViewItemscount} but got Item Name '{AllItemscount}'"
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//i[@class='fa fa-arrow-left clrChangeHeader pointer-cursor']")
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            consumer_login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  