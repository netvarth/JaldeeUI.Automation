from Framework.common_utils import *
from Framework.common_dates_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("item_Variants")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Orders(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Item Variants')]") 
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Categories')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-label']") 
        time.sleep(2)
        Category = "Category_" + str(uuid.uuid4())[:8]
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Category Name']", Category)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-label'][normalize-space()='Create Category']") 
        time.sleep(2)
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Item Variants')]") 
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Groups')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create']") 
        time.sleep(2)
        Group_name = "Group_" + str(uuid.uuid4())[:8]
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Group Name']", Group_name)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-label'][normalize-space()='Create Group']") 
        time.sleep(2)
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Item Variants')]") 
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Types')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create']") 
        time.sleep(2)
        Type_name = "Type_" + str(uuid.uuid4())[:8]
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Type Name']", Type_name)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-label'][normalize-space()='Create Type']") 
        time.sleep(2)
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Item Variants')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Manufacturers')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create']") 
        time.sleep(2)
        Manufacture_name = "Manufacturer_" + str(uuid.uuid4())[:8]
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Manufacturer Name']", Manufacture_name)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-label'][normalize-space()='Create Manufacturer']") 
        time.sleep(2)
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Item Variants')]") 
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Units')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create']") 
        time.sleep(2)
        units = ['meters', 'kilometers', 'grams', 'kilograms', 'liters', 'milliliters']
        random_unit = random.choice(units)
        unique_id = str(uuid.uuid4())[:6]
        unit_name = f"{random_unit}_{unique_id}"
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Unit Name']", unit_name)
        time.sleep(2)
        quantity = random.randint(1, 100)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Unit Convertion Quantity']", quantity)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-label'][normalize-space()='Create Unit']") 
        time.sleep(2)
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Item Variants')]") 
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Compositions')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create']") 
        time.sleep(2)
        Composition_name = "Composition_" + str(uuid.uuid4())[:8]
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Composition Name']", Composition_name)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-label'][normalize-space()='Create Composition']") 
        time.sleep(2)
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Item Variants')]") 
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'HSN Codes')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create']") 
        time.sleep(2)
        HSN_code = random.randint(1000, 9999)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter HSN Code']", HSN_code)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-label'][normalize-space()='Create HSN']") 
        time.sleep(2)
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-arrow-left']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Item Variants')]") 
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Remarks')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create']") 
        time.sleep(2)
        Remark_name = "Remark_" + str(uuid.uuid4())[:8]
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Remark Name']", Remark_name)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']") 
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[@aria-label='Sales Order']//span[@class='ng-star-inserted'][normalize-space()='Sales Order']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-label'][normalize-space()='Create Remark']") 
        time.sleep(2)
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(2)


    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  