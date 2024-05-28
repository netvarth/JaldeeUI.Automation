import time

from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


#################   Enable the Inventory Setting   #############################
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_enable_inventory_setting(login):
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@ptooltip='Settings']"))
    ).click()

    element = login.find_element(By.XPATH, "//div[@class='disp-flex'][normalize-space()='RX Orders']")
    login.execute_script("arguments[0].scrollIntoView();", element)

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
    element = login.find_element(By.XPATH, "//div[@class='disp-flex'][normalize-space()='RX Orders']")

    # Scroll to the element
    login.execute_script("arguments[0].scrollIntoView();", element)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Inventory Management System']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Inventory Management  Off']"))
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

    element = login.find_element(By.XPATH, "//div[@class='disp-flex'][normalize-space()='RX Orders']")
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

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Stores']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Store']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Type']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='PHARMACY']"))
    ).click()

    store_name = "Store_" + str(uuid.uuid4())[:6]

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Name']"))
    ).send_keys(store_name)

    email = f"{store_name}{test_mail}"
    random_number = str(random.randint(1111111, 9999999))
    phonenumber = f"{555}{random_number}"

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
    ).send_keys(phonenumber)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
    ).send_keys(email)

    invoice_prefix = "KKM_" + str(uuid.uuid4())[:4]

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, " //input[@placeholder= 'Invoice prefix']"))
    ).send_keys(invoice_prefix)

    WebDriverWait(login, 10).until(
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
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Inventory')]"))
    ).click()

    WebDriverWait(login, 10).until(
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
            (By.XPATH, "//p-dropdown[@placeholder='Inventory Item or Not']//div[@class='p-dropdown p-component']"))
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
            (By.XPATH, "//div[contains(text(),'Inventory')]"))
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


######################################  Create Purchase ######################################################3
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_create_purchase(login):
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Inventory')]"))
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

    login.find_element(By.XPATH, "//span[normalize-space()='Select Supplier']").click()

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

    item_list = ["items", "item 1", "item3", "item4"]
    random_batch_number = str(random.randint(5, 99))

    for i in range(len(item_list)):
        print(item_list[i])
        item_xpath = f"//div[@class='d-flex justify-content-between fw-bold']//div[@class='ng-star-inserted'][normalize-space()='{item_list[i]}']"

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search items']"))
        ).send_keys("ite")

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

        item_exp = f"(//input[starts-with(@class, 'ng-tns-c') and contains(@class, 'p-inputtext p-component ng-star-inserted')])[{i + 2}]"
        WebDriverWait(login, 10).until(
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

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, month_xpath))
        ).click()
        time.sleep(2)
        day_xpath = f"//span[normalize-space()='{day}'][contains(@class, 'p-highlight')]"
        print(day_xpath)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, day_xpath))
        ).click()

        time.sleep(5)
        qty = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@min='1']"))
        )
        qty.click()
        qty.clear()

        qty_random_number = str(random.randint(10, 50))
        qty.send_keys(qty_random_number)
        print("Qty Of Item:", qty_random_number)

        time.sleep(3)
        price = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//input[@class='p-inputtext p-component p-element ng-valid p-filled ng-touched ng-dirty'][@type='number']"))
        )
        price.click()

        price_random_number = str(random.randint(60, 200))
        price.send_keys(price_random_number)
        print("Price of the item:", price_random_number)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Add']"))
        ).click()

    element = login.find_element(By.XPATH, "//div[contains(text(),'Add Items')]")
    login.execute_script("arguments[0].scrollIntoView();", element)

