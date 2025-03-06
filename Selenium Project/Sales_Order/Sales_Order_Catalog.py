import time
import allure

from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.common.exceptions import ElementClickInterceptedException



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Creating the item in sales order")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_sales_order_catalog(login):
   
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[contains(text(),'Catalogs')])[1]"))    
    ).click()

    time.sleep(1)

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[@class='p-ripple p-element p-button p-component'])[1]"))
    ).click()

    time.sleep(2)

    catalog_name = "Catalog_" + str(uuid.uuid4())[:6]
    print(catalog_name)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Enter Catalog Name'])[1]"))
    ).send_keys(catalog_name)
    
    dropdown = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    )
    dropdown.click()
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='B&B Stores'])[1]"))
    ).click()
   
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
    ).click()
    time.sleep(1)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Yes'])[1]"))
    ).click()
 
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Save & Next'])[1]"))
    ).click()

    time.sleep(3)
 
    start_index = 2   # First checkbox to select
    end_index = 4     # Last checkbox to select

    # Find all checkboxes using XPath
    checkboxes = login.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'mat-mdc-checkbox')]")

    # Iterate and select checkboxes within the range
    for i in range(start_index - 1, min(end_index, len(checkboxes))):  # Adjusting for 0-based index
        if not checkboxes[i].is_selected():  # Check if not already selected
            checkboxes[i].click()

    # Confirm selections
    selected_checkboxes = [cb.get_attribute("id") for cb in checkboxes if cb.is_selected()]
    print(f"Selected checkboxes: {selected_checkboxes}")

    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[2]"))
    ).click()

    
    # Wait for the dialog to appear
    dialog = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "(//p[contains(text(),'Warning: Once added to the catalog, item’s attribu')])[1]"))
    )

    # Extract the warning message
    warning_text = dialog.text
    print("message :", warning_text)
    # Expected message
    expected_message = "Warning: Once added to the catalog, item’s attributes cannot be edited. Do you want to proceed?"

    # Assert the warning message  
    assert warning_text.strip() == expected_message, f"Expected '{expected_message}', but got '{warning_text}'"

    # Click the "Yes" button
    yes_button = login.find_element(By.XPATH, "(//button[normalize-space()='Yes'])[1]")
    yes_button.click()

    time.sleep(5)

