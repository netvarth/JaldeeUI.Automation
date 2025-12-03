
from ast import arguments
import pyautogui
import random
from pathlib import Path
from Framework.common_utils import *
from Framework.common_dates_utils import *

from faker import Faker
import random

def generate_number_with_zeros():
    number = random.randint(3, 9)  # Generate a two-digit number
    zeros = "0" * random.randint(3,5)  # Append 1 to 5 zeros
    return int(f"{number}{zeros}")





@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Basic LOS work flow")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_officer, password)])
def test_los_workflow(login):

    try:
        wait = WebDriverWait(login, 20)

        login.implicitly_wait(10)
        los_menu = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[4]"))
        )
        login.execute_script("arguments[0].click();", los_menu)


        # Create the Lead
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
        ).click()

        login.implicitly_wait(10)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Round North'])[1]"))
        ).click()
        
        login.implicitly_wait(10)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Create Lead')]"))
        ).click()

        time.sleep(3)

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter First Name']"))
        ).send_keys(first_name)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Last Name']"))
        ).send_keys(last_name)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='phone']"))
        ).send_keys(phonenumber)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Email']"))
        ).send_keys(email)
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        time.sleep(3)
       
        
       
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

        # Generate Date of Birth (DOB)
        [year, month, day] = Generate_dob()
        print(f"Year: {year}, Month: {month}, Day: {day}")

        time.sleep(2)
        # Select Year
        year_xpath = f"//span[normalize-space()='{year}']"
        wait_and_locate_click(login, By.XPATH, year_xpath)

        time.sleep(2)
        # Select Month
        month_xpath = f"//span[normalize-space()='{month}']"
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, month_xpath))
        ).click()

        time.sleep(1)
        # Select Day
        day = str(int(day))  # Ensuring day is in integer form
        day_xpath = f"//span[normalize-space()='{day}']"
        select_day = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, day_xpath))
        )
        select_day.click()


        login.implicitly_wait(10)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Select Gender']"))
        ).click()

        login.implicitly_wait(10)
        gender = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Male'])[1]"))
        )
        login.execute_script("arguments[0].click();", gender)

        login.implicitly_wait(10)
        dropdown = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Select Sourcing Channel']"))
        )
        dropdown.click()

        print("test case")
        login.implicitly_wait(10)
        options = dropdown.find_elements(By.XPATH, "//ul[@role='listbox']")

        # Select a random option
        if options:
            random_option = random.choice(options)
            random_option.click()
        else:
            print("No options found in the dropdown.")
        
        login.implicitly_wait(10) 

   

        # Generate a random amount within the range
        random_amount = generate_number_with_zeros()

        # Print the result
        print(f"The random amount is: ₹{random_amount}") 

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@formcontrolname='proposedAmount']"))
        ).send_keys(random_amount)

        login.implicitly_wait(10)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Select Preferred Scheme']"))
        ).click()

        login.implicitly_wait(10)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='SCHEME - B']"))
        ).click()

        login.implicitly_wait(10)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Tenure (in months)'])[1]"))
        ).send_keys("48")



        # Lead 

        login.implicitly_wait(10)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='Leads']"))
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='add-btn btn started ng-star-inserted'])[1]"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Remarks']"))
        ).send_keys("Follow up 1 proceed")


        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Proceed']"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='add-btn btn started ng-star-inserted'])[1]"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Remarks']"))
        ).send_keys("Follow up 2 proceed")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Proceed']"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text

        print("Toast Message:", message)

        # Update KYC 

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='add-btn btn started ng-star-inserted'])[1]"))
        ).click()

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'Verify')])[1]"))
        ).click()

        snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

        otp_digits = "55555"
        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )

        # print("Number of OTP input fields:", len(otp_inputs))
        # print(otp_inputs)

        for i, otp_input in enumerate(otp_inputs):

            # print(i)
            # print(otp_input)
            otp_input.send_keys(otp_digits[i])

        snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Aadhaar Number']"))
        ).send_keys("555555555555")

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[1]"))
        ).click()           

        time.sleep(3)
        # Construct the absolute path
        absolute_path = Path("Extras/test.png").resolve()

        # Use pyautogui to write the path and press Enter
        pyautogui.write(str(absolute_path))
        pyautogui.press("enter")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Verify'])[1]"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Refresh']"))
        ).click()


        time.sleep(3)
        pan_card = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Pan Number']"))
          )
        
        pan_card.click()
        pan_card.send_keys("5555555555")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[2]"))
        ).click()

        time.sleep(3)
        absolute_path = Path("Extras/test.png").resolve()
        pyautogui.write(str(absolute_path))
        time.sleep(2)
        pyautogui.press("enter")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'Verify')])[2]"))
        ).click()


        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        scroll = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[normalize-space()='Select Alternate Id'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", scroll)

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Select Alternate Id']"))
        ).click()

        time.sleep(3)
        id_option = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Driving License'])[1]"))
        )

        login.execute_script("arguments[0].click();", id_option)

        

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Id Card Number'])[1]"))
        ).send_keys("31125478453")
 
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[normalize-space()='Upload File'])[2]")
            )
        ).click()

        time.sleep(3)
        
        # Construct the absolute path
        absolute_path = Path("Extras/test.png").resolve()

        # Use pyautogui to write the path and press Enter
        pyautogui.write(str(absolute_path))
        pyautogui.press("enter")

        time.sleep(3)


        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Select Relationship Type']"))
        ).click()

        time.sleep(3)
        type_option = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Father'])[1]"))
        )
        type_option.click()

        first_name, last_name, cons_manual_id, phonenumber, email=create_user_data()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Name of Relative']"))
        ).send_keys(first_name)


        time.sleep(3)
  
        fake_india= Faker('en_IN')
        fake_india_address= fake_india.address().replace("\n", " ").strip()
        print(fake_india_address)

        
        file_path = r"F:\UI Automation\JaldeeUI.Automation\Selenium Project\Data\address.txt"
    
        # Open the file in 'w' mode (create the file if it doesn't exist, overwrite it if it does)
        print("value to be written to file", fake_india_address)
        with open(file_path, 'w') as file:
        # Write the value to the file
            file.write(fake_india_address)
        print("value written to file", fake_india_address)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Permanent Address 1'])[1]"))            
        ).send_keys(fake_india_address)

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Permanent Address 2'])[1]"))            
        ).send_keys(fake_india_address)

        street_address, city, state, zip_code, country = generate_random_billing_india_address()
        print("street_address: ", street_address, "city:", city, "state:",  state, "zip_code:", zip_code, "country:", country)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Permanent City'])[1]"))
        ).send_keys(city)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Permanent State'])[1]"))
        ).click()

        time.sleep(3)
        dropdown = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//ul[@role='listbox']"))
        )
    
        kerala_option = dropdown.find_element(By.XPATH, "//li[@aria-label='Kerala']")
        kerala_option.click()


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Permanent Pincode'])[1]"))
        ).send_keys("680505")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='p-checkbox-box'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='btn btn-add-coapplicant ng-star-inserted'])[1]"))
        ).click()

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter First Name']"))
        ).send_keys(first_name)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Last Name']"))
        ).send_keys(last_name)


        # time.sleep(2)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]"))
        # ).click()
        
        # time.sleep(3)

        # login.find_element(By.XPATH, "//button[normalize-space()='2025']").click()

        # backward_arrow = WebDriverWait(login, 10).until(
        #     EC.element_to_be_clickable(
        #         (By.XPATH, "//button[contains(@class, 'p-ripple') and contains(@class, 'p-element') and contains(@class, 'p-datepicker-prev') and contains(@class, 'p-link') and contains(@class, 'ng-star-inserted')]")
        #     )
        # )

        # # Clicking backward arrows 4 times to navigate to the correct year
        # for _ in range(4):
        #     backward_arrow.click()

        # # Generate Date of Birth (DOB)
        # [year, month, day] = Generate_dob()
        # print(f"Year: {year}, Month: {month}, Day: {day}")

        # # Select Year
        # year_xpath = f"//span[normalize-space()='{year}']"
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, year_xpath))
        # ).click()

        # # Select Month
        # month_xpath = f"//span[normalize-space()='{month}']"
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, month_xpath))
        # ).click()

        # # Select Day
        # day = str(int(day))  # Ensuring day is in integer form
        # day_xpath = f"//span[normalize-space()='{day}']"
        # select_day = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, day_xpath))
        # )
        # login.execute_script("arguments[0].click();",select_day)
         # Open date picker
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")
            )
        ).click()

        # Open year picker
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='2025']")
            )
        ).click()

        # Generate DOB
        year, month, day = Generate_dob()
        print(f"Year: {year}, Month: {month}, Day: {day}")

        # Click backward arrow if necessary (assuming you always want to go back 4 times)
        backward_arrow = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'p-datepicker-prev')]")
            )
        )
        for _ in range(4):
            backward_arrow.click()
        time.sleep(2)
        # Select year
        year_xpath = f"//span[normalize-space()='{year}']"
        wait.until(EC.element_to_be_clickable((By.XPATH, year_xpath))).click()

        time.sleep(2)
        # Select month
        month_xpath = f"//span[normalize-space()='{month}']"
        wait.until(EC.element_to_be_clickable((By.XPATH, month_xpath))).click()

        time.sleep(2)
        # Select day
        day = str(int(day))  # remove leading zeros if any
        day_xpath = f"//span[normalize-space()='{day}']"
        select_day = wait.until(EC.presence_of_element_located((By.XPATH, day_xpath)))

        # Using execute_script for safe clicking
        login.execute_script("arguments[0].click();", select_day)
       
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Select Gender']"))
        ).click()

        time.sleep(3)
        gender = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Male'])[1]"))
        )
        login.execute_script("arguments[0].click();", gender)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='phone'])[1]"))
        ).send_keys(phonenumber)


        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'Verify')])[2]"))
        ).click()

        time.sleep(3)
        snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

        otp_digits = "55555"
        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )


        for i, otp_input in enumerate(otp_inputs):

            # print(i)
            # print(otp_input)
            otp_input.send_keys(otp_digits[i])

        snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)


        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@formcontrolname='coApplicantEmail'])[1]"))
        ).send_keys(email)

        time.sleep(3)
        select_type = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-dropdown[@placeholder='Select Relationship Type'])[2]"))
        )
        select_type.click()
        login.execute_script("arguments[0].click();", select_type)

        # print("type option")
        time.sleep(2)
        type_option = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Mother'])[1]"))
        )
        type_option.click()

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        time.sleep(2)
        print(first_name)
        relative_name = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Name of Relative'])[2]"))
        )
        relative_name.click()
        relative_name.send_keys(first_name)

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Aadhaar Number'])[2]"))
        ).send_keys("555555555551")

        time.sleep(1)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[2]")
            )
        ).click()

        time.sleep(3)
        absolute_path = Path("Extras/test.png").resolve()

        # Use pyautogui to write the path and press Enter
        pyautogui.write(str(absolute_path))
        pyautogui.press("enter")


        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'Verify')])[3]"))
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Refresh']"))
        ).click()

      
        time.sleep(3)
        pan_card = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Pan Number'])[2]"))
          )
        
        pan_card.click()
        pan_card.send_keys("5555555551")

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[3]")
            )
        ).click()

        time.sleep(3)
        absolute_path = Path("Extras/test.png").resolve()

        pyautogui.write(str(absolute_path))
        time.sleep(3)
        pyautogui.press("enter")

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'Verify')])[3]"))
        ).click()


        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        scroll1 = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[contains(text(),'Select Alternate Id')])[2]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", scroll1 )
    
        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Select Alternate Id']"))
        ).click()

        time.sleep(2)

        wait.until(
          EC.presence_of_element_located(
              (By.XPATH, "(//span[normalize-space()='Driving License'])[2]"))
        ).click()


        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Id Card Number'])[2]"))
        ).send_keys("3112546464753")

        time.sleep(2)  
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[3]")
            )
        ).click()

        time.sleep(3)
        absolute_path = Path("Extras/test.png").resolve()

        pyautogui.write(str(absolute_path))
        time.sleep(2)
        pyautogui.press("enter")
        
        fake_india= Faker('en_IN')
        fake_india_address= fake_india.address().replace("\n", " ").strip()
        print(fake_india_address)

        time.sleep(3)
        co_address = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Permanent Address 1'])[2]"))            
        )
        co_address.click()
        co_address.send_keys(fake_india_address)

        time.sleep(4)
        co_address1 = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Permanent Address 2'])[2]"))            
        )
        co_address1.click()
        co_address1.send_keys(fake_india_address)

        
        street_address, city, state, zip_code, country = generate_random_billing_india_address()
        print("street_address: ", street_address, " city:", city, " state:",  state, "zip_code: ", zip_code, "country: ", country)

        time.sleep(3)
        permanentcity = WebDriverWait(login, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@formcontrolname='coApplicantPermanentCity' and @type='text' and @placeholder='Enter Permanent City']"))
        )
        login.execute_script("arguments[0].click();", permanentcity )
        time.sleep(3)
        permanentcity.send_keys(city)


        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Permanent State'])[1]"))
        ).click()

        time.sleep(3)
        dropdown = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//ul[@role='listbox']"))
        )
    
        # Locate the option with "Kerala" text and click on it
        kerala_option = dropdown.find_element(By.XPATH, "//li[@aria-label='Kerala']")
        kerala_option.click()


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Permanent Pincode'])[2]"))
        ).send_keys("680505")



        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Proceed']"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        home_button = WebDriverWait(login, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@id='kt_quick_user_toggle']//span[contains(@class, 'bname')]")
        )
        )
        login.execute_script("arguments[0].click();", home_button)

        time.sleep(2)
        signout_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Sign Out']"))
        )
        login.execute_script("arguments[0].click();", signout_button)

        # Re-login to verify options

        print("Login with Credit Head")
        login_id = login.find_element(By.XPATH, "//input[@id='loginId']")
        login_id.clear()
        login_id.send_keys("001921")

        password = login.find_element(By.XPATH, "//input[@id='password']")
        password.clear()
        password.send_keys("Jaldee01")

        login.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(3)
        wait = WebDriverWait(login, 20)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='Leads']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        time.sleep(3)

        View_CRIF = WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-file'])[1]"))
        )                   
        login.execute_script("arguments[0].scrollIntoView();", View_CRIF)

        View_CRIF.click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'Generate')])[1]"))
        ).click()


        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'Generate')])[1]"))
        ).click()

        time.sleep(2)

        score_element = login.find_element(By.CLASS_NAME, "center-text")

        # Get the displayed text
        score_text = score_element.text.strip()

        # Expected text
        expected_text = "777/900"

        # Assert the value is displayed correctly
        assert score_text == expected_text, f"Expected '{expected_text}', but got '{score_text}'"

        print("Assertion passed: Correct score is displayed.")

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-arrow-left'])[1]"))
        ).click()

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Update'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Remarks']"))
        ).send_keys("KYC Verification")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Verify'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        home_button = WebDriverWait(login, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@id='kt_quick_user_toggle']//span[contains(@class, 'bname')]")
        )
        )
        login.execute_script("arguments[0].click();", home_button)

        time.sleep(3)
        signout_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Sign Out']"))
        )
        login.execute_script("arguments[0].click();", signout_button)

        # Re-login to verify options
        print("Login with Sales officer")
        login_id = login.find_element(By.XPATH, "//input[@id='loginId']")
        login_id.clear()
        login_id.send_keys("001920")

        password = login.find_element(By.XPATH, "//input[@id='password']")
        password.clear()
        password.send_keys("Jaldee01")

        login.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='Leads']"))
        ).click()


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='add-btn btn started ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Location']"))
        ).click()

        time.sleep(3)

        try:
            # Locate the input field using XPath
            input_field = login.find_element(By.XPATH, "//input[@id='txtsearchlocation_LMS_googlemap']")

            # Input "Thrissur" into the text field
            input_field.send_keys("thrissur")
            time.sleep(3)

            # Wait for the suggestions to appear and select the appropriate one
            suggestions = wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='pac-item']"))
            )

            time.sleep(3)

            # Iterate through the suggestions and select the one that matches "Thrissur, Kerala, India"
            for suggestion in suggestions:
                if "Thrissur, Kerala, India" in suggestion.text:
                    suggestion.click()
                    break

        finally:
                print("Loaction : Thrissur, Kerala, India")

        time.sleep(2)
        login.find_element(By.XPATH, "//button[@type='button']//span[@class='mdc-button__label']").click()


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[1]"))
        ).click()

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\ test.png")
        )
        pyautogui.write(absolute_path)
        time.sleep(3)
        pyautogui.press("enter")
        print("Successfully upload the file")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[2]"))
        ).click()

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\ test10mbvideo.mp4")
        )
        pyautogui.write(absolute_path)
        time.sleep(3)
        pyautogui.press("enter")
        print("Successfully upload the file")

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Remarks']"))
        ).send_keys("Remarks from sale team")

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Proceed'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-sign-in'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()
         

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        # Processing File Loan Application 

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Update'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@data-bs-target='#flush-collapseFinancials'])[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[1]"))
        ).click()

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\ prescription.pdf")
        )
        pyautogui.write(absolute_path)
        time.sleep(3)
        pyautogui.press("enter")


        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[2]"))
        ).click()

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\ prescription.pdf")
        )
        pyautogui.write(absolute_path)
        time.sleep(2)
        pyautogui.press("enter")


        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[3]"))
        ).click()

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\ test.png")
        )
        pyautogui.write(absolute_path)
        time.sleep(2)
        pyautogui.press("enter")


        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[4]"))
        ).click()

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\ prescription.pdf")
        )
        pyautogui.write(absolute_path)
        time.sleep(3)
        pyautogui.press("enter")


        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[5]"))
        ).click()

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\ test.png")
        )
        pyautogui.write(absolute_path)
        time.sleep(3)
        pyautogui.press("enter")


        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[6]"))
        ).click()

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\ prescription.pdf")
        )
        pyautogui.write(absolute_path)
        time.sleep(3)
        pyautogui.press("enter")


        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[7]"))
        ).click()

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\ test.png")
        )
        pyautogui.write(absolute_path)
        time.sleep(3)
        pyautogui.press("enter")

        time.sleep(3)
        save_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save Financial Documents'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", save_button)
        time.sleep(3)
        save_button.click()
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3) 


        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@data-bs-target='#flush-collapseLegal'])[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[8]"))
        ).click()

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\ test.png")
        )
        pyautogui.write(absolute_path)
        time.sleep(3)
        pyautogui.press("enter")


        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[9]"))
        ).click()

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\ test.png")
        )
        pyautogui.write(absolute_path)
        time.sleep(3)
        pyautogui.press("enter")


        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[10]"))
        ).click()

        time.sleep(3)
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\ test.png")
        ) 
        pyautogui.write(absolute_path)
        time.sleep(2)
        pyautogui.press("enter")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[11]"))
        ).click()

        time.sleep(3)
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\ test.png")
        )
        pyautogui.write(absolute_path)
        time.sleep(2)
        pyautogui.press("enter")

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[12]"))
        ).click()

        time.sleep(3)
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\ test.png")
        )
        pyautogui.write(absolute_path)
        time.sleep(2)
        pyautogui.press("enter")

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[13]"))
        ).click()

        time.sleep(3)
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\ test.png")
        )
        pyautogui.write(absolute_path)
        time.sleep(2)
        pyautogui.press("enter") 


        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[14]"))
        ).click()

        time.sleep(3)
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\ test.png")
        )
        pyautogui.write(absolute_path)
        time.sleep(2)
        pyautogui.press("enter")


        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[15]"))
        ).click()

        time.sleep(3)
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\ test.png")
        )
        pyautogui.write(absolute_path)
        time.sleep(2)
        pyautogui.press("enter")


        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[@for='input-file'][normalize-space()='Upload File'])[16]"))
        ).click()

        time.sleep(3)
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\ test.png")
        )
        pyautogui.write(absolute_path)
        time.sleep(2)
        pyautogui.press("enter")


        time.sleep(3)
                
        save_button1 = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save Legal Documents'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", save_button1)
        time.sleep(2)
        save_button1.click()

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
@allure.title("Sales officer report")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_officer, password)])
def test_sales_officer_report(login):

    try:
        
        time.sleep(3)
        wait = WebDriverWait(login, 20)
        print("Login with Sales Officer")
        print("Sales Officer Report")
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Processing Files'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='add-btn btn started ng-star-inserted'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@aria-controls='flush-collapseParent'])[1]"))        
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@aria-controls='flush-collapseOne'])[1]"))
        ).click()   

        time.sleep(3)

    #     ####################Income####################
        income = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='I. INCOME'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", income)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(@class, 'btn back-btn') and contains(@class, 'p-button') and contains(., 'Add Income')]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-dropdown[@placeholder='Select Applicant/CoApplicant']//div[@class='text-left p-dropdown p-component']//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//ul[@role='listbox']//li[@role='option'][1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Category'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Business Income'])[1]"))
        ).click()

        Enter_value = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Value'])[1]"))
        )
        Enter_value.clear()
        Enter_value.send_keys("120000")

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(@class, 'btn back-btn') and contains(@class, 'p-button') and contains(., 'Add Income')]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-dropdown[@placeholder='Select Applicant/CoApplicant']//div[@class='text-left p-dropdown p-component']//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//ul[@role='listbox']//li[@role='option'][1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Category'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Rental Income'])[1]"))
        ).click()

        Enter_value_1 = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Value'])[2]"))
        )
        Enter_value_1.clear()
        time.sleep(2)
        Enter_value_1.send_keys("12000")

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(@class, 'btn back-btn') and contains(@class, 'p-button') and contains(., 'Add Income')]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-dropdown[@placeholder='Select Applicant/CoApplicant']//div[@class='text-left p-dropdown p-component']//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//ul[@role='listbox']//li[@role='option'][1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Category'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Salary Income'])[1]"))
        ).click()

        Enter_value_2 = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Value'])[3]"))
        )
        Enter_value_2.clear()
        Enter_value_2.send_keys("45000")

        time.sleep(3)

    #Expenses

        expense = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='II. EXPENSE'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", expense)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(@class, 'btn back-btn') and contains(@class, 'p-button') and contains(., 'Add Expense')]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-dropdown[@placeholder='Select Applicant/CoApplicant']//div[@class='text-left p-dropdown p-component']//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//ul[@role='listbox']//li[@role='option'][1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
          
      (By.XPATH, "(//span[normalize-space()='Select Category'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Electricity Expense'])[1]"))
        ).click()

        Enter_value_3 = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Value'])[4]"))
        )
        Enter_value_3.clear()
        Enter_value_3.send_keys("2000")

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(@class, 'btn back-btn') and contains(@class, 'p-button') and contains(., 'Add Expense')]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-dropdown[@placeholder='Select Applicant/CoApplicant']//div[@class='text-left p-dropdown p-component']//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//ul[@role='listbox']//li[@role='option'][1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Category'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Salary Expense'])[1]"))
        ).click()

        Enter_value_4 = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Value'])[5]"))
        )
        Enter_value_4.clear()
        Enter_value_4.send_keys("3000")

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(@class, 'btn back-btn') and contains(@class, 'p-button') and contains(., 'Add Expense')]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-dropdown[@placeholder='Select Applicant/CoApplicant']//div[@class='text-left p-dropdown p-component']//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//ul[@role='listbox']//li[@role='option'][1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Category'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Family Expense'])[1]"))
        ).click()

        Enter_value_5 = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Value'])[6]"))
        )
        Enter_value_5.clear()
        Enter_value_5.send_keys("18000")

        time.sleep(3)


        #COMMITMENTS

        commitments = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='III. COMMITMENTS (IF ANY - MONTHLY BASIS)'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", commitments)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(@class, 'btn back-btn') and contains(@class, 'p-button') and contains(., 'Add Commitment')]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-dropdown[@placeholder='Select Applicant/CoApplicant']//div[@class='text-left p-dropdown p-component']//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//ul[@role='listbox']//li[@role='option'][1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Category'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Chitty'])[1]"))
        ).click()

        Enter_value_6 = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Value'])[7]"))
        )
        Enter_value_6.clear()
        Enter_value_6.send_keys("8000")

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(@class, 'btn back-btn') and contains(@class, 'p-button') and contains(., 'Add Commitment')]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p-dropdown[@placeholder='Select Applicant/CoApplicant']//div[@class='text-left p-dropdown p-component']//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//ul[@role='listbox']//li[@role='option'][1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Category'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Insurance'])[1]"))
        ).click()

        Enter_value_7 = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter Value'])[8]"))
        )
        Enter_value_7.clear()
        Enter_value_7.send_keys("13000")

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-plus'])[4]"))
        ).click()

        add_foir = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Select Applicant/CoApplicant'])[1]"))
        )
        add_foir.click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//ul[@role='listbox']//li[@role='option'][1]"))
        ).click()


        time.sleep(3)

        per_foir = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter FOIR Percentage'])[1]"))
        )
        per_foir.clear()
        per_foir.send_keys("80")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@placeholder='Enter Remarks'])[1]"))
        ).send_keys("There are two types of clauses: independent and non-independent/interdependent. An independent clause realises a speech act such as a statement, a question, a command or an offer. A non-independent clause does not realise any act. A non-independent clause (simplex or complex) is usually logically related to other non-independent clauses. Together, they usually constitute a single independent clause (complex). For that reason, non-independent clauses are also called interdependent. For instance, the non-")
                           
        login.implicitly_wait(4)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save Financials'])[1]"))
        ).click()


        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        ) 
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)


        cash_flow_report = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Generate Cash Flow'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", cash_flow_report)
        cash_flow_report.click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='fs-5 pi pi-times'])[1]"))
        ).click()

        print("Generated Cash Flow for Sales Officer")

        time.sleep(3)
        legal_validation = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Legal Validation and Property Valuation'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", legal_validation)
        
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@aria-controls='flush-collapseTwo'])[1]"))
        ).click()
        
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

            

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Owner First Name'])[1]"))
        ).send_keys(first_name)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Owner Last Name'])[1]"))
        ).send_keys(last_name)


        # file_path = r"F:\UI Automation\JaldeeUI.Automation\Selenium Project\Data\address.txt"
        # # Open the file in 'w' mode (create the file if it doesn't exist, overwrite it if it does)
        # with open(file_path, 'r') as file:
        #     fake_india_address = file.read()

        # print("Address obtained :",fake_india_address)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Owner Address'])[1]"))
        ).send_keys("Thrissur, guruvayoor")

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[19]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Father'])[1]"))
        ).click()


        # option_other = wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//span[normalize-space()='Other'])[1]"))
        # )
        # login.execute_script("arguments[0].scrollIntoView();", option_other)
        # time.sleep(3)
        # option_other.click()


        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[20]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Agriculture Land'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='In Cent']"))
        ).send_keys("35")

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Nature of deed'])[1]"))
        ).send_keys("None")

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[21]"))
        ).click()
        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Four Wheeler'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Road Width'])[1]"))
        ).send_keys("4")

        #Land Details

        land = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Land Details'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", land)
        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='District'])[1]"))
        ).send_keys("Thrissur")
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Sub Reg.Office'])[1]"))
        ).send_keys("Kottapadi")
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Taluk'])[1]"))
        ).send_keys("chavakad")
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Corporation/Municipality/Panchayath'])[1]"))
        ).send_keys("Guruvayur")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Village'])[1]"))
        ).send_keys("Kottapadi")
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Desham'])[1]"))
        ).send_keys("Pokode")
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Block No'])[1]"))
        ).send_keys("3")
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Survey No'])[1]"))
        ).send_keys("302")
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Area'])[1]"))
        ).send_keys("kottapadi")
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Classification'])[1]"))
        ).send_keys("Agriculture")

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[22]"))
        ).click()

        login.find_element(By.XPATH, "(//span[normalize-space()='Plot'])[1]").click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[23]"))
        ).click()
        time.sleep(3)
        login.find_element(By.XPATH, "(//span[normalize-space()='Residential'])[1]").click()
        time.sleep(3)
        login.find_element(By.XPATH, "(//input[@placeholder='Usage Restriction'])[1]").send_keys("None")   

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[24]"))
        ).click()

        time.sleep(3)
        login.find_element(By.XPATH, "(//span[normalize-space()='Not Specified'])[1]").click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[25]"))
        ).click()
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Owner Occupied'])[1]"))
        ).click()


        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//input[@type='radio'])[9]"))
        # ).click()

