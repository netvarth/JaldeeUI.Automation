
from Framework.common_utils import *
from Framework.consumer_common_utils import *

driver = login

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating a walk-in sales order and invoice, and Share payment link")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_1(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login
        
        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
    
        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"))
        ).click()
        
        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnCrtCs_ORD_CrtItemPop'])[1]"))
        ).click()

        
        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(3)

        Drop_element = driver.find_element(By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']")                          
        time.sleep(1)
        Drop_element.click()

        time.sleep(2)
        # wait_and_locate_click(driver, By.XPATH, "(//p-multiselect[@id='selectCat_ORD_CrtItemPop'])[1]")
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        driver.execute_script("arguments[0].click();", select_element)

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

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
                (By.XPATH, "(//input[@id='actionSltSts_ORD_ItemSelect-input'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//button[@id='btnSltDn_ORD_ItemSelect'])[1]")
 
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnConf_ORD_CrtItem'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnCrtInv_ORD_CrtItem'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnViewInv_ORD_CrtItem'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//p-dropdown[@placeholder='Get Payment'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Share Payment Link'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnSend_ORD_PayBill'])[1]")

        message = get_snack_bar_message(login)
        print("Snack bar message:", message)

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnOdCng_ORD_CrtItem'])[1]")

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[2]")

        time.sleep(2)
       # Wait for rows properly (avoid time.sleep)
        rows = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//tbody/tr")
            )
        )

        first_row = rows[0]

        # Consumer name (td[2])
        first_row_consumer = first_row.find_element(
            By.XPATH, "./td[2]//span[contains(@class,'text-capitalize')]"
        ).text.strip()

        # Status (td[5])
        first_row_status = first_row.find_element(
            By.XPATH, "./td[7]//span"
        ).text.strip()

        print(f"First row -> Consumer: {first_row_consumer}, Status: {first_row_status}")

        # Assertions
        assert first_row_consumer == consumer_name, f"Expected consumer {consumer_name}, but found {first_row_consumer}"
        assert first_row_status == "Completed", f"Expected status Completed, but found {first_row_status}"

        time.sleep(5)
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e    


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating a walk-in sales order and invoice, and pay now.")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_2(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
    
        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"))
        ).click()
        
        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnCrtCs_ORD_CrtItemPop'])[1]"))
        ).click()

        
        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(3)

        Drop_element = driver.find_element(By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']")                          
        time.sleep(1)
        Drop_element.click()
    
        time.sleep(2)
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        login.execute_script("arguments[0].click();", select_element)

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

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
                (By.XPATH, "(//input[@id='actionSltSts_ORD_ItemSelect-input'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"))
        ).click()
       
        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//i[@class='pi pi-check'])[1]")

        

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnConf_ORD_CrtItem'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnCrtInv_ORD_CrtItem'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnViewInv_ORD_CrtItem'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//p-dropdown[@placeholder='Get Payment'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Pay by Cash'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnMkPay_ORD_PayBill'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnSltYes_ORD_ConfPay'])[1]")

        message = get_snack_bar_message(login)
        print("Snack bar message:", message)

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnOdCng_ORD_CrtItem'])[1]")

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[2]")

        time.sleep(2)
       # Wait for rows properly (avoid time.sleep)
        rows = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//tbody/tr")
            )
        )

        first_row = rows[0]

        # Consumer name (td[2])
        first_row_consumer = first_row.find_element(
            By.XPATH, "./td[2]//span[contains(@class,'text-capitalize')]"
        ).text.strip()

        # Status (td[5])
        first_row_status = first_row.find_element(
            By.XPATH, "./td[7]//span"
        ).text.strip()

        print(f"First row -> Consumer: {first_row_consumer}, Status: {first_row_status}")

        # Assertions
        assert first_row_consumer == consumer_name, f"Expected consumer {consumer_name}, but found {first_row_consumer}"
        assert first_row_status == "Completed", f"Expected status Completed, but found {first_row_status}"

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating a walk-in sales order and invoice, and Settle Invoice.")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_3(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login

        
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
    
        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"))
        ).click()
        
        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnCrtCs_ORD_CrtItemPop'])[1]"))
        ).click()

        
        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        time.sleep(1)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(3)

        Drop_element = driver.find_element(By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']")                          
        time.sleep(1)
        Drop_element.click()
    
        time.sleep(2)
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        login.execute_script("arguments[0].click();", select_element)

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

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

        

        # time.sleep(3)
        # wait_and_locate_click(login, By.XPATH, "(//button[@id='btnBrowse_ORD_CrtItem'])[1]")

        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//input[@type='checkbox' and contains(@class,'mdc-checkbox__native-control')])[2]"))
        # ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[span[normalize-space()='Select Item']]"))
        # ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//i[@class='pi pi-check'])[2]"))
        # ).click()

        # time.sleep(2)
        # wait_and_locate_click(login, By.XPATH, "(//i[@class='fa fa-caret-down'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnConf_ORD_CrtItem'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnCrtInv_ORD_CrtItem'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnViewInv_ORD_CrtItem'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Settle Invoice'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Confirm & Settle Invoice'])[1]")


        message = get_snack_bar_message(login)
        print("Snack bar message:", message)

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnOdCng_ORD_CrtItem'])[1]")

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[2]")

        time.sleep(2)
       # Wait for rows properly (avoid time.sleep)
        rows = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//tbody/tr")
            )
        )

        first_row = rows[0]

        # Consumer name (td[2])
        first_row_consumer = first_row.find_element(
            By.XPATH, "./td[2]//span[contains(@class,'text-capitalize')]"
        ).text.strip()

        # Status (td[5])
        first_row_status = first_row.find_element(
            By.XPATH, "./td[7]//span"
        ).text.strip()

        print(f"First row -> Consumer: {first_row_consumer}, Status: {first_row_status}")

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating a walk-in sales order and invoice, and cancel Invoice.")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_4(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login

        
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
    
        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"))
        ).click()
        
        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnCrtCs_ORD_CrtItemPop'])[1]"))
        ).click()

        
        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(3)

        Drop_element = driver.find_element(By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']")                          
        time.sleep(1)
        Drop_element.click()
    
        time.sleep(2)
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        login.execute_script("arguments[0].click();", select_element)

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

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
                (By.XPATH, "(//input[@id='actionSltSts_ORD_ItemSelect-input'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-check'])[2]"))
        ).click()

        

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnConf_ORD_CrtItem'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnCrtInv_ORD_CrtItem'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnViewInv_ORD_CrtItem'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Cancel Invoice'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnCancelInv_ORD_SetInv'])[1]")

        message = get_snack_bar_message(login)
        print("Snack bar message:", message)

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnOdCng_ORD_CrtItem'])[1]")

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[2]")

        time.sleep(2)
       # Wait for rows properly (avoid time.sleep)
        rows = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//tbody/tr")
            )
        )

        first_row = rows[0]

        # Consumer name (td[2])
        first_row_consumer = first_row.find_element(
            By.XPATH, "./td[2]//span[contains(@class,'text-capitalize')]"
        ).text.strip()

        # Status (td[5])
        first_row_status = first_row.find_element(
            By.XPATH, "./td[7]//span"
        ).text.strip()

        print(f"First row -> Consumer: {first_row_consumer}, Status: {first_row_status}")

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating a walk-in sales order and create a new label complete the order")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_5(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login
        
        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
    
        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"))
        ).click()
        
        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnCrtCs_ORD_CrtItemPop'])[1]"))
        ).click()

        
        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(3)

        Drop_element = driver.find_element(By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']")                          
        time.sleep(1)
        Drop_element.click()
    
        time.sleep(2)
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        login.execute_script("arguments[0].click();", select_element)

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

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
                (By.XPATH, "(//input[@id='actionSltSts_ORD_ItemSelect-input'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//button[@id='btnSltDn_ORD_ItemSelect'])[1]")

        

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnConf_ORD_CrtItem'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        # time.sleep(3)
        # wait_and_locate_click(
        #     driver, By.XPATH, "//button[@id='btnEdt_ORD_CrtItem']"
        # )

        # time.sleep(2)
        # wait_and_locate_click(
        #     driver, By.XPATH, "(//button[normalize-space()='Yes'])[1]"
        # )

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//button[normalize-space()='Add Label'])[1]"
        )

        label_name = "Label_" + str(uuid.uuid4())[:4]
        print("Label Name", label_name)

        wait_and_locate_click(
            login, By.XPATH, "//span[normalize-space()='Add New']"
        )

        wait_and_send_keys(
            login, By.XPATH, "//input[@id='displayName']", label_name
        )

        wait_and_locate_click(
            login, By.XPATH, "//span[@class='mdc-button__label']"
        )

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//input[@type='checkbox'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            login, By.XPATH, "//span[normalize-space()='Done']"
        )

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)
        time.sleep(3)

        create_element = login.find_element(By.XPATH, "//button[@id='btnOdCng_ORD_CrtItem']")
        scroll_to_element(login, create_element)
        time.sleep(2)
        create_element.click()
        
        time.sleep(3)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e 


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating a walk-in sales order with Label ")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_6(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login
        
        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
    
        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"))
        ).click()
        
        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnCrtCs_ORD_CrtItemPop'])[1]"))
        ).click()

        
        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(3)

        Drop_element = driver.find_element(By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']")                          
        time.sleep(1)
        Drop_element.click()
    
        time.sleep(2)
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        login.execute_script("arguments[0].click();", select_element)

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

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
                (By.XPATH, "(//input[@id='actionSltSts_ORD_ItemSelect-input'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//button[@id='btnSltDn_ORD_ItemSelect'])[1]")

        

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnConf_ORD_CrtItem'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        wait_and_locate_click(
            login, By.XPATH, "(//button[normalize-space()='Add Label'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            login, By.XPATH, "(//input[@type='checkbox'])[2]"
        )

        time.sleep(1)
        wait_and_locate_click(
            login, By.XPATH, "//span[normalize-space()='Done']"
        )

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)
        time.sleep(3)

        create_element = login.find_element(By.XPATH, "//button[@id='btnOdCng_ORD_CrtItem']")
        scroll_to_element(login, create_element)
        time.sleep(2)
        create_element.click()
        
        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)


    
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Remove the Label from the order")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_7(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
    
        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[2]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"
        )

        time.sleep(1)
        element_store = login.find_element(By.XPATH, "//span[normalize-space()='B&B Stores']")

        scroll_to_element(login, element_store)
        time.sleep(1)
        element_store.click()

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//button[@id='btnViewOrdr_ORD_OrdsList'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "//i[@class='pi pi-times remove-label']"
        )

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(3)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Assign user to the order")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_8(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login
        
        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
    
        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"))
        ).click()
        
        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnCrtCs_ORD_CrtItemPop'])[1]"))
        ).click()

        
        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(3)

        Drop_element = driver.find_element(By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']")                          
        time.sleep(1)
        Drop_element.click()            
    
        time.sleep(2)
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        login.execute_script("arguments[0].click();", select_element)


        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

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
                (By.XPATH, "(//input[@id='actionSltSts_ORD_ItemSelect-input'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//button[@id='btnSltDn_ORD_ItemSelect'])[1]")

        

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnConf_ORD_CrtItem'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        wait_and_locate_click(
            login, By.XPATH, "(//button[normalize-space()='Add Label'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            login, By.XPATH, "(//input[@type='checkbox'])[2]"
        )

        time.sleep(1)
        wait_and_locate_click(
            login, By.XPATH, "//span[normalize-space()='Done']"
        )

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)
        time.sleep(3)

        wait_and_locate_click(
            login, By.XPATH, "(//i[@class='fa fa-user-plus'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "//div[@role='button']"
        )

        wait_and_locate_click(
            login, By.XPATH, "//button[@id='btnAssignUser_FIN_finAction']"
        )

        msg = get_snack_bar_message(login)
        print("Snac Bar Message: ", msg)
        time.sleep(2)
        

        create_element = login.find_element(By.XPATH, "//button[@id='btnOdCng_ORD_CrtItem']")
        scroll_to_element(login, create_element)
        time.sleep(2)
        create_element.click()
        
        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)


    
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Remove the Label from the order")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_9(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
    
        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[2]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"
        )

        time.sleep(1)
        element_store = login.find_element(By.XPATH, "//span[normalize-space()='B&B Stores']")

        scroll_to_element(login, element_store)
        time.sleep(1)
        element_store.click()

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//button[@id='btnViewOrdr_ORD_OrdsList'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//i[@class='fa fa-times'])[1]"
        )

        wait_and_locate_click(
            login, By.XPATH, "(//button[normalize-space()='Unassign'])[1]"
        )

        time.sleep(3)

        

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create invoice for a walk-in order assert user")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_10(login):
    try:
        time.sleep(3)
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(2)


        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()


        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"))
        ).click()
        
        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnCrtCs_ORD_CrtItemPop'])[1]"))
        ).click()

        
        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(3)

        Drop_element = driver.find_element(By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']")                          
        time.sleep(1)
        Drop_element.click()
    
        time.sleep(2)
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        login.execute_script("arguments[0].click();", select_element)

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

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
                (By.XPATH, "(//input[@id='actionSltSts_ORD_ItemSelect-input'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//button[@id='btnSltDn_ORD_ItemSelect'])[1]")

        

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnConf_ORD_CrtItem'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnCrtInv_ORD_CrtItem'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnViewInv_ORD_CrtItem'])[1]")

        time.sleep(2)
        created_by_element = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'fw-bold') and contains(.,'Created By')]")
            )
        )

        actual_text = created_by_element.text.strip()
        print("Actual:", actual_text)

        assert "Vijay Kumar" in actual_text




    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create Order without customer")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_11(login):
    try:
        time.sleep(3)
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(2)


        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//img[@src='./assets/images/menu/settings.png']"
        )


        time.sleep(2)
        pos_option_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_option_element)


        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//a[.//p[normalize-space()='Draft Order Creation With customer']]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//*[name()='svg'][@class='mdc-switch__icon mdc-switch__icon--off'])[1]"
        )

        msg = get_snack_bar_message(driver)
        print("Snack Bar Message :", msg)
        time.sleep(3)


        wait_and_locate_click(
                    driver, By.XPATH, "(//img)[2]"
                )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"
        )

        time.sleep(1)
        Drop_element = driver.find_element(By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']")                          
        time.sleep(1)
        Drop_element.click()
    
        time.sleep(2)
        element = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Item_1')])[1]")))
        click_to_element(login, element)

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

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
                (By.XPATH, "(//input[@id='actionSltSts_ORD_ItemSelect-input'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//button[@id='btnSltDn_ORD_ItemSelect'])[1]")

        

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnConf_ORD_CrtItem'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "(//img[@src='./assets/images/menu/settings.png'])[1]"
        )

        time.sleep(2)
        pos_option_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_option_element)


        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//a[.//p[normalize-space()='Draft Order Creation With customer']]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//*[name()='svg'][@class='mdc-switch__icon mdc-switch__icon--off'])[1]"
        )

        msg = get_snack_bar_message(driver)
        print("Snack Bar Message :", msg)
        time.sleep(3)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Sales price shows box price instead of item price after editing purchase price")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_12(login):
    try:
        time.sleep(3)
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(2)


        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//img)[3]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionNav_ORD_Inventory'])[5]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnMenu_ORD_PurchsList'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnEdts_ORD_PurchsList'])[1]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "(//p-dropdown[@id='selectCat_ORD_EdtPurchs'])[1]"
        )

        time.sleep(1)
        catalog_element = driver.find_element(By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Sale_catalog'])[1]")
        scroll_to_element(driver, catalog_element)
        time.sleep(2)
        catalog_element.click()

        price = random.randint(20000, 21000)
        print(price)

        time.sleep(1)
        sell_price_element = driver.find_element(By.XPATH, "(//input[@type='number'])[1]")
        sell_price_element.click()
        time.sleep(1)
        sell_price_element.clear()
        sell_price_element.send_keys(price)



        time.sleep(1)

        # wait_and_locate_click(
        #     driver, By.XPATH, "(//p-dropdown[@id='selectCat_ORD_EdtPurchs'])[2]"
        # )
        
        # time.sleep(1)
        # catalog_element = driver.find_element(By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Sale_catalog'])[1]")
        # scroll_to_element(driver, catalog_element)
        # time.sleep(2)
        # catalog_element.click()

        # time.sleep(1)
        # sell_price_element = driver.find_element(By.XPATH, "(//input[@type='number'])[2]")
        # sell_price_element.click()
        # time.sleep(1)
        # sell_price_element.clear()
        # sell_price_element.send_keys(price)

        # time.sleep(1)

        # wait_and_locate_click(
        #     driver, By.XPATH, "(//p-dropdown[@id='selectCat_ORD_EdtPurchs'])[3]"
        # )
        
        # time.sleep(1)
        # catalog_element = driver.find_element(By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Sale_catalog'])[1]")
        # scroll_to_element(driver, catalog_element)
        # time.sleep(2)
        # catalog_element.click()

        # time.sleep(1)
        # sell_price_element = driver.find_element(By.XPATH, "(//input[@type='number'])[3]")
        # sell_price_element.click()
        # time.sleep(1)
        # sell_price_element.clear()
        # sell_price_element.send_keys(price)


        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnSave_ORD_EdtPurchs']"
        )

        msg =  get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "(//img)[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[4]"
        )

        catalog_name = "Sale_catalog"

        while True:
            # Use find_elements instead of find_element
            rows = driver.find_elements(
                By.XPATH,
                f"//tr[.//div[contains(@class,'fw-bold') and normalize-space(.)='{catalog_name}']]"
            )

            if rows:
                action_btn = rows[0].find_element(
                    By.XPATH, ".//button[@id='btnActMenu_ORD_OrdCat']"
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", action_btn)
                wait.until(EC.element_to_be_clickable(action_btn))
                action_btn.click()
                print("Catalog found and action clicked")
                break

            # If not found → go to next page
            next_btn = driver.find_element(
                By.XPATH, "//button[contains(@class,'p-paginator-next')]"
            )

            if "p-disabled" in next_btn.get_attribute("class"):
                raise Exception("Catalog not found in any page")

            next_btn.click()

            # Wait for table to refresh
            wait.until(EC.presence_of_element_located(
                (By.XPATH, "//tbody[contains(@class,'p-datatable-tbody')]")
            ))

        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnViewCata_ORD_OrdCat'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnEdtVItem_ORD_CatDet'])[1]"
        )

        # Calculate expected actual price
        expected_price = round(price / 100, 2)
        print("Expected Actual Price:", expected_price)

        # Wait for table rows
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//tbody[contains(@class,'p-datatable-tbody')]//tr")
        ))

        # Get all Sales Price input fields
        price_inputs = driver.find_elements(
            By.XPATH,
            "//input[@id='inputPrice_ORD_AttrbtSltn']"
        )

        for index, input_field in enumerate(price_inputs, start=1):

            # Get value from input
            actual_value = input_field.get_attribute("value")

            if actual_value == "":
                raise Exception(f"Row {index} price is empty")

            actual_value = float(actual_value)

            print(f"Row {index} UI Price:", actual_value)

            assert actual_value == expected_price, \
                f"Price mismatch in row {index}. Expected: {expected_price}, Got: {actual_value}"

        print("✅ All catalog item selling prices are correct")



    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Add Item from Wishlist to Cart after adding it to Wishlist.")
