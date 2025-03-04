from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.common.exceptions import NoSuchElementException, TimeoutException


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("ViewOrders Drafts Orders Status")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])

def navigate_to_first_page(login):
    try:
        # Wait for the "First" button to be clickable
        first_page_button = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='1']"))
        )
        first_page_button.click()
        print("Navigated back to the first page.")
        time.sleep(5)
       
    except TimeoutException:
        print("Timeout while trying to navigate to the first page.")
    except NoSuchElementException:
        print("First page button not found.")

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("ViewOrders Drafts Orders Status")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])


def test_View_Draft_Orders(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Orders'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@styleclass='text-left']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Draft Orders']") 
        time.sleep(5)
        all_draft_statuses = []
        while True:
            try:
                print("Checking current page for Draft statuses...")
                time.sleep(3)  # Consider removing or minimizing this
                # Wait for the table body to be updated
                table_body = WebDriverWait(login, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//tbody"))
                )
                # Get all rows in the table
                table_rows = table_body.find_elements(By.XPATH, ".//tr")
                print(f"Found {len(table_rows)} rows on this page.")
                # Check if all store statuses are 'Draft'
                for row in table_rows:
                    try:
                        store_status = row.find_element(By.XPATH, './/span[contains(@class, "status-")]').text
                        all_draft_statuses.append(store_status)
                        print(f"Status found: {store_status}")
                        
                        # Assert that the store status is 'Draft'
                        assert store_status == "Draft", f"Store Status '{store_status}' does not match the filter 'Draft'"

                    except Exception as row_error:
                        print(f"Error processing row: {row_error}")
                # Check for the next button and click if available
                try:
                    next_page_button = login.find_element(By.XPATH, "//button[@class='p-ripple p-element p-paginator-next p-paginator-element p-link']")
                    scroll_to_element(login, next_page_button)
                    if next_page_button.is_enabled():
                        next_page_button.click()
                        time.sleep(3)
                        tbody = WebDriverWait(login, 20).until(
                        EC.visibility_of_element_located((By.XPATH, "//tbody"))
                        )
                        scroll_to_element(login, tbody)
                        time.sleep(3) 
                    else:
                        break 
                except NoSuchElementException:
                    break  
                
            except TimeoutException:
                print("A timeout occurred while waiting for the table or next button.")
                break
        print("Finished checking all pages.")
        assert all(all_status == "Draft" for all_status in all_draft_statuses), "Not all statuses are 'Draft'."
        print("All statuses are 'Draft'.")
        time.sleep(3)
        navigate_to_first_page(login)  # Make sure you have this function defined

        # Wait for the first page's table body to be visible
        first_table_body = WebDriverWait(login, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//tbody"))  # Adjust as needed
        )
        scroll_to_element(login, first_table_body)
        time.sleep(2)
        first_row = login.find_element(By.XPATH, ".//tr[1]")
        view_button = first_row.find_element(By.XPATH, "(//button[@label='View'])[1]")  # Adjust the XPath as needed
        scroll_to_element(login, view_button)  
        view_button.click()
        print("Clicked the View button in the first row.")
        time.sleep(3)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        time.sleep(2)
        confirmorder.click()
        time.sleep(5)
        confirmedorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )
        actual_message = confirmedorder.text
        expected_message = "Confirmed"
        print(f"Expected status: '{expected_message}', Actual status: '{actual_message}'")
        assert actual_message == expected_message, f"Expected message '{expected_message} but got Message '{actual_message}'"
        complete_Order = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Complete Order']"))
        )
        scroll_to_element(login, complete_Order)
        time.sleep(2)
        complete_Order.click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        print("Toast Message:", toast_message.text)
        expected_message = "Order Completed Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{toast_message.text}'")
        assert toast_message.text == expected_message, f"Expected toast message '{expected_message}', but got '{toast_message.text}'"
        time.sleep(5)
        
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("ViewOrders Confirmed Orders Status")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])


