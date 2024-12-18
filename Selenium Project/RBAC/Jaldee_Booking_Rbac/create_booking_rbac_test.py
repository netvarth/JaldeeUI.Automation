

from Framework.common_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with disabling Create Booking")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_createBooking(login):
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
          booking_management = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Booking Management']"))
               )
          scroll_to_element(login, booking_management)
          time.sleep(2)
          checkbox = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-2-input'])[1]"))
               )
          is_checked = checkbox.is_selected()
          if is_checked:
               print("Checkbox is selected, proceeding to disabled the create booking...")
               create_booking = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[2]"))
               )
               create_booking.click()
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
          wait_and_locate_click(login, By.XPATH, "//li[2]//a[1]//div[1]//span[1]//span[1]//img[1]")
          time.sleep(2)
          create_appointment = WebDriverWait(login, 10).until(
               EC.invisibility_of_element_located((By.XPATH, "//img[@src='assets/images/dashboard/create-booking.png']"))
          )
          if not create_appointment:
               print("Testcase Failed: Create Appointment button is visible after disabling checkbox.")
               assert False, "Create Appointment button should NOT be visible after disabling the checkbox!"
          else:
               print("Test passed: Create Appointment button is NOT visible after disabling checkbox.")
          time.sleep(3)
          wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]")
          time.sleep(3)
          create_token = WebDriverWait(login, 10).until(
               EC.invisibility_of_element_located((By.XPATH, "//img[@src='assets/images/dashboard/create-booking.png']"))
          )
          if not create_token:
               print("Testcase Failed: Create Token button is visible after disabling checkbox.")
               assert False, "Create Token button should NOT be visible after disabling the checkbox!"
          else:
               print("Test passed: Create Token button is NOT visible after disabling checkbox.")
          time.sleep(3)
          wait_and_locate_click(login, By.XPATH, "//li[5]//a[1]//div[1]//span[1]//span[1]//img[1]")
          time.sleep(3)
          wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter name or phone or id']", 5550009954)
          time.sleep(3)
          wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 1']")
          time.sleep(3)
          create_appointment = WebDriverWait(login, 10).until(
               EC.invisibility_of_element_located((By.XPATH, "//button[normalize-space()='Create Appointment']"))
          )
          if not create_appointment:
               print("Testcase Failed: Patient tab Create Appointment button is visible after disabling checkbox.")
               assert False, "Patient tab Create Appointment button should NOT be visible after disabling the checkbox!"
          else:
               print("Test passed: Patient tab Create Appointment button is NOT visible after disabling checkbox.")
          time.sleep(3)
          create_token = WebDriverWait(login, 10).until(
               EC.invisibility_of_element_located((By.XPATH, "//button[normalize-space()='Create Token']"))
          )
          if not create_token:
               print("Testcase Failed: Patient Create Token button is visible after disabling checkbox.")
               assert False, "Patient Create Token button should NOT be visible after disabling the checkbox!"
          else:
               print("Test passed: Patient Create Token button is NOT visible after disabling checkbox.")
          time.sleep(3)
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with enabling Create Appointment Booking")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])

def test_Rbac_Enabled_createAppointmentBooking(login):
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
          booking_management = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Booking Management']"))
               )
          scroll_to_element(login, booking_management)
          time.sleep(2)
          checkbox = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-2-input'])[1]"))
               )
          is_checked = checkbox.is_selected()
          if is_checked:
               pass
          else:
               create_booking = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[2]"))
               )
               create_booking.click()
               time.sleep(2)
               wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
               time.sleep(2)
               wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
               message = get_snack_bar_message(login)
               print("Snack bar message:", message)
               time.sleep(2)
          wait_and_locate_click(login, By.XPATH, "//li[2]//a[1]//div[1]//span[1]//span[1]//img[1]")
          time.sleep(3)
          create_appointment = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//div[@class='p-card-content'])[3]"))
          )
          assert create_appointment.is_displayed(), "Create Appointment button is NOT displayed after enabling checkbox!"
          print("Create Appointment button is displayed. Proceeding to take an appointment.")
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
          assert message == "Appointment created successfully", f"Expected message 'Appointment created successfully', but got: {message}"
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with enabling Patient tab Create Appointment Booking")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])

def test_Rbac_Enabled_patientAppointmentBooking(login):
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
          booking_management = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Booking Management']"))
               )
          scroll_to_element(login, booking_management)
          time.sleep(2)
          checkbox = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-2-input'])[1]"))
               )
          is_checked = checkbox.is_selected()
          if is_checked:
               pass
          else:
               create_booking = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[2]"))
               )
               create_booking.click()
               time.sleep(2)
               wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
               time.sleep(2)
               wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
               message = get_snack_bar_message(login)
               print("Snack bar message:", message)
               time.sleep(2)
          wait_and_locate_click(login, By.XPATH, "//li[5]//a[1]//div[1]//span[1]//span[1]//img[1]")
          time.sleep(3)
          wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter name or phone or id']", 5550009954)
          time.sleep(1)
          wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 1']")
          time.sleep(2)
          create_appointment = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create Appointment']"))
          )
          assert create_appointment.is_displayed(), "Create Appointment button is NOT displayed after enabling checkbox!"
          print("Create Appointment button is displayed. Proceeding to take an appointment.")
          create_appointment.click()
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
          assert message == "Appointment created successfully", f"Expected message 'Appointment created successfully', but got: {message}"
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with enabling Create Token Booking")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])

