import time
import allure

from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.common.exceptions import ElementClickInterceptedException



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create a catalog with adding the Item")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_sales_order_catalog_with_item(login):
    try:
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[4]"))    
        ).click()

        time.sleep(1)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-button[@id='btnCrtCat_ORD_OrdCat'])[1]"))
        ).click()

        time.sleep(2)

        catalog_name = "Catalog_" + str(uuid.uuid4())[:6]
        print(catalog_name)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='inputCatName_ORD_CatCrt'])[1]"))
        ).send_keys(catalog_name)
        
        dropdown = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "(//p-dropdown[@id='selectStore_ORD_CatCrt'])[1]"))
        )
        dropdown.click()
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='B&B Stores'])[1]"))
        ).click()
    
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-dropdown[@id='selectOrdType_ORD_CatCrt'])[1]"))
        ).click()
        time.sleep(1)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Yes'])[1]"))
        ).click()
    
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnSave_ORD_CatCrt']"))
        ).click()

        time.sleep(3)
    
        start_index = 2   # First checkbox to select
        end_index = 4     # Last checkbox to select

        # Find all checkboxes using XPath
        checkboxes = login.find_elements(By.XPATH, "//input[@id='SelectItem_ORD_ItemSelection-input']")

        # Iterate and select checkboxes within the range
        for i in range(start_index - 1, min(end_index, len(checkboxes))):  # Adjusting for 0-based index
            if not checkboxes[i].is_selected():  # Check if not already selected
                checkboxes[i].click()

        # Confirm selections
        selected_checkboxes = [cb.get_attribute("id") for cb in checkboxes if cb.is_selected()]
        print(f"Selected checkboxes: {selected_checkboxes}")

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnSubmitItems_ORD_ItemSelection']"))
        ).click()

        
        # Wait for the dialog to appear
        dialog = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//p[contains(text(),'Warning: Once added to the catalog, item’s attribu')])[1]"))
        )

        # Extract the warning message
        warning_text = dialog.text
        print("message :", warning_text)
        # Expected message
        expected_message = "Warning: Once added to the catalog, item’s attributes cannot be edited. Do you want to proceed?"

        # Assert the warning message  
        assert warning_text.strip() == expected_message, f"Expected '{expected_message}', but got '{warning_text}'"

        # Click the "Yes" button
        yes_button = login.find_element(By.XPATH, "(//button[normalize-space()='Yes'])[1]")
        yes_button.click()

        time.sleep(5)

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create Catalog without item")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_sales_order_catalog(login):
    try:

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[4]"))    
        ).click()

        time.sleep(1)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-button[@id='btnCrtCat_ORD_OrdCat'])[1]"))
        ).click()

        time.sleep(2)

        catalog_name = "Catalog_" + str(uuid.uuid4())[:6]
        print(catalog_name)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='inputCatName_ORD_CatCrt'])[1]"))
        ).send_keys(catalog_name)
        
        dropdown = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//p-dropdown[@id='selectStore_ORD_CatCrt']"))
        )
        dropdown.click()
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='B&B Stores'])[1]"))
        ).click()
    
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@id='selectOrdType_ORD_CatCrt']"))
        ).click()
        time.sleep(1)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Yes'])[1]"))
        ).click()
    
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnSave_ORD_CatCrt']"))
        ).click()

        time.sleep(3)
    
        # start_index = 2   # First checkbox to select
        # end_index = 4     # Last checkbox to select

        # # Find all checkboxes using XPath
        # checkboxes = login.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'mat-mdc-checkbox')]")

        # # Iterate and select checkboxes within the range
        # for i in range(start_index - 1, min(end_index, len(checkboxes))):  # Adjusting for 0-based index
        #     if not checkboxes[i].is_selected():  # Check if not already selected
        #         checkboxes[i].click()

        # # Confirm selections
        # selected_checkboxes = [cb.get_attribute("id") for cb in checkboxes if cb.is_selected()]
        # print(f"Selected checkboxes: {selected_checkboxes}")

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-times'])[1]"))
        ).click()

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(5)

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e