#Description of the property 

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Property Level and Shape'])[1]"))
        ).send_keys("square")

        wait.until(
           EC.presence_of_element_located(
               (By.XPATH, "(//input[@placeholder='How the property was identified'])[1]")) 
        ).send_keys("Agricultural Plot")

#Doc No , Registration Date

        doc_no = "doc_" + str(uuid.uuid4())[:4]
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Doc No'])[1]"))
        ).send_keys(doc_no)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[name()='svg'][@class='p-icon'])[1]"))
        ).click()

        login.find_element(By.XPATH, "//button[normalize-space()='2025']").click()

        # Wait until the backward arrow is clickable before clicking it
        backward_arrow = WebDriverWait(login, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'p-ripple') and contains(@class, 'p-element') and contains(@class, 'p-datepicker-prev') and contains(@class, 'p-link') and contains(@class, 'ng-star-inserted')]")
            )
        )

       
        for _ in range(4):
            backward_arrow.click()

        
        [year, month, day] = Generate_dob()
        print(f"Year: {year}, Month: {month}, Day: {day}")

        time.sleep(2)
        # Select Year
        year_xpath = f"//span[normalize-space()='{year}']"
        WebDriverWait(login, 20).until(
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

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Load Bearing Structure'])[1]"))
        ).send_keys("Bricks and stones")


        wait.until(
            EC.presence_of_element_located (
                (By.XPATH, "(//input[@placeholder='Framed structure'])[1]"))
        ).send_keys("Beam")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@type='radio'])[11]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@type='radio'])[13]"))
        ).click()

