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
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
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

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Sales Order  Off']"))
    ).click()

    try:

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

    except:

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

    login.find_element(By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']").click()

    # Find the element you want to scroll to
    element = login.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")

    # Scroll to the element
    login.execute_script("arguments[0].scrollIntoView();", element)

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='RX Push Management System']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='mdc-switch__icons']"))
    ).click()

    try:

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

    except:

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

    login.find_element(By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']").click()

    # Find the element you want to scroll to
    element = login.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
    login.execute_script("arguments[0].scrollIntoView();", element)

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Inventory Management System']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='mdc-switch__icons']"))
    ).click()

    try:

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

    except:

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

    login.find_element(By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']").click()

    element = login.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
    login.execute_script("arguments[0].scrollIntoView();", element)

    print("Inventory setting Enabled Successfully")

    time.sleep(5)


##################   New Store creation   #############################
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_store_creation(login):
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@class='menu-item menu-item-submenu mt-2 ng-star-inserted'][7]"))
    ).click()

    time.sleep(5)

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Stores']"))
    ).click()

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Store']"))
    ).click()

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Type']"))
    ).click()

    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='PHARMACY']"))
    ).click()

    store_name = "Store_" + str(uuid.uuid4())[:6]
    print(store_name)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Name']"))
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


    invoice_prefix = "K_" + str(uuid.uuid4())[:1]
    print(invoice_prefix)
    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, " //input[@placeholder= 'Invoice prefix']"))
    ).send_keys(invoice_prefix)
    

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Location']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Chavakkad']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create']"))
    ).click()

    try:

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

    except:

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)
    time.sleep(3)


###############################   Item Creation   ################################

@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_item_creation(login):
    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//li[@class='menu-item menu-item-submenu mt-2 ng-star-inserted'][7]"))
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

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Item Description']"))
    ).send_keys("A Item name is required and recommended to be unique.")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select Category']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Antibacterials']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Select Group')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Medicine']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select Type']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Tablet']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select Manufacturer']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='ALPHA DRUGS']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Select Unit')]"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Box of 10'] "))
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
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='33215478']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Select Item Compositions')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'starch, hydroxypropyl methylcellulose, propylene g')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Select Item Tax')]"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='GST 12%']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Item']"))
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

@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_inventory_catalog(login):
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@class='menu-item menu-item-submenu mt-2 ng-star-inserted'][7]"))
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
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Geetha']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create Catalog']"))
    ).click()

    time.sleep(5)

    checkboxes = WebDriverWait(login, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//input[contains(@id, 'mat-mdc-checkbox')]"))
    )

    # Click the first three checkboxes
    for i in range(1, min(6, len(checkboxes))):
        checkboxes[i].click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']"))
    ).click()

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

