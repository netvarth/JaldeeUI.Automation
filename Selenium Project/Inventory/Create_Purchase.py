import time
import uuid

from Framework.common_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Framework.common_dates_utils import *

def add_date(years_to_add):
    future_date = datetime.now().replace(year=datetime.now().year + years_to_add)
    return [future_date.year, future_date.strftime("%b"), future_date.day]

def title_to_item(title_case_string):
    return title_case_string.title()


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Create purchase and push to Expense")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_create_purchase(login):
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//img)[6]"))
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
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Geetha']"))
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

    time.sleep(2)
    Inventory_Catalog = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='catalog1']"))
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
    bill_number = random_number
    login.find_element(By.XPATH, "//p-calendar//input[@type='text']").click()

    Today_Date = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]"))
    )
    Today_Date.click()
    print("Date:", Today_Date.text)

    login.find_element(By.XPATH, "//textarea[@placeholder='Notes to Vendor']").send_keys("Medcc  Supplied item ")

    element1 = login.find_element(By.XPATH, "//span[normalize-space()='Add Items']")
    login.execute_script("arguments[0].scrollIntoView();", element1)

    # item_list = ["Items,Item3"]
    # random_batch_number = str(random.randint(100, 1000))
    time.sleep(3)
    # for i in range(len(item_list)):
    #     print(item_list[i])
    #     item_xpath = item_xpath = f"//div[@class='d-flex justify-content-between fw-bold']//div[@class='ng-star-inserted'][normalize-space()='{title_to_item(item_list[i])}']"

    #     time.sleep(2)                                    
    #     WebDriverWait(login, 30).until(
    #         EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search items']"))
    #     ).send_keys("it")
 
    #     time.sleep(3)
    #     WebDriverWait(login, 10).until(
    #         EC.presence_of_element_located((By.XPATH, item_xpath))
    #     ).click()

    item_list = ["items,item3"]
    random_batch_number = str(random.randint(100, 1000))
    time.sleep(3)
    for i in range(len(item_list)):
        print(item_list[i])
        item_xpath = f"//div[@class='d-flex justify-content-between fw-bold']//div[@class='ng-star-inserted'][normalize-space()='{title_to_item(item_list[i])}']"
        time.sleep(2)                                    
        WebDriverWait(login, 30).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search items']"))
        ).send_keys("it")
        print("Searched for item")

        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, item_xpath))
        ).click()
        print("Clicked on item")

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
        mrpprice.clear()
        mrpprice_random_number = str(random.randint(100, 200))
        mrpprice.send_keys(mrpprice_random_number)
        print("MRP of the item:", mrpprice_random_number)


        time.sleep(2)
        price = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[contains(@class,'item-price')])[2]"))
        )
        price.click()
        price.clear()
        price_random_number = str(random.randint(40, 90))
        price.send_keys(price_random_number)
        print("Price of the item:", price_random_number)


        # time.sleep(1)
        # WebDriverWait(login,10).until(
        #     EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel= 'displayName']"))
        # ).click()

        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='%']"))
        # ).click()

        # time.sleep(1)
        # WebDriverWait(login ,10).until(
        #     EC.presence_of_element_located((By.XPATH, "//input[contains(@class,'discount')]"))
        # ).send_keys("5")
        
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
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[@aria-haspopup='menu'][normalize-space()='Actions'])[1]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[2]"))
    ).click()

    toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_detail.text
    print("toast_Message:", message)

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='ng-star-inserted'])[7]"))
    ).click()

    time.sleep(2)
    expenses_card = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='Expenses'])[1]"))
    )
    login.execute_script("arguments[0].click();", expenses_card)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[contains(text(),'View')])[1]"))
    ).click()

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[@src='./assets/images/finance/uil.svg']"))
    ).click()

    time.sleep(3)

    bill_input = WebDriverWait(login, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Purchase Bill#']"))
    )

    # Get the value (this will give the dynamically entered bill number)
    bill_value = bill_input.get_attribute("value")
    print("Entered Bill Number:", bill_value)

    print(f"Expected bill_number: '{bill_value}', Actual bill_number: '{bill_number}'")
    # Assert that the patient's name matches
    assert bill_number == bill_value, f"Expected bill_number '{bill_value}', but found '{bill_number}' on invoice."

    time.sleep(5)

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Sales Price Higher than MRP with Toast Message Validation")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_sales_price_higher_than_mrp(login):
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//img)[6]"))
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
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Geetha']"))
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

    time.sleep(3)
    Inventory_Catalog = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Inventory_catalog']"))
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

    login.find_element(By.XPATH, "//textarea[@placeholder='Notes to Vendor']").send_keys("Medcc Supplied item")

    element1 = login.find_element(By.XPATH, "//span[normalize-space()='Add Items']")
    login.execute_script("arguments[0].scrollIntoView();", element1)

    item_list = ["Item3"]
    random_batch_number = str(random.randint(5, 99))

    for i in range(len(item_list)):
        print(item_list[i])
        item_xpath = f"//div[@class='d-flex justify-content-between fw-bold']//div[@class='ng-star-inserted'][normalize-space()='{item_list[i]}']"
                                            
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search items']"))
        ).send_keys("item")

        time.sleep(2)
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

        time.sleep(2)
        
        # Capturing MRP and Sales Price with Sales Price greater than MRP
        mrpprice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            "(//input[contains(@class,'item-price')])[1]"))
        )
        mrpprice.click()
        mrpprice.clear()
        mrpprice_random_number = str(random.randint(40, 60))  # Setting MRP
        mrpprice.send_keys(mrpprice_random_number)
        print("MRP of the item:", mrpprice_random_number)

        time.sleep(2)
        price = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[contains(@class,'item-price')])[2]"))
        )
        price.click()
        price.clear()
        price_random_number = str(random.randint(61, 100))  # Sales price is set higher than MRP
        price.send_keys(price_random_number)
        print("Price of the item:", price_random_number)

        # Validation: Assert that MRP should not be less than Sales Price
        assert float(mrpprice_random_number) < float(price_random_number), f"Test failed: Sales Price {price_random_number} is not greater than MRP {mrpprice_random_number}"
        print(f"Validation Passed: Sales Price ({price_random_number}) is higher than MRP ({mrpprice_random_number})")
        

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Add']"))
        ).click()

        # Capturing Toast Message after validation
        time.sleep(1)
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        toast_text = toast_message.text
        print("Toast Message:", toast_text)

        # Assert that the toast message contains the expected text
        expected_toast_message = "Purchase price should not exceed than MRP"
        assert expected_toast_message in toast_text, f"Expected toast message not found! Got: {toast_text}"
        print("Toast message validation passed!")

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Discount in percentage")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_discount_in_percentage(login):
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//img)[6]"))
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
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Geetha']"))
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
    time.sleep(2)
    Inventory_Catalog = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Inventory_catalog']"))
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

    login.find_element(By.XPATH, "//textarea[@placeholder='Notes to Vendor']").send_keys("Medcc  Supplied item ")

    element1 = login.find_element(By.XPATH, "//span[normalize-space()='Add Items']")
    login.execute_script("arguments[0].scrollIntoView();", element1)

    item_list = ["Item3"]
    random_batch_number = str(random.randint(5, 99))

    for i in range(len(item_list)):
        print(item_list[i])
        item_xpath = item_xpath = f"//div[@class='d-flex justify-content-between fw-bold']//div[@class='ng-star-inserted'][normalize-space()='{title_to_item(item_list[i])}']"
                                            
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search items']"))
        ).send_keys("item")

        time.sleep(2)
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
        mrpprice.clear()
        mrpprice_random_number = str(random.randint(60, 200))
        mrpprice.send_keys(mrpprice_random_number)
        print("MRP of the item:", mrpprice_random_number)


        time.sleep(2)
        price = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[contains(@class,'item-price')])[2]"))
        )
        price.click()
        price.clear()
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
        discount_percentage = WebDriverWait(login ,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@class,'discount')]"))
        )
        discount_percentage.click()
        discount_percentage.clear()
        discount_percentage.send_keys("5")
        
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Add']"))
    ).click()
    time.sleep(3) 

    after_discount = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//tbody)[2]//td[11]"))
    )

    amount_after_discount = float(after_discount.text.replace(',', '').strip())

    before_discount = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//tbody)[2]//td[9]"))
    )
    amount_before_discount = float(before_discount.text.replace(',', '').strip())


   
    discount_percentage = 5  
    expected_bill_amount = amount_before_discount - (amount_before_discount * (discount_percentage / 100))
    print("Expected Bill Amount:", expected_bill_amount)
    print("Actual amount after discount:", amount_after_discount)
    # Assertion to verify discount applied correctly
    assert round(amount_after_discount, 2) == round(expected_bill_amount, 2), "Discount amount is incorrect!"

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Discount in amount")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_discount_in_amount(login):
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//img)[6]"))
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
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Geetha']"))
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
    time.sleep(2)
    Inventory_Catalog = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Inventory_catalog']"))
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

    login.find_element(By.XPATH, "//textarea[@placeholder='Notes to Vendor']").send_keys("Medcc  Supplied item ")

    element1 = login.find_element(By.XPATH, "//span[normalize-space()='Add Items']")
    login.execute_script("arguments[0].scrollIntoView();", element1)

    item_list = ["Item3"]
    random_batch_number = str(random.randint(5, 99))

    for i in range(len(item_list)):
        print(item_list[i])
        item_xpath = item_xpath = f"//div[@class='d-flex justify-content-between fw-bold']//div[@class='ng-star-inserted'][normalize-space()='{title_to_item(item_list[i])}']"
                                            
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search items']"))
        ).send_keys("item")

        time.sleep(2)
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
        mrpprice.clear()
        mrpprice_random_number = str(random.randint(60, 200))
        mrpprice.send_keys(mrpprice_random_number)
        print("MRP of the item:", mrpprice_random_number)


        time.sleep(2)
        price = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[contains(@class,'item-price')])[2]"))
        )
        price.click()
        price.clear()
        price_random_number = str(random.randint(40, 100))
        price.send_keys(price_random_number)
        print("Price of the item:", price_random_number)


        time.sleep(1)
        # WebDriverWait(login,10).until(
        #     EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel= 'displayName']"))
        # ).click()

        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='%']"))
        # ).click()

        time.sleep(1)
        discount_percentage = WebDriverWait(login ,10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@class,'discount')]"))
        )
        discount_percentage.click()
        discount_percentage.clear()
        discount_percentage.send_keys("100")
        
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Add']"))
    ).click()
    time.sleep(3) 

    after_discount = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//tbody)[2]//td[11]"))
    )

    amount_after_discount = float(after_discount.text.replace(',', '').strip())
    before_discount = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//tbody)[2]//td[9]"))
    )
    amount_before_discount = float(before_discount.text.replace(',', '').strip())
   
    discount_amount = 100  
    expected_bill_amount = amount_before_discount - (discount_amount)
    print("Expected Bill Amount:", expected_bill_amount)
    print("Actual amount after discount:", amount_after_discount)
    # Assertion to verify discount applied correctly
    assert round(amount_after_discount, 2) == round(expected_bill_amount, 2), "Discount amount is incorrect!"


    
        