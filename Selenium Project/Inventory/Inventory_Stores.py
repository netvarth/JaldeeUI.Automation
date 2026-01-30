import random
import time
import uuid

import allure
import pytest

from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException


@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Store Creation")
def test_store_creation(login):
    try:
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[3]"))
        ).click()

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
                (By.XPATH, "//span[normalize-space()='Medical Lab']"))
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


        invoice_prefix = "KT_" + str(uuid.uuid4())[:6]
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

        create_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create']"))
        )
        login.execute_script("arguments[0].click();", create_button)

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(3)


    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  

@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Rename Store")
def test_rename_store(login):
    try:
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
        ).click()

        time.sleep(5)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Stores']"))
        ).click()

        time.sleep(2)
        # Click on Edit for the first store
        wait_and_click(login, By.XPATH, "(//span[@class='p-button-label ng-star-inserted'][normalize-space()='Edit'])[1]")

        time.sleep(2)

        # Locate store name field
        store_name_input = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='storeName']"))
        )

        # Clear old name
        store_name_input.clear()

        # Enter new store name
        new_store_name = "Renamed_" + str(uuid.uuid4())[:6]
        store_name_input.send_keys(new_store_name)
        print("New Store Name:", new_store_name)

        time.sleep(2)

        # Click Update button
        update_button = WebDriverWait(login, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']"))
        )
        login.execute_script("arguments[0].click();", update_button)

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(3)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e

@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Disable and Re-enable Store")
def test_disable_and_enable_store(login):
    try:
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
        ).click()

        time.sleep(5)

        # Navigate to Stores
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Stores']")
            )
        ).click()

        time.sleep(2)

        # View first store
        wait_and_click(login, By.XPATH, "(//span[@class='p-button-label ng-star-inserted'][normalize-space()='View'])[1]")
        time.sleep(2)

        # Disable store
        wait_and_click(login, By.XPATH, "(//span[@class='p-button-label ng-star-inserted'])[1]")

        # Capture the snackbar message
        message = get_snack_bar_message(login)
        print("Snack Bar Message (Disable):", message)

        time.sleep(2)

        # Back to store list
        wait_and_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")
        time.sleep(2)

        # ✅ Assert status is Inactive
        status_element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//table[@role='table']//tbody/tr[1]/td[@class='desktop-only']/div")
            )
        )
        status_text = status_element.text.strip()
        print("Status after disable:", status_text)
        assert status_text == "Inactive", f"Expected 'Inactive' but got '{status_text}'"

        # ---------- Re-enable (to reset state) ----------
        # View first store again
        wait_and_click(login, By.XPATH, "(//span[@class='p-button-label ng-star-inserted'][normalize-space()='View'])[1]")
        time.sleep(2)

        # Enable store
        wait_and_click(login, By.XPATH, "(//span[@class='p-button-label ng-star-inserted'])[1]")
        message = get_snack_bar_message(login)
        print("Snack Bar Message (Enable):", message)

        time.sleep(2)

        # Back again to store list
        wait_and_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")
        time.sleep(2)

        # ✅ Assert status is Active
        status_element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//table[@role='table']//tbody/tr[1]/td[@class='desktop-only']/div")
            )
        )
        status_text = status_element.text.strip()
        print("Status after enable:", status_text)
        assert status_text == "Active", f"Expected 'Active' but got '{status_text}'"

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e

@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@pytest.mark.xfail(reason="Create button incorrectly enabled without selecting Type")
@allure.title("Store Creation")
def test_store_creation_exculded_type(login):
    try:
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
        ).click()

        time.sleep(5)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Stores']"))
        ).click()

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Store']"))
        ).click()

        time.sleep(2)
        store_name = "Store_" + str(uuid.uuid4())[:6]
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='storeName']"))
        ).send_keys(store_name)

        time.sleep(2)
        email = f"{store_name}{test_mail}"
        random_number = str(random.randint(1111111, 9999999))
        phonenumber = f"{555}{random_number}"

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        ).send_keys(phonenumber)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
        ).send_keys(email)

        invoice_prefix = "KT_" + str(uuid.uuid4())[:6]
        print(invoice_prefix)
        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Invoice prefix']"))  
        ).send_keys(invoice_prefix)

        time.sleep(2)
        # Select Location
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Location']"))
        ).click()
        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[normalize-space()='West Nada'])[1]"))
        ).click()

        time.sleep(2)

        # Assert Create button is still disabled
        create_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create']"))
        )
        is_disabled_after = create_button.get_attribute("disabled")
        btn_class_after = create_button.get_attribute("class")

        assert (is_disabled_after is not None) or ("p-disabled" in btn_class_after), \
            "❌ Create button is enabled even though Type was not selected!"
        print("✅ Create button remained disabled when mandatory field 'Type' was skipped")                                   




    except Exception as e: 
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e

