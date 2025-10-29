from Framework.common_utils import *
from Framework.common_dates_utils import *
import random
from faker import Faker

# <<< << <<  << Room and Bed Test cases >>  >>  >>  >>  

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Room creation")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_1(login):

    try:

        wait = WebDriverWait(login, 30)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='dashboard-card-image'])[6]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Create Room')]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Building'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Floor'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Type'])[1]"))
        ).click()

        time.sleep(1)   
        room_type = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal Room'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", room_type)
        room_type.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Category'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Private Room'])[1]"))
        ).click()

        time.sleep(2)
        room_name = get_next_room_name()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Room Name'])[1]")
            )
        ).send_keys(room_name)

        print(f"🏨 Room created: {room_name}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Room Nature'])[1]")
            )
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Room'])[1]")
            )
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]")
            )
        ).click()

        toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_detail.text
        print("toast_Message:", message)

        time.sleep(2)
        WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody//tr[1]"))
        )

        # Step 3: Fetch and print the first row text
        first_row = login.find_element(By.XPATH, "//tbody//tr[1]")
        print(f"First row text: {first_row.text}")

        # Step 4: Assertion and print result
        if room_name in first_row.text:
            print(f"✅ Room '{room_name}' is present in the first row.")
            print(f"❌ Room '{room_name}' NOT found in the first row: {first_row.text}")
            assert False, f"{room_name} not found in first row"

        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Bed creation for room")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_2(login):

    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30) 

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//img)[4]"))    
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='my-1 font-small fw-bold text-capitalize ng-star-inserted'][normalize-space()='Rooms'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'Room Details')])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1] "))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Bed Type'])[1]"))
        ).click()

        time.sleep(3)
        bed_type = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", bed_type)
        bed_type.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Bed Category'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Observation Beds'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Bed Pricing'])[1]"))
        ).click()

        time.sleep(1)
        bed_price = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Manual Hospital Bed'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_price)
        bed_price.click()

        time.sleep(1)

        room_name = get_next_room_name()
        
        bed_name  = f'Bed{room_name}'
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Bed Name'])[1]"))
        ).send_keys(bed_name) 

        print(f"🛏️ Bed created: {bed_name}")

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()

        toast_detail = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )   
        assert "Bed created" in toast_detail.text   
        print("toast_Message:", toast_detail.text)
        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: IP room creation with existing room name")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_3(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='dashboard-card-image'])[6]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Create Room')]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Building'])[1]"))
        ).click()   

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Block B'])[1]"))
        ).click()   

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Floor'])[1]"))
        ).click()
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Type'])[1]"))
        ).click()

        time.sleep(1)
        room_type = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal Room'])[1]"))
        )   
        login.execute_script("arguments[0].scrollIntoView();", room_type)
        room_type.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Category'])[1]"))
        ).click()
        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Private Room'])[1]"))
        ).click()
        
        existing_room_name = "305B"

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Room Name'])[1]")
            )
        ).send_keys(existing_room_name)     

        print(f"🏨 Room created: {existing_room_name}")

        time.sleep(2)   

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Room Nature'])[1]")
            )
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Room'])[1]")
            )
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]")
            )
        ).click()

        toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_detail.text
        print("toast_Message:", message)
        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: IP room creation with existing bed name")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_4(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//img)[4]"))    
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='my-1 font-small fw-bold text-capitalize ng-star-inserted'][normalize-space()='Rooms'])[1]"))
        ).click()

        time.sleep(1)

        room_name_to_find = "581B"
        found = False

        while True:
            # Get all rows
            rows = login.find_elements(By.XPATH, "//tbody[@class='p-element p-datatable-tbody']/tr")

            for row in rows:
                try:
                    room_name_element = row.find_element(By.XPATH, ".//td[1]//span[contains(@class, 'fw-bold')]")
                    room_name = room_name_element.text.strip()

                    if room_name == room_name_to_find:
                        print(f"✅ Room '{room_name}' found")

                        # Click the Room Details button in the same row
                        room_details_button = row.find_element(
                            By.XPATH, ".//button[.//span[normalize-space()='Room Details']]"
                        )
                        login.execute_script("arguments[0].scrollIntoView();", room_details_button)
                        room_details_button.click()
                        time.sleep(10)
                        print(f"🟢 Clicked 'Room Details' for room '{room_name}'")
                        # return True
                        found = True
                        break  # break inner for-loop
                except Exception as e:
                    continue  # If a row structure is malformed, skip to next row
            if found:
                break  # break outer while-loop

            # If not found on current page, try clicking "next"
            try:
                next_button = login.find_element(
                    By.XPATH,
                    "//button[contains(@class, 'p-paginator-next') and not(contains(@class, 'p-disabled'))]"
                )
                login.execute_script("arguments[0].scrollIntoView();", next_button)
                next_button.click()
                time.sleep(2)  # wait for new page to load
            except:
                print(f"❌ Room '{room_name_to_find}' not found after checking all pages.")
                return False  # Exit if no more pages

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Select Bed Type'])[1]"))
        ).click()

        time.sleep(2)
        bed_type = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Normal'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_type)
        bed_type.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Select Bed Category'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Observation Beds'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Select Bed Pricing'])[1]"))
        ).click()

        time.sleep(1)
        bed_price = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Manual Hospital Bed'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_price)
        bed_price.click()
        
        time.sleep(1)
        existing_bed_name = "Bed351B"

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Bed Name'])[1]")
            )
        ).send_keys(existing_bed_name)

        print(f"🛏️ Bed created: {existing_bed_name}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]")
            )
        ).click()

        toast_detail = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_detail.text
        print("toast_Message:", message)

        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
# <<  <<  <<  <<  IP Prescription  >>  >>  >>  >>>  >>>

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Create the prescription From Medical Record")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_5(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//img)[4]"))    
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[13]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Medical Record')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='+ Add New Visit'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Krishna JP'])[1]"))
        ).click()   

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Visit'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)    
        
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Prescription'])[1]"))
        ).click()

        time.sleep(2)
        for i in range(5):
            login.find_element(
                By.XPATH, "//button[normalize-space()='+ Add Medicine']"
            ).click()
            login.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(
                "Medicine"
            )

            # Scope to the prescription modal dialog
            
            before_XPath = "//mat-dialog-container[@role='dialog' and contains(@class, 'mat-mdc-dialog-container')]//table[contains(@class, 'p-datatable-table')]//tbody/tr"
            aftertd_XPath_1 = "/td[2]"
            aftertd_XPath_2 = "/td[3]"
            aftertd_XPath_3 = "/td[4]"
            aftertd_XPath_4 = "/td[5]"
            textarea_xpath = "//input[@role='searchbox']"
            row = i + 1
            if i > 0:
                trXPath = before_XPath + str([row])
                trXPath = before_XPath

            PreFinalXPath = trXPath + aftertd_XPath_1
            FinalXPath = PreFinalXPath + textarea_xpath

            Dose = login.find_element(By.XPATH, PreFinalXPath)
            Dose.click()
            Dose1 = login.find_element(By.XPATH, FinalXPath)
            Dose1.send_keys("650 mg")

            PreFinalXPath = trXPath + aftertd_XPath_2
            FinalXPath = PreFinalXPath + textarea_xpath

            Frequency = login.find_element(By.XPATH, PreFinalXPath)
            Frequency.click()
            Frequency1 = login.find_element(By.XPATH, FinalXPath)
            Frequency1.send_keys("1-1-1")

            PreFinalXPath = trXPath + aftertd_XPath_3
            FinalXPath = PreFinalXPath + textarea_xpath
            Duration = login.find_element(By.XPATH, PreFinalXPath)
            Duration.click()
            Duration1 = login.find_element(By.XPATH, FinalXPath)
            Duration1.send_keys("5 Days")

            PreFinalXPath = trXPath + aftertd_XPath_4
            FinalXPath = PreFinalXPath + textarea_xpath
            Notes = login.find_element(By.XPATH, PreFinalXPath)
            Notes.click()
            Notes1 = login.find_element(By.XPATH, FinalXPath)
            Notes1.send_keys("After Food")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        share_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Share'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", share_button)    
        time.sleep(1)
        share_button.click()
        
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@placeholder='Enter message description'])[1]"))
        ).send_keys("This is a test message.")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Email'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Whatsapp'])[1]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@type='button'][normalize-space()='Share'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Upload the prescription From Medical Record")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_upload_prescription(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//img)[4]"))    
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[13]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Medical Record')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='+ Add New Visit'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Krishna JP'])[1]"))
        ).click()   

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Visit'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)    
        
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Prescription'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Upload Prescription'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Drop your files here'])[1]")

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()
        time.sleep(2)
        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        time.sleep(1)
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Save'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
    
        time.sleep(3)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.xfail(reason="Save button not clickable")
@allure.title("Test Case: Upload the prescription From Medical Record and edit upload another record")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_upload_prescription_edit_upload_second_one (login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//img)[4]"))    
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[13]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Medical Record')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='+ Add New Visit'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Krishna JP'])[1]"))
        ).click()   

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Visit'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)    
        
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Prescription'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Upload Prescription'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Drop your files here'])[1]")

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()
        time.sleep(2)
        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        time.sleep(1)
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Save'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//img[@alt='dropdown'])[1]")
        time.sleep(1)

        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Edit'])[1]")
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Upload Prescription'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Drop your files here'])[1]")

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()
        time.sleep(2)
        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        time.sleep(1)
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Save'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Save'])[1]")

        time.sleep(3)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
