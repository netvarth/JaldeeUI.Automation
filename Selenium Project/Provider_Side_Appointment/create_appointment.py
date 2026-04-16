from Framework.common_utils import *
from Framework.consumer_common_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_create_sales_order_1(login):
    try:
        driver = login
        wait_and_locate_click(
            login, By.XPATH, "(//img)[3]"
        )

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "//span[normalize-space()='Appointment']"
        )

        

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e    
