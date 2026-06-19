from Framework.common_utils import *
from Framework.consumer_common_utils import *
from selenium.webdriver.common.keys import Keys

driver = login

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Add Item from Wishlist to Cart after adding it to Wishlist.")
@pytest.mark.parametrize("url", [sales_order_consumer_scale_url])
def test_create_online_order_1(consumer_login):
   
   
    try:
        time.sleep(3)
        wait = WebDriverWait(consumer_login, 30)
        driver = consumer_login
        time.sleep(2)


        item_element = driver.find_element(By.XPATH, "//h2[normalize-space()='Categories']")
        scroll_to_element(driver, item_element)
        time.sleep(2)
        
        wait_and_locate_click(
            driver, By.XPATH, "//div[contains(text(),'Item_1')]"
        )

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "(//h3[normalize-space()='Item_1'])[1]"
        )

        # Click Add to Cart without login
        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnAddToCart'])[1]"
        )

        time.sleep(2)
        wait_and_send_keys(
            driver, By.XPATH, "(//input[@placeholder='81234 56789'])[1]", "8281276241"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//input[@type='checkbox'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnSendOTP']"
        )

        time.sleep(2)

        otp_digits = "5555"
        # otp_digits = "55555"
        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )

        # print("Number of OTP input fields:", len(otp_inputs))
        # print(otp_inputs)

        for i, otp_input in enumerate(otp_inputs):

            # print(i)
            # print(otp_input)
            otp_input.send_keys(otp_digits[i])

        consumer_login.find_element(By.XPATH, "//button[@id='btnVerifyOTP']").click()

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        
        time.sleep(3)
        element_item = driver.find_element(By.XPATH, "//div[normalize-space()='Item_4']")
        scroll_to_element(driver, element_item)
        time.sleep(2)
        element_item.click()

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[normalize-space()='Add to Wishlist']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "(//i[@class='fa fa-heart-o wishlist-icon'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//h3[normalize-space()='Item_4']"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnAddToCart']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//img[@class='ms-1'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCheckout']"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnPrimaryAction']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//div[contains(text(),'Net Banking')])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnPrimaryAction']"
        )

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnPrimaryAction']"
        )

        time.sleep(3)
        # Store main window
        main_window = driver.current_window_handle

        # Wait for Razorpay iframe and switch
        wait.until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe.razorpay-checkout-frame")
            )
        )

        print("Switched to Razorpay iframe")

        # Click Netbanking option
        netbanking = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@data-testid='netbanking']")
            )
        )
        netbanking.click()

        print("Netbanking selected")

        # Select bank (Example: State Bank of India)
        bank = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'Kotak Mahindra Bank')]")
            )
        )
        bank.click()

        print("Bank selected")

        # Exit iframe
        driver.switch_to.default_content()

        time.sleep(2)
       # Store main window
        main_window = driver.current_window_handle

        print("Main window:", main_window)

        # Wait for Razorpay simulator window
        wait.until(lambda d: len(d.window_handles) > 1)

        # Switch to Razorpay window
        for window in driver.window_handles:
            driver.switch_to.window(window)
            if "mocksharp/payment" in driver.current_url:
                print("Switched to Razorpay simulator:", driver.current_url)
                break

        # Wait for Success button
        success_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-val='S']"))
        )

        # Click success
        driver.execute_script("arguments[0].click();", success_btn)

        print("Success button clicked")

        # Switch back to main window
        driver.switch_to.window(main_window)

        print("Returned to main window")


        driver.implicitly_wait(30)
        element_invoice = driver.find_element(By.XPATH, "//button[@id='btnInvoice']")
        scroll_to_element(driver, element_invoice)
        time.sleep(1)
        element_invoice.click()


        time.sleep(3)
    except Exception as e:
        allure.attach(
            consumer_login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Add Item from to Cart edit qty")
@pytest.mark.parametrize("url", [sales_order_consumer_scale_url])
def test_create_online_order_2(consumer_login):
   
   
    try:
        time.sleep(3)
        wait = WebDriverWait(consumer_login, 30)
        driver = consumer_login
        time.sleep(2)


        item_element = driver.find_element(By.XPATH, "//h2[normalize-space()='Categories']")
        scroll_to_element(driver, item_element)
        time.sleep(2)
        
        wait_and_locate_click(
            driver, By.XPATH, "//div[contains(text(),'Item_1')]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//h3[normalize-space()='Item_4']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnAddToCart']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)

        # --------------------------------------------------
        # Add Item_6 from Products next page
        # --------------------------------------------------

        item_to_add = "Item_6"

        # Click Products
        wait_and_locate_click(
            driver,
            By.XPATH,
            "//span[normalize-space()='Products']"
        )

        print("Clicked Products")
        time.sleep(2)


        while True:

            # Check whether Item_6 is visible on current page
            item_6_elements = driver.find_elements(
                By.XPATH,
                "//h3[normalize-space()='Item_6']"
            )

            if item_6_elements:
                item_6 = item_6_elements[0]
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", item_6)
                time.sleep(1)

                wait_and_locate_click(
                    driver,
                    By.XPATH,
                    "//h3[normalize-space()='Item_6']"
                )

                print("Clicked Item_6")
                time.sleep(2)
                break

            # Scroll down to see Next button
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

            # Check Next button
            next_buttons = driver.find_elements(
                By.XPATH,
                "//button[contains(normalize-space(),'Next')]"
            )

            if not next_buttons:
                raise Exception("Next button not found on Products page")

            next_button = next_buttons[-1]

            if next_button.get_attribute("disabled") is not None:
                raise Exception("Item_6 not found and Next button is disabled")

            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", next_button)
            time.sleep(1)

            wait_and_locate_click(
                driver,
                By.XPATH,
                "(//button[contains(normalize-space(),'Next')])[last()]"
            )

            print("Clicked Next page")
            time.sleep(2)


        # --------------------------------------------------
        # Item_6 details page opened - click Add to Cart
        # --------------------------------------------------

        wait_and_locate_click(
            driver,
            By.XPATH,
            "//button[@id='btnAddToCart']"
        )

        print("Clicked Add to Cart for Item_6")
        time.sleep(2)

        msg = get_toast_message(driver)
        print("Toast Message :", msg)


        time.sleep(3)
        item_element_2 = driver.find_element(By.XPATH, "//div[normalize-space()='Item_1']")
        scroll_to_element(driver, item_element_2)
        time.sleep(2)
        item_element_2.click()

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnAddToCart']"
        )

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//img[@alt='Logo']"
        )

        time.sleep(2)
        
        item_element_3 = driver.find_element(By.XPATH, "//div[contains(text(),'Item_1')]")
        scroll_to_element(driver, item_element_3)
        time.sleep(2)
        item_element_3.click()
        time.sleep(2)
    
        item_element_4 = driver.find_element(By.XPATH, "//button[contains(text(),'Next ›')]")
        scroll_to_element(driver, item_element_4)
        time.sleep(2)
        item_element_4.click()

        time.sleep(2)

        
        def click_product_cart_icon(driver, item_name):
            wait = WebDriverWait(driver, 20)

            product = wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        f"//div[contains(@class,'product-card')][.//h3[normalize-space()='{item_name}']]"
                    )
                )
            )

            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", product)
            time.sleep(1)

            actions = ActionChains(driver)
            actions.move_to_element(product).perform()
            time.sleep(1)

            cart_icon = product.find_element(
                By.XPATH,
                ".//img[@alt='Change address']"
            )

            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", cart_icon)
            time.sleep(1)

            # Use JS click because normal click is intercepted by product-actions overlay
            driver.execute_script("arguments[0].click();", cart_icon)

            print(f"Clicked cart icon for {item_name}")
            time.sleep(2)

        click_product_cart_icon(driver, "Item_8")
        click_product_cart_icon(driver, "Item_5")


        time.sleep(5)

        wait_and_locate_click(
            driver, By.XPATH, "(//img[@class='ms-1'])[1]"
        )

        time.sleep(2)
        cart_image = driver.find_element(By.XPATH, "(//img[@class='ms-1'])[1]")
        driver.execute_script("arguments[0].click();", cart_image)


        time.sleep(2)
        items_xpath = "//div[contains(@class,'cart-item-card')]"

        items_count = len(driver.find_elements(By.XPATH, items_xpath))

        for i in range(items_count):
            for _ in range(2):
                items = driver.find_elements(By.XPATH, items_xpath)
                item = items[i]

                plus_btn = item.find_element(By.XPATH, ".//button[normalize-space()='+']")

                # 🔹 Scroll into view (center is IMPORTANT)
                driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", plus_btn
                )

                time.sleep(0.5)

                # 🔹 Wait until clickable
                wait.until(EC.element_to_be_clickable(plus_btn))

                try:
                    plus_btn.click()
                except:
                    # 🔹 Fallback if intercepted
                    driver.execute_script("arguments[0].click();", plus_btn)

                time.sleep(0.5)


        time.sleep(2)
        element_placeorder = driver.find_element(By.XPATH, "//label[normalize-space()='NOTES']")
        scroll_to_element(driver, element_placeorder)
        time.sleep(2)
        
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCheckout']"
        )

        time.sleep(2)
        wait_and_send_keys(
            driver, By.XPATH, "(//input[@placeholder='81234 56789'])[1]", "8281276241"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//input[@type='checkbox'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnSendOTP']"
        )

        time.sleep(2)

        otp_digits = "5555"
        # otp_digits = "55555"
        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )


        for i, otp_input in enumerate(otp_inputs):

            # print(i)
            # print(otp_input)
            otp_input.send_keys(otp_digits[i])

        consumer_login.find_element(By.XPATH, "//button[@id='btnVerifyOTP']").click()

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        

    except Exception as e:
        allure.attach(
            consumer_login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create online order by click on Buy it Now button the item")
@pytest.mark.parametrize("url", [sales_order_consumer_scale_url])
def test_create_sales_order_3(consumer_login):
   
   
    try:
        time.sleep(3)
        wait = WebDriverWait(consumer_login, 30)
        driver = consumer_login
        time.sleep(2)


        item_element = driver.find_element(By.XPATH, "//h2[normalize-space()='Categories']")
        scroll_to_element(driver, item_element)
        time.sleep(2)
        
        wait_and_locate_click(
            driver, By.XPATH, "//div[contains(text(),'Item_1')]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//h3[normalize-space()='Item_1'])[1]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[normalize-space()='+']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnAddToCart'])[1]"
        )


        time.sleep(2)
        wait_and_send_keys(
            driver, By.XPATH, "(//input[@placeholder='81234 56789'])[1]", "8281276241"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//input[@type='checkbox'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnSendOTP']"
        )

        time.sleep(2)

        otp_digits = "5555"
        # otp_digits = "55555"
        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )


        for i, otp_input in enumerate(otp_inputs):

            # print(i)
            # print(otp_input)
            otp_input.send_keys(otp_digits[i])

        consumer_login.find_element(By.XPATH, "//button[@id='btnVerifyOTP']").click()

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        
        time.sleep(3)
    
        wait_and_locate_click(
            driver, By.XPATH, "(//img[@class='ms-1'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCheckout']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnPrimaryAction']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//div[contains(text(),'Net Banking')])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnPrimaryAction']"
        )


        time.sleep(3)
        # Store main window
        main_window = driver.current_window_handle

        # Wait for Razorpay iframe and switch
        wait.until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe.razorpay-checkout-frame")
            )
        )

        print("Switched to Razorpay iframe")

        # Click Netbanking option
        netbanking = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@data-testid='netbanking']")
            )
        )
        netbanking.click()

        print("Netbanking selected")

        # Select bank (Example: State Bank of India)
        bank = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'Kotak Mahindra Bank')]")
            )
        )
        bank.click()

        print("Bank selected")

        # Exit iframe
        driver.switch_to.default_content()

        time.sleep(2)
       # Store main window
        main_window = driver.current_window_handle

        print("Main window:", main_window)

        # Wait for Razorpay simulator window
        wait.until(lambda d: len(d.window_handles) > 1)

        # Switch to Razorpay window
        for window in driver.window_handles:
            driver.switch_to.window(window)
            if "mocksharp/payment" in driver.current_url:
                print("Switched to Razorpay simulator:", driver.current_url)
                break

        # Wait for Success button
        success_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-val='S']"))
        )

        # Click success
        driver.execute_script("arguments[0].click();", success_btn)

        print("Success button clicked")

        # Switch back to main window
        driver.switch_to.window(main_window)

        print("Returned to main window")


        driver.implicitly_wait(30)
        element_invoice = driver.find_element(By.XPATH, "//button[@id='btnInvoice']")
        scroll_to_element(driver, element_invoice)
        time.sleep(1)
        element_invoice.click()


        time.sleep(3)
    except Exception as e:
        allure.attach(
            consumer_login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    


