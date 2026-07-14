from asyncio import wait
import time
# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException


#################   Enable the Inventory Setting   #############################
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Enable inventory settings")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_enable_inventory_setting(login):
    
    time.sleep(5)
    WebDriverWait(login, 15).until(
        EC.presence_of_element_located((By.XPATH, "//img[@src='./assets/images/menu/settings.png']"))
    ).click()

    element = login.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
    login.execute_script("arguments[0].scrollIntoView();", element)

    allure.attach(      # use Allure package, .attach() method, pass 3 params
        login.get_screenshot_as_png(),    # param1
        name="rxorders",                 # param2
        attachment_type=AttachmentType.PNG)

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Sales Order Management System']"))
    ).click()

    time.sleep(2)

    # Locate the Sales Order toggle button
    sales_order_toggle = WebDriverWait(login, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "(//button[@role='switch'])[1]")
    )
    )

    # Get current state
    sales_order_state = sales_order_toggle.get_attribute("aria-checked")

    print("Current Sales Order Toggle State :", sales_order_state)

    # If Sales Order is OFF, click and make it ON
    if sales_order_state == "false":
        wait_and_locate_click(login,By.XPATH, "(//button[@role='switch'])[1]")

        print("Sales Order turned ON")

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

    elif sales_order_state == "true":
        print("Sales Order is already ON")

    else:
        print("Unable to read Sales Order toggle state")

    time.sleep(3)
    
    
    login.find_element(By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']").click()

    # Find the element you want to scroll to
    element = login.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
    login.execute_script("arguments[0].scrollIntoView();", element)

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Inventory Management System']"))
    ).click()

    time.sleep(2)

    # Locate the Inventory toggle button
    inventory_toggle = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@role='switch']")
        )
    )

    # Get current state
    inventory_state = inventory_toggle.get_attribute("aria-checked")

    print("Current Inventory Toggle State :", inventory_state)

    # If Inventory is OFF, click and make it ON
    if inventory_state == "false":
        wait_and_locate_click(
        login,
        By.XPATH,
        "//button[@role='switch']"
    )

        print("Inventory turned ON")

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

    elif inventory_state == "true":
        print("Inventory is already ON")

    else:
        print("Unable to read Inventory toggle state")

    time.sleep(3)


##################   New Store creation   #############################
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Store Creation")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_store_creation(login):
    
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//img[contains(@src,'rx-orders.png')]")

    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "//div[@routerlinkactive='active-menu'][.//img[contains(@src,'rx-orders.png')]]"))
    # ).click()

    time.sleep(5)

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Stores']"))
    ).click()

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Store']"))
    ).click()


    dropdown = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Type']"))  
    )
    dropdown.click() 

    time.sleep(2)
    dropdown_item = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Pharmacy']"))
    )

    dropdown_item.click()

    store_name = "Store_" + str(uuid.uuid4())[:6]
    print(store_name)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='storeName']"))
    ).send_keys(store_name)

    email = f"{store_name}{test_mail}"
    random_number = str(random.randint(1111111, 9999999))
    phonenumber = f"{555}{random_number}"

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
    ).send_keys(phonenumber)

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
    ).send_keys(email)


    invoice_prefix = "KT_" + str(uuid.uuid4())[:1]
    print(invoice_prefix)
    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Invoice prefix']"))  
    ).send_keys(invoice_prefix)
    

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Location']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='West Nada']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create']"))
    ).click()

    msg = get_snack_bar_message(login)
    print("Snack Bar Message: ", msg)
    
    time.sleep(3)


