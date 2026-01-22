from Framework.common_utils import *
import allure
from allure_commons.types import AttachmentType
import os




@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Appointment Pre deployment testing")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale_2, password)])
def test_item_creation(login):

    try:
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//img)[6]")
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//*[@id='actionRouteTo_ORD_Dashbrd'])[6]")
        wait = WebDriverWait(login, 20)

        LOOP_COUNT = 119

        for i in range(LOOP_COUNT):
            
            time.sleep(4)

            wait_and_locate_click(login, By.XPATH, "//button[@id='btnCrtItem_ORD_Items']")

            item_name = "Item_" + str(uuid.uuid4())[:4]
            print("Item Name", item_name)
            WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='inpItemName_ORD_INV_ItemCreate']"))
            ).send_keys(item_name)

            WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='txtaShortDesc_ORD_INV_ItemCreate']"))
            ).send_keys("A Item name is required and recommended to be unique.")

    
            time.sleep(2)
            WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[@id='ddBatchApplicable_ORD_INV_ItemCreate']"))
            ).click()

            WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "(//*[@class='ng-star-inserted'][normalize-space()='Yes'])[1]"))
            ).click()

            time.sleep(1)
            WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//p-multiselect[@id='msTaxes_ORD_INV_ItemCreate'])[1]"))
            ).click()

            time.sleep(1)
            WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[normalize-space()='GST 5%']"))
            ).click()

            time.sleep(1)
            wait_and_locate_click(login, By.XPATH, "//button[@id='btnSubmit_ORD_INV_ItemCreate']")

    except Exception as e:
            allure.attach(  # use Allure package, .attach() method, pass 3 params
                login.get_screenshot_as_png(),  # param1
                # login.screenshot()
                name="full_page",  # param2
                attachment_type=AttachmentType.PNG,
            )
            raise e