#Documents Produced For Verification

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[28]"))
        ).click()

        login.find_element(By.XPATH, "(//span[normalize-space()='Photo Copy'])[1]").click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[29]"))
        ).click()
        login.find_element(By.XPATH, "(//span[normalize-space()='Photo Copy'])[1]").click()

        login.find_element(By.XPATH, "(//input[@type='radio'])[15]").click()
        login.find_element(By.XPATH, "(//label[contains(text(),'Yes')])[11]").click()
        login.find_element(By.XPATH, "(//input[@type='radio'])[23]").click()
        login.find_element(By.XPATH, "(//input[@type='radio'])[25]").click()
        login.find_element(By.XPATH, "(//input[@type='radio'])[15]").click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@placeholder='Enter Brief description about the derivation of the title of the Property / Remarks'])[1]"))
        ).send_keys("Load-bearing structures are built with walls that support the weight of the building, while framed structures are built with a separate framework of beams, columns, and slabs")


        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@placeholder='Enter Any Other Observations'])[1]"))
        ).send_keys("A sentence is typically associated with a clause. A clause can either be a clause simplex or a clause complex. A clause simplex represents a single process going on through time.")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@placeholder='Enter Final Opinion'])[1]"))
        ).send_keys("Approved")


        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save Details'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        legal_report = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Generate Legal Validation'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", legal_report)
        legal_report.click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='pointer-cursor'])[1]"))
        ).click()

        print("Generate Legal Validation Report")

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Generate Property Valuation'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='pointer-cursor'])[1]"))
        ).click()

        print("Generate Property Valuation Report")

        time.sleep(3)

        sales_info = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@aria-controls='flush-collapseThree'])[1]"))
        )
        sales_info.click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save Sales Info'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)


        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@type='text'])[1]"))
        ).send_keys("Document Collection Remarks")

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Proceed'])[1]"))
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
@allure.title("Credit Head Document Verification")
@pytest.mark.parametrize("url, username, password", [(scale_url, credit_head, password)])
def test_credit_head_report(login):

    try:
        
        time.sleep(3)
        wait = WebDriverWait(login, 20)
        print("Sales Officer report")
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Processing Files'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='add-btn btn started ng-star-inserted'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@placeholder='Enter Remarks'])[4]"))
        ).send_keys("Document Verification Remarks")

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='p-element p-button-primary p-button p-component ng-star-inserted'])[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-times'])[2]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Approve'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        time.sleep(3)

# Credit Verification

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Update'])[1]"))
        ).click()

        time.sleep(3)
        credit_report = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Generate Credit Reports'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", credit_report)

        credit_report.click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@aria-controls='flush-collapseParent'])[2]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@aria-controls='flush-collapseOne'])[2]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Generate Cash Flow'])[2]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='fs-5 pi pi-times'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@aria-controls='flush-collapseTwo'])[2]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Generate Legal Validation'])[2]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='fs-5 pi pi-times'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Generate Property Valuation'])[2]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='fs-5 pi pi-times'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@aria-controls='flush-collapseFour'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Generate'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Generate CAM'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='fs-5 pi pi-times'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Save Cam Details'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)  

        time.sleep(3)

        credit_doc_verfication = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@placeholder='Enter Remarks'])[5]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", credit_doc_verfication)
        credit_doc_verfication.send_keys("Credit Verification Remarks")

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Recommend'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        
        time.sleep(3)
        home_button = WebDriverWait(login, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@id='kt_quick_user_toggle']//span[contains(@class, 'bname')]")
        )
        )
        login.execute_script("arguments[0].click();", home_button)

        time.sleep(3)
        signout_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Sign Out']"))
        )
        login.execute_script("arguments[0].click();", signout_button)

        time.sleep(3)
        print("Login with Branch Manager")
        login_id = login.find_element(By.XPATH, "//input[@id='loginId']")
        login_id.clear()
        login_id.send_keys("001923 ")

        password = login.find_element(By.XPATH, "//input[@id='password']")
        password.clear()
        password.send_keys("Jaldee01")

        login.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(3)
        wait = WebDriverWait(login, 20)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Processing Files'])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Update'])[1]"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Generate Branch Reports'])[1]"))
        ).click()


        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@aria-controls ='flush-collapseParent'])[3]"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@aria-controls='flush-collapseFour'])[2]"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Generate CAM'])[2]"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='fs-5 pi pi-times'])[1]"))
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@placeholder='Enter Remarks'])[5]"))
        ).send_keys("Branch Manager Remarks")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Sanction'])[1]"))
        ).click()


        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)


        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='pi pi-sign-in'])[1]"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Yes'])[1]"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)


        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='add-btn btn btn-verified started ng-star-inserted'][normalize-space()='View'])[2]"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Approved Report'])[1]"))
        ).click()

        time.sleep(3)
         
    except Exception as e:
        allure.attach(# use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Credit Head Document Verification")
@pytest.mark.parametrize("url, username, password", [(scale_url, credit_head, password)])
def test_marketing_activity(login):

    try:

        wait = WebDriverWait(login, 20)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Marketing Activity')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Create Task'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Telecalling')]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter activity description']"))
        ).send_keys("Call the customer for loan promotion")

        time.sleep(2)
        element = login.find_element(By.XPATH, "//input[@formcontrolname='areaName']")
        element.send_keys("Round North")

        time.sleep(2) 
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='fa fa-user'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Search by employee details'])[1]"))
        ).send_keys("sures")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[normalize-space()='Suresh'])[1]"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Assign'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[1]"))
        ).click()

        [year,month,day] = add_days(15)
        # print(f"Rescheduling to: {year}-{month}-{day}")
        print(year)
        print(month)
        print(day)
        month = month.upper()
        time.sleep(2)
        ploygon_point = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[2]"))
        )
        login.execute_script("arguments[0].click();", ploygon_point)

        year_xpath = f"//span[normalize-space()='{year}']"
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, year_xpath))
        ).click()
        time.sleep(2)
        month_xpath = f"//span[normalize-space()='{month}']"
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, month_xpath))
        ).click()
        time.sleep(5)
        day_xpath = f"//span[normalize-space()='{day}']"
       
        time.sleep(1)
        day_button = WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, day_xpath))
        )
        login.execute_script("arguments[0].click();", day_button)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Save'])[1]"))
        ).click()

        snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)
        time.sleep(3)

        home_button = WebDriverWait(login, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@id='kt_quick_user_toggle']//span[contains(@class, 'bname')]")
        )
        )
        login.execute_script("arguments[0].click();", home_button)

        time.sleep(2)
        signout_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Sign Out']"))
        )
        login.execute_script("arguments[0].click();", signout_button)

        print("login with assigned user")
        login_id = login.find_element(By.XPATH, "//input[@id='loginId']")
        login_id.clear()
        login_id.send_keys("001920")

        password = login.find_element(By.XPATH, "//input[@id='password']")
        password.clear()
        password.send_keys("Jaldee01")

        login.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[contains(text(),'Marketing Activity')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//tr)[2]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='text-dark btn-text'])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Choose Files'])[1]"))
        ).click()

        time.sleep(3)
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\Financial Sample.xlsx")
        )
        pyautogui.write(absolute_path)
        time.sleep(2)
        pyautogui.press("enter")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Upload'])[1]"))
        ).click()

        snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)
        time.sleep(3)

        # time.sleep(1)
        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//i[@class='fa fa-eye'])[1]"))
        # ).click()
        # time.sleep(3)

        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "(//i[@class='fa fa-times'])[1]"))
        # ).click()
 
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@placeholder='Enter remarks description'])[1]"))
        ).send_keys("Task Compeleted")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Enter activity number'])[1]"))
        ).send_keys("105")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='No of data collected'])[1]"))
        ).send_keys("68")

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Complete'])[1]"))
        ).click()

        snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)
        time.sleep(3)

    except Exception as e:
        allure.attach(# use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
        
        

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Branch Tranfer fron Lead")
@pytest.mark.parametrize("url, username, password", [(scale_url, credit_head, password)])
def test_(login):

    try:

        time.sleep(3)


    except Exception as e:
        allure.attach(# use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e