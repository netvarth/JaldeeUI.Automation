from Framework.common_utils import *
import allure
from allure_commons.types import AttachmentType


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Invoices Filter")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_InvoiceFilter(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        invoices = WebDriverWait(login, 15).until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Invoices'])[1]"))
        )
        scroll_to_element(login,invoices)
        time.sleep(2) 
        invoices.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[1]") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@id='amount']", 450)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[3]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='text-left p-dropdown p-component'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='New']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[4]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='text-left p-dropdown p-component'])[2]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Booking']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[5]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='text-left p-dropdown p-component'])[3]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Fully Paid']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[6]") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@id='providerConsumerData']", 105)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[7]") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@id='invoiceId']", 2427)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[8]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='text-left p-dropdown p-component'])[4]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[@aria-label='Chavakkad']//span[@class='ng-star-inserted'][normalize-space()='Chavakkad']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-icon p-button-icon-left pi pi-check']") 
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Reset']") 
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[contains(@class, 'p-ripple') and contains(@class, 'p-sidebar-close')]") 
        time.sleep(2)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Order Invoices Filter")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_OrderInvoiceFilter(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        orderinvoices = WebDriverWait(login, 15).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Order Invoices']"))
        )
        scroll_to_element(login,orderinvoices)
        time.sleep(2) 
        orderinvoices.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[1]") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@id='providerConsumerName']", "Stephanie Herrera")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[2]") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@id='memberJaldeeId'])[1]", "w2G") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[3]") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@id='invoiceNum']", 26) 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[5]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'Select Invoice Status')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='New']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[6]") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@id='netRate']", 9750) 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[7]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'Select Payment Status')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Not Paid']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[8]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Geetha']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-icon p-button-icon-left pi pi-check']") 
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Reset']") 
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[contains(@class, 'p-ripple') and contains(@class, 'p-sidebar-close')]") 
        time.sleep(2)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e         
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Expense Filter")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_Expense_Filter(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        expenses = WebDriverWait(login, 15).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'dash_font') and normalize-space(text())='Expenses']"))
        )
        scroll_to_element(login,expenses)
        time.sleep(2) 
        expenses.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='pe-2 category-section'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Purchase']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[1]") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@id='amount']", "6950")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[2]") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@id='amountDue']", "6950") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[3]") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@id='amountPaid']", "0.00") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[5]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='text-left p-dropdown p-component'])[2]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='New']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[6]") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@id='referenceNo']", "00077") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[7]") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@id='encId']", "ex-73b91u7-u") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[8]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='text-left p-dropdown p-component'])[3]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Chavakkad']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-icon p-button-icon-left pi pi-check']") 
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Reset']") 
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[contains(@class, 'p-ripple') and contains(@class, 'p-sidebar-close')]") 
        time.sleep(2)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e
    



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Revenue Filter")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_Revenue_Filter(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        revenue = WebDriverWait(login, 15).until(
            EC.presence_of_element_located((By.XPATH, "(//span[contains(@class, 'dash_font')][normalize-space()='Revenue'])[1]"))
        )
        scroll_to_element(login,revenue)
        time.sleep(2) 
        revenue.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[1]") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@id='amount'])[1]", "100")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@id='amount'])[2]", "175")
        time.sleep(2)
        # wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[3]") 
        # time.sleep(2)
        # wait_and_send_keys(login, By.XPATH, "//input[@id='referenceNo']", "Invoice # 2510") 
        # time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[4]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='text-left p-dropdown p-component'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='New']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[5]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='text-left p-dropdown p-component'])[2]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[@role='option' and @aria-label='Booking']//span[normalize-space(text())='Booking']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[6]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='text-left p-dropdown p-component'])[3]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[@role='option' and @aria-label='Booking']//span[normalize-space(text())='Booking']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[8]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='text-left p-dropdown p-component'])[5]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[@aria-label='Chavakkad']//span[@class='ng-star-inserted'][normalize-space()='Chavakkad']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-icon p-button-icon-left pi pi-check']") 
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Reset']") 
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[contains(@class, 'p-ripple') and contains(@class, 'p-sidebar-close')]") 
        time.sleep(2)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Payout Filter")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_Payout_Filter(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        payout = WebDriverWait(login, 15).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Payouts']"))
        )
        scroll_to_element(login,payout)
        time.sleep(2) 
        payout.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[1]") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@id='amount'])[1]", "50")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@id='amount'])[2]", "586")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[3]") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@id='referenceNo']", "ex-73b91u7-7") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[4]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='text-left p-dropdown p-component'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Approved']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[5]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='text-left p-dropdown p-component'])[2]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[@aria-label='Expense']//span[@class='ng-star-inserted'][normalize-space()='Expense']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[6]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='text-left p-dropdown p-component'])[3]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[@aria-label='Purchase']//span[@class='ng-star-inserted'][normalize-space()='Purchase']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[7]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='text-left p-dropdown p-component'])[4]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//li[@aria-label='whiteboard transparent networks'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[8]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='text-left p-dropdown p-component'])[5]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[@aria-label='Chavakkad']//span[@class='ng-star-inserted'][normalize-space()='Chavakkad']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-icon p-button-icon-left pi pi-check']") 
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Reset']") 
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[contains(@class, 'p-ripple') and contains(@class, 'p-sidebar-close')]") 
        time.sleep(2)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Vendor Filter")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_Vendor_Filter(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        vendors = WebDriverWait(login, 15).until(
            EC.presence_of_element_located((By.XPATH, "(//span[contains(@class, 'dash_font')][normalize-space()='Vendors'])[1]"))
        )
        scroll_to_element(login,vendors)
        time.sleep(2) 
        vendors.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='text-left p-dropdown p-component'])[1]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='whiteboard transparent networks'])[1]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[3]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='text-left p-dropdown p-component'])[2]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='New']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[4]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='text-left p-dropdown p-component'])[3]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Medicine']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-icon p-button-icon-left pi pi-check']") 
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//i[@class='pi pi-filter-fill']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Reset']") 
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[contains(@class, 'p-ripple') and contains(@class, 'p-sidebar-close')]") 
        time.sleep(2)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e
    