@pytest.mark.parametrize("url", [sales_order_consumer_scale_url])
def test_create_sales_order_13(consumer_login):
   
   
    try:
        time.sleep(3)
        wait = WebDriverWait(consumer_login, 30)
        driver = consumer_login
        time.sleep(2)


        item_element = driver.find_element(By.XPATH, "//h2[normalize-space()='Categories']")
        scroll_to_element(driver, item_element)
        time.sleep(2)
        
        wait_and_locate_click(
            driver, By.XPATH, "//div[contains(text(),'Item_1')]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//h3[normalize-space()='Item_1'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnAddToCart'])[1]"
        )

        time.sleep(2)
        wait_and_send_keys(
            driver, By.XPATH, "(//input[@placeholder='81234 56789'])[1]", "9207206005"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//input[@type='checkbox'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnSendOTP']"
        )

        time.sleep(2)

        otp_digits = "5555"
        # otp_digits = "55555"
        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )

        # print("Number of OTP input fields:", len(otp_inputs))
        # print(otp_inputs)

        for i, otp_input in enumerate(otp_inputs):

            # print(i)
            # print(otp_input)
            otp_input.send_keys(otp_digits[i])

        consumer_login.find_element(By.XPATH, "//button[@id='btnVerifyOTP']").click()

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        
        time.sleep(3)
        element_item = driver.find_element(By.XPATH, "//div[normalize-space()='Item_2']")
        scroll_to_element(driver, element_item)
        time.sleep(2)
        element_item.click()

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[normalize-space()='Add to Wishlist']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "(//i[@class='fa fa-heart-o wishlist-icon'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//h3[normalize-space()='Item_2 Black']"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnAddToCart']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//img[@class='ms-1'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCheckout']"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnPrimaryAction']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//div[contains(text(),'Net Banking')])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnPrimaryAction']"
        )

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnPrimaryAction']"
        )

        time.sleep(3)
        # Store main window
        main_window = driver.current_window_handle

        # Wait for Razorpay iframe and switch
        wait.until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe.razorpay-checkout-frame")
            )
        )

        print("Switched to Razorpay iframe")

        # Click Netbanking option
        netbanking = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@data-testid='netbanking']")
            )
        )
        netbanking.click()

        print("Netbanking selected")

        # Select bank (Example: State Bank of India)
        bank = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'Kotak Mahindra Bank')]")
            )
        )
        bank.click()

        print("Bank selected")

        # Exit iframe
        driver.switch_to.default_content()

        time.sleep(2)
       # Store main window
        main_window = driver.current_window_handle

        print("Main window:", main_window)

        # Wait for Razorpay simulator window
        wait.until(lambda d: len(d.window_handles) > 1)

        # Switch to Razorpay window
        for window in driver.window_handles:
            driver.switch_to.window(window)
            if "mocksharp/payment" in driver.current_url:
                print("Switched to Razorpay simulator:", driver.current_url)
                break

        # Wait for Success button
        success_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-val='S']"))
        )

        # Click success
        driver.execute_script("arguments[0].click();", success_btn)

        print("Success button clicked")

        # Switch back to main window
        driver.switch_to.window(main_window)

        print("Returned to main window")


        driver.implicitly_wait(30)
        element_invoice = driver.find_element(By.XPATH, "//button[@id='btnInvoice']")
        scroll_to_element(driver, element_invoice)
        time.sleep(1)
        element_invoice.click()


        time.sleep(3)
    except Exception as e:
        allure.attach(
            consumer_login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify that the Add Shipment button is not displayed when Shipment is turned OFF in the account settings.")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_14(login):
    try:
        time.sleep(3)
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(2)


        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
        
        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//img[@src='./assets/images/menu/settings.png'])[1]"
        )

        pos_order_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_order_element)
        
        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//a[.//span[contains(text(),'Shipments')]]"
        )

        time.sleep(2)

        toggle = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']"))
        )

        state = toggle.get_attribute("aria-checked")

        if state == "true":
            print("Toggle is enabled. Disabling it...")
            toggle.click()
        else:
            print("Toggle already disabled. No action needed.")

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//img)[2]"
        )

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"))
        ).click()
        
        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnCrtCs_ORD_CrtItemPop'])[1]"))
        ).click()

        
        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(3)

        Drop_element = driver.find_element(By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']")                          
        time.sleep(1)
        Drop_element.click()
    
        time.sleep(2)
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        login.execute_script("arguments[0].click();", select_element)

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

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
                (By.XPATH, "(//input[@id='actionSltSts_ORD_ItemSelect-input'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//button[@id='btnSltDn_ORD_ItemSelect'])[1]")

        

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnConf_ORD_CrtItem'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnOdCng_ORD_CrtItem']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        add_shipment_btn = driver.find_elements(
            By.XPATH, "//button[.//span[normalize-space()='Add Shipment']]"
        )

        if len(add_shipment_btn) > 0 and add_shipment_btn[0].is_displayed():
            print("Add Shipment button is visible")
        else:
            print("Add Shipment button is NOT visible")

        time.sleep(3)
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify items remain in order when returning from Create Consumer page without creating a consumer")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_15(login):
    try:
        time.sleep(3)
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(2)


        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
        
        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//img[@src='./assets/images/menu/settings.png'])[1]"
        )

        pos_order_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_order_element)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//a[.//span[contains(text(),'Draft Order With customer')]]"
        )

        time.sleep(2)

        toggle = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']"))
        )

        state = toggle.get_attribute("aria-checked")

        if state == "true":
            print("Toggle is enabled. Disabling it...")
            toggle.click()
        else:
            print("Toggle already disabled. No action needed.")

        msg = get_snack_bar_message(driver)
        print("Snack Bar message :", msg)
        time.sleep(2)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//img)[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"
        )

        time.sleep(1)
        Drop_element = driver.find_element(By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']")                          
        time.sleep(1)
        Drop_element.click()
    
        time.sleep(2)
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        login.execute_script("arguments[0].click();", select_element)

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

        time.sleep(3)
                                                            
        # wait_and_locate_click(login,By.XPATH, "(//p-autocomplete[@id='inputSearch_ORD_ItemSrch'])[1]")
        # time.sleep(1)
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
                (By.XPATH, "(//input[@id='actionSltSts_ORD_ItemSelect-input'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//button[@id='btnSltDn_ORD_ItemSelect'])[1]")

        

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//span[@class='p-button-icon pi pi-plus'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//span[@class='fa fa-arrow-left pointer-cursor'])[1]"
        )

        with allure.step("Verify added item remains in order after returning from Create Consumer page"):
            items = driver.find_elements(By.XPATH, "//div[normalize-space()='Item_1']")

        if not items:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="item_not_present",
                attachment_type=AttachmentType.PNG,
            )

        assert len(items) > 0 and items[0].is_displayed(), \
            "Added item is not present in the order after returning from Create Consumer page"



        time.sleep(3)
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify items remain when consumer is removed")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_16(login):
    try:
        time.sleep(3)
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(2)


        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
        
        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//img[@src='./assets/images/menu/settings.png'])[1]"
        )

        pos_order_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_order_element)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//a[.//span[contains(text(),'Draft Order With customer')]]"
        )

        time.sleep(2)

        toggle = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']"))
        )

        state = toggle.get_attribute("aria-checked")

        if state == "true":
            print("Toggle is enabled. Disabling it...")
            toggle.click()
        else:
            print("Toggle already disabled. No action needed.")

        msg = get_snack_bar_message(driver)
        print("Snack Bar message :", msg)
        time.sleep(2)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//img)[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"
        )

        time.sleep(1)
        Drop_element = driver.find_element(By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']")                          
        time.sleep(1)
        Drop_element.click()
    
        time.sleep(2)
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        login.execute_script("arguments[0].click();", select_element)

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

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
                (By.XPATH, "(//input[@id='actionSltSts_ORD_ItemSelect-input'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//button[@id='btnSltDn_ORD_ItemSelect'])[1]")

        

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//span[@class='p-button-icon pi pi-plus'])[1]"
        )

        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()
        time.sleep(2)
        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(3)

        with allure.step("Verify added item remains in order after returning from Create Consumer page"):
            items = driver.find_elements(By.XPATH, "//div[normalize-space()='Item_1']")

        if not items:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="item_not_present",
                attachment_type=AttachmentType.PNG,
            )

        assert len(items) > 0 and items[0].is_displayed(), \
            "Added item is not present in the order after returning from Create Consumer page"
        
        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//img[@src='./assets/images/menu/settings.png'])[1]"
        )

        time.sleep(2)
        pos_order_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_order_element)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//a[.//span[contains(text(),'Draft Order With customer')]]"
        )

        time.sleep(2)

        toggle = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']"))
        )

        state = toggle.get_attribute("aria-checked")

        if state == "false":
            print("Toggle is disabled. Enabling it...")
            toggle.click()
        else:
            print("Toggle already enabled. No action needed.")

        msg = get_snack_bar_message(driver)
        print("Snack Bar message :", msg)
        time.sleep(2)


    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify items remain when a consumer is created and redirected back")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_17(login):
    try:
        time.sleep(3)
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(2)


        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
        
        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//img[@src='./assets/images/menu/settings.png'])[1]"
        )

        pos_order_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_order_element)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//a[.//span[contains(text(),'Draft Order With customer')]]"
        )

        time.sleep(2)

        toggle = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']"))
        )

        state = toggle.get_attribute("aria-checked")

        if state == "true":
            print("Toggle is enabled. Disabling it...")
            toggle.click()
        else:
            print("Toggle already disabled. No action needed.")

        msg = get_snack_bar_message(driver)
        print("Snack Bar message :", msg)
        time.sleep(2)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//img)[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"
        )

        time.sleep(1)
        Drop_element = driver.find_element(By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']")                          
        time.sleep(1)
        Drop_element.click()
    
        time.sleep(2)
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        login.execute_script("arguments[0].click();", select_element)

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

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
                (By.XPATH, "(//input[@id='actionSltSts_ORD_ItemSelect-input'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//button[@id='btnSltDn_ORD_ItemSelect'])[1]")

        

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//span[@class='p-button-icon pi pi-plus'])[1]"
        )

        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()

        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        msg = get_snack_bar_message(driver)
        print("Snack Bar Message:", msg)
        time.sleep(5)

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnRmvCs_ORD_CrtItem']"
        )

        with allure.step("Verify item remains in order after removing consumer"):
            items = driver.find_elements(By.XPATH, "//div[normalize-space()='Item_1']")

            if not items:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="item_missing_after_consumer_removal",
                    attachment_type=allure.attachment_type.PNG,
                )

            assert len(items) > 0 and items[0].is_displayed(), \
                "Item_1 is not present after removing the consumer"


        time.sleep(3)
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Editing an order to add a new item and then performing “Add Label” or “Assign User” should not remove the newly added item from the page.")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_18(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login

        
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//img[@src='./assets/images/menu/settings.png'])[1]"
        )

        pos_order_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_order_element)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//a[.//span[contains(text(),'Draft Order With customer')]]"
        )

        time.sleep(2)

        toggle = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']"))
        )

        state = toggle.get_attribute("aria-checked")

        if state == "false":
            print("Toggle is disabled. Enabling it...")
            toggle.click()
        else:
            print("Toggle already enabled. No action needed.")

        msg = get_snack_bar_message(driver)
        print("Snack Bar message :", msg)

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "(//img)[2]"
        )

    
        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"))
        ).click()
        
        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnCrtCs_ORD_CrtItemPop'])[1]"))
        ).click()

        
        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(3)

        drop_element = driver.find_element(By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        driver.execute_script("arguments[0].click();", drop_element)
        time.sleep(2)
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        login.execute_script("arguments[0].click();", select_element)

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"
        )

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
                (By.XPATH, "(//input[@id='actionSltSts_ORD_ItemSelect-input'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-check'])[2]"))
        ).click()

        

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnConf_ORD_CrtItem'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)
        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnEdt_ORD_CrtItem']"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[normalize-space()='Yes']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnBrowse_ORD_CrtItem']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//input[@type='checkbox'])[2]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnSltDn_ORD_ItemSelect'])[1]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='selectBatch_ORD_CrtItem']"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//li[@id='p-highlighted-option']//span[@class='ng-star-inserted'][normalize-space()='278']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[normalize-space()='Add Label'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//input[@type='checkbox'])[1]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "(//span[normalize-space()='Done'])[1]"
        )

        msg = get_snack_bar_message(driver)
        print("Snack Bar Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "(//button[normalize-space()='Assign user'])[1]"
        )

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "(//div[@class='user-name'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnAssignUser_FIN_finAction']" 
        )

        msg = get_snack_bar_message(driver)
        print("Snack Bar Message :", msg)
        time.sleep(2)

        time.sleep(2)

        rows = driver.find_elements(By.XPATH, "//table//tbody//tr")

        item_names = []
        for row in rows:
            text = row.text
            item_names.append(text)

        print("Items in order table:", item_names)

        assert any("Item_1" in item for item in item_names), "Item_1 disappeared after label or user assignment"
        assert any("Item_2" in item for item in item_names), "Item_2 disappeared after label or user assignment"

        print("Validation Passed: Items are still present after assigning label and user.")
        time.sleep(3)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Draft Order Creation With customer OFF")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_19(login):
    try:
        time.sleep(3)
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(2)


        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//img[@src='./assets/images/menu/settings.png']"
        )


        time.sleep(2)
        pos_option_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_option_element)


        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//a[.//p[normalize-space()='Draft Order Creation With customer']]"
        )

        time.sleep(2)

        toggle = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']"))
        )

        is_checked = toggle.get_attribute("aria-checked")

        toggle_changed = False

        if is_checked == "true":
            toggle.click()
            toggle_changed = False
            print("Toggle was ON. Now turned OFF.")
        else:
            print("Toggle already OFF. No action taken.")

        # Check snackbar only if toggle changed
        if toggle_changed:
            msg = get_snack_bar_message(driver)
            print("Snack Bar Message :", msg)

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor text-capitalize']"
        )

        time.sleep(2)
        time.sleep(2)
        pos_option_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_option_element)

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//li//span[contains(text(),'Add to Cart With Login')]"
        )

        time.sleep(2)

        toggle = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']"))
        )

        is_checked = toggle.get_attribute("aria-checked")

        toggle_changed = False

        if is_checked == "true":
            toggle.click()
            toggle_changed = False
            print("Toggle was ON. Now turned OFF.")
        else:
            print("Toggle already OFF. No action taken.")

        # Check snackbar only if toggle changed
        if toggle_changed:
            msg = get_snack_bar_message(driver)
            print("Snack Bar Message :", msg)

        time.sleep(2)


    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Add Item from to Cart edit qty")
