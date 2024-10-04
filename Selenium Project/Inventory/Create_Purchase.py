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



@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_create_purchase(login):
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
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

    item_list = ["Items", "Item3"]
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

    