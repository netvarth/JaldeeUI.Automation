from Framework.common_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with disabling Send-attachments")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_send_booking_attachment(login):
    try:
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Settings')]")
        time.sleep(2)
        rbac = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='RBAC']"))
            )
        scroll_to_element(login, rbac)
        time.sleep(2)
        rbac.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//h2[normalize-space()='Roles']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Jaldee Booking']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//tbody/tr[3]/td[3]/div[1]/div[1]/p-button[1]/button[1]/span[1]")
        time.sleep(2)
        booking_attachments = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Booking Attachments and Communication']"))
            )
        scroll_to_element(login, booking_attachments)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='mat-mdc-checkbox-touch-target'])[20]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the send booking attachments...")
            send_booking_attachments = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Send booking Attachments']"))
            )
            send_booking_attachments.click()
            time.sleep(3)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        else:
            pass
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