@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_create_purchase(login):
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@class='menu-item menu-item-submenu mt-2 ng-star-inserted'][7]"))
    ).click()

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Purchase']"))
    ).click()
    login.implicitly_wait(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='p-element create-purchase-button me-1 p-button p-component']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Select Store']"))
    ).click()

    time.sleep(3)
    store = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Swathy Pharmacy')]"))
    )
    store.click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p-dropdown[@placeholder='Select Vendor']//div[@aria-label='dropdown trigger']"))
    ).click()

    Select_supplier = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='MedCC']"))
    )
    Select_supplier.click()
    print("Select Supplier:", Select_supplier.text)

    login.find_element(By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']").click()

    Inventory_Catalog = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Inventory Catalog2']"))
    )
    Inventory_Catalog.click()
    print("Inventory Selected:", Inventory_Catalog.text)

    Bill_no = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Purchase Bill#']"))
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

    login.find_element(By.XPATH, "//textarea[@placeholder='Notes to supplier']").send_keys("Medcc  Supplied item ")

    element = login.find_element(By.XPATH, "//div[contains(text(),'Add Items')]")
    login.execute_script("arguments[0].scrollIntoView();", element)

    item_list = ["items", "item3", "item4"]
    random_batch_number = str(random.randint(5, 99))

    for i in range(len(item_list)):
        print(item_list[i])
        item_xpath = item_xpath = f"//div[@class='d-flex justify-content-between fw-bold']//div[@class='ng-star-inserted'][normalize-space()='{title_to_item(item_list[i])}']"
                                            
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search items']"))
        ).send_keys("item")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, item_xpath))
        ).click()

        time.sleep(5)
        batch_number = WebDriverWait(login, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "//td//div[@class='ng-star-inserted']//input[@type='text' and contains(@class, 'p-inputtext')]"))
        )
        batch_number.click()

        # random_number = str(random.randint(5, 99))
        batch_number.send_keys(random_batch_number)
        print("Batch_Number:", random_batch_number)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//p-dropdown[@placeholder='Item Units']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Box of 10']"))
        ).click()

        time.sleep(3)
        item_exp = f"//p-calendar[contains(@class, 'exp-date') and contains(@class, 'ng-tns-c')]"
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, item_exp))
        ).click()

        time.sleep(3)
        current_year = datetime.now().strftime("%Y")
        current_year_xpath = f"//button[normalize-space()='{current_year}']"
        print(current_year_xpath)
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, current_year_xpath))
        ).click()

        [year, month, day] = add_date(2)
        print(year)
        year_xpath = f"//span[normalize-space()='{year}']"
        print(year_xpath)
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, year_xpath))
        ).click()
        time.sleep(2)
        month_xpath = f"//span[normalize-space()='{month}']"
        print(month_xpath)
        WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, month_xpath))
         ).click()
        time.sleep(2)
        day_xpath = f"//span[normalize-space()='{day}' and not(contains(@class,'p-disabled'))]"
        print(day_xpath)
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, day_xpath))
        ).click()

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

        price = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//input[contains(@class,'item-price')]"))
        )
        price.click()

        price_random_number = str(random.randint(60, 200))
        price.send_keys(price_random_number)
        print("Price of the item:", price_random_number)

        WebDriverWait(login,10).until(
            EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel= 'displayName']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='%']"))
        ).click()

        WebDriverWait(login ,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@class,'discount')]"))
        ).send_keys("5")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Add']"))
        ).click()

    element = login.find_element(By.XPATH, "//div[contains(text(),'Add Items')]")
    login.execute_script("arguments[0].scrollIntoView();", element)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Create Purchase']"))
    ).click()

   
   

    # Wait for the table to be present
    table_body = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "p-datatable-tbody"))
    )

    # Locate the first table row
    first_row = table_body.find_element(By.XPATH, './tr[1]')

    # Find the status element within the first row
    status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
    status_text = status_element.text
    expected_status = "DRAFT"

    print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

    # Assert that the status is "DRAFT"
    assert status_text == "DRAFT", f"Expected status to be 'DRAFT', but got '{status_text}'"

    # Find and click the "Edit" button within the first row
    edit_button = first_row.find_element(By.XPATH, './/button[contains(@class, "p-button")]')
    edit_button.click()

    print("Status is correctly set to 'DRAFT' and 'Edit' button clicked successfully.")
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Send to review']"))
    ).click()


    table_body = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "p-datatable-tbody"))
    )

    
    first_row = table_body.find_element(By.XPATH, './tr[1]')

    status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
    status_text = status_element.text
    expected_status = "IN REVIEW"

    print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

    # Assert that the status is "IN REVIEW"
    assert status_text == "IN REVIEW", f"Expected status to be 'IN REVIEW', but got '{status_text}'"


    view_button = first_row.find_element(By.XPATH, './/button[contains(@class, "p-button")]')
    view_button.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Approve']"))
    ).click()



    table_body = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "p-datatable-tbody"))
    )

    
    first_row = table_body.find_element(By.XPATH, './tr[1]')

    status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
    status_text = status_element.text
    expected_status = "APPROVED"

    print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

    # Assert that the status is "APPROVED"
    assert status_text == "APPROVED", f"Expected status to be 'APPROVED', but got '{status_text}'"

    time.sleep(5)

    WebDriverWait(login,10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//i[@class='pi pi-arrow-left']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Swathy Pharmacy']"))
    ).click()

    time.sleep(2)








############################################ Create Order Catalogue ##########################################



