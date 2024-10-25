from Framework.common_utils import *
from Framework.common_dates_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Store_Walkin_POS and Online_POS Enabled")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_store_POS_Enabled(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//img[contains(@src, 'settings.gif')]//following::div[contains(text(),'Settings')]")
        time.sleep(2)
        POS = wait_and_locate_click(login, By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(login, POS)       
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p[normalize-space()='Sales Order Management System']")
        time.sleep(2)
        Sales_order = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']")) 
            )
        aria_checked = Sales_order.get_attribute("aria-checked")
        if aria_checked == "true":
            print("Sales Orders Management is already active, no need to click.")
        else:
            Sales_order.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Stores')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create Store']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Type']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Pharmacy']")
        time.sleep(2)
        storename = f"Store{''.join(random.choices(string.ascii_letters + string.digits, k=8))}"
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Name']", storename)
        actualstorename_value = storename.strip()
        print("StoreName is:", actualstorename_value)
        time.sleep(2)
        random_number = str(random.randint(1111111, 9999999))
        phonenumber = f"{555}{random_number}"
        wait_and_send_keys(login, By.XPATH, "//input[@id='phone']", phonenumber)
        time.sleep(2)
        email = f"{storename}{test_mail}"
        wait_and_send_keys(login, By.XPATH, "//input[@id='email']", email)
        time.sleep(2)
        invoice_prefix = "S-" + str(uuid.uuid4())[:2]
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Invoice prefix']", invoice_prefix)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Location']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Round North']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Online Self Order']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Yes']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Walk-in-POS']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Yes']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Create']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        login.refresh()
        time.sleep(3)
        stores = login.find_element(By.XPATH, "//tbody/tr[1]")
        storetext = stores.text
        storename_before_id = storetext.split("Id:")[0]
        expectedstorename_value = storename_before_id.strip()
        print("StoreName is:", expectedstorename_value)
        print(f"Expected Storename: '{expectedstorename_value}', Actual Storename: '{actualstorename_value}'")
        assert actualstorename_value == expectedstorename_value, f"Expected Storename: {storename_before_id} but got Storename {actualstorename_value}"
        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Store_Walkin_POS and Online_POS Disabled")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_store_POS_Disabled(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//img[contains(@src, 'settings.gif')]//following::div[contains(text(),'Settings')]")
        time.sleep(2)
        POS = wait_and_locate_click(login, By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(login, POS)       
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p[normalize-space()='Sales Order Management System']")
        time.sleep(2)
        Sales_order = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']")) 
            )
        aria_checked = Sales_order.get_attribute("aria-checked")
        if aria_checked == "true":
            print("Sales Orders Management is already active, no need to click.")
        else:
            Sales_order.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Stores')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create Store']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Type']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Pharmacy']")
        time.sleep(2)
        storename = f"Store{''.join(random.choices(string.ascii_letters + string.digits, k=8))}"
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Name']", storename)
        actualstorename_value = storename.strip()
        print("StoreName is:", actualstorename_value)
        time.sleep(2)
        random_number = str(random.randint(1111111, 9999999))
        phonenumber = f"{555}{random_number}"
        wait_and_send_keys(login, By.XPATH, "//input[@id='phone']", phonenumber)
        time.sleep(2)
        email = f"{storename}{test_mail}"
        wait_and_send_keys(login, By.XPATH, "//input[@id='email']", email)
        time.sleep(2)
        invoice_prefix = "S-" + str(uuid.uuid4())[:2]
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Invoice prefix']", invoice_prefix)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Location']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Round North']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Online Self Order']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='No']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Walk-in-POS']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='No']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Create']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        login.refresh()
        time.sleep(3)
        stores = login.find_element(By.XPATH, "//tbody/tr[1]")
        storetext = stores.text
        storename_before_id = storetext.split("Id:")[0]
        expectedstorename_value = storename_before_id.strip()
        print("StoreName is:", expectedstorename_value)
        print(f"Expected Storename: '{expectedstorename_value}', Actual Storename: '{actualstorename_value}'")
        assert actualstorename_value == expectedstorename_value, f"Expected Storename: {storename_before_id} but got Storename {actualstorename_value}"
        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Store_Walkin_POS Enabled")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_store_Walkin_POS(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//img[contains(@src, 'settings.gif')]//following::div[contains(text(),'Settings')]")
        time.sleep(2)
        POS = wait_and_locate_click(login, By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(login, POS)       
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p[normalize-space()='Sales Order Management System']")
        time.sleep(2)
        Sales_order = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']")) 
            )
        aria_checked = Sales_order.get_attribute("aria-checked")
        if aria_checked == "true":
            print("Sales Orders Management is already active, no need to click.")
        else:
            Sales_order.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Stores')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create Store']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Type']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Pharmacy']")
        time.sleep(2)
        storename = f"Store{''.join(random.choices(string.ascii_letters + string.digits, k=8))}"
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Name']", storename)
        actualstorename_value = storename.strip()
        print("StoreName is:", actualstorename_value)
        time.sleep(2)
        random_number = str(random.randint(1111111, 9999999))
        phonenumber = f"{555}{random_number}"
        wait_and_send_keys(login, By.XPATH, "//input[@id='phone']", phonenumber)
        time.sleep(2)
        email = f"{storename}{test_mail}"
        wait_and_send_keys(login, By.XPATH, "//input[@id='email']", email)
        time.sleep(2)
        invoice_prefix = "S-" + str(uuid.uuid4())[:2]
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Invoice prefix']", invoice_prefix)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Location']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Round North']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Online Self Order']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='No']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Walk-in-POS']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Yes']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Create']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        login.refresh()
        time.sleep(3)
        stores = login.find_element(By.XPATH, "//tbody/tr[1]")
        storetext = stores.text
        storename_before_id = storetext.split("Id:")[0]
        expectedstorename_value = storename_before_id.strip()
        print("StoreName is:", expectedstorename_value)
        print(f"Expected Storename: '{expectedstorename_value}', Actual Storename: '{actualstorename_value}'")
        assert actualstorename_value == expectedstorename_value, f"Expected Storename: {storename_before_id} but got Storename {actualstorename_value}"
        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Store_Online_POS Enabled")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_store_Online_POS(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//img[contains(@src, 'settings.gif')]//following::div[contains(text(),'Settings')]")
        time.sleep(2)
        POS = wait_and_locate_click(login, By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(login, POS)       
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p[normalize-space()='Sales Order Management System']")
        time.sleep(2)
        Sales_order = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']")) 
            )
        aria_checked = Sales_order.get_attribute("aria-checked")
        if aria_checked == "true":
            print("Sales Orders Management is already active, no need to click.")
        else:
            Sales_order.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Stores')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create Store']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Type']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Pharmacy']")
        time.sleep(2)
        storename = f"Store{''.join(random.choices(string.ascii_letters + string.digits, k=8))}"
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Name']", storename)
        actualstorename_value = storename.strip()
        print("StoreName is:", actualstorename_value)
        time.sleep(2)
        random_number = str(random.randint(1111111, 9999999))
        phonenumber = f"{555}{random_number}"
        wait_and_send_keys(login, By.XPATH, "//input[@id='phone']", phonenumber)
        time.sleep(2)
        email = f"{storename}{test_mail}"
        wait_and_send_keys(login, By.XPATH, "//input[@id='email']", email)
        time.sleep(2)
        invoice_prefix = "S-" + str(uuid.uuid4())[:2]
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Invoice prefix']", invoice_prefix)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Location']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Round North']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Online Self Order']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Yes']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Walk-in-POS']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='No']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Create']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
        login.refresh()
        time.sleep(3)
        stores = login.find_element(By.XPATH, "//tbody/tr[1]")
        storetext = stores.text
        storename_before_id = storetext.split("Id:")[0]
        expectedstorename_value = storename_before_id.strip()
        print("StoreName is:", expectedstorename_value)
        print(f"Expected Storename: '{expectedstorename_value}', Actual Storename: '{actualstorename_value}'")
        assert actualstorename_value == expectedstorename_value, f"Expected Storename: {storename_before_id} but got Storename {actualstorename_value}"
        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    