def test_View_Confirmed_Orders(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Orders'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@styleclass='text-left']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Confirmed Orders']") 
        time.sleep(5)
        all_confirmed_statuses = []
        while True:
            try:
                print("Checking current page for Confirmed statuses...")
                time.sleep(3)  # Consider removing or minimizing this
                # Wait for the table body to be updated
                table_body = WebDriverWait(login, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//tbody"))
                )
                # Get all rows in the table
                table_rows = table_body.find_elements(By.XPATH, ".//tr")
                print(f"Found {len(table_rows)} rows on this page.")
                # Check if all store statuses are 'Confimred'
                for row in table_rows:
                    try:
                        store_status = row.find_element(By.XPATH, './/span[contains(@class, "status-")]').text
                        all_confirmed_statuses.append(store_status)
                        print(f"Status found: {store_status}")
                        
                        # Assert that the store status is 'Draft'
                        assert store_status == "Confirmed", f"Store Status '{store_status}' does not match the filter 'Confirmed'"

                    except Exception as row_error:
                        print(f"Error processing row: {row_error}")
                # Check for the next button and click if available
                try:
                    next_page_button = login.find_element(By.XPATH, "//button[@class='p-ripple p-element p-paginator-next p-paginator-element p-link']")
                    scroll_to_element(login, next_page_button)
                    if next_page_button.is_enabled():
                        next_page_button.click()
                        time.sleep(3)
                        tbody = WebDriverWait(login, 20).until(
                        EC.visibility_of_element_located((By.XPATH, "//tbody"))
                        )
                        scroll_to_element(login, tbody)
                        time.sleep(3) 
                    else:
                        break 
                except NoSuchElementException:
                    break  
                
            except TimeoutException:
                print("A timeout occurred while waiting for the table or next button.")
                break
        print("Finished checking all pages.")
        assert all(all_status == "Confirmed" for all_status in all_confirmed_statuses), "Not all statuses are 'Confirmed'."
        print("All statuses are 'Confirmed'.")
        time.sleep(3)

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("ViewOrders Discarded Orders Status")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])


def test_View_Discarded_Orders(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Orders'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@styleclass='text-left']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Discarded Orders']") 
        time.sleep(5)
        all_discarded_statuses = []
        while True:
            try:
                print("Checking current page for Discarded statuses...")
                time.sleep(3)  # Consider removing or minimizing this
                # Wait for the table body to be updated
                table_body = WebDriverWait(login, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//tbody"))
                )
                # Get all rows in the table
                table_rows = table_body.find_elements(By.XPATH, ".//tr")
                print(f"Found {len(table_rows)} rows on this page.")
                # Check if all store statuses are 'Confimred'
                for row in table_rows:
                    try:
                        store_status = row.find_element(By.XPATH, './/span[contains(@class, "status-")]').text
                        all_discarded_statuses.append(store_status)
                        print(f"Status found: {store_status}")
                        # Assert that the store status is 'Discarded'
                        assert store_status == "Discarded", f"Store Status '{store_status}' does not match the filter 'Discarded'"

                    except Exception as row_error:
                        print(f"Error processing row: {row_error}")
                # Check for the next button and click if available
                try:
                    next_page_button = login.find_element(By.XPATH, "//button[@class='p-ripple p-element p-paginator-next p-paginator-element p-link']")
                    scroll_to_element(login, next_page_button)
                    if next_page_button.is_enabled():
                        next_page_button.click()
                        time.sleep(3)
                        tbody = WebDriverWait(login, 20).until(
                        EC.visibility_of_element_located((By.XPATH, "//tbody"))
                        )
                        scroll_to_element(login, tbody)
                        time.sleep(3) 
                    else:
                        break 
                except NoSuchElementException:
                    break  
                
            except TimeoutException:
                print("A timeout occurred while waiting for the table or next button.")
                break
        print("Finished checking all pages.")
        assert all(all_status == "Discarded" for all_status in all_discarded_statuses), "Not all statuses are 'Discarded'."
        print("All statuses are 'Discarded'.")
        time.sleep(3)

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("ViewOrders Canceled Orders Status")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])