@pytest.mark.parametrize("url", [sales_order_consumer_scale_url])
def test_create_sales_order_20(consumer_login):
   
   
    try:
        time.sleep(3)
        wait = WebDriverWait(consumer_login, 30)
        driver = consumer_login
        time.sleep(2)


        item_element = driver.find_element(By.XPATH, "//h2[normalize-space()='Categories']")
        scroll_to_element(driver, item_element)
        time.sleep(2)
        
        wait_and_locate_click(
            driver, By.XPATH, "//div[contains(text(),'Item_1')]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//h3[normalize-space()='Item_2']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnAddToCart']"
        )

        time.sleep(2)
        item_element_1 = driver.find_element(By.XPATH, "//div[normalize-space()='Item_6']")
        scroll_to_element(driver, item_element_1)
        time.sleep(2)
        item_element_1.click()

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnAddToCart']"
        )

        time.sleep(3)
        item_element_2 = driver.find_element(By.XPATH, "//div[normalize-space()='Item_1']")
        scroll_to_element(driver, item_element_2)
        time.sleep(2)
        item_element_2.click()

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnAddToCart']"
        )

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//img[@alt='Logo']"
        )

        time.sleep(2)
        
        item_element_3 = driver.find_element(By.XPATH, "//div[contains(text(),'Item_1')]")
        scroll_to_element(driver, item_element_3)
        time.sleep(2)
        item_element_3.click()
        time.sleep(2)
    
        item_element_4 = driver.find_element(By.XPATH, "//button[contains(text(),'Next ›')]")
        scroll_to_element(driver, item_element_4)
        time.sleep(2)
        item_element_4.click()

        time.sleep(2)

        # Locate product card
        product = wait.until(EC.presence_of_element_located((
            By.XPATH, "//div[contains(@class,'product-card')][.//h3[text()='Item_8']]"
        )))

        # Hover over product
        actions = ActionChains(driver)
        actions.move_to_element(product).perform()

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//img[@alt='Change address'])[1]"
        )

        time.sleep(2)

        # Locate product card
        product = wait.until(EC.presence_of_element_located((
            By.XPATH, "//div[contains(@class,'product-card')][.//h3[text()='Item_5']]"
        )))

        # Hover over product
        actions = ActionChains(driver)
        actions.move_to_element(product).perform()

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "(//img[@alt='Change address'])[4]"
        )

        time.sleep(2)

        # Locate product card
        product = wait.until(EC.presence_of_element_located((
            By.XPATH, "//div[contains(@class,'product-card')][.//h3[text()='Item_4']]"
        )))

        # Hover over product
        actions = ActionChains(driver)
        actions.move_to_element(product).perform()

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "(//img[@alt='Change address'])[3]"
        )

        time.sleep(5)

        wait_and_locate_click(
            driver, By.XPATH, "(//img[@class='ms-1'])[1]"
        )

        time.sleep(2)
        cart_image = driver.find_element(By.XPATH, "(//img[@class='ms-1'])[1]")
        driver.execute_script("arguments[0].click();", cart_image)


        time.sleep(2)
        items_xpath = "//div[contains(@class,'cart-item-card')]"

        items_count = len(driver.find_elements(By.XPATH, items_xpath))

        for i in range(items_count):
            for _ in range(2):
                items = driver.find_elements(By.XPATH, items_xpath)
                item = items[i]

                plus_btn = item.find_element(By.XPATH, ".//button[normalize-space()='+']")

                # 🔹 Scroll into view (center is IMPORTANT)
                driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", plus_btn
                )

                time.sleep(0.5)

                # 🔹 Wait until clickable
                wait.until(EC.element_to_be_clickable(plus_btn))

                try:
                    plus_btn.click()
                except:
                    # 🔹 Fallback if intercepted
                    driver.execute_script("arguments[0].click();", plus_btn)

                time.sleep(0.5)


        time.sleep(2)
        element_placeorder = driver.find_element(By.XPATH, "//label[normalize-space()='NOTES']")
        scroll_to_element(driver, element_placeorder)
        time.sleep(2)
        
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCheckout']"
        )

        time.sleep(2)
        wait_and_send_keys(
            driver, By.XPATH, "(//input[@placeholder='81234 56789'])[1]", "9207206005"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//input[@type='checkbox'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnSendOTP']"
        )

        time.sleep(2)

        otp_digits = "5555"
        # otp_digits = "55555"
        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )

        # print("Number of OTP input fields:", len(otp_inputs))
        # print(otp_inputs)

        for i, otp_input in enumerate(otp_inputs):

            # print(i)
            # print(otp_input)
            otp_input.send_keys(otp_digits[i])

        consumer_login.find_element(By.XPATH, "//button[@id='btnVerifyOTP']").click()

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        








    except Exception as e:
        allure.attach(
            consumer_login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Draft Order Creation With customer ON")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_21(login):
    try:
        time.sleep(3)
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(2)


        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//img[@src='./assets/images/menu/settings.png']"
        )


        time.sleep(2)
        pos_option_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_option_element)


        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//a[.//p[normalize-space()='Draft Order Creation With customer']]"
        )

        time.sleep(2)

        toggle = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']"))
        )

        is_checked = toggle.get_attribute("aria-checked")

        toggle_changed = True

        if is_checked == "false":
            toggle.click()
            toggle_changed = True
            print("Toggle was OFF. Now turned ON.")
        else:
            print("Toggle already ON. No action taken.")

        # Check snackbar only if toggle changed
        if toggle_changed:
            msg = get_snack_bar_message(driver)
            print("Snack Bar Message :", msg)

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor text-capitalize']"
        )

        time.sleep(2)
        time.sleep(2)
        pos_option_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_option_element)

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//li//span[contains(text(),'Add to Cart With Login')]"
        )

        time.sleep(2)

        toggle = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']"))
        )

        is_checked = toggle.get_attribute("aria-checked")

        toggle_changed = True

        if is_checked == "false":
            toggle.click()
            toggle_changed = True
            print("Toggle was OFF. Now turned ON.")
        else:
            print("Toggle already ON. No action taken.")

        # Check snackbar only if toggle changed
        if toggle_changed:
            msg = get_snack_bar_message(driver)
            print("Snack Bar Message :", msg)

        time.sleep(2)
    
    except Exception as e:
        allure.attach(
            consumer_login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("")
@pytest.mark.parametrize("url", [sales_order_consumer_scale_url])
def test_create_sales_order_22(consumer_login):
   
   
    try:
        time.sleep(3)
        wait = WebDriverWait(consumer_login, 30)
        driver = consumer_login
        time.sleep(2)


        item_element = driver.find_element(By.XPATH, "//h2[normalize-space()='Categories']")
        scroll_to_element(driver, item_element)
        time.sleep(2)
        
        wait_and_locate_click(
            driver, By.XPATH, "//div[contains(text(),'Item_1')]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//h3[normalize-space()='Item_1'])[1]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[normalize-space()='+']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnAddToCart'])[1]"
        )


        time.sleep(2)
        wait_and_send_keys(
            driver, By.XPATH, "(//input[@placeholder='81234 56789'])[1]", "9207206005"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//input[@type='checkbox'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnSendOTP']"
        )

        time.sleep(2)

        otp_digits = "5555"
        # otp_digits = "55555"
        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )

        # print("Number of OTP input fields:", len(otp_inputs))
        # print(otp_inputs)

        for i, otp_input in enumerate(otp_inputs):

            # print(i)
            # print(otp_input)
            otp_input.send_keys(otp_digits[i])

        consumer_login.find_element(By.XPATH, "//button[@id='btnVerifyOTP']").click()

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        
        time.sleep(3)
    
        wait_and_locate_click(
            driver, By.XPATH, "(//img[@class='ms-1'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCheckout']"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnPrimaryAction']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//div[contains(text(),'Net Banking')])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnPrimaryAction']"
        )

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnPrimaryAction']"
        )

        time.sleep(3)
        # Store main window
        main_window = driver.current_window_handle

        # Wait for Razorpay iframe and switch
        wait.until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe.razorpay-checkout-frame")
            )
        )

        print("Switched to Razorpay iframe")

        # Click Netbanking option
        netbanking = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@data-testid='netbanking']")
            )
        )
        netbanking.click()

        print("Netbanking selected")

        # Select bank (Example: State Bank of India)
        bank = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'Kotak Mahindra Bank')]")
            )
        )
        bank.click()

        print("Bank selected")

        # Exit iframe
        driver.switch_to.default_content()

        time.sleep(2)
       # Store main window
        main_window = driver.current_window_handle

        print("Main window:", main_window)

        # Wait for Razorpay simulator window
        wait.until(lambda d: len(d.window_handles) > 1)

        # Switch to Razorpay window
        for window in driver.window_handles:
            driver.switch_to.window(window)
            if "mocksharp/payment" in driver.current_url:
                print("Switched to Razorpay simulator:", driver.current_url)
                break

        # Wait for Success button
        success_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-val='S']"))
        )

        # Click success
        driver.execute_script("arguments[0].click();", success_btn)

        print("Success button clicked")

        # Switch back to main window
        driver.switch_to.window(main_window)

        print("Returned to main window")


        driver.implicitly_wait(30)
        element_invoice = driver.find_element(By.XPATH, "//button[@id='btnInvoice']")
        scroll_to_element(driver, element_invoice)
        time.sleep(1)
        element_invoice.click()


        time.sleep(3)
    except Exception as e:
        allure.attach(
            consumer_login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Refund completed → Total Amount Due should be ₹0 (not negative)")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_23(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login
        
        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
    
        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[2]"))
        ).click()
        
        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id= 'btnViewOrdr_ORD_OrdsList'])[1]"
        )
        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnEdt_ORD_CrtItem']"
        )                       


        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//button[normalize-space()='Yes']")



        time.sleep(3)
        input_element = driver.find_element(By.XPATH, "(//input[@id= 'inputQty_ORD_CrtItem'])[1]")
        input_element.click()
        time.sleep(1)
        input_element.clear()
        time.sleep(1)
        input_element.send_keys("1")

        time.sleep(2)
        update_element = driver.find_element(By.XPATH, "//button[@id='btnUpdOrd_ORD_CrtItem']")
        scroll_to_element(driver, update_element)
        time.sleep(1)
        update_element.click()

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[normalize-space()='Yes']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        confirm_element = driver.find_element(By.XPATH, "//button[@id='btnOdConfirm_ORD_CrtItem']")
        scroll_to_element(driver, confirm_element)
        time.sleep(1)
        confirm_element.click()

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnViewInv_ORD_CrtItem']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[normalize-space()='Refund']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[normalize-space()='Refund'])[2]"
        )

        time.sleep(2)
        input_number = driver.find_element(By.XPATH, "//input[@id='example-number-input']")
        input_number.click()
        time.sleep(1)
        input_number.clear()
        time.sleep(1)
        input_number.send_keys("350")

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[normalize-space()='Pay Online']"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[normalize-space()='Yes']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//div[normalize-space()='Amount Paid']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[normalize-space()='Close']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//img)[2]"
        )

        time.sleep(2)
        
        amount_text = driver.find_element(By.XPATH, "//div[contains(@class,'stats-due')]").text

        amount = float(
            amount_text.replace("₹", "")
                    .replace(",", "")
                    .replace("-", "")  # remove negative sign
                    .strip()
        )

        amount_text = driver.find_element(By.XPATH, "//div[contains(@class,'stats-due')]").text

        clean_amount = amount_text.replace("₹", "").replace(",", "").strip()

        print(f"Total Amount Due (raw): {amount_text}")

        if "-" in clean_amount:
            print(f"⚠️ Amount is NEGATIVE: {clean_amount}")
        else:
            print(f"✅ Amount is POSITIVE or ZERO: {clean_amount}")

        time.sleep(5)
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e    



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Clear GST & Business Details After Customer Removal; Not Visible Post-Order Confirmation")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_24(login):
    try:
        time.sleep(3)
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(2)


        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//img[@src='./assets/images/menu/settings.png']"
        )


        time.sleep(2)
        pos_option_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_option_element)


        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//a[.//p[normalize-space()='Draft Order Creation With customer']]"
        )

        time.sleep(2)

        toggle = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']"))
        )

        is_checked = toggle.get_attribute("aria-checked")

        toggle_changed = False

        if is_checked == "true":
            toggle.click()
            toggle_changed = False
            print("Toggle was ON. Now turned OFF.")
        else:
            print("Toggle already OFF. No action taken.")

        # Check snackbar only if toggle changed
        if toggle_changed:
            msg = get_snack_bar_message(driver)
            print("Snack Bar Message :", msg)

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor text-capitalize']"
        )

        time.sleep(2)
        pos_option_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_option_element)

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//li//span[contains(text(),'Add to Cart With Login')]"
        )

        time.sleep(2)

        toggle = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']"))
        )

        is_checked = toggle.get_attribute("aria-checked")

        toggle_changed = False

        if is_checked == "true":
            toggle.click()
            toggle_changed = False
            print("Toggle was ON. Now turned OFF.")
        else:
            print("Toggle already OFF. No action taken.")

        # Check snackbar only if toggle changed
        if toggle_changed:
            msg = get_snack_bar_message(driver)
            print("Snack Bar Message :", msg)

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "(//img)[2]"
        )

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "(//*[@id='actionRouteTo_ORD_Dashbrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']"
        )            
    
        time.sleep(2)
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        login.execute_script("arguments[0].click();", select_element)

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnSave_ORD_CrtItemPop']"
        )

        time.sleep(2)
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
        wait_and_send_keys(
            driver, By.XPATH, "(//input[@placeholder='Search customers'])[1]", "555"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//span[normalize-space()='Id : 10']"
        )

        time.sleep(2)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@placeholder='GST Number']", "08ABCDE9999F1Z8"
        )

        time.sleep(1)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@placeholder='Business Name']", "Business"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnRmvCs_ORD_CrtItem']"
        )

        time.sleep(1)
        wait_and_locate_click(
        driver, By.XPATH, "//button[@id='btnConf_ORD_CrtItem']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        # Locate fields
        gst_field = driver.find_element(By.XPATH, "//input[@placeholder='GST Number']")
        business_field = driver.find_element(By.XPATH, "//input[@placeholder='Business Name']")

        # Get values
        gst_value = gst_field.get_attribute("value")
        business_value = business_field.get_attribute("value")

        # Print values
        print(f"GST Field Value: '{gst_value}'")
        print(f"Business Name Field Value: '{business_value}'")

        # Assertions
        assert gst_value == "", f"GST field is not empty, found: '{gst_value}'"
        assert business_value == "", f"Business Name field is not empty, found: '{business_value}'"

        # Check disabled status and print
        print(f"GST Field Enabled: {gst_field.is_enabled()}")
        print(f"Business Field Enabled: {business_field.is_enabled()}")

        assert not gst_field.is_enabled(), "GST field is not disabled"
        assert not business_field.is_enabled(), "Business Name field is not disabled"

        print("✅ Both GST and Business Name fields are empty and disabled.")

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//img[@src='./assets/images/menu/settings.png']"
        )


        time.sleep(2)
        pos_option_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_option_element)


        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//a[.//p[normalize-space()='Draft Order Creation With customer']]"
        )

        time.sleep(2)

        toggle = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']"))
        )

        is_checked = toggle.get_attribute("aria-checked")

        toggle_changed = True

        if is_checked == "false":
            toggle.click()
            toggle_changed = True
            print("Toggle was OFF. Now turned ON.")
        else:
            print("Toggle already ON. No action taken.")

        # Check snackbar only if toggle changed
        if toggle_changed:
            msg = get_snack_bar_message(driver)
            print("Snack Bar Message :", msg)

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor text-capitalize']"
        )

        time.sleep(2)
        time.sleep(2)
        pos_option_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_option_element)

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//li//span[contains(text(),'Add to Cart With Login')]"
        )

        time.sleep(2)

        toggle = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']"))
        )

        is_checked = toggle.get_attribute("aria-checked")

        toggle_changed = True

        if is_checked == "false":
            toggle.click()
            toggle_changed = True
            print("Toggle was OFF. Now turned ON.")
        else:
            print("Toggle already ON. No action taken.")

        # Check snackbar only if toggle changed
        if toggle_changed:
            msg = get_snack_bar_message(driver)
            print("Snack Bar Message :", msg)

        time.sleep(3)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Enable Order without patient and create and order finally disabled it")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_25(login):
    try:
        time.sleep(3)
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(2)

        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//img[@src='./assets/images/menu/settings.png']"
        )

        time.sleep(2)
        pos_option_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_option_element)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//a[.//span[contains(normalize-space(),'Sales Order')]]"
        )

        time.sleep(2)
        toggle = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@role='switch'])[4]"))
        )

        is_checked = toggle.get_attribute("aria-checked")

        toggle_changed = True

        if is_checked == "false":
            toggle.click()
            toggle_changed = True
            print("Toggle was OFF. Now turned ON.")
        else:
            print("Toggle already ON. No action taken.")

        # Check snackbar only if toggle changed
        if toggle_changed:
            msg = get_snack_bar_message(driver)
            print("Snack Bar Message :", msg)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//img)[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"
        )

        time.sleep(2)
        # Locate the toggle input
        toggle = driver.find_element(By.XPATH, "//div[contains(@class,'guest-mode-toggle')]//input[@role='switch']")

        # Check current state
        state = toggle.get_attribute("aria-checked")
        print(f"Current Guest Mode State: {'ON' if state == 'true' else 'OFF'}")

        # Turn ON only if it's OFF
        if state == "false":
            driver.find_element(By.XPATH, "//div[contains(@class,'guest-mode-toggle')]//span[contains(@class,'p-inputswitch-slider')]").click()
            print("Guest Mode turned ON")
        else:
            print("Guest Mode is already ON")

        time.sleep(2)
        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()

        full_name = first_name + " " + last_name

        wait_and_send_keys(
            driver, By.XPATH, "//input[@placeholder='Enter name']", full_name
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']"
        )            
    
        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//p-multiselect[@id='selectCat_ORD_CrtItemPop'])[1]")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

        time.sleep(2)
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

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnConf_ORD_CrtItem']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCrtInv_ORD_CrtItem']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnViewInv_ORD_CrtItem']"
        )

        
        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//img[@src='./assets/images/menu/settings.png']"
        )

        time.sleep(2)
        pos_option_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_option_element)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//a[.//span[contains(normalize-space(),'Sales Order')]]"
        )

        time.sleep(2)
        toggle = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@role='switch'])[4]"))
        )

        is_checked = toggle.get_attribute("aria-checked")

        toggle_changed = False  # default

        # ✅ Turn OFF only if it's ON
        if is_checked == "true":
            toggle.click()
            toggle_changed = True
            print("Toggle was ON. Now turned OFF.")
        else:
            print("Toggle already OFF. No action taken.")

        # ✅ Check snackbar only if toggle changed
        if toggle_changed:
            msg = get_snack_bar_message(driver)
            print("Snack Bar Message :", msg)

        time.sleep(3)
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating Order with the order without patient settings enabled and without name")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_26(login):
    try:
        time.sleep(3)
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(2)

        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//img[@src='./assets/images/menu/settings.png']"
        )

        time.sleep(2)
        pos_option_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_option_element)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//a[.//span[contains(normalize-space(),'Sales Order')]]"
        )

        time.sleep(2)
        toggle = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@role='switch'])[4]"))
        )

        is_checked = toggle.get_attribute("aria-checked")

        toggle_changed = True

        if is_checked == "false":
            toggle.click()
            toggle_changed = True
            print("Toggle was OFF. Now turned ON.")
        else:
            print("Toggle already ON. No action taken.")

        # Check snackbar only if toggle changed
        if toggle_changed:
            msg = get_snack_bar_message(driver)
            print("Snack Bar Message :", msg)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//img)[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"
        )

        time.sleep(2)
        # Locate the toggle input
        toggle = driver.find_element(By.XPATH, "//div[contains(@class,'guest-mode-toggle')]//input[@role='switch']")

        # Check current state
        state = toggle.get_attribute("aria-checked")
        print(f"Current Guest Mode State: {'ON' if state == 'true' else 'OFF'}")

        # Turn ON only if it's OFF
        if state == "false":
            driver.find_element(By.XPATH, "//div[contains(@class,'guest-mode-toggle')]//span[contains(@class,'p-inputswitch-slider')]").click()
            print("Guest Mode turned ON")
        else:
            print("Guest Mode is already ON")

        # time.sleep(2)
        # first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()

        # full_name = first_name + " " + last_name

        # wait_and_send_keys(
        #     driver, By.XPATH, "//input[@placeholder='Enter name']", full_name
        # )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']"
        )            
    
        time.sleep(2)
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        login.execute_script("arguments[0].click();", select_element)

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

        time.sleep(2)
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

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnConf_ORD_CrtItem']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)


        wait_and_locate_click(
            driver, By.XPATH, "//img[@src='./assets/images/menu/settings.png']"
        )

        time.sleep(2)
        pos_option_element = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, pos_option_element)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//a[.//span[contains(normalize-space(),'Sales Order')]]"
        )

        time.sleep(2)
        toggle = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@role='switch'])[4]"))
        )

        is_checked = toggle.get_attribute("aria-checked")

        toggle_changed = False  # default

        # ✅ Turn OFF only if it's ON
        if is_checked == "true":
            toggle.click()
            toggle_changed = True
            print("Toggle was ON. Now turned OFF.")
        else:
            print("Toggle already OFF. No action taken.")

        # ✅ Check snackbar only if toggle changed
        if toggle_changed:
            msg = get_snack_bar_message(driver)
            print("Snack Bar Message :", msg)

        time.sleep(3)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Adding GST and Business name to the order")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_27(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login
        
        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
    
        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"))
        ).click()
        
        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnCrtCs_ORD_CrtItemPop'])[1]"))
        ).click()

        
        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']"
        )            
    
        time.sleep(2)
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        login.execute_script("arguments[0].click();", select_element)

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

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
                (By.XPATH, "(//input[@id='actionSltSts_ORD_ItemSelect-input'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//button[@id='btnSltDn_ORD_ItemSelect'])[1]")

        time.sleep(2)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@placeholder='GST Number']", "27ABCDE1234F2Z5"
        )

        Business_name = "Business_name" + str(uuid.uuid4())[:6]
        
        time.sleep(2)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@placeholder='Business Name']", Business_name
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnConf_ORD_CrtItem'])[1]"
        )

        msg = get_toast_message(driver)
        print("Toast message:", msg)

        time.sleep(3)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating order with only GST number")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_28(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login
        
        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
    
        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"))
        ).click()
        
        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnCrtCs_ORD_CrtItemPop'])[1]"))
        ).click()

        
        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']"
        )            
    
        time.sleep(2)
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        login.execute_script("arguments[0].click();", select_element)

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

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
                (By.XPATH, "(//input[@id='actionSltSts_ORD_ItemSelect-input'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//button[@id='btnSltDn_ORD_ItemSelect'])[1]")

        time.sleep(2)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@placeholder='GST Number']", "27ABCDE1234F2Z5"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnConf_ORD_CrtItem'])[1]"
        )

        msg = get_toast_message(driver)
        print("Toast message:", msg)

        time.sleep(3)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating order with only business name")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_29(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login
        
        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
    
        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"))
        ).click()
        
        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnCrtCs_ORD_CrtItemPop'])[1]"))
        ).click()

        
        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(5)

        
        wait_and_locate_click(
            driver, By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']"
        )           
    
        time.sleep(2)
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        login.execute_script("arguments[0].click();", select_element)

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

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
                (By.XPATH, "(//input[@id='actionSltSts_ORD_ItemSelect-input'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//button[@id='btnSltDn_ORD_ItemSelect'])[1]")

        Business_name = "Business_name" + str(uuid.uuid4())[:6]
        
        time.sleep(2)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@placeholder='Business Name']", Business_name
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnConf_ORD_CrtItem'])[1]"
        )

        msg = get_toast_message(driver)
        print("Toast message:", msg)

        time.sleep(3)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating a walk-in sales order and invoice, and Share payment link")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_30(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login
        
        wait_and_locate_click(driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        option1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")))
        option1.click()
    
        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"))
        ).click()
        
        first_name, last_name, cons_manual_id, phonenumber,  email = create_user_data()
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnCrtCs_ORD_CrtItemPop'])[1]"))
        ).click()

        
        consumer_name = f"{first_name} {last_name}"
        print(f"Creating consumer: {consumer_name}")
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        time.sleep(5)

        wait_and_locate_click(
            driver, By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']"
        )            
    
        time.sleep(2)
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        login.execute_script("arguments[0].click();", select_element)

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

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
                (By.XPATH, "(//input[@id='actionSltSts_ORD_ItemSelect-input'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_Vitem'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//button[@id='btnSltDn_ORD_ItemSelect'])[1]")
 
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnConf_ORD_CrtItem'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "(//img)[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//*[@id='actionRouteTo_ORD_Dashbrd'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//*[@id='btnViewOrdr_ORD_OrdsList'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnEdt_ORD_CrtItem']"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[normalize-space()='Yes']"
        )

        time.sleep(2)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@placeholder='GST Number']", "27ABCDE1234F2Z5"
        )

        Business_name = "Business_name" + str(uuid.uuid4())[:6]
        
        time.sleep(2)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@placeholder='Business Name']", Business_name
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnUpdOrd_ORD_CrtItem']"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[normalize-space()='Yes']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnOdConfirm_ORD_CrtItem']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(3)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise 



