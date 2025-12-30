import time
import uuid

from Framework.common_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale , password)])
@allure.title(" Create Inventoary Catalog")
def test_inventory_catalog(login):
    try:
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[3]"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@id='actionNav_ORD_Inventory'])[4]"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-button[@id='btnCreateCat_ORD_Catalog']"))
        ).click()

        catalog_name = "Inventory_Catalog_" + str(uuid.uuid4())[:6]

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='inputCatName_ORD_CatlgCreate']"))
        ).send_keys(catalog_name)

        login.find_element(By.XPATH, "//p-dropdown[@id='selectStore_ORD_CatlgCreate']").click()

        wait_and_locate_click(
            login, By.XPATH, "(//span[normalize-space()='B&B Stores'])[1]")

        wait_and_locate_click(login, By.XPATH, "//button[@id='btnCrtCat_ORD_CatlgCreate']")

        time.sleep(3)

        checkboxes = WebDriverWait(login, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//input[contains(@type, 'checkbox')]"))
        )

        # Click the first three checkboxes
        for i in range(1, min(6, len(checkboxes))):
            checkboxes[i].click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']"))
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

        time.sleep(3)
        msg = get_toast_message(login)
        print("Toast Message :", msg)
        
        time.sleep(3)
        wait_and_locate_click(
            login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(3)
        wait_and_locate_click(
            login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        store_dropdown = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='B&B Stores'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", store_dropdown)

        store_dropdown.click()

        time.sleep(5)
    
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e 


@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Inventory Catalog - Link catalog with sales order catalog ")
def test_Link_catalog_with_sales_order_catalog(login):
    driver = login
    try:

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//img)[2]")


        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[4]"
        )

        # Select store from dropdown
        wait_and_locate_click(
            login, By.XPATH,
            "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"
        )

        time.sleep(3)
        store = login.find_element(
            By.XPATH, "//*[@class='ng-star-inserted'][normalize-space()='B&B Stores']"
        )
        scroll_to_element(login, store)
        store.click()

        time.sleep(3)

        wait_and_locate_click(
            login, By.XPATH, "//p-button[@id='btnCrtCat_ORD_OrdCat']"
        )
        
        time.sleep(2)
        # wait_and_locate_click(
        #     driver, By.XPATH, "(//button[@id='btnActMenu_ORD_OrdCat'])[1]"
        # )

        Inv_sales_catalog_name = "Inv_Sales_Catalog_" + str(uuid.uuid4())[:6]
        # time.sleep(2)
        # wait_and_locate_click(
        #     driver, By.XPATH, "//button[@id='btnEdtCat_ORD_OrdCat']"
        # )

        time.sleep(2)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputCatName_ORD_CatCrt']", Inv_sales_catalog_name
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='selectStore_ORD_CatCrt']"
        )

        time.sleep(1)
        element1 = driver.find_element(By.XPATH, "//span[normalize-space()='B&B Stores']")
        scroll_to_element(driver, element1)
        element1.click()

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='selectInvMgmt_ORD_CatCrt']"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//*[@class='ng-star-inserted'][normalize-space()='Yes']"
        )     

        wait_and_locate_click(
            driver, By.XPATH, "//p-multiselect[@id='selectCatlog_ORD_CatCrt']"
        )       

        time.sleep(1)
        element2 = driver.find_element(By.XPATH, "//span[normalize-space()='Catalog_Inventory']")
        scroll_to_element(driver, element2)
        element2.click()

        wait_and_locate_click(
            driver, By.XPATH, "(//button[@class='p-ripple p-element p-multiselect-close p-link p-button-icon-only ng-star-inserted'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='selectOrdType_ORD_CatCrt']"
        )
        wait_and_locate_click(
            driver, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Yes']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='selectSelf_ORD_CatCrt']"
        )
        wait_and_locate_click(
            driver, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Yes']"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnSave_ORD_CatCrt']"
        )

        time.sleep(3)

        checkboxes = WebDriverWait(login, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//input[contains(@type, 'checkbox')]"))
        )

        # Click the first three checkboxes
        for i in range(1, min(6, len(checkboxes))):
            checkboxes[i].click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']"))
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

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        # time.sleep(3)

        # wait_and_locate_click(
        #     driver, By.XPATH, "(//div[@id='actionView_ORD_OrdCat'])[1]"
        # )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnEdtVItem_ORD_CatDet'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//p-dropdown[@id='selectMrp_ORD_AttrbtSltn'])[1]"
        )
        wait_and_locate_click(
            driver, By.XPATH, "(//span[normalize-space()='Yes'])[1]"
        )
        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//div[@id='actionMrp_ORD_AttrbtSltn']"
        )

        mrp_price = round(random.uniform(400, 600))
        print("Random MRP:", mrp_price)
        time.sleep(1)

        mrp_element = driver.find_element(By.XPATH, "(//input[@id='inputMrp_ORD_AttrbtSltn'])[1]")
        mrp_element.clear()
        mrp_element.send_keys(mrp_price)

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//div[@id='actionMrpAll_ORD_AttrbtSltn']"
        )

        sales_price = round(random.uniform(100, 399), 2)
        print("Random MRP:", sales_price)
        time.sleep(1)
        sales_price_element = driver.find_element(By.XPATH, "(//input[@id='inputPrice_ORD_AttrbtSltn'])[1]")
        sales_price_element.clear()
        sales_price_element.send_keys(sales_price)

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//div[@id='actionPrice_ORD_AttrbtSltn']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnSave_ORD_AttrbtSltn']"
        )

        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e
    

