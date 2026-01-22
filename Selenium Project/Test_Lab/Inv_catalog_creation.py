from Framework.common_utils import *
import allure
from allure_commons.types import AttachmentType
import os




@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Appointment Pre deployment testing")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale_2, password)])
def test_Inv_catalog_creation(login):

    try:
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//img)[7]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//*[@id='actionNav_ORD_Inventory'])[4]")
        time.sleep(2)

        LOOP_COUNT = 55
        wait = WebDriverWait(login, 20)

        for i in range(LOOP_COUNT):

            time.sleep(4)

            wait_and_locate_click(login, By.XPATH, "//*[@id='btnCreateCat_ORD_Catalog']")
            catalog_name = "|Inv_Catalog_" + str(uuid.uuid4())[:6]
            wait_and_send_keys(login, By.XPATH, "//input[@id='inputCatName_ORD_CatlgCreate']", catalog_name)
            wait_and_locate_click(login, By.XPATH, "//*[@id='selectStore_ORD_CatlgCreate']")
            wait_and_locate_click(
                 login, By.XPATH, "//span[normalize-space()='Thrissur']"
            )

            wait_and_locate_click(
                 login, By.XPATH, "//button[@id='btnCrtCat_ORD_CatlgCreate']"
            )

            time.sleep(3)

            checkboxes = WebDriverWait(login, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//input[contains(@type, 'checkbox')]"))
            )

            # Click the first three checkboxes
            for i in range(1, min(6, len(checkboxes))):
                checkboxes[i].click()

            wait_and_locate_click(
                 login, By.XPATH, "//*[@id='btnSelect_ORD_ItemSelection']"
            
            )

            wait_and_locate_click(login, By.XPATH, "//div[@id='actionBack_ORD_CatlgDetls']")




        
    except Exception as e:
            allure.attach(  # use Allure package, .attach() method, pass 3 params
                login.get_screenshot_as_png(),  # param1
                # login.screenshot()
                name="full_page",  # param2
                attachment_type=AttachmentType.PNG,
            )
            raise e