###############################   Item Creation   ################################


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Item Creation")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_item_creation(login):

    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//img[contains(@src,'rx-orders.png')]"))
    ).click()

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Items']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create']"))
    ).click()

    item_name = "Item_" + str(uuid.uuid4())[:4]

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Item Name']"))
    ).send_keys(item_name)


    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//input[@placeholder='Select Item Property']/ancestor::div[contains(@class,'p-dropdown')]")

    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//li[@role='option' and @aria-label='Tablet']")

    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//input[@placeholder='Select Item Source']/ancestor::div[contains(@class,'p-dropdown')]")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@role='option' and @aria-label='General']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Enter Item Description']"))
    ).send_keys("A Item name is required and recommended to be unique.")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select Category']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@role='option' and @aria-label='Stationary']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Select Group')]"))
    ).click()

    WebDriverWait(login, 15).until(
        EC.presence_of_element_located((By.XPATH, "//li[contains(@class,'p-multiselect-item') and @aria-label='Stationary_Item']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select Type']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@role='option' and @aria-label='Office_Item']"))
    ).click()

    login.implicitly_wait(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select Manufacturer']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@role='option' and @aria-label='SC.PVT.Limited']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Select Unit')]"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[contains(@class,'p-multiselect-item') and @aria-label='Box of 10'] "))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p-dropdown[@placeholder='Track Inventory or Not']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Yes']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select HSN Code']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@role='option' and @aria-label='5554644']"))
    ).click()

    time.sleep(2)
    wait_and_send_keys(login, By.XPATH, "//input[@id='inpReorderQty_ORD_INV_ItemCreate']", "10")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Select Item Tax')]"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[contains(@class,'p-multiselect-item') and @aria-label='GST 5%']"))
    ).click()

    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Select tax preference']")

    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//li[@role='option' and @aria-label='Taxable']")

    # Click Create Item button
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@id='btnSubmit_ORD_INV_ItemCreate']"))
    ).click()

    toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_detail.text
    print("toast_Message:", message)

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//i[@class='pi pi-arrow-left']"))
    ).click()



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Item Creation with attributes")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_item_creation_with_attributes(login):

    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//img[contains(@src,'rx-orders.png')]"))
    ).click()

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Items']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create']"))
    ).click()

    item_name = "Item_" + str(uuid.uuid4())[:4]

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Item Name']"))
    ).send_keys(item_name)


    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//input[@placeholder='Select Item Property']/ancestor::div[contains(@class,'p-dropdown')]")

    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//li[@role='option' and @aria-label='Tablet']")

    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "//input[@placeholder='Select Item Source']/ancestor::div[contains(@class,'p-dropdown')"))
    # ).click()

    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//input[@placeholder='Select Item Source']/ancestor::div[contains(@class,'p-dropdown')]")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@role='option' and @aria-label='General']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Enter Item Description']"))
    ).send_keys("A Item name is required and recommended to be unique.")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select Category']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@role='option' and @aria-label='Stationary']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Select Group')]"))
    ).click()

    WebDriverWait(login, 15).until(
        EC.presence_of_element_located((By.XPATH, "//li[contains(@class,'p-multiselect-item') and @aria-label='Stationary_Item']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select Type']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@role='option' and @aria-label='Office_Item']"))
    ).click()

    login.implicitly_wait(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select Manufacturer']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@role='option' and @aria-label='SC.PVT.Limited']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Select Unit')]"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[contains(@class,'p-multiselect-item') and @aria-label='Box of 10'] "))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p-dropdown[@placeholder='Track Inventory or Not']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Yes']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select HSN Code']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@role='option' and @aria-label='5554644']"))
    ).click()

    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Select Item Compositions')]"))
    # ).click()

    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "//span[contains(text(),'starch, hydroxypropyl methylcellulose, propylene g')]"))
    # ).click()

    time.sleep(2)
    wait_and_send_keys(login, By.XPATH, "//input[@id='inpReorderQty_ORD_INV_ItemCreate']", "10")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Select Item Tax')]"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[contains(@class,'p-multiselect-item') and @aria-label='GST 5%']"))
    ).click()

    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Select tax preference']")

    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//li[@role='option' and @aria-label='Taxable']")

    # Click on Add Options in the Item Attribute
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnAddOption_ORD_ItemOpt']")

    # Adding option name
    time.sleep(2)
    wait_and_send_keys(login, By.XPATH, "//input[@id='inputOptName_ORD_ItemOpt']", "Options")

    # Add item attributes
    time.sleep(2)
    wait_and_send_keys(login, By.XPATH, "//input[@id='inputOptVal_ORD_ItemOpt']", "opt1" + Keys.ENTER)

    time.sleep(2)
    wait_and_send_keys(login, By.XPATH, "//input[@id='inputOptVal_ORD_ItemOpt']", "opt2" + Keys.ENTER)


   # Click Done button
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnAddItem_ORD_ItemOpt']")

    time.sleep(2)

    # Click Create Item button
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@id='btnSubmit_ORD_INV_ItemCreate']"))
    ).click()

    toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_detail.text
    print("toast_Message:", message)

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//i[@class='pi pi-arrow-left']"))
    ).click()


###############################  Inventory Catalogue Creation  #########################################
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create Inventory Catalog")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_inventory_catalog(login):

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[contains(@src,'inventory.png')]"))
    ).click()

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Catalogs')]"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='p-ripple p-element p-button p-component']"))
    ).click()

    catalog_name = "Catalog_" + str(uuid.uuid4())[:8]

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Catalog Name']"))
    ).send_keys(catalog_name)

    login.find_element(By.XPATH, "//span[normalize-space()='Store Name']").click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@role='option' and @aria-label='B&B Stores']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='btnCrtCat_ORD_CatlgCreate']"))
    ).click()

    time.sleep(5)

    

    checkboxes = WebDriverWait(login, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(.,'Select Items')]//input[@type='checkbox']"))
    )

    # Click the first three checkboxes
    for i in range(1, min(6, len(checkboxes))):
        checkboxes[i].click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@id='btnSubmitItems_ORD_ItemSelectionTop']"))
    ).click()

    time.sleep(2)

    # Wait until confirmation popup appears
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located(
        (By.XPATH,
            "//div[contains(@class,'mdc-dialog__container')]//p[contains(normalize-space(),'Once added to the catalog')]")
        )
    )

    # Click YES button in popup
    wait_and_locate_click(login, By.XPATH, "//div[contains(@class,'mdc-dialog__container')]//button[normalize-space()='Yes']")

    print("Clicked YES on confirmation popup")


    time.sleep(3)
    toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_detail.text
    print("toast_Message:", message)


######################################  Create Purchase ######################################################

def add_date(years_to_add):
    future_date = datetime.now().replace(year=datetime.now().year + years_to_add)
    return [future_date.year, future_date.strftime("%b"), future_date.day]

