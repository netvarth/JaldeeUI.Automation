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
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-20-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the send booking attachments...")
            send_booking_attachments = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[20]"))
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
        wait_and_locate_click(login, By.XPATH, "//li[2]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        create_appointment = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//div[@class='p-card-content'])[3]"))
        )
        create_appointment.click()
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter name or phone or id']", 5550009954)
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 1']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='place']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Round North']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='displayName']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='General Services']")
        time.sleep(2)
        uploadfile = login.find_elements(By.XPATH, "//span[normalize-space()='Upload File']")
        assert len(uploadfile) == 0 or not uploadfile[0].is_displayed(),\
        "'Upload File' button should NOT be visible after disabling the checkbox!"
        print("Test passed: Upload File button is NOT visible after disabling checkbox.")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Confirm']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        while True:
            try:
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                        )
                    )
                )

                next_button.click()
            except:
                break
            time.sleep(3)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
                )
            )
        )
        last_element_in_accordian.click()
        time.sleep(3)  
        WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")) 
        ).click()

        time.sleep(2)
        wait_and_visible_click(login, By.XPATH,  "//button[normalize-space()='More Actions']")
        send_attachment = login.find_elements(By.XPATH, "//button[normalize-space()='Send Attachments']")
        assert len(send_attachment) == 0 or not send_attachment[0].is_displayed(),\
        "'Send_attachment' button should NOT be visible after disabling the checkbox!"
        print("Test passed: Send_attachment button is NOT visible after disabling checkbox.")
        time.sleep(3)
        
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with disabling Send-attachments")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_send_booking_attachment(login):
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
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-20-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to disabled the send booking attachments...")
            send_booking_attachments = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[20]"))
            )
            send_booking_attachments.click()
            time.sleep(3)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[2]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        create_appointment = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//div[@class='p-card-content'])[3]"))
        )
        create_appointment.click()
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter name or phone or id']", 5550009954)
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 1']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='place']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Round North']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='displayName']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='General Services']")
        time.sleep(2)
        uploadfile = login.find_elements(By.XPATH, "//span[normalize-space()='Upload File']")
        assert uploadfile[0].is_displayed(),\
        "'Upload File' button should  be visible after enabling the checkbox!"
        print("Test passed: Upload File button is visible after enabling checkbox.")
        time.sleep(3)
        uploadfile = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Upload File']"))
        )
        login.execute_script("arguments[0].scrollIntoView(true);", uploadfile)
        time.sleep(2)
        uploadfile.click()
        time.sleep(2)
        current_working_directory = os.getcwd()
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Confirm']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        while True:
            try:
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                        )
                    )
                )

                next_button.click()
            except:
                break
            time.sleep(3)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
                )
            )
        )
        last_element_in_accordian.click()
        time.sleep(3)  
        WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")) 
        ).click()

        time.sleep(2)
        wait_and_visible_click(login, By.XPATH,  "//button[normalize-space()='More Actions']")
        send_attachment = login.find_elements(By.XPATH, "//button[normalize-space()='Send Attachments']")
        assert send_attachment[0].is_displayed(),\
        "'Send_attachment' button should be visible after enabling the checkbox!"
        print("Test passed: Send_attachment button is visible after enabling checkbox.")
        time.sleep(3)
        wait_and_visible_click(login, By.XPATH,  "//button[normalize-space()='Send Attachments']")
        wait_and_locate_click(login, By.XPATH,  "//label[normalize-space()='Click here to select the files']")
        time.sleep(3)
        current_working_directory = os.getcwd()
        absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))
        pyautogui.write(absolute_path)
        pyautogui.press('enter')
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH,  "//span[contains(text(),'send')]")
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
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with disabling Share Booking Information")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_Sharebookinginfo(login):
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
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-22-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the send booking attachments...")
            share_booking_info = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[22]"))
            )
            share_booking_info.click()
            time.sleep(3)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        else:
            pass
        wait_and_locate_click(login, By.XPATH, "//li[2]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        create_appointment = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//div[@class='p-card-content'])[3]"))
        )
        create_appointment.click()
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter name or phone or id']", 5550009954)
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 1']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='place']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Round North']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='displayName']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='General Services']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Confirm']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        while True:
            try:
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                        )
                    )
                )

                next_button.click()
            except:
                break
            time.sleep(3)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
                )
            )
        )
        last_element_in_accordian.click()
        time.sleep(3)  
        WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")) 
        ).click()

        time.sleep(2)
        wait_and_visible_click(login, By.XPATH,  "//button[normalize-space()='More Actions']")
        Share_Info = login.find_elements(By.XPATH, "//button[normalize-space()='Share Info']")
        assert len(Share_Info) == 0 or not Share_Info[0].is_displayed(),\
        "'Share_Info' button should NOT be visible after disabling the checkbox!"
        print("Test passed: Share_Info button is NOT visible after disabling checkbox.")
        time.sleep(3)
        
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with enabling Share Booking Information")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_shareinfo(login):
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
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-22-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to disabled the share info...")
            shareinfo = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[22]"))
            )
            shareinfo.click()
            time.sleep(3)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[2]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        create_appointment = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//div[@class='p-card-content'])[3]"))
        )
        create_appointment.click()
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter name or phone or id']", 5550009954)
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 1']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='place']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Round North']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='displayName']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='General Services']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Confirm']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        while True:
            try:
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                        )
                    )
                )

                next_button.click()
            except:
                break
            time.sleep(3)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
                )
            )
        )
        last_element_in_accordian.click()
        time.sleep(3)  
        WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")) 
        ).click()

        time.sleep(2)
        wait_and_visible_click(login, By.XPATH,  "//button[normalize-space()='More Actions']")
        shareinfor = login.find_elements(By.XPATH, "//button[normalize-space()='Share Info']")
        assert shareinfor[0].is_displayed(),\
        "'Share Info' button should be visible after enabling the checkbox!"
        print("Test passed: Share Info button is visible after enabling checkbox.")
        time.sleep(3)
        wait_and_visible_click(login, By.XPATH,  "//button[normalize-space()='Share Info']")
        wait_and_locate_click(login, By.XPATH,  "//span[@class='mdc-button__label']")
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
    


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with disabling Send_communication_messages")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_Send_communication_messages(login):
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
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-21-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the send booking attachments...")
            send_communication_msgs = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[21]"))
            )
            send_communication_msgs.click()
            time.sleep(3)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        else:
            pass
        wait_and_locate_click(login, By.XPATH, "//li[2]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        create_appointment = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//div[@class='p-card-content'])[3]"))
        )
        create_appointment.click()
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter name or phone or id']", 5550009954)
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 1']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='place']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Round North']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='displayName']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='General Services']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Confirm']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        while True:
            try:
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                        )
                    )
                )

                next_button.click()
            except:
                break
            time.sleep(3)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
                )
            )
        )
        last_element_in_accordian.click()
        time.sleep(3)  
        WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")) 
        ).click()

        time.sleep(2)
        wait_and_visible_click(login, By.XPATH,  "//button[normalize-space()='More Actions']")
        send_communication = login.find_elements(By.XPATH, "//button[normalize-space()='Send Message']")
        assert len(send_communication) == 0 or not send_communication[0].is_displayed(),\
        "'Send_communication_messages' button should NOT be visible after disabling the checkbox!"
        print("Test passed: Send_communication_messages button is NOT visible after disabling checkbox.")
        time.sleep(3)
        
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with enabling Send_communication_messages")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_Send_communication_messages(login):
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
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-21-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to enabled the send booking attachments...")
            send_communication_msgs = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[21]"))
            )
            send_communication_msgs.click()
            time.sleep(3)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[2]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        create_appointment = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//div[@class='p-card-content'])[3]"))
        )
        create_appointment.click()
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter name or phone or id']", 5550009954)
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 1']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='place']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Round North']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='displayName']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='General Services']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Confirm']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        while True:
            try:
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                        )
                    )
                )

                next_button.click()
            except:
                break
            time.sleep(3)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
                )
            )
        )
        last_element_in_accordian.click()
        time.sleep(3)  
        WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")) 
        ).click()

        time.sleep(2)
        wait_and_visible_click(login, By.XPATH,  "//button[normalize-space()='More Actions']")
        send_communication = login.find_elements(By.XPATH, "//button[normalize-space()='Send Message']")
        assert send_communication[0].is_displayed(),\
        "'Send_communication' button should be visible after enabling the checkbox!"
        print("Test passed: Send_communication button is visible after enabling checkbox.")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH,  "//button[normalize-space()='Send Message']")
        login.find_element(By.XPATH, " //textarea[@id='messageData']").send_keys("test_selenium project")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH,  "//label[normalize-space()='Click here to select the files']")
        time.sleep(3)
        current_working_directory = os.getcwd()
        absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))
        pyautogui.write(absolute_path)
        pyautogui.press('enter')
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH,  "//span[contains(text(),'send')]")
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
    


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with disabling View_Attachment")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_Viewattachment(login):
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
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-23-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the Viewattachments...")
            share_booking_info = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[23]"))
            )
            share_booking_info.click()
            time.sleep(3)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        else:
            pass
        wait_and_locate_click(login, By.XPATH, "//li[2]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        create_appointment = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//div[@class='p-card-content'])[3]"))
        )
        create_appointment.click()
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter name or phone or id']", 5550009954)
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 1']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='place']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Round North']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='displayName']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='General Services']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Confirm']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        while True:
            try:
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                        )
                    )
                )

                next_button.click()
            except:
                break
            time.sleep(3)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
                )
            )
        )
        last_element_in_accordian.click()
        time.sleep(3)  
        View_Attachments = login.find_elements(By.XPATH, "//button[normalize-space()='View Attachments']")
        assert len(View_Attachments) == 0 or not View_Attachments[0].is_displayed(),\
        "'View_Attachments' button should NOT be visible after disabling the checkbox!"
        print("Test passed: View_Attachments button is NOT visible after disabling checkbox.")
        time.sleep(3)
        WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")) 
        ).click()

        time.sleep(2)
        wait_and_visible_click(login, By.XPATH,  "//button[normalize-space()='More Actions']")
        View_Attachments = login.find_elements(By.XPATH, "//button[normalize-space()='View Attachments']")
        assert len(View_Attachments) == 0 or not View_Attachments[0].is_displayed(),\
        "'View_Attachments' button should NOT be visible after disabling the checkbox!"
        print("Test passed: View_Attachments button is NOT visible after disabling checkbox.")
        time.sleep(3)
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with enabling View Attachments")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_View_Attachments(login):
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
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-23-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to enabled the send booking attachments...")
            send_communication_msgs = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[23]"))
            )
            send_communication_msgs.click()
            time.sleep(3)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
            time.sleep(2)
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
            message = get_snack_bar_message(login)
            print("Snack bar message:", message)
            time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//li[2]//a[1]//div[1]//span[1]//span[1]//img[1]")
        time.sleep(2)
        create_appointment = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//div[@class='p-card-content'])[3]"))
        )
        create_appointment.click()
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter name or phone or id']", 5550009954)
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 1']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='place']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Round North']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@optionlabel='displayName']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='General Services']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Confirm']")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        while True:
            try:
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                        )
                    )
                )

                next_button.click()
            except:
                break
            time.sleep(3)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
                )
            )
        )
        last_element_in_accordian.click()
        time.sleep(3)  
        View_Attachments = login.find_elements(By.XPATH, "//button[normalize-space()='View Attachments']")
        assert View_Attachments[0].is_displayed(),\
        "'View_Attachments' button should be visible after enabling the checkbox!"
        print("Test passed: View_Attachments button is visible after enabling checkbox.")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH,  "//button[normalize-space()='View Attachments']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH,  "//i[@class='fa fa-window-close']")
        time.sleep(2)
        WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")) 
        ).click()

        time.sleep(2)
        wait_and_visible_click(login, By.XPATH,  "//button[normalize-space()='More Actions']")
        View_Attachment = login.find_elements(By.XPATH, "//button[normalize-space()='View Attachments']")
        assert View_Attachment[0].is_displayed(),\
        "'View_Attachment' button should be visible after enabling the checkbox!"
        print("Test passed: View_Attachment button is visible after enabling checkbox.")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH,  "//button[normalize-space()='View Attachments']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH,  "//i[@class='fa fa-window-close']")
        time.sleep(2)
       
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
    
