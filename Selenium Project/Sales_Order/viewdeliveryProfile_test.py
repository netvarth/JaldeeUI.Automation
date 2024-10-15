
from Framework.common_utils import *
from Framework.common_dates_utils import *
import re


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("View_Delivery_Profile")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_View_deliveryProfile(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Delivery Profile')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@type='submit'][normalize-space()='View'])[2]")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//button[@class='cs-btn btn btn-primary btn-transform mgn-lt-20 pull-right display-min-none ng-star-inserted'])[1]")
        time.sleep(3)
        deliveryprice = wait_and_locate_click(login, By.XPATH, "(//input[@type='number'])[3]")
        time.sleep(2)
        currentprice = float(deliveryprice.get_attribute('value'))
        newprice = currentprice + 10.00
        deliveryprice.clear()
        deliveryprice.send_keys(str(newprice))
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Update']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='View Store']")
        time.sleep(5)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  