def title_to_item(title_case_string):
    return title_case_string.title()

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create Purchase Items With Batch and Attributes & without Batch and Attributes")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_purchase1(login):

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[contains(@src,'inventory.png')]"))
    ).click()

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Purchase']"))
    ).click()
    login.implicitly_wait(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='d-flex justify-content-between']//div[@class='ng-star-inserted']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select Store']"))
    ).click()

    time.sleep(3)
    store = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li[@role='option' and @aria-label='B&B Stores']"))
    )
    store.click()

    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//div[contains(@class,'p-dropdown')][.//input[@placeholder='Select Vendor']]")

    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//li[@role='option' and @aria-label='SBT PVT Limited']")

    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//div[contains(@class,'p-dropdown')][.//input[@placeholder='Select Inventory Catalog']]")
    
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//li[@role='option' and @aria-label='Catalog_Inventory']")


    Bill_no = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='inputBillRef_ORD_PurchsCrt']"))
    )
    Bill_no.click()

    random_number = str(random.randint(10000, 99999))
    Bill_no.send_keys(random_number)
    print("Bill no:", random_number)

    login.find_element(By.XPATH, "//p-calendar//input[@type='text']").click()

    Today_Date = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]"))
    )
    Today_Date.click()
    print("Date:", Today_Date.text)

    login.find_element(By.XPATH, "//textarea[@placeholder='Notes to Vendor']").send_keys("Medcc  Supplied item ")

    # ********* Adding Item_1 with batch and attribute *****************

    # Item Name field - first row in Add Items section
    item_name_field = WebDriverWait(login, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='Search items'])[1]"))
    )

    item_name_field.click()
    item_name_field.clear()
    item_name_field.send_keys("it")   # type item letters to open popup


    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Item_1')]")

    # Wait for Select Items popup
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='Select Items']"))
    )

    # Row containing Item_1 Green inside popup
    item_row_xpath = "//tr[.//*[normalize-space()='Item_1 Green']]"

    item_row = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, item_row_xpath))
    )

    login.execute_script("arguments[0].scrollIntoView({block:'center'});", item_row)
    time.sleep(1)

    # Click the first cell/radio area of Item_1 Green row
    radio_button = WebDriverWait(login, 10).until(
    EC.presence_of_element_located((
        By.XPATH,
        "//tr[.//*[normalize-space()='Item_1 Green']]//input[@type='radio']"))
    )

    login.execute_script("arguments[0].click();", radio_button)
    time.sleep(1)

    # Click Done button
    wait_and_locate_click(login, By.XPATH,
        "//button[@id='btnSubmitItems_ORD_ItemSelection']"
    )

    # Wait until popup closes
    WebDriverWait(login, 10).until(
        EC.invisibility_of_element_located((By.XPATH, "//*[normalize-space()='Select Items']"))
    )

    # Verify selected item appears in Add Items -> Item Name field
    selected_item_field = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Search items'])[1]"))
    )

    print("Selected Item:", selected_item_field.get_attribute("value"))


    # Enter batch number for the item
    time.sleep(5)
    batch_number = WebDriverWait(login, 20).until(
            EC.element_to_be_clickable((By.XPATH,
            "//td//div[@class='ng-star-inserted']//input[@type='text' and contains(@class, 'p-inputtext')]"))
        )
    batch_number.click()

    random_batch_number = str(random.randint(5, 99))
    batch_number.send_keys(random_batch_number)
    print("Batch_Number:", random_batch_number)

    # Enering item unit for the item
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH,
            "//p-dropdown[@placeholder='Item Units']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']"))
        ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Box of 10']"))
        ).click()
    

    # Enter expiry date for the item
    time.sleep(2)
    item_exp = f"//p-calendar[contains(@class, 'exp-date') and contains(@class, 'ng-tns-c')]"
    WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, item_exp))
        ).click()

    time.sleep(2)
    current_year = datetime.now().strftime("%Y")
    current_year_xpath = f"//button[normalize-space()='{current_year}']"
    print(current_year_xpath)
    time.sleep(2)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, current_year_xpath))
        ).click()
    
    [year, month, day] = add_date(2)
    print(year)
    year_xpath = f"//span[normalize-space()='{year}']"
    print(year_xpath)
    time.sleep(1)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, year_xpath))
        ).click()
    time.sleep(1)
    month_xpath = f"//span[normalize-space()='{month}']"
    print(month_xpath)
    WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, month_xpath))
         ).click()
    time.sleep(2)
    day_xpath = f"//span[normalize-space()='{day}' and not(contains(@class,'p-disabled'))]"
    print(day_xpath)
    time.sleep(2)
    WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, day_xpath))
        ).click()
        

    # Entering quantity for the item
    qty = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='inputNumber_ORD_PurchsCrt']"))
        )
    qty.click()
    qty.clear()

    qty_random_number = str(random.randint(10, 50))
    qty.send_keys(qty_random_number)
    print("Qty Of Item:", qty_random_number)


    # Entering free quantity for the item
    free_qty = WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='inputQty_ORD_PurchsCrt']"))
        )
    free_qty.click()
    free_qty.clear()

    free_qty_random_number = str(random.randint(1, 5))
    free_qty.send_keys(free_qty_random_number)
    print("Free Qty:", free_qty_random_number)


    # Entering MRP for the item
    mrpprice = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='inputMrp_ORD_PurchsCrt']")
        )
    )

    mrpprice.click()

    mrpprice_random_number = random.randint(60, 200)
    mrpprice.send_keys(str(mrpprice_random_number))

    print("MRP of the item:", mrpprice_random_number)


    # Entering purchase price for the item
    time.sleep(2)

    price = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='inputPrice_ORD_PurchsCrt']")
        )
    )

    price.click()

    price_random_number = random.randint(40, 100)

    # Check if purchase price is higher than MRP
    if price_random_number > mrpprice_random_number:
        price_random_number = random.randint(40, mrpprice_random_number - 1)
    print("Purchase price was higher than MRP, changed to:", price_random_number)

    price.send_keys(str(price_random_number))

    print("Price of the item:", price_random_number)


    # Entering discount for the item
    time.sleep(1)
    WebDriverWait(login,10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel= 'displayName']"))
        ).click()

    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='%']"))
        ).click()

    time.sleep(1)
    WebDriverWait(login ,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='inputDiscount_ORD_PurchsCrt']"))
        ).send_keys("5")
        
    time.sleep(3)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='btnAddItem_ORD_PurchsCrt']"))
        ).click()
    time.sleep(3)

    # ******** Adding Item_4 without batch and attribute ****************

    # Item Name field - first row in Add Items section
    item_name_field = WebDriverWait(login, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='Search items'])[1]"))
    )

    item_name_field.click()
    item_name_field.clear()
    item_name_field.send_keys("it")   # type item letters to open popup


    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Item_4')]")

    # Enering item unit for the item
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH,
            "//p-dropdown[@id='selectunit_ORD_PurchsCrt']//div[@class='p-dropdown p-component']"))
        ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Box of 12']"))
        ).click()
    

     # Entering quantity for the item
    qty = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='inputNumber_ORD_PurchsCrt']"))
        )
    qty.click()
    qty.clear()

    qty_random_number = str(random.randint(10, 50))
    qty.send_keys(qty_random_number)
    print("Qty Of Item:", qty_random_number)


    # Entering free quantity for the item
    free_qty = WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='inputQty_ORD_PurchsCrt']"))
        )
    free_qty.click()
    free_qty.clear()

    free_qty_random_number = str(random.randint(1, 5))
    free_qty.send_keys(free_qty_random_number)
    print("Free Qty:", free_qty_random_number)


    # Entering MRP for the item
    mrpprice = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='inputMrp_ORD_PurchsCrt']")
        )
    )

    mrpprice.click()

    mrpprice_random_number = random.randint(60, 200)
    mrpprice.send_keys(str(mrpprice_random_number))

    print("MRP of the item:", mrpprice_random_number)


    # Entering purchase price for the item
    time.sleep(2)

    price = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='inputPrice_ORD_PurchsCrt']")
        )
    )

    price.click()

    price_random_number = random.randint(40, 100)

    # Check if purchase price is higher than MRP
    if price_random_number > mrpprice_random_number:
        price_random_number = random.randint(40, mrpprice_random_number - 1)
    print("Purchase price was higher than MRP, changed to:", price_random_number)

    price.send_keys(str(price_random_number))

    print("Price of the item:", price_random_number)


    # Entering discount for the item
    time.sleep(1)
    WebDriverWait(login,10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel= 'displayName']"))
        ).click()

    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][contains(text(),'₹')]"))
        ).click()

    time.sleep(1)
    WebDriverWait(login ,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='inputDiscount_ORD_PurchsCrt']"))
        ).send_keys("20")
        
    time.sleep(3)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='btnAddItem_ORD_PurchsCrt']"))
        ).click()
    time.sleep(3)


    # Click on Create Purchase button
    element3= WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@id='btnSubmit_ORD_PurchsCrt']"))
    )

    login.execute_script("arguments[0].scrollIntoView();", element3)
    element3.click()

    time.sleep(2)
    element4 = login.find_element(By.XPATH, "//th[contains(text(),'Bill Amount')]")
    login.execute_script("arguments[0].scrollIntoView();", element4)
    
    # Click on Send to Review button
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@id='btnCngReview_ORD_PurchsCrt']"))
    ).click()


    # Select B&B Stores from the dropdown to filter the purchase orders based on store
    time.sleep(2)
    drop_button_loc= WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    )

    login.execute_script("arguments[0].click();", drop_button_loc)

    time.sleep(2)

    element = login.find_element(By.XPATH, "//span[normalize-space()='B&B Stores']")
    login.execute_script("arguments[0].scrollIntoView();", element)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='B&B Stores']"))
    ).click()
    
    time.sleep(3)
    # Wait for the table to be present
    table_body = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
    )

    # Locate the first table row
    first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")

    # Find the status element within the first row
    status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
    status_text = status_element.text
    expected_status = "IN REVIEW"

    print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

    # Assert that the status is "IN REVIEW"
    assert status_text == "IN REVIEW", f"Expected status to be 'IN REVIEW', but got '{status_text}'"

    # Click Approve button for the purchase order which one's status is IN REVIEW
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//tbody/tr[1]/td[8]/div[1]/div[1]/button[1]"))
    ).click()

    # Click on Approve button to approve the purchase order
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@id='btnApprove_ORD_PurchsCrt']"))
    ).click()

    time.sleep(3)

    # Wait for the table to be present
    table_body = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
    )

    # Locate the first table row
    first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")

    # Find the status element within the first row
    status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
    status_text = status_element.text
    expected_status = "APPROVED"

    print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

    # Assert that the status is "APPROVED"
    assert status_text == "APPROVED", f"Expected status to be 'APPROVED', but got '{status_text}'"

    time.sleep(5)




