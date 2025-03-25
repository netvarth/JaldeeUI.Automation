from Framework.common_utils import *
from Framework.common_dates_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Basic lab order work flow")
@pytest.mark.parametrize("url, username, password", [(test_url, test_user, password_1)])
def test_lab_order(login):

    try:
        
        time.sleep(5)
        wait = WebDriverWait(login, 30)

        order_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[3]"))
        )
        login.refresh()
        order_element.click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Create Order')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        clinic_option = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='ASTRAL CLINIC'])[1]"))
        )
        clinic_option.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[6]"))
        ).click()

        delivery_type = wait.until(
            EC.presence_of_element_located(
                (By))
        )

        time.sleep(5)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e