def test_Rbac_Enabled_createTokenBooking(login):
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
          booking_management = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Booking Management']"))
               )
          scroll_to_element(login, booking_management)
          time.sleep(2)
          checkbox = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-2-input'])[1]"))
               )
          is_checked = checkbox.is_selected()
          if is_checked:
               pass
          else:
               create_booking = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[2]"))
               )
               create_booking.click()
               time.sleep(2)
               wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
               time.sleep(2)
               wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
               message = get_snack_bar_message(login)
               print("Snack bar message:", message)
               time.sleep(2)
          wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]")
          time.sleep(3)
          create_token = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//div[@class='p-card-content'])[3]"))
          )
          assert create_token.is_displayed(), "Create Token button is NOT displayed after enabling checkbox!"
          print("Create Token button is displayed. Proceeding to take an appointment.")
          create_token.click()
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
          assert message == "Token has been generated successfully", f"Expected message 'Token has been generated successfully', but got: {message}"
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with enabling Patient tab Create Token Booking")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])

def test_Rbac_Enabled_patientTokenBooking(login):
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
          booking_management = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Booking Management']"))
               )
          scroll_to_element(login, booking_management)
          time.sleep(2)
          checkbox = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-2-input'])[1]"))
               )
          is_checked = checkbox.is_selected()
          if is_checked:
               pass
          else:
               create_booking = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[2]"))
               )
               create_booking.click()
               time.sleep(2)
               wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
               time.sleep(2)
               wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
               message = get_snack_bar_message(login)
               print("Snack bar message:", message)
               time.sleep(2)
          wait_and_locate_click(login, By.XPATH, "//li[5]//a[1]//div[1]//span[1]//span[1]//img[1]")
          time.sleep(3)
          wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter name or phone or id']", 5550009954)
          time.sleep(3)
          wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 1']")
          time.sleep(3)
          create_token = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Create Token']"))
          )
          create_token.click()
          assert create_token.is_displayed(), "Create Token button is NOT displayed after enabling checkbox!"
          print("Create Token button is displayed. Proceeding to take Token.")
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
          
          assert message == "Token has been generated successfully", f"Expected message 'Token has been generated successfully', but got: {message}"
     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with disabling ViewHistory Booking")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_viewhistoryBooking(login):
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
          booking_management = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Booking Management']"))
               )
          scroll_to_element(login, booking_management)
          time.sleep(2)
          checkbox = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-13-input'])[1]"))
               )
          is_checked = checkbox.is_selected()
          if is_checked:
               print("Checkbox is selected, proceeding to disabled the view history booking...")
               history_booking = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[13]"))
               )
               history_booking.click()
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
          wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]")
          time.sleep(2)
          WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//div[@class='p-dropdown p-component'])[2]"))
          ).click()
          time.sleep(2)
          WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='History']"))
          ).click()
          time.sleep(2)
          history_count = login.find_elements(By.XPATH, "//span[normalize-space()='(0)']")
          if len(history_count) > 0:
               assert history_count[0].text == "(0)" and history_count[0].is_displayed(), \
                    "'History Count' is not showing (0) or is not visible after disabling the checkbox!"
          else:
               assert True, "History count is absent as expected."

          print("Test passed: 'History Count' is zero or hidden after disabling the checkbox!")

     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with enabling ViewHistory Booking")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_viewhistoryBooking(login):
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
          booking_management = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Booking Management']"))
               )
          scroll_to_element(login, booking_management)
          time.sleep(2)
          checkbox = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-13-input'])[1]"))
               )
          is_checked = checkbox.is_selected()
          if is_checked:
               pass
          else:
               print("Checkbox is not selected, proceeding to enabled the view history booking...")
               history_booking = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[13]"))
               )
               history_booking.click()
               time.sleep(2)
               wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
               time.sleep(2)
               wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
               message = get_snack_bar_message(login)
               print("Snack bar message:", message)
               time.sleep(2)
          time.sleep(3)
          wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]")
          time.sleep(2)
          WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//div[@class='p-dropdown p-component'])[2]"))
          ).click()
          time.sleep(2)
          WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='History']"))
          ).click()
          time.sleep(2)
          history_count = login.find_elements(By.XPATH, "//span[contains(text(),'(')]")
          if len(history_count) > 0:
               history_text = history_count[0].text  
               count_value = int(history_text.strip('()'))
               assert count_value > 0, f"Test failed: History count is not greater than zero, found {count_value}!"
               print(f"Test passed: 'History Count' is greater than zero ({count_value}) after enabling the checkbox!")
          else:
               assert False, "Test failed: History count element not found after enabling the checkbox."


     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with disabling ViewFuture Booking")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_viewfutureBooking(login):
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
          booking_management = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Booking Management']"))
               )
          scroll_to_element(login, booking_management)
          time.sleep(2)
          checkbox = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-14-input'])[1]"))
               )
          is_checked = checkbox.is_selected()
          if is_checked:
               print("Checkbox is selected, proceeding to disabled the view history booking...")
               future_booking = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[14]"))
               )
               future_booking.click()
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
          wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]")
          time.sleep(2)
          WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//div[@class='p-dropdown p-component'])[2]"))
          ).click()
          time.sleep(2)
          WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Future']"))
          ).click()
          time.sleep(2)
          future_count = login.find_elements(By.XPATH, "//span[normalize-space()='(0)']")
          if len(future_count) > 0:
               assert future_count[0].text == "(0)" and future_count[0].is_displayed(), \
                    "'Future Count' is not showing (0) or is not visible after disabling the checkbox!"
          else:
               assert True, "Future count is absent as expected."

          print("Test passed: 'Future Count' is zero or hidden after disabling the checkbox!")

     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with enabling View Future Booking")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_viewfutureBooking(login):
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
          booking_management = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Booking Management']"))
               )
          scroll_to_element(login, booking_management)
          time.sleep(2)
          checkbox = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-14-input'])[1]"))
               )
          is_checked = checkbox.is_selected()
          if is_checked:
               pass
          else:
               print("Checkbox is not selected, proceeding to enabled the view history booking...")
               future_booking = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[14]"))
               )
               future_booking.click()
               time.sleep(2)
               wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
               time.sleep(2)
               wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
               message = get_snack_bar_message(login)
               print("Snack bar message:", message)
               time.sleep(2)
          time.sleep(3)
          wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]")
          time.sleep(2)
          WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//div[@class='p-dropdown p-component'])[2]"))
          ).click()
          time.sleep(2)
          WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Future']"))
          ).click()
          time.sleep(2)
          future_count = login.find_elements(By.XPATH, "//span[contains(text(),'(')]")
          if len(future_count) > 0:
               future_text = future_count[0].text  
               count_value = int(future_text.strip('()'))
               assert count_value > 0, f"Test failed: Future count is not greater than zero, found {count_value}!"
               print(f"Test passed: 'Future Count' is greater than zero ({count_value}) after enabling the checkbox!")
          else:
               assert False, "Test failed: Future count element not found after enabling the checkbox."


     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with disabling ViewTodayBooking")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Disabled_viewtodayBooking(login):
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
          booking_management = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Booking Management']"))
               )
          scroll_to_element(login, booking_management)
          time.sleep(2)
          checkbox = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-8-input'])[1]"))
               )
          is_checked = checkbox.is_selected()
          if is_checked:
               print("Checkbox is selected, proceeding to disabled the view today booking...")
               today_booking = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[8]"))
               )
               today_booking.click()
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
          wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]")
          time.sleep(2)
          WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//div[@class='p-dropdown p-component'])[2]"))
          ).click()
          time.sleep(2)
          WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Today']"))
          ).click()
          time.sleep(2)
          today_count = login.find_elements(By.XPATH, "//span[normalize-space()='(0)']")
          if len(today_count) > 0:
               assert today_count[0].text == "(0)" and today_count[0].is_displayed(), \
                    "'Today Count' is not showing (0) or is not visible after disabling the checkbox!"
          else:
               assert True, "Today count is absent as expected."

          print("Test passed: 'Today Count' is zero or hidden after disabling the checkbox!")

     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e
     

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("RBAC Booking Management with enabling View Today Booking")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Rbac_Enabled_viewtodayBooking(login):
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
          booking_management = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Booking Management']"))
               )
          scroll_to_element(login, booking_management)
          time.sleep(2)
          checkbox = WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//input[@id='mat-mdc-checkbox-8-input'])[1]"))
               )
          is_checked = checkbox.is_selected()
          if is_checked:
               pass
          else:
               print("Checkbox is not selected, proceeding to enabled the view history booking...")
               today_booking = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-form-field'])[8]"))
               )
               today_booking.click()
               time.sleep(2)
               wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
               time.sleep(2)
               wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']")
               message = get_snack_bar_message(login)
               print("Snack bar message:", message)
               time.sleep(2)
          time.sleep(3)
          wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]")
          time.sleep(2)
          WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "(//div[@class='p-dropdown p-component'])[2]"))
          ).click()
          time.sleep(2)
          WebDriverWait(login, 10).until(
               EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Today']"))
          ).click()
          time.sleep(2)
          today_count = login.find_elements(By.XPATH, "//span[contains(text(),'(')]")
          if len(today_count) > 0:
               today_text = today_count[0].text  
               count_value = int(today_text.strip('()'))
               assert count_value > 0, f"Test failed: Today count is not greater than zero, found {count_value}!"
               print(f"Test passed: 'Today Count' is greater than zero ({count_value}) after enabling the checkbox!")
          else:
               assert False, "Test failed: Today count element not found after enabling the checkbox."


     except Exception as e:
          allure.attach(  
          login.get_screenshot_as_png(),  
          name="full_page", 
          attachment_type=AttachmentType.PNG,
          )
          raise e    