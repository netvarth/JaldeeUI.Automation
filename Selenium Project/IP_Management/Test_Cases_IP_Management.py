from Framework.common_utils import *
from Framework.common_dates_utils import *
import random

from faker import Faker

# <<< << <<  << Room and Bed Test cases >>  >>  >>  >>  

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Room creation")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_room_creation_1(login):

    try:

        wait = WebDriverWait(login, 30)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[2]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='dashboard-card-image'])[6]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[@class='p-element create-item-button p-button p-component'])[1]"))
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

        # time.sleep(1)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[normalize-space()='Select Status'])[1]"))
        # ).click()

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
        else:
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
def test_IP_room_creation_2(login):
    
 
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30) 

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//img)[2]"))    
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
            EC.presence_of_element_located((By.XPATH, "(//button[@class='p-element create-item-button p-button p-component'])[1]"))
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
def test_IP_room_creation_3(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[2]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='dashboard-card-image'])[6]"))
        ).click()


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[@class='p-element create-item-button p-button p-component'])[1]"))
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
def test_IP_room_creation_4(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//img)[2]"))    
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='my-1 font-small fw-bold text-capitalize ng-star-inserted'][normalize-space()='Rooms'])[1]"))
        ).click()

        time.sleep(1)

        room_name_to_find = "351B"
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
            EC.presence_of_element_located((By.XPATH, "(//button[@class='p-element create-item-button p-button p-component'])[1]"))
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
def test_IP_room_creation_5(login):

    try:

        wait = WebDriverWait(login, 30)
        time.sleep(5)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//img)[2]"))    
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
        
        time.sleep(5)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component'])[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click() 

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Doc Visit'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        time.sleep(1)
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
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(2)
        # Locate the minute up arrow
        minute_up_button = login.find_element(By.XPATH, "//div[contains(@class,'p-minute-picker')]//button[1]")

        # Click it 10 times
        for _ in range(10):
            minute_up_button.click()
            time.sleep(0.2)  # slight delay to ensure the click registers

        print("✅ Increased minutes by 10 clicks.")
        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))

        # Click on today's date
        today_element.click()

        print("Clicked today's date:", today_element.text)
        
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]"))
        ).click()

        time.sleep(2)
        # Locate the minute up arrow
        minute_up_button = login.find_element(By.XPATH, "//div[contains(@class,'p-minute-picker')]//button[1]")

        # Click it 10 times
        for _ in range(20):
            minute_up_button.click()
            time.sleep(0.2)  # slight delay to ensure the click registers

        print("✅ Increased minutes by 20 clicks.")

        time.sleep(2)

        today_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")))

        # Click on today's date
        today_element.click()

        print("Clicked today's date:", today_element.text)

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Add Service'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Medical Records'])[1]"))
        ).click()


        time.sleep(2)
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
            else:
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

        
        
        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Share'])[1]"))
        ).click()
        
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
@allure.title("Test Case: Create the RX Push and Complete Order")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_room_creation_6(login):


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
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='mdc-switch__ripple'])[1]"))
        ).click()

        





        time.sleep(2)
      



    
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e