# <<<<   <<<<  << <<                >>>  >>  >>  >>  >>>>>  >>>
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Take admission from OP patient and cancel it")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)]) 
def  test_OP_Converted_to_IP_Patient_cancel(login):

    wait = WebDriverWait(login, 20)
    try: 
        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='dashboard-card-image'])[6]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(., 'Create Room')]"))  
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        drop_downlist = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal Room'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", drop_downlist)
        time.sleep(1)   
        drop_downlist.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Private Room'])[1]"))
        ).click()

        room_name = get_next_room_name()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Room Name'])[1]")
            )
        ).send_keys(room_name)

        print(f"🏨 Room created: {room_name}")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[5]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Room'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()
    
        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='Room Details'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()
        
        time.sleep(1)
        bed_type = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_type)
        time.sleep(1)
        bed_type.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Observation Beds'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        bed_price = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Manual Hospital Bed'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_price)
        time.sleep(1)
        bed_price.click()

        bed_name  = f'Bed{room_name}'
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Bed Name'])[1]"))
        ).send_keys(bed_name)   

        time.sleep(1)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()   

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Appointment'])[1]"))
        ).click()

        time.sleep(2)
        time.sleep(3)
        print("Create new patient")
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//b[normalize-space()='Create New Patient']")
            )
        )
        element_appoint.click()
        login.implicitly_wait(3)
        time.sleep(2)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='first_name'])[1]"))
        ).send_keys(first_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='last_name'])[1]"))
        ).send_keys(last_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='email_id'])[1]"))
        ).send_keys(email)

        time.sleep(1)   
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[1]"))
        ).send_keys(phonenumber)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[normalize-space()='Male'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)   
        # Click on the "2025" button
        login.find_element(By.XPATH, "//button[normalize-space()='2025']").click()

        # Wait until the backward arrow is clickable before clicking it
        backward_arrow = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'p-ripple') and contains(@class, 'p-element') and contains(@class, 'p-datepicker-prev') and contains(@class, 'p-link') and contains(@class, 'ng-star-inserted')]")
            )
        )

        # Clicking backward arrows 4 times to navigate to the correct year
        for _ in range(4):
            backward_arrow.click()
        time.sleep(2)
        # Generate Date of Birth (DOB)
        [year, month, day] = Generate_dob()
        print(f"Year: {year}, Month: {month}, Day: {day}")
        time.sleep(2)
        # Select Year
        year_xpath = f"//span[normalize-space()='{year}']"
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, year_xpath))
        ).click()
        time.sleep(2)
        # Select Month
        month_xpath = f"//span[normalize-space()='{month}']"
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, month_xpath))
        ).click()

        time.sleep(2)
        # Select Day
        day = str(int(day))  # Ensuring day is in integer form
        day_xpath = f"//span[normalize-space()='{day}']"
        select_day = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, day_xpath))
        )
        select_day.click()

        print(f"Selected Date of Birth: {day}-{month}-{year}")
        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Save'])[1]"))
        ).click()

        try:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        except:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)
        
        time.sleep(5)
       
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm']"))
        ).click()

        time.sleep(3)
        while True:
            try:
                
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                if next_button.is_enabled():
                   
                    login.execute_script("arguments[0].click();", next_button)
                  
                    break

            except Exception as e:
                
                break

        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(3)
        View_Detail_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(), 'View Details')]")
            )
        )
        View_Detail_button.click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Convert to IP'])[1]"))
        ).click()

        time.sleep(2)

        admission_dropdown = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        )
        admission_dropdown.click()

        # Wait and fetch all options in the dropdown
        dropdown_options = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@role='listbox' and contains(@class, 'p-dropdown-items')]/p-dropdownitem/li")
            )
        )

        # Randomly choose and click one option
        random_option = random.choice(dropdown_options)
        random_option_text = random_option.text.strip()
        random_option.click()

        print(f"✅ Randomly selected admission type: {random_option_text}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        today_element = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
        (By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")
                )
        )          

        # Click using JavaScript in case normal click doesn't work
        login.execute_script("arguments[0].click();", today_element)

        print("Clicked today's date:", today_element.text)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]"))
        ).click()

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=3)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")
            )
        ).click()                                                                                                                                            
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"))
        ).click()

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Cancel'])[1]")

        print("Admission cancelled")
        time.sleep(2)
        # ✅ Verify redirection to patient detail page
        try:
            # Wait until a known element from Patient Detail page appears
            patient_detail_header = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "(//span[normalize-space()='Appointment'])[1]")
                )
            )
            
            assert patient_detail_header.is_displayed(), "Appointment header not visible"
            print("✅ Redirected to Patient Detail page successfully.")

            # Optionally log in Allure
            allure.attach(
                login.get_screenshot_as_png(),
                name="Redirected_to_Appointment_Detail_Page",
                attachment_type=AttachmentType.PNG,
            )

        except Exception:
            # Capture failure
            allure.attach(
                login.get_screenshot_as_png(),
                name="Patient_Detail_Page_Not_Visible",
                attachment_type=AttachmentType.PNG,
            )
            raise AssertionError("❌ Did not redirect to Patient Detail page after cancelling admission.")

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Take admission from OP patient and cancel it after the admissions")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)]) 
def  test_take_admission_from_op_and_cancel_after_conversion(login):

    wait = WebDriverWait(login, 20)
    try: 
        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='dashboard-card-image'])[6]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(., 'Create Room')]"))  
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        drop_downlist = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal Room'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", drop_downlist)
        time.sleep(1)   
        drop_downlist.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Private Room'])[1]"))
        ).click()

        room_name = get_next_room_name()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Room Name'])[1]")
            )
        ).send_keys(room_name)

        print(f"🏨 Room created: {room_name}")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[5]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Room'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()
    
        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='Room Details'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()
        
        time.sleep(1)
        bed_type = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_type)
        time.sleep(1)
        bed_type.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Observation Beds'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        bed_price = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Manual Hospital Bed'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_price)
        time.sleep(1)
        bed_price.click()

        bed_name  = f'Bed{room_name}'
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Bed Name'])[1]"))
        ).send_keys(bed_name)   

        time.sleep(1)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()   

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//img)[3]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Appointment'])[1]"))
        ).click()

        time.sleep(2)
        time.sleep(3)
        print("Create new patient")
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//b[normalize-space()='Create New Patient']")
            )
        )
        element_appoint.click()
        login.implicitly_wait(3)
        time.sleep(2)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='first_name'])[1]"))
        ).send_keys(first_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='last_name'])[1]"))
        ).send_keys(last_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='email_id'])[1]"))
        ).send_keys(email)

        time.sleep(1)   
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[1]"))
        ).send_keys(phonenumber)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[normalize-space()='Male'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)   
        # Click on the "2025" button
        login.find_element(By.XPATH, "//button[normalize-space()='2025']").click()

        # Wait until the backward arrow is clickable before clicking it
        backward_arrow = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'p-ripple') and contains(@class, 'p-element') and contains(@class, 'p-datepicker-prev') and contains(@class, 'p-link') and contains(@class, 'ng-star-inserted')]")
            )
        )

        # Clicking backward arrows 4 times to navigate to the correct year
        for _ in range(4):
            backward_arrow.click()
        time.sleep(2)
        # Generate Date of Birth (DOB)
        [year, month, day] = Generate_dob()
        print(f"Year: {year}, Month: {month}, Day: {day}")
        time.sleep(2)
        # Select Year
        year_xpath = f"//span[normalize-space()='{year}']"
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, year_xpath))
        ).click()
        time.sleep(2)
        # Select Month
        month_xpath = f"//span[normalize-space()='{month}']"
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, month_xpath))
        ).click()

        time.sleep(2)
        # Select Day
        day = str(int(day))  # Ensuring day is in integer form
        day_xpath = f"//span[normalize-space()='{day}' and not(contains(@class, 'p-disabled'))]"

        # Wait until the day becomes clickable
        select_day = WebDriverWait(login, 15).until(
            EC.element_to_be_clickable((By.XPATH, day_xpath))
        )

        # Scroll into view and click using JS to avoid overlay interception
        login.execute_script("arguments[0].scrollIntoView(true);", select_day)
        login.execute_script("arguments[0].click();", select_day)

        print(f"✅ Selected Date of Birth: {day}-{month}-{year}")
        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Save'])[1]"))
        ).click()

        msg = get_snack_bar_message(login)
        print("Snack Bar MEssage :", msg)
        
        time.sleep(5)
       
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm']"))
        ).click()

        time.sleep(3)
        while True:
            try:
                
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                if next_button.is_enabled():
                   
                    login.execute_script("arguments[0].click();", next_button)
                  
                    break

            except Exception as e:
                
                break

        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(3)
        View_Detail_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(), 'View Details')]")
            )
        )
        View_Detail_button.click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Convert to IP'])[1]"))
        ).click()

        time.sleep(2)

        admission_dropdown = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        )
        admission_dropdown.click()

        # Wait and fetch all options in the dropdown
        dropdown_options = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@role='listbox' and contains(@class, 'p-dropdown-items')]/p-dropdownitem/li")
            )
        )

        # Randomly choose and click one option
        random_option = random.choice(dropdown_options)
        random_option_text = random_option.text.strip()
        random_option.click()

        print(f"✅ Randomly selected admission type: {random_option_text}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        today_element = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
        (By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")
                )
        )          

        # Click using JavaScript in case normal click doesn't work
        login.execute_script("arguments[0].click();", today_element)

        print("Clicked today's date:", today_element.text)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]"))
        ).click()

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=3)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")
            )
        ).click()                                                                                                                                            
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"))
        ).click()

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Admit Now'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[normalize-space()='Discharge'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[contains(text(),'Use Template')])[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[normalize-space()='Use template'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Yes'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(2)
        scroll_to_window(login)

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Discharge'])[1]")
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Yes'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Checkout'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//*[@type='button'][normalize-space()='Checkout'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Yes'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//div[contains(text(),'Invoices')])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-plus'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Generate'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Generate Invoice'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Settle Invoice'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Confirm & Settle Invoice'])[1]")

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Checkout'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//*[@type='button'][normalize-space()='Checkout'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Yes'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(2)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("AFter IP Reservation cancel the reservation")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Reservations_cancel(login):

    wait = WebDriverWait(login, 20)
    try:
        time.sleep(5)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='dashboard-card-image'])[6]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1] "))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        drop_downlist = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal Room'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", drop_downlist)
        time.sleep(1)   
        drop_downlist.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Private Room'])[1]"))
        ).click()

        room_name = get_next_room_name()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Room Name'])[1]")
            )
        ).send_keys(room_name)

        print(f"🏨 Room created: {room_name}")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[5]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Room'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()
    
        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='Room Details'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Yes'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()
        
        time.sleep(1)
        bed_type = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_type)
        time.sleep(1)
        bed_type.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Observation Beds'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        bed_price = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Manual Hospital Bed'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_price)
        time.sleep(1)
        bed_price.click()

        bed_name  = f'Bed{room_name}'
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Bed Name'])[1]"))
        ).send_keys(bed_name)   

        time.sleep(1)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()   

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(5)  
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'New Admission')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[1]"))
        ).click()

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter First Name'])[1]"))
        ).send_keys(first_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Last Name'])[1]"))
        ).send_keys(last_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Email Id'])[1]"))
        ).send_keys(email)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[1]"))
        ).send_keys(phonenumber)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Male'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save & Next'])[1]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[normalize-space()='Reserve'])[1]"))
        ).click()

        time.sleep(2)
        admission_dropdown = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        )
        admission_dropdown.click()

        # Wait and fetch all options in the dropdown
        dropdown_options = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@role='listbox' and contains(@class, 'p-dropdown-items')]/p-dropdownitem/li")
            )
        )

        # Randomly choose and click one option
        random_option = random.choice(dropdown_options)
        random_option_text = random_option.text.strip()
        random_option.click()

        print(f"✅ Randomly selected admission type: {random_option_text}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        time.sleep(2)

        today_element = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
        (By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")
                )
        )          

        # Click using JavaScript in case normal click doesn't work
        login.execute_script("arguments[0].click();", today_element)

        print("Clicked today's date:", today_element.text)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]"))
        ).click()

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=3)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")
            )
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"))
        ).click()

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()
        
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Reserve Now'])[1]"))
        ).click()

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)

        # Locate the table by class
        table = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//table[contains(@class,'p-datatable-table')]")
            )
        )

        # Assuming you want the first row (recently reserved)
        first_row = table.find_element(By.XPATH, ".//tbody/tr[1]")

        # Get Reg.No from first column
        patient_reg_no = first_row.find_element(By.XPATH, ".//td[1]").text.strip()
        print(f"✅ Reserved patient Reg.No: {patient_reg_no}")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//img[@src='assets/images/membrship/dashboard-actions/icon.png'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Cancel'])[1]")

        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, "//textarea[@pinputtextarea]", "Reservation cancelled")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='OK'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Yes'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Cancelled'])[1]")

        time.sleep(3)
        # XPath to all rows inside the admissions table body
        tbody_rows_xpath = "//table[contains(@class,'p-datatable-table')]//tbody/tr"

        # Wait until at least one row is visible
        rows = WebDriverWait(login, 15).until(
            EC.visibility_of_all_elements_located((By.XPATH, tbody_rows_xpath))
        )

        print(f"✅ Found {len(rows)} rows in the admissions table body.")

        # Loop through rows to find your patient Reg.No
        patient_reg_no = "Seva314MP"  # example
        cancellation_verified = False

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >= 9:
                reg_no = cells[1].text.strip()
                cancel_date = cells[8].text.strip()
                print(f"Reg.No: {reg_no}, Cancellation Date: {cancel_date}")

                if reg_no == patient_reg_no:
                    assert cancel_date != "-", f"❌ Admission not cancelled for {reg_no}"
                    print(f"✅ Admission cancelled successfully for {reg_no}. Date: {cancel_date}")
                    cancellation_verified = True
                    break

        assert cancellation_verified, "❌ Cancelled admission record not found in the table"

        time.sleep(5)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
