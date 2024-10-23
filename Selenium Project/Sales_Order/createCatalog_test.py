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