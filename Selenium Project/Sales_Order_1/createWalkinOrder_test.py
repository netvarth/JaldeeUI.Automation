
from Framework.common_utils import *
from Framework.common_dates_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_WalkinOrder_confirmed and completed_order")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_walkin_Order(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search customers']", "5550004454")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 1']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[2]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        time.sleep(2)
        confirmorder.click()
        time.sleep(5)
        confirmedorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )
        actual_message = confirmedorder.text
        expected_message = "Confirmed"
        print(f"Expected status: '{expected_message}', Actual status: '{actual_message}'")
        assert actual_message == expected_message, f"Expected message '{expected_message} but got Message '{actual_message}'"
        complete_Order = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Complete Order']"))
        )
        scroll_to_element(login, complete_Order)
        time.sleep(2)
        complete_Order.click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        print("Toast Message:", toast_message.text)
        expected_message = "Order Completed Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{toast_message.text}'")
        assert toast_message.text == expected_message, f"Expected toast message '{expected_message}', but got '{toast_message.text}'"
        time.sleep(5)
        create_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Invoice']"))
        )
        create_Invoice.click()
        time.sleep(3)
        view_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='View Invoice']"))
        )
        scroll_to_element(login, view_Invoice)
        view_Invoice.click()
        time.sleep(3)
        paymentlink = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        scroll_to_element(login, paymentlink)
        paymentlink.click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[@aria-label='Share Payment Link']")
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "The invoice has been sent to the customer"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_WalkinOrder_confirmed and canceled_order")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_walkin_confirmed_canceled_Order(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='New customer']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//mat-select[@placeholder='Select']")
        time.sleep(3)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        salutation_option_element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, salutation_option_xpath))
        )
        salutation_option_element.click()
        time.sleep(3)
        first_name, last_name, phonenumber, email = create_users_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='mobileNumber']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//span[normalize-space()='Save']").click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[2]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        confirmorder.click()
        time.sleep(5)
        confirmedorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )
        actual_message = confirmedorder.text
        expected_message = "Confirmed"
        print(f"Expected status: '{expected_message}', Actual status: '{actual_message}'")
        assert actual_message == expected_message, f"Expected message '{expected_message} but got Message '{actual_message}'"
        time.sleep(2)
        cancelorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Cancel Order']"))
        )
        scroll_to_element(login, cancelorder)
        cancelorder.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(2)
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        print("Toast Message:", toast_message.text)
        expected_message = "Order Cancelled Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{toast_message.text}'")
        assert toast_message.text == expected_message, f"Expected toast message '{expected_message}', but got '{toast_message.text}'"
        # print("Test passed:", toast_message.text)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_WalkinOrder_confirmed")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_walkin_Confirm_Order(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search customers']", "5550004454")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 1']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[2]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        confirmorder.click()
        time.sleep(5)
        confirmedorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )
        actual_message = confirmedorder.text
        expected_message = "Confirmed"
        print(f"Expected status: '{expected_message}', Actual status: '{actual_message}'")
        assert actual_message == expected_message, f"Expected message '{expected_message} but got Message '{actual_message}'"
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_WalkinOrder_canceled_order")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_walkin_canceled_Order(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='New customer']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//mat-select[@placeholder='Select']")
        time.sleep(3)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        salutation_option_element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, salutation_option_xpath))
        )
        salutation_option_element.click()
        time.sleep(3)
        first_name, last_name, phonenumber, email = create_users_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='mobileNumber']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//span[normalize-space()='Save']").click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        cancelorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Cancel']"))
        )
        scroll_to_element(login, cancelorder)
        cancelorder.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_WalkinOrder_saveasdraft and Discard Order")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_walkin_saveasdraft_discard_Order(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='New customer']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//mat-select[@placeholder='Select']")
        time.sleep(3)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        salutation_option_element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, salutation_option_xpath))
        )
        salutation_option_element.click()
        time.sleep(3)
        first_name, last_name, phonenumber, email = create_users_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='mobileNumber']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//span[normalize-space()='Save']").click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[2]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        saveasdraft = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Save as draft']"))
        )
        scroll_to_element(login, saveasdraft)
        saveasdraft.click()
        time.sleep(5)
        saveasdraft = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Draft ng-star-inserted']"))
        )
        actual_message = saveasdraft.text
        expected_message = "Draft"
        print(f"Expected status: '{expected_message}', Actual status: '{saveasdraft.text}'")
        assert actual_message == expected_message, f"Expected message '{expected_message}' but got Message '{actual_message}'"
        time.sleep(2)
        discardorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Discard Order']"))
        )
        scroll_to_element(login, discardorder)
        discardorder.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(2)
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        print("Toast Message:", toast_message.text)
        expected_message = "Order Discarded Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{toast_message.text}'")
        assert toast_message.text == expected_message, f"Expected toast message '{expected_message}', but got '{toast_message.text}'"
        # print("Test passed:", toast_message.text)
        time.sleep(2)
        discarded = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Canceled ng-star-inserted']"))
        )
        actual_message = discarded.text
        expected_message = "Discarded"
        print(f"Expected status: '{expected_message}', Actual status: '{discarded.text}'")
        assert actual_message == expected_message, f"Expected message '{expected_message} but got Message '{actual_message}'"
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_WalkinOrder_Saveasdraft and confirmed Order")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_walkin_Saveasdraft_Confirm_Order(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='New customer']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//mat-select[@placeholder='Select']")
        time.sleep(3)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        salutation_option_element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, salutation_option_xpath))
        )
        salutation_option_element.click()
        time.sleep(3)
        first_name, last_name, phonenumber, email = create_users_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='mobileNumber']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//span[normalize-space()='Save']").click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[2]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        saveasdraft = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Save as draft']"))
        )
        scroll_to_element(login, saveasdraft)
        time.sleep(2)
        saveasdraft.click()
        time.sleep(5)
        saveasdraft = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Draft ng-star-inserted']"))
        )
        actual_message = saveasdraft.text
        expected_message = "Draft"
        print(f"Expected status: '{expected_message}', Actual status: '{saveasdraft.text}'")
        assert actual_message == expected_message, f"Expected message '{expected_message} but got Message '{actual_message}'"
        time.sleep(2)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        time.sleep(2)
        confirmorder.click()
        time.sleep(5)
        confirmedorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )
        actual_message = confirmedorder.text
        expected_message = "Confirmed"
        print(f"Expected status: '{expected_message}', Actual status: '{actual_message}'")
        assert actual_message == expected_message, f"Expected message '{expected_message} but got Message '{actual_message}'"
        complete_Order = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Complete Order']"))
        )
        scroll_to_element(login, complete_Order)
        time.sleep(2)
        complete_Order.click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        print("Toast Message:", toast_message.text)
        expected_message = "Order Completed Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{toast_message.text}'")
        assert toast_message.text == expected_message, f"Expected toast message '{expected_message}', but got '{toast_message.text}'"
        time.sleep(5)
        create_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Invoice']"))
        )
        create_Invoice.click()
        time.sleep(3)
        view_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='View Invoice']"))
        )
        scroll_to_element(login, view_Invoice)
        view_Invoice.click()
        time.sleep(3)
        paymentlink = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        scroll_to_element(login, paymentlink)
        paymentlink.click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[@aria-label='Share Payment Link']")
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "The invoice has been sent to the customer"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_WalkinOrder_Saveasdraft _Edit order and additems and confirmed_Order")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_walkin_Saveasdraft_Edit_Confirm_Order(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='New customer']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//mat-select[@placeholder='Select']")
        time.sleep(3)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        salutation_option_element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, salutation_option_xpath))
        )
        salutation_option_element.click()
        time.sleep(3)
        first_name, last_name, phonenumber, email = create_users_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='mobileNumber']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//span[normalize-space()='Save']").click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[2]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        saveasdraft = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Save as draft']"))
        )
        scroll_to_element(login, saveasdraft)
        time.sleep(2)
        saveasdraft.click()
        time.sleep(5)
        saveasdraft = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Draft ng-star-inserted']"))
        )
        actual_message = saveasdraft.text
        expected_message = "Draft"
        print(f"Expected status: '{expected_message}', Actual status: '{saveasdraft.text}'")
        assert actual_message == expected_message, f"Expected message '{expected_message} but got Message '{actual_message}'"
        time.sleep(2)
        Editorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Edit Order']"))
        )
        Editorder.click()
        time.sleep(2)
        Additem = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Add Item']"))
        )
        Additem.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[3]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        updateorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Update Order']"))
        )
        scroll_to_element(login, updateorder)
        time.sleep(2)
        updateorder.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(2)
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        print("Toast Message:", toast_message.text)
        expected_message = "Order Updated Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{toast_message.text}'")
        assert toast_message.text == expected_message, f"Expected toast message '{expected_message}', but got '{toast_message.text}'"
        time.sleep(2)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        time.sleep(2)
        confirmorder.click()
        time.sleep(5)
        confirmedorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )
        actual_message = confirmedorder.text
        expected_message = "Confirmed"
        print(f"Expected status: '{expected_message}', Actual status: '{actual_message}'")
        assert actual_message == expected_message, f"Expected message '{expected_message} but got Message '{actual_message}'"
        complete_Order = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Complete Order']"))
        )
        scroll_to_element(login, complete_Order)
        time.sleep(2)
        complete_Order.click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        print("Toast Message:", toast_message.text)
        expected_message = "Order Completed Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{toast_message.text}'")
        assert toast_message.text == expected_message, f"Expected toast message '{expected_message}', but got '{toast_message.text}'"
        time.sleep(5)
        create_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Invoice']"))
        )
        create_Invoice.click()
        time.sleep(3)
        view_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='View Invoice']"))
        )
        scroll_to_element(login, view_Invoice)
        view_Invoice.click()
        time.sleep(3)
        paymentlink = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        scroll_to_element(login, paymentlink)
        paymentlink.click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[@aria-label='Share Payment Link']")
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "The invoice has been sent to the customer"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

   


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_WalkinOrder_with NotesFromProvider and NotesTOCustomer.")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_walkin_Notes(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='New customer']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//mat-select[@placeholder='Select']")
        time.sleep(3)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//div[normalize-space()='{salutation}']"
        salutation_option_element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, salutation_option_xpath))
        )
        salutation_option_element.click()
        time.sleep(3)
        first_name, last_name, phonenumber, email = create_users_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='mobileNumber']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//span[normalize-space()='Save']").click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[2]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Notes to customer']")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//textarea[@placeholder='Enter Notes ( Max : 500 chars )']", "Item is ready to be delivered")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Notes from staff member']")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//textarea[@placeholder='Enter Notes ( Max : 500 chars )']", "Item is ready to be shipped")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
        time.sleep(3)
        confirmorder.click()
        time.sleep(3)
        confirmed_order = WebDriverWait(login, 15).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )
        actual_message = confirmed_order.text
        expected_message = "Confirmed"
        print(f"Expected status: '{expected_message}', Actual status: '{actual_message}'")
        assert actual_message == expected_message, f"Expected message '{expected_message} but got Message '{actual_message}'"
        time.sleep(3)
        complete_Order = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Complete Order']"))
        )
        scroll_to_element(login, complete_Order)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Notes to customer']")
        time.sleep(2)
        Custnotes = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='prescription-notes-order-creation ng-star-inserted']"))
        )
        customernotes = Custnotes.text.strip()
        print(customernotes)
        ExpectedCustomernotes = "Item is ready to be delivered"
        time.sleep(3)
        print(f"Expected Customernotes: '{ExpectedCustomernotes}', Actual Customernotes: '{customernotes}'")
        assert customernotes == ExpectedCustomernotes, f"Expected Customernotes: '{ExpectedCustomernotes}', Actual Customernotes: '{customernotes}'"
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-times']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@type='button'])[2]")
        time.sleep(2)
        Provnotes = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='prescription-notes-order-creation ng-star-inserted']"))
        )
        providernotes = Provnotes.text.strip()
        print(providernotes)
        ExpectedProvidernotes = "Item is ready to be shipped"
        print(f"Expected Providernotes: '{ExpectedProvidernotes}', Actual Providernotes: '{providernotes}'")
        assert providernotes == ExpectedProvidernotes, f"Expected Providernotes: '{ExpectedProvidernotes}', Actual Providernotes: '{providernotes}'"
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-times']")
        time.sleep(2)
        complete_Order.click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        print("Toast Message:", toast_message.text)
        expected_message = "Order Completed Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{toast_message.text}'")
        assert toast_message.text == expected_message, f"Expected toast message '{expected_message}', but got '{toast_message.text}'"
        time.sleep(5)
        create_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Invoice']"))
        )
        create_Invoice.click()
        time.sleep(3)
        view_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='View Invoice']"))
        )
        scroll_to_element(login, view_Invoice)
        view_Invoice.click()
        time.sleep(3)
        paymentlink = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        scroll_to_element(login, paymentlink)
        paymentlink.click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[@aria-label='Share Payment Link']")
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "The invoice has been sent to the customer"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_WalkinOrder_ with searching an item and Increasing Its Quantity")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_walkin_Order_Increased_Item_Quantity(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search customers']", "5550004454")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 1']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        # Add items
        search_items_names_to_select = ['Gulab jamun']
        item_prices = [800]
        sum = 0
        search_items_data_before_confirm = []
        for i in range(len(search_items_names_to_select)):
            item_name = search_items_names_to_select[i]
            item_price = item_prices[i]
            print(item_name)
            # Search and select item
            WebDriverWait(login, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search items']"))
            ).send_keys(item_name)

            item_xpath = f"//div[contains(text(), '{item_name}')]"

            WebDriverWait(login, 10).until(EC.presence_of_element_located( (By.XPATH, item_xpath))
            ).click()
            qty_xpath = f"(//input[@min='1'])[{i + 1}]"
            qty = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, qty_xpath))
            )
            qty.click()
            qty.clear()
            qty_random_number = str(random.randint(3, 5))
            qty.send_keys(qty_random_number)
            print("Qty Of Item:", qty_random_number)

            # Calculate total for each item
            total = item_price * float(qty_random_number)
            print("total:", total)
            sum += total
            print("sum: ", sum)
            # Capture row data
            row_xpath = f"//tbody[@class='p-element p-datatable-tbody']/tr[{i + 1}]"
            print(row_xpath)
            row = login.find_element(By.XPATH, row_xpath)
            columns = row.find_elements(By.TAG_NAME, "td")
            item_total_text = columns[4].text.strip()

            # Save item data before confirmation
            search_items_data_before_confirm.append({
                'item_name': item_name,
                'qty': qty_random_number,
                'price': item_price,
                'total': item_total_text
            })

        time.sleep(5)

        # Verify the summary total
        summary_total_element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='fw-bold mt-2']//span[@class='min-width-span-value']"))
        )

        summary_total_text = summary_total_element.text.replace('₹', '').replace(',', '').strip()
        summary_total = float(summary_total_text)

        print(f"Expected Total Sum: {sum:.2f}")
        print(f"Actual Summary Total: {summary_total:.2f}")

        # Perform the final assertion for the total
        assert round(sum, 2) == round(summary_total, 2), f"Expected Summary Total to be {sum:.2f}, but got '{summary_total_text}'"

        # Step 2: Press "Confirm Order" button
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm Order']"))
        ).click()

        # Step 3: Capture the item details after pressing "Confirm Order"
        search_items_data_after_confirm = []

        for i in range(len(search_items_names_to_select)):
            row_xpath = f"//tbody[@class='p-element p-datatable-tbody']/tr[{i + 1}]"
            row = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, row_xpath))
            )

            columns = row.find_elements(By.TAG_NAME, "td")
            item_total_text = columns[4].text.strip()
            qty_confirmed = login.find_element(By.XPATH, f"(//input[@min='1'])[{i + 1}]").get_attribute('value')

            search_items_data_after_confirm.append({
                'item_name': search_items_names_to_select[i],
                'qty': qty_confirmed,
                'price': item_prices[i],
                'total': item_total_text
            })

        # Step 4: Compare the item details before and after confirming the order
        for before, after in zip(search_items_data_before_confirm, search_items_data_after_confirm):
            assert before == after, f"Mismatch found! Before: {before}, After: {after}"

        print("Order confirmation data matches successfully.")
        WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Complete Order']"))
        ).click()

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//i[@class='pi pi-arrow-left']"))
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Orders'])[1]"))
        ).click()


        time.sleep(2)
        # Wait for the table to be present
        table_body = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody"))
        )

        # Locate the first table row
        first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")

        # Find the status element within the first row
        status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
        status_text = status_element.text
        expected_status = "Completed"

        print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

        # Assert that the status is "Completed"
        assert status_text == "Completed", f"Expected status to be 'Completed', but got '{status_text}'"

        time.sleep(5)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_WalkinOrder_confirmed and completed_order and applied Discount ")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_walkin_Order_discount(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search customers']", "5550004454")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 1']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[2]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        time.sleep(2)
        confirmorder.click()
        time.sleep(5)
        create_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Invoice']"))
        )
        create_Invoice.click()
        time.sleep(3)
        add_discount = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//th[@class='btn btn-primary ng-star-inserted']"))
        )
        scroll_to_element(login, add_discount)
        add_discount.click()
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        ).click()
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='On Demand Discount']"))
        ).click()
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter amount']", "100")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//textarea[@placeholder='Private note']", "Apply on demand discount 100 Rupees")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//textarea[@placeholder='Notes for customer']", "Applied On Demand Discount 100 Rupees")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Apply']")
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(2)
        confirmedorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )
        actual_message = confirmedorder.text
        expected_message = "Confirmed"
        print(f"Expected status: '{expected_message}', Actual status: '{actual_message}'")
        assert actual_message == expected_message, f"Expected message '{expected_message} but got Message '{actual_message}'"
        complete_Order = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Complete Order']"))
        )
        scroll_to_element(login, complete_Order)
        time.sleep(2)
        complete_Order.click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        print("Toast Message:", toast_message.text)
        expected_message = "Order Completed Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{toast_message.text}'")
        assert toast_message.text == expected_message, f"Expected toast message '{expected_message}', but got '{toast_message.text}'"
        time.sleep(5)
        
        view_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='View Invoice']"))
        )
        scroll_to_element(login, view_Invoice)
        view_Invoice.click()
        time.sleep(3)
        paymentlink = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        scroll_to_element(login, paymentlink)
        paymentlink.click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[@aria-label='Share Payment Link']")
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "The invoice has been sent to the customer"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_WalkinOrder_confirmed and completed_order and applied coupon ")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_walkin_Order_Coupon(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search customers']", "5550004454")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 1']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[2]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        time.sleep(2)
        confirmorder.click()
        time.sleep(5)
        create_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Invoice']"))
        )
        create_Invoice.click()
        time.sleep(3)
        add_coupon = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//th[@class='btn btn-primary ms-2'])[1]"))
        )
        scroll_to_element(login, add_coupon)
        add_coupon.click()
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        ).click()
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Christmas']"))
        ).click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Apply']")
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(3)
        confirmedorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )
        actual_message = confirmedorder.text
        expected_message = "Confirmed"
        print(f"Expected status: '{expected_message}', Actual status: '{actual_message}'")
        assert actual_message == expected_message, f"Expected message '{expected_message} but got Message '{actual_message}'"
        complete_Order = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Complete Order']"))
        )
        scroll_to_element(login, complete_Order)
        time.sleep(2)
        complete_Order.click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        print("Toast Message:", toast_message.text)
        expected_message = "Order Completed Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{toast_message.text}'")
        assert toast_message.text == expected_message, f"Expected toast message '{expected_message}', but got '{toast_message.text}'"
        time.sleep(5)
        
        view_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='View Invoice']"))
        )
        scroll_to_element(login, view_Invoice)
        view_Invoice.click()
        time.sleep(3)
        paymentlink = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        scroll_to_element(login, paymentlink)
        paymentlink.click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[@aria-label='Share Payment Link']")
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        expected_message = "The invoice has been sent to the customer"
        print(f"Expected status: '{expected_message}', Actual status: '{message}'")
        assert message == expected_message, f"Expected message '{expected_message} but got Message '{message}'"
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

    
    