@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Inventory Catalog - Edit and Verify Updated Name")
def test_inventory_catalog_name_update(login):
    

    try:
        time.sleep(3)
        # Step 1: Open the Inventory module
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
        ).click()
        
        time.sleep(3)

        # Navigate to Inv.Catalogs
        wait_and_locate_click(login, By.XPATH, "(//div[@id='actionNav_ORD_Inventory'])[4]")

        # Select store from dropdown
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        time.sleep(3)
        store = login.find_element(By.XPATH, "//*[@class='ng-star-inserted'][normalize-space()='B&B Stores']")
        scroll_to_element(login, store)
        store.click()

        time.sleep(3)
        # Open Actions menu for the first catalog
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnActMenu_ORD_Catalog'])[1]")
        time.sleep(2)
        # Click 'Edit Catalog'
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnEditCat_ORD_Catalog']")

        time.sleep(3)
        # Step 2: Edit the catalog name
        name_field = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='inputCatName_ORD_CatlgCreate']"))
        )
        old_name = name_field.get_attribute("value")
        new_name = old_name + "_Edited"

        name_field.clear()
        name_field.send_keys(new_name)

        time.sleep(1)
        # Step 3: Click Update Catalog button
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnCrtCat_ORD_CatlgCreate']")

        msg = get_toast_message(login)
        print("Toast Message: ", msg)

        time.sleep(3)
        # Step 4: Click Done button (don't add any items)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnSelect_ORD_ItemSelection']")

        time.sleep(3)
        # Step 5: Click Back Arrow to return to Catalog list
        wait_and_locate_click(login, By.XPATH, "//div[@id='actionBack_ORD_CatlgDetls']")

        time.sleep(3)
        # Step 6: Assert that the edited name appears in the catalog table
        table_catalogs = login.find_elements(By.XPATH, "//tbody//tr//div[@class='fw-bold']")
        catalog_names = [c.text.strip() for c in table_catalogs]

        assert new_name in catalog_names, f"Catalog name not found after update! Expected '{new_name}', Found: {catalog_names}"

        allure.attach(
            login.get_screenshot_as_png(),
            name="catalog_name_verified",
            attachment_type=AttachmentType.PNG,
        )

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e

@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Enable and Disable the Inventory Catalog")
def test_inventory_catalog_enable_disable(login):
    try:
        wait = WebDriverWait(login, 20)

        # Step 1: Open the Inventory module
        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//img)[3]"))).click()

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
            (By.XPATH, "(//div[@id='actionNav_ORD_Inventory'])[4]"))).click()

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
                                  "(//button[@id='btnActMenu_ORD_Catalog'])[1]")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH,
                                  "//button[@id='btnViewCatlg_ORD_Catalog']")
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
                              "(//button[@id='btnActMenu_ORD_Catalog'])[1]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH,
                              "//button[@id='btnViewCatlg_ORD_Catalog']")
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
        wait.until(EC.presence_of_element_located((By.XPATH, "(//img)[3]"))).click()

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
            (By.XPATH, "//*[contains(text(),'Inv.Catalogs')]"))).click()

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
@allure.title("Inventory Catalog - Filter and Verify Results")
def test_inventory_catalog_filter(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 20)

        # Step 1: Navigate to Inventory Catalog
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
        ).click()

        time.sleep(3)
        # Select store from dropdown
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//*[@class='ng-star-inserted'][normalize-space()='B&B Stores']")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Inv.Catalogs')]"))
        ).click()

        # Step 2: Open filter and apply catalog name
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-filter-fill'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-accordion-toggle-icon p-icon'])[2]")

        time.sleep(2)
        filter_text = "Catalog_Inventory"
        wait_and_send_keys(login, By.XPATH, "//*[@id='catalogName']", filter_text)

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//*[normalize-space()='Apply']")

        time.sleep(3)
        rows = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//tbody[@class='p-element p-datatable-tbody']//div[@class='fw-bold']")
            )
        )

        # Step 4: Extract catalog names from table
        catalog_names = [row.text.strip() for row in rows if row.text.strip()]

        # Step 5: Print the catalog names found
        print(f"\n✅ Catalogs displayed after filtering: {catalog_names}\n")

        # Step 6: Assert all visible names contain the filter text
        assert catalog_names, "❌ No catalogs found after applying the filter!"
        for name in catalog_names:
            assert filter_text.lower() in name.lower(), f"❌ Filtered catalog '{name}' does not match filter '{filter_text}'"

        print(f"✅ All filtered catalogs correctly contain '{filter_text}'")

        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e 
    

@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Inventory Catalog - Edit and update the price of the item ")
def test_inventory_catalog_name_update_price(login):

    wait = WebDriverWait(login, 30)
    try:
        time.sleep(3)

        # Step 1: Open the Inventory module
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//img)[2]"))
        ).click()

        time.sleep(3)

        # Navigate to Inventory Catalogs
        wait_and_locate_click(
            login, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[4]"
        )

        # Select store from dropdown
        wait_and_locate_click(
            login, By.XPATH,
            "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"
        )

        time.sleep(3)
        store = login.find_element(
            By.XPATH, "//*[@class='ng-star-inserted'][normalize-space()='B&B Stores']"
        )
        scroll_to_element(login, store)
        store.click()

        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//div[@id='actionView_ORD_OrdCat'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "")

        

    
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e
 