allure.severity(allure.severity_level.CRITICAL)
@allure.title("Update the catalog name")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_sales_order_catalog_update(login):
    try:

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[4]"))    
        ).click()

        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnActMenu_ORD_OrdCat'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnEdtCat_ORD_OrdCat'])[1]")
        
        time.sleep(2)
        catalog_rename = "Catalog_Rename" + str(uuid.uuid4())[:6]
        print("Catalog name : ", catalog_rename)
        catalog_name = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='inputCatName_ORD_CatCrt'])[1]"))
        )
        catalog_name.clear()
        time.sleep(1)
        catalog_name.send_keys(catalog_rename)
        
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnSave_ORD_CatCrt']"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-times'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e
    
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Enable and Disable the sales order Catalog")
def test_sales_order_catalog_enable_disable(login):
    try:
        wait = WebDriverWait(login, 20)

        # Step 1: Open the Inventory module
        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//img)[2]"))).click()

        # Step 2: Select store
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH,
                              "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH,
                              "//*[@class='ng-star-inserted'][normalize-space()='B&B Stores']")

        # Step 3: Navigate to Inv.Catalogs
        time.sleep(3)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//*[contains(text(),'Catalogs')])[1]"))).click()

        # Step 4: Capture current state
        time.sleep(3)
        row = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//tbody[@class='p-element p-datatable-tbody']//tr[1]")))
        catalog_name = row.find_element(By.XPATH, ".//div[@class='fw-bold']").text.strip()
        switch_input = row.find_element(By.XPATH, ".//input[@type='checkbox']")
        current_state = switch_input.get_attribute("aria-checked")

        print(f"\n📦 Catalog: {catalog_name}")
        print(f"➡️  Initial State: {'Enabled ✅' if current_state == 'true' else 'Disabled ❌'}")

        # Step 5: Disable if currently enabled
        if current_state == "true":
            wait_and_locate_click(login, By.XPATH,
                                  "(//*[@aria-haspopup='menu'][normalize-space()='Actions'])[1]")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH,
                                  "(//span[@class='mdc-list-item__primary-text'])[1]")
            time.sleep(1)
            wait_and_locate_click(login, By.XPATH, "//*[normalize-space()='Disable']")
            time.sleep(2)
            msg = get_toast_message(login)
            print("📢 Toast (Disable):", msg)

            # Verify disabled
            time.sleep(3)
            wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

            time.sleep(3)
            new_state = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//tbody[@class='p-element p-datatable-tbody']//tr[1]//input[@type='checkbox']"))
            ).get_attribute("aria-checked")

            print(f"➡️  After Disable: {'Enabled ✅' if new_state == 'true' else 'Disabled ❌'}")
            assert new_state == "false", "❌ Catalog was not disabled!"

        # Step 6: Enable back
        wait_and_locate_click(login, By.XPATH,
                              "(//*[@aria-haspopup='menu'][normalize-space()='Actions'])[1]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH,
                              "(//span[@class='mdc-list-item__primary-text'])[1]")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//*[normalize-space()='Enable']")
        time.sleep(2)
        msg = get_toast_message(login)
        print("📢 Toast (Enable):", msg)

        # Verify enabled
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")
        
        time.sleep(2)
        final_state = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//tbody[@class='p-element p-datatable-tbody']//tr[1]//input[@type='checkbox']"))
        ).get_attribute("aria-checked")

        print(f"➡️  After Enable: {'Enabled ✅' if final_state == 'true' else 'Disabled ❌'}")
        assert final_state == "true", "❌ Catalog was not enabled back!"

        print(f"🎯 Catalog '{catalog_name}' successfully Disabled and then Enabled back.")

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="inventory_catalog_enable_disable_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e

@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Enable and Disable the Inventory Catalog using Toggle")
def test_inventory_catalog_enable_disable_with_toggle(login):
    try:
        wait = WebDriverWait(login, 20)

        # Step 1: Open the Inventory module
        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//img)[2]"))).click()

        # Step 2: Select store
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH,
                              "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH,
                              "//*[@class='ng-star-inserted'][normalize-space()='B&B Stores']")

        # Step 3: Navigate to Inv.Catalogs
        time.sleep(3)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//*[contains(text(),'Catalogs')])[1]"))).click()

        # Step 4: Capture current state
        time.sleep(3)
        row = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//tbody[@class='p-element p-datatable-tbody']//tr[1]")))

        catalog_name = row.find_element(By.XPATH, ".//div[@class='fw-bold']").text.strip()
        switch_input = row.find_element(By.XPATH, ".//input[@type='checkbox']")
        current_state = switch_input.get_attribute("aria-checked")

        print(f"\n📦 Catalog: {catalog_name}")
        print(f"➡️ Initial State: {'Enabled ✅' if current_state == 'true' else 'Disabled ❌'}")

        # Step 5: Disable catalog if it's enabled
        if current_state == "true":
            wait_and_locate_click(login, By.XPATH, "(//*[@class='p-inputswitch-slider'])[1]")
            msg_disable = get_toast_message(login)
            print("📢 Toast Message (Disable):", msg_disable)

            time.sleep(3)
            login.refresh()
            time.sleep(5)

            new_switch = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//tbody[@class='p-element p-datatable-tbody']//tr[1]//input[@type='checkbox']")))
            new_state = new_switch.get_attribute("aria-checked")
            print(f"➡️ After Disable Toggle: {'Enabled ✅' if new_state == 'true' else 'Disabled ❌'}")
            assert new_state == "false", f"❌ Catalog '{catalog_name}' was not disabled!"
            print(f"✅ Assertion Passed: Catalog '{catalog_name}' is Disabled.")

        # Step 6: Enable the catalog
        wait_and_locate_click(login, By.XPATH, "(//*[@class='p-inputswitch-slider'])[1]")
        msg_enable = get_toast_message(login)
        print("📢 Toast Message (Enable):", msg_enable)

        time.sleep(3)
        login.refresh()
        time.sleep(5)

        new_switch_enable = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//tbody[@class='p-element p-datatable-tbody']//tr[1]//input[@type='checkbox']")))
        new_state_enable = new_switch_enable.get_attribute("aria-checked")
        print(f"➡️ After Enable Toggle: {'Enabled ✅' if new_state_enable == 'true' else 'Disabled ❌'}")
        assert new_state_enable == "true", f"❌ Catalog '{catalog_name}' was not enabled!"
        print(f"✅ Assertion Passed: Catalog '{catalog_name}' is Enabled.")

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="inventory_catalog_toggle_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Disable the sales order Catalog with active order")
def test_sales_order_catalog_disable_active_order(login):
    try:
        wait = WebDriverWait(login, 20)

        # Step 1: Open the Inventory module
        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//img)[2]"))).click()

        # Step 2: Select store
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH,
                              "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH,
                              "//*[@class='ng-star-inserted'][normalize-space()='B&B Stores']")

        # Step 3: Navigate to order.Catalogs
        time.sleep(3)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[3] "))).click()
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH,
                              "(//button[@id='btnActMenu_ORD_OrdCat'])[2]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH,
                              "(//button[@id='btnViewCata_ORD_OrdCat'])[1]")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//p-button[@id='btnCatSts_ORD_CatDet'])[1]")
        
        msg = get_toast_message(login)
        print("Toast Message : ", msg)
        time.sleep(3)
        
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="inventory_catalog_toggle_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e