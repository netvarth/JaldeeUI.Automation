
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


          

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with enabling Create Service")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_createService(login):
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
            pass
        else:
            print("Checkbox is not selected, proceeding to enabled the create own services...")
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
        token_create_service = login.find_element(By.XPATH, "//p-button[@class='p-element add-btn ng-star-inserted']")  
        assert token_create_service.is_displayed(), "Add token create service button is not visible, but it should be when 'Create Service' is checked."
        print("Test passed: Token Create Service button is visible after enabling checkbox.")
        time.sleep(2)
        token_create_service.click()
        time.sleep(2)
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
        assert appointment_create_service.is_displayed(), "Add appointment create service button is not visible, but it should be when 'Create Service' is checked."
        print("Test passed: Appointment Create Service button is visible after enabling checkbox.")
        time.sleep(3)
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
    
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with disabling Update Service")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_updateService(login):
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
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-40-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the create own services...")
            create_update_service = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[40]"))
            )
            create_update_service.click()
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
        services_morebutton = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[4]"))
        )
        services_morebutton.click()
        time.sleep(2)
        token_edit_service = WebDriverWait(login, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[normalize-space()='Edit']") )
        ) 
        if not token_edit_service:
            print("Testcase Failed: 'Token Update Service' button should NOT be visible after disabling the checkbox!'")
            assert False, "'Token Update Service' button should NOT be visible after disabling the checkbox!"
        else:
            print("Test passed: 'Token Update Service' button is NOT visible after disabling checkbox.") 
        actions = ActionChains(login)
        actions.send_keys(Keys.TAB).perform()
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
        services_morebutton = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[4]"))
        )
        services_morebutton.click()
        time.sleep(2)
        appointment_create_service = WebDriverWait(login, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[normalize-space()='Edit']") )
        ) 
        if not appointment_create_service:
            print("Testcase Failed: 'Appointment Update Service' button should NOT be visible after disabling the checkbox!'")
            assert False, "'Appointment Update Service' button should NOT be visible after disabling the checkbox!"
        else:
            print("Test passed: 'Appointment Update Service' button is NOT visible after disabling checkbox.")
        time.sleep(3)
        actions = ActionChains(login)
        actions.send_keys(Keys.TAB).perform()
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e 


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with disabling Update Service")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_updateService(login):
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
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-40-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            pass
            
        else:
            print("Checkbox is not selected, proceeding to enabled the create own services...")
            create_update_service = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[40]"))
            )
            create_update_service.click()
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
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
        services_morebutton = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[4]"))
        )
        services_morebutton.click()
        time.sleep(2)
        token_edit_service = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Edit']") )
        ) 
        if not token_edit_service:
            print("Testcase Failed: 'Token Update Service' button should  be visible after enabling the checkbox!'")
            assert False, "'Token Update Service' button should  be visible after enabling the checkbox!"
        else:
            print("Test passed: 'Token Update Service' button is  visible after enabling checkbox.") 
        token_edit_service.click()
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
        services_morebutton = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[4]"))
        )
        services_morebutton.click()
        time.sleep(2)
        appointment_create_service = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Edit']") )
        ) 
        if not appointment_create_service:
            print("Testcase Failed: 'Appointment Update Service' button should  be visible after enabling the checkbox!'")
            assert False, "'Appointment Update Service' button should be visible after enabling the checkbox!"
        else:
            print("Test passed: 'Appointment Update Service' button is visible after enabling checkbox.")
        appointment_create_service.click()
        time.sleep(3)
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e 


              