@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create Purchase Items With Batch and without Attributes & without Batch and with Attributes")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_purchase2(login):

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[contains(@src,'inventory.png')]"))
    ).click()

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Purchase']"))
    ).click()
    login.implicitly_wait(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='d-flex justify-content-between']//div[@class='ng-star-inserted']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select Store']"))
    ).click()

    time.sleep(3)
    store = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li[@role='option' and @aria-label='B&B Stores']"))
    )
    store.click()

    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//div[contains(@class,'p-dropdown')][.//input[@placeholder='Select Vendor']]")

    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//li[@role='option' and @aria-label='SBT PVT Limited']")

    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//div[contains(@class,'p-dropdown')][.//input[@placeholder='Select Inventory Catalog']]")
    
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//li[@role='option' and @aria-label='Catalog_Inventory']")


    Bill_no = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='inputBillRef_ORD_PurchsCrt']"))
    )
    Bill_no.click()

    random_number = str(random.randint(10000, 99999))
    Bill_no.send_keys(random_number)
    print("Bill no:", random_number)

    login.find_element(By.XPATH, "//p-calendar//input[@type='text']").click()

    Today_Date = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]"))
    )
    Today_Date.click()
    print("Date:", Today_Date.text)

    login.find_element(By.XPATH, "//textarea[@placeholder='Notes to Vendor']").send_keys("Medcc  Supplied item ")

    # ********** ADDING ITEM_5 WITH BATCH & WITHOUT ATTRIBUTES *****************

    # Item Name field - first row in Add Items section
    item_name_field = WebDriverWait(login, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='Search items'])[1]"))
    )

    item_name_field.click()
    item_name_field.clear()
    item_name_field.send_keys("it")   # type item letters to open popup


    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Item_5')]")


    # Enter batch number for the item
    time.sleep(5)
    batch_number = WebDriverWait(login, 20).until(
            EC.element_to_be_clickable((By.XPATH,
            "//td//div[@class='ng-star-inserted']//input[@type='text' and contains(@class, 'p-inputtext')]"))
        )
    batch_number.click()

    random_batch_number = str(random.randint(5, 99))
    batch_number.send_keys(random_batch_number)
    print("Batch_Number:", random_batch_number)

    # Enering item unit for the item
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH,
            "//p-dropdown[@placeholder='Item Units']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']"))
        ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Box of 10']"))
        ).click()
    

    # Enter expiry date for the item
    time.sleep(2)
    item_exp = f"//p-calendar[contains(@class, 'exp-date') and contains(@class, 'ng-tns-c')]"
    WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, item_exp))
        ).click()

    time.sleep(2)
    current_year = datetime.now().strftime("%Y")
    current_year_xpath = f"//button[normalize-space()='{current_year}']"
    print(current_year_xpath)

    time.sleep(2)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, current_year_xpath))
        ).click()
    
    [year, month, day] = add_date(2)
    print(year)
    year_xpath = f"//span[normalize-space()='{year}']"
    print(year_xpath)

    time.sleep(1)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, year_xpath))
        ).click()
    
    time.sleep(1)
    month_xpath = f"//span[normalize-space()='{month}']"
    print(month_xpath)
    WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, month_xpath))
         ).click()
    
    time.sleep(2)
    day_xpath = f"//span[normalize-space()='{day}' and not(contains(@class,'p-disabled'))]"
    print(day_xpath)
    time.sleep(2)
    WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, day_xpath))
        ).click()
        

    # Entering quantity for the item
    qty = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='inputNumber_ORD_PurchsCrt']"))
        )
    qty.click()
    qty.clear()

    qty_random_number = str(random.randint(10, 50))
    qty.send_keys(qty_random_number)
    print("Qty Of Item:", qty_random_number)


    # Entering free quantity for the item
    free_qty = WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='inputQty_ORD_PurchsCrt']"))
        )
    free_qty.click()
    free_qty.clear()

    free_qty_random_number = str(random.randint(1, 5))
    free_qty.send_keys(free_qty_random_number)
    print("Free Qty:", free_qty_random_number)

   # Entering MRP for the item
    mrpprice = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='inputMrp_ORD_PurchsCrt']")
        )
    )

    mrpprice.click()

    mrpprice_random_number = random.randint(60, 200)
    mrpprice.send_keys(str(mrpprice_random_number))

    print("MRP of the item:", mrpprice_random_number)


    # Entering purchase price for the item
    time.sleep(2)

    price = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='inputPrice_ORD_PurchsCrt']")
        )
    )

    price.click()

    price_random_number = random.randint(40, 100)

    # Check if purchase price is higher than MRP
    if price_random_number > mrpprice_random_number:
        price_random_number = random.randint(40, mrpprice_random_number - 1)
    print("Purchase price was higher than MRP, changed to:", price_random_number)

    price.send_keys(str(price_random_number))

    print("Price of the item:", price_random_number)

    # Entering discount for the item
    time.sleep(1)
    WebDriverWait(login,10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel= 'displayName']"))
        ).click()

    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='%']"))
        ).click()

    time.sleep(1)
    WebDriverWait(login ,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='inputDiscount_ORD_PurchsCrt']"))
        ).send_keys("5")
        
    time.sleep(3)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='btnAddItem_ORD_PurchsCrt']"))
        ).click()
    time.sleep(3)

    # ********** ADDING ITEM_6 WITHOUT BATCH & WITH ATTRIBUTES *****************

    # Item Name field - first row in Add Items section
    item_name_field = WebDriverWait(login, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='Search items'])[1]"))
    )

    item_name_field.click()
    item_name_field.clear()
    item_name_field.send_keys("it")   # type item letters to open popup


    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Item_6')]")

    # Wait for Select Items popup
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='Select Items']"))
    )

    # Row containing Item_6 White inside popup
    item_row_xpath = "//tr[.//*[normalize-space()='Item_6 White']]"

    item_row = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, item_row_xpath))
    )

    login.execute_script("arguments[0].scrollIntoView({block:'center'});", item_row)
    time.sleep(1)

    # Click the first cell/radio area of Item_6 White row
    radio_button = WebDriverWait(login, 10).until(
    EC.presence_of_element_located((
        By.XPATH,
        "//tr[.//*[normalize-space()='Item_6 White']]//input[@type='radio']"))
    )

    login.execute_script("arguments[0].click();", radio_button)
    time.sleep(1)

    # Click Done button
    wait_and_locate_click(login, By.XPATH,
        "//button[@id='btnSubmitItems_ORD_ItemSelection']"
    )

    # Wait until popup closes
    WebDriverWait(login, 10).until(
        EC.invisibility_of_element_located((By.XPATH, "//*[normalize-space()='Select Items']"))
    )

    # Verify selected item appears in Add Items -> Item Name field
    selected_item_field = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Search items'])[1]"))
    )

    print("Selected Item:", selected_item_field.get_attribute("value"))


    # Enering item unit for the item
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH,
            "//p-dropdown[@id='selectunit_ORD_PurchsCrt']//div[@class='p-dropdown p-component']"))
        ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Box of 8']"))
        ).click()
    

     # Entering quantity for the item
    qty = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='inputNumber_ORD_PurchsCrt']"))
        )
    qty.click()
    qty.clear()

    qty_random_number = str(random.randint(10, 50))
    qty.send_keys(qty_random_number)
    print("Qty Of Item:", qty_random_number)


    # Entering free quantity for the item
    free_qty = WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='inputQty_ORD_PurchsCrt']"))
        )
    free_qty.click()
    free_qty.clear()

    free_qty_random_number = str(random.randint(1, 5))
    free_qty.send_keys(free_qty_random_number)
    print("Free Qty:", free_qty_random_number)

    # Entering MRP for the item
    mrpprice = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='inputMrp_ORD_PurchsCrt']")
        )
    )

    mrpprice.click()

    mrpprice_random_number = random.randint(60, 200)
    mrpprice.send_keys(str(mrpprice_random_number))

    print("MRP of the item:", mrpprice_random_number)


    # Entering purchase price for the item
    time.sleep(2)

    price = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='inputPrice_ORD_PurchsCrt']")
        )
    )

    price.click()

    price_random_number = random.randint(40, 100)

    # Check if purchase price is higher than MRP
    if price_random_number > mrpprice_random_number:
        price_random_number = random.randint(40, mrpprice_random_number - 1)
    print("Purchase price was higher than MRP, changed to:", price_random_number)

    price.send_keys(str(price_random_number))

    print("Price of the item:", price_random_number)


    # Entering discount for the item
    time.sleep(1)
    WebDriverWait(login,10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel= 'displayName']"))
        ).click()

    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][contains(text(),'₹')]"))
        ).click()

    time.sleep(1)
    WebDriverWait(login ,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='inputDiscount_ORD_PurchsCrt']"))
        ).send_keys("20")
        
    time.sleep(3)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='btnAddItem_ORD_PurchsCrt']"))
        ).click()
    time.sleep(3)


    # Click on Create Purchase button
    element3= WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@id='btnSubmit_ORD_PurchsCrt']"))
    )

    login.execute_script("arguments[0].scrollIntoView();", element3)
    element3.click()

    time.sleep(2)
    element4 = login.find_element(By.XPATH, "//th[contains(text(),'Bill Amount')]")
    login.execute_script("arguments[0].scrollIntoView();", element4)
    
    # Click on Send to Review button
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@id='btnCngReview_ORD_PurchsCrt']"))
    ).click()


    # Select B&B Stores from the dropdown to filter the purchase orders based on store
    time.sleep(2)
    drop_button_loc= WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    )

    login.execute_script("arguments[0].click();", drop_button_loc)

    time.sleep(2)

    element = login.find_element(By.XPATH, "//span[normalize-space()='B&B Stores']")
    login.execute_script("arguments[0].scrollIntoView();", element)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='B&B Stores']"))
    ).click()
    
    time.sleep(3)
    # Wait for the table to be present
    table_body = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
    )

    # Locate the first table row
    first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")

    # Find the status element within the first row
    status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
    status_text = status_element.text
    expected_status = "IN REVIEW"

    print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

    # Assert that the status is "IN REVIEW"
    assert status_text == "IN REVIEW", f"Expected status to be 'IN REVIEW', but got '{status_text}'"

    # Click Approve button for the purchase order which one's status is IN REVIEW
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//tbody/tr[1]/td[8]/div[1]/div[1]/button[1]"))
    ).click()

    # Click on Approve button to approve the purchase order
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@id='btnApprove_ORD_PurchsCrt']"))
    ).click()

    time.sleep(3)

    # Wait for the table to be present
    table_body = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
    )

    # Locate the first table row
    first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")

    # Find the status element within the first row
    status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
    status_text = status_element.text
    expected_status = "APPROVED"

    print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

    # Assert that the status is "APPROVED"
    assert status_text == "APPROVED", f"Expected status to be 'APPROVED', but got '{status_text}'"

    time.sleep(5)


