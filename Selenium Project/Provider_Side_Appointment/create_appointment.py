from Framework.common_utils import *
from Framework.consumer_common_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_create_sales_order_1(login):

    try:

        wait= WebDriverWait(login, 30)
        driver = login
        wait_and_locate_click(
            login, By.XPATH, "//img[contains(@src,'appointments.png')]"
        )

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "//div[@id='actionCreate_BUS_bookList']//p-card[@class='p-element']"
        )

        

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e    
