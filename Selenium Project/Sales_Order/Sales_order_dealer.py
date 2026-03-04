
import time
import allure

from Framework.common_utils import *
from Framework.consumer_common_utils import *




@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Dealer Creation")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_sales_order_1(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[8]"
        )
        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCreateClinic_ORD_dealer']"
        )

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        bs_name, vendors_id = create_business_detail()


        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputName_ORD_crteDlr']", bs_name
        )

        time.sleep(1)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputAliasName_ORD_crteDlr']", bs_name
        )

        time.sleep(1)
        wait_and_send_keys(
            driver, By.XPATH, "(//input[@id='phone'])[1]", phonenumber
        )
        time.sleep(1)
        
        wait_and_send_keys(
            driver, By.XPATH, "(//input[@id='phone'])[3]", phonenumber
        )

        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputEmail_ORD_crteDlr']", email
        )

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "//input[@id='inputShowGooglemap_ORD_crteDlr']"
        )

        time.sleep(2)

        try:
            # Locate the input field using XPath
            input_field = login.find_element(By.XPATH, "(//input[@id='pac-input'])[1]")

            # Input "Thrissur" into the text field
            input_field.send_keys("Thrissur")
            time.sleep(3)

            # Wait for the suggestions to appear and select the appropriate one
            wait = WebDriverWait(login, 10)
            suggestions = wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='pac-item']"))
            )

            time.sleep(3)

            # Iterate through the suggestions and select the one that matches "Thrissur, Kerala, India"
            for suggestion in suggestions:
                if "Thrissur, Kerala, India" in suggestion.text:
                    suggestion.click()
                    break

        finally:
            print("Loaction : Thrissur, Kerala, India")


        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnMpSele_ORD_gleMap']"
        )

        fake_india= Faker('en_IN')
        fake_india_address= fake_india.address().replace("\n", " ").strip()

        time.sleep(1)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputAddr1_ORD_crteDlr']", fake_india_address
        )

        time.sleep(1)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputAddr2_ORD_crteDlr']", fake_india_address
        )

        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputDistrt_ORD_crteDlr']", "Thrissur"
        )

        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputCity_ORD_crteDlr']", "Thrissur"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='dropdownState_ORD_crteDlr']"
        )

        time.sleep(1)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@class='p-dropdown-filter p-inputtext p-component']", "keral"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//span[normalize-space()='Kerala'])[1]"
        )

        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputPin_ORD_crteDlr']", "680505"
        )


        wait_and_locate_click(
            driver, By.XPATH, "//label[@id='lblgstphotoup_ODR_crteDlr']"
        )

        time.sleep(8)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))
        pyautogui.write(absolute_path)
        pyautogui.press('enter')

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCreatePartner_ORD_crteDlr']"
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
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Dealer Creation without mandatory field")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_sales_order_2(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[8]"
        )
        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCreateClinic_ORD_dealer']"
        )


         
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Reject the dealer")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_sales_order_3(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[8]"
        )
        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCreateClinic_ORD_dealer']"
        )

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        bs_name, vendors_id = create_business_detail()


        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputName_ORD_crteDlr']", bs_name
        )

        time.sleep(1)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputAliasName_ORD_crteDlr']", bs_name
        )

        time.sleep(1)
        wait_and_send_keys(
            driver, By.XPATH, "(//input[@id='phone'])[1]", phonenumber
        )
        time.sleep(1)
        
        wait_and_send_keys(
            driver, By.XPATH, "(//input[@id='phone'])[3]", phonenumber
        )

        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputEmail_ORD_crteDlr']", email
        )

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "//input[@id='inputShowGooglemap_ORD_crteDlr']"
        )

        time.sleep(2)

        try:
            # Locate the input field using XPath
            input_field = login.find_element(By.XPATH, "(//input[@id='pac-input'])[1]")

            # Input "Thrissur" into the text field
            input_field.send_keys("Thrissur")
            time.sleep(3)

            # Wait for the suggestions to appear and select the appropriate one
            wait = WebDriverWait(login, 10)
            suggestions = wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='pac-item']"))
            )

            time.sleep(3)

            # Iterate through the suggestions and select the one that matches "Thrissur, Kerala, India"
            for suggestion in suggestions:
                if "Thrissur, Kerala, India" in suggestion.text:
                    suggestion.click()
                    break

        finally:
            print("Loaction : Thrissur, Kerala, India")


        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnMpSele_ORD_gleMap']"
        )

        fake_india= Faker('en_IN')
        fake_india_address= fake_india.address().replace("\n", " ").strip()

        time.sleep(1)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputAddr1_ORD_crteDlr']", fake_india_address
        )

        time.sleep(1)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputAddr2_ORD_crteDlr']", fake_india_address
        )

        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputDistrt_ORD_crteDlr']", "Thrissur"
        )

        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputCity_ORD_crteDlr']", "Thrissur"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='dropdownState_ORD_crteDlr']"
        )

        time.sleep(1)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@class='p-dropdown-filter p-inputtext p-component']", "keral"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//span[normalize-space()='Kerala'])[1]"
        )

        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputPin_ORD_crteDlr']", "680505"
        )


        wait_and_locate_click(
            driver, By.XPATH, "//label[@id='lblgstphotoup_ODR_crteDlr']"
        )

        time.sleep(8)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))
        pyautogui.write(absolute_path)
        pyautogui.press('enter')

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCreatePartner_ORD_crteDlr']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnUpdateClinic_ORD_dealer'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCreatePartner_ORD_crteDlr']"
        )

        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnViewClinic_ORD_dealer'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//div[@id='divRejectClinic_ORD_dlrApprve']"
        )

        wait_and_send_keys(
            driver, By.XPATH, "//textarea[@placeholder='Enter Remarks']", "Reject"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//div[@id='divChecked_ORD_cnfrmBox']"
        )

        msg =  get_snack_bar_message(driver)
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
@allure.title("Create order for the Dealer")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_sales_order_4(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"
        )

        time.sleep(1)
        element_store = login.find_element(By.XPATH, "//span[normalize-space()='B&B Stores']")

        scroll_to_element(login, element_store)
        time.sleep(1)
        element_store.click()

        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='drpCustPrtnrType_ORD_CrtItemPop']"
        )

        time.sleep(2)
        option_element = driver.find_element(By.XPATH, "//li[@aria-label='Dealer']")
        driver.execute_script("arguments[0].click();", option_element)

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='drpPartnrs_ORD_CrtItemPop']"
        )

        time.sleep(2)
        dealer_option = driver.find_element(By.XPATH, "//li[@aria-label='M&M']")
        driver.execute_script("arguments[0].click();", dealer_option)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//span[normalize-space()='Sale_catalog']"
        )

        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

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
        confirm_element = driver.find_element(By.XPATH, "//button[@id='btnConf_ORD_CrtItem']")
        time.sleep(2)
        scroll_to_element(driver, confirm_element)
        time.sleep(1)
        confirm_element.click()

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        invoice_element = driver.find_element(By.XPATH, "//button[@id='btnCrtInv_ORD_CrtItem']")
        scroll_to_element(driver, invoice_element)
        time.sleep(2)
        invoice_element.click()

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnViewInv_ORD_CrtItem']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//i[@class='pi pi-arrow-left']"
        )

        time.sleep(2)
        complete_element = driver.find_element(By.XPATH, "//button[@id='btnOdCng_ORD_CrtItem']")
        scroll_to_element(driver, complete_element)
        time.sleep(2)
        complete_element.click()

        msg = get_toast_message(driver)
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
@allure.title("Create Dealer from Create Order popup")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_sales_order_5(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"
        )

        time.sleep(1)
        element_store = login.find_element(By.XPATH, "//span[normalize-space()='B&B Stores']")

        scroll_to_element(login, element_store)
        time.sleep(1)
        element_store.click()

        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='drpCustPrtnrType_ORD_CrtItemPop']"
        )

        time.sleep(2)
        option_element = driver.find_element(By.XPATH, "//li[@aria-label='Dealer']")
        driver.execute_script("arguments[0].click();", option_element)


        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCrtClin_ORD_CrtItemPop']"
        )


        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        bs_name, vendors_id = create_business_detail()


        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputName_ORD_crteDlr']", bs_name
        )

        time.sleep(1)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputAliasName_ORD_crteDlr']", bs_name
        )

        time.sleep(1)
        wait_and_send_keys(
            driver, By.XPATH, "(//input[@id='phone'])[1]", phonenumber
        )
        time.sleep(1)
        
        wait_and_send_keys(
            driver, By.XPATH, "(//input[@id='phone'])[3]", phonenumber
        )

        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputEmail_ORD_crteDlr']", email
        )

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "//input[@id='inputShowGooglemap_ORD_crteDlr']"
        )

        time.sleep(2)

        try:
            # Locate the input field using XPath
            input_field = login.find_element(By.XPATH, "(//input[@id='pac-input'])[1]")

            # Input "Thrissur" into the text field
            input_field.send_keys("Thrissur")
            time.sleep(3)

            # Wait for the suggestions to appear and select the appropriate one
            wait = WebDriverWait(login, 10)
            suggestions = wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='pac-item']"))
            )

            time.sleep(3)

            # Iterate through the suggestions and select the one that matches "Thrissur, Kerala, India"
            for suggestion in suggestions:
                if "Thrissur, Kerala, India" in suggestion.text:
                    suggestion.click()
                    break

        finally:
            print("Loaction : Thrissur, Kerala, India")


        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnMpSele_ORD_gleMap']"
        )

        fake_india= Faker('en_IN')
        fake_india_address= fake_india.address().replace("\n", " ").strip()

        time.sleep(1)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputAddr1_ORD_crteDlr']", fake_india_address
        )

        time.sleep(1)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputAddr2_ORD_crteDlr']", fake_india_address
        )

        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputDistrt_ORD_crteDlr']", "Thrissur"
        )

        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputCity_ORD_crteDlr']", "Thrissur"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='dropdownState_ORD_crteDlr']"
        )

        time.sleep(1)
        wait_and_send_keys(
            driver, By.XPATH, "//input[@class='p-dropdown-filter p-inputtext p-component']", "keral"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//span[normalize-space()='Kerala'])[1]"
        )

        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputPin_ORD_crteDlr']", "680505"
        )


        wait_and_locate_click(
            driver, By.XPATH, "//label[@id='lblgstphotoup_ODR_crteDlr']"
        )

        time.sleep(8)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))
        pyautogui.write(absolute_path)
        pyautogui.press('enter')

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCreatePartner_ORD_crteDlr']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        
        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnUpdateClinic_ORD_dealer'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCreatePartner_ORD_crteDlr']"
        )

        wait_and_locate_click(
            driver, By.XPATH, "(//button[@id='btnViewClinic_ORD_dealer'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//div[@id='divApproveClinic_ORD_dlrApprve']"
        )

        time.sleep(1)
        wait_and_send_keys(
            driver, By.XPATH, "//textarea[@placeholder='Enter Remarks']", "Dealer Remarks"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//div[@id='divApproveClinic_ORD_cnfrmBox']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//p-multiselect[@id='selectCat_ORD_CrtItemPop']"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//span[normalize-space()='Sale_catalog']"
        )

        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))).click()


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@id='btnSave_ORD_CrtItemPop'])[1]"))
        ).click()

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
        confirm_element = driver.find_element(By.XPATH, "//button[@id='btnConf_ORD_CrtItem']")
        time.sleep(2)
        scroll_to_element(driver, confirm_element)
        time.sleep(1)
        confirm_element.click()

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        invoice_element = driver.find_element(By.XPATH, "//button[@id='btnCrtInv_ORD_CrtItem']")
        scroll_to_element(driver, invoice_element)
        time.sleep(2)
        invoice_element.click()

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnViewInv_ORD_CrtItem']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//i[@class='pi pi-arrow-left']"
        )

        time.sleep(2)
        complete_element = driver.find_element(By.XPATH, "//button[@id='btnOdCng_ORD_CrtItem']")
        scroll_to_element(driver, complete_element)
        time.sleep(2)
        complete_element.click()

        msg = get_toast_message(driver)
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
@allure.title("Item Disable Error Handling in Inventory Catalog")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_sales_order_6(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login

        wait_and_locate_click(
            driver, By.XPATH, "(//img)[3]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionNav_ORD_Inventory'])[4]"
        )

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"
        )

        store_element = driver.find_element(By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='B&B Stores']")

        scroll_to_element(driver, store_element)
        time.sleep(2)
        store_element.click()

        time.sleep(2)

        catalog_name = "Catalog_Inventory"

        while True:
            # Use find_elements instead of find_element
            rows = driver.find_elements(
                By.XPATH,
                f"//tr[.//div[contains(@class,'fw-bold') and normalize-space(.)='{catalog_name}']]"
            )

            if rows:
                action_btn = rows[0].find_element(
                    By.XPATH, ".//button[@id='btnActMenu_ORD_Catalog']"
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

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnViewCatlg_ORD_Catalog']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//p-inputswitch)[9]"
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
        raise e