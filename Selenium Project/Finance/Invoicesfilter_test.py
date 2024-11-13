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
        wait_and_locate_click(login, By.XPATH, "(//div[@role='tablist'])[6]") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@id='providerConsumerData']", 105)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-icon p-button-icon-left pi pi-check']") 
        time.sleep(5)
    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e