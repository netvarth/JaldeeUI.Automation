from Framework.common_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with disabling Create Booking Invoice")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_Invoicecreate(login):
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
        booking_invoices = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Booking Invoices']"))
            )
        scroll_to_element(login, booking_invoices)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-24-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the send booking attachments...")
            create_bookinginvoices = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[24]"))
            )
            create_bookinginvoices.click()
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
        New_Invoice = login.find_elements(By.XPATH, "//button[normalize-space()='New Invoice']")
        assert len(New_Invoice) == 0 or not New_Invoice[0].is_displayed(),\
        "'New_Invoice' button should NOT be visible after disabling the checkbox!"
        print("Test passed: New_Invoice button is NOT visible after disabling checkbox.")
        time.sleep(3)
        WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")) 
        ).click()
        time.sleep(2)
        New_Invoices = login.find_elements(By.XPATH, "//button[normalize-space()='New Invoice']")
        assert len(New_Invoices) == 0 or not New_Invoices[0].is_displayed(),\
        "'New_Invoices' button should NOT be visible after disabling the checkbox!"
        print("Test passed: New_Invoices button is NOT visible after disabling checkbox.")
        time.sleep(3)
        
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with enabling Invoice Create")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_Invoicecreate(login):
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
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-24-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to disabled the send booking attachments...")
            create_booking_invoices = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[24]"))
            )
            create_booking_invoices.click()
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
        create_invoice = login.find_elements(By.XPATH, "//button[normalize-space()='New Invoice']")
        assert create_invoice[0].is_displayed(),\
        "'Create_invoice' button should be visible after enabling the checkbox!"
        print("Test passed: Create_invoice button is visible after enabling checkbox.")
        time.sleep(3)
        WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")) 
        ).click()
        time.sleep(2)
        create_invoice = login.find_elements(By.XPATH, "//button[normalize-space()='New Invoice']")
        assert create_invoice[0].is_displayed(),\
        "'Create_invoice' button should be visible after enabling the checkbox!"
        print("Test passed: Create_invoice button is visible after enabling checkbox.")
        time.sleep(3)
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with disabling Create Booking View Invoice")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_ViewInvoice(login):
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
        booking_invoices = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Booking Invoices']"))
            )
        scroll_to_element(login, booking_invoices)
        time.sleep(2)
        checkbox = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-26-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            print("Checkbox is selected, proceeding to disabled the send booking attachments...")
            create_booking_viewinvoices = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[26]"))
            )
            create_booking_viewinvoices.click()
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
        View_Invoice = login.find_elements(By.XPATH, "//button[normalize-space()='View Invoice']")
        assert len(View_Invoice) == 0 or not View_Invoice[0].is_displayed(),\
        "'View_Invoice' button should NOT be visible after disabling the checkbox!"
        print("Test passed: View_Invoice button is NOT visible after disabling checkbox.")
        time.sleep(3)
        WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")) 
        ).click()
        time.sleep(2)
        View_Invoices = login.find_elements(By.XPATH, "//button[normalize-space()='View Invoice']")
        assert len(View_Invoices) == 0 or not View_Invoices[0].is_displayed(),\
        "'View_Invoices' button should NOT be visible after disabling the checkbox!"
        print("Test passed: View_Invoices button is NOT visible after disabling checkbox.")
        time.sleep(3)
        
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with enabling View Invoice ")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_ViewInvoice(login):
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
            EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-26-input'])[1]"))
            )
        is_checked = checkbox.is_selected()
        if is_checked:
            pass
        else:
            print("Checkbox is selected, proceeding to disabled the send booking attachments...")
            view_booking_invoices = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[26]"))
            )
            view_booking_invoices.click()
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
        view_invoice = login.find_elements(By.XPATH, "//button[normalize-space()='View Invoice']")
        assert view_invoice[0].is_displayed(),\
        "'View_invoice' button should be visible after enabling the checkbox!"
        print("Test passed: View_invoice button is visible after enabling checkbox.")
        time.sleep(3)
        WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")) 
        ).click()
        time.sleep(2)
        view_invoice = login.find_elements(By.XPATH, "//button[normalize-space()='View Invoice']")
        assert view_invoice[0].is_displayed(),\
        "'View_invoice' button should be visible after enabling the checkbox!"
        print("Test passed: View_invoice button is visible after enabling checkbox.")
        time.sleep(3)
    except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
    

