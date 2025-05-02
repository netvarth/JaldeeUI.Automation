
from Framework.common_utils import *
from Framework.common_dates_utils import *
from Framework.consumer_common_utils import *




@allure.severity(allure.severity_level.CRITICAL)
@allure.title("sales order")
@pytest.mark.parametrize("url", [sales_order_consumer_scale_url])
def test_sales_order_1(consumer_login):

    try:

        wait= WebDriverWait(consumer_login, 30)

        Scroll = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//h2[normalize-space(.)='Cakes'])[1]"))
        )

        consumer_login.execute_script("arguments[0].scrollIntoView();", Scroll)

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space(.)='Chocolate Cake'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Buy it now'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='81234 56789'])[1]"))
        ).send_keys("9207206005")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='continue ng-star-inserted'])[1]"))
        ).click()

        time.sleep(3)
        otp_digits = "5555"
        wait = WebDriverWait(consumer_login, 10)
        # Wait for the OTP input fields to be present
        otp_inputs = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )

        for i, otp_input in enumerate(otp_inputs):
            otp_input.send_keys(otp_digits[i])

        consumer_login.find_element(By.XPATH, "(//span[@class='continue ng-star-inserted'])[1]").click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space(.)='Proceed to payment'])[1]"))
        ).click()

        time.sleep(5)
        confirm_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH , "(//button[normalize-space(.)='Confirm'])[1]"))
        )
        consumer_login.execute_script("arguments[0].scrollIntoView();", confirm_button)
        time.sleep(2)
        confirm_button.click()



        time.sleep(2)
        Net_Banking_Opt = WebDriverWait(consumer_login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(text(),'NET BANKING')]")
                )
        )
        consumer_login.execute_script("arguments[0].click();", Net_Banking_Opt)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnPay']"))
        ).click()

        # Switch to the iframe containing the Razorpay modal
        razorpay_iframe = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "razorpay-checkout-frame"))
        )
        consumer_login.switch_to.frame(razorpay_iframe)
        print("Switched to Razorpay iframe")

        bank_opt = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='mr-auto flex flex-col truncate text-on-surface']//span[text()='Netbanking']"))
        ).click()


        # Select bank option (e.g., State Bank of India)
        select_bank = WebDriverWait(consumer_login, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(@class, 'font-medium text-on-surface') and text()='State Bank of India']")
            )
        )
        consumer_login.execute_script("arguments[0].click();", select_bank)
        print("Selected bank option")


        main_window_handle = consumer_login.current_window_handle
        WebDriverWait(consumer_login, 10).until(EC.new_window_is_opened)
        all_window_handles = consumer_login.window_handles

        new_window_handle = None
        for handle in all_window_handles:
            if handle != main_window_handle:
                new_window_handle = handle
                break

        if new_window_handle:
            consumer_login.switch_to.window(new_window_handle)

            time.sleep(3)
            WebDriverWait(consumer_login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@data-val='S' and contains(@class, 'success')]"))
            ).click()

            consumer_login.switch_to.window(main_window_handle)
        
        print("success")

        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            consumer_login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("After consumer confirmed the order and payment done, send the invoice to the consumer")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_sales_order_2(login):

    try:

        wait = WebDriverWait(login, 30)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='my-1 font-small ng-star-inserted'][normalize-space(.)='Orders'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        time.sleep(3)
        complete_order = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Complete Order'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", complete_order)
        complete_order.click()

        time.sleep(2)
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space(.)='View Invoice'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space(.)='Share Invoice'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='mdc-button__label'])[1]"))
        ).click()

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

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[2]"))
        ).click()  

        time.sleep(2) 
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Orders'])[1]"))
        ).click()


        expected_status = "Completed"

        # Locate the first row's status cell
        status_element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//tr[contains(@class,'ng-star-inserted')]/td[4]/span)[1]"))
        )
        actual_status = status_element.text.strip()

        # Print the status
        print(f"Order Status: {actual_status}")

        # Assert with message
        assert actual_status.lower() == expected_status.lower(), (
            f"Status mismatch: Expected = '{expected_status}', Actual = '{actual_status}'"
        )


        time.sleep(5)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Provider takes the walkin order and send the invoice to the consumer")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_sales_order_3(login): 

    try:

        wait = WebDriverWait(login, 30)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Create Order')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Search customers'])[1]"))
        ).send_keys("9207206005")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Id : 1'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space(.)='Next'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Search items'])[1]"))
        ).send_keys("Cake")

        time.sleep(2)
        option_1 = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Chocolate cake')])[1]"))
        )
        login.execute_script("arguments[0].click();", option_1)    

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space(.)='2 kg'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space(text())='Select Item'])[2]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space(.)='Confirm Order'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Create Invoice'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space(.)='View Invoice'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-dropdown-trigger-icon p-icon'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Share Invoice'])[1]"))
        ).click()   

        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Consumer confirm the order with zero payment")
@pytest.mark.parametrize("url", [sales_order_consumer_scale_url])
def test_sales_order_4(consumer_login):
    try:

        wait = WebDriverWait(consumer_login, 30)
        Scroll = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//h2[normalize-space(.)='Cakes'])[1]"))
        )

        consumer_login.execute_script("arguments[0].scrollIntoView();", Scroll)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space(.)='Samosa'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Buy it now'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='81234 56789'])[1]"))
        ).send_keys("9207206005")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='continue ng-star-inserted'])[1]"))
        ).click()

        time.sleep(3)
        otp_digits = "5555"
        wait = WebDriverWait(consumer_login, 10)
        # Wait for the OTP input fields to be present
        otp_inputs = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )

        for i, otp_input in enumerate(otp_inputs):
            otp_input.send_keys(otp_digits[i])

        consumer_login.find_element(By.XPATH, "(//span[@class='continue ng-star-inserted'])[1]").click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space(.)='Proceed to payment'])[1]"))
        ).click()

        time.sleep(5)
        confirm_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH , "(//button[normalize-space(.)='Confirm'])[1]"))
        )
        consumer_login.execute_script("arguments[0].scrollIntoView();", confirm_button)
        time.sleep(2)
        confirm_button.click()
        time.sleep(4)

        # Wait for the "ORDER CONFIRMED" status to appear
        order_status = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(@class, 'status-confirmed') and normalize-space(text())='ORDER CONFIRMED']")
            )
        )

        # Print the status text
        print("Order status found:", order_status.text.strip())

        # Assert that the status is as expected
        assert order_status.text.strip() == "ORDER CONFIRMED", f"Expected 'ORDER CONFIRMED', but got '{order_status.text.strip()}'"

        time.sleep(5)



    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            consumer_login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("After consumer confirmed the order and payment done, send the invoice to the consumer")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_sales_order_5(login):
    try:

        wait = WebDriverWait(login, 30)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='my-1 font-small ng-star-inserted'][normalize-space(.)='Orders'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space(.)='Cancel Order'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space(.)='Yes'])[1]"))
        ).click()


        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(5)
        
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            consumer_login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e