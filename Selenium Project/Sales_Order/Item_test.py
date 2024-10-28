from webbrowser import get
from Framework.common_utils import *
from Framework.common_dates_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Item")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_Item(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Items']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create']") 
        time.sleep(2)
        item_name = "Item_" + str(uuid.uuid4())[:4]
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Item Name']", item_name) 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Select Item Property']//div[@aria-label='dropdown trigger']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Other']") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//textarea[@placeholder='Enter Item Description']", "The Desserts") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Select Category']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Dessert']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Select Group')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Sweets']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Select Type']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[@aria-label='Cultural']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Select Manufacturer']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Nestlé']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Select Unit')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Numbers']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Select HSN Code']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='1704']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Select Item Compositions')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Sugar']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Select Item Tax')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='GST 18%']") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter SKU']", "1704-001-CHO-500G") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create Item']") 
        time.sleep(3)
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Search_Item_View_And_Enabled_Disabled_Alternatively")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_search_Item(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Items']") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search Item with name']", "Icecream")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-icon pi pi-search']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Actions']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@role='menuitem'])[1]")
        time.sleep(2)
        try:
            itemdisable_button = WebDriverWait(login, 10).until(
                                EC.element_to_be_clickable((By.XPATH, "//p-button[@class='p-element disable-btn ng-star-inserted']"))
                            )
            itemdisable_button.click()
            toast_detail = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
            )
            message = toast_detail.text
            print("toast_Message:", message)
            wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
            time.sleep(2)
            wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search Item with name']", "Icecream")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-icon pi pi-search']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Actions']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[3]")
            time.sleep(2)
            toast_detail = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
            )
            message = toast_detail.text
            print("toast_Message:", message)
        except:
            itemenable_button = WebDriverWait(login, 10).until(
                                EC.element_to_be_clickable((By.XPATH, "//span[@class='p-button-label ng-star-inserted']"))
                            )
            itemenable_button.click()
            toast_detail = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
            )
            message = toast_detail.text
            print("toast_Message:", message)
            time.sleep(3)
            wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']")
            time.sleep(2)
            wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search Item with name']", "Icecream")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-icon pi pi-search']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Actions']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[3]")
            time.sleep(2)
            toast_detail = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
            )
            message = toast_detail.text
            print("toast_Message:", message)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Item Updation")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_edit_Item(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Items']") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search Item with name']", "Icecream")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-icon pi pi-search']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Actions']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@role='menuitem'])[1]")
        time.sleep(2)   
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Edit']")
        time.sleep(2)
        item_description = f"Item{''.join(random.choices(string.ascii_letters + string.digits, k=8))}"
        wait_and_send_keys(login, By.XPATH, "//textarea[@placeholder='Enter Item Description']", item_description)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@type='submit']")
        toast_detail = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
            )
        message = toast_detail.text
        print("toast_Message:", message)

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Item_Filters")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Item_Filters(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Items']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[1]") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@id='name']", "Rasmalai") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[2]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'Select Item Property')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Other']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[4]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'Select Status')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Enabled']") 
        time.sleep(2)
        scroll_to_window(login)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[5]") 
        time.sleep(2)
        scroll_to_window(login)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Select Category')]") 
        time.sleep(2)
        scroll_to_window(login)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Dessert']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Apply']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Reset']") 
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
    
    

    