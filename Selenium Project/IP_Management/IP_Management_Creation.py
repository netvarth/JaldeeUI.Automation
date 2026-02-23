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
        driver = driver
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
            driver.get_screenshot_as_png(),  # param1
            # driver.screenshot()
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
        driver = driver
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
            driver.get_screenshot_as_png(),  # param1
            # driver.screenshot()
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
        driver = driver
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[6]"))
        ).click()

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//*[@id='btnCreate_IP_RO_RO']")

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//*[@formcontrolname='building']")

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//*[normalize-space()='Block C']")

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//p-dropdown[@formcontrolname='floor']")

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='First floor']")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//p-dropdown[@formcontrolname='roomType']")

        drop_downlist = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Private']"))
        )

        driver.execute_script("arguments[0].scrollIntoView();", drop_downlist)
        time.sleep(1)   
        drop_downlist.click()

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//p-dropdown[@formcontrolname='roomCategory']")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Private'])[1]")


        room_name = get_next_room_name()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Room Name'])[1]")
            )
        ).send_keys(room_name)

        print(f"🏨 Room created: {room_name}")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//p-dropdown[@formcontrolname='roomNature']")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "(//span[normalize-space()='Room'])[1]")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "(//button[normalize-space()='Create'])[1]")
    
        msg = get_toast_message(driver)
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
                driver.get_screenshot_as_png(),  # param1
                # driver.screenshot()
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
        driver = driver
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
                driver.get_screenshot_as_png(),  # param1
                # driver.screenshot()
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
        driver = driver
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
                    driver.get_screenshot_as_png(),  # param1
                    # driver.screenshot()
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
        driver = driver
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
                    driver.get_screenshot_as_png(),  # param1
                    # driver.screenshot()
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
        driver = driver
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
                    driver.get_screenshot_as_png(),  # param1
                    # driver.screenshot()
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
        driver = driver
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
                    driver.get_screenshot_as_png(),  # param1
                    # driver.screenshot()
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
        driver = driver
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
                    driver.get_screenshot_as_png(),  # param1
                    # driver.screenshot()
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
        driver = driver
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
                    driver.get_screenshot_as_png(),  # param1
                    # driver.screenshot()
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
        driver = driver
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
                    driver.get_screenshot_as_png(),  # param1
                    # driver.screenshot()
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
        driver = driver
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
             driver, By.XPATH, "(//*[contains(@class,'mdc-switch')])[1]"
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
                    driver.get_screenshot_as_png(),  # param1
                    # driver.screenshot()
                    name="full_page",  # param2
                    attachment_type=AttachmentType.PNG,
                )
                raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Service creation with same gender, Updation, Status Enable and Disable")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_13(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = driver
        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "(//*[@id='actionNav_IP_DBoard'])[10]"
        )

        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnCreate_IP_SE_SE']"
        )

        time.sleep(1)
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
             driver, By.XPATH, "(//*[@class='mdc-switch__icons'])[4]"
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
                    driver.get_screenshot_as_png(),  # param1
                    # driver.screenshot()
                    name="full_page",  # param2
                    attachment_type=AttachmentType.PNG,
                )
                raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Discharge template creation, Updation, Status Inactive and Active")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_14(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = driver
        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "(//*[@id='actionNav_IP_DBoard'])[13]"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnCrtTemp_IP_Dscrg']"
        )

        Template_name = "Template" + str(uuid.uuid4().int)[:4]

        time.sleep(2)
        wait_and_send_keys(
             driver, By.XPATH, "//*[@id='inputTname_IP_CrtDscrg']", Template_name 
        )

        wait_and_locate_click(
             driver, By.XPATH, "//p-dropdown[@id='selectUsrs_IP_CrtDscrg']"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@class='ng-star-inserted'][normalize-space()='Venu Gopal']"
        )


        discharge_summary = """
            Discharge Summary

            Patient Information:

            Name : [d_var_providerConsumerFirstName] [d_var_providerConsumerLastName]
            Age: [d_var_age]
            Gender: [d_var_gender]
            Date of Admission : [d_var_checkinDate]
            Medical Record : [d_var_inPatientNumber]

            Brief Hospital Course:
            Carmel Ryan was admitted on June 14, 2050, with complaints of chest pain, shortness of breath, and diaphoresis. Initial evaluation revealed an ST-segment elevation myocardial infarction (STEMI) on the electrocardiogram (ECG). Prompt treatment was initiated with aspirin, clopidogrel, and intravenous heparin. An urgent coronary angiography revealed critical stenosis in the left anterior descending artery (LAD), necessitating a percutaneous coronary intervention (PCI) with stent placement. The procedure successfully restored blood flow to the affected area.

            Hospital Course:
            Throughout her hospital stay, Carmel Ryan remained hemodynamically stable. Cardiac enzyme levels trended downwards, indicating successful myocardial reperfusion. Continuous monitoring in the coronary care unit (CCU) showed no signs of arrhythmias or hemodynamic instability. Her chest pain resolved completely, and no further ischemic events were observed.

            Diagnostic Tests:
            ECG: Showed ST-segment elevation in leads V1-V4, indicating an anterior wall myocardial infarction.
            Cardiac Enzymes: Elevated troponin levels peaked 12 hours post-PCI and subsequently decreased.
            Coronary Angiography: Revealed critical stenosis in the LAD, with successful PCI and stent placement.

            Medications at Discharge:
            Aspirin 81 mg once daily
            Clopidogrel 75 mg once daily
            Atorvastatin 40 mg once daily
            Lisinopril 10 mg once daily

            Follow-Up:
            Dr. Sarah Patel is scheduled to follow up with a cardiologist in one week for a repeat ECG and further assessment of cardiac function. The patient is instructed to strictly adhere to the prescribed medication regimen, follow a heart-healthy diet, and engage in regular exercise as tolerated.

            Discharge Instructions:
            Education: Carmel Ryan was educated on recognizing the signs and symptoms of a recurrent myocardial infarction and instructed to seek immediate medical care if they occur.
            Dietary Counseling: A low-sodium, low-fat diet was recommended to prevent future cardiovascular incidents.
            Smoking Cessation: Counseling was provided, and Carmel Ryan was referred to smoking cessation resources for support.
            Activity: Gradual resumption of activity is advised, starting with light exercises as tolerated.

            Conclusion:
            In summary, Carmel Ryan received prompt intervention with successful PCI, leading to stabilization of her cardiac condition. With proper discharge planning and follow-up care, continued recovery is anticipated. Strict adherence to the medication regimen, follow-up appointments, and lifestyle modifications are crucial to optimize long-term cardiovascular health.

            Summarized By: [d_var_providerName]
            """


        temp_body = driver.find_element(
             By.XPATH, "(//div[contains(@class,'ck-editor__editable')])[2]"
        )
        scroll_to_element(driver, temp_body)
        temp_body.click()
        temp_body.send_keys(discharge_summary)

        wait_and_locate_click(
             driver, By.XPATH, "(//div[contains(@class,'ck-editor__editable')])[3]"
        )

        wait_and_locate_click(
             driver, By.XPATH, "(//*[contains(text(),'Add Variables')])[3]"
        )

        variables = driver.find_element(
             By.XPATH, "(//li[contains(@class,'p-dropdown-item')])[8]"
        )

        scroll_to_element(driver, variables)
        variables.click()

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnSave_IP_CrtDscrg']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(3)

        wait_and_locate_click(
             driver, By.XPATH, "(//*[@alt='add'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//button[@id='btnEdtTmp_IP_DscrgTemp']"
        )

        time.sleep(2)

        Template_Rename = "Temp_Ren" + str(uuid.uuid4().int)[:4]

        template_rename = driver.find_element(By.XPATH, "//*[@id='inputTname_IP_CrtDscrg']")
        template_rename.click()
        template_rename.clear()
        template_rename.send_keys(Template_Rename)

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnSave_IP_CrtDscrg']"
            
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "(//*[@alt='add'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnSts_IP_DscrgTemp']//*[@class='mdc-list-item__primary-text']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        inactive_xpath = (
            "//tbody[contains(@class,'p-datatable-tbody')]"
            "//tr[1]//td[4]//span[contains(normalize-space(.), 'Inactive')]"
        )

        try:
            is_inactive = driver.find_element(By.XPATH, inactive_xpath).is_displayed()
        except Exception:
            is_inactive = False

        print("ASSERT Inactive status :", is_inactive)
        assert is_inactive, "Inactive status not displayed"
        
        
        
        wait_and_locate_click(
             driver, By.XPATH, "(//*[@alt='add'])[1]"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnSts_IP_DscrgTemp']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        active_xpath = (
            "//tbody[contains(@class,'p-datatable-tbody')]"
            "//tr[1]//td[4]//span[contains(normalize-space(.), 'Active')]"
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
                    driver.get_screenshot_as_png(),  # param1
                    # driver.screenshot()
                    name="full_page",  # param2
                    attachment_type=AttachmentType.PNG,
                )
                raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Custom Variables creation, Updation, Status Inactive and Active")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_15(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = driver
        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "(//*[@id='actionNav_IP_DBoard'])[13]"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnCfIlds_IP_Dscrg']"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//button[@id='CrtVarbls_IP_CsFld']"
        )
        
        custom_var_name = "cus_var" + str(uuid.uuid4().int)[:4]

        time.sleep(2)
        wait_and_send_keys(
             driver, By.XPATH, "//*[@id='inputName_IP_CsFlds']", custom_var_name
        )

        Display_name = "Display_name" + str(uuid.uuid4().int)[:4]
        wait_and_send_keys(
             driver, By.XPATH, "//*[@id='inputDisp_IP_CsFlds']", Display_name
        )

        wait_and_send_keys(
             driver, By.XPATH, "//*[@id='inputVal_IP_CsFlds']", "Note for the custom variable"
        )

        time.sleep(1)

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnCrtFld_IP_CsFlds']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "(//*[@alt='add'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnEdtFld_IP_CsFld']"
        )

        custom_var_rename = "cus_var_re" + str(uuid.uuid4().int)[:4]

        time.sleep(1)
        Re_Name= driver.find_element(By.XPATH, "//input[@id='inputName_IP_CsFlds']")
        Re_Name.click()
        Re_Name.clear()
        Re_Name.send_keys(custom_var_rename)

        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnCrtFld_IP_CsFlds']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
             driver, By.XPATH, "(//*[@alt='add'])[1]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnSts_IP_CsFld']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)

        time.sleep(2)
        inactive_xpath = (
            "//tbody[contains(@class,'p-datatable-tbody')]"
            "//tr[1]//td[3]//span[contains(normalize-space(.), 'Inactive')]"
        )

        try:
            is_inactive = driver.find_element(By.XPATH, inactive_xpath).is_displayed()
        except Exception:
            is_inactive = False

        print("ASSERT Inactive status :", is_inactive)
        assert is_inactive, "Inactive status not displayed"

        wait_and_locate_click(
             driver, By.XPATH, "(//*[@alt='add'])[1]"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='btnSts_IP_CsFld']"
        )

        msg = get_toast_message(driver)
        print("Toast Message:", msg)
        time.sleep(2)

        active_xpath = (
            "//tbody[contains(@class,'p-datatable-tbody')]"
            "//tr[1]//td[3]//span[contains(normalize-space(.), 'Active')]"
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
                    driver.get_screenshot_as_png(),  # param1
                    # driver.screenshot()
                    name="full_page",  # param2
                    attachment_type=AttachmentType.PNG,
                )
                raise e


        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
             driver, By.XPATH, "(//img)[5]"
        )
        
        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[6]"
        )

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//*[@id='btnCreate_IP_RO_RO']")

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//*[@formcontrolname='building']")

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//*[normalize-space()='Block D']")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='Select Type']")

        room_type = driver.find_element(By.XPATH, "//span[normalize-space()='Private']")
        scroll_to_element(driver, room_type)
        room_type.click()

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='Select Category']")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Private'])[1]")
        
        time.sleep(1)
        room_name = get_next_room_name()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Room Name'])[1]")
            )
        ).send_keys(room_name)

        print(f"🏨 Room created: {room_name}")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//p-dropdown[@formcontrolname='roomNature']")

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='Room']")

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "(//button[normalize-space()='Create'])[1]")
    
        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(3)

        wait_and_locate_click(driver, By.XPATH, "(//*[contains(@class,'btnView_IP_RmGrd')])[1]")

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//*[@id='btnCreateBed_IP_RmDet']")

        wait_and_locate_click(driver, By.XPATH, "//p-dropdown[@id='selectResrv_IP_BedCrt']")

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//li[@aria-label='Yes']"
        )

        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//p-dropdown[@id='selectBed_IP_BedCrt']")


        bed_type = driver.find_element(By.XPATH, "//span[normalize-space()='Normal']")
        scroll_to_element(driver, bed_type)
        bed_type.click()

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='selectBedCat_IP_BedCrt']"
        )

        bed_cat = driver.find_element(By.XPATH, "//span[normalize-space()='Observation']")
        scroll_to_element(driver, bed_cat)
        bed_cat.click()
        
        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='selectBedPrice_IP_BedCrt']"
        )

        bed_price = driver.find_element(By.XPATH, "//span[normalize-space()='Normal Bed']")
        scroll_to_element(driver, bed_price)
        bed_price.click()

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
        time.sleep(3)

        wait_and_locate_click(
             driver, By.XPATH, "//i[@class='pi pi-arrow-left']"
        )


        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "//i[@class='pi pi-arrow-left']"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "//i[@class='pi pi-arrow-left']"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "//i[@class='pi pi-arrow-left']"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//img)[5]"
        )
        
        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[3]"
        )
        
        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[.//span[normalize-space()='New Reservation']]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnCreatePatient_IP_NA_NA']"
        )

        time.sleep(1)

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
        wait_and_locate_click(login, By.XPATH, "(//p-dropdown[@placeholder='Select Gender'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Male'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space()='Save & Next'])[1]")

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
        wait_and_locate_click(login, By.XPATH, "(//p-dropdown[@placeholder='Select Admitted Doctor'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Venu Gopal']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]")

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
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

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
        wait_and_locate_click(login, By.XPATH, "(//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='p-checkbox-box'])[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Select Building']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block D'])[1]")

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"
        )

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//*[@id='btnReserveNow_IP_NA_NA']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(3)



    except Exception as e:
                        allure.attach(  # use Allure package, .attach() method, pass 3 params
                            driver.get_screenshot_as_png(),  # param1
                            # driver.screenshot()
                            name="full_page",  # param2
                            attachment_type=AttachmentType.PNG,
                        )
                        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Diet Item Creation, updation, Status")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_16(login):
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(5)
        
        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(3)         
        wait_and_locate_click(
               driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[9]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "(//div[contains(text(),'Diet Items')])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCrtItem_ORD_Items']"
        )

        diet_item_name = "DietItem_" + str(uuid.uuid4())[:4]
        print("DietItem Name", diet_item_name)
        wait_and_send_keys(
               driver, By.XPATH, "//input[@id='inpItemName_ORD_INV_ItemCreate']", diet_item_name
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "//p-dropdown[@id='ddCategory_ORD_INV_ItemCreate']"
        )

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

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnSubmit_ORD_INV_ItemCreate']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
              driver, By.XPATH, "(//button[normalize-space()='Actions'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnEdtItem_ORD_ItemList']"
        )

        time.sleep(1)
        diet_item_rename = "DietItem_Rename_" + str(uuid.uuid4())[:4]
        print("DietItem Rename", diet_item_rename)

        itemname_element = driver.find_element(By.XPATH, "//input[@id='inpItemName_ORD_INV_ItemCreate']")

        itemname_element.click()
        time.sleep(1)
        itemname_element.clear()

        time.sleep(1)
        itemname_element.send_keys(diet_item_rename)

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnSubmit_ORD_INV_ItemCreate']"
        )

        msg = get_toast_message(driver)
        print("Toast Message:", msg)
        time.sleep(2)

        wait_and_locate_click(
              driver, By.XPATH, "(//button[normalize-space()='Actions'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnStsCng_ORD_ItemList']"
        ) 

        msg = get_toast_message(driver)
        print("Toast Message:", msg)
        time.sleep(2) 


        time.sleep(2)
        status_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//tbody//tr[1]//span[contains(@class,'status-Disable')]")
            )
        )

        status_text = status_element.text.strip()

        assert status_text == "Disable", f"Expected 'Disable' but got '{status_text}'"

        print("Status verified:", status_text)

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "(//button[normalize-space()='Actions'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnStsCng_ORD_ItemList']"
        )

        msg = get_toast_message(driver)
        print("Toast Message:", msg)
        time.sleep(2) 

        status_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//tbody/tr)[1]//span[contains(@class,'status')]")
            )
        )

        status_text = status_element.text.strip()

        assert status_text == "Enable", f"Expected 'Enable' but got '{status_text}'"

        print("✅ First row status:", status_text)

        time.sleep(2)

    except Exception as e:
                    allure.attach(  # use Allure package, .attach() method, pass 3 params
                        driver.get_screenshot_as_png(),  # param1
                        # driver.screenshot()
                        name="full_page",  # param2
                        attachment_type=AttachmentType.PNG,
                    )
                    raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Diet Plan Creation, updation, Status")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_17(login):
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(5)
        
        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(3)         
        wait_and_locate_click(
               driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[9]"
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "//div[@id='actionNav_IP_ktcAnlDshBrd']"
        )

        time.sleep(2)

        diet_plan_name = "DietPlan_" + str(uuid.uuid4())[:4]
        print("DietPlan Name", diet_plan_name)

        wait_and_send_keys(
              driver, By.XPATH, "//input[@id='inputTName_IP_ktcAnlDietCrt']", diet_plan_name
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "//p-dropdown[@id='selectUser_IP_ktcAnlDietCrt']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//span[normalize-space()='Venu Gopal']"
        )

        time.sleep(1)
        wait_and_send_keys(
              driver, By.XPATH, "//input[@id='inputPps_IP_ktcAnlDietCrt']", "WL"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnSave_IP_ktcAnlDietCrt']"
        )
        # msg = get_toast_message(driver)
        # print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnAddDay_IP_ktcAnlDietDet']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnAdMeal_IP_ktcAnlDietDet']"
        )


        wait_and_locate_click(
              driver, By.XPATH, "//*[@id='selectMeal_IP_ktcAnlAdMeal']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "(//span[normalize-space()='Breakfast'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnSave_IP_ktcAnlAdMeal']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnAddItem_IP_ktcAnlDietDet']"
        )

        diet_item_name = "DietItem_" + str(uuid.uuid4())[:4]
        print("DietItem Name", diet_item_name)
        wait_and_send_keys(
              driver, By.XPATH, "(//input[@role='searchbox'])[1]", diet_item_name
        )
        
        calorie = random.randint(100, 500)   
        protein = random.randint(5, 50)      
        carbs = random.randint(10, 100)     
        fat = random.randint(1, 40)


        print("Calories:", calorie)
        print("Protein:", protein)
        print("Carbs:", carbs)
        print("Fat:", fat)

        calorie_element = driver.find_element(By.XPATH, "//input[@i='inputCal_IP_ktcAnlDietDet']")
        calorie_element.click()
        time.sleep(1)
        calorie_element.clear()
        calorie_element.send_keys(calorie)

        time.sleep(2)

        carbs_element = driver.find_element(By.XPATH, "(//input[@id='inputCarb_IP_ktcAnlDietDet'])[1]")
        carbs_element.click()
        time.sleep(1)
        carbs_element.clear()
        carbs_element.send_keys(carbs)

        time.sleep(2)

        protein_element = driver.find_element(By.XPATH, "(//input[@id='inputProt_IP_ktcAnlDietDet'])[1]")
        protein_element.click()
        time.sleep(1)
        protein_element.clear()
        protein_element.send_keys(protein)

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnAdMeal_IP_ktcAnlDietDet']"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//*[@id='selectMeal_IP_ktcAnlAdMeal']"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "(//span[normalize-space()='Lunch'])[1]"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnSave_IP_ktcAnlAdMeal']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "(//button[@id='btnAddItem_IP_ktcAnlDietDet'])[2]"
        )

        time.sleep(1)

        diet_item_name = "DietItem_" + str(uuid.uuid4())[:4]
        print("DietItem Name", diet_item_name)

        wait_and_send_keys(
              driver, By.XPATH, "(//input[@role='searchbox'])[1]", diet_item_name
        )

        time.sleep(2)

        calorie_element = driver.find_element(By.XPATH, "(//input[@i='inputCal_IP_ktcAnlDietDet'])[last()]")
        calorie_element.click()
        time.sleep(1)
        calorie_element.clear()
        calorie_element.send_keys(calorie)

        time.sleep(2)

        carbs_element = driver.find_element(By.XPATH, "(//input[@id='inputCarb_IP_ktcAnlDietDet'])[last()]")
        carbs_element.click()
        time.sleep(1)
        carbs_element.clear()
        carbs_element.send_keys(carbs)


        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnAdMeal_IP_ktcAnlDietDet']"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//*[@id='selectMeal_IP_ktcAnlAdMeal']"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "(//span[normalize-space()='Dinner'])[1]"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnSave_IP_ktcAnlAdMeal']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "(//button[@id='btnAddItem_IP_ktcAnlDietDet'])[3]"
        )

        time.sleep(1)

        diet_item_name = "DietItem_" + str(uuid.uuid4())[:4]
        print("DietItem Name", diet_item_name)

        wait_and_send_keys(
              driver, By.XPATH, "(//input[@role='searchbox'])[1]", diet_item_name
        )

        time.sleep(2)
        calorie_element = driver.find_element(By.XPATH, "(//input[@i='inputCal_IP_ktcAnlDietDet'])[last()]")
        calorie_element.click()
        time.sleep(1)
        calorie_element.clear()
        calorie_element.send_keys(calorie)

        time.sleep(2)

        carbs_element = driver.find_element(By.XPATH, "(//input[@id='inputCarb_IP_ktcAnlDietDet'])[last()]")
        carbs_element.click()
        time.sleep(1)
        carbs_element.clear()
        carbs_element.send_keys(carbs)

        time.sleep(2)

        protein_element = driver.find_element(By.XPATH, "(//input[@id='inputProt_IP_ktcAnlDietDet'])[last()]")
        protein_element.click()
        time.sleep(1)
        protein_element.clear()
        protein_element.send_keys(protein)

        time.sleep(2)

        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnSave_IP_ktcAnlDietCrt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message:", msg)
        time.sleep(2)

        wait_and_locate_click(
              driver, By.XPATH, "(//button[@id='btnActMenu_IP_ktcAnlDietTmplt'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnMngEdt_IP_ktcAnlDietTmplt']"
        )

        diet_plan_rename = "DietPlan_rename" + str(uuid.uuid4())[:4]
        print("DietPlan Name", diet_plan_rename)

        planname_text = driver.find_element(By.XPATH, "//input[@id='inputTName_IP_ktcAnlDietCrt']")
        planname_text.click()
        time.sleep(1)
        planname_text.clear()
        planname_text.send_keys(diet_plan_rename)

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnSave_IP_ktcAnlDietCrt']"
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnSave_IP_ktcAnlDietCrt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message:", msg)
        time.sleep(2)

        wait_and_locate_click(
              driver, By.XPATH, "(//button[@id='btnActMenu_IP_ktcAnlDietTmplt'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnCngSts_IP_ktcAnlDietTmplt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message:", msg)
        time.slepe(2)

        inactive_xpath = (
            "(//tr[contains(@class,'ng-star-inserted')]//td[5]//span[contains(normalize-space(.),'Inactive')])[1]"
        ) 

        try:
            is_inactive = driver.find_element(By.XPATH, inactive_xpath).is_displayed()
        except Exception:
            is_inactive = False

        print("ASSERT Inactive status :", is_inactive)
        assert is_inactive, "Inactive status not displayed"


        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "(//button[@id='btnActMenu_IP_ktcAnlDietTmplt'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//button[@id='btnCngSts_IP_ktcAnlDietTmplt']"
        )

        msg = get_toast_message(driver)
        print("Toast Message:", msg)
        time.slepe(2)

        active_xpath = (
            "(//tr[contains(@class,'ng-star-inserted')]//td[5]//span[contains(normalize-space(.),'Active')])[1]"
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
                        driver.get_screenshot_as_png(),  # param1
                        # driver.screenshot()
                        name="full_page",  # param2
                        attachment_type=AttachmentType.PNG,
                    )
                    raise e