# <<<  << << << <<  RX Push  >> >> >> >>> >>>

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Create the RX Push and Complete Order")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_6(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img[@src='./assets/images/menu/settings.png'])[1]"))
        ).click()

        time.sleep(2)
        POS_setting = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='POS Ordering'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", POS_setting)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p[normalize-space()='RX Push Management System'])[1]"))
        ).click()

        time.sleep(2)
        # Wait for the toggle to be present
        wait = WebDriverWait(login, 10)
        toggle_button = wait.until(EC.presence_of_element_located((By.ID, "mat-mdc-slide-toggle-1-button")))

        # Check the value of aria-checked to determine toggle state
        is_checked = toggle_button.get_attribute("aria-checked")

        if is_checked == "false":
            print("RX Push is disabled. Enabling it now.")
            toggle_button.click()
            print("RX Push is already enabled. No action needed.")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[16]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[15]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Medical Records'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[normalize-space()='Prescription'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Krishna JP'])[1]")

        time.sleep(2)
        
        # List of medicines to enter
        medicines = ["Item01", "Item02", "Item03"]
        frequencies = ["TID (1-1-1)", "0-1-0", "QID (1-1-1-1)"] 
        qty = ["15", "5", "20"]
        dosages = ["1 tablet", "5 ml", "2 capsules"]

        for i, med in enumerate(medicines):
            # Step 1: Click "+ Add Medicine"
            add_btn = login.find_element(By.XPATH, "//button[contains(text(), '+ Add Medicine')]")
            add_btn.click()
            time.sleep(1)

            # Step 2: Get the last row
            rows = login.find_elements(By.XPATH, "//tbody[@class='p-element p-datatable-tbody']/tr")
            row = rows[-1]

            # Step 3: Fill medicine name
            med_input = row.find_element(By.XPATH, ".//td[2]//input[@type='text']")
            med_input.clear()
            med_input.send_keys(med)
            time.sleep(2)
            med_input.send_keys(Keys.ARROW_DOWN)
            med_input.send_keys(Keys.ENTER)

            # Step 4: Duration
            duration_input = row.find_element(By.XPATH, ".//td[3]//input[@type='number']")
            duration_input.clear()
            duration_input.send_keys("5")

            # Step 5: Frequency
            freq_dropdown = row.find_element(By.XPATH, ".//td[4]//div[contains(@class, 'p-dropdown')]")
            freq_dropdown.click()
            time.sleep(1)

            freq_value = frequencies[i] if i < len(frequencies) else frequencies[0]
            freq_options = login.find_elements(By.XPATH, "//ul[@role='listbox']//li[@role='option']")

            selected = False
            for option in freq_options:
                option_text = option.get_attribute("aria-label")
                if option_text.strip() == freq_value:
                    option.click()
                    selected = True
                    print(f"✅ Selected frequency: {freq_value}")
                    break

            if not selected:
                print(f"❌ Frequency '{freq_value}' not found in dropdown.")

            # Step 6: Dosage (td[5])
            dosage_input = row.find_element(By.XPATH, ".//td[5]//input[@type='text']")
            dosage_value = dosages[i] if i < len(dosages) else "1 tablet"
            dosage_input.clear()
            dosage_input.send_keys(dosage_value)

            time.sleep(2)

            # Step 7: Assert Auto-Generated Quantity (td[6])
            qty_input = row.find_element(By.XPATH, ".//td[6]//input[@type='number']")
            actual_qty = qty_input.get_attribute("value")
            expected_qty = qty[i]
            print(f"🔎 Auto-generated quantity for {med}: Expected {expected_qty}, Got {actual_qty}")
            assert actual_qty == expected_qty, f"❌ Quantity mismatch for {med}: Expected {expected_qty}, Got {actual_qty}"
            print(f"✅ Quantity matched for {med}")

            # Step 8: Notes / Instructions (td[7])
            editable_td = row.find_element(By.XPATH, ".//td[7]")
            editable_td.click()
            time.sleep(2)
            textarea = editable_td.find_element(By.XPATH, "//input[@role='searchbox']")
            food_text = random.choice(["after food", "before food"])
            textarea.send_keys(food_text)

        # Add general notes
        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@aria-label='Rich Text Editor. Editing area: main'])[1]"))
        ).send_keys("200-word limit restricts essays to a concise length, typically resulting in 3-4 paragraphs. Despite the brevity, the essay should still maintain a clear structure with an introduction, body, and conclusion. This format helps organize thoughts and convey ideas effectively within the word count constraint")

        # Submit
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create Prescription'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//img[@alt='dropdown'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space(.)='Push RX'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//img[@src='assets/images/rx-order/dashboard-actions/storeIcon.svg'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Push'])[1]"))
        ).click()

        toast_detail = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_detail.text
        print("toast_Message:", message)    

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//button[normalize-space()='Push RX'])[1]"))
        # ).click()

        # time.sleep(1)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//img[@src='assets/images/rx-order/dashboard-actions/storeIcon.svg'])[1]"))
        # ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//button[normalize-space()='Push'])[1]"))
        # ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[5]"))
        ).click()

        time.sleep(3)

        RX_request = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Rx Requests'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", RX_request) 
        
        time.sleep(2)
        RX_request.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Confirm Order'])[1]"))
        ).click()

        toast_detail = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_detail.text
        print("toast_Message:", message) 

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Create Invoice'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='View Invoice'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Pay by Cash'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Pay'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        # toast_detail = WebDriverWait(login, 10).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        # )
        # message = toast_detail.text
        # print("toast_Message:", message)

        time.sleep(2)
        BA_Button = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", BA_Button)
        time.sleep(2)
        BA_Button.click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Complete Order'])[1]"))    
        ).click()

        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Retained Bed when transfer")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def  test_IP_Management_7(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[16]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Transfer Bed')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='First Floor B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal ICU'])[1]"))
        ).click()

        time.sleep(2)          

        # Find all bed cards
        bed_cards = login.find_elements(By.XPATH, "//div[contains(@class, 'bed-card')]")

        # Randomly choose one bed
        random_bed = random.choice(bed_cards)

        # Click the "Select Bed" button inside that bed-card
        select_button = random_bed.find_element(By.XPATH, ".//button[contains(text(), 'Select Bed')]")
        select_button.click()

        # (Optional) Print which bed was selected
        bed_name = random_bed.find_element(By.XPATH, ".//span[contains(@class, 'bed-title')]").text
        print(f"Selected Bed: {bed_name}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        today_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        today_date.click()
        print("Clicked today's date:", today_date.text)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save & Transfer'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)    

        time.sleep(3)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]"))
        # ).click()

        # time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Transfer Bed')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Select Bed'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        today_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        today_date.click()
        print("Clicked today's date:", today_date.text)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[normalize-space()='No'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save & Transfer'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@allure.severity(allure.severity_level.CRITICAL) 
@allure.title("Test Case:  Not Retained Bed when transfer")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_8(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[16]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Transfer Bed')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Building'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block A'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Select Bed Type'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Fowler Beds'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[contains(text(),'Select Bed')])[1]"))
        ).click()

        time.sleep(2)

        # ✅ Assert that it changed to 'Unselect Bed'
        unselect_bed_button = wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Unselect Bed'])[1]")
        ))
        assert unselect_bed_button.is_displayed(), "'Unselect Bed' button did not appear as expected"
        print("✅ 'Select Bed' successfully changed to 'Unselect Bed'.")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        today_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        today_date.click()
        print("Clicked today's date:", today_date.text)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//label[normalize-space()='No'])[1]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//textarea[@placeholder='Enter Notes'])[1]"))
        ).send_keys("Note for the Transfering Bed")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save & Transfer'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)    

        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Create 2 unpaid invoices, then create a master invoice and pay it. After that, discharge and check out.")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_9(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='dashboard-card-image'])[6]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1]"))  
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        drop_downlist = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal Room'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", drop_downlist)
        time.sleep(1)   
        drop_downlist.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Private Room'])[1]"))
        ).click()

        room_name = get_next_room_name()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Room Name'])[1]")
            )
        ).send_keys(room_name)

        print(f"🏨 Room created: {room_name}")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[5]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Room'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()
    
        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='Room Details'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Bed Type'])[1]"))
        ).click()
        
        time.sleep(2)
        bed_type = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_type)
        time.sleep(1)
        bed_type.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Bed Category'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Observation Beds'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Bed Pricing'])[1]"))
        ).click()

        time.sleep(1)
        bed_price = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Manual Hospital Bed'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_price)
        time.sleep(1)
        bed_price.click()

        bed_name  = f'Bed{room_name}'
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Bed Name'])[1]"))
        ).send_keys(bed_name)   

        time.sleep(1)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()   

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(5)  
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'New Admission')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[1]"))
        ).click()

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter First Name'])[1]"))
        ).send_keys(first_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Last Name'])[1]"))
        ).send_keys(last_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Email Id'])[1]"))
        ).send_keys(email)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[1]"))
        ).send_keys(phonenumber)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Male'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save & Next'])[1]"))
        ).click()

        time.sleep(2)
        admission_dropdown = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        )
        admission_dropdown.click()

        # Wait and fetch all options in the dropdown
        dropdown_options = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@role='listbox' and contains(@class, 'p-dropdown-items')]/p-dropdownitem/li")
            )
        )

        # Randomly choose and click one option
        random_option = random.choice(dropdown_options)
        random_option_text = random_option.text.strip()
        random_option.click()

        print(f"✅ Randomly selected admission type: {random_option_text}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        time.sleep(2)

        today_element = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
        (By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")
                )
        )          

        # Click using JavaScript in case normal click doesn't work
        login.execute_script("arguments[0].click();", today_element)

        print("Clicked today's date:", today_element.text)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]"))
        ).click()

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=3)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")
            )
        ).click()                                                                                                                                            
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"))
        ).click()

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name}')]"
        wait.until(   
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[6]"))
        # ).click()

        # time.sleep(2)   
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[normalize-space()='Normal'])[1]"))
        # ).click()

        # time.sleep(2)
        # room_xpath1 = f"//div[contains(text(),'Room : {room_name}')]"
        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, room_xpath1))
        # ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space(.)='Admit Now'])[1]")
            )
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(5)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click() 

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Medical Record')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='+ Add New Visit'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()   

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Visit'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)    
        
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Services'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-plus'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Search Service'])[1]"))
        ).send_keys("Doc")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//li[@role='option'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        # time.sleep(2)
        # wait_and_click(login, By.XPATH, "//button[contains(@class,'p-datepicker-trigger')]//span[contains(@class,'pi-clock')]")
        # time.sleep(1)
        # # Locate the minute up arrow
        # minute_up_button = login.find_element(By.XPATH, "//div[contains(@class,'p-minute-picker')]//button[1]")

        # # Click it 10 times
        # for _ in range(3):
        #     minute_up_button.click()
        #     time.sleep(0.5)

        # time.sleep(2)
        # wait_and_click(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]", "2")
      
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Service'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Medical Records'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Vital Signs'])[1]"))
        ).click()

        # Generate vitals
        temp = generate_temperature_f()
        pulse = generate_pulse_rate()
        resp = generate_respiration_rate()
        systolic, diastolic = generate_blood_pressure()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Temperature in °F , Max : 200'])[1]"))
        ).send_keys(str(temp))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Pulse Rate , Max : 999'])[1]"))
        ).send_keys(str(pulse))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Respiration , Max : 90'])[1]"))
        ).send_keys(str(resp))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Systolic , Max : 500'])[1]"))
        ).send_keys(str(systolic))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Diastolic , Max : 500'])[1]"))
        ).send_keys(str(diastolic))

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save'])[1]"))
            
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Create Invoice')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Generate'])[1]"))
        ).click()

        time.sleep(1)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Generate Invoice'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Overview')])[1]"))
        # ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Medical Record')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='+ Add New Visit'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()   

        # time.sleep(1)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))
        # ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Visit'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(5)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Services'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-plus'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Search Service'])[1]"))
        ).send_keys("Doc")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//li[@role='option'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        # time.sleep(2)
        # wait_and_click(login, By.XPATH, "//button[contains(@class,'p-datepicker-trigger')]//span[contains(@class,'pi-clock')]")
        # time.sleep(1)
        # # Locate the minute up arrow
        # minute_up_button = login.find_element(By.XPATH, "//div[contains(@class,'p-minute-picker')]//button[1]")

        # # Click it 10 times
        # for _ in range(3):
        #     minute_up_button.click()
        #     time.sleep(0.5)

        # time.sleep(2)
        # wait_and_click(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]", "2")
      
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='p-checkbox-box'])[2]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Service'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Create Invoice')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Generate'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Generate Invoice'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Invoices')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-plus'])[1]"))
        ).click()

        time.sleep(2)
        wait.until( 
            EC.presence_of_element_located((By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//input[contains(@class, 'mdc-checkbox__native-control')])[2]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//input[contains(@class, 'mdc-checkbox__native-control')])[3]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(normalize-space(.), 'Link & Generate Master Invoice')]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Pay by Cash'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Pay'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[1]"))
        ).click()

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//div[contains(text(),'Overview')])[1]")

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='my-1 font-small fw-bold text-capitalize ng-star-inserted'][normalize-space()='Discharge'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Use Template'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Use template'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        discharge_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space(.)='Discharge'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", discharge_button)

        time.sleep(2)
        discharge_button.click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        # Wait for the discharge status to appear
        discharge_status_xpath = "//div[contains(@class, 'status-discharged') and normalize-space()='Discharged']"
        WebDriverWait(login, 10).until(EC.visibility_of_element_located((By.XPATH, discharge_status_xpath)))

        # Assert that the "Discharged" status is displayed
        discharge_status_element = login.find_element(By.XPATH, discharge_status_xpath)
        assert discharge_status_element.is_displayed(), "Discharge status is not visible after discharge."

        print("✅ Discharge status is visible after discharge.")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[contains(text(),'Create Invoice')])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Generate'])[1]")
        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Generate Invoice'])[1]")

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Pay by Cash'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Pay'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()                   

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Checkout'])[1]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@type='button'][normalize-space()='Checkout'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)
 
        time.sleep(3)
        # XPath for "Checked Out" status
        checkout_xpath = "//div[contains(@class, 'status-checkout') and normalize-space()='Checked Out']"

        # Wait for the element to be visible
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, checkout_xpath))
        )

        # Assert the element is displayed
        checkout_status = login.find_element(By.XPATH, checkout_xpath)
        assert checkout_status.is_displayed(), "'Checked Out' status is not visible."

        print("✅ Checked Out status is visible after checkout.")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Checked Out'])[1]"))
        ).click()

        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case:Create two invoices, one paid and one unpaid, then group them into a master invoice. Make a payment for the unpaid invoice, then proceed to discharge and check out.")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def  test_IP_Management_10(login):
    
    try:

        time.sleep(3)
        wait = WebDriverWait(login, 30)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='dashboard-card-image'])[6]"))
        ).click()

        time.sleep(2)
        wait.until( 
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1]"))  
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space(.)='Second Floor B'])[1]"))
        ).click()
 
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        drop_downlist = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal Room'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", drop_downlist)
        time.sleep(1)   
        drop_downlist.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Private Room'])[1]"))
        ).click()

        room_name = get_next_room_name()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Room Name'])[1]")
            )
        ).send_keys(room_name)

        print(f"🏨 Room created: {room_name}")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[5]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Room'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()
    
        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='Room Details'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Bed Type'])[1]"))
        ).click()
        
        time.sleep(2)
        bed_type = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_type)
        time.sleep(1)
        bed_type.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Bed Category'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Observation Beds'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Bed Pricing'])[1]"))
        ).click()

        time.sleep(1)
        bed_price = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Manual Hospital Bed'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_price)
        time.sleep(1)
        bed_price.click()

        bed_name  = f'Bed{room_name}'
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Bed Name'])[1]"))
        ).send_keys(bed_name)   

        time.sleep(1)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()   

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(5)  
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'New Admission')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[1]"))
        ).click()

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter First Name'])[1]"))
        ).send_keys(first_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Last Name'])[1]"))
        ).send_keys(last_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Email Id'])[1]"))
        ).send_keys(email)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[1]"))
        ).send_keys(phonenumber)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Male'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save & Next'])[1]"))
        ).click()

        time.sleep(2)
        admission_dropdown = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        )
        admission_dropdown.click()

        # Wait and fetch all options in the dropdown
        dropdown_options = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@role='listbox' and contains(@class, 'p-dropdown-items')]/p-dropdownitem/li")
            )
        )

        # Randomly choose and click one option
        random_option = random.choice(dropdown_options)
        random_option_text = random_option.text.strip()
        random_option.click()

        print(f"✅ Randomly selected admission type: {random_option_text}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        time.sleep(2)

        today_element = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
        (By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")
                )
        )          

        # Click using JavaScript in case normal click doesn't work
        login.execute_script("arguments[0].click();", today_element)

        print("Clicked today's date:", today_element.text)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]"))
        ).click()

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=3)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")
            )
        ).click()                                                                                                                                            
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"))
        ).click()

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space(.)='Admit Now'])[1]")
            )
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click() 

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Medical Record')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='+ Add New Visit'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()   

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Visit'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)    
        
        time.sleep(5)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Services'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-plus'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Search Service'])[1]"))
        ).send_keys("Doc")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//li[@role='option'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        # time.sleep(2)
        # wait_and_click(login, By.XPATH, "//button[contains(@class,'p-datepicker-trigger')]//span[contains(@class,'pi-clock')]")
        # time.sleep(1)
        # # Locate the minute up arrow
        # minute_up_button = login.find_element(By.XPATH, "//div[contains(@class,'p-minute-picker')]//button[1]")

        # # Click it 10 times
        # for _ in range(2):
        #     minute_up_button.click()
        #     time.sleep(0.5)

        # time.sleep(2)
        # wait_and_click(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]", "2")
      
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Service'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Medical Records'])[1]"))

        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Vital Signs'])[1]"))
        ).click()

        # Generate vitals
        temp = generate_temperature_f()
        pulse = generate_pulse_rate()
        resp = generate_respiration_rate()
        systolic, diastolic = generate_blood_pressure()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Temperature in °F , Max : 200'])[1]"))
        ).send_keys(str(temp))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Pulse Rate , Max : 999'])[1]"))
        ).send_keys(str(pulse))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Respiration , Max : 90'])[1]"))
        ).send_keys(str(resp))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Systolic , Max : 500'])[1]"))
        ).send_keys(str(systolic))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Diastolic , Max : 500'])[1]"))
        ).send_keys(str(diastolic))

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save'])[1]"))
            
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Create Invoice')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Generate'])[1]"))
        ).click()

        time.sleep(1)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Generate Invoice'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Pay by Cash'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Pay'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        try:
            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        except:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Overview')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Medical Record')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='+ Add New Visit'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()   

        # time.sleep(1)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))
        # ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Visit'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(5)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Services'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-plus'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Search Service'])[1]"))
        ).send_keys("Doc")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//li[@role='option'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        # time.sleep(2)
        # wait_and_click(login, By.XPATH, "//button[contains(@class,'p-datepicker-trigger')]//span[contains(@class,'pi-clock')]")
        # time.sleep(1)
        # # Locate the minute up arrow
        # minute_up_button = login.find_element(By.XPATH, "//div[contains(@class,'p-minute-picker')]//button[1]")

        # # Click it 10 times
        # for _ in range(2):
        #     minute_up_button.click()
        #     time.sleep(0.5)

        # time.sleep(2)
        # wait_and_click(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]", "2")
      
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='p-checkbox-box'])[2]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")
        
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Service'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Create Invoice')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Generate'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Generate Invoice'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Invoices')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-plus'])[1]"))
        ).click()

        time.sleep(2)
        wait.until( 
            EC.presence_of_element_located((By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//input[contains(@class, 'mdc-checkbox__native-control')])[2]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//input[contains(@class, 'mdc-checkbox__native-control')])[3]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(normalize-space(.), 'Link & Generate Master Invoice')]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Overview')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='my-1 font-small fw-bold text-capitalize ng-star-inserted'][normalize-space()='Discharge'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Use Template'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Use template'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        discharge_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space(.)='Discharge'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", discharge_button)

        time.sleep(2)
        discharge_button.click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        # Wait for the discharge status to appear
        discharge_status_xpath = "//div[contains(@class, 'status-discharged') and normalize-space()='Discharged']"
        WebDriverWait(login, 10).until(EC.visibility_of_element_located((By.XPATH, discharge_status_xpath)))

        # Assert that the "Discharged" status is displayed
        discharge_status_element = login.find_element(By.XPATH, discharge_status_xpath)
        assert discharge_status_element.is_displayed(), "Discharge status is not visible after discharge."

        print("✅ Discharge status is visible after discharge.")

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='fw-bold ng-star-inserted'][normalize-space()='Invoices'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-plus'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[1]"))
        ).click()

        time.sleep(2)  
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space(.)='Generate'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space(.)='Generate Invoice'])[1]"))
        ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        # ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'View')])[2]"))
        # ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='+ Link Invoice'])[1]"))
        # ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-checkbox']//input[@type='checkbox'])[1]"))
        # ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[1]"))
        # ).click()

        # # # time.sleep(2)

        # # # wait.until(
        # # #     EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'View')])[1]"))
        # # # ).click()

        # # time.sleep(2)
        # # wait.until(
        # #     EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        # # ).click()

        # time.sleep(2)
        # yes_button = wait.until(
        #     EC.presence_of_element_located((By.XPATH, "//app-confirm-box//button[normalize-space(text())='Yes']"))
        # )
        # login.execute_script("arguments[0].click();", yes_button)
        
        # toast_message = WebDriverWait(login, 10).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        # message = toast_message.text
        # print("Toast Message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Pay by Others'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Pay'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space(.)='Yes'])[1]"))
        ).click()

        try:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        except:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//div[@class='fw-bold ng-star-inserted'][normalize-space()='Invoices'])[1]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='p-button-label'][normalize-space()='View'])[2]")
        
        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]")

        time.sleep(1)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Pay by Cash'])[1]")  

        time.sleep(1)
        wait_and_click(login, By.XPATH, "(//button[normalize-space()='Pay'])[1]")   

        time.sleep(1)
        wait_and_click(login, By.XPATH, "(//button[normalize-space()='Yes'])[1]")
        
        try:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        except:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        time.sleep(3)
        wait_and_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Overview')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Checkout'])[1]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@type='button'][normalize-space()='Checkout'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Snack bar message:", message)
        
        time.sleep(3)

        wait_and_click(login, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]")
        time.sleep(2)

        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        time.sleep(2)

        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Checked Out'])[1]")
        # XPath for "Checked Out" status
        checkout_xpath = "//div[contains(@class, 'status-checkout') and normalize-space()='Checked Out']"

        # Wait for the element to be visible
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, checkout_xpath))
        )

        # Assert the element is displayed
        checkout_status = login.find_element(By.XPATH, checkout_xpath)
        assert checkout_status.is_displayed(), "'Checked Out' status is not visible."

        print("✅ Checked Out status is visible after checkout.")

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        # ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        # ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Checked Out'])[1]"))
        # ).click()

        time.sleep(5)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case:After Discharge Create 2 Invoice with unpaid and paid and make it master invoice, make payment to the unpaid invoice and check out")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_11(login):

    try:

        time.sleep(3)  

        wait = WebDriverWait(login, 30)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='dashboard-card-image'])[6]"))
        ).click()

        time.sleep(2)
        wait.until( 
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component'])[1] "))  
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space(.)='Second Floor B'])[1]"))
        ).click()
 
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        drop_downlist = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal Room'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", drop_downlist)
        time.sleep(1)   
        drop_downlist.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Private Room'])[1]"))
        ).click()

        room_name = get_next_room_name()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Room Name'])[1]")
            )
        ).send_keys(room_name)

        print(f"🏨 Room created: {room_name}")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[5]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Room'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()
    
        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='Room Details'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Bed Type'])[1]"))
        ).click()
        
        time.sleep(2)
        bed_type = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_type)
        time.sleep(1)
        bed_type.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Bed Category'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Observation Beds'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Bed Pricing'])[1]"))
        ).click()

        time.sleep(1)
        bed_price = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Manual Hospital Bed'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_price)
        time.sleep(1)
        bed_price.click()

        bed_name  = f'Bed{room_name}'
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Bed Name'])[1]"))
        ).send_keys(bed_name)   

        time.sleep(1)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()   

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(5)  
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'New Admission')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[1]"))
        ).click()

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter First Name'])[1]"))
        ).send_keys(first_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Last Name'])[1]"))
        ).send_keys(last_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Email Id'])[1]"))
        ).send_keys(email)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[1]"))
        ).send_keys(phonenumber)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Male'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save & Next'])[1]"))
        ).click()

        time.sleep(2)
        admission_dropdown = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        )
        admission_dropdown.click()

        # Wait and fetch all options in the dropdown
        dropdown_options = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@role='listbox' and contains(@class, 'p-dropdown-items')]/p-dropdownitem/li")
            )
        )

        # Randomly choose and click one option
        random_option = random.choice(dropdown_options)
        random_option_text = random_option.text.strip()
        random_option.click()

        print(f"✅ Randomly selected admission type: {random_option_text}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        time.sleep(2)

        today_element = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
        (By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")
                )
        )          

        # Click using JavaScript in case normal click doesn't work
        login.execute_script("arguments[0].click();", today_element)

        print("Clicked today's date:", today_element.text)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]"))
        ).click()

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=3)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")
            )
        ).click()                                                                                                                                            
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"))
        ).click()

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space(.)='Admit Now'])[1]")
            )
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click() 

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Medical Record')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='+ Add New Visit'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()   

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Visit'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)    
        
        time.sleep(5)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Services'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-plus'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Search Service'])[1]"))
        ).send_keys("Doc")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//li[@role='option'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        # time.sleep(2)
        # wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[3]")
        # time.sleep(1)
        # # Locate the minute up arrow
        # minute_up_button = login.find_element(By.XPATH, "//div[contains(@class,'p-minute-picker')]//button[1]")

        # # Click it 10 times
        # for _ in range(3):
        #     minute_up_button.click()
        #     time.sleep(0.5)

        # time.sleep(2)
        # wait_and_click(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]", "2")
      
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Service'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Medical Records'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Vital Signs'])[1]"))
        ).click()

        # Generate vitals
        temp = generate_temperature_f()
        pulse = generate_pulse_rate()
        resp = generate_respiration_rate()
        systolic, diastolic = generate_blood_pressure()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Temperature in °F , Max : 200'])[1]"))
        ).send_keys(str(temp))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Pulse Rate , Max : 999'])[1]"))
        ).send_keys(str(pulse))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Respiration , Max : 90'])[1]"))
        ).send_keys(str(resp))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Systolic , Max : 500'])[1]"))
        ).send_keys(str(systolic))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Diastolic , Max : 500'])[1]"))
        ).send_keys(str(diastolic))

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save'])[1]"))
            
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Create Invoice')])[1]"))
        # ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Generate'])[1]"))
        # ).click()

        # time.sleep(1)

        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Generate Invoice'])[1]"))
        # ).click()

        # toast_message = WebDriverWait(login, 10).until(
        # EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        # )
        # message = toast_message.text
        # print("Toast Message:", message)

        # time.sleep(3)
        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        # ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='my-1 font-small fw-bold text-capitalize ng-star-inserted'][normalize-space()='Discharge'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Use Template'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Use template'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        discharge_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space(.)='Discharge'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", discharge_button)

        time.sleep(2)
        discharge_button.click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        # Wait for the discharge status to appear
        discharge_status_xpath = "//div[contains(@class, 'status-discharged') and normalize-space()='Discharged']"
        WebDriverWait(login, 10).until(EC.visibility_of_element_located((By.XPATH, discharge_status_xpath)))

        # Assert that the "Discharged" status is displayed
        discharge_status_element = login.find_element(By.XPATH, discharge_status_xpath)
        assert discharge_status_element.is_displayed(), "Discharge status is not visible after discharge."

        print("✅ Discharge status is visible after discharge.")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Create Invoice')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Generate'])[1]"))
        ).click()

        time.sleep(1)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Generate Invoice'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Pay by Cash'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Pay'])[1]"))
        ).click()
        
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        try:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        except:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Checkout'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[@type='button'][normalize-space()='Checkout'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail")))    
        message = toast_message.text
        print("Toast Message:", message)    
        time.sleep(5)
    
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Create 2 unpaid invoices, then create a master invoice and try to edit the Invoive")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_master_invoice_edit(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='dashboard-card-image'])[6]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1]"))  
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        drop_downlist = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal Room'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", drop_downlist)
        time.sleep(1)   
        drop_downlist.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Private Room'])[1]"))
        ).click()

        room_name = get_next_room_name()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Room Name'])[1]")
            )
        ).send_keys(room_name)

        print(f"🏨 Room created: {room_name}")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[5]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Room'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()
    
        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='Room Details'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Bed Type'])[1]"))
        ).click()
        
        time.sleep(2)
        bed_type = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_type)
        time.sleep(1)
        bed_type.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Bed Category'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Observation Beds'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Bed Pricing'])[1]"))
        ).click()

        time.sleep(1)
        bed_price = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Manual Hospital Bed'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_price)
        time.sleep(1)
        bed_price.click()

        bed_name  = f'Bed{room_name}'
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Bed Name'])[1]"))
        ).send_keys(bed_name)   

        time.sleep(1)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()   

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        time.sleep(5)  
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'New Admission')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[1]"))
        ).click()

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter First Name'])[1]"))
        ).send_keys(first_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Last Name'])[1]"))
        ).send_keys(last_name)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Email Id'])[1]"))
        ).send_keys(email)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[1]"))
        ).send_keys(phonenumber)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Male'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save & Next'])[1]"))
        ).click()

        time.sleep(2)
        admission_dropdown = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        )
        admission_dropdown.click()

        # Wait and fetch all options in the dropdown
        dropdown_options = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@role='listbox' and contains(@class, 'p-dropdown-items')]/p-dropdownitem/li")
            )
        )

        # Randomly choose and click one option
        random_option = random.choice(dropdown_options)
        random_option_text = random_option.text.strip()
        random_option.click()

        print(f"✅ Randomly selected admission type: {random_option_text}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        time.sleep(2)

        today_element = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
        (By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")
                )
        )          

        # Click using JavaScript in case normal click doesn't work
        login.execute_script("arguments[0].click();", today_element)

        print("Clicked today's date:", today_element.text)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]"))
        ).click()

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=3)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")
            )
        ).click()                                                                                                                                            
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"))
        ).click()

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name}')]"
        wait.until(   
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[6]"))
        # ).click()

        # time.sleep(2)   
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[normalize-space()='Normal'])[1]"))
        # ).click()

        # time.sleep(2)
        # room_xpath1 = f"//div[contains(text(),'Room : {room_name}')]"
        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, room_xpath1))
        # ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space(.)='Admit Now'])[1]")
            )
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(5)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click() 

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Medical Record')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='+ Add New Visit'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()   

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Visit'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)    
        
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Services'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-plus'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Search Service'])[1]"))
        ).send_keys("Doc")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//li[@role='option'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        # time.sleep(2)
        # wait_and_click(login, By.XPATH, "//button[contains(@class,'p-datepicker-trigger')]//span[contains(@class,'pi-clock')]")
        # time.sleep(1)
        # # Locate the minute up arrow
        # minute_up_button = login.find_element(By.XPATH, "//div[contains(@class,'p-minute-picker')]//button[1]")

        # # Click it 10 times
        # for _ in range(3):
        #     minute_up_button.click()
        #     time.sleep(0.5)

        # time.sleep(2)
        # wait_and_click(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]", "2")
      
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Service'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Medical Records'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Vital Signs'])[1]"))
        ).click()

        # Generate vitals
        temp = generate_temperature_f()
        pulse = generate_pulse_rate()
        resp = generate_respiration_rate()
        systolic, diastolic = generate_blood_pressure()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Temperature in °F , Max : 200'])[1]"))
        ).send_keys(str(temp))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Pulse Rate , Max : 999'])[1]"))
        ).send_keys(str(pulse))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Respiration , Max : 90'])[1]"))
        ).send_keys(str(resp))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Systolic , Max : 500'])[1]"))
        ).send_keys(str(systolic))

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Diastolic , Max : 500'])[1]"))
        ).send_keys(str(diastolic))

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save'])[1]"))
            
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Create Invoice')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Generate'])[1]"))
        ).click()

        time.sleep(1)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Generate Invoice'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        # time.sleep(2)
        # wait.until(
        #     EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Overview')])[1]"))
        # ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Medical Record')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='+ Add New Visit'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()   

        # time.sleep(1)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"))
        # ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Visit'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(5)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Services'])[1]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='pi pi-plus'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Search Service'])[1]"))
        ).send_keys("Doc")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//li[@role='option'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))
        # Click on today's date
        today_element.click()
        print("Clicked today's date:", today_element.text)

        # time.sleep(2)
        # wait_and_click(login, By.XPATH, "//button[contains(@class,'p-datepicker-trigger')]//span[contains(@class,'pi-clock')]")
        # time.sleep(1)
        # # Locate the minute up arrow
        # minute_up_button = login.find_element(By.XPATH, "//div[contains(@class,'p-minute-picker')]//button[1]")

        # # Click it 10 times
        # for _ in range(3):
        #     minute_up_button.click()
        #     time.sleep(0.5)

        # time.sleep(2)
        # wait_and_click(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]", "2")
      
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='p-checkbox-box'])[2]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Service'])[1]"))
        ).click()

        message = get_toast_message(login)
        print("Toast message:", message)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Create Invoice')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Generate'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Generate Invoice'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Invoices')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//i[@class='pi pi-plus'])[1]"))
        ).click()

        time.sleep(2)
        wait.until( 
            EC.presence_of_element_located((By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//input[contains(@class, 'mdc-checkbox__native-control')])[2]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//input[contains(@class, 'mdc-checkbox__native-control')])[3]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(normalize-space(.), 'Link & Generate Master Invoice')]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create a Service")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_12(login):
    try:

        time.sleep(5)
        wait = WebDriverWait(login, 30)

        # Navigate to Services section
        wait.until(EC.presence_of_element_located((By.XPATH, "(//img)[4]"))).click()

        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Services')])[1]"))).click()

        # Click Create Service
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'create-item-button') and contains(text(), 'Create Service')]"))).click()

        # Click on the first group option (if needed)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='font-weight-bold grouping-heading float-left'])[1]"))).click()

        # Fill in Service Name
        service_name = "Service" + str(uuid.uuid4())[:4]
        wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='service_name'])[1]"))).send_keys(service_name)

        # Toggle first switch
        toggle_button1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-switch__ripple'])[1]")))
        login.execute_script("arguments[0].click();", toggle_button1)

        # Select Service Location
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'mat-mdc-select-trigger') and .//span[text()='Service Location *']]"))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[1]"))).click()

        # Toggle second switch
        toggle_button2 = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-switch__ripple'])[2]")))
        login.execute_script("arguments[0].click();", toggle_button2)

        # Select Service Building
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'mat-mdc-select-trigger') and .//span[text()='Service Building *']]"))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Block B'])[1]"))).click()

        # Enter Pricing
        pricing = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[normalize-space(.)='Pricing'])[1]")))
        login.execute_script("arguments[0].scrollIntoView();", pricing)
        pricing.click()
        pricing_text = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='price'])[1]")))
        pricing_text.clear()
        pricing_text.send_keys("400")

        # Click Save
        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='mdc-button__label'])[1]"))).click()

        # ✅ Assertion: Verify the created service is listed
        row_xpath = f"//tr[td[1]//span[normalize-space()='{service_name}'] and td[2][normalize-space()='Chembukkav'] and td[3][normalize-space()='Block B']]"
        service_row = wait.until(EC.presence_of_element_located((By.XPATH, row_xpath)))
        assert service_row.is_displayed(), f"Service '{service_name}' with location 'Chembukkav' and building 'Block B' not found in the table."

        time.sleep(3)
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create a Service without pricing and addon applicable")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_13(login):
    try:

        time.sleep(5)
        wait = WebDriverWait(login, 30)

        # Navigate to Services section
        wait.until(EC.presence_of_element_located((By.XPATH, "(//img)[4]"))).click()

        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Services')])[1]"))).click()

        # Click Create Service
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'create-item-button') and contains(text(), 'Create Service')]"))).click()

        # Click on the first group option (if needed)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='font-weight-bold grouping-heading float-left'])[1]"))).click()

        # Fill in Service Name
        service_name = "Service" + str(uuid.uuid4())[:4]
        wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='service_name'])[1]"))).send_keys(service_name)

        # Toggle first switch
        toggle_button1 = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-switch__ripple'])[1]")))
        login.execute_script("arguments[0].click();", toggle_button1)

        # Select Service Location
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'mat-mdc-select-trigger') and .//span[text()='Service Location *']]"))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[1]"))).click()

        # Toggle second switch
        toggle_button2 = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-switch__ripple'])[2]")))
        login.execute_script("arguments[0].click();", toggle_button2)

        # Select Service Building
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'mat-mdc-select-trigger') and .//span[text()='Service Building *']]"))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Block B'])[1]"))).click()

        toggle_button3 = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='mdc-switch__ripple'])[3]")))
        login.execute_script("arguments[0].click();", toggle_button3)

        time.sleep(2)

        # Click Save
        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='mdc-button__label'])[1]"))).click()

        # ✅ Assertion: Verify the created service is listed
        row_xpath = f"//tr[td[1]//span[normalize-space()='{service_name}'] and td[2][normalize-space()='Chembukkav'] and td[3][normalize-space()='Block B']]"
        service_row = wait.until(EC.presence_of_element_located((By.XPATH, row_xpath)))
        assert service_row.is_displayed(), f"Service '{service_name}' with location 'Chembukkav' and building 'Block B' not found in the table."

        time.sleep(3)
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Treatment Room Creation and Patient Admission")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_14(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        wait.until(
        EC.presence_of_element_located((By.XPATH, "(//img)[4]"))
        ).click()
        
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='dashboard-card-image'])[6]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        room_name = f'TreatmentRoom{random.randint(1000, 9999)}'

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Select Building'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Select Floor'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='First Floor B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Select Type'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Treatment Room'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Select Category'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Private Room'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Room Name'])[1]"))
        ).send_keys(room_name)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Select Room Nature'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Room'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.step("Click on IP Management Menu")
