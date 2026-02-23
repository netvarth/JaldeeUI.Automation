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
        
        time.sleep(2)
        wait_and_locate_click(driver, By.XPATH, "//span[normalize-space()='Normal']")

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "//*[@id='selectBedCat_IP_BedCrt']"
        )

        time.sleep(1)
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

        time.sleep(2)
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

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(1)
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
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: A new visit is created for the patient")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_11(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
             driver, By.XPATH, "(//img)[5]"
        )
        
        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "(//button[@label='View'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnQuickAction_IP_AD_DE_New_medical-record']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//*[@id='btnAddVisit_IP_VL_VL']"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//p-multiselect[@placeholder='Select Doctors']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//span[normalize-space()='Venu Gopal']"
        )


        wait_and_locate_click(
              driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//button[normalize-space()='Add Visit']"
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
@allure.title("Test Case: Update the visit")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_12(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
             driver, By.XPATH, "(//img)[5]"
        )
        
        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "(//button[@label='View'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnQuickAction_IP_AD_DE_New_medical-record']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//*[@id='btnAddVisit_IP_VL_VL']"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//p-multiselect[@placeholder='Select Doctors']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//span[normalize-space()='Venu Gopal']"
        )


        wait_and_locate_click(
              driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//button[normalize-space()='Add Visit']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//*[contains(@class,'btnEditVisit_IP_VL_VL')]"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//p-multiselect[@placeholder='Select Doctors']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Vijay Kumar']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//button[normalize-space()='Update Visit']"
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
@allure.title("Test Case: Create prescription in Medical Record")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_13(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
             driver, By.XPATH, "(//img)[5]"
        )
        
        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "(//button[@label='View'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnQuickAction_IP_AD_DE_New_medical-record']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//*[@id='btnAddVisit_IP_VL_VL']"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//p-multiselect[@placeholder='Select Doctors']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//span[normalize-space()='Venu Gopal']"
        )


        wait_and_locate_click(
              driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//button[normalize-space()='Add Visit']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//*[contains(@class,'btnSelectSection_IP_VL_VL')])[10]"
        )

        for i in range(5):
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='+ Add Medicine']")
            wait_and_send_keys( login, By.XPATH, "//input[@role='searchbox']", "Medicine")

            before_XPath = "//*[contains(@id, 'pr_id')]/tbody/tr"
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
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
        
        msg = get_toast_message(driver)
        print("Toast Message :", msg )

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
@allure.title("Test Case: Prescription created from choosing a template")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_14(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
             driver, By.XPATH, "(//img)[5]"
        )
        
        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "(//button[@label='View'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnQuickAction_IP_AD_DE_New_medical-record']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//*[@id='btnAddVisit_IP_VL_VL']"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//p-multiselect[@placeholder='Select Doctors']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//span[normalize-space()='Venu Gopal']"
        )


        wait_and_locate_click(
              driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//button[normalize-space()='Add Visit']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//*[contains(@class,'btnSelectSection_IP_VL_VL')])[10]"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//button[normalize-space()='Choose RX Template']"
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "//button[normalize-space()='Use']"
        )

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
        
        msg = get_toast_message(driver)
        print("Toast Message :", msg )

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
@allure.title("Test Case: Update prescription")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_15(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
             driver, By.XPATH, "(//img)[5]"
        )
        
        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "(//button[@label='View'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnQuickAction_IP_AD_DE_New_medical-record']"
        )

        time.sleep(2)
        dropdown = driver.find_element(By.XPATH, "(//img[@alt='dropdown'])[1]")

        scroll_to_element(driver, dropdown)
        time.sleep(2)
        dropdown.click()

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Edit'])[1]"
        )

        time.sleep(1)

        for i in range(2):
            login.find_element(
                By.XPATH, "//button[normalize-space()='+ Add Medicine']"
            ).click()
            login.find_element(By.XPATH, "//input[@role='searchbox']").send_keys("Medicine")

            before_XPath = "//*[contains(@id, 'pr_id')]/tbody/tr"
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

        wait_and_locate_click(
               driver, By.XPATH, "(//button[normalize-space()='Save'])[1]"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//i[@class='pi pi-times'])[1]"
        )

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
@allure.title("Test Case: Share prescription from Medical Record")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_16(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
             driver, By.XPATH, "(//img)[5]"
        )
        
        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "(//button[@label='View'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnQuickAction_IP_AD_DE_New_medical-record']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//*[@id='btnAddVisit_IP_VL_VL']"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//p-multiselect[@placeholder='Select Doctors']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//span[normalize-space()='Venu Gopal']"
        )


        wait_and_locate_click(
              driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//button[normalize-space()='Add Visit']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//*[contains(@class,'btnSelectSection_IP_VL_VL')])[10]"
        )

        for i in range(5):
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='+ Add Medicine']")
            wait_and_send_keys( login, By.XPATH, "//input[@role='searchbox']", "Medicine")

            before_XPath = "//*[contains(@id, 'pr_id')]/tbody/tr"
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
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
        
        msg = get_toast_message(driver)
        print("Toast Message :", msg )

        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//span[contains(text(),'Share')])[1]"
        )
        time.sleep(2)

        wait_and_send_keys(
               driver, By.XPATH, "(//textarea[@placeholder='Enter message description'])[1]", "Message to the Patient"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Email'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Whatsapp'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//button[normalize-space()='Share'])[1]"
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
@allure.title("Test Case: Thrid party Share prescription from Medical Record")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_17(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
             driver, By.XPATH, "(//img)[5]"
        )
        
        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "(//button[@label='View'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnQuickAction_IP_AD_DE_New_medical-record']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//*[@id='btnAddVisit_IP_VL_VL']"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//p-multiselect[@placeholder='Select Doctors']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//span[normalize-space()='Venu Gopal']"
        )


        wait_and_locate_click(
              driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//button[normalize-space()='Add Visit']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//*[contains(@class,'btnSelectSection_IP_VL_VL')])[10]"
        )

        for i in range(5):
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='+ Add Medicine']")
            wait_and_send_keys( login, By.XPATH, "//input[@role='searchbox']", "Medicine")

            before_XPath = "//*[contains(@id, 'pr_id')]/tbody/tr"
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
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
        
        msg = get_toast_message(driver)
        print("Toast Message :", msg )

        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//span[contains(text(),'Share')])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//mat-select[@placeholder='Share with whom']"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//div[normalize-space()='Others'])[1]"
        )

        wait_and_send_keys(
               driver, By.XPATH, "(//textarea[@placeholder='Enter message description'])[1]", "Message to the Patient"
        )

        element_1 = driver.find_element(By.XPATH, "(//label[normalize-space()='Email'])[1]")
        element_1.click()

        time.sleep(1)
        wait_and_send_keys(
               driver, By.XPATH, "(//input[@id='thirdpartyemail'])[1]", "test@jaldee.com"
        )


        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//button[normalize-space()='Share'])[1]"
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
@allure.title("Test Case: Rx is pushed to the store")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_18(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)


        wait_and_locate_click(
               driver, By.XPATH, "(//a[@class='menu-link menu-toggle'])[10]"
        )

        time.sleep(2)

        element1 = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, element1)

        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "//li//span[contains(normalize-space(), 'RX Push')]"
        )

        time.sleep(1)
        toggle = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']"))
        )

        is_enabled = toggle.get_attribute("aria-checked")

        if is_enabled == "false":
            toggle.click()
            print("Toggle was OFF. Now turned ON.")
        else:
            print("Toggle already ON. No action taken.")


        # msg = get_snack_bar_message(driver)
        # print("Snack Bar Message :", msg)

        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "(//img)[5]"
                    )
        
        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "(//button[@label='View'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnQuickAction_IP_AD_DE_New_medical-record']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//*[@id='btnAddVisit_IP_VL_VL']"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//p-multiselect[@placeholder='Select Doctors']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//span[normalize-space()='Venu Gopal']"
        )


        wait_and_locate_click(
              driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//button[normalize-space()='Add Visit']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//*[contains(@class,'btnSelectSection_IP_VL_VL')])[10]"
        )

        for i in range(5):
            
            # Click + Add Medicine
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='+ Add Medicine']")

            # Wait for the newly added last row
            row = WebDriverWait(login, 15).until(
                EC.presence_of_element_located((By.XPATH, "//tbody/tr[last()]"))
            )

            # ----------------------------
            # Select Medicine Name
            # ----------------------------
            search_box = row.find_element(By.XPATH, ".//td[2]//input[@role='searchbox']")
            search_box.clear()
            search_box.send_keys("Med")

            medicines = WebDriverWait(login, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//ul[@role='listbox']//li[@role='option']")
                )
            )

            medicines[i % len(medicines)].click()

            # ----------------------------
            # Dosage
            # ----------------------------
            dosage = row.find_element(By.XPATH, ".//td[3]//input[@type='text']")
            dosage.clear()
            dosage.send_keys("650")

            # ----------------------------
            # Frequency Dropdown
            # ----------------------------
            dropdown_trigger = row.find_element(
                By.XPATH, ".//td[4]//div[contains(@class,'p-dropdown-trigger')]"
            )
            dropdown_trigger.click()

            dropdown_options = WebDriverWait(login, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//div[contains(@class,'p-dropdown-items-wrapper')]//li")
                )
            )

            option = random.choice(dropdown_options)
            login.execute_script("arguments[0].click();", option)

            # ----------------------------
            # Duration
            # ----------------------------
            duration = row.find_element(By.XPATH, ".//td[5]//input[@type='number']")
            duration.clear()
            duration.send_keys("5")

            # ----------------------------
            # Quantity
            # ----------------------------
            qty_input = row.find_element(By.XPATH, ".//td[6]//input[@type='number']")
            qty_input.clear()
            qty_input.send_keys("1")

            # ----------------------------
            # Remarks (Correct Column = td[7])
            # ----------------------------
            remarks_cell = row.find_element(By.XPATH, ".//td[7]")
            login.execute_script("arguments[0].scrollIntoView(true);", remarks_cell)
            remarks_cell.click()

            remarks_input = WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[7]//input"))
            )

            remarks_input.clear()
            remarks_input.send_keys("Notes for Patient")


        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Create Prescription']")

        msg = get_toast_message(driver)
        print("Toast Message:", msg)
        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//img[@alt='dropdown'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Push RX'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//div[normalize-space()='Swathi Medical']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//button[normalize-space()='Push']"
        )

        msg =  get_toast_message(driver)
        print("Toast Message : ", msg)
        time.sleep(2)

        status = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((
                By.XPATH,
                "(//tbody[contains(@class,'p-datatable-tbody')]//tr)[1]//span[normalize-space()='Pushed']"
            ))
        )

        assert status.text.strip() == "Pushed", "First row status is not Pushed"


        wait_and_locate_click(
               driver, By.XPATH, "(//img)[6]"
        )   

        time.sleep(2)
        element2 = driver.find_element(By.XPATH, "//div[@class='heading']")
        scroll_to_element(driver, element2)

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnRXReq_ORD_Dashbrd']"
        )


        status_element = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((
                By.XPATH,
                "(//tbody[contains(@class,'p-datatable-tbody')]//tr)[1]/td[5]//span"
            ))
        )

        actual_status = status_element.text.strip()

        assert actual_status == "Pushed", f"Expected 'Pushed' but got '{actual_status}'"


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
@allure.title("Test Case: Cancel the prescription")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_19(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
             driver, By.XPATH, "(//img)[5]"
        )
        
        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "(//button[@label='View'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnQuickAction_IP_AD_DE_New_medical-record']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//*[@id='btnAddVisit_IP_VL_VL']"
        )

        time.sleep(1)
        wait_and_locate_click(
              driver, By.XPATH, "//p-multiselect[@placeholder='Select Doctors']"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//span[normalize-space()='Venu Gopal']"
        )


        wait_and_locate_click(
              driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"
        )

        wait_and_locate_click(
              driver, By.XPATH, "//button[normalize-space()='Add Visit']"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//*[contains(@class,'btnSelectSection_IP_VL_VL')])[10]"
        )

        for i in range(5):
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='+ Add Medicine']")
            wait_and_send_keys( login, By.XPATH, "//input[@role='searchbox']", "Medicine")

            before_XPath = "//*[contains(@id, 'pr_id')]/tbody/tr"
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
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
        
        msg = get_toast_message(driver)
        print("Toast Message :", msg )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//img[@alt='dropdown'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Cancel'])[1]"
        )

        wait_and_locate_click(
               driver, By.XPATH, "(//button[normalize-space()='Yes'])[1]"
        )

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        first_row = WebDriverWait(login, 15).until(
            EC.presence_of_element_located((By.XPATH, "//tbody/tr[1]"))
        )

        # Locate the status element inside first row
        status_element = first_row.find_element(
            By.XPATH, ".//span[contains(@class,'customer-badge')]"
        )

        # Get text
        status_text = status_element.text.strip().lower()

        # Assertion
        assert status_text == "cancelled", f"Expected 'cancelled' but got '{status_text}'"

        print("✅ Prescription status is cancelled") 

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
@allure.title("Test Case: Prescription template creation")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_20(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
             driver, By.XPATH, "(//img)[5]"
        )
        
        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "(//button[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnQuickAction_IP_AD_DE_New_medical-record']"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//*[contains(@class,'btnSelectSection_IP_VL_VL')])[10]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//button[normalize-space()='Choose RX Template'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//i[@class='fa fa-plus'])[1]"
        )

        Prescript_Tem_name = "Template_name" + str(uuid.uuid4().int)[:4]

        wait_and_send_keys(
               driver, By.XPATH, "//input[@placeholder='Enter Template Name']", Prescript_Tem_name
        )

        time.sleep(1)


        for i in range(5):

            # Click Add row
            wait_and_locate_click(login, By.XPATH, "//div[@class='add']")

            # Wait for last row
            row = WebDriverWait(login, 15).until(
                EC.presence_of_element_located((By.XPATH, "(//table[contains(@id,'pr_id')]//tbody/tr[last()])[2]"))
            )

            # =========================
            # Medicine Name
            # =========================
            med_cell = row.find_element(By.XPATH, "./td[1]")
            login.execute_script("arguments[0].click();", med_cell)

            med_input = WebDriverWait(row, 10).until(
                EC.visibility_of_element_located((By.XPATH, "./td[1]//textarea"))
            )
            med_input.clear()
            med_input.send_keys("Medicine")

            # =========================
            # Dose
            # =========================
            dose_cell = row.find_element(By.XPATH, "./td[2]")
            login.execute_script("arguments[0].click();", dose_cell)

            dose_input = WebDriverWait(row, 10).until(
                EC.visibility_of_element_located((By.XPATH, "./td[2]//textarea"))
            )
            dose_input.clear()
            dose_input.send_keys("650 mg")

            # =========================
            # Frequency
            # =========================
            freq_cell = row.find_element(By.XPATH, "./td[3]")
            login.execute_script("arguments[0].click();", freq_cell)

            freq_input = WebDriverWait(row, 10).until(
                EC.visibility_of_element_located((By.XPATH, "./td[3]//textarea"))
            )
            freq_input.clear()
            freq_input.send_keys("1-1-1")

            # =========================
            # Duration
            # =========================
            duration_cell = row.find_element(By.XPATH, "./td[4]")
            login.execute_script("arguments[0].click();", duration_cell)

            duration_input = WebDriverWait(row, 10).until(
                EC.visibility_of_element_located((By.XPATH, "./td[4]//textarea"))
            )
            duration_input.clear()
            duration_input.send_keys("5 Days")

            # =========================
            # Notes
            # =========================
            notes_cell = row.find_element(By.XPATH, "./td[5]")
            login.execute_script("arguments[0].click();", notes_cell)

            notes_input = WebDriverWait(row, 10).until(
                EC.visibility_of_element_located((By.XPATH, "./td[5]//textarea"))
            )
            notes_input.clear()
            notes_input.send_keys("After Food")

        # Save
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save Template']")

        msg = get_toast_message(login)
        print("Toast Message:", msg)


        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//button[contains(text(),'Use')])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//button[normalize-space()='Save']"
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
@allure.title("Test Case: Prescription template updation")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_21(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
             driver, By.XPATH, "(//img)[5]"
        )
        
        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "(//button[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnQuickAction_IP_AD_DE_New_medical-record']"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//*[contains(@class,'btnSelectSection_IP_VL_VL')])[10]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//button[normalize-space()='Choose RX Template'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[contains(text(),'Edit')])[1]"
        )

        time.sleep(2)
        Prescript_Tem_Rename = "Template_Rename" + str(uuid.uuid4().int)[:4]

        element_update = driver.find_element(By.XPATH, "//input[@placeholder='Enter Template Name']")
        element_update.click()
        time.sleep(1)
        element_update.clear()
        element_update.send_keys(Prescript_Tem_Rename)

        time.sleep(1)

        wait_and_locate_click(
               driver, By.XPATH, "//button[normalize-space()='Update Template']"
        )

        msg = get_snack_bar_message(driver)
        print("Snack Bar Message:", msg)
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
@allure.title("Test Case: Prescription template Deletion")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_22(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
             driver, By.XPATH, "(//img)[5]"
        )
        
        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "(//button[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//*[@id='btnQuickAction_IP_AD_DE_New_medical-record']"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//*[contains(@class,'btnSelectSection_IP_VL_VL')])[10]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//button[normalize-space()='Choose RX Template'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[contains(text(),'Delete')])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//button[normalize-space()='Yes']"
        )

        msg = get_toast_message(driver)
        print("Toast Message:", msg)
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
@allure.title("Test Case: Adding Single service to a patient")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_23(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//*[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//*[@id='btnAddService_IP_AD_DE_New']"
        )

        time.sleep(1)
        wait_and_send_keys(
               driver, By.XPATH, "//input[@placeholder='Search Service']", "Doc"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "//li[@role='option']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//p-multiselect[@placeholder='Select Doctors']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Venu Gopal']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//*[normalize-space()='Add Service']"
        )

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
@allure.title("Test Case: update the service")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_24(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//*[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Services'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[@class='service-action-dots'])[1]"
        )

        wait_and_locate_click(
               driver, By.XPATH, "(//i[@class='pi pi-pencil'])[1]"
        )

        time.sleep(2)
        service_element =  driver.find_element(By.XPATH, "(//input[@placeholder='Search Service'])[1]")
        service_element.click()
        service_element.clear()

        time.sleep(1)
        service_element.send_keys("s")

        time.sleep(1)
        options = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@role='listbox']//li[@role='option']")
            )
        )

        # Pick random option
        random_option = random.choice(options)

        # Scroll into view (optional but safe)
        driver.execute_script("arguments[0].scrollIntoView(true);", random_option)

        # Click it
        random_option.click()

        wait_and_locate_click(
               driver, By.XPATH, "//button[normalize-space()='Update Service']"
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
@allure.title("Test Case: Delete the service")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_25(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//*[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Services'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[@class='service-action-dots'])[1]"
        )

        wait_and_locate_click(
               driver, By.XPATH, "(//i[@class='pi pi-trash'])[1]"
        )

        wait_and_locate_click(
               driver, By.XPATH, "(//button[normalize-space()='Yes'])[1]"
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
@allure.title("Test Case: Create Recurrent Service")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_26(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//*[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Services'])[1]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnAddService_IP_AD_DE_New']"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "//div[normalize-space()='Recurrent']"
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

        time.sleep(1)
        duration_element = driver.find_element(By.XPATH, "//input[@placeholder='Duration (mins)']")
        duration_element.click()
        time.sleep(1)
        duration_element.clear()
        time.sleep(1)
        duration_element.send_keys("2")

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//div[contains(text(),'Select Doctors')]"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//li[@aria-label='Venu Gopal']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"
        )

        wait_and_locate_click(
               driver, By.XPATH, "(//button[normalize-space()='Next'])[1]"
        )

        time.sleep(2)

        service_element = driver.find_element(By.XPATH, "(//button[normalize-space()='Add Service'])[1]")
        scroll_to_element(driver, service_element)
        time.sleep(2)
        service_element.click()

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
@allure.title("Test Case: Update Recurrent Service")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_27(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//*[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Services'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnServiceTimestamp_IP_AD_DE_New_TOMMORROW']"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[@class='service-action-dots'])[1]"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//i[@class='pi pi-pencil']"
        )

        time.sleep(2)
        service_element =  driver.find_element(By.XPATH, "(//input[@placeholder='Search Service'])[1]")
        service_element.click()
        service_element.clear()

        time.sleep(1)
        service_element.send_keys("s")

        time.sleep(1)
        options = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@role='listbox']//li[@role='option']")
            )
        )

        # Pick random option
        random_option = random.choice(options)

        # Scroll into view (optional but safe)
        driver.execute_script("arguments[0].scrollIntoView(true);", random_option)

        # Click it
        random_option.click()

        wait_and_locate_click(
               driver, By.XPATH, "//button[normalize-space()='Update Service']"
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
@allure.title("Test Case: Delete Recurrent Service")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_28(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//*[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Services'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnServiceTimestamp_IP_AD_DE_New_TOMMORROW']"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[@class='service-action-dots'])[1]"
        )

        wait_and_locate_click(
               driver, By.XPATH, "(//i[@class='pi pi-trash'])[1]"
        )

        wait_and_locate_click(
               driver, By.XPATH, "(//button[normalize-space()='Yes'])[1]"
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
@allure.title("Test Case: Multiple deletion of single services")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_29(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//*[@id='btnViewIp_IP_IpGrd'])[1]"
        )
        LOOP_COUNT = 5

        for i in range(LOOP_COUNT):
            time.sleep(1)
            wait_and_locate_click(
                driver, By.XPATH, "//*[@id='btnAddService_IP_AD_DE_New']"
            )

            time.sleep(1)
            wait_and_send_keys(
                driver, By.XPATH, "//input[@placeholder='Search Service']", "Doc"
            )

            time.sleep(2)
            wait_and_locate_click(
                driver, By.XPATH, "//li[@role='option']"
            )

            wait_and_locate_click(
                driver, By.XPATH, "//p-multiselect[@placeholder='Select Doctors']"
            )

            wait_and_locate_click(
                driver, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Venu Gopal']"
            )

            wait_and_locate_click(
                driver, By.XPATH, "//*[normalize-space()='Add Service']"
            )

        time.sleep(3)
        wait_and_locate_click(
            driver, By.XPATH, "(//input[@id='chkSelectAllServices_IP_AD_DE_New-input'])[1]"   
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnRemoveServices_IP_AD_DE_New']"
        )

        msg = get_toast_message(driver)
        print("Toast Message:", msg)
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
@allure.title("Test Case: Multiple deletion of Recurrent services")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_30(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//*[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Services'])[1]"
        )

        LOOP_COUNT = 5

        for i in range(LOOP_COUNT):

            wait_and_locate_click(
                driver, By.XPATH, "//button[@id='btnAddService_IP_AD_DE_New']"
            )

            time.sleep(2)
            wait_and_locate_click(
                driver, By.XPATH, "//div[normalize-space()='Recurrent']"
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

            time.sleep(1)
            duration_element = driver.find_element(By.XPATH, "//input[@placeholder='Duration (mins)']")
            duration_element.click()
            time.sleep(1)
            duration_element.clear()
            time.sleep(1)
            duration_element.send_keys("2")

            time.sleep(1)
            wait_and_locate_click(
                driver, By.XPATH, "//div[contains(text(),'Select Doctors')]"
            )

            wait_and_locate_click(
                driver, By.XPATH, "//li[@aria-label='Venu Gopal']"
            )

            wait_and_locate_click(
                driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-multiselect-close-icon'])[1]"
            )

            wait_and_locate_click(
                driver, By.XPATH, "(//button[normalize-space()='Next'])[1]"
            )

            time.sleep(2)

            service_element = driver.find_element(By.XPATH, "(//button[normalize-space()='Add Service'])[1]")
            scroll_to_element(driver, service_element)
            time.sleep(2)
            service_element.click()

            msg = get_toast_message(driver)
            print("Toast Message :", msg)
            time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnServiceTimestamp_IP_AD_DE_New_TOMMORROW']"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//input[@id='chkSelectAllServices_IP_AD_DE_New-input'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnRemoveServices_IP_AD_DE_New']"
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
@allure.title("Test Case: Transferred to new bed without retaining old bed")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_31(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[6]"
        )

        room_name_1 = get_next_room_name()
        room_name_2 = get_next_room_name()

        print("Admission Room:", room_name_1)
        print("Transfer Room:", room_name_2)


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
        # room_name = get_next_room_name()
        room_name = room_name_1
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
        # room_name = get_next_room_name()
        room_name = room_name_2
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

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"
        )

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name_2}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "//button[@id='btnAdmitNow_IP_NA_NA']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//button[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnQuickAction_IP_AD_DE_New_transferBed']"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//p-dropdown[@id='selectbldn_IP_BedTfr']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block D'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Select Floor'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='1st floor'])[1]"
        )

        time.sleep(2)

        # Build bed name exactly same as created earlier
        bed_name = f"Bed{room_name_1}"

        print("Transferring to Bed:", bed_name)

        # Locate and click Select Bed button for that bed
        bed_xpath = f"""
        //span[contains(text(),'{bed_name}')]/ancestor::div[contains(@class,'bed-card')]
        //button[contains(@class,'btnSelectBed_IP_BedTfr')]
        """

        bed_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, bed_xpath))
        )

        bed_element.click()

        time.sleep(2)

        transfer_element = driver.find_element(By.XPATH, "//button[@id='btnSave_IP_BedTfr']")

        scroll_to_element(driver, transfer_element)
        transfer_element.click()

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        # wait_and_locate_click(
        #        driver, By.XPATH, "(//span[normalize-space()='Bed Transactions'])[1]"
        # )

        # time.sleep(1)
        # wa
    except Exception as e:
                    allure.attach(  # use Allure package, .attach() method, pass 3 params
                        driver.get_screenshot_as_png(),  # param1
                        # driver.screenshot()
                        name="full_page",  # param2
                        attachment_type=AttachmentType.PNG,
                    )
                    raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Transferred to new bed with retaining old bed")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_32(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[6]"
        )

        room_name_1 = get_next_room_name()
        room_name_2 = get_next_room_name()

        print("Admission Room:", room_name_1)
        print("Transfer Room:", room_name_2)


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
        # room_name = get_next_room_name()
        room_name = room_name_1
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
        # room_name = get_next_room_name()
        room_name = room_name_2
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

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"
        )

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name_2}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "//button[@id='btnAdmitNow_IP_NA_NA']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//button[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnQuickAction_IP_AD_DE_New_transferBed']"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//p-dropdown[@id='selectbldn_IP_BedTfr']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block D'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Select Floor'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='1st floor'])[1]"
        )

        time.sleep(2)

        # Build bed name exactly same as created earlier
        bed_name = f"Bed{room_name_1}"

        print("Transferring to Bed:", bed_name)

        # Locate and click Select Bed button for that bed
        bed_xpath = f"""
        //span[contains(text(),'{bed_name}')]/ancestor::div[contains(@class,'bed-card')]
        //button[contains(@class,'btnSelectBed_IP_BedTfr')]
        """

        bed_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, bed_xpath))
        )

        bed_element.click()

        time.sleep(2)
        retain_element = driver.find_element(By.XPATH, "(//label[normalize-space()='Yes'])[1]")
        
        scroll_to_element(driver, retain_element)
        time.sleep(2)
        retain_element.click()

        transfer_element = driver.find_element(By.XPATH, "//button[@id='btnSave_IP_BedTfr']")

        scroll_to_element(driver, transfer_element)
        time.sleep(2)
        transfer_element.click()

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
@allure.title("Test Case: Transfer from IP details page bed transcation section without retaining the old bed")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_33(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[6]"
        )

        room_name_1 = get_next_room_name()
        room_name_2 = get_next_room_name()

        print("Admission Room:", room_name_1)
        print("Transfer Room:", room_name_2)


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
        # room_name = get_next_room_name()
        room_name = room_name_1
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
        # room_name = get_next_room_name()
        room_name = room_name_2
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

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"
        )

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name_2}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "//button[@id='btnAdmitNow_IP_NA_NA']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//button[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Bed Transactions'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Transfer'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "//p-dropdown[@id='selectbldn_IP_BedTfr']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block D'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Select Floor'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='1st floor'])[1]"
        )

        time.sleep(2)

        # Build bed name exactly same as created earlier
        bed_name = f"Bed{room_name_1}"

        print("Transferring to Bed:", bed_name)

        # Locate and click Select Bed button for that bed
        bed_xpath = f"""
        //span[contains(text(),'{bed_name}')]/ancestor::div[contains(@class,'bed-card')]
        //button[contains(@class,'btnSelectBed_IP_BedTfr')]
        """

        bed_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, bed_xpath))
        )

        bed_element.click()

        time.sleep(2)

        transfer_element = driver.find_element(By.XPATH, "//button[@id='btnSave_IP_BedTfr']")

        scroll_to_element(driver, transfer_element)
        transfer_element.click()

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
@allure.title("Test Case: Transfer from IP details page bed transcation section by retaining the old bed")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_34(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[6]"
        )

        room_name_1 = get_next_room_name()
        room_name_2 = get_next_room_name()

        print("Admission Room:", room_name_1)
        print("Transfer Room:", room_name_2)


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
        # room_name = get_next_room_name()
        room_name = room_name_1
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
        # room_name = get_next_room_name()
        room_name = room_name_2
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

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"
        )

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name_2}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "//button[@id='btnAdmitNow_IP_NA_NA']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//button[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Bed Transactions'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Transfer'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "//p-dropdown[@id='selectbldn_IP_BedTfr']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block D'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Select Floor'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='1st floor'])[1]"
        )

        time.sleep(2)

        # Build bed name exactly same as created earlier
        bed_name = f"Bed{room_name_1}"

        print("Transferring to Bed:", bed_name)

        # Locate and click Select Bed button for that bed
        bed_xpath = f"""
        //span[contains(text(),'{bed_name}')]/ancestor::div[contains(@class,'bed-card')]
        //button[contains(@class,'btnSelectBed_IP_BedTfr')]
        """

        bed_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, bed_xpath))
        )

        bed_element.click()

        time.sleep(2)
        retain_element = driver.find_element(By.XPATH, "(//label[normalize-space()='Yes'])[1]")
        
        scroll_to_element(driver, retain_element)
        time.sleep(2)
        retain_element.click()

        time.sleep(2)

        transfer_element = driver.find_element(By.XPATH, "//button[@id='btnSave_IP_BedTfr']")

        scroll_to_element(driver, transfer_element)
        time.sleep(2)
        transfer_element.click()

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
@allure.title("Test Case: Cancelling Retained Bed")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_35(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[6]"
        )

        room_name_1 = get_next_room_name()
        room_name_2 = get_next_room_name()

        print("Admission Room:", room_name_1)
        print("Transfer Room:", room_name_2)


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
        # room_name = get_next_room_name()
        room_name = room_name_1
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
        # room_name = get_next_room_name()
        room_name = room_name_2
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

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"
        )

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name_2}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "//button[@id='btnAdmitNow_IP_NA_NA']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//button[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnQuickAction_IP_AD_DE_New_transferBed']"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//p-dropdown[@id='selectbldn_IP_BedTfr']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block D'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Select Floor'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='1st floor'])[1]"
        )

        time.sleep(2)

        # Build bed name exactly same as created earlier
        bed_name = f"Bed{room_name_1}"

        print("Transferring to Bed:", bed_name)

        # Locate and click Select Bed button for that bed
        bed_xpath = f"""
        //span[contains(text(),'{bed_name}')]/ancestor::div[contains(@class,'bed-card')]
        //button[contains(@class,'btnSelectBed_IP_BedTfr')]
        """

        bed_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, bed_xpath))
        )

        bed_element.click()

        time.sleep(2)
        retain_element = driver.find_element(By.XPATH, "(//label[normalize-space()='Yes'])[1]")
        
        scroll_to_element(driver, retain_element)
        time.sleep(2)
        retain_element.click()

        transfer_element = driver.find_element(By.XPATH, "//button[@id='btnSave_IP_BedTfr']")

        scroll_to_element(driver, transfer_element)
        time.sleep(2)
        transfer_element.click()

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "(//span[normalize-space()='Bed Transactions'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//a[contains(text(),'Bed Transactions')])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "//button[contains(@class,'btnCancel_IP_BT_BT')][1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[normalize-space()='Yes'])[1]"
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
@allure.title("Test Case: Not Cancelling Retained Bed")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_36(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[6]"
        )

        room_name_1 = get_next_room_name()
        room_name_2 = get_next_room_name()

        print("Admission Room:", room_name_1)
        print("Transfer Room:", room_name_2)


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
        # room_name = get_next_room_name()
        room_name = room_name_1
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
        # room_name = get_next_room_name()
        room_name = room_name_2
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

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "(//*[name()='svg'][@class='p-icon p-paginator-icon'])[4]"
        )

        time.sleep(2)
        room_xpath = f"//div[contains(text(),'Room : {room_name_2}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
             
        ).click()

        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "//button[@id='btnAdmitNow_IP_NA_NA']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//button[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnQuickAction_IP_AD_DE_New_transferBed']"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//p-dropdown[@id='selectbldn_IP_BedTfr']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Block D'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Select Floor'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='1st floor'])[1]"
        )

        time.sleep(2)

        # Build bed name exactly same as created earlier
        bed_name = f"Bed{room_name_1}"

        print("Transferring to Bed:", bed_name)

        # Locate and click Select Bed button for that bed
        bed_xpath = f"""
        //span[contains(text(),'{bed_name}')]/ancestor::div[contains(@class,'bed-card')]
        //button[contains(@class,'btnSelectBed_IP_BedTfr')]
        """

        bed_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, bed_xpath))
        )

        bed_element.click()

        time.sleep(2)
        retain_element = driver.find_element(By.XPATH, "(//label[normalize-space()='Yes'])[1]")
        
        scroll_to_element(driver, retain_element)
        time.sleep(2)
        retain_element.click()

        transfer_element = driver.find_element(By.XPATH, "//button[@id='btnSave_IP_BedTfr']")

        scroll_to_element(driver, transfer_element)
        time.sleep(2)
        transfer_element.click()

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "(//span[normalize-space()='Bed Transactions'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//a[contains(text(),'Bed Transactions')])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "//button[contains(@class,'btnCancel_IP_BT_BT')][1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[normalize-space()='No'])[1]"
        )
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
@allure.title("Test Case: Assigned Diet Plan to patient")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_37(login):
        
    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
             driver, By.XPATH, "(//img)[5]"
        )
        
        time.sleep(2)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"
        )

        time.sleep(2)
        wait_and_locate_click(
              driver, By.XPATH, "(//button[@label='View'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Diet Plans'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnAssign_IP_ktcAnlDietGrd']"
        )


        diet_plan_name = "DietPlan_" + str(uuid.uuid4())[:4]
        print("DietPlan Name", diet_plan_name)

        wait_and_send_keys(
               driver, By.XPATH, "//input[@id='inputDiet_IP_ktcAnlDBrdAssign']", diet_plan_name
        )

        wait_and_locate_click(
               driver, By.XPATH, "//p-dropdown[@id='selectUsr_IP_ktcAnlDBrdAssign']"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Venu Gopal'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]")
        time.sleep(2)

        today_element = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
        (By.XPATH, "//td[contains(@class, 'p-datepicker-today')]//span")
                )
        )          

        # Click using JavaScript in case normal click doesn't work
        login.execute_script("arguments[0].click();", today_element)

        print("Assigned date selected:", today_element.text)

        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")
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
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[3]")

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
               driver, By.XPATH, "(//button[@id='btnUseTemp_IP_ktcAnlDietTmplt'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnAssign_IP_ktcAnlDBrdAssign']"
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
@allure.title("Test Case: IP invoice is now created till the invoice generation date and time")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_38(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(1)
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

        wait_and_locate_click(login, By.XPATH, "//button[@id='btnAdmitNow_IP_NA_NA']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//button[@id='btnViewIp_IP_IpGrd'])[1]"
        )


        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//*[@id='btnAddService_IP_AD_DE_New']"
        )

        time.sleep(1)
        wait_and_send_keys(
               driver, By.XPATH, "//input[@placeholder='Search Service']", "Doc"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "//li[@role='option']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//p-multiselect[@placeholder='Select Doctors']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Venu Gopal']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//*[normalize-space()='Add Service']"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Invoices'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnCreate_IP_AD_INV']"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//button[@role='menuitem'])[1]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnGenerate_IP_Invoice']"
        )

        time.sleep(2)

        gen_element = driver.find_element(By.XPATH, "//button[@id='btnGenerateInvoice_IP_Invoice']")
        scroll_to_element(driver, gen_element)

        time.sleep(1)
        gen_element.click()

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
@allure.title("Test Case:Inline Item Apply discount and  update the Invoice")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_39(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"

        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//button[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Invoices'])[1]"
        )

        time.sleep(1)

        wait_and_locate_click(
            driver, By.XPATH, "(//button[contains(@class, 'btnEdit_IP_AD_INV')])[1]"
        )

        wait_and_locate_click(
               driver, By.XPATH, "(//mat-icon[@role='img'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnApplyDisc_Service_IP_Invoice']"
        )


        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//option[normalize-space()='On Demand Discount'])[2]"))
            ).click()

        time.sleep(2)
        discount_amount = random.randint(20, 100)
        wait_and_send_keys(login, By.XPATH, "//input[@id='inptItemDiscAmt_IP_Invoice']", discount_amount)

        wait_and_locate_click(login, By.XPATH, "//button[@id='btnApplyItemDiscount_IP_Invoice']")

        msg = get_toast_message(login)
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
@allure.title("Test Case: Invoice generated with ADHOC items")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_40(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(1)
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

        wait_and_locate_click(login, By.XPATH, "//button[@id='btnAdmitNow_IP_NA_NA']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//button[@id='btnViewIp_IP_IpGrd'])[1]"
        )


        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "//*[@id='btnAddService_IP_AD_DE_New']"
        )

        time.sleep(2)
        wait_and_send_keys(
               driver, By.XPATH, "//input[@placeholder='Search Service']", "Doc"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//li[@role='option']"
        )

        time.sleep(2)
        duration_element = driver.find_element(By.XPATH, "//input[@placeholder='Duration (mins)']")
        duration_element.click()
        time.sleep(1)
        duration_element.clear()
        time.sleep(1)
        duration_element.send_keys("2")

        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "//p-multiselect[@placeholder='Select Doctors']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Venu Gopal']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//*[normalize-space()='Add Service']"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//button[@id='btnQuickAction_IP_AD_DE_New_createInvoices'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnGenerate_IP_Invoice']"
        )

        time.sleep(1)

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnAddMore_IP_Invoice']"
        )

        wait_and_send_keys(
               driver, By.XPATH, "(//input[@id='inptService_IP_Invoice'])[1]", "ADOHC Item"
        )

        time.sleep(1)
        price_element = driver.find_element(By.XPATH, "//input[@id='inptPrice_IP_Invoice']")
        price_element.click()
        time.sleep(1)
        price_element.clear()

        price_element.send_keys("157")

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnAddUpdate_IP_Invoice']"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnGenerateInvoice_IP_Invoice']"
        )

        msg = get_toast_message(driver)
        print("Toast Message:", msg)
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
@allure.title("Test Case: Apply Discount to Invoice")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_41(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(1)
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

        wait_and_locate_click(login, By.XPATH, "//button[@id='btnAdmitNow_IP_NA_NA']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//button[@id='btnViewIp_IP_IpGrd'])[1]"
        )


        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "//*[@id='btnAddService_IP_AD_DE_New']"
        )

        time.sleep(2)
        wait_and_send_keys(
               driver, By.XPATH, "//input[@placeholder='Search Service']", "Doc"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "//li[@role='option']"
        )

        time.sleep(2)
        duration_element = driver.find_element(By.XPATH, "//input[@placeholder='Duration (mins)']")
        duration_element.click()
        time.sleep(1)
        duration_element.clear()
        time.sleep(1)
        duration_element.send_keys("2")

        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "//p-multiselect[@placeholder='Select Doctors']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Venu Gopal']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//*[normalize-space()='Add Service']"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//button[@id='btnQuickAction_IP_AD_DE_New_createInvoices'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnGenerate_IP_Invoice']"
        )

        time.sleep(1)

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnAddMore_IP_Invoice']"
        )

        wait_and_send_keys(
               driver, By.XPATH, "(//input[@id='inptService_IP_Invoice'])[1]", "ADOHC Item"
        )

        time.sleep(1)
        price_element = driver.find_element(By.XPATH, "//input[@id='inptPrice_IP_Invoice']")
        price_element.click()
        time.sleep(1)
        price_element.clear()

        price_element.send_keys("157")

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnAddUpdate_IP_Invoice']"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnGenerateInvoice_IP_Invoice']"
        )

        msg = get_toast_message(driver)
        print("Toast Message:", msg)
        time.sleep(3)

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnEdt_IP_InvView']"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//a[@id='aApplyDiscount_IP_Invoice']"
        )

        time.sleep(1)

        dropdown = Select(driver.find_element(By.ID, "slctOrderDiscount_IP_Invoice"))
        dropdown.select_by_visible_text("On Demand Discount")


        time.sleep(2)
        discount_amount = random.randint(20, 100)
        wait_and_send_keys(login, By.XPATH, "(//input[@id='inptDiscAmt_IP_Invoice'])[1]", discount_amount)

        wait_and_locate_click(login, By.XPATH, "//button[@id='btnApplyDiscount_IP_Invoice']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnViewInvoice_IP_Invoice']"
        )

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
@allure.title("Test Case: Item is removed from the invoice")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_42(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(1)
        wait_and_locate_click(
             driver, By.XPATH, "(//div[@id='actionNav_IP_DBoard'])[2]"

        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//button[@id='btnViewIp_IP_IpGrd'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Invoices'])[1]"
        )

        time.sleep(1)

        wait_and_locate_click(
            driver, By.XPATH, "(//button[contains(@class, 'btnEdit_IP_AD_INV')])[1]"
        )

        wait_and_locate_click(
               driver, By.XPATH, "(//button[@id='btnRowMenu_Adhoc_IP_Invoice'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnRemServer_Adhoc_IP_Invoice']"
        )

        msg = get_toast_message(driver)
        print("Toast Message:", msg )
        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnViewInvoice_IP_Invoice']"
        )

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
@allure.title("Test Case: Master Invoice is enabled in the account")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_43(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "//img[@src='./assets/images/menu/settings.png']"
        )

        time.sleep(2)

        finance_element = driver.find_element(By.XPATH, "//div[normalize-space()='Finance manager']")
        scroll_to_element(driver, finance_element)
        time.sleep(1)
        
        wait_and_locate_click(
            driver, By.XPATH, "(//i[@class='fa fa-gears mgn-lt-auto'])[4]"
        )

        time.sleep(2)

        toggle = wait.until(EC.element_to_be_clickable((
            By.XPATH, "(//button[@role='switch'])[2]"
        )))

        if toggle.get_attribute("aria-checked") == "false":
            driver.execute_script("arguments[0].click();", toggle)


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
@allure.title("Test Case:Master Invoice")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management_1, password)])
def test_IP_Management_44(login):

    try:
        wait = WebDriverWait(login, 30)
        driver = login
        time.sleep(3)

        wait_and_locate_click(
               driver, By.XPATH, "(//img)[5]"
        )

        time.sleep(1)
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

        wait_and_locate_click(login, By.XPATH, "//button[@id='btnAdmitNow_IP_NA_NA']")

        msg = get_toast_message(login)
        print("Toast Message :", msg)

        time.sleep(2)

        wait_and_locate_click(
               driver, By.XPATH, "(//button[@id='btnViewIp_IP_IpGrd'])[1]"
        )


        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//*[@id='btnAddService_IP_AD_DE_New']"
        )

        time.sleep(1)
        wait_and_send_keys(
               driver, By.XPATH, "//input[@placeholder='Search Service']", "Doc"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "//li[@role='option']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//p-multiselect[@placeholder='Select Doctors']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Venu Gopal']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//*[normalize-space()='Add Service']"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Invoices'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnCreate_IP_AD_INV']"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//button[@role='menuitem'])[1]"
        )

        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnGenerate_IP_Invoice']"
        )

        time.sleep(2)

        gen_element = driver.find_element(By.XPATH, "//button[@id='btnGenerateInvoice_IP_Invoice']")
        scroll_to_element(driver, gen_element)

        time.sleep(1)
        gen_element.click()

        msg = get_toast_message(driver)
        print("Toast Message :", msg)
        time.sleep(2)


        wait_and_locate_click(
            driver, By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"
        )

        time.sleep(2) 
        wait_and_locate_click(
            driver, By.XPATH, "(//span[normalize-space()='Services'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnAddService_IP_AD_DE_New']"
        )

        time.sleep(1)
        wait_and_send_keys(
               driver, By.XPATH, "//input[@placeholder='Search Service']", "Doc"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "//li[@role='option']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//p-multiselect[@placeholder='Select Doctors']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Venu Gopal']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//*[normalize-space()='Add Service']"
        )

        time.sleep(2)
        wait_and_locate_click(
               driver, By.XPATH, "(//span[normalize-space()='Invoices'])[1]"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "//button[@id='btnCreate_IP_AD_INV']"
        )

        time.sleep(1)
        wait_and_locate_click(
               driver, By.XPATH, "(//button[@role='menuitem'])[1]"
        )

        time.sleep(2)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnGenerate_IP_Invoice']"
        )

        wait_and_locate_click(
               driver, By.XPATH, "//i[@class='pi pi-arrow-left']"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnCreate_IP_AD_INV']"
        )
        
        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//div[@class='mdc-checkbox'])[2]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//div[@class='mdc-checkbox'])[3]"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[@id='btnMasterInvoice_IP_AD_INV']"
        )

        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "(//button[normalize-space()='Yes'])[1]"
        )

        msg = get_toast_message(driver)
        print("Toast Message: ", msg)
        time.sleep(2)

        invoice_type = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//tbody/tr[1]//span[contains(@class,'invoice')]")
            )
        ).text

        print("Invoice Type in first row is:", invoice_type)

        assert invoice_type.strip() == "Master Invoice"

        time.sleep(3)
        
    except Exception as e:
                    allure.attach(  # use Allure package, .attach() method, pass 3 params
                        driver.get_screenshot_as_png(),  # param1
                        # driver.screenshot()
                        name="full_page",  # param2
                        attachment_type=AttachmentType.PNG,
                    )
                    raise e