@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_create_order_catalog(login):

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Sales Order')]"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//p-dropdown[@optionlabel='name']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Swathy Pharmacy']"))
    ).click()


    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Catalogs')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='p-ripple p-element p-button p-component']"))
    ).click()

    order_catalog_name = "Catalog_" + str(uuid.uuid4())[:6]

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter Catalog Name']"))
    ).send_keys(order_catalog_name)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Swathy Pharmacy']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p-dropdown[@placeholder = 'Select Inventory Management']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Yes']"))
    ).click()


    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p-dropdown[@placeholder = 'Online Self Order']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Yes']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='p-multiselect-label p-placeholder']"))
    ).click()
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Inventory Catalog2']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Save & Next']"))
    ).click()

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='p-ripple p-element p-paginator-last p-paginator-element p-link ng-star-inserted']"))
    ).click()

    #List of item names to be selected
    item_names_to_select = ['items', 'Item3', 'Item4']

     # Find all rows in the table
    # rows = WebDriverWait(login, 10).until(
    #     EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr"))
    # )
    # time.sleep(3)

    for item_name in item_names_to_select:
        print(f"Looking for item: {item_name}")
        # Locate the row containing the item name
        try:
            try:
                row = WebDriverWait(login, 20).until(
                    EC.presence_of_element_located((By.XPATH, f"//tr[td/span[text()='{item_name}']]"))
                )
            except Exception as e:
                print(f"Error finding item: {item_name}. Exception: {e}")
                WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//anglelefticon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']"))
                ).click()
            print(f"Found row for item: {item_name}")
            
            # Locate the checkbox within that row
            checkbox = row.find_element(By.XPATH, ".//input[@type='checkbox']")
            
            # Click the checkbox if it is not already selected
            if not checkbox.is_selected():
                checkbox.click()
                print(f"Selected item: {item_name}")
        except Exception as e:
            print(f"Error finding item: {item_name}. Exception: {e}")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']"))
    ).click()

    # try:
        # Wait for the table body to be present
    time.sleep(2)
    table_body = WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//tbody[@class='p-element p-datatable-tbody']"))
    )
    
    # Find all rows in the table body
    rows = table_body.find_elements(By.XPATH, ".//tr[@class='ng-star-inserted']")
    
    for row in rows:
        # Find the "Edit Details" button in the current row
        edit_button = row.find_element(By.XPATH, ".//button[contains(@class, 'btn fw-bold p-button-light')]")
        
        # Click the "Edit Details" button
        edit_button.click()
        
        # Perform the necessary actions on the edit details page
        items_to_select = ["GST 5%", "GST 12%", "GST 18%"]

        try:
                # Locate the MultiSelect component
                multiSelect = WebDriverWait(login, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "p-multiselect"))
                )
                
                # Open the dropdown
                multiSelect.click()
                
                # Wait for the dropdown options to be visible
                optionsContainer = WebDriverWait(login, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".p-multiselect-items"))
                )
                
                # Get all available options
                options = optionsContainer.find_elements(By.CSS_SELECTOR, ".p-multiselect-item")
                
                # Filter the options to match the items to select
                optionsToSelect = [option for option in options if option.text.strip() in items_to_select]
                
                # Select a random item
                selectedOption = random.choice(optionsToSelect)
                selectedOption.click()  # Click to select the option
                
                # Optionally, close the dropdown by clicking outside or performing another action
                multiSelect.click()  # Clicking on the component again might close the dropdown

        finally:
                time.sleep(5)  # Allow some time to observe the change or for any additional processing


        try:


            # Wait for the dropdown options to be visible
            options_container = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Select Batch']"))
            )
            options_container.click()


            # Get all available options
            options = options_container.find_elements(By.XPATH, "//ul[@role='listbox' and contains(@class, 'p-dropdown-items')]/p-dropdownitem/li[@role='option']")
            # print(options.text)
            if options:
                # Select the last option
                last_option = options[-1]
                last_option_text = last_option.text.strip()  # Optionally, you can get the text of the last option
                last_option.click()   
                print(f"Selected last option: {last_option_text}")
            else:
                print("No options found in the dropdown.")

            # Optionally, close the dropdown by clicking outside or performing another action
            # multiSelect.click()  # Clicking on the component again might close the dropdown

        finally:
            time.sleep(5)  # Allow some time to observe the change or for any additional processing



        price = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//input[@placeholder='Enter Batch Price']"))
        )
        price.click()

        price_random_number = str(random.randint(60, 200))
        price.send_keys(price_random_number)
        print("Price of the item:", price_random_number)

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Save']"))
        ).click()
   
    time.sleep(2)


