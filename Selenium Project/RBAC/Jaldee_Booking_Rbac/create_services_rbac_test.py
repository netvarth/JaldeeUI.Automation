from Framework.common_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with disabling Create Service")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_createService(login):
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
        service_management = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Service Management']"))
            )
        scroll_to_element(login, service_management)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-39-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the create own services...")
            create_own_service = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[39]"))
            )
            create_own_service.click()
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        else:
            pass
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[7]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        token_service = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='lnk setings ml-auto'])[6]"))
        )
        time.sleep(2)
        scroll_to_element(login, token_service)
        time.sleep(2)
        token_service.click()
        time.sleep(2)
        token_create_service = login.find_elements(By.XPATH, "//p-button[@class='p-element add-btn ng-star-inserted']")  # Use find_elements
        assert len(token_create_service) == 0 or not token_create_service[0].is_displayed(), \
        "'Token Create Service' button should NOT be visible after disabling the checkbox!"
        print("Test passed: Token Create Service button is NOT visible after disabling checkbox.")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[7]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        appointment_service = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='lnk setings ml-auto'])[10]"))
        )
        time.sleep(2)
        scroll_to_element(login, appointment_service)
        time.sleep(2)
        appointment_service.click()
        time.sleep(2)
        appointment_create_service = login.find_elements(By.XPATH, "//p-button[@class='p-element add-btn ng-star-inserted']")  # Use find_elements
        assert len(appointment_create_service) == 0 or not appointment_create_service[0].is_displayed(), \
        "'Appointment Create Service' button should NOT be visible after disabling the checkbox!"
        print("Test passed: Appointment Create Service button is NOT visible after disabling checkbox.")
        time.sleep(3)
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e