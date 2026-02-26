
from Framework.common_utils import *
from Framework.common_dates_utils import *
import random
from faker import Faker



# Global variable to store invoice type
invoice_type_name_global = None

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Create a Invoice type")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_invoice_type_1(login):
    global invoice_type_name_global
    driver = login
    wait = WebDriverWait(driver, 30)
    
    try:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        )).click()

        element = driver.find_element(By.XPATH, "(//span[normalize-space()='B&B Stores'])[1]")
        scroll_to_element(driver, element)

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[3]")

        invoice_type_name_global = f"Inv_Type_{str(uuid.uuid4())[:4]}"
        print("Created Invoice Type:", invoice_type_name_global)

        wait_and_locate_click(driver, By.XPATH, "//p-button[@id='btnCreate_ORD_InvTypes']")
        wait_and_send_keys(driver, By.XPATH, "//input[@id='typeName_ORD_InvTypeCre']", invoice_type_name_global)

        prefix = "p" + str(uuid.uuid4()).replace("-", "")[:3]
        suffix = "s" + str(uuid.uuid4()).replace("-", "")[:3]

        wait_and_send_keys(driver, By.XPATH, "//input[@id='typePrefix_ORD_InvTypeCre']", prefix)
        wait_and_send_keys(driver, By.XPATH, "//input[@id='typeSuffix_ORD_InvTypeCre']", suffix)

        status_switch = driver.find_element(
            By.XPATH, "//p-inputswitch[@id='status_ORD_InvTypeCre']//input[@role='switch']"
        )
        assert status_switch.get_attribute("aria-checked") == "true"

        wait_and_locate_click(driver, By.XPATH, "//button[@id='btnSave_ORD_InvTypeCre']")
        print("Toast Message:", get_toast_message(driver))

    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name="Failure Screenshot", attachment_type=AttachmentType.PNG)
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Enable Invoice type and Apply the Invoice type in Store")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_invoice_type_2(login):
    global invoice_type_name_global
    driver = login
    wait = WebDriverWait(driver, 30)

    # if not invoice_type_name_global:
    #     raise Exception("Invoice type not created yet! Run test_invoice_type_1 first.")

    try:
        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[5]")

        store_name = "B&B Stores"
        page = 1
        found = False
        time.sleep(3)
        while True:
            print(f"Searching for store '{store_name}' on page {page}")
            try:
                driver.find_element(
                    By.XPATH,
                    f"//div[normalize-space()='{store_name}']/ancestor::tr//span[normalize-space()='Edit']"
                ).click()
                found = True
                break
            except:
                next_btn = driver.find_element(By.XPATH, "//button[contains(@class,'p-paginator-next')]")
                if "p-disabled" in next_btn.get_attribute("class"):
                    break
                next_btn.click()
                time.sleep(1)
                page += 1

        assert found, f"Store '{store_name}' not found in any page"

        time.sleep(2)
        switch_input = driver.find_element(
            By.XPATH,
            "//p-inputswitch[@id='typeStatus_ORD_storeCre']//input[@role='switch']"
        )

        is_enabled = switch_input.get_attribute("aria-checked")
        print("Invoice Type Switch Status (before):", is_enabled)

        if is_enabled == "false":
            print("Invoice type is disabled. Enabling it now...")
            driver.find_element(
                By.XPATH,
                "//p-inputswitch[@id='typeStatus_ORD_storeCre']//span[contains(@class,'p-inputswitch-slider')]"
            ).click()

            WebDriverWait(driver, 10).until(
                lambda d: switch_input.get_attribute("aria-checked") == "true"
            )
        else:
            print("Invoice type already enabled. No action needed.")

        time.sleep(2)
        # wait_and_locate_click(driver, By.XPATH, "//p-inputswitch[@id='typeStatus_ORD_storeCre']")
        wait_and_locate_click(driver, By.XPATH, "//p-multiselect[@id='invTypes_ORD_CrtItemPop']")

        wait_and_locate_click(driver, By.XPATH, f"//span[normalize-space()='{invoice_type_name_global}']")
        print("Selected invoice type:", invoice_type_name_global)

        time.sleep(2)
        wait_and_locate_click(
            driver,
            By.XPATH,
            "//button[contains(@class,'p-multiselect-close')]"
        )

        wait_and_locate_click(driver, By.XPATH, "//button[@id='create_ORD_storeCre']")
        print("Snack Bar Message:", get_snack_bar_message(driver))

        time.sleep(3)
    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name="Failure Screenshot", attachment_type=AttachmentType.PNG)
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Edit the Invoice Type")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_invoice_type_3(login):

    try:
        driver = login
        wait = WebDriverWait(driver, 30)

        wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        )).click()

        time.sleep(1)
        element = driver.find_element(By.XPATH, "(//span[normalize-space()='B&B Stores'])[1]")
        scroll_to_element(driver, element)

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[3]")

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnEdit_ORD_InvTypes'])[1]")
        
        time.sleep(1)
        prefix_edit = "p" + str(uuid.uuid4()).replace("-", "")[:3]

        prefix_text = driver.find_element(By.XPATH, "//input[@id='typePrefix_ORD_InvTypeCre']")
        prefix_text.clear()
        time.sleep(1)
        prefix_text.send_keys(prefix_edit)

        wait_and_locate_click(driver, By.XPATH, "//button[@id='btnSave_ORD_InvTypeCre']")

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        wait_and_locate_click(driver, By.XPATH, "(//img)[2]")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[5]")

        time.sleep(2)
        store_name = "B&B Stores"
        page = 1
        found = False

        while True:
            print(f"Searching for store '{store_name}' on page {page}")
            try:
                driver.find_element(
                    By.XPATH,
                    f"//div[normalize-space()='{store_name}']/ancestor::tr//span[normalize-space()='Edit']"
                ).click()
                found = True
                break
            except:
                next_btn = driver.find_element(By.XPATH, "//button[contains(@class,'p-paginator-next')]")
                if "p-disabled" in next_btn.get_attribute("class"):
                    break
                next_btn.click()
                time.sleep(1)
                page += 1

        assert found, f"Store '{store_name}' not found in any page"
        time.sleep(2)
        
        
        
        
        
        # wait until table is visible
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//table[contains(@class,'p-datatable-table')]//tbody/tr")
        ))

        # get the prefix from first row (2nd column)
        table_prefix = driver.find_element(
            By.XPATH,
            "(//table[contains(@class,'p-datatable-table')]//tbody/tr[1]/td[2])"
        ).text.strip()

        print("Edited Prefix in Table :", table_prefix)
        print("Expected Prefix        :", prefix_edit)

        assert table_prefix == prefix_edit, (
            f"Prefix mismatch! Expected: {prefix_edit}, Found: {table_prefix}"
        )
        time.sleep(3)
    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name="Failure Screenshot", attachment_type=AttachmentType.PNG)
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Disable the status of the Invoice Type.")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_invoice_type_4(login):

    try:
        driver = login
        wait = WebDriverWait(driver, 30)

        wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        )).click()

        time.sleep(1)
        element = driver.find_element(By.XPATH, "(//span[normalize-space()='B&B Stores'])[1]")
        scroll_to_element(driver, element)

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[3]")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "(//button[@type='button'])[2]")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//p-inputswitch[@id='status_ORD_InvTypeCre']")



    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name="Failure Screenshot", attachment_type=AttachmentType.PNG)
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Create an Order and Generate an Invoice by Applying an Invoice Type")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_invoice_type_5(login):

    try:
        driver = login
        wait = WebDriverWait(driver, 30)

        wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        )).click()

        time.sleep(1)
        element = driver.find_element(By.XPATH, "(//span[normalize-space()='B&B Stores'])[1]")
        scroll_to_element(driver, element)
        element.click()

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]")

        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//button[@id='btnCrtCs_ORD_CrtItemPop'])[1]")

        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        driver.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        driver.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        driver.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        driver.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()




        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "(//p-multiselect[@id='selectCat_ORD_CrtItemPop'])[1]")

        wait_and_locate_click(driver, By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")

        wait_and_locate_click(driver, By.XPATH, "//button[@id='btnSave_ORD_CrtItemPop']")

        time.sleep(3)

        wait_and_locate_click(login,By.XPATH, "(//p-autocomplete[@id='inputSearch_ORD_ItemSrch'])[1]")
        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Search items'])[1]", "item")
        
        time.sleep(3)
        element = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Item_1')])[1]")))
        click_to_element(login, element)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSltVal_ORD_Vitem'])[2]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"))
        ).click()

        

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnBrowse_ORD_CrtItem'])[1]")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='actionSltSts_ORD_ItemSelect-input'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//button[@id='btnSltDn_ORD_ItemSelect'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@id='actionSltBatch_ORD_CrtItem'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnConf_ORD_CrtItem'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(2)
        
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnCrtInv_ORD_CrtItem'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnViewInv_ORD_CrtItem'])[1]")



        time.sleep(3)
    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name="Failure Screenshot", attachment_type=AttachmentType.PNG)
        raise e