@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
@allure.title("Store Active Filter")
def test_Store_Activefilter(login):

    try:
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Stores')]") 
        time.sleep(2)

        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//i[@class='pi pi-filter-fill']"))
        ).click()
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Status']"))
        ).click()
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='text-left p-dropdown p-component'])[4]"))
        ).click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[@aria-label='Active']"))
        ).click()
          
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Apply']"))
        ).click()
        time.sleep(5)
        table_body = WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//tbody")
            )
        )
        table_rows = table_body.find_elements(By.XPATH, ".//tr")

       
        for row in table_rows:
          
            store_status = row.find_element(By.XPATH, "//tbody/tr/td[@class='desktop-only']//div[@class='active ng-star-inserted']").text
            assert store_status == "Active", f"Store Status '{store_status}' does not match the filter 'Active'"

        

        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//i[@class='pi pi-filter-fill']"))
        ).click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@aria-label='dropdown trigger'])[4]"))
        ).click()


        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Inactive']"))
        ).click()
        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Apply']"))
        ).click()
        time.sleep(3)
        table_body = WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//tbody")
            )
        )

       
        table_rows = table_body.find_elements(By.XPATH, ".//tr")
        for row in table_rows:
           
            store_status = row.find_element(By.XPATH, "//tbody/tr/td[@class='desktop-only']//div[@class='inactive ng-star-inserted']").text
            assert store_status == "Inactive", f"Store Status '{store_status}' does not match the filter 'Inactive'"

    except Exception as e: 
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e 
    
