
from Framework.common_utils import *
from Framework.consumer_common_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating a walk-in sales order and invoice, and Share payment link")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_1(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        
        
        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))).click()

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

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-multiselect[@id='selectCat_ORD_CrtItemPop'])[1]"))
        ).click()
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


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

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-multiselect[@id='selectCat_ORD_CrtItemPop'])[1]"))
        ).click()
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


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

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-multiselect[@id='selectCat_ORD_CrtItemPop'])[1]"))
        ).click()
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


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

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-multiselect[@id='selectCat_ORD_CrtItemPop'])[1]"))
        ).click()
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


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
        
        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))).click()

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

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-multiselect[@id='selectCat_ORD_CrtItemPop'])[1]"))
        ).click()
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


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

        create_element = login.find_element(By.XPATH, "//button[@id='btnUpdOrd_ORD_CrtItem']")
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
@allure.title("Creating a walk-in sales order with Label ")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_sales_order_6(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        
        
        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))).click()

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

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-multiselect[@id='selectCat_ORD_CrtItemPop'])[1]"))
        ).click()
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


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
        
        
        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))).click()

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

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-multiselect[@id='selectCat_ORD_CrtItemPop'])[1]"))
        ).click()
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


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


        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))).click()

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

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-multiselect[@id='selectCat_ORD_CrtItemPop'])[1]"))
        ).click()
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


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


        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))).click()
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
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-multiselect[@id='selectCat_ORD_CrtItemPop'])[1]"))
        ).click()
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


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


        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))).click()
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

        price = random.randint(23000, 26000)
        print(price)

        time.sleep(1)
        sell_price_element = driver.find_element(By.XPATH, "(//input[@type='number'])[1]")
        sell_price_element.click()
        time.sleep(1)
        sell_price_element.clear()
        sell_price_element.send_keys(price)



        time.sleep(1)

        wait_and_locate_click(
            driver, By.XPATH, "(//p-dropdown[@id='selectCat_ORD_EdtPurchs'])[2]"
        )
        
        time.sleep(1)
        catalog_element = driver.find_element(By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Sale_catalog'])[1]")
        scroll_to_element(driver, catalog_element)
        time.sleep(2)
        catalog_element.click()

        time.sleep(1)
        sell_price_element = driver.find_element(By.XPATH, "(//input[@type='number'])[2]")
        sell_price_element.click()
        time.sleep(1)
        sell_price_element.clear()
        sell_price_element.send_keys(price)

        time.sleep(1)

        wait_and_locate_click(
            driver, By.XPATH, "(//p-dropdown[@id='selectCat_ORD_EdtPurchs'])[3]"
        )
        
        time.sleep(1)
        catalog_element = driver.find_element(By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Sale_catalog'])[1]")
        scroll_to_element(driver, catalog_element)
        time.sleep(2)
        catalog_element.click()

        time.sleep(1)
        sell_price_element = driver.find_element(By.XPATH, "(//input[@type='number'])[3]")
        sell_price_element.click()
        time.sleep(1)
        sell_price_element.clear()
        sell_price_element.send_keys(price)


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
        
        time.sleep(2)
        element_item = driver.find_element(By.XPATH, "//div[normalize-space()='Item_8']")
        scroll_to_element(driver, element_item)
        time.sleep(2)
        element_item.click()

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[normalize-space()='Add to Wishlist']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//i[@class='fa fa-heart-o wishlist-icon'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//h3[normalize-space()='Item_8']"
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

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnPrimaryAction']"
        )

        time.sleep(1)
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


        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))).click()
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

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-multiselect[@id='selectCat_ORD_CrtItemPop'])[1]"))
        ).click()
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


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


        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))).click()
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
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-multiselect[@id='selectCat_ORD_CrtItemPop'])[1]"))
        ).click()
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


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


        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))).click()
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
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-multiselect[@id='selectCat_ORD_CrtItemPop'])[1]"))
        ).click()
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


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


        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))).click()
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
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-multiselect[@id='selectCat_ORD_CrtItemPop'])[1]"))
        ).click()
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


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
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Sale_catalog'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


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
            driver, By.XPATH, "(//input[@type='checkbox'])[6]"
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
            driver, By.XPATH, "(//span[@id='actionSltBatch_ORD_CrtItem'])[1]"
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
    
