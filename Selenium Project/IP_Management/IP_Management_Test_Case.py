from Framework.common_utils import *
from Framework.common_dates_utils import *
import random
from faker import Faker





@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: IP New admission is created for existing patient")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_1(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        #Room
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

        wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='Normal']")

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
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[1]"
        )

        time.sleep(1)

        wait_and_send_keys(
             driver, By.XPATH, "//*[@id='inputSrch_IP_Search']", "5556413113"
        )

        wait_and_locate_click(
             driver, By.XPATH, "//span[normalize-space()='Id : 1']"
        )

        time.sleep(1)
        admission_dropdown = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//p-dropdown[@placeholder='Select Admission Type']")
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
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Select Admitted Doctor']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Venu Gopal']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]")
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

        print("future day: ", future_day)
        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 10  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
        else:
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # ✅ Click the future day but only inside the correct month/year panel
        date_xpath = (
        f"//td[not(contains(@class,'p-disabled')) "
        f"and not(contains(@class,'p-datepicker-other-month'))]"
        f"//span[normalize-space()='{future_day}']"
        )

        target_date = wait.until(EC.element_to_be_clickable((By.XPATH, date_xpath)))
        login.execute_script("arguments[0].click();", target_date)
        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-multiselect[@placeholder='Select Assignee Doctor']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='p-checkbox-box'])[2]")                                                                                                                                            
    
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Select Building']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block D'])[1]")

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "//button[@id='btnAdmitNow_IP_NA_NA']")

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
@allure.title("Test Case: IP New admission for new patient")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_2(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        #Room
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

        wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='Normal']")

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
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[1]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCreatePatient_IP_NA_NA']"
        )

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

        time.sleep(1)
        admission_dropdown = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//p-dropdown[@placeholder='Select Admission Type']")
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
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Select Admitted Doctor']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Venu Gopal']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]")
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

        print("future day: ", future_day)
        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 10  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
        else:
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # ✅ Click the future day but only inside the correct month/year panel
        date_xpath = (
        f"//td[not(contains(@class,'p-disabled')) "
        f"and not(contains(@class,'p-datepicker-other-month'))]"
        f"//span[normalize-space()='{future_day}']"
        )

        target_date = wait.until(EC.element_to_be_clickable((By.XPATH, date_xpath)))
        login.execute_script("arguments[0].click();", target_date)
        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-multiselect[@placeholder='Select Assignee Doctor']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='p-checkbox-box'])[2]")                                                                                                                                            
    
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Select Building']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block D'])[1]")

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "//button[@id='btnAdmitNow_IP_NA_NA']")

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
@allure.title("Test Case: IP New admission from patient tab")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_3(login):
        
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

        wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='Normal']")

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
            driver, By.XPATH, "(//img)[7]"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//span[@class='p-button-label ng-star-inserted'][normalize-space()='Add New'])[1]"
        )

        wait_and_locate_click(
             driver, By.XPATH, "(//img[@alt='add Patient'])[1]"
        )

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
        wait_and_locate_click(login, By.XPATH, "(//label[normalize-space()='Male'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Save'])[1]")

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//p-button[contains(@class,'more-btn')])[1]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//span[normalize-space()='Create IP Admission']"
        )

        time.sleep(2)

        admission_dropdown = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//p-dropdown[@placeholder='Select Admission Type']")
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
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Select Admitted Doctor']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Venu Gopal']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]")
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

        print("future day: ", future_day)
        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 10  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
        else:
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # ✅ Click the future day but only inside the correct month/year panel
        date_xpath = (
        f"//td[not(contains(@class,'p-disabled')) "
        f"and not(contains(@class,'p-datepicker-other-month'))]"
        f"//span[normalize-space()='{future_day}']"
        )

        target_date = wait.until(EC.element_to_be_clickable((By.XPATH, date_xpath)))
        login.execute_script("arguments[0].click();", target_date)
        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-multiselect[@placeholder='Select Assignee Doctor']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='p-checkbox-box'])[2]")                                                                                                                                            
    
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Select Building']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block D'])[1]")

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "//button[@id='btnAdmitNow_IP_NA_NA']")

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
@allure.title("Test Case: IP New admission from convert ip patient")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_4(login):
        
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

        time.sleep(1)
        wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='Normal']")

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
            driver, By.XPATH, "(//img)[3]"
        )

        time.sleep(2)
      
        wait_and_click(login, By.XPATH, "(//div[@id='actionCreate_BUS_bookList'])[1]")
        
        time.sleep(3)
        print("Create new patient")
       
        wait_and_click(login, By.XPATH, "(//span[@id='btnCreateCust_BUS_appt'])[1]")
        
        login.implicitly_wait(3)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        wait_and_send_keys(login, By.XPATH, "//input[@id='first_name']", str(first_name))
        wait_and_send_keys(login, By.XPATH, "//input[@id='last_name']", str(last_name))
        # wait_and_send_keys(login, By.XPATH, "//*[@id='customer_id']", cons_manual_id)
        wait_and_send_keys(login, By.XPATH, "//*[@id='phone']", phonenumber)
        wait_and_send_keys(login, By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']", phonenumber)
        wait_and_send_keys(login, By.XPATH, "//input[@id='email_id']", email)
        wait_and_locate_click(driver, By.XPATH, "//label[normalize-space()='Male']")
        wait_and_click(login, By.XPATH, "//span[contains(text(),'Save')]")

        time.sleep(3)

        confirm_element = driver.find_element(By.XPATH, "//button[@id='btnConfirm_BUS_apptForm']")
        scroll_to_element(driver, confirm_element)
        time.sleep(2)
        confirm_element.click()

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
                else:
                  
                    break

            except Exception as e:
                
                break

        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(3)
        View_Detail_button = WebDriverWait(login, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")
            )
        )
        click_to_element(login, View_Detail_button)

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCovertIp_BUS_bookAction']"
        )

        time.sleep(2)

        admission_dropdown = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//p-dropdown[@placeholder='Select Admission Type']")
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
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Select Admitted Doctor']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Venu Gopal']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]")
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

        print("future day: ", future_day)
        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 10  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
        else:
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # ✅ Click the future day but only inside the correct month/year panel
        date_xpath = (
        f"//td[not(contains(@class,'p-disabled')) "
        f"and not(contains(@class,'p-datepicker-other-month'))]"
        f"//span[normalize-space()='{future_day}']"
        )

        target_date = wait.until(EC.element_to_be_clickable((By.XPATH, date_xpath)))
        login.execute_script("arguments[0].click();", target_date)
        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-multiselect[@placeholder='Select Assignee Doctor']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//div[@class='p-checkbox-box'])[2]")                                                                                                                                            
    
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//p-dropdown[@placeholder='Select Building']")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block D'])[1]")

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "//button[@id='btnAdmitNow_IP_NA_NA']")

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
@allure.title("Test Case: Update the admission")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_5(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
             driver, By.XPATH, "(//img)[5]"
        )

        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "(//button[@id='btnSts_IP_IpGrd'])[1]"
        )

        time.sleep(1)

        wait_and_locate_click(
              driver, By.XPATH, "//*[@id='btnEdtAd_IP_IpGrd']"
        )

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        time.sleep(2)
        future_date = datetime.now() + timedelta(days=3)
        future_day = str(future_date.day)
        future_month = future_date.strftime("%B")
        future_year = str(future_date.year)

        print("future day: ", future_day)
        # Get the "next month" arrow
        next_month_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='p-datepicker-next-icon p-icon'])[1]"))
        )

        # Loop until the correct month and year is visible
        max_tries = 10  # Prevent infinite loop
        for _ in range(max_tries):
            month_elem = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-month')]"))
            )
            year_elem = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'p-datepicker-title')]/button[contains(@class, 'p-datepicker-year')]"))
            )

            current_month = month_elem.text.strip()
            current_year = year_elem.text.strip()

            if current_month == future_month and current_year == future_year:
                break

            next_month_arrow.click()
            time.sleep(1)
        else:
            raise Exception("❌ Could not navigate to the target date in calendar.")

        # ✅ Click the future day but only inside the correct month/year panel
        date_xpath = (
        f"//td[not(contains(@class,'p-disabled')) "
        f"and not(contains(@class,'p-datepicker-other-month'))]"
        f"//span[normalize-space()='{future_day}']"
        )

        target_date = wait.until(EC.element_to_be_clickable((By.XPATH, date_xpath)))
        login.execute_script("arguments[0].click();", target_date)
        print(f"✅ Selected future date: {future_day}-{future_month}-{future_year}")

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnAdmitNow_IP_NA_NA']"
        )

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
@allure.title("Test Case: IP patient is updated from Inpatient Menu")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_6(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
             driver, By.XPATH, "(//img)[5]"
        )

        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "(//button[@id='btnSts_IP_IpGrd'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnEdt_IP_IpGrd']"
        )

        time.sleep(2)

        login.implicitly_wait(3)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        patient_number = driver.find_element(By.XPATH, "//*[@id='phone']")
        patient_number.click()
        patient_number.clear()
        time.sleep(1)
        patient_number.send_keys(phonenumber)
        
        wait_and_click(login, By.XPATH, "//*[normalize-space()='Update']")

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
@allure.title("Test Case: Reservation is created without selecting a bed")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_7(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)


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

        time.sleep(1)
        wait_and_send_keys(
             driver, By.XPATH, "//input[@id='inputSrch_IP_Search']", "555"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//span[normalize-space()='Id : 1']"
        )

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
        wait_and_locate_click(login, By.XPATH, "//button[@id='btnReserveNow_IP_NA_NA']")

        msg = get_toast_message(login)
        print("Toas Message :", msg)
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
@allure.title("Test Case: Reservation created and bed is selected")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_8(login):
        
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

        time.sleep(1)
        wait_and_send_keys(
             driver, By.XPATH, "//input[@id='inputSrch_IP_Search']", "555"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//span[normalize-space()='Id : 1']"
        )

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
@allure.title("Test Case: Reservation created for a new patient without selecting bed")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_9(login):
        
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
@allure.title("Test Case: Reservation created for new patient with bed selection")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_10(login):
        
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