def click_ip_management_menu(driver):
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "(//img)[4]"))
    ).click()

@allure.step("Navigate to Room Management")
def navigate_to_room_management(driver):
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "(//div[@class='dashboard-card-image'])[6]"))
    ).click()

@allure.step("Click on 'Create Room' button")
def click_create_room(driver):
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Create Room')]"))
    ).click()

@allure.step("Select building: Block B")
def select_building(driver):
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Select Building'])[1]"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Block B'])[1]"))
    ).click()

@allure.step("Select floor: Second Floor B")
def select_floor(driver):
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Select Floor'])[1]"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Second Floor B'])[1]"))
    ).click()

@allure.step("Select room type: Normal Room")
def select_room_type(driver):
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Select Type'])[1]"))
    ).click()
    room_type = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Normal Room'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", room_type)
    room_type.click()

@allure.step("Select room category: Private Room")
def select_room_category(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Select Category'])[1]"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Private Room'])[1]"))
    ).click()

@allure.step("Enter room name: {room_name}")
def enter_room_name(driver, room_name):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Room Name'])[1]"))
    ).send_keys(room_name)

@allure.step("Select room nature: Room")
def select_room_nature(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Select Room Nature'])[1]"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Room'])[1]"))
    ).click()

@allure.step("Click Create button")
def click_create_button(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Create'])[1]"))
    ).click()

