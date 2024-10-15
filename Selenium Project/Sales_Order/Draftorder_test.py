from cgitb import text
from Framework.common_utils import *
from Framework.common_dates_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Store")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_store(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//img[contains(@src, 'settings.gif')]//following::div[contains(text(),'Settings')]")
        time.sleep(2)
        POS = wait_and_locate_click(login, By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(login, POS)       
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p[normalize-space()='Sales Order Management System']")
        time.sleep(2)
        Sales_order = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']")) 
            )
        aria_checked = Sales_order.get_attribute("aria-checked")
        if aria_checked == "true":
            print("Sales Orders Management is already active, no need to click.")
        else:
            Sales_order.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
        time.sleep(3)
        draftorder = wait_and_locate_click(login, By.XPATH, "//span[@class='lnk setings ml-auto text-capitalize']")
        scroll_to_element(login, draftorder)
        time.sleep(2)
        draftorder_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@id='mat-mdc-slide-toggle-2-button'])[1]")))
        aria_checked = draftorder_button.get_attribute("aria-checked")
        if aria_checked == "true":
            draftorder_button.click()
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
        else:
            print("Draft Order is already active, no need to click.")
        time.sleep(2)
        wait_and_click(login, By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor text-capitalize']", 20)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Create Order')]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Next']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='d-flex item-btn align-items-center']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='mdc-checkbox'])[2]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        time.sleep(2)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm Order']"))
        )
        scroll_to_element(login, confirmorder)
        time.sleep(2)
        confirmorder.click()
        time.sleep(5)
        confirmorder = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='status-Completed ng-star-inserted']"))
        )
        actual_message = confirmorder.text
        expected_message = "Confirmed"
        print(f"Expected status: '{expected_message}', Actual status: '{confirmorder.text}'")
        assert actual_message == expected_message, f"Expected message '{expected_message} but got Message '{actual_message}'"
        complete_Order = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Complete Order']"))
        )
        scroll_to_element(login, complete_Order)
        time.sleep(2)
        complete_Order.click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        print("Toast Message:", toast_message.text)
        expected_message = "Order Completed Successfully"
        print(f"Expected status: '{expected_message}', Actual status: '{toast_message.text}'")
        assert toast_message.text == expected_message, f"Expected toast message '{expected_message}', but got '{toast_message.text}'"
        time.sleep(5)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  