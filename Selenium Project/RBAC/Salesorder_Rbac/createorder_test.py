from Framework.common_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with disabling Create Salesorder ")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_createorder(login):
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
        salesorder_settings = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Sales Order Settings']"))
            )
        scroll_to_element(login, salesorder_settings)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Create Order')]/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the create order ..")
            create_order = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[2]"))
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
        createorder = WebDriverWait(login, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[contains(text(),'Create Order')]"))
        )
        if not createorder:
            print("Testcase Failed: Create Order  button is visible after disabling checkbox.")
            assert False, "Create Order button should NOT be visible after disabling the checkbox!"
        else:
            print("Test passed: Create Order button is NOT visible after disabling checkbox.")
        time.sleep(3)
        
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with enabling Create Salesorder")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_createorder(login):
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
        salesorder_settings = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Sales Order Settings']"))
            )
        scroll_to_element(login, salesorder_settings)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Create Order')]/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to enabled the create order catalog..")
            create_order_catalog = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[2]"))
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
     

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with disabling Update Salesorder ")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_updateorder(login):
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
        salesorder_settings = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Sales Order Settings']"))
            )
        scroll_to_element(login, salesorder_settings)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Update Order']/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the update order ..")
            update_order = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[3]"))
            )
            update_order.click()
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
        wait_and_locate_click(login, By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Orders']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-button-label'])[1]")
        time.sleep(2)
        updateorder = WebDriverWait(login, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[normalize-space()='Edit Order']"))
        )
        if not updateorder:
            print("Testcase Failed: Update Order button is visible after disabling checkbox.")
            assert False, "Update Order button should NOT be visible after disabling the checkbox!"
        else:
            print("Test passed: Update Order button is NOT visible after disabling checkbox.")
        time.sleep(3)
        
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with enabling Update Salesorder")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_UpdateOrder(login):
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
        salesorder_settings = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Sales Order Settings']"))
            )
        scroll_to_element(login, salesorder_settings)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Update Order']/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to enabled the create order catalog..")
            update_order_catalog = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[3]"))
            )
            update_order_catalog.click()
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
        wait_and_locate_click(login, By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Orders']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-button-label'])[1]")
        time.sleep(2)
        edit_order = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Edit Order']"))
        )
        assert edit_order.is_displayed(), "Update_Order button is NOT displayed after enabling checkbox!"
        print("Update_Order button is displayed. Proceeding to update order.")
        edit_order.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
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
        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        time.sleep(2)
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     