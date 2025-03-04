
from Framework.common_utils import *
from Framework.common_dates_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_SaveasDraft_Withoutconsumer")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_SaveasDraft(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//img[contains(@src, 'settings.gif')]//following::div[contains(text(),'Settings')]")
        time.sleep(2)
        POS = wait_and_locate_click(login, By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(login, POS)       
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p[normalize-space()='Sales Order Management System']")
        time.sleep(2)
        Sales_order = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']")) 
            )
        aria_checked = Sales_order.get_attribute("aria-checked")
        if aria_checked == "true":
            print("Sales Orders Management is already active, no need to click.")
        else:
            Sales_order.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
        time.sleep(3)
        draftorder = wait_and_locate_click(login, By.XPATH, "//span[@class='lnk setings ml-auto text-capitalize']")
        scroll_to_element(login, draftorder)
        time.sleep(2)
        draftorder_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@id='mat-mdc-slide-toggle-2-button'])[1]")))
        aria_checked = draftorder_button.get_attribute("aria-checked")
        if aria_checked == "true":
            draftorder_button.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
        else:
            print("Draft Order is already active, no need to click.")
        time.sleep(2)
        wait_and_click(login, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor text-capitalize']", 20)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[2]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        saveasdraft = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Save as draft']"))
        )
        scroll_to_element(login, saveasdraft)
        time.sleep(2)
        saveasdraft.click()
        time.sleep(5)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        time.sleep(2)
        confirmorder.click()
        time.sleep(2)
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
        paymentlink = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        scroll_to_element(login, paymentlink)
        paymentlink.click()
        time.sleep(3)
        pay_by_cash = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Pay by Cash']"))
        )
        pay_by_cash.click()
        time.sleep(5)
        paymentnote = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname = 'paymentNote']"))
        )
        paymentnote.click()
        time.sleep(2)
        paymentnote.send_keys("Fully Paid")
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Pay']"))
        ).click()
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
        ).click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(2)
        expected_message = "Payment completed successfully"
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
@allure.title("Create_SaveasDraft_Withconsumer_Via_Lucenesearch")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_edit_SaveasDraft_search(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//img[contains(@src, 'settings.gif')]//following::div[contains(text(),'Settings')]")
        time.sleep(2)
        POS = wait_and_locate_click(login, By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(login, POS)       
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p[normalize-space()='Sales Order Management System']")
        time.sleep(2)
        Sales_order = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']")) 
            )
        aria_checked = Sales_order.get_attribute("aria-checked")
        if aria_checked == "true":
            print("Sales Orders Management is already active, no need to click.")
        else:
            Sales_order.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
        time.sleep(3)
        draftorder = wait_and_locate_click(login, By.XPATH, "//span[@class='lnk setings ml-auto text-capitalize']")
        scroll_to_element(login, draftorder)
        time.sleep(2)
        draftorder_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@id='mat-mdc-slide-toggle-2-button'])[1]")))
        aria_checked = draftorder_button.get_attribute("aria-checked")
        if aria_checked == "true":
            draftorder_button.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
        else:
            print("Draft Order is already active, no need to click.")
        time.sleep(2)
        wait_and_click(login, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor text-capitalize']", 20)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[2]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        saveasdraft = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Save as draft']"))
        )
        scroll_to_element(login, saveasdraft)
        time.sleep(2)
        saveasdraft.click()
        time.sleep(3)
        editorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Edit Order']"))
        )
        editorder.click()
        time.sleep(3)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search customers']", "5550004454")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 1']")
        time.sleep(2)
        updateorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Update Order']"))
        )
        scroll_to_element(login, updateorder)
        time.sleep(2)
        updateorder.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(3)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        time.sleep(2)
        confirmorder.click()
        time.sleep(2)
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
        paymentlink = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        scroll_to_element(login, paymentlink)
        paymentlink.click()
        time.sleep(3)
        pay_by_cash = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Pay by Cash']"))
        )
        pay_by_cash.click()
        time.sleep(5)
        paymentnote = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname = 'paymentNote']"))
        )
        paymentnote.click()
        time.sleep(2)
        paymentnote.send_keys("Fully Paid")
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Pay']"))
        ).click()
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
        ).click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(2)
        expected_message = "Payment completed successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(2)
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
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_SaveasDraft_With_Newconsumer")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_edit_SaveasDraft_Newconsumer(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//img[contains(@src, 'settings.gif')]//following::div[contains(text(),'Settings')]")
        time.sleep(2)
        POS = wait_and_locate_click(login, By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(login, POS)       
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p[normalize-space()='Sales Order Management System']")
        time.sleep(2)
        Sales_order = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']")) 
            )
        aria_checked = Sales_order.get_attribute("aria-checked")
        if aria_checked == "true":
            print("Sales Orders Management is already active, no need to click.")
        else:
            Sales_order.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
        time.sleep(3)
        draftorder = wait_and_locate_click(login, By.XPATH, "//span[@class='lnk setings ml-auto text-capitalize']")
        scroll_to_element(login, draftorder)
        time.sleep(2)
        draftorder_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@id='mat-mdc-slide-toggle-2-button'])[1]")))
        aria_checked = draftorder_button.get_attribute("aria-checked")
        if aria_checked == "true":
            draftorder_button.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
        else:
            print("Draft Order is already active, no need to click.")
        time.sleep(2)
        wait_and_click(login, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor text-capitalize']", 20)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[2]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        saveasdraft = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Save as draft']"))
        )
        scroll_to_element(login, saveasdraft)
        time.sleep(2)
        saveasdraft.click()
        time.sleep(3)
        editorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Edit Order']"))
        )
        editorder.click()
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-icon pi pi-plus']")
        time.sleep(2)
        WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//mat-select[@placeholder='Select']")
        )
        ).click()
        time.sleep(3)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        salutation_option_element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, salutation_option_xpath))
        )
        salutation_option_element.click()
        time.sleep(3)
        first_name, last_name, phonenumber, email = create_users_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(
            By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
        ).send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[normalize-space()='Save']").click()
        time.sleep(3)
        updateorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Update Order']"))
        )
        scroll_to_element(login, updateorder)
        time.sleep(2)
        updateorder.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(3)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        time.sleep(2)
        confirmorder.click()
        time.sleep(2)
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
        paymentlink = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        scroll_to_element(login, paymentlink)
        paymentlink.click()
        time.sleep(3)
        pay_by_cash = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Pay by Cash']"))
        )
        pay_by_cash.click()
        time.sleep(5)
        paymentnote = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname = 'paymentNote']"))
        )
        paymentnote.click()
        time.sleep(2)
        paymentnote.send_keys("Fully Paid")
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Pay']"))
        ).click()
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
        ).click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(2)
        expected_message = "Payment completed successfully"
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
@allure.title("Create_Draft_Withoutconsumer")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_Draft(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//img[contains(@src, 'settings.gif')]//following::div[contains(text(),'Settings')]")
        time.sleep(2)
        POS = wait_and_locate_click(login, By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(login, POS)       
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p[normalize-space()='Sales Order Management System']")
        time.sleep(2)
        Sales_order = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']")) 
            )
        aria_checked = Sales_order.get_attribute("aria-checked")
        if aria_checked == "true":
            print("Sales Orders Management is already active, no need to click.")
        else:
            Sales_order.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
        time.sleep(3)
        draftorder = wait_and_locate_click(login, By.XPATH, "//span[@class='lnk setings ml-auto text-capitalize']")
        scroll_to_element(login, draftorder)
        time.sleep(2)
        draftorder_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@id='mat-mdc-slide-toggle-2-button'])[1]")))
        aria_checked = draftorder_button.get_attribute("aria-checked")
        if aria_checked == "true":
            draftorder_button.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
        else:
            print("Draft Order is already active, no need to click.")
        time.sleep(2)
        wait_and_click(login, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor text-capitalize']", 20)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
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
        paymentlink = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        scroll_to_element(login, paymentlink)
        paymentlink.click()
        time.sleep(3)
        pay_by_cash = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Pay by Cash']"))
        )
        pay_by_cash.click()
        time.sleep(5)
        paymentnote = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname = 'paymentNote']"))
        )
        paymentnote.click()
        time.sleep(2)
        paymentnote.send_keys("Fully Paid")
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Pay']"))
        ).click()
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
        ).click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(2)
        expected_message = "Payment completed successfully"
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
@allure.title("Create_Draft_With_Existing_consumer")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_Draft_Consumer(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//img[contains(@src, 'settings.gif')]//following::div[contains(text(),'Settings')]")
        time.sleep(2)
        POS = wait_and_locate_click(login, By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(login, POS)       
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p[normalize-space()='Sales Order Management System']")
        time.sleep(2)
        Sales_order = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']")) 
            )
        aria_checked = Sales_order.get_attribute("aria-checked")
        if aria_checked == "true":
            print("Sales Orders Management is already active, no need to click.")
        else:
            Sales_order.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
        time.sleep(3)
        draftorder = wait_and_locate_click(login, By.XPATH, "//span[@class='lnk setings ml-auto text-capitalize']")
        scroll_to_element(login, draftorder)
        time.sleep(2)
        draftorder_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@id='mat-mdc-slide-toggle-2-button'])[1]")))
        aria_checked = draftorder_button.get_attribute("aria-checked")
        if aria_checked == "true":
            draftorder_button.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
        else:
            print("Draft Order is already active, no need to click.")
        time.sleep(2)
        wait_and_click(login, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor text-capitalize']", 20)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[2]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search customers']", "5550004454")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 1']")
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
@allure.title("Create_Draft_With_New_consumer")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_Draft_NewConsumer(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//img[contains(@src, 'settings.gif')]//following::div[contains(text(),'Settings')]")
        time.sleep(2)
        POS = wait_and_locate_click(login, By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(login, POS)       
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p[normalize-space()='Sales Order Management System']")
        time.sleep(2)
        Sales_order = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']")) 
            )
        aria_checked = Sales_order.get_attribute("aria-checked")
        if aria_checked == "true":
            print("Sales Orders Management is already active, no need to click.")
        else:
            Sales_order.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
        time.sleep(3)
        draftorder = wait_and_locate_click(login, By.XPATH, "//span[@class='lnk setings ml-auto text-capitalize']")
        scroll_to_element(login, draftorder)
        time.sleep(2)
        draftorder_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@id='mat-mdc-slide-toggle-2-button'])[1]")))
        aria_checked = draftorder_button.get_attribute("aria-checked")
        if aria_checked == "true":
            draftorder_button.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
        else:
            print("Draft Order is already active, no need to click.")
        time.sleep(2)
        wait_and_click(login, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor text-capitalize']", 20)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-icon pi pi-plus']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//mat-select[@placeholder='Select']")
        time.sleep(3)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        salutation_option_element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, salutation_option_xpath))
        )
        salutation_option_element.click()
        time.sleep(3)
        first_name, last_name, phonenumber, email = create_users_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='mobileNumber']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//span[normalize-space()='Save']").click()
        time.sleep(3)
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
        time.sleep(3)
        paymentlink = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        scroll_to_element(login, paymentlink)
        paymentlink.click()
        time.sleep(3)
        pay_by_others = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Pay by Others']"))
        )
        pay_by_others.click()
        time.sleep(5)
        paymentnote = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname = 'paymentNote']"))
        )
        paymentnote.click()
        time.sleep(2)
        paymentnote.send_keys("Fully Paid")
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Pay']"))
        ).click()
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
        ).click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(2)
        expected_message = "Payment completed successfully"
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
@allure.title("Create_Draft_Checking_ConsumerVisibility")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_Draft_ConsumerVisibility(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//img[contains(@src, 'settings.gif')]//following::div[contains(text(),'Settings')]")
        time.sleep(2)
        POS = wait_and_locate_click(login, By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(login, POS)       
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p[normalize-space()='Sales Order Management System']")
        time.sleep(2)
        Sales_order = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']")) 
            )
        aria_checked = Sales_order.get_attribute("aria-checked")
        if aria_checked == "true":
            print("Sales Orders Management is already active, no need to click.")
        else:
            Sales_order.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
        time.sleep(3)
        draftorder = wait_and_locate_click(login, By.XPATH, "//span[@class='lnk setings ml-auto text-capitalize']")
        scroll_to_element(login, draftorder)
        time.sleep(2)
        draftorder_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@id='mat-mdc-slide-toggle-2-button'])[1]")))
        aria_checked = draftorder_button.get_attribute("aria-checked")
        if aria_checked == "true":
            draftorder_button.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
        else:
            print("Draft Order is already active, no need to click.")
        time.sleep(2)
        wait_and_click(login, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor text-capitalize']", 20)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
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
        try:
            consumer_button = login.find_element(By.XPATH, "//div[@class='card ng-star-inserted']")  
            is_visible = consumer_button.is_displayed()
            if not is_visible:
                print("Consumer button is NOT showing after confirming the order.")
            else:
                print("Consumer button is showing after confirming the order.")
        except NoSuchElementException:
            print("Consumer button is NOT present after confirming the order.")
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
        paymentlink = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        scroll_to_element(login, paymentlink)
        paymentlink.click()
        time.sleep(3)
        pay_by_cash = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Pay by Cash']"))
        )
        pay_by_cash.click()
        time.sleep(5)
        paymentnote = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname = 'paymentNote']"))
        )
        paymentnote.click()
        time.sleep(2)
        paymentnote.send_keys("Fully Paid")
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Pay']"))
        ).click()
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
        ).click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(2)
        expected_message = "Payment completed successfully"
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