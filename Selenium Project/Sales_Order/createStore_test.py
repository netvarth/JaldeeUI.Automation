from Framework.common_utils import *
from Framework.common_dates_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Store")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_store(login):
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
        time.sleep(2)
        random_number = str(random.randint(1111111, 9999999))
        phonenumber = f"{555}{random_number}"
        wait_and_send_keys(login, By.XPATH, "//input[@id='phone']", phonenumber)
        time.sleep(2)
        email = f"{storename}{test_mail}"
        wait_and_send_keys(login, By.XPATH, "//input[@id='email']", email)
        time.sleep(2)
        invoice_prefix = "S-" + str(uuid.uuid4())[:2]
        print(invoice_prefix)
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
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  