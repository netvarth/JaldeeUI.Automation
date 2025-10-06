
from Framework.common_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title(" Create Invoice on Finance Dasahboard")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_createinvoice(login): 
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create Invoice']") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Name or Phone or Email or Id']", 9207206005) 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 105']")
        time.sleep(2)
        WebDriverWait(login, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='p-button-label']")
            )
        ).click()
        time.sleep(2)
        billings = WebDriverWait(login, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='mt-3 Billing-Address ng-star-inserted'])[1]")
            )
        )
        billings.click()
        time.sleep(3)
        textarea = WebDriverWait(login, 15).until(
            EC.visibility_of_element_located((By.XPATH, "(//div[@class='mt-3 Billing-Address ng-star-inserted']//textarea)[1]"))
        )
        textarea.click()
        random_billing_address = generate_random_billing_address()
        textarea.send_keys(random_billing_address)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-label']") 
        time.sleep(2)
        reference_number = str(uuid.uuid4())
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Referal Number']", reference_number) 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add Procedure/Item']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//div[@class='item-name'][normalize-space()='Consultation']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add']")
        time.sleep(3)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Private Note']", "invoice for consultation")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Shared with patient']", "invoice for consultation shared")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Terms and condition']", "T&C")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Share Payment Link']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e     
    


    