#################      Delivery Profile      #######################

print()
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create Delivery Profile from Sales Order Module")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_delivery_profile(login):
    try:

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, 
                              "(//img)[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH,  
                              "(//div[@id='actionRouteTo_ORD_Dashbrd'])[10]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//p-button[@id='btnCretDprofile_ORD_DProfille'])[1]")
        
        delivery_profile = "Delivery_Profile" + str(uuid.uuid4())[:6]
        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, 
                              "(//input[@id='inputDPName_ORD_CreateDP'])[1]", delivery_profile)
        

        minimum_amount = WebDriverWait(login, 20).until(
                EC.presence_of_element_located((By.XPATH,
                                                "(//input[@type='number'])[1]"))
            )
        minimum_amount.click()
        minimum_amount.clear()
        minimum_amount_random_number = str(random.randint(150, 299))  # Setting MRP
        minimum_amount.send_keys(minimum_amount_random_number)
        print("minimum amount of the item:",minimum_amount_random_number)

        time.sleep(2)

        maximum_amount = WebDriverWait(login, 20).until(
                EC.presence_of_element_located((By.XPATH,
                                                "(//input[@type='number'])[2]"))
            )
        maximum_amount.click()
        maximum_amount.clear()
        maximum_amount_random_number = str(random.randint(300, 599))  # Setting MRP
        maximum_amount.send_keys(maximum_amount_random_number)
        print("minimum amount of the item:",maximum_amount_random_number)

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@type='number'])[3]", "35")

        
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnAdPrice_ORD_CreateDP']")


        minimum_amount = WebDriverWait(login, 20).until(
                EC.presence_of_element_located((By.XPATH,
                                                "(//input[@type='number'])[4]"))
            )
        minimum_amount.click()
        minimum_amount.clear()
        minimum_amount_random_number = str(random.randint(600, 999))  # Setting MRP
        minimum_amount.send_keys(minimum_amount_random_number)
        print("minimum amount of the item:",minimum_amount_random_number)

        time.sleep(2)

        maximum_amount = WebDriverWait(login, 20).until(
                EC.presence_of_element_located((By.XPATH,
                                                "(//input[@type='number'])[5]"))
            )
        maximum_amount.click()
        maximum_amount.clear()
        maximum_amount_random_number = str(random.randint(1000, 1499))  # Setting MRP
        maximum_amount.send_keys(maximum_amount_random_number)
        print("maximum amount of the item:",maximum_amount_random_number)

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@type='number'])[6]", "15")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnCreate_ORD_CreateDP']")

        msg = get_snack_bar_message(login)
        print("Toast Message :",msg)

        time.sleep(3)


    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create the Delivery Profile with Empty Fields")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_delivery_profile_with_empty_fields(login):
    try:
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//img)[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//div[@id='actionRouteTo_ORD_Dashbrd'])[10]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//p-button[@id='btnCretDprofile_ORD_DProfille'])[1]")
        
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnCreate_ORD_CreateDP']")

        msg = get_snack_bar_message(login)
        print("Snack bar Message :", msg)

        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create a Delivery Profile with Empty Price Range")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_delivery_profile_with_empty_price_range(login):
    try:
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//img)[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//div[@id='actionRouteTo_ORD_Dashbrd'])[10]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//p-button[@id='btnCretDprofile_ORD_DProfille'])[1]")
        
        delivery_profile = "Delivery_Profile" + str(uuid.uuid4())[:6]
        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, 
                              "(//input[@id='inputDPName_ORD_CreateDP'])[1]", delivery_profile)
        
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnCreate_ORD_CreateDP']")

        msg = get_snack_bar_message(login, timeout=5)
        print("Snack bar Message :", msg)

        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Edit delivery profile and Update")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_edit_delivery_profile_and_update(login):
    try:
        wait = WebDriverWait(login, 10)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//img)[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//*[contains(text(),'Delivery Profile')])[1]")

        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//button[@type='submit'][normalize-space()='View'])[2]")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='fa fa-pencil'])[1]")

        time.sleep(2)
    
        delivery_charge = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//input[@type='number'])[3]"))
        )
        delivery_charge.clear()
        delivery_charge.send_keys("40")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//*[normalize-space()='Update']")

        msg = get_snack_bar_message(login)
        print("Snack bar Message :", msg)

        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Assign delivery profile to the store")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_assign_delivery_profile_to_store(login):
    try:
        wait = WebDriverWait(login, 10)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//img)[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//*[contains(text(),'Delivery Profile')])[1]")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[contains(text(),'Assign')])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@aria-label='dropdown trigger'])[2]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='B&B Stores'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//div[@aria-label='dropdown trigger'])[3]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Home Delivery'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Save'])[1]")

        msg = get_snack_bar_message(login)
        print("Snack bar Message :", msg)

        time.sleep(2)
        
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Assign delivery profile to the store from detail page")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_assign_delivery_profile_to_store_from_detail_page(login):
    try:
        wait = WebDriverWait(login, 10)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//img)[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, 
                              "(//*[contains(text(),'Delivery Profile')])[1]")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@type='submit'][normalize-space()='View'])[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[contains(text(),'Assign')])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@aria-label='dropdown trigger'])[2]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='B&B Stores'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//div[@aria-label='dropdown trigger'])[3]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Store Pickup'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Save'])[1]")

        msg = get_snack_bar_message(login)
        print("Snack bar Message :", msg)

        time.sleep(2)
        
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e




#####################     Invoice Type     ####################################


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




        time.sleep(3)
        wait_and_locate_click(driver, By.XPATH, "(//p-multiselect[@id='selectCat_ORD_CrtItemPop'])[1]")

        time.sleep(2)
        select_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]")
        login.execute_script("arguments[0].click();", select_element)

        time.sleep(2)
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

        # time.sleep(2)
        # wait_and_locate_click(login, By.XPATH, "(//span[@id='actionSltBatch_ORD_CrtItem'])[1]")

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
    


########################    Sale Order Catalog    ############################


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
            (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[4] "))).click()
        
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