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
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Chavakkad']"))
        ).click()

        create_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create']"))
        )
        login.execute_script("arguments[0].click();", create_button)

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

        # Validate snackbar message
        try:
            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
            )
            message = snack_bar.text
            print("✅ Snackbar (success):", message)

        except:
            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            print("❌ Snackbar (error):", message)

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

    


