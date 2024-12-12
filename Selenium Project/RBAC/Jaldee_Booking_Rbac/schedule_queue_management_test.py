

from Framework.common_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Schedule creation Disabling")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_Schedulecreation(login):
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
        schedule_management = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Schedule and Queue Management']"))
            )
        scroll_to_element(login, schedule_management)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-33-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the send booking attachments...")
            create_schedule = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[33]"))
            )
            create_schedule.click()
            time.sleep(3)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        else:
            pass
        wait_and_locate_click(login, By.XPATH, "//li[7]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        schedules = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Set when you want to accept bookings.']"))
        )
        scroll_to_element(login, schedules)
        time.sleep(2)
        schedules.click()
        time.sleep(2)
        Scheduleplusbutton = login.find_elements(By.XPATH, "//body//app-root//p-button[1]")
        assert len(Scheduleplusbutton) == 0 or not Scheduleplusbutton[0].is_displayed(),\
        "'Create Schedule' button should NOT be visible after disabling the checkbox!"
        print("Test passed: Create Schedule button is NOT visible after disabling checkbox.")
        time.sleep(3)
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with enabling Schedule button")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_Schedulecreation(login):
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
        schedule_management = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Schedule and Queue Management']"))
            )
        scroll_to_element(login, schedule_management)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-33-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to enabled the send booking attachments...")
            create_schedule = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[33]"))
            )
            create_schedule.click()
            time.sleep(3)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[7]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        time.sleep(2)
        schedules = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Set when you want to accept bookings.']"))
        )
        scroll_to_element(login, schedules)
        time.sleep(2)
        schedules.click()
        time.sleep(2)
        Scheduleplusbutton = login.find_elements(By.XPATH, "//body//app-root//p-button[1]")
        assert Scheduleplusbutton[0].is_displayed(),\
        "'Create Schedule' button should be visible after enabling the checkbox!"
        print("Test passed: Create Schedule button is visible after enabling checkbox.")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH,  "//body//app-root//p-button[1]")
        time.sleep(3)
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Schedule Updation Disabling")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_ScheduleUpdation(login):
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
        schedule_management = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Schedule and Queue Management']"))
            )
        scroll_to_element(login, schedule_management)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-34-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the send booking attachments...")
            update_schedule = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[34]"))
            )
            update_schedule.click()
            time.sleep(3)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        else:
            pass
        wait_and_locate_click(login, By.XPATH, "//li[7]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        schedules = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Set when you want to accept bookings.']"))
        )
        scroll_to_element(login, schedules)
        time.sleep(2)
        schedules.click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Active Schedules (2)']"))
        ).click()
        time.sleep(5)
        WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[8]"))
        ).click()
        time.sleep(2)
        Scheduleedit = login.find_elements(By.XPATH, "//span[normalize-space()='Edit']")
        assert len(Scheduleedit) == 0 or not Scheduleedit[0].is_displayed(),\
        "'Update Schedule' button should NOT be visible after disabling the checkbox!"
        print("Test passed: Update Schedule button is NOT visible after disabling checkbox.")
        time.sleep(3)
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Schedule Updation Enabling")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_ScheduleUpdation(login):
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
        schedule_management = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Schedule and Queue Management']"))
            )
        scroll_to_element(login, schedule_management)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-34-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to disabled the send booking attachments...")
            update_schedule = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[34]"))
            )
            update_schedule.click()
            time.sleep(3)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "//li[7]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        schedules = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Set when you want to accept bookings.']"))
        )
        scroll_to_element(login, schedules)
        time.sleep(2)
        schedules.click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Active Schedules (2)']"))
        ).click()
        time.sleep(5)
        WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[8]"))
        ).click()
        time.sleep(2)
        Scheduleedit = login.find_elements(By.XPATH, "//span[normalize-space()='Edit']")
        assert Scheduleedit[0].is_displayed(),\
        "'Update Schedule' button should be visible after enabling the checkbox!"
        print("Test passed: Update Schedule button is visible after enabling checkbox.")
        time.sleep(3)
        WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Edit']"))
        ).click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()
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
@allure.title("RBAC Queue creation Disabling")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_Queuecreation(login):
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
        schedule_management = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Schedule and Queue Management']"))
            )
        scroll_to_element(login, schedule_management)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-36-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the send booking attachments...")
            create_queue = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[36]"))
            )
            create_queue.click()
            time.sleep(3)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        else:
            pass
        wait_and_locate_click(login, By.XPATH, "//li[7]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        queues = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Set when you want to start a virtual queue and iss')]"))
        )
        scroll_to_element(login, queues)
        time.sleep(2)
        queues.click()
        time.sleep(2)
        Queueplusbutton = login.find_elements(By.XPATH, "//span[normalize-space()='Add Queue']")
        assert len(Queueplusbutton) == 0 or not Queueplusbutton[0].is_displayed(),\
        "'Create Queue' button should NOT be visible after disabling the checkbox!"
        print("Test passed: Create Queue button is NOT visible after disabling checkbox.")
        time.sleep(3)
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with enabling Queue button")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_Queuecreation(login):
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
        schedule_management = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Schedule and Queue Management']"))
            )
        scroll_to_element(login, schedule_management)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-36-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to enabled the send booking attachments...")
            create_queue = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[36]"))
            )
            create_queue.click()
            time.sleep(3)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[7]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        time.sleep(2)
        queues = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Set when you want to start a virtual queue and iss')]"))
        )
        scroll_to_element(login, queues)
        time.sleep(2)
        queues.click()
        time.sleep(2)
        Queueplusbutton = login.find_elements(By.XPATH, "//span[normalize-space()='Add Queue']")
        assert Queueplusbutton[0].is_displayed(),\
        "'Create Queue' button should be visible after enabling the checkbox!"
        print("Test passed: Create Queue button is visible after enabling checkbox.")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH,  "//span[normalize-space()='Add Queue']")
        time.sleep(3)
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Queue Updation Disabling")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_QueueUpdation(login):
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
        schedule_management = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Schedule and Queue Management']"))
            )
        scroll_to_element(login, schedule_management)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-37-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the send booking attachments...")
            update_queue = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[37]"))
            )
            update_queue.click()
            time.sleep(3)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        else:
            pass
        wait_and_locate_click(login, By.XPATH, "//li[7]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        queues = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Set when you want to start a virtual queue and iss')]"))
        )
        scroll_to_element(login, queues)
        time.sleep(2)
        queues.click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[6]"))
        ).click()
        time.sleep(2)
        Queueedit = login.find_elements(By.XPATH, "//span[normalize-space()='Edit']")
        assert len(Queueedit) == 0 or not Queueedit[0].is_displayed(),\
        "'Update Queue' button should NOT be visible after disabling the checkbox!"
        print("Test passed: Update Queue button is NOT visible after disabling checkbox.")
        time.sleep(3)
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
    
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Queue Updation Enabling")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_QueueUpdation(login):
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
        schedule_management = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Schedule and Queue Management']"))
            )
        scroll_to_element(login, schedule_management)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-37-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to Enabled the send booking attachments...")
            update_queue = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[37]"))
            )
            update_queue.click()
            time.sleep(3)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "//li[7]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        queues = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Set when you want to start a virtual queue and iss')]"))
        )
        scroll_to_element(login, queues)
        time.sleep(2)
        queues.click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[6]"))
        ).click()
        time.sleep(2)
        Queueedit = login.find_elements(By.XPATH, "//span[normalize-space()='Edit']")
        assert Queueedit[0].is_displayed(),\
        "'Update Queue' button should be visible after enabling the checkbox!"
        print("Test passed: Update Queue button is visible after enabling checkbox.")
        time.sleep(3)
        WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Edit']"))
        ).click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()
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
    
    





