from Framework.common_utils import *
from Framework.common_dates_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Orderlog")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Orderlog(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search customers']", "5555430917")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 10']")
        time.sleep(2)
        customer_name = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='fw-bold ng-star-inserted'][normalize-space()='Joseph Hernandez']"))
        )
        actual_customer_name = customer_name.text
        print(actual_customer_name)
        store_name = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='p-dropdown p-component'])[3]"))
        )
        actual_storename = store_name.text
        print(actual_storename)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[2]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        time.sleep(2)
        confirmorder.click()
        time.sleep(5)

        #####Confirmed Log#########
        confirmedorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )
        actual_message = confirmedorder.text
        print(actual_message)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Log']")
        time.sleep(2)
        log_table = login.find_element(By.XPATH, "(//tbody)[2]//tr//td[4]")
        confirmedlogs = log_table.text
        print(confirmedlogs)
        assert f"Order created for '{actual_customer_name}' in store '{actual_storename}' with status Order {actual_message}" in confirmedlogs, "Log entry not found!"
        wait_and_locate_click(login, By.XPATH, "//i[@class='fa fa-times']")
        time.sleep(3)

        ########Completed Order Log ##########
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
        order_id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='order-id ng-star-inserted']"))
        )
        full_order_id = order_id.text  
        actual_order_formatid = full_order_id.replace('#', '').strip()  
        parts = actual_order_formatid.split()  
        actual_order_id = f"{parts[0]} '{parts[1]}'"  
        print(actual_order_id) 
        completedorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )
        completedorder_message = completedorder.text
        print(completedorder_message)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Log']")
        time.sleep(2)
        logs_table = login.find_element(By.XPATH, "(//tbody)[2]//tr[1]//td[4]")
        completedlogs = logs_table.text
        print(completedlogs)
        assert f"{actual_order_id} status changed to 'Order {completedorder_message}' in completedlogs," "Log entry not found!"
        wait_and_locate_click(login, By.XPATH, "//i[@class='fa fa-times']")
        time.sleep(3)

        ###########Invoice Log##########
        create_Invoice = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Invoice']"))
        )
        createinvoicelog = create_Invoice.text
        print(createinvoicelog)
        create_Invoice.click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Log']")
        time.sleep(2)
        logs_table = login.find_element(By.XPATH, "(//tbody)[3]//tr[1]//td[2]")
        invoicelogs = logs_table.text
        print(invoicelogs)
        assert f"{createinvoicelog}  in invoicelogs," "Log entry not found!"
        print(f"{createinvoicelog}  in invoicelogs")
        wait_and_locate_click(login, By.XPATH, "//i[@class='fa fa-times']")
        time.sleep(3)

        #########View Invoice Log############
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='View Invoice']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//button[@class='p-element log-btn me-1 p-button p-component ng-star-inserted'])[1]")
        time.sleep(3)
        logs_table = login.find_element(By.XPATH, "(//tbody)[3]//tr//td[4]")
        viewinvoiceslogs = logs_table.text
        print(viewinvoiceslogs)
        assert f"Invoice created for the {actual_order_id} in viewinvoiceslogs," "Log entry not found!"
    except Exception as e:  
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Orderlog With Editlog")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Order_Editlog(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Search customers']", "5555430917")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 10']")
        time.sleep(2)
        customer_name = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='fw-bold ng-star-inserted'][normalize-space()='Joseph Hernandez']"))
        )
        actual_customer_name = customer_name.text
        print(actual_customer_name)
        store_name = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='p-dropdown p-component'])[3]"))
        )
        actual_storename = store_name.text
        print(actual_storename)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[2]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        saveasdraft = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Save as draft']"))
        )
        scroll_to_element(login, saveasdraft)
        time.sleep(2)
        saveasdraft.click()
        time.sleep(5)
        saveasdraft = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Draft ng-star-inserted']"))
        )
        Draft_text = saveasdraft.text
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Log']")
        time.sleep(2)
        log_table = login.find_element(By.XPATH, "(//tbody)[2]//tr//td[4]")
        saveasdraftlogs = log_table.text
        assert f"Order created for '{actual_customer_name}' in store '{actual_storename}' with status {Draft_text}" in saveasdraftlogs, "Log entry not found!"
        wait_and_locate_click(login, By.XPATH, "//i[@class='fa fa-times']")
        time.sleep(3)
        #####Edit Log#########
    
        Editorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Edit Order']"))
        )
        Editorder.click()
        time.sleep(3)
        Additem = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Add Item']"))
        )
        Additem.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[3]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        updateorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Update Order']"))
        )
        scroll_to_element(login, updateorder)
        time.sleep(2)
        updateorder.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
        time.sleep(2)
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        print("Toast Message:", toast_message.text)
        order_id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='order-id ng-star-inserted']"))
        )
        full_order_id = order_id.text  
        actual_order_formatid = full_order_id.replace('#', '').strip()  
        parts = actual_order_formatid.split()  
        actual_order_id = f"{parts[0]} '{parts[1]}'"  
        print(actual_order_id) 
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Log']")
        time.sleep(2)
        log_table = login.find_element(By.XPATH, "(//tbody)[2]//tr//td[4]")
        updatelogs = log_table.text
        print(updatelogs)
        assert f"{actual_order_id} updated" in updatelogs, "Log entry not found!"
        time.sleep(2)
        log_table_secondrow = login.find_element(By.XPATH, "(//tbody)[2]//tr[2]//td[4]")
        itemlogs = log_table_secondrow.text
        print(itemlogs)
        assert f"{actual_order_id} items changed" in itemlogs, "Log entry not found!"
        wait_and_locate_click(login, By.XPATH, "//i[@class='fa fa-times']")
        time.sleep(3)

        #######Confirmed############
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        time.sleep(2)
        confirmorder.click()
        time.sleep(5)

        #####Confirmed Log#########
        confirmedorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )
        actual_message = confirmedorder.text
        print(actual_message)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Log']")
        time.sleep(2)
        log_table = login.find_element(By.XPATH, "(//tbody)[2]//tr//td[4]")
        confirmedlogs = log_table.text
        print(confirmedlogs)
        order_id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='order-id ng-star-inserted']"))
        )
        full_order_id = order_id.text  
        actual_order_formatid = full_order_id.replace('#', '').strip()  
        parts = actual_order_formatid.split()  
        actual_order_id = f"{parts[0]} '{parts[1]}'"  
        print(actual_order_id) 
        assert f"{actual_order_id} status changed to 'Order {actual_message}'" in confirmedlogs,"Log entry not found!"
        wait_and_locate_click(login, By.XPATH, "//i[@class='fa fa-times']")
        time.sleep(3)

        ########Completed Order Log ##########
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
        order_id = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='order-id ng-star-inserted']"))
        )
        full_order_id = order_id.text  
        actual_order_formatid = full_order_id.replace('#', '').strip()  
        parts = actual_order_formatid.split()  
        actual_order_id = f"{parts[0]} '{parts[1]}'"  
        print(actual_order_id) 
        completedorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )
        completedorder_message = completedorder.text
        print(completedorder_message)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Log']")
        time.sleep(2)
        logs_table = login.find_element(By.XPATH, "(//tbody)[2]//tr[1]//td[4]")
        completedlogs = logs_table.text
        print(completedlogs)
        assert f"{actual_order_id} status changed to 'Order {completedorder_message}' in completedlogs," "Log entry not found!"
        wait_and_locate_click(login, By.XPATH, "//i[@class='fa fa-times']")
        time.sleep(3)
    except Exception as e:  
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
        