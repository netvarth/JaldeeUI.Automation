import time
import allure

from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating the item")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_item_creation_1(login):

    wait = WebDriverWait(login, 30)
    try:
        time.sleep(5)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
        ).click()

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//div[@id='actionNav_ORD_Inventory'])[3]")          

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='btnCrtItem_ORD_Items']"))
        ).click()

        item_name = "Item_" + str(uuid.uuid4())[:4]

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='inpItemName_ORD_INV_ItemCreate']"))
        ).send_keys(item_name)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='txtaShortDesc_ORD_INV_ItemCreate']"))
        ).send_keys("A Item name is required and recommended to be unique.")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@id='ddCategory_ORD_INV_ItemCreate']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='Stationary']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-multiselect[@id='msGroup_ORD_INV_ItemCreate']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='Stationary_Item']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@id='ddType_ORD_INV_ItemCreate']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='Office_Item']"))
        ).click()

        login.implicitly_wait(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@id='ddManufacturer_ORD_INV_ItemCreate']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='SC.PVT.Limited']"))
        ).click()

        dropdown = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//p-multiselect[@id='msUnits_ORD_INV_ItemCreate']"))
        )
        dropdown.click()

        time.sleep(2)
        options = dropdown.find_elements(By.XPATH, "//ul[@role='listbox']")

        # Select a random option
        if options:
            random_option = random.choice(options)
            random_option.click()
        else:
            print("No options found in the dropdown.")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@placeholder='Track Inventory or Not']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='ng-star-inserted'][normalize-space()='Yes']"))
        ).click()

        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@id='ddHSN_ORD_INV_ItemCreate']")

        time.sleep(2)
        options = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@role='listbox']//li[@role='option']")
            )
        )

        # Pick a random option
        random_option = random.choice(options)

        # Scroll into view (important for PrimeNG)
        login.execute_script("arguments[0].scrollIntoView(true);", random_option)

        # Click the option
        random_option.click()

        # (Optional) Print selected value
        print("Selected value:", random_option.text)

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-multiselect[@id='msTaxes_ORD_INV_ItemCreate']")
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='GST 5%']"))
        ).click()

        time.sleep(2)

        scroll_to_window(login)
        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='btnSubmit_ORD_INV_ItemCreate']"))
        ).click()

        msg = get_toast_message(login)
        print("Toast Message : ", msg)

        time.sleep(3)

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e 
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating the item with item option")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_item_creation_2(login):

    wait = WebDriverWait(login, 30)
    try:
        time.sleep(5)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
        ).click()

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//div[@id='actionNav_ORD_Inventory'])[3]")          

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='btnCrtItem_ORD_Items']"))
        ).click()

        item_name = "Item_" + str(uuid.uuid4())[:4]

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='inpItemName_ORD_INV_ItemCreate']"))
        ).send_keys(item_name)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='txtaShortDesc_ORD_INV_ItemCreate']"))
        ).send_keys("A Item name is required and recommended to be unique.")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@id='ddCategory_ORD_INV_ItemCreate']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='Stationary']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-multiselect[@id='msGroup_ORD_INV_ItemCreate']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='Stationary_Item']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@id='ddType_ORD_INV_ItemCreate']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='Office_Item']"))
        ).click()

        login.implicitly_wait(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@id='ddManufacturer_ORD_INV_ItemCreate']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='SC.PVT.Limited']"))
        ).click()

        dropdown = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//p-multiselect[@id='msUnits_ORD_INV_ItemCreate']"))
        )
        dropdown.click()

        time.sleep(2)
        options = dropdown.find_elements(By.XPATH, "//ul[@role='listbox']")

        # Select a random option
        if options:
            random_option = random.choice(options)
            random_option.click()
        else:
            print("No options found in the dropdown.")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@placeholder='Track Inventory or Not']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='ng-star-inserted'][normalize-space()='Yes']"))
        ).click()

        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@id='ddHSN_ORD_INV_ItemCreate']")

        time.sleep(2)
        options = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@role='listbox']//li[@role='option']")
            )
        )

        # Pick a random option
        random_option = random.choice(options)

        # Scroll into view (important for PrimeNG)
        login.execute_script("arguments[0].scrollIntoView(true);", random_option)

        # Click the option
        random_option.click()

        # (Optional) Print selected value
        print("Selected value:", random_option.text)

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='ddBatchApplicable_ORD_INV_ItemCreate']"))
        ).click()

        wait_and_locate_click(login, By.XPATH, "(//*[@class='ng-star-inserted'][normalize-space()='Yes'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-multiselect[@id='msTaxes_ORD_INV_ItemCreate']")
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='GST 5%']"))
        ).click()

        time.sleep(2)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnAddOption_ORD_ItemOpt']"))
        ).click()
        
        time.sleep(2)
        option_name = WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='inputOptName_ORD_ItemOpt']"))
        )  
        login.execute_script("arguments[0].click();", option_name)
        time.sleep(3)
        option_name.send_keys("Colour")

        time.sleep(2)
        enter_name = WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='inputOptVal_ORD_ItemOpt']"))
        )
        enter_name.send_keys("Bule")
        enter_name.send_keys(Keys.RETURN)

        time.sleep(2)
        enter_name.send_keys("Black")
        enter_name.send_keys(Keys.RETURN)

        time.sleep(2)
        enter_name.send_keys("Green")
        enter_name.send_keys(Keys.RETURN)

        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnAddItem_ORD_ItemOpt']"))
        ).click()


        scroll_to_window(login)
        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='btnSubmit_ORD_INV_ItemCreate']"))
        ).click()

        msg = get_toast_message(login)
        print("Toast Message : ", msg)

        time.sleep(3)

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e 

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating the item wit Batch Enabled")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_item_creation_3(login):

    wait = WebDriverWait(login, 30)
    try:
        time.sleep(5)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
        ).click()

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//div[@id='actionNav_ORD_Inventory'])[3]")          

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='btnCrtItem_ORD_Items']"))
        ).click()

        item_name = "Item_" + str(uuid.uuid4())[:4]

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='inpItemName_ORD_INV_ItemCreate']"))
        ).send_keys(item_name)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='txtaShortDesc_ORD_INV_ItemCreate']"))
        ).send_keys("A Item name is required and recommended to be unique.")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@id='ddCategory_ORD_INV_ItemCreate']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='Stationary']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-multiselect[@id='msGroup_ORD_INV_ItemCreate']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='Stationary_Item']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@id='ddType_ORD_INV_ItemCreate']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='Office_Item']"))
        ).click()

        login.implicitly_wait(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@id='ddManufacturer_ORD_INV_ItemCreate']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='SC.PVT.Limited']"))
        ).click()

        dropdown = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//p-multiselect[@id='msUnits_ORD_INV_ItemCreate']"))
        )
        dropdown.click()

        time.sleep(2)
        options = dropdown.find_elements(By.XPATH, "//ul[@role='listbox']")

        # Select a random option
        if options:
            random_option = random.choice(options)
            random_option.click()
        else:
            print("No options found in the dropdown.")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@placeholder='Track Inventory or Not']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='ng-star-inserted'][normalize-space()='Yes']"))
        ).click()

        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@id='ddHSN_ORD_INV_ItemCreate']")

        time.sleep(2)
        options = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@role='listbox']//li[@role='option']")
            )
        )

        # Pick a random option
        random_option = random.choice(options)

        # Scroll into view (important for PrimeNG)
        login.execute_script("arguments[0].scrollIntoView(true);", random_option)

        # Click the option
        random_option.click()

        # (Optional) Print selected value
        print("Selected value:", random_option.text)

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='ddBatchApplicable_ORD_INV_ItemCreate']"))
        ).click()

        wait_and_locate_click(login, By.XPATH, "(//*[@class='ng-star-inserted'][normalize-space()='Yes'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-multiselect[@id='msTaxes_ORD_INV_ItemCreate']")
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='GST 5%']"))
        ).click()

        time.sleep(2)

        scroll_to_window(login)
        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='btnSubmit_ORD_INV_ItemCreate']"))
        ).click()

        msg = get_toast_message(login)
        print("Toast Message : ", msg)

        time.sleep(3)

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e 
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Item disable and enabled")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_item_disable_and_enabled(login):
    try:
        # ---- Navigate to Items ----
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
        ).click()

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@id='actionNav_ORD_Inventory'])[3]"))
        ).click()

        # ---- Row 1 locators ----
        row1_xpath = "//table[@role='table']//tbody/tr[1]"
        status_cell_xpath = "//table[@role='table']//tbody/tr[1]//span[contains(@class,'status-')]"
        actions_btn_xpath = "(//table[@role='table']//tbody/tr[1]//button[@aria-haspopup='menu' and normalize-space()='Actions'])[1]"
        overlay_xpath = "//div[contains(@class,'cdk-overlay-pane')]"

        # ================== DISABLE ==================
        # Open Actions (scroll into view + retry)
        btn = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, actions_btn_xpath)))
        login.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
        try:
            btn.click()
        except Exception:
            time.sleep(0.4)
            login.execute_script("arguments[0].click();", btn)

        WebDriverWait(login, 7).until(EC.presence_of_element_located((By.XPATH, overlay_xpath)))

        # Click "Disable" (text-first, fallback index [3])
        try:
            WebDriverWait(login, 5).until(
                EC.element_to_be_clickable((By.XPATH, f"{overlay_xpath}//span[@class='mdc-list-item__primary-text' and normalize-space()='Disable']"))
            ).click()
        except Exception:
            WebDriverWait(login, 5).until(
                EC.element_to_be_clickable((By.XPATH, f"({overlay_xpath}//span[@class='mdc-list-item__primary-text'])[3]"))
            ).click()

        # Toast + wait for status text to become "Disable"
        message = get_toast_message(login)
        print("Toast Message :", message)

        WebDriverWait(login, 15).until(
            EC.text_to_be_present_in_element((By.XPATH, status_cell_xpath), "Disable")
        )
        status_after_disable = login.find_element(By.XPATH, status_cell_xpath).text.strip()
        assert status_after_disable == "Disable", f"Expected 'Disable' but got '{status_after_disable}'"
        allure.attach(status_after_disable, "Status after Disable", attachment_type=AttachmentType.TEXT)

        # ================== ENABLE (cleanup) ==================
        # Open Actions again (re-find button to avoid stale)
        btn = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, actions_btn_xpath)))
        login.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
        try:
            btn.click()
        except Exception:
            time.sleep(0.4)
            login.execute_script("arguments[0].click();", btn)

        WebDriverWait(login, 7).until(EC.presence_of_element_located((By.XPATH, overlay_xpath)))

        # Click "Enable" (text-first, fallback index [2] per your note)
        try:
            WebDriverWait(login, 5).until(
                EC.element_to_be_clickable((By.XPATH, f"{overlay_xpath}//span[@class='mdc-list-item__primary-text' and normalize-space()='Enable']"))
            ).click()
        except Exception:
            WebDriverWait(login, 5).until(
                EC.element_to_be_clickable((By.XPATH, f"({overlay_xpath}//span[@class='mdc-list-item__primary-text'])[2]"))
            ).click()

        # Toast + wait for status text to become "Enable"
        message = get_toast_message(login)
        print("Toast (Enable):", message)

        WebDriverWait(login, 15).until(
            EC.text_to_be_present_in_element((By.XPATH, status_cell_xpath), "Enable")
        )
        status_after_enable = login.find_element(By.XPATH, status_cell_xpath).text.strip()
        assert status_after_enable == "Enable", f"Expected 'Enable' but got '{status_after_enable}'"
        allure.attach(status_after_enable, "Status after Enable", attachment_type=AttachmentType.TEXT)

        print("✅ Disable → verified in table, then Enable → verified in table")

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Item Edit and update")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_item_edit_update(login):
    try:
        # ---- Navigate to Items ----
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
        ).click()

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Items']"))
        ).click()
        wait_and_click(login, By.XPATH, "(//table[@role='table']//tbody/tr[1]//button[@aria-haspopup='menu' and normalize-space()='Actions'])[1]")
        
        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[2]")





    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test for item filter item id ")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_item_filter(login):

    time.sleep(3)
    wait = WebDriverWait(login, 20)
    wait.until(
        EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
    ).click()

    time.sleep(3)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Items']"))
    ).click()  

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//i[@class='pi pi-filter-fill'])[1]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(), 'Item ID')]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//input[@id='spCode'])[1]"))
    ).send_keys("alrx-33b5uu2-2wl")

    time.sleep(3)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='Apply'])[1]"))
    ).click()

    print("Apply the the filter")
    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Actions'])[1]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[1]"))
    ).click()
    print("Enter into the item detail page")
    time.sleep(3)
    # Assert that the ID is present on the page
    element = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, f"//*[contains(text(), 'alrx-33b5uu2-2wl')]")
        )
    )
    assert element is not None, "The ID 'alrx-33b5uu2-2wl' was not found on the page"
    print("Assertion passed: The ID 'alrx-33b5uu2-2wl' is present on the page")
    
      
    scroll_down = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(), 'Item Consumption History')]"))
    )
    login.execute_script("arguments[0].scrollIntoView();", scroll_down)

    time.sleep(3)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//i[@class='pi pi-filter-fill'])[1]"))
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(), 'Transaction Type')]"))
    ).click()

    time.sleep(2)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Select transactionTypeEnum')]"))
    ).click()

    select_sales = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='Sales'])[1]"))
    )
    login.execute_script("arguments[0].click();", select_sales)

    time.sleep(3)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='Apply'])[1]"))
    ).click()


    print("Applied filter for Transaction Type: Sales")

    # Assert the table only contains rows with Transaction Type as "Sales"
    time.sleep(3)
    table = wait.until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
    )
    rows = table.find_elements(By.XPATH, "//tbody/tr")

    for row in rows:
        transaction_type = row.find_element(By.XPATH, "./td[5]/span").text.strip()
        assert transaction_type == "SALES", f"Found non-SALES transaction type: {transaction_type}"

    print("Assertion passed: All rows in the table have Transaction Type as 'SALES'.")

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create the Remarks from item Variant")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_item_variant_remarks(login):
    wait = WebDriverWait(login, 30)
    try:
        time.sleep(5)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
        ).click()

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//div[@id='actionNav_ORD_Inventory'])[9]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@id='actionSltOpt_ORD_ItemVar'])[8]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnCrt_ORD_Remarks']")

        Remarks = "ItemRemarks" + str(uuid.uuid4())[:4]
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@id='inputHsn_ORD_ItemCrtPop']", Remarks)

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@id='selectRmrks_ORD_ItemCrtPop']")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='Adjustment'])[1]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnSave_ORD_ItemCrtPop']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(2)
        # XPath for first row remark name (tr[1], td[1])
        first_row_remark = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "(//tbody//tr)[1]/td[1]//span")
            )
        )

        print("Table Remark:", first_row_remark.text)

        assert Remarks.strip() == first_row_remark.text.strip(), (
            f"Expected remark '{Remarks}' but found '{first_row_remark.text}'"
        )
        

        time.sleep(1)
        status_switch = login.find_element(
            By.XPATH,
            "(//tbody//tr)[1]//input[@role='switch']"
        )

        assert status_switch.get_attribute("aria-checked") == "true", "Status is not enabled"

        time.sleep(2)
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Update the Remarks from item Variant")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_update_item_variant_remarks(login):
    wait = WebDriverWait(login, 30)
    try:
        time.sleep(5)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
        ).click()

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//div[@id='actionNav_ORD_Inventory'])[9]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@id='actionSltOpt_ORD_ItemVar'])[8]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnCraeat_ORD_Remarks'])[1]")

        Remarks = "Rename_ItemRemarks" + str(uuid.uuid4())[:4]
        time.sleep(2)
        remarks_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='inputHsn_ORD_ItemCrtPop']"))
        )
        remarks_element.clear()
        remarks_element.send_keys(Remarks)
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnSave_ORD_ItemCrtPop']")

        time.sleep(1)
        

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(2)

        updated_remark = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "(//tbody//tr)[1]/td[1]//span")
            )
        )

        print("Table Remark:", updated_remark.text)
        assert updated_remark.text.strip() == Remarks.strip()
        
        time.sleep(2)
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e