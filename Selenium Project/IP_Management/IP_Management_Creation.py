from Framework.common_utils import *
from Framework.common_dates_utils import *
import random
from faker import Faker




@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Buliding creation, Updation, Status Enable and Disable")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_1(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "(//*[@id='actionNav_IP_DBoard'])[4]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCrtBdng_IP_Buildgs']"
        )

        building_name = "Block" + str(uuid.uuid4().int)[:4]

        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputBdng_IP_CrtBdng']", building_name
        )

        wait_and_send_keys(
            driver, By.XPATH, "//textarea[@id='inputDec_IP_CrtBdng']", "Operating 24/7, with specialized teams prepared for trauma, accidents, and life-threatening conditions."
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnSave_IP_CrtBdng']"
        )

        msg = get_snack_bar_message(driver)
        print("Snack Bar Message:", msg)

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "(//img[@alt='add'])[3]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[contains(@class,'btnEdit_IP_BdngGrd')]"
        )

        building_rename = "BlockRen" + str(uuid.uuid4().int)[:4]

        name_element = driver.find_element(By.XPATH, "//input[@id='inputBdng_IP_CrtBdng']")
        name_element.click()
        name_element.clear()
        name_element.send_keys(building_rename)

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnSave_IP_CrtBdng']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//img[@alt='add'])[3]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[contains(@class,'btnStatus_IP_BdngGrd')]"
        )                                                

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        
        time.sleep(2)

        inactive_xpath = (
            "//tbody[contains(@class,'p-datatable-tbody')]"
            "//tr[1]//td[2]//span[contains(normalize-space(.), 'Inactive')]"
        )

        try:
            is_inactive = driver.find_element(By.XPATH, inactive_xpath).is_displayed()
        except Exception:
            is_inactive = False

        print("ASSERT Inactive status :", is_inactive)
        assert is_inactive, "Inactive status not displayed"

        wait_and_locate_click(
            driver, By.XPATH, "(//img[@alt='add'])[2]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[contains(@class,'btnStatus_IP_BdngGrd')]"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)
        active_xpath = (
            "//tbody[contains(@class,'p-datatable-tbody')]"
            "//tr[1]//td[2]//span[contains(normalize-space(.), 'Active')]"
        )

        try:
            is_active = driver.find_element(By.XPATH, active_xpath).is_displayed()
        except Exception:
            is_active = False

        print("ASSERT Active status :", is_active)
        assert is_active, "Active status not displayed"



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
@allure.title("Test Case: Floor creation, Updation, Status Enable and Disable")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_2(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "(//*[@id='actionNav_IP_DBoard'])[5]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCrt_IP_Flors']"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@id='selectBldgs_IP_FlrCrt']"
        )

        element1 = driver.find_element(By.XPATH, "//*[normalize-space()='Block C']")
        scroll_to_element(driver, element1)
        element1.click()

        time.sleep(1)
        floor_name = "Floor" + str(uuid.uuid4().int)[:4]
        wait_and_send_keys(
            driver, By.XPATH, "//input[@id='inputFloor_IP_FlrCrt']" , floor_name
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnSave_IP_FlrCrt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//img[@alt='add'])[3]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//*[contains(@class,'btnEdit_IP_FlrGrd')]"
        )

        floor_rename = "FloorRen" + str(uuid.uuid4().int)[:4]
        floor_element = driver.find_element(By.XPATH, "//*[@id='inputFloor_IP_FlrCrt']")
        floor_element.click()
        floor_element.clear()
        floor_element.send_keys(floor_rename)

        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnSave_IP_FlrCrt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//img[@alt='add'])[3]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[contains(@class,'btnStatus_IP_FlrGrd ')]"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        inactive_xpath = (
            "(//tr[contains(@class,'ng-star-inserted')]//td[3]//span[contains(normalize-space(.),'Inactive')])[1]"
        )

        try:
            is_inactive = driver.find_element(By.XPATH, inactive_xpath).is_displayed()
        except Exception:
            is_inactive = False

        print("ASSERT Inactive status :", is_inactive)
        assert is_inactive, "Inactive status not displayed"

        wait_and_locate_click(
            driver, By.XPATH, "(//img[@alt='add'])[2]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[contains(@class,'btnStatus_IP_FlrGrd ')]"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)
        active_xpath = (
            "//tr[contains(@class,'ng-star-inserted')]//td[3]//span[contains(normalize-space(.),'Active')]"
        )

        try:
            is_active = driver.find_element(By.XPATH, active_xpath).is_displayed()
        except Exception:
            is_active = False

        print("ASSERT Active status :", is_active)
        assert is_active, "Active status not displayed"


    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Room Creation , Updation, Status Enable and Disable")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_3(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[6]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//*[@id='btnCreate_IP_RO_RO']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//*[@formcontrolname='building']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//*[normalize-space()='Block C']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@formcontrolname='floor']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='First floor']")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@formcontrolname='roomType']")

        drop_downlist = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Private']"))
        )

        login.execute_script("arguments[0].scrollIntoView();", drop_downlist)
        time.sleep(1)   
        drop_downlist.click()

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@formcontrolname='roomCategory']")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Private'])[1]")


        room_name = get_next_room_name()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Room Name'])[1]")
            )
        ).send_keys(room_name)

        print(f"🏨 Room created: {room_name}")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@formcontrolname='roomNature']")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Room'])[1]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Create'])[1]")
    
        msg = get_toast_message(login)
        print("Toast Message :", msg)
        
        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[contains(@class,'btnActMenu_IP_RmGrd')])[1]"
        )

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//button[contains(@class,'btnEdit_IP_RmGrd')]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//p-dropdown[@formcontrolname='building']"
        )

        room_element = driver.find_element(By.XPATH, "//*[normalize-space()='Block C']")
        scroll_to_element(driver, room_element)
        room_element.click()

        wait_and_locate_click(
            driver, By.XPATH, "//*[normalize-space()='Update']"
        )

        msg = get_toast_message(driver)
        print("Toast Message : ", msg)

        wait_and_locate_click(
            driver, By.XPATH, "(//button[contains(@class,'btnActMenu_IP_RmGrd')])[1]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[contains(@class,'btnStatus_IP_RmGrd ')]"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        inactive_xpath = (
            "(//tr[contains(@class,'ng-star-inserted')]//td[5]//span[contains(normalize-space(.),'Inactive')])[1]"
        )

        try:
            is_inactive = driver.find_element(By.XPATH, inactive_xpath).is_displayed()
        except Exception:
            is_inactive = False

        print("ASSERT Inactive status :", is_inactive)
        assert is_inactive, "Inactive status not displayed"

        wait_and_locate_click(
            driver, By.XPATH, "(//img[@alt='add'])[2]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[contains(@class,'btnStatus_IP_RmGrd')]"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)
        active_xpath = (
            "//tr[contains(@class,'ng-star-inserted')]//td[5]//span[contains(normalize-space(.),'Active')]"
        )

        try:
            is_active = driver.find_element(By.XPATH, active_xpath).is_displayed()
        except Exception:
            is_active = False

        print("ASSERT Active status :", is_active)
        assert is_active, "Active status not displayed"

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
@allure.title("Test Case: Room type creation, Updation, Status Enable and Disable")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_4(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[6]"
        )

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//*[@id='btnCreate_IP_RO_RO']")

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//span[normalize-space()='Create Room Type'])[1]"
        )

        time.sleep(1)
        room_type = "RoomType" + str(uuid.uuid4().int)[:4]

        wait_and_send_keys(
            driver, By.XPATH, "//input[@placeholder='Enter Name']", room_type
        )

        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='selectRoom_IP_Crt']"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//*[normalize-space()='Accommodation Room']"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='selectType_IP_Crt']"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//*[normalize-space()='Semi-Private Room']"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnSave_IP_Crt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//*[@class='pi pi-arrow-left']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//*[@placeholder='Variants']"
        )

        wait_and_locate_click(
            driver, By.XPATH, "(//*[normalize-space()='Type'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//*[contains(@class,'btnUpdate_IP_TY_TY ')])[1]"
        )

        room_type_rename = "RoomTypeRename" + str(uuid.uuid4().int)[:4]

        room_type_element = driver.find_element(By.XPATH, "//*[@placeholder='Enter Name']")
        room_type_element.click()
        room_type_element.clear()
        room_type_element.send_keys(room_type_rename)
        

        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnSave_IP_Crt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//*[contains(@class,'togStatus_IP_TY_TY ')])[1]"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "(//*[contains(@class,'togStatus_IP_TY_TY ')])[1]"
        )

        msg = get_toast_message(driver)
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
@allure.title("Test Case: Room Category creation, Updation, Status Enable and Disable")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_5(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[6]"
        )

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//*[@id='btnCreate_IP_RO_RO']")

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "//span[normalize-space()='Create Room Category']"
        )

        room_category = "RoomCat" + str(uuid.uuid4().int)[:4]

        wait_and_send_keys(
             driver, By.XPATH, "//*[@placeholder='Enter Name']", room_category
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnSave_IP_Crt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "//*[@class='pi pi-arrow-left']"
        )

        time.sleep(1)

        wait_and_locate_click(
             driver, By.XPATH, "//*[@placeholder='Variants']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "(//*[normalize-space()='Category'])[1]"
        )

        wait_and_locate_click(
             driver, By.XPATH, "(//*[contains(@class,'btnUpdate_IP_Catgry ')])[1]"
        )

        time.sleep(1)
        
        room_category_rename = "RoCatRe" + str(uuid.uuid4().int)[:4]

        room_cat_element = driver.find_element(By.XPATH, "//*[@placeholder='Enter Name']")
        room_cat_element.click()
        room_cat_element.clear()
        room_cat_element.send_keys(room_category_rename)

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnSave_IP_Crt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "(//*[contains(@class,'togStatus_IP_Catgry')])[1]"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "(//*[contains(@class,'togStatus_IP_Catgry')])[1]"
        )

        msg = get_toast_message(driver)
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
@allure.title("Test Case: Bed creation, Updation, Status Blocked, Not available and Available")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_6(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[7]"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "//button[@id='btnCrtBed_IP_Beds']"
        )
        
        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='selectBld_IP_BedCrt']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[normalize-space()='Block D']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='selectResrv_IP_BedCrt']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[normalize-space()='Yes']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='selectBed_IP_BedCrt']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[normalize-space()='Normal']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='selectBedCat_IP_BedCrt']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Normal'])[1]"
        )
        
        wait_and_locate_click(
             driver, By.XPATH, "//p-dropdown[@id='selectBedPrice_IP_BedCrt']"
        )
    
        wait_and_locate_click(
             driver, By.XPATH, "//*[normalize-space()='Normal Bed']"
        )

        room_name = get_next_room_name()
        bed_name = f"Bed{room_name}"

        bed_input = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@id='inputBed_IP_BedCrt']")
            )
        )
        bed_input.clear()
        bed_input.send_keys(bed_name)

        print(f"🛏️ Bed created: {bed_name}")

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnCrt_IP_BedCrt']"
        )
        
        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnEdtBed_IP_BedGrd']"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='selectResrv_IP_BedCrt']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[normalize-space()='No']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnCrt_IP_BedCrt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(3)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnView_IP_BedGrd']"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "//button[@id='btnActMenu_IP_BedDetls']"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnBlock_IP_BedDetls']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='actionBack_IP_BedDetls']"
        )

        time.sleep(2)
        blocked_xpath = (
            "(//tr[contains(@class,'ng-star-inserted')]//td[6]//span[contains(normalize-space(.),'Blocked')])[1]"
        )

        try:
            is_blocked = driver.find_element(By.XPATH, blocked_xpath).is_displayed()
        except Exception:
            is_blocked = False

        print("ASSERT blocked status :", is_blocked)
        assert is_blocked, "blocked status not displayed"

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnView_IP_BedGrd']"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnActMenu_IP_BedDetls']"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnAvlbl_IP_BedDetls']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='actionBack_IP_BedDetls']"
        )



        time.sleep(2)
        Not_Available_xpath = (
            "(//tr[contains(@class,'ng-star-inserted')]//td[6]//span[contains(normalize-space(.),'Not Available')])[1]"
        )

        try:
            is_Not_Available = driver.find_element(By.XPATH, Not_Available_xpath).is_displayed()
        except Exception:
            is_Not_Available = False

        print("ASSERT Not_Available status :", is_Not_Available)
        assert is_Not_Available, "Not_Available status not displayed"


        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnView_IP_BedGrd']"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnActMenu_IP_BedDetls']"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnAvbl_IP_BedDetls']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='actionBack_IP_BedDetls']"
        )

        time.sleep(2)
        Available_xpath = (
            "(//tr[contains(@class,'ng-star-inserted')]//td[6]//span[contains(normalize-space(.),'Available')])[1]"
        )

        try:
            is_Available = driver.find_element(By.XPATH, Available_xpath).is_displayed()
        except Exception:
            is_Available = False

        print("ASSERT Available status :", is_Available)
        assert is_Available, "Available status not displayed"

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
@allure.title("Test Case: Bed Price creation, Updation, Status Enable and Disable")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_7(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[7]"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "//button[@id='btnCrtBed_IP_Beds']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnCrtBed_IP_BedCrt']"
        )

        bed_price = "bedprice" + str(uuid.uuid4().int)[:4]

        wait_and_send_keys(
             driver, By.XPATH, "//*[@placeholder='Enter Name']", bed_price 
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='selectRate_IP_Crt']"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[normalize-space()='Daily']"
        )

        price_input = driver.find_element(By.XPATH, "//*[@id='inputRate_IP_Crt']")
        price_input.click()
        price_input.clear()
        price_input.send_keys("700")


        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='selectUpdt_IP_Crt']"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[normalize-space()='Daily']"
        )

        price_input_1 = driver.find_element(By.XPATH, "//*[@id='inputRet_IP_Crt']")
        price_input_1.click()
        price_input_1.clear()
        price_input_1.send_keys("350")

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnSave_IP_Crt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='actionBack_IP_BedCrt']"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='selectVar_IP_BedGrd']"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[normalize-space()='Pricing']"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//button[@id='btnCrtPrice_IP_Pricing'])[1]"
        )

        time.sleep(1)
        price_input_2 = driver.find_element(By.XPATH, "//*[@id='inputRate_IP_Crt']")
        price_input_2.click()
        price_input_2.clear()
        price_input_2.send_keys("600")

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnSave_IP_Crt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "(//*[@id='selectSts_IP_Pricing'])[1]"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "(//*[@id='selectSts_IP_Pricing'])[1]"
        ) 

        msg = get_toast_message(driver)
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
@allure.title("Test Case: Bed Type creation, Updation, Status Enable and Disable")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_8(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[7]"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "//button[@id='btnCrtBed_IP_Beds']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnCrtPop_IP_BedCrt']"
        )

        Bed_type = "Bedtype" + str(uuid.uuid4().int)[:4]

        wait_and_send_keys(
             driver, By.XPATH, "//input[@placeholder='Enter Name']", Bed_type  
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='selectBedPr_IP_Crt']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[normalize-space()='Normal Bed']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnSave_IP_Crt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)


        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='actionBack_IP_BedCrt']"
        )

        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='selectVar_IP_BedGrd']"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[normalize-space()='Type']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "(//*[contains(@class,'btnUpdate_IP_TY_TY')])[1]"
        )

        bedtype_rename = "BedtypeRen" + str(uuid.uuid4().int)[:4]

        bed_type_element = driver.find_element(By.XPATH, "//input[@placeholder='Enter Name']")
        bed_type_element.click()
        bed_type_element.clear()
        bed_type_element.send_keys(bedtype_rename)

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnSave_IP_Crt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "(//*[contains(@class,'togStatus_IP_TY_TY')])[1]"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "(//*[contains(@class,'togStatus_IP_TY_TY')])[1]"
        )

        msg = get_toast_message(driver)
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
@allure.title("Test Case: Bed Category creation, Updation, Status Enable and Disable")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_9(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[7]"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "//button[@id='btnCrtBed_IP_Beds']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnCrtBedCat_IP_BedCrt']"
        )


        Bed_category = "Bedcategory" + str(uuid.uuid4().int)[:4]

        wait_and_send_keys(
             driver, By.XPATH, "//input[@placeholder='Enter Name']", Bed_category
        )

        wait_and_locate_click(
             driver, By.XPATH, "//button[@id='btnSave_IP_Crt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "//div[@id='actionBack_IP_BedCrt']"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='selectVar_IP_BedGrd']"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[normalize-space()='Category']"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "(//*[contains(@class,'btnUpdate_IP_Catgry')])[1]"
        )

        Bed_category_1 = "BedcategoryRen" + str(uuid.uuid4().int)[:4]

        time.sleep(2)

        category_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Name']")
        category_input.click()
        category_input.clear()
        category_input.send_keys(Bed_category_1)

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnSave_IP_Crt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "(//*[contains(@class,'togStatus_IP_Catgry')])[1]"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "(//*[contains(@class,'togStatus_IP_Catgry')])[1]"
        )

        msg = get_toast_message(driver)
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
@allure.title("Test Case: Admission type creation, Updation, Status Enable and Disable")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_10(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "(//*[@id='actionNav_IP_DBoard'])[11]"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnCrtReg_IP_Regstr']"
        )

        Admission_name = "Admission" + str(uuid.uuid4().int)[:4]
        wait_and_send_keys(
             driver, By.XPATH, "//*[@placeholder='Enter Name']", Admission_name
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='selectReg_IP_Crt']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[normalize-space()='Generic']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnSave_IP_Crt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "(//*[@id='btnSave_IP_Regstr'])[1]"
        )

        time.sleep(2)
        Admission_rename = "Admis-Ren" + str(uuid.uuid4().int)[:4]

        Admission_name_element= driver.find_element(By.XPATH, "//*[@placeholder='Enter Name']") 
        Admission_name_element.click()
        Admission_name_element.clear()
        Admission_name_element.send_keys(Admission_rename)

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnSave_IP_Crt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "(//*[@id='selectSts_IP_Regstr'])[1]"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)


        wait_and_locate_click(
             driver, By.XPATH, "(//*[@id='selectSts_IP_Regstr'])[1]"
        )

        msg = get_toast_message(driver)
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
@allure.title("Test Case: Service creation, Updation, Status Enable and Disable")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_11(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "(//*[@id='actionNav_IP_DBoard'])[10]"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnCreate_IP_SE_SE']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "(//*[@class='fa fa-angle-down'])[1]"
        )

        Service_name = "Service" + str(uuid.uuid4().int)[:4]

        wait_and_send_keys(
             driver, By.XPATH, "//*[@id='service_name']", Service_name
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@placeholder='Rate type']"
        )
        
        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[normalize-space()='Fixed']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "(//*[@class='fa fa-angle-down'])[2]"
        )

        time_element = driver.find_element(By.XPATH, "//input[@placeholder='MM']")
        time_element.click()
        time_element.clear()
        time_element.send_keys("5")

        wait_and_locate_click(
             driver, By.XPATH, "(//*[@class='fa fa-angle-down'])[3]"
        )

        price = random.randint(400, 1000)

        ser_price = driver.find_element(By.XPATH, "//*[@id='price']")
        ser_price.click()
        ser_price.clear()
        ser_price.send_keys(price)

        wait_and_locate_click(
             driver, By.XPATH, "//*[@type='submit']"
        )

        msg = get_snack_bar_message(driver)
        print("Snack Bar Message: ", msg)
        time.sleep(3)

        wait_and_locate_click(
             driver, By.XPATH, "(//*[contains(@class,'btnActMenu_IP_SV_GR')])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "(//*[contains(@class,'btnEdit_IP_SV_GR')])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//*[@class='fa fa-angle-down'])[1]"
        )

        Service_rename = "Ser_Ren" + str(uuid.uuid4().int)[:4]

        Rename_element = driver.find_element(By.XPATH, "//*[@id='service_name']")
        Rename_element.click()
        Rename_element.clear()
        Rename_element.send_keys(Service_rename)

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@type='submit']"
        )

        msg = get_snack_bar_message(driver)
        print("Snack Bar Message: ", msg)
        time.sleep(3)

        wait_and_locate_click(
             driver, By.XPATH, "(//*[contains(@class,'btnActMenu_IP_SV_GR')])[1]"
        )

        wait_and_locate_click(
             driver, By.XPATH, "(//*[contains(@class,'btnStatus_IP_SV_GR')])[1]"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        inactive_xpath = (
            "//tbody[contains(@class,'p-datatable-tbody')]"
            "//tr[1]//td[5]//span[contains(normalize-space(.), 'Inactive')]"
        )

        try:
            is_inactive = driver.find_element(By.XPATH, inactive_xpath).is_displayed()
        except Exception:
            is_inactive = False

        print("ASSERT Inactive status :", is_inactive)
        assert is_inactive, "Inactive status not displayed"

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//*[contains(@class,'btnActMenu_IP_SV_GR')])[1]"
        )    

        wait_and_locate_click(
             driver, By.XPATH, "(//*[contains(@class,'btnStatus_IP_SV_GR')])[1]"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg) 
        time.sleep(2)

        active_xpath = (
            "//tbody[contains(@class,'p-datatable-tbody')]"
            "//tr[1]//td[5]//span[contains(normalize-space(.), 'Active')]"
        )

        try:
            is_active = driver.find_element(By.XPATH, active_xpath).is_displayed()
        except Exception:
            is_active = False

        print("ASSERT Active status :", is_active)
        assert is_active, "Active status not displayed"                                         


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
@allure.title("Test Case: Service creation with location, Updation, Status Enable and Disable")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_12(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "(//*[@id='actionNav_IP_DBoard'])[10]"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnCreate_IP_SE_SE']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "(//*[@class='fa fa-angle-down'])[1]"
        )

        Service_name = "Service" + str(uuid.uuid4().int)[:4]

        wait_and_send_keys(
             driver, By.XPATH, "//*[@id='service_name']", Service_name
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@placeholder='Rate type']"
        )
        
        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[normalize-space()='Fixed']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "(//button[contains(@class,'mdc-switch')])[1]"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@placeholder='Service Location *']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//span[normalize-space()='Veliyannur']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "(//*[@class='fa fa-angle-down'])[2]"
        )

        time_element = driver.find_element(By.XPATH, "//input[@placeholder='MM']")
        time_element.click()
        time_element.clear()
        time_element.send_keys("5")

        wait_and_locate_click(
             driver, By.XPATH, "(//*[@class='fa fa-angle-down'])[3]"
        )

        price = random.randint(400, 1000)

        ser_price = driver.find_element(By.XPATH, "//*[@id='price']")
        ser_price.click()
        ser_price.clear()
        ser_price.send_keys(price)

        wait_and_locate_click(
             driver, By.XPATH, "//*[@type='submit']"
        )

        msg = get_snack_bar_message(driver)
        print("Snack Bar Message: ", msg)
        time.sleep(3)




    except Exception as e:
                allure.attach(  # use Allure package, .attach() method, pass 3 params
                    login.get_screenshot_as_png(),  # param1
                    # login.screenshot()
                    name="full_page",  # param2
                    attachment_type=AttachmentType.PNG,
                )
                raise e