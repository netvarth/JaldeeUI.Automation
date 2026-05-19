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
        (
            By.XPATH,
            "//div[contains(@class,'mdc-dialog__container')]//p[contains(normalize-space(),'Once added to the catalog')]"
        )
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
@allure.title("Create Purchase")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_create_purchase(login):

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

    # Click Add Items button
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "//button[@id='btnBrowse_ORD_PurchsCrt']")

#     # 2. Wait for popup and click the first radio button
#     first_radio = wait.until(
#     EC.presence_of_element_located(
#         (By.XPATH, "(//input[@type='radio' and contains(@class,'mdc-radio__native-control')])[1]")
#     )
# )

#     # Normal click may fail for Angular Material radio, so JS click is safer
#     login.execute_script("arguments[0].click();", first_radio)

    first_radio = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "(//input[@type='radio' and contains(@class,'mdc-radio__native-control')])[1]")
    )
)

    login.execute_script("arguments[0].click();", first_radio)

    login.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
        done_btn
)

    # Click Done button
    wait.until(
    EC.element_to_be_clickable(
        (By.ID, "btnSubmitItems_ORD_ItemSelection")
    )
)

    login.execute_script("arguments[0].click();", done_btn)

    # element1 = login.find_element(By.XPATH, "//button[@id='btnBrowse_ORD_PurchsCrt']")
    # login.execute_script("arguments[0].scrollIntoView();", element1)

    # item_list = ["Item_2", "Item_3"]
    # random_batch_number = str(random.randint(5, 99))

    # for i in range(len(item_list)):
    #     print(item_list[i])
    #     item_xpath = item_xpath = f"//div[@class='d-flex justify-content-between fw-bold']//div[@class='ng-star-inserted'][normalize-space()='{title_to_item(item_list[i])}']"
                                            
    #     WebDriverWait(login, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search items']"))
    #     ).send_keys("item")

    #     time.sleep(2)
    #     WebDriverWait(login, 10).until(
    #         EC.presence_of_element_located((By.XPATH, item_xpath))
    #     ).click()

    time.sleep(5)
    batch_number = WebDriverWait(login, 20).until(
            EC.element_to_be_clickable((By.XPATH,
            "//td//div[@class='ng-star-inserted']//input[@type='text' and contains(@class, 'p-inputtext')]"))
        )
    batch_number.click()

    random_batch_number = str(random.randint(5, 99))
    batch_number.send_keys(random_batch_number)
    print("Batch_Number:", random_batch_number)

    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH,
            "//p-dropdown[@placeholder='Item Units']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']"))
        ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Box of 10']"))
        ).click()

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


        # pr_date = WebDriverWait(login, 15).until(
        # EC.presence_of_element_located(
        # (By.XPATH, "//button[normalize-space()='Send Message']"))
        # )        
        # login.execute_script("arguments[0].click();", pr_date)

        # time.sleep(3)
        
    qty = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@min='1']"))
        )
    qty.click()
    qty.clear()

    qty_random_number = str(random.randint(10, 50))
    qty.send_keys(qty_random_number)
    print("Qty Of Item:", qty_random_number)

    free_qty = WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[contains(@class,'free-quantity')]"))
        )
    free_qty.click()
    free_qty.clear()

    free_qty_random_number = str(random.randint(1, 5))
    free_qty.send_keys(free_qty_random_number)
    print("Free Qty:", free_qty_random_number)

        
    mrpprice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            "(//input[contains(@class,'item-price')])[1]"))
        )
    mrpprice.click()
    mrpprice_random_number = str(random.randint(60, 200))
    mrpprice.send_keys(mrpprice_random_number)
    print("MRP of the item:", mrpprice_random_number)


    time.sleep(2)
    price = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[contains(@class,'item-price')])[2]"))
        )
    price.click()
    price_random_number = str(random.randint(40, 100))
    price.send_keys(price_random_number)
    print("Price of the item:", price_random_number)


    time.sleep(1)
    WebDriverWait(login,10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel= 'displayName']"))
        ).click()

    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='%']"))
        ).click()

    time.sleep(1)
    WebDriverWait(login ,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@class,'discount')]"))
        ).send_keys("5")
        
    time.sleep(3)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Add']"))
        ).click()
    time.sleep(3)

    # element2 = login.find_element(By.XPATH, "//div[contains(text(),'Add Items')]")
    # login.execute_script("arguments[0].scrollIntoView();", element2)

    element3= WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Create Purchase']"))
    )

    login.execute_script("arguments[0].scrollIntoView();", element3)
    element3.click()

    time.sleep(2)
    element4 = login.find_element(By.XPATH, "//th[contains(text(),'Bill Amount')]")
    login.execute_script("arguments[0].scrollIntoView();", element4)
    

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Send to Review']"))
    ).click()

    time.sleep(2)
    drop_button_loc= WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    )

    login.execute_script("arguments[0].click();", drop_button_loc)

    time.sleep(2)

    element = login.find_element(By.XPATH, "//span[contains(text(),'Geetha')]")
    login.execute_script("arguments[0].scrollIntoView();", element)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Geetha')]"))
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


    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//tbody/tr[1]/td[8]/div[1]/div[1]/button[1]"))
    ).click()

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Approve')]"))
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

    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//p-dropdown[@optionlabel='name']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Geetha']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Create Order')]"))
    ).click()


    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Search patients']"))
    ).send_keys("5558210996")

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Id : etf']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
    ).click()              

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Geetha']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Geetha_order_catalog']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "(//span[normalize-space()='Next'])[1]"))
    ).click()



    # Add items
    item_names_to_select = ['Item3']
    item_prices = [95]
    sum = 0
    items_data_before_confirm = []

    for i in range(len(item_names_to_select)):
        item_name = item_names_to_select[i]
        item_price = item_prices[i]
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

        qty_xpath = f"(//input[@min='1'])[{i + 1}]"
        qty = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, qty_xpath))
        )
        qty.click()
        qty.clear()

        qty_random_number = str(random.randint(5, 10))
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
        items_data_before_confirm.append({
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
            'price': item_prices[i],
            'total': item_total_text
        })

    # Step 4: Compare the item details before and after confirming the order
    for before, after in zip(items_data_before_confirm, items_data_after_confirm):
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
