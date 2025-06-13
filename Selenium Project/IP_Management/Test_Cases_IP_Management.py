from Framework.common_utils import *
from Framework.common_dates_utils import *
import random

from faker import Faker



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

        



    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e