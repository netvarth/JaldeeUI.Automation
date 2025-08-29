import time
import allure

from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create Order")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_create_order(login):

 
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//img)[5]"))
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
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[5]"))
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
    item_names_to_select = ['Items']
    item_prices = [115]
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



