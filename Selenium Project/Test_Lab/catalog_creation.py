from Framework.common_utils import *
import allure
from allure_commons.types import AttachmentType
import os




@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Appointment Pre deployment testing")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale_2, password)])
def test_catalog_creation(login):

    try:
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//img)[6]")
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//*[@id='actionRouteTo_ORD_Dashbrd'])[5]")

        time.sleep(3)

        LOOP_COUNT = 200
        wait = WebDriverWait(login, 20)

        for i in range(LOOP_COUNT):

            time.sleep(4)
            WebDriverWait(login, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "(//p-button[@id='btnCrtCat_ORD_OrdCat'])[1]"))
            ).click()

            time.sleep(2)

            catalog_name = "Catalog_" + str(uuid.uuid4())[:6]
            print(catalog_name)
            WebDriverWait(login, 20).until(
                EC.presence_of_element_located((By.XPATH, "(//input[@id='inputCatName_ORD_CatCrt'])[1]"))
            ).send_keys(catalog_name)
            
            dropdown = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "(//p-dropdown[@id='selectStore_ORD_CatCrt'])[1]"))
            )
            dropdown.click()
            WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[normalize-space()='Thrissur']"))
            ).click()
        
            WebDriverWait(login, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//p-dropdown[@id='selectWalk_ORD_CatCrt']"))
            ).click()
            time.sleep(1)
            WebDriverWait(login, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Yes'])[1]"))
            ).click()

            time.sleep(2)

            WebDriverWait(login, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//p-dropdown[@id='selectSelf_ORD_CatCrt']"))
            ).click()
            time.sleep(1)
            WebDriverWait(login, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Yes'])[1]"))
            ).click()

        
            WebDriverWait(login, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[@id='btnSave_ORD_CatCrt']"))
            ).click()

            time.sleep(3)
        
            start_index = 2   # First checkbox to select
            end_index = 4     # Last checkbox to select

            # Find all checkboxes using XPath
            checkboxes = login.find_elements(By.XPATH, "//input[@id='SelectItem_ORD_ItemSelection-input']")

            # Iterate and select checkboxes within the range
            for i in range(start_index - 1, min(end_index, len(checkboxes))):  # Adjusting for 0-based index
                if not checkboxes[i].is_selected():  # Check if not already selected
                    checkboxes[i].click()

            # Confirm selections
            selected_checkboxes = [cb.get_attribute("id") for cb in checkboxes if cb.is_selected()]
            print(f"Selected checkboxes: {selected_checkboxes}")

            WebDriverWait(login, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[@id='btnSubmitItems_ORD_ItemSelection']"))
            ).click()

            time.sleep(2)

            wait_and_locate_click(login, By.XPATH, "//div[@id='actionBack_ORD_CatDet']")



    except Exception as e:
            allure.attach(  # use Allure package, .attach() method, pass 3 params
                login.get_screenshot_as_png(),  # param1
                # login.screenshot()
                name="full_page",  # param2
                attachment_type=AttachmentType.PNG,
            )
            raise e