
from Framework.common_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with disabling Create Salesorder Catalog")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_createordercatalog(login):
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
        catalog_management = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Sales Order Catalog Settings']"))
            )
        scroll_to_element(login, catalog_management)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Create Sales Order Catalog')]/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the create order catalog..")
            create_order_catalog = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[9]"))
            )
            create_order_catalog.click()
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
        create_catalog = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Catalogs')]"))
        )
        create_catalog.click()
        time.sleep(3)
        create_catalog_button = WebDriverWait(login, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//button[@class='p-ripple p-element p-button p-component']"))
        )
        if not create_catalog_button:
            print("Testcase Failed: Create Order Catalogs button is visible after disabling checkbox.")
            assert False, "Create Order Catalogs button should NOT be visible after disabling the checkbox!"
        else:
            print("Test passed: Create Order Catalogs button is NOT visible after disabling checkbox.")
        time.sleep(3)
        
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     

   

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with enabling Create Salesorder Catalog")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_createordercatalog(login):
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
        catalog_management = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Sales Order Catalog Settings']"))
            )
        scroll_to_element(login, catalog_management)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Create Sales Order Catalog')]/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to enabled the create order catalog..")
            create_order_catalog = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[9]"))
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
        create_catalog = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Catalogs')]"))
        )
        create_catalog.click()
        time.sleep(3)
        create_catalog_button = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//button[@class='p-ripple p-element p-button p-component']"))
          )
        assert create_catalog_button.is_displayed(), "Create_catalog button is NOT displayed after enabling checkbox!"
        print("Create_catalog button is displayed. Proceeding to create catalog.")
        create_catalog_button.click()
        time.sleep(2)
        Order_catalog = "Order_Catalog_" + str(uuid.uuid4())[:8]
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Catalog Name']", Order_catalog)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Select Store']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdownitem[1]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@formcontrolname ='onlineSelfOrder']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Yes']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@formcontrolname='walkInPOS']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Yes']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@formcontrolname='storePickup']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Yes']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@formcontrolname='homeDelivery']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Yes']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save & Next']")
        time.sleep(2)
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with disabling Update Salesorder Catalog")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_updateordercatalog(login):
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
        catalog_management = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Sales Order Catalog Settings']"))
            )
        scroll_to_element(login, catalog_management)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Update Sales Order Catalog')]/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the create order catalog..")
            update_order_catalog = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[10]"))
            )
            update_order_catalog.click()
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
        create_catalog = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Catalogs')]"))
        )
        create_catalog.click()
        time.sleep(3)
        action_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Actions'])[1]"))
        )
        action_button.click()
        time.sleep(3)
        edit_catalog = WebDriverWait(login, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "(//button[@role='menuitem'])[2]"))
        )
        if not edit_catalog:
            print("Testcase Failed: Order Catalogs Edit button is visible after disabling checkbox.")
            assert False, "Order Catalogs Edit button should NOT be visible after disabling the checkbox!"
        else:
            print("Test passed: Order Catalogs Edit button is NOT visible after disabling checkbox.")
        time.sleep(3)
        
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with enabling Update Salesorder Catalog")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_updateordercatalog(login):
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
        catalog_management = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Sales Order Catalog Settings']"))
            )
        scroll_to_element(login, catalog_management)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Update Sales Order Catalog')]/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to enabled the create order catalog..")
            update_order_catalog = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[10]"))
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
        create_catalog = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Catalogs')]"))
        )
        create_catalog.click()
        time.sleep(3)
        action_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Actions'])[1]"))
        )
        action_button.click()
        time.sleep(3)
        edit_catalog = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@role='menuitem'])[2]"))
        )
        assert edit_catalog.is_displayed(), "Edit_catalog button is NOT displayed after enabling checkbox!"
        print("Edit_catalog  button is displayed. Proceeding to create catalog.")
        edit_catalog.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Update Catalog']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[2]")
        toasts= WebDriverWait(login, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "p-toast-detail"))
        )
        for toast in toasts:
            print("toast_Message:", toast.text)
        time.sleep(2)
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with disabling Update Salesorder Catalog")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_viewordercatalog(login):
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
        catalog_management = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Sales Order Catalog Settings']"))
            )
        scroll_to_element(login, catalog_management)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'View Sales Order Catalog')]/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the create order catalog..")
            view_order_catalog = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[11]"))
            )
            view_order_catalog.click()
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
        create_catalog = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Catalogs')]"))
        )
        create_catalog.click()
        time.sleep(3)
        action_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Actions'])[1]"))
        )
        action_button.click()
        time.sleep(3)
        view_catalog = WebDriverWait(login, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "(//button[@role='menuitem'])[2]"))
        )
        if not view_catalog:
            print("Testcase Failed: Order Catalogs View button is visible after disabling checkbox.")
            assert False, "Order Catalogs View button should NOT be visible after disabling the checkbox!"
        else:
            print("Test passed: Order Catalogs View button is NOT visible after disabling checkbox.")
        time.sleep(3)
        
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e  
     

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with enabling View Salesorder Catalog")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_viewordercatalog(login):
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
        catalog_management = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Sales Order Catalog Settings']"))
            )
        scroll_to_element(login, catalog_management)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'View Sales Order Catalog')]/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to enabled the create order catalog..")
            view_order_catalog = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[11]"))
            )
            view_order_catalog.click()
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
        create_catalog = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Catalogs')]"))
        )
        create_catalog.click()
        time.sleep(3)
        action_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Actions'])[1]"))
        )
        action_button.click()
        time.sleep(3)
        view_catalog = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@role='menuitem'])[1]"))
        )
        assert view_catalog.is_displayed(), "View_catalog button is NOT displayed after enabling checkbox!"
        print("View_catalog  button is displayed. Proceeding to create catalog.")
        view_catalog.click()
        time.sleep(2)
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e


   