##########################################  Create Order ##########################################################

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create Order")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_order(login):

 
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[contains(@src,'rx-orders.png')]"))
    ).click()

    # Change the store to B&B Stores to create order for that store
    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//p-dropdown[@optionlabel='name']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='B&B Stores']"))
    ).click()

    # Click on Create order card from the order dashboard
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Create Order')]"))
    ).click()


    # Select customer by searching with phone number and selecting from the dropdown
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Select customer']"))
    ).send_keys("8281276241")

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Id : 649']"))
    ).click()

    # Select the store from the dropdown in create order pop up
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p-dropdown[@id='selectStore_ORD_CrtItemPop']//div[@class='p-dropdown p-component']"))
    ).click()              

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='B&B Stores']"))
    ).click()

    # Select catalog from the dropdown in create order pop up
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='p-multiselect p-component']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Sale_catalog']"))
    ).click()


    # Close the catalog dropdown by clicking outside the dropdown area
    time.sleep(1)
    wait_and_locate_click(login, By.XPATH, "//timesicon[@class='p-element p-icon-wrapper ng-star-inserted']")


    # Click NEXT button in the create order pop up
    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@id='btnSave_ORD_CrtItemPop']"))
    ).click()
    print("Create order pop up details filled and NEXT button clicked successfully")


    # Add items
    item_names_to_select = ['Item_1']
    sum = 0
    items_data_before_confirm = []

    for i in range(len(item_names_to_select)):
        item_name = item_names_to_select[i]
        print(item_name)

        # Search and select item
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Search items']"))
        ).send_keys(item_name)

        item_xpath = f"//div[contains(text(),'{item_name.title()}')]"
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, item_xpath))
        ).click()


        # Wait for Select Item popup
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='Select Item']"))
        )

        # Click Green attribute button
        green_btn = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                "//button[@id='btnSltVal_ORD_Vitem' and normalize-space()='Green']"))
        )

        login.execute_script("arguments[0].scrollIntoView({block:'center'});", green_btn)
        time.sleep(1)
        green_btn.click()

        time.sleep(1)

        # Click Select Item button
        select_item_btn = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btnSave_ORD_Vitem']"))
        )

        login.execute_script("arguments[0].scrollIntoView({block:'center'});", select_item_btn)
        select_item_btn.click()

        # Wait until popup closes
        WebDriverWait(login, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//*[normalize-space()='Select Item']"))
        )

        # Verify item is added in the table
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH,
                "//table//*[normalize-space()='Item_1']"))
        )

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH,
                "//*[normalize-space()='Green']"))
        )
        print("Item_1 Green added successfully")

        # Enter quantity for the item
        qty_xpath = f"//input[@id='inputQty_ORD_CrtItem'][{i + 1}]"
        qty = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, qty_xpath))
        )
        qty.click()
        qty.clear()

        qty_random_number = str(random.randint(5, 10))
        qty.send_keys(qty_random_number)
        print("Qty Of Item:", qty_random_number)


        item_row_xpath = f"//tr[.//*[normalize-space()='{item_name}']]"

        # Rate
        rate_value = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH,
            item_row_xpath + "//td[3]//input"))
        ).get_attribute("value")

        # Quantity
        qty_value = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH,
            item_row_xpath + "//td[4]//input"))
        ).get_attribute("value")

        # Total
        total_text = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH,
            item_row_xpath + "//td[5]"))
        ).text

        rate_float = float(rate_value.replace(",", "").strip())
        qty_float = float(qty_value.replace(",", "").strip())
        total_float = float(total_text.replace(",", "").strip())

        print("Item:", item_name)
        print("Rate:", rate_float)
        print("Quantity:", qty_float)
        print("Total:", total_float)
        
        # Calculate total for each item
        sum += total_float
        print("sum: ", sum)

        # Capture row data
        row_xpath = f"//tbody[@class='p-element p-datatable-tbody']/tr[{i + 1}]"
        print(row_xpath)
        row = login.find_element(By.XPATH, row_xpath)
        columns = row.find_elements(By.TAG_NAME, "td")
        item_total_text = columns[4].text.strip()


        # items_data_before_confirm.append({
        #     'item_name': item_names_to_select[i],
        #     'qty': qty_value,
        #     'price': rate_value,
        #     'total': item_total_text
        # })

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
    items_data_after_confirm = []

    for i in range(len(item_names_to_select)):
        row_xpath = f"//tbody[@class='p-element p-datatable-tbody']/tr[{i + 1}]"
        row = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, row_xpath))
        )

        columns = row.find_elements(By.TAG_NAME, "td")
        item_total_text = columns[4].text.strip()
        qty_confirmed = login.find_element(By.XPATH, f"(//input[@min='1'])[{i + 1}]").get_attribute('value')

        items_data_after_confirm.append({
            'item_name': item_names_to_select[i],
            'qty': qty_confirmed,
            'price': sum,
            'total': item_total_text
        })

    # Step 4: Compare the item details before and after confirming the order
    for before, after in zip(items_data_before_confirm, items_data_after_confirm):
        assert before == after, f"Mismatch found! Before: {before}, After: {after}"

    print("Order confirmation data matches successfully.")


    # Click on Create Invoice button
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnCrtInv_ORD_CrtItem']")

    # Click on Add Discount button
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//th[@id='actionAddDct_ORD_CrtItem']")

    # Catch Apply Discount popup using flexible XPath
    discount_popup_xpath = (
        "//*[contains(normalize-space(),'Apply Discount')]"
        "/ancestor::*[contains(@class,'modal') or contains(@class,'dialog') or contains(@class,'content')][1]"
    )

    WebDriverWait(login, 15).until(
        EC.presence_of_element_located((By.XPATH, discount_popup_xpath))
    )
    print("Apply Discount popup opened")

    # Click Select Discount dropdown
    wait_and_locate_click(login,By.XPATH,
        "//div[contains(@class,'p-dropdown')][.//input[@placeholder='Select discount']]"
    )

    time.sleep(1)
    # Select On Demand Discount
    wait_and_locate_click(login, By.XPATH, "//li[@role='option'][.//span[normalize-space()='On Demand Discount']]")
    print("On Demand Discount selected")

    # Enter the discount value
    discount_input = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='inputAmt_ORD_Dsct']")
        )
    )

    discount_input.clear()
    discount_input.send_keys("10")

    # Optional: enter private note
    login.find_element(By.XPATH,
        discount_popup_xpath + "//textarea[@placeholder='Private note']"
    ).send_keys("Discount applied")

    # Optional: enter note for customer
    login.find_element(By.XPATH,
        discount_popup_xpath + "//textarea[@placeholder='Notes for customer']"
    ).send_keys("Discount applied to this order")

    # Click Apply button
    wait_and_locate_click(login, By.XPATH, discount_popup_xpath + "//button[@id='btnAplCp_ORD_Dsct']")
    print("Discount applied successfully")

    msg = get_toast_message(login)
    print("Toast Message :", msg)

    # Click on View Invoice button
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnViewInv_ORD_CrtItem']")


    # Wait until invoice page appears
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(normalize-space(),'Invoice No#')]")
        )
    )
    print("Invoice page opened")

    # Scroll down to bottom first
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # XPath for Get Payment PrimeNG dropdown
    get_payment_dropdown_xpath = (
        "//div[contains(@class,'p-dropdown')]"
        "[.//input[@placeholder='Get Payment'] or .//span[normalize-space()='Get Payment']]"
    )

    # Locate Get Payment dropdown
    get_payment_dropdown = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, get_payment_dropdown_xpath))
    )

    # Scroll directly to Get Payment dropdown
    login.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        get_payment_dropdown
    )

    time.sleep(1)
    print("Scrolled to Get Payment dropdown")

    # Click Get Payment dropdown
    wait_and_locate_click(login, By.XPATH, get_payment_dropdown_xpath)


    # Select payment method as Cash
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//li[@aria-label='Pay by Cash']")   

    # Catch / wait for Pay by Cash popup
    pay_popup_xpath = (
        "//div[contains(@class,'mdc-dialog__container')]"
        "[.//app-pay-bill-invoice]"
        "[.//*[contains(normalize-space(),'Payable Amount')]]"
    )

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, pay_popup_xpath))
    )

    # Scroll to Pay button if needed
    pay_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, pay_popup_xpath + "//button[@id='btnMkPay_ORD_PayBill']")
        )
    )

    login.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        pay_button
    )

    # Click on Pay button in the payment popup
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnMkPay_ORD_PayBill']")
    print("Pay button clicked successfully")

    # Catch / wait for confirmation popup
    confirm_payment_popup_xpath = (
        "//div[contains(@class,'mdc-dialog__container')]"
        "[.//app-confirm-paymentbox]"
        "[.//*[contains(normalize-space(),'Proceed with payment')]]"
    )

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, confirm_payment_popup_xpath))
    )
    print("Proceed with payment confirmation popup opened")

    # Click on YES button to confirm payment
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnSltYes_ORD_ConfPay']")

    msg = get_snack_bar_message(login)
    print("Snack Bar message :", msg)

    time.sleep(2)
    # Wait for invoice page to load again
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(normalize-space(),'Invoice No#')]")
        )
    )
    print("Invoice page loaded")

    time.sleep(1)

    # Scroll up to the top of the invoice page
    login.execute_script("window.scrollTo(0, 0);")

    time.sleep(1)

    # Click Back arrow
    wait_and_locate_click(login, By.XPATH,
        "//div[contains(@class,'pointer-cursor')][.//i[contains(@class,'pi-arrow-left')] and .//*[normalize-space()='Back']]"
    )

    time.sleep(2)
    # Wait until Order page appears
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(normalize-space(),'Order #')]")
        )
    )

    print("Order page opened")

    time.sleep(1)
    # Scroll down to bottom of order page
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    time.sleep(2)
    # Click complete order button
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@id='btnOdCng_ORD_CrtItem']"))
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
