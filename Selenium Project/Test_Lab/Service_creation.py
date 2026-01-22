
from Framework.common_utils import *
import allure
from allure_commons.types import AttachmentType
import os




@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Appointment Pre deployment testing")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale_2, password)])
def test_service_creation(login): 

     try:
        time.sleep(2)
          
        wait_and_locate_click(login, By.XPATH, "//img[@src='./assets/images/menu/settings.png']")


        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='lnk setings ml-auto'])[8]")
        time.sleep(2)
        LOOP_COUNT = 15

        for i in range(LOOP_COUNT):

            wait_and_locate_click(
                login,
                By.XPATH,
                "//p-button[contains(@class,'add-btn')]//span[1]"
            )
            time.sleep(2)

            wait_and_locate_click(
                login,
                By.XPATH,
                "//span[normalize-space()='Service Details']"
            )

            Service_name = f"Service_{i}_{str(uuid.uuid4())[:4]}"

            wait_and_send_keys(
                login,
                By.XPATH,
                "//input[@id='service_name']",
                Service_name
            )

            time.sleep(2)
            wait_and_locate_click(
                login,
                By.XPATH,
                "(//span[contains(@class,'fa-angle-down')])[2]"
            )

            time.sleep(2)
            input_time = login.find_element(By.XPATH, "//input[@placeholder='MM']")
            input_time.clear()
            input_time.send_keys("15")

            wait_and_locate_click(login, By.XPATH, "//div[@class='ngb-tp']")

            time.sleep(2)
            element = login.find_element(By.XPATH, "//button[@type='submit']")
            scroll_to_element(login, element)
            time.sleep(2)
            element.click()

            wait_and_locate_click(
                login,
                By.XPATH,
                "//span[contains(@class,'fa-arrow-left')]"
            )

     except Exception as e:
            allure.attach(  # use Allure package, .attach() method, pass 3 params
                login.get_screenshot_as_png(),  # param1
                # login.screenshot()
                name="full_page",  # param2
                attachment_type=AttachmentType.PNG,
            )
            raise e