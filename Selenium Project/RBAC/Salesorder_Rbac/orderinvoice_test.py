from Framework.common_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with disabling Create Salesorder Invoice ")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_createorderInvoice(login):
     try:
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Settings')]")
        time.sleep(2)
        rbac = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='RBAC']"))
            )
        scroll_to_element(login, rbac)
        time.sleep(2)
        rbac.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//h2[normalize-space()='Roles']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Jaldee Order POS']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//tbody/tr[2]/td[3]/div[1]/div[1]/p-button[1]/button[1]/span[1]")
        time.sleep(2)
        salesorder_invoice = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Sales Order Invoice']"))
            )
        scroll_to_element(login, salesorder_invoice)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Create Order Invoice')]/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the create order invoice ..")
            create_order = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[12]"))
            )
            create_order.click()
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        else:
            pass
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[4]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        create_order = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Create Order')]"))
        )
        create_order.click()
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search patients']", "5550009954")
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
        time.sleep(3)
        createorderinvoice = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@class='p-element draft-button me-1 p-button p-component'])[1]"))
        )
        scroll_to_element(login, createorderinvoice)
        time.sleep(2)
        createorderinvoice.click()
        Permission_error = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@role='alert']"))
        )
        permission_error_message = Permission_error.text
        print("Permission error message:", permission_error_message)
        expected_message = "Sorry! You have no permission to process this request!!!"
        assert permission_error_message == expected_message, f"Unexpected error message: {permission_error_message}"
        time.sleep(4)
        complete_Order = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Complete Order']"))
        )
        scroll_to_element(login, complete_Order)
        time.sleep(3)
        complete_Order.click()
        time.sleep(3)
        createorderinvoice = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@class='p-element draft-button me-1 p-button p-component'])[1]"))
        )
        scroll_to_element(login, createorderinvoice)
        time.sleep(2)
        createorderinvoice.click()
        Permission_error = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@role='alert']"))
        )
        permission_error_message = Permission_error.text
        print("Permission error message:", permission_error_message)
        expected_message = "Sorry! You have no permission to process this request!!!"
        assert permission_error_message == expected_message, f"Unexpected error message: {permission_error_message}"
        time.sleep(3)
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with enabling Create Order_Invoice")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_OrderInvoice(login):
     try:
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Settings')]")
        time.sleep(2)
        rbac = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='RBAC']"))
            )
        scroll_to_element(login, rbac)
        time.sleep(2)
        rbac.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//h2[normalize-space()='Roles']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Jaldee Order POS']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//tbody/tr[2]/td[3]/div[1]/div[1]/p-button[1]/button[1]/span[1]")
        time.sleep(2)
         salesorder_invoice = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Sales Order Invoice']"))
            )
        scroll_to_element(login, salesorder_invoice)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Create Order Invoice')]/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to enabled the create order catalog..")
            create_order_catalog = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[12]"))
            )
            create_order_catalog.click()
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[4]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        create_order = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Create Order')]"))
        )
        assert create_order.is_displayed(), "Create_Order button is NOT displayed after enabling checkbox!"
        print("Create_Order button is displayed. Proceeding to create order.")
        create_order.click()
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search patients']", "5550009954")
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
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e