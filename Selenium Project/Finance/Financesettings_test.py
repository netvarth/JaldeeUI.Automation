from Framework.common_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Finance Enabling and Disabling in Settings")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_finance_settings(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Settings')]") 
        time.sleep(2)
        Financemanager = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Finance manager']"))
            )
        scroll_to_element(login, Financemanager)
        time.sleep(3)
        Financemanager.click()
        time.sleep(3)
        Finance = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@role='switch']")) 
                )
        aria_checked = Finance.get_attribute("aria-checked")
        if aria_checked == "true":
            print("Finance is already active, no need to click.")
            Finance.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
        else:
            Finance.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']") 
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e
