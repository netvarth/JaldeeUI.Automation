from Framework.common_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with disabling Delivery_Profile ")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_Delivery_profile(login):
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
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Jaldee Order POS']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//tbody/tr[2]/td[3]/div[1]/div[1]/p-button[1]/button[1]/span[1]")
        time.sleep(2)
        delivery_profile_settings = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Delivery Profile Settings']"))
            )
        scroll_to_element(login, delivery_profile_settings)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Create Or Update Delivery Profile')]/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the Delivery Profile ..")
            delivery_profile = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[24]"))
            )
            delivery_profile.click()
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
        wait_and_locate_click(login, By.XPATH, "//li[4]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Delivery Profile')]")
        time.sleep(2)
        delivery_profile = WebDriverWait(login, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//p-button[@label='Delivery Profile']//button[@type='button']"))
        )
        if not delivery_profile:
            print("Testcase Failed: Delivery_profile button is visible after disabling checkbox.")
            assert False, "Delivery_profile button should NOT be visible after disabling the checkbox!"
        else:
            print("Test passed: Delivery_profile button is NOT visible after disabling checkbox.")
        time.sleep(3)
        
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with enabling Delivery_Profile")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_Delivery_profile(login):
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
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Jaldee Order POS']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//tbody/tr[2]/td[3]/div[1]/div[1]/p-button[1]/button[1]/span[1]")
        time.sleep(2)
        delivery_profile_settings = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Delivery Profile Settings']"))
            )
        scroll_to_element(login, delivery_profile_settings)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Create Or Update Delivery Profile')]/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to enabled the delivery profile..")
            DeliveryProfile = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[24]"))
            )
            DeliveryProfile.click()
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[4]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Delivery Profile')]")
        time.sleep(2)
        Delivery_profile = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p-button[@label='Delivery Profile']//button[@type='button']"))
        )
        assert Delivery_profile.is_displayed(), "Delivery_profile button is NOT displayed after enabling checkbox!"
        print("Delivery_profile button is displayed. Proceeding to createDelivery Profile.")
        Delivery_profile.click()
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
        max_price.send_keys("3000")
        time.sleep(3)
        wait_and_send_keys(login, By.XPATH, "(//input[@type='number'])[3]", 50)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Create']") 
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@class='cs-btn btn view-btn'])[1]") 
        time.sleep(2)
        Delivery_editprofile = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='fa fa-pencil'])[1]"))
        )
        assert Delivery_editprofile.is_displayed(), "Delivery_Editprofile button is NOT displayed after enabling checkbox!"
        print("Delivery_Editprofile button is displayed. Proceeding to view Delivery Profile.")
        Delivery_editprofile.click()
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Update']") 
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
     
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with disabling viewDelivery_Profile ")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_viewDelivery_profile(login):
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
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Jaldee Order POS']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//tbody/tr[2]/td[3]/div[1]/div[1]/p-button[1]/button[1]/span[1]")
        time.sleep(2)
        delivery_profile_settings = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Delivery Profile Settings']"))
            )
        scroll_to_element(login, delivery_profile_settings)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'View Delivery Profile')]/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the View Delivery Profile ..")
            viewdelivery_profile = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[25]"))
            )
            viewdelivery_profile.click()
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
        wait_and_locate_click(login, By.XPATH, "//li[4]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Delivery Profile')]")
        time.sleep(2)
        viewdelivery_profile = WebDriverWait(login, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//tbody/tr[1]/td[5]/button[1]"))
        )
        if not viewdelivery_profile:
            print("Testcase Failed: View Delivery_profile button is visible after disabling checkbox.")
            assert False, "View Delivery_profile button should NOT be visible after disabling the checkbox!"
        else:
            print("Test passed: View Delivery_profile button is NOT visible after disabling checkbox.")
        time.sleep(3)
        
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Jaldee Order POS with enabling View Delivery_Profile")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_viewDelivery_profile(login):
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
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Jaldee Order POS']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//tbody/tr[2]/td[3]/div[1]/div[1]/p-button[1]/button[1]/span[1]")
        time.sleep(2)
        delivery_profile_settings = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Delivery Profile Settings']"))
            )
        scroll_to_element(login, delivery_profile_settings)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'View Delivery Profile')]/preceding-sibling::div//input"))
        )
        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print("Checkbox is selected:", is_checked)
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to enabled the delivery profile..")
            view_DeliveryProfile = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[25]"))
            )
            view_DeliveryProfile.click()
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//li[4]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Delivery Profile')]")
        time.sleep(2)
        viewDelivery_profile = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@type='submit'][normalize-space()='View'])[6]"))
        )
        assert viewDelivery_profile.is_displayed(), "View Delivery_profile button is NOT displayed after enabling checkbox!"
        print("View Delivery_profile button is displayed. Proceeding to view Delivery Profile.")
        viewDelivery_profile.click()
        time.sleep(2)
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     

     