@allure.step("Validate room creation: {room_name}")
def validate_room_creation(driver, room_name):
    toast_detail = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_detail.text
    print("toast_Message:", message)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody//tr[1]"))
    )
    first_row = driver.find_element(By.XPATH, "//tbody//tr[1]")
    print(f"First row text: {first_row.text}")

    if room_name in first_row.text:
        print(f"✅ Room '{room_name}' is present in the first row.")
        print(f"❌ Room '{room_name}' NOT found in the first row: {first_row.text}")
        assert False, f"{room_name} not found in first row"

# >>> Test Case <<<

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Room creation")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_15(login):
    try:
        time.sleep(3)
        click_ip_management_menu(login)

        time.sleep(3)
        navigate_to_room_management(login)

        time.sleep(3)
        click_create_room(login)

        time.sleep(2)
        select_building(login)

        time.sleep(1)
        select_floor(login)

        time.sleep(1)
        select_room_type(login)

        time.sleep(1)
        select_room_category(login)

        room_name = get_next_room_name()
        enter_room_name(login, room_name)

        time.sleep(2)
        select_room_nature(login)

        time.sleep(1)
        click_create_button(login)

        validate_room_creation(login, room_name)

        time.sleep(5)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Reservation with existing IP Patient without bed")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_16(login):

    wait = WebDriverWait(login, 20)
    try:
        time.sleep(5)

        wait_and_locate_click(login, By.XPATH, "(//img)[4]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[3]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='New Reservation'])[1]")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@id='inputSrch_IP_Search'])[1]", "555")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Id : 102'])[1]")

        time.sleep(2)
        admission_dropdown = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//p-dropdown[@placeholder='Select Admission Type'])[1]")
            )
        )
        admission_dropdown.click()

        # Wait and fetch all options in the dropdown
        dropdown_options = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@role='listbox' and contains(@class, 'p-dropdown-items')]/p-dropdownitem/li")
            )
        )

        # Randomly choose and click one option
        random_option = random.choice(dropdown_options)
        random_option_text = random_option.text.strip()
        random_option.click()

        print(f"✅ Randomly selected admission type: {random_option_text}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-dropdown[@placeholder='Select Admitted Doctor'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        time.sleep(2)

        today_element = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
        (By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")
                )
        )          

        # Click using JavaScript in case normal click doesn't work
        login.execute_script("arguments[0].click();", today_element)

        print("Clicked today's date:", today_element.text)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]"))
        ).click()

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=3)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")
            )
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Reserve Now'])[1]")

        msg = get_toast_message(login)
        print("Toas Message :", msg)
        time.sleep(3)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Reservation with existing IP Patient with bed")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_17(login):

    wait = WebDriverWait(login, 20)
    try:
        time.sleep(5)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='dashboard-card-image'])[6]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1] "))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        drop_downlist = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal Room'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", drop_downlist)
        time.sleep(1)   
        drop_downlist.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Private Room'])[1]"))
        ).click()

        room_name = get_next_room_name()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Room Name'])[1]")
            )
        ).send_keys(room_name)

        print(f"🏨 Room created: {room_name}")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[5]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Room'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()
    
        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-button-label'][normalize-space()='Room Details'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Yes'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()
        
        time.sleep(1)
        bed_type = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_type)
        time.sleep(1)
        bed_type.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Observation Beds'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(1)
        bed_price = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Manual Hospital Bed'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", bed_price)
        time.sleep(1)
        bed_price.click()

        bed_name  = f'Bed{room_name}'
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Bed Name'])[1]"))
        ).send_keys(bed_name)   

        time.sleep(1)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Create'])[1]"))
        ).click()   

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//img)[4]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[3]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='New Reservation'])[1]")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@id='inputSrch_IP_Search'])[1]", "555")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Id : 102'])[1]")

        time.sleep(2)
        admission_dropdown = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//p-dropdown[@placeholder='Select Admission Type'])[1]")
            )
        )
        admission_dropdown.click()

        # Wait and fetch all options in the dropdown
        dropdown_options = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@role='listbox' and contains(@class, 'p-dropdown-items')]/p-dropdownitem/li")
            )
        )

        # Randomly choose and click one option
        random_option = random.choice(dropdown_options)
        random_option_text = random_option.text.strip()
        random_option.click()

        print(f"✅ Randomly selected admission type: {random_option_text}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-dropdown[@placeholder='Select Admitted Doctor'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        time.sleep(2)

        today_element = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
        (By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")
                )
        )          

        # Click using JavaScript in case normal click doesn't work
        login.execute_script("arguments[0].click();", today_element)

        print("Clicked today's date:", today_element.text)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]"))
        ).click()

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=3)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
            )
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")
            )
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block B'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"))
        ).click()

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Reserve Now'])[1]")

        msg = get_toast_message(login)
        print("Toas Message :", msg)
        time.sleep(3)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Update the Reservation")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_18(login):

    wait = WebDriverWait(login, 20)
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "(//img)[4]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[3]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//img[@alt='add'])[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Edit'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]")

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=3)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=6)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Update'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Cancel the Reservation")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_19(login):
    wait = WebDriverWait(login, 20)
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "(//img)[4]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[3]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//img[@alt='add'])[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@role='menuitem'])[2]")

        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, "//textarea[contains(@class, 'p-inputtextarea') and contains(@class, 'p-inputtext')]", "other")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='OK'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Yes'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)
    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Add the service with recurrent")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_20(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)
        wait_and_locate_click(
            login, By.XPATH, "(//div[@routerlinkactive='active-menu'])[3]"
        )

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//button[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//div[contains(text(),'Medical Record')])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//button[normalize-space()='Services'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//label[normalize-space()='Recurrent'])[1]"
        )   

        time.sleep(1)
        wait_and_send_keys(
            login, By.XPATH, "(//input[@placeholder='Search Service'])[1]", "Doc"
        )

        time.sleep(1)
        wait_and_locate_click(
            login, By.XPATH, "(//li[@role='option'])[1]"
        )

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=1)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=4)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Enter Service Duration (in minutes)'])[1]", "2")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//p-multiselect[@placeholder='Select Doctors'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Krishna JP'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Next'])[1]")

        # Verify follow-up containers/cards are rendered for all dates
        time.sleep(2)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class,'followup-container')]")))
            print("Follow-up container detected.")
        except Exception:
            # Fallback: presence of section header indicating recurrence summary
            wait.until(EC.presence_of_element_located((By.XPATH, "//h4[contains(., 'Recurrent')]")))
            print("Fallback used: 'Recurrent' header present (container class not found).")

        # Collect displayed dates from follow-up cards
        date_elements = login.find_elements(By.XPATH, "//div[contains(@class,'followup-card')]//p[contains(., 'Date')]/span | //div[contains(@class,'followup-card')]//span[contains(@class,'text-blue-600')]")
        displayed_dates = [el.text.strip() for el in date_elements if el.text and el.text.strip()]
        print(f"Displayed follow-up dates: {displayed_dates}")
        assert displayed_dates, "No follow-up dates rendered in UI"

        # Compute expected dates between selected start and end (inclusive)
        start_dt = (datetime.now() + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        end_dt = (datetime.now() + timedelta(days=4)).replace(hour=0, minute=0, second=0, microsecond=0)
        expected_dates = []
        cur = start_dt
        while cur <= end_dt:
            expected_dates.append(cur.strftime("%d/%m/%Y"))
            cur += timedelta(days=1)
        print(f"Expected follow-up dates: {expected_dates}")

        # Assert card count and exact dates
        cards = login.find_elements(By.XPATH, "//div[contains(@class,'followup-card')]")
        cards_count = len(cards)
        expected_count = len(expected_dates)
        print(f"Asserting card count. Found: {cards_count}, Expected: {expected_count}")
        assert cards_count == expected_count, f"Expected {expected_count} follow-up cards, found {cards_count}"
        print("Card count assertion passed.")
        missing = [d for d in expected_dates if d not in displayed_dates]
        if missing:
            print(f"Missing follow-up dates in UI: {missing}")
        else:
            print("All expected follow-up dates are present.")
        assert not missing, f"Missing follow-up dates in UI: {missing}"

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Add Service'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "(//p-dropdown[@placeholder='Select TimeStamp'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Date Range'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]")

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=1)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=4)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnSave_IP_DBAnltcs']")

        time.sleep(2)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Update the service")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_21(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)
        wait_and_locate_click(
            login, By.XPATH, "(//div[@routerlinkactive='active-menu'])[3]"
        )

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//button[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//div[contains(text(),'Visits & Services')])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            login, By.XPATH, "(//p-dropdown[@placeholder='Select TimeStamp'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='All'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//img[@alt='add'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@role='menuitem'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]")

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=2)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=7)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 12  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # Click the future day
        date_xpath = f"//td[not(contains(@class, 'p-disabled'))]//span[normalize-space()='{future_day}']"
        target_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        target_date.click()

        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Update Service'])[1]")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(2)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Update the service")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_Management_21(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "(//div[@routerlinkactive='active-menu'])[3]")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "")


    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e