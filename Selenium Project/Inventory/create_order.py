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


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create Order")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_create_order(login):

 
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
            (By.XPATH, "//div[@class='p-multiselect-label p-placeholder']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Swathy Order Catalog']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "(//span[normalize-space()='Next'])[1]"))
    ).click()

    item_names_to_select = ['Item4', 'Item3', 'items']
    item_prices= [5, 1.3, 1.5]
    sum=0

    for i in range(len(item_names_to_select)):
    # for item_name, item_price in zip(item_names_to_select, item_prices):
        item_name= item_names_to_select[i]
        item_price= item_prices[i]
        print(item_name)


    
    
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Search items']"))
        ).send_keys(item_name)

        item_xpath = f"//div[contains(text(),'{item_name.title()}')]"
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, item_xpath))
        ).click()

        qty_xpath=f"(//input[@min='1'])[{i+1}]"
        qty = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, qty_xpath))
            )
        qty.click()
        qty.clear()

        qty_random_number = str(random.randint(5,10))
        qty.send_keys(qty_random_number)
        print("Qty Of Item:", qty_random_number) 
        total=item_price*float(qty_random_number)
        print("total:",total)
        sum=sum+total
        print("sum: ", sum)
        # Locate the table rows
        row_xpath=f"//tbody[@class='p-element p-datatable-tbody']/tr[{i+1}]"
        print(row_xpath)
        row= login.find_element(By.XPATH, row_xpath)

        # Loop through each row and extract the text from the 5th column
        fifth_column = row.find_elements(By.TAG_NAME, "td")
        len(fifth_column)
        print(fifth_column[4].text)
        # Total_element = login.find_element(By.XPATH, './/td[contains(@input, "_ngcontent-tap")]')
        total_text = fifth_column[4].text
        # expected_status = "DRAFT"
        expected_total = f"{total:.2f}"

        print(f"Expected Total is: '{expected_total}', Total shown is: '{total_text}'")

        # Assert that the status is "DRAFT"
        assert total_text == str(expected_total), f"Expected Total to be {expected_total}, but got '{total_text}'"

    time.sleep(5)

    # Verify the summary total
    summary_total_element = WebDriverWait(login, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='fw-bold mt-2']//span[@class='min-width-span-value']"))
    )
    summary_total_text = summary_total_element.text.replace('₹', '').strip()
    summary_total = float(summary_total_text)

    print(f"Expected Total Sum: {sum:.2f}")
    print(f"Actual Summary Total: {summary_total:.2f}")

    # Perform the final assertion
    assert round(sum, 2) == round(summary_total, 2), f"Expected Summary Total to be {sum:.2f}, but got '{summary_total_text}'"
