from Framework.common_utils import *
from Framework.common_dates_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Delivery_Profile")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_deliveryProfile(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Delivery Profile')]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Delivery Profile']")
        time.sleep(2)
        Delivery_profile = "Delivery_profile_" + str(uuid.uuid4())[:8]
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Delivery Profile 1']", Delivery_profile)
        time.sleep(2)
        min_price = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@type='number'])[1]"))
        )
        min_price.clear()
        min_price.send_keys("50")
        time.sleep(3)
        max_price = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@type='number'])[2]"))
        )
        max_price.clear()
        max_price.send_keys("5000")
        time.sleep(3)
        wait_and_send_keys(login, By.XPATH, "(//input[@type='number'])[3]", 50)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Create']") 
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='name']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[@id='p-highlighted-option']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='displayname']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Home Delivery']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']") 
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  