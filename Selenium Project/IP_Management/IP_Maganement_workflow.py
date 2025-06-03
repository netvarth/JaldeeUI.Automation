from Framework.common_utils import *
from Framework.common_dates_utils import *
import random

from faker import Faker

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Basic workflow of IP Mangement")
@pytest.mark.parametrize("url, username, password", [(scale_url, IP_Management, password)])
def test_IP_workflow(login):

    wait = WebDriverWait(login, 20)
    try:
        time.sleep(5)
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
                (By.XPATH, "(//button[@class='p-element create-item-button p-button p-component'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
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
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Observation Beds'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
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
                (By.XPATH, "(//img)[2]"))
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
        else:
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
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Second Floor B'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(2)
        room_xpath = f"//span[normalize-space()='{room_name}']"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
        ).click()

        time.sleep(2)   
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Normal'])[1]"))
        ).click()

        time.sleep(2)
        room_xpath1 = f"//div[contains(text(),'Room : {room_name}')]"
        wait.until(
            EC.presence_of_element_located((By.XPATH, room_xpath1))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Assign Bed'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        time.sleep(5)

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

        

        time.sleep(10)
 




    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e