def test_View_Canceled_Orders(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Orders'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@styleclass='text-left']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Canceled Orders']") 
        time.sleep(5)
        all_canceled_statuses = []
        while True:
            try:
                print("Checking current page for Canceled statuses...")
                time.sleep(3)  # Consider removing or minimizing this
                # Wait for the table body to be updated
                table_body = WebDriverWait(login, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//tbody"))
                )
                # Get all rows in the table
                table_rows = table_body.find_elements(By.XPATH, ".//tr")
                print(f"Found {len(table_rows)} rows on this page.")
                # Check if all store statuses are 'Canceled'
                for row in table_rows:
                    try:
                        store_status = row.find_element(By.XPATH, './/span[contains(@class, "status-")]').text
                        all_canceled_statuses.append(store_status)
                        print(f"Status found: {store_status}")
                        # Assert that the store status is 'Canceled'
                        assert store_status == "Canceled", f"Store Status '{store_status}' does not match the filter 'Canceled'"

                    except Exception as row_error:
                        print(f"Error processing row: {row_error}")
                # Check for the next button and click if available
                try:
                    next_page_button = login.find_element(By.XPATH, "//button[@class='p-ripple p-element p-paginator-next p-paginator-element p-link']")
                    scroll_to_element(login, next_page_button)
                    if next_page_button.is_enabled():
                        next_page_button.click()
                        time.sleep(3)
                        tbody = WebDriverWait(login, 20).until(
                        EC.visibility_of_element_located((By.XPATH, "//tbody"))
                        )
                        scroll_to_element(login, tbody)
                        time.sleep(3) 
                    else:
                        break 
                except NoSuchElementException:
                    break  
                
            except TimeoutException:
                print("A timeout occurred while waiting for the table or next button.")
                break
        print("Finished checking all pages.")
        assert all(all_status == "Canceled" for all_status in all_canceled_statuses), "Not all statuses are 'Canceled'."
        print("All statuses are 'Canceled'.")
        time.sleep(3)

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("ViewOrders Completed Orders Status")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])


def test_View_Completed_Orders(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Orders'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@styleclass='text-left']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Completed Orders']") 
        time.sleep(5)
        all_completed_statuses = []
        while True:
            try:
                print("Checking current page for Completed statuses...")
                time.sleep(3)  # Consider removing or minimizing this
                # Wait for the table body to be updated
                table_body = WebDriverWait(login, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//tbody"))
                )
                # Get all rows in the table
                table_rows = table_body.find_elements(By.XPATH, ".//tr")
                print(f"Found {len(table_rows)} rows on this page.")
                # Check if all store statuses are 'Completed'
                for row in table_rows:
                    try:
                        store_status = row.find_element(By.XPATH, './/span[contains(@class, "status-")]').text
                        all_completed_statuses.append(store_status)
                        print(f"Status found: {store_status}")
                        # Assert that the store status is 'Completed'
                        assert store_status == "Completed", f"Store Status '{store_status}' does not match the filter 'Completed'"

                    except Exception as row_error:
                        print(f"Error processing row: {row_error}")
                # Check for the next button and click if available
                try:
                    next_page_button = login.find_element(By.XPATH, "//button[@class='p-ripple p-element p-paginator-next p-paginator-element p-link']")
                    scroll_to_element(login, next_page_button)
                    if next_page_button.is_enabled():
                        next_page_button.click()
                        time.sleep(3)
                        tbody = WebDriverWait(login, 20).until(
                        EC.visibility_of_element_located((By.XPATH, "//tbody"))
                        )
                        scroll_to_element(login, tbody)
                        time.sleep(3) 
                    else:
                        break 
                except NoSuchElementException:
                    break  
                
            except TimeoutException:
                print("A timeout occurred while waiting for the table or next button.")
                break
        print("Finished checking all pages.")
        assert all(all_status == "Completed" for all_status in all_completed_statuses), "Not all statuses are 'Completed'."
        print("All statuses are 'Completed'.")
        time.sleep(3)

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  