@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Store Filter Location")
def test_store_filter_location(login):
    try:
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
        ).click()

        time.sleep(5)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Stores']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='pi pi-filter-fill']"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Location']"))
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='West Nada'])[1]"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Apply']"))
        ).click()

        # Wait for the table to load after applying the filter
        time.sleep(5)

        # Locate the table body containing the filtered results
        table_body = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//tbody"))
        )

        # Get all rows in the table
        table_rows = table_body.find_elements(By.XPATH, ".//tr")

        found_locations = []
        for idx, row in enumerate(table_rows, start=1):
            # ⚠️ Use relative XPath (.) instead of absolute //tbody
            store_location = row.find_element(By.XPATH, ".//td[@class='desktop-only'][1]").text.strip()
            found_locations.append(f"Row {idx}: {store_location}")

            assert store_location == "West Nada", \
                f"❌ Store location '{store_location}' does not match the filter 'West Nada'"

        # ✅ Attach results to Allure for better reporting
        allure.attach(
            "\n".join(found_locations),
            name="Filtered Store Locations",
            attachment_type=AttachmentType.TEXT
        )

        print("✅ All stores matched filter 'West Nada'")
        print("\n".join(found_locations))

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e
 
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Store Filter_Status")
def test_store_filter_storestatus(login):
    try:
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
        ).click()

        time.sleep(5)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Stores']")
            )
        ).click()

        time.sleep(2)

        # ---------------- Apply Active Filter ----------------
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='pi pi-filter-fill']"))
        ).click()

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Status']"))
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Active']"))
        ).click()

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Apply']"))
        ).click()

        time.sleep(3)

        # Assert all rows show Active
        table_body = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//tbody"))
        )
        table_rows = table_body.find_elements(By.XPATH, ".//tr")

        active_results = []
        for idx, row in enumerate(table_rows, start=1):
            status = row.find_element(By.XPATH, ".//td[@class='desktop-only'][3]").text.strip()
            active_results.append(f"Row {idx}: {status}")
            assert status == "Active", f"❌ Row {idx} status '{status}' does not match 'Active'"

        allure.attach("\n".join(active_results), "Active Filter Results", attachment_type=AttachmentType.TEXT)
        print("✅ All stores are Active after filter")
        
        # ---------------- Apply Inactive Filter ----------------
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//i[@class='pi pi-filter-fill']"))
        ).click()

        time.sleep(1)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Reset'])[1]")

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Inactive']"))
        ).click()

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Apply']"))
        ).click()

        time.sleep(3)

        # Assert all rows show Inactive
        table_body = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//tbody"))
        )
        table_rows = table_body.find_elements(By.XPATH, ".//tr")

        inactive_results = []
        for idx, row in enumerate(table_rows, start=1):
            status = row.find_element(By.XPATH, ".//td[@class='desktop-only'][3]").text.strip()
            inactive_results.append(f"Row {idx}: {status}")
            assert status == "Inactive", f"❌ Row {idx} status '{status}' does not match 'Inactive'"

        allure.attach("\n".join(inactive_results), "Inactive Filter Results", attachment_type=AttachmentType.TEXT)
        print("✅ All stores are Inactive after filter")


    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e

    

