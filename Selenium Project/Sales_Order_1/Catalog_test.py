from Framework.common_utils import *
from Framework.common_dates_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Catalog")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_Catalog(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Catalogs')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-ripple p-element p-button p-component']")
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
        add_Item = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-checkbox'])[2]")) 
            )
        native_checkbox = add_Item.find_element(By.XPATH, ".//input[@type='checkbox']")
        if native_checkbox.is_selected():
            print("Item is already added, no need to again added.")
        else:
            add_Item.click()
        wait_and_locate_click(login, By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[2]")
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(1)
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Edit Details']")
        time.sleep(3)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Display Order']", 1)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Yes']")
        time.sleep(2)
        MRP= WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//input[@placeholder='Enter Price'])[1]"))
        )
        MRP.clear()
        MRP.send_keys("1000")
        time.sleep(2)
        Sales_price = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//input[@placeholder='Enter Price'])[2]"))
        )
        Sales_price.clear()
        Sales_price.send_keys("800")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='p-multiselect-label p-placeholder']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[@aria-label='GST 5%']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Save']")
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Active_Catalog_Filter")
@pytest.mark.parametrize("url", ["https://scale.jaldeetest.in/business/"])
def test_Active_Catalog_Filter(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Catalogs')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[3]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'Select Status')]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Active']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-raised p-button-primary font-weight-bold p-button p-component']")
        time.sleep(5)
        
        while True:
            try:
                print("Checking current page for Active catalogs...")
                time.sleep(3) 
                table_body = WebDriverWait(login, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//tbody"))
                )
                active_catalogs = []
                # Get all rows in the table
                table_rows = table_body.find_elements(By.XPATH, ".//tr")
                print(f"Found {len(table_rows)} rows on this page.")
                if not table_rows:
                    print("No more rows found. Stopping iteration.")
                    break
                for row in table_rows:
                    try:
                        
                        toggle_button = row.find_element(By.XPATH, ".//div[contains(@class,'p-inputswitch')]")
                        is_active = 'p-inputswitch-checked' in toggle_button.get_attribute('class')
                        print(f"Toggle button status: {'Active' if is_active else 'Inactive'}")

                        catalog_name = row.find_element(By.XPATH, ".//div[contains(@class, 'fw-bold')]").text
                        if is_active:
                            active_catalogs.append(catalog_name)
                            print("Active catalog found:", catalog_name)
                        
                    except Exception as row_error:
                        print(f"Error processing row: {row_error}")
                # Check for the next button and click if available
                try:
                    next_page_button = login.find_element(By.XPATH, "//button[@class='p-ripple p-element p-paginator-next p-paginator-element p-link']")
                    scroll_to_element(login, next_page_button)
                    if next_page_button.is_enabled():
                        next_page_button.click()
                        time.sleep(3)
                        tbody = WebDriverWait(login, 20).until(
                        EC.visibility_of_element_located((By.XPATH, "//tbody"))
                        )
                        scroll_to_element(login, tbody)
                        time.sleep(3) 
                    else:
                        break 
                except NoSuchElementException:
                    break
                # Assertions for the active catalogs
                assert len(active_catalogs) > 0, "Expected active catalogs but found none."

            except TimeoutException:
                print("A timeout occurred while waiting for the table.")
                break

        # Click to refresh and close
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-icon p-button-icon-left pi pi-refresh']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon p-sidebar-close-icon'])[1]")
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("InActive_Catalog_Filter")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Inactive_Catalog_Filter(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Catalogs')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[3]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'Select Status')]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Inactive']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-raised p-button-primary font-weight-bold p-button p-component']")
        time.sleep(5)
        
        while True:
            try:
                print("Checking current page for InActive catalogs...")
                time.sleep(3) 
                table_body = WebDriverWait(login, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//tbody"))
                )
                inactive_catalogs = []
                # Get all rows in the table
                table_rows = table_body.find_elements(By.XPATH, ".//tr")
                print(f"Found {len(table_rows)} rows on this page.")
                if not table_rows:
                    print("No more rows found. Stopping iteration.")
                    break
                for row in table_rows:
                    try:
                        
                        toggle_button = row.find_element(By.XPATH, ".//div[contains(@class,'p-inputswitch')]")
                        is_active = 'p-inputswitch-checked' in toggle_button.get_attribute('class')
                        print(f"Toggle button status: {'Active' if is_active else 'Inactive'}")

                        catalog_name = row.find_element(By.XPATH, ".//div[contains(@class, 'fw-bold')]").text
                        if not is_active:
                            inactive_catalogs.append(catalog_name)
                            print("InActive catalog found:", catalog_name)
                        
                    except Exception as row_error:
                        print(f"Error processing row: {row_error}")
                # Check for the next button and click if available
                try:
                    next_page_button = login.find_element(By.XPATH, "//button[@class='p-ripple p-element p-paginator-next p-paginator-element p-link']")
                    scroll_to_element(login, next_page_button)
                    if next_page_button.is_enabled():
                        next_page_button.click()
                        time.sleep(3)
                        tbody = WebDriverWait(login, 20).until(
                        EC.visibility_of_element_located((By.XPATH, "//tbody"))
                        )
                        scroll_to_element(login, tbody)
                        time.sleep(3) 
                    else:
                        break 
                except NoSuchElementException:
                    break
                # Assertions for the active catalogs
                assert len(inactive_catalogs) > 0, "Expected inactive catalogs but found none."

            except TimeoutException:
                print("A timeout occurred while waiting for the table.")
                break

        # Click to refresh and close
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-icon p-button-icon-left pi pi-refresh']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon p-sidebar-close-icon'])[1]")
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  