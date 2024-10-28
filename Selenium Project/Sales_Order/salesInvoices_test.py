from Framework.common_utils import *
from Framework.common_dates_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoice Filter with Notpaid Payment Status")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Invoice_Notpaid_Filter_Payment(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Invoices')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[7]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'Select Payment Status')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Not Paid']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Apply']") 
        time.sleep(2)
        table_body = WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//tbody")
            )
        )
        table_rows = table_body.find_elements(By.XPATH, ".//tr")
        for row in table_rows:
            invoice_status = row.find_element(By.XPATH, "//tbody/tr/td[@class='tb-display-none ng-star-inserted'][normalize-space()='NotPaid']").text
            assert invoice_status == "NotPaid", f"Store Status '{invoice_status}' does not match the filter 'NotPaid'"
        
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Reset']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon p-sidebar-close-icon'])[1]") 
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoice Filter with Partiallypaid Payment Status")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Invoice_Partiallypaid_Filter_Payment(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Invoices')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[7]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'Select Payment Status')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Partially Paid']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Apply']") 
        time.sleep(2)
        table_body = WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//tbody")
            )
        )
        table_rows = table_body.find_elements(By.XPATH, ".//tr")
        for row in table_rows:
            invoice_status = row.find_element(By.XPATH, "//tbody/tr/td[@class='tb-display-none ng-star-inserted'][normalize-space()='PartiallyPaid']").text
            assert invoice_status == "PartiallyPaid", f"Store Status '{invoice_status}' does not match the filter 'PartiallyPaid'"
    
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Reset']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon p-sidebar-close-icon'])[1]") 
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoice Filter with Fullypaid Payment Status")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Invoice_Fullypaid_Filter_Payment(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Invoices')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[7]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'Select Payment Status')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Fully Paid']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Apply']") 
        time.sleep(2)
        table_body = WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//tbody")
            )
        )
        table_rows = table_body.find_elements(By.XPATH, ".//tr")
        for row in table_rows:
            invoice_status = row.find_element(By.XPATH, "//tbody/tr/td[@class='tb-display-none ng-star-inserted'][normalize-space()='FullyPaid']").text
            assert invoice_status == "FullyPaid", f"Store Status '{invoice_status}' does not match the filter 'FullyPaid'"
        
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Reset']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon p-sidebar-close-icon'])[1]") 
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoice Filter with Invoice Status")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_InvoiceStatus__Filter_Payment(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Invoices')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[5]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'Select Invoice Status')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Settled']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Apply']") 
        time.sleep(2)
        table_body = WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//tbody")
            )
        )
        table_rows = table_body.find_elements(By.XPATH, ".//tr")
        for row in table_rows:
            invoice_status = row.find_element(By.XPATH, "//tbody/tr/td[@class='tb-display-none ng-star-inserted'][normalize-space()='Settled']").text
            assert invoice_status == "Settled", f"Store Status '{invoice_status}' does not match the filter 'Settled'"
        
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[5]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'Select Invoice Status')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Cancelled'']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Apply']") 
        time.sleep(2)
        table_body = WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//tbody")
            )
        )
        table_rows = table_body.find_elements(By.XPATH, ".//tr")
        for row in table_rows:
            invoice_status = row.find_element(By.XPATH, "//tbody/tr/td[@class='tb-display-none ng-star-inserted'][normalize-space()='Settled']").text
            assert invoice_status == "Cancelled'", f"Store Status '{invoice_status}' does not match the filter 'Cancelled''"
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Reset']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon p-sidebar-close-icon'])[1]") 
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

    