@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
@allure.title("Disable the Expense_Conversion")
def test_Expense_Conversion(login):
    try:
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
        ).click()

        time.sleep(5)

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Stores']")
            )
        ).click()

        time.sleep(2)

        while True:
            try:
                store = login.find_element(
                    By.XPATH,
                    "//tr[.//div[@class='fw-bold' and normalize-space()='B&B Stores']]"
                )

                store.find_element(
                    By.XPATH,
                    ".//span[normalize-space()='Edit']"
                ).click()
                break

            except NoSuchElementException:
                next_btn = login.find_element(
                    By.XPATH,
                    "//button[contains(@class,'p-paginator-next') and not(contains(@class,'p-disabled'))]"
                )

                # If next button is disabled → stop to avoid infinite loop
                if "p-disabled" in next_btn.get_attribute("class"):
                    raise Exception("B&B Stores not found in any page")

                next_btn.click()

                # Wait for table to reload
                WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//tbody//tr")
                    )
                )

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='changeSts_ORD_storeCre-button']")
        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//img)[3]")
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionNav_ORD_Inventory'])[5]"))
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
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]"))
        )
        store.click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@placeholder='Select Vendor']//div[@aria-label='dropdown trigger']"))
        ).click()

        Select_supplier = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='SBT PVT Limited'])[1]"))
        )
        Select_supplier.click()
        print("Select Supplier:", Select_supplier.text)

        login.find_element(By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']").click()

        time.sleep(2)
        Inventory_Catalog = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Catalog_Inventory'])[1]"))
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

        login.find_element(By.XPATH, "//textarea[@placeholder='Notes to Vendor']").send_keys("Supplied item ")

        time.sleep(3)

        item_list = ["Item_1"]
        random_batch_number = str(random.randint(100, 1000))
        time.sleep(3)
        
        for item in item_list:
        
            print(item)
            item_xpath = f"//div[@class='d-flex justify-content-between fw-bold']//div[@class='ng-star-inserted'][normalize-space()='{item}']"
            time.sleep(2)

            WebDriverWait(login, 30).until(
                EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Search items'])[1]"))
            ).send_keys("it")
            print("Searched for item")

            time.sleep(3)
            WebDriverWait(login, 20).until(
                EC.presence_of_element_located((By.XPATH, item_xpath))
            ).click()
            print("Clicked on item")

            time.sleep(1)
            WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//input[@type='radio'])[1]")) 
            ).click()

            WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "(//i[@class='pi pi-check'])[1]"))
            ).click()

            time.sleep(3)
            batch_number = WebDriverWait(login, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//td//div[@class='ng-star-inserted']//input[@type='text' and contains(@class, 'p-inputtext')]")
                )
            )
            batch_number.click()

            random_number = str(random.randint(5, 99))
            batch_number.send_keys(random_batch_number)
            print("Batch_Number:", random_batch_number)

            WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//p-dropdown[@placeholder='Item Units']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']"))
            ).click()

            time.sleep(2)
            WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Box of 10']"))
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

            qty_random_number = str(random.randint(15, 50))
            qty.send_keys(qty_random_number)
            print("Qty Of Item:", qty_random_number)

            free_qty = WebDriverWait(login, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//input[contains(@class,'free-quantity')]"))
            )
            free_qty.click()
            free_qty.clear()

            free_qty_random_number = str(random.randint(1, 3))
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

        element = login.find_element(By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]")
        login.execute_script("arguments[0].scrollIntoView();", element)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='B&B Stores'])[1]"))
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
        
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//img)[4]")
        wait_and_locate_click(
            login, By.XPATH, "(//div[@id='actionRoute_FIN_Dashbord'])[8]"
        )

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[@id='btnMenu_FIN_Expense'])[1]"))
        ).click()

        wait_and_locate_click(login, By.XPATH, "//*[@id='btnConvert_FIN_Expense']")
        time.sleep(2)

        wait_and_locate_click(
            login, By.XPATH, "(//button[@id='btnConvert_FIN_PayableDetails'])[1]"
        )

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(2)

        wait_and_locate_click(
            login, By.XPATH, "(//img)[3]"
        )

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//div[@id='actionNav_ORD_Inventory'])[2]"
        )

        time.sleep(2)
        while True:
            try:
                store = login.find_element(
                    By.XPATH,
                    "//tr[.//div[@class='fw-bold' and normalize-space()='B&B Stores']]"
                )

                store.find_element(
                    By.XPATH,
                    ".//span[normalize-space()='Edit']"
                ).click()
                break

            except NoSuchElementException:
                next_btn = login.find_element(
                    By.XPATH,
                    "//button[contains(@class,'p-paginator-next') and not(contains(@class,'p-disabled'))]"
                )

                # If next button is disabled → stop to avoid infinite loop
                if "p-disabled" in next_btn.get_attribute("class"):
                    raise Exception("B&B Stores not found in any page")

                next_btn.click()

                # Wait for table to reload
                WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//tbody//tr")
                    )
                )
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='changeSts_ORD_storeCre-button']")
        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(3)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e