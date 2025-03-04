from Framework.common_utils import *
from Framework.common_dates_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Active Carts")
@pytest.mark.parametrize("url", ["https://scale.jaldeetest.in/business/"])
def test_activecarts(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Active Cart')]")
        time.sleep(5)
        while True:
            try:
                next_page_button = login.find_element(By.XPATH, "//button[@class='p-ripple p-element p-paginator-next p-paginator-element p-link']")
                scroll_to_element(login, next_page_button)
                if next_page_button.is_enabled():
                    next_page_button.click()
                    time.sleep(3)
                    first_item = wait_and_locate_click(login, By.XPATH, "//th[normalize-space()='Quantity']")
                    scroll_to_element(login, first_item)
                    time.sleep(3) 
                else:
                    break 
            except NoSuchElementException:
                break  
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  