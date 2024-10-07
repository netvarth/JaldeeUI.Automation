from Framework.common_utils import *
from Framework.common_dates_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("item_Variants")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Orders(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Item Variants')]") 
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Categories')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-label']") 
        time.sleep(2)
        Category = "Category_" + str(uuid.uuid4())[:8]
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Category Name']", Category)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-label'][normalize-space()='Create Category']") 
        time.sleep(2)
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  