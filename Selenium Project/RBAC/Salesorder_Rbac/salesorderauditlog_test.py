from Framework.common_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with disabling Auditlog ")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_Auditlog(login):
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
        Sales_Order_Auditlog = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Sales Order Auditlog']"))
            )
        scroll_to_element(login, Sales_Order_Auditlog)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'View Order Auditlog')]/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the Audit log ..")
            audit_log = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[19]"))
            )
            audit_log.click()
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
        order_audit_logs1 = WebDriverWait(login, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//button[@label='Log']"))
        )
        if not order_audit_logs1:
            print("Testcase Failed: order_audit_logs button is visible after disabling checkbox.")
            assert False, "order_audit_logs button should NOT be visible after disabling the checkbox!"
        else:
            print("Test passed: order_audit_logs button is NOT visible after disabling checkbox.")
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
        time.sleep(2)
        order_audit_logs2 = WebDriverWait(login, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//button[@label='Log']"))
        )
        if not order_audit_logs2:
            print("Testcase Failed: order_audit_logs button is visible after disabling checkbox.")
            assert False, "order_audit_logs button should NOT be visible after disabling the checkbox!"
        else:
            print("Test passed: order_audit_logs button is NOT visible after disabling checkbox.")
        time.sleep(3)
        create_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Invoice']"))
        )
        create_Invoice.click()
        time.sleep(2)
        order_audit_logs3 = WebDriverWait(login, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//button[@label='Log']"))
        )
        if not order_audit_logs3:
            print("Testcase Failed: order_audit_logs button is visible after disabling checkbox.")
            assert False, "order_audit_logs button should NOT be visible after disabling the checkbox!"
        else:
            print("Test passed: order_audit_logs button is NOT visible after disabling checkbox.")
        time.sleep(3)
        view_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='View Invoice']"))
        )
        scroll_to_element(login, view_Invoice)
        view_Invoice.click()
        time.sleep(2)
        order_audit_logs4 = WebDriverWait(login, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//button[@label='Log']"))
        )
        if not order_audit_logs4:
            print("Testcase Failed: order_audit_logs button is visible after disabling checkbox.")
            assert False, "order_audit_logs button should NOT be visible after disabling the checkbox!"
        else:
            print("Test passed: order_audit_logs button is NOT visible after disabling checkbox.")
        time.sleep(3)
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with enabling Audit Log")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_auditlog(login):
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
        Sales_Order_Auditlog = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Sales Order Auditlog']"))
            )
        scroll_to_element(login, Sales_Order_Auditlog)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'View Order Auditlog')]/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to enabled the vieworder auditlog..")
            audit_log = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[19]"))
            )
            audit_log.click()
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
        order_audit_logs1 = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@label='Log']"))
        )
        assert order_audit_logs1.is_displayed(), "Order_audit_logs1 button is NOT displayed after enabling checkbox!"
        print("Order_audit_logs1 button is displayed.")
        order_audit_logs1.click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-times']"))
        ).click()
        time.sleep(2)
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
        time.sleep(2)
        order_audit_logs2 = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@label='Log']"))
        )
        scroll_to_element(login, order_audit_logs2)
        time.sleep(2)
        assert order_audit_logs2.is_displayed(), "Order_audit_logs2 button is NOT displayed after enabling checkbox!"
        print("Order_audit_logs2 button is displayed.")
        order_audit_logs2.click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-times']"))
        ).click()
        time.sleep(2)
        create_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Invoice']"))
        )
        create_Invoice.click()
        time.sleep(2)
        order_audit_logs3 = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@label='Log']"))
        )
        scroll_to_element(login, order_audit_logs3)
        time.sleep(2)
        assert order_audit_logs3.is_displayed(), "Order_audit_logs3 button is NOT displayed after enabling checkbox!"
        print("Order_audit_logs3 button is displayed.")
        order_audit_logs3.click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-times']"))
        ).click()
        time.sleep(2)
        view_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='View Invoice']"))
        )
        scroll_to_element(login, view_Invoice)
        view_Invoice.click()
        time.sleep(2)
        order_audit_logs4 = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@label='Log']"))
        )
        scroll_to_element(login, order_audit_logs4)
        time.sleep(2)
        assert order_audit_logs4.is_displayed(), "Order_audit_logs4 button is NOT displayed after enabling checkbox!"
        print("Order_audit_logs4 button is displayed.")
        order_audit_logs4.click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-times']"))
        ).click()
        time.sleep(2)
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with disabling EditAuditlog ")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_editAuditlog(login):
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
        Sales_Order_Auditlog = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Sales Order Auditlog']"))
            )
        scroll_to_element(login, Sales_Order_Auditlog)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'View Order Auditlog')]/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the Audit log ..")
            audit_log = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[19]"))
            )
            audit_log.click()
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
        saveasdraft = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Save as draft']"))
        )
        scroll_to_element(login, saveasdraft)
        time.sleep(2)
        saveasdraft.click()
        time.sleep(3)
        order_audit_logs1 = WebDriverWait(login, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//button[@label='Log']"))
        )
        if not order_audit_logs1:
            print("Testcase Failed: order_audit_logs button is visible after disabling checkbox.")
            assert False, "order_audit_logs button should NOT be visible after disabling the checkbox!"
        else:
            print("Test passed: order_audit_logs button is NOT visible after disabling checkbox.")
        time.sleep(2)
        Editorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Edit Order']"))
        )
        Editorder.click()
        time.sleep(3)
        updateorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Update Order']"))
        )
        scroll_to_element(login, updateorder)
        time.sleep(2)
        updateorder.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(2)
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        print("Toast Message:", toast_message.text)
        order_audit_logs2 = WebDriverWait(login, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//button[@label='Log']"))
        )
        if not order_audit_logs2:
            print("Testcase Failed: order_audit_logs button is visible after disabling checkbox.")
            assert False, "order_audit_logs button should NOT be visible after disabling the checkbox!"
        else:
            print("Test passed: order_audit_logs button is NOT visible after disabling checkbox.")
        time.sleep(3)
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with enabling editAudit Log")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_editauditlog(login):
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
        Sales_Order_Auditlog = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Sales Order Auditlog']"))
            )
        scroll_to_element(login, Sales_Order_Auditlog)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'View Order Auditlog')]/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to enabled the vieworder auditlog..")
            audit_log = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[19]"))
            )
            audit_log.click()
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
        saveasdraft = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Save as draft']"))
        )
        scroll_to_element(login, saveasdraft)
        time.sleep(2)
        saveasdraft.click()
        time.sleep(3)
        order_audit_logs1 = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@label='Log']"))
        )
        assert order_audit_logs1.is_displayed(), "Order_audit_logs1 button is NOT displayed after enabling checkbox!"
        print("Order_audit_logs1 button is displayed.")
        order_audit_logs1.click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-times']"))
        ).click()
        time.sleep(2)
        Editorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Edit Order']"))
        )
        Editorder.click()
        time.sleep(3)
        updateorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Update Order']"))
        )
        scroll_to_element(login, updateorder)
        time.sleep(2)
        updateorder.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(2)
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        print("Toast Message:", toast_message.text)
        order_audit_logs2 = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@label='Log']"))
        )
        scroll_to_element(login, order_audit_logs2)
        time.sleep(2)
        assert order_audit_logs2.is_displayed(), "Order_audit_logs2 button is NOT displayed after enabling checkbox!"
        print("Order_audit_logs2 button is displayed.")
        order_audit_logs2.click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-times']"))
        ).click()
        time.sleep(2)
     except Exception as e:
            allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page", 
            attachment_type=AttachmentType.PNG,
            )
            raise e     