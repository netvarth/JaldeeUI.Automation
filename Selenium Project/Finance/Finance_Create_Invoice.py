from Framework.common_utils import *
import allure
from allure_commons.types import AttachmentType
from Framework.consumer_common_utils import *
import os
first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create the Invoice for Booking and pay by cash from Finance Module")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_Finance_Create_Invoice_Booking(login):
    wait= WebDriverWait(login, 30)
    try:
        time.sleep(5)
        wait_and_click(login, By.XPATH, "(//div[contains(text(),'Finance')])[1]")

        time.sleep(3)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Create Invoice'])[1]")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Enter Name or Phone or Email or Id'])[1]", "920720600")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Id : 2'])[1]")

        time.sleep(3)
        referal_number = f"REF-{random.randint(100000, 999999)}"
        # wait_and_click(login, By.XPATH, "(//input[@placeholder='Referal Number'])[1]")
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Referal Number'])[1]", referal_number)
        print("Referral Number:", referal_number)  


        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        # Calculate today + 5 days
        today = datetime.today()
        future_date = today + timedelta(days=5)
        future_day = future_date.day
        future_month = future_date.strftime("%B")   # e.g., 'October'
        future_year = future_date.year              # int

        while True:
            # Example header text: "September 2025"
            header_text = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "p-datepicker-title"))
            ).text.strip()

            # Split into month and year
            current_month, current_year = header_text.split()
            current_year = int(current_year)

            if current_month == future_month and current_year == future_year:
                break  # ✅ target month/year reached

            # Compare dates
            current_date = datetime.strptime(f"{current_month} {current_year}", "%B %Y")

            if current_date < future_date:
                # Need to go forward
                next_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "p-datepicker-next")))
                next_btn.click()
            else:
                # (Optional) Go backward if future_date is before current_date
                prev_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "p-datepicker-prev")))
                prev_btn.click()

            time.sleep(0.5)

        # ✅ Once correct month/year → pick the day
        future_day_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//td//span[normalize-space()='{future_day}']"))
        )
        future_day_element.click()
        
        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='ENT'])[1]")

        login.implicitly_wait(5)

        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Let your patient know what this invoice is for'])[1]", "Booking Invoice")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//button[normalize-space()='Add Procedure/Item'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//input[@placeholder='Choose Procedure/Item'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//div[@class='item-name'][normalize-space()='Consultation'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//input[@id='from'])[2]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "//td[contains(@class,'p-datepicker-today')]//span") 

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//button[normalize-space()='Add'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "//button[contains(@class,'invoice-update-btn') and normalize-space()='Update']")

        message = get_snack_bar_message(login)
        print("Snack bar message:", message)

        time.sleep(5)

        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Pay by Cash'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//button[normalize-space()='Pay'])[1]")

        login.implicitly_wait(5)    
        wait_and_click(login, By.XPATH, "(//button[normalize-space()='Yes'])[1]")

        message = get_snack_bar_message(login)
        print("Snack bar message:", message)

        time.sleep(3)

        wait_and_click(login, By.XPATH, "(//i[@class='fa fa-arrow-left'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "//img[contains(@src,'viewinvoice.gif')]/following-sibling::span[normalize-space()='Invoices']")

        login.implicitly_wait(5)
        #Get first invoice ID dynamically
        first_invoice_id = login.find_element(
            By.XPATH, "(//tbody[@class='p-element p-datatable-tbody']//tr/td[1]/span)[1]"
        ).text
        print(f"First Invoice ID: {first_invoice_id}")

        # Get first row (latest invoice)
        first_row = login.find_element(
            By.XPATH, "(//tbody[@class='p-element p-datatable-tbody']//tr)[1]"
        )

        # Get status of first invoice
        status = first_row.find_element(
            By.XPATH, ".//td/span[contains(text(),'Paid')]"
        ).text
        print(f"Status for Invoice {first_invoice_id}: {status}")

        # Click "View" button of first invoice
        view_button = first_row.find_element(
            By.XPATH, ".//button[span[normalize-space()='View']]"
        )
        view_button.click()

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create the Invoice for Booking and Settled from Finance Module")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_Finance_Create_Invoice_Booking_settled(login):
    wait= WebDriverWait(login, 30)
    try:
        time.sleep(5)
        wait_and_click(login, By.XPATH, "(//div[contains(text(),'Finance')])[1]")

        time.sleep(3)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Create Invoice'])[1]")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Enter Name or Phone or Email or Id'])[1]", "920720600")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Id : 2'])[1]")

        time.sleep(3)
        referral_number = f"REF-{random.randint(100000, 999999)}"
        # wait_and_click(login, By.XPATH, "(//input[@placeholder='Referal Number'])[1]")
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Referal Number'])[1]", referral_number)
        print("Referral Number:", referral_number)  


        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        # Calculate today + 5 days
        today = datetime.today()
        future_date = today + timedelta(days=5)
        future_day = future_date.day
        future_month = future_date.strftime("%B")   # e.g., 'October'
        future_year = future_date.year              # int

        while True:
            # Example header text: "September 2025"
            header_text = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "p-datepicker-title"))
            ).text.strip()

            # Split into month and year
            current_month, current_year = header_text.split()
            current_year = int(current_year)

            if current_month == future_month and current_year == future_year:
                break  # ✅ target month/year reached

            # Compare dates
            current_date = datetime.strptime(f"{current_month} {current_year}", "%B %Y")

            if current_date < future_date:
                # Need to go forward
                next_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "p-datepicker-next")))
                next_btn.click()
            else:
                # (Optional) Go backward if future_date is before current_date
                prev_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "p-datepicker-prev")))
                prev_btn.click()

            time.sleep(0.5)

        # ✅ Once correct month/year → pick the day
        future_day_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//td//span[normalize-space()='{future_day}']"))
        )
        future_day_element.click()
        
        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='ENT'])[1]")

        login.implicitly_wait(5)

        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Let your patient know what this invoice is for'])[1]", "Booking Invoice")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//button[normalize-space()='Add Procedure/Item'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//input[@placeholder='Choose Procedure/Item'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//div[@class='item-name'][normalize-space()='Consultation'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//input[@id='from'])[2]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "//td[contains(@class,'p-datepicker-today')]//span") 

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//button[normalize-space()='Add'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "//button[contains(@class,'invoice-update-btn') and normalize-space()='Update']")

        message = get_snack_bar_message(login)
        print("Snack bar message:", message)

        time.sleep(3)

        wait_and_click(login, By.XPATH, "(//button[normalize-space()='Settle Invoice'])[1]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//button[normalize-space()='Confirm & Settle Invoice'])[1]")

        message = get_snack_bar_message(login)
        print("Snack bar message:", message)

        time.sleep(3)

        wait_and_click(login, By.XPATH, "(//i[@class='fa fa-arrow-left'])[1]")
        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "//img[contains(@src,'viewinvoice.gif')]/following-sibling::span[normalize-space()='Invoices']")

        login.implicitly_wait(5)
        #Get first invoice ID dynamically
        first_invoice_id = login.find_element(
            By.XPATH, "(//tbody[@class='p-element p-datatable-tbody']//tr/td[1]/span)[1]"
        ).text
        print(f"First Invoice ID: {first_invoice_id}")

        # Get first row (latest invoice)
        first_row = login.find_element(
            By.XPATH, "(//tbody[@class='p-element p-datatable-tbody']//tr)[1]"
        )

        # Get status of first invoice
        status = first_row.find_element(
            By.XPATH, ".//td/span[contains(text(),'Settled')]"
        ).text
        print(f"Status for Invoice {first_invoice_id}: {status}")

        # Click "View" button of first invoice
        view_button = first_row.find_element(
            By.XPATH, ".//button[span[normalize-space()='View']]"
        )
        view_button.click()


    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create the Invoice for Booking and Share payment link from Finance Module")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_Finance_Create_Invoice_Booking_Sharepaymentlink(login):
    wait = WebDriverWait(login, 30)
    try:
        time.sleep(5)
        wait_and_click(login, By.XPATH, "(//div[contains(text(),'Finance')])[1]")

        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Create Invoice'])[1]")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Enter Name or Phone or Email or Id'])[1]", "920720600")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Id : 2'])[1]")

        time.sleep(3)
        referral_number = f"REF-{random.randint(100000, 999999)}"
        # wait_and_click(login, By.XPATH, "(//input[@placeholder='Referal Number'])[1]")
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Referal Number'])[1]", referral_number)
        print("Referral Number:", referral_number)  


        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        # Calculate today + 5 days
        today = datetime.today()
        future_date = today + timedelta(days=5)
        future_day = future_date.day
        future_month = future_date.strftime("%B")   # e.g., 'October'
        future_year = future_date.year              # int

        while True:
            # Example header text: "September 2025"
            header_text = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "p-datepicker-title"))
            ).text.strip()

            # Split into month and year
            current_month, current_year = header_text.split()
            current_year = int(current_year)

            if current_month == future_month and current_year == future_year:
                break  # ✅ target month/year reached

            # Compare dates
            current_date = datetime.strptime(f"{current_month} {current_year}", "%B %Y")

            if current_date < future_date:
                # Need to go forward
                next_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "p-datepicker-next")))
                next_btn.click()
            else:
                # (Optional) Go backward if future_date is before current_date
                prev_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "p-datepicker-prev")))
                prev_btn.click()

            time.sleep(0.5)

        # ✅ Once correct month/year → pick the day
        future_day_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//td//span[normalize-space()='{future_day}']"))
        )
        future_day_element.click()
        
        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='ENT'])[1]")

        login.implicitly_wait(5)

        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Let your patient know what this invoice is for'])[1]", "Booking Invoice")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//button[normalize-space()='Add Procedure/Item'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//input[@placeholder='Choose Procedure/Item'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//div[@class='item-name'][normalize-space()='Consultation'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//input[@id='from'])[2]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "//td[contains(@class,'p-datepicker-today')]//span") 

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//button[normalize-space()='Add'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "//button[contains(@class,'invoice-update-btn') and normalize-space()='Update']")

        message = get_snack_bar_message(login)
        print("Snack bar message:", message)

        time.sleep(5)

        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Share Payment Link'])[1]")

        time.sleep(1)
        wait_and_click(login, By.XPATH, "(//span[@class='mdc-button__label'])[1]")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)

        time.sleep(3)

        wait_and_click(login, By.XPATH, "(//i[@class='fa fa-arrow-left'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "//img[contains(@src,'viewinvoice.gif')]/following-sibling::span[normalize-space()='Invoices']")

        login.implicitly_wait(5)
        #Get first invoice ID dynamically
        first_invoice_id = login.find_element(
            By.XPATH, "(//tbody[@class='p-element p-datatable-tbody']//tr/td[1]/span)[1]"
        ).text
        print(f"First Invoice ID: {first_invoice_id}")

        # Get first row (latest invoice)
        first_row = login.find_element(
            By.XPATH, "(//tbody[@class='p-element p-datatable-tbody']//tr)[1]"
        )

        # Get status of first invoice
        status = first_row.find_element(
            By.XPATH, ".//td/span[contains(text(),'Not Paid')]"
        ).text
        print(f"Status for Invoice {first_invoice_id}: {status}")

        # Click "View" button of first invoice
        view_button = first_row.find_element(
            By.XPATH, ".//button[span[normalize-space()='View']]"
        )
        view_button.click()


    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create the Invoice for Booking and Share payment link from Finance Module")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_Finance_Create_Invoice_Booking_Cancelled(login):
    wait = WebDriverWait(login, 30)
    try:
        time.sleep(5)
        wait_and_click(login, By.XPATH, "(//div[contains(text(),'Finance')])[1]")

        time.sleep(3)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Create Invoice'])[1]")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Enter Name or Phone or Email or Id'])[1]", "920720600")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Id : 2'])[1]")

        time.sleep(3)
        referral_number = f"REF-{random.randint(100000, 999999)}"
        # wait_and_click(login, By.XPATH, "(//input[@placeholder='Referal Number'])[1]")
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Referal Number'])[1]", referral_number)
        print("Referral Number:", referral_number)  


        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        # Calculate today + 5 days
        today = datetime.today()
        future_date = today + timedelta(days=5)
        future_day = future_date.day
        future_month = future_date.strftime("%B")   # e.g., 'October'
        future_year = future_date.year              # int

        while True:
            # Example header text: "September 2025"
            header_text = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "p-datepicker-title"))
            ).text.strip()

            # Split into month and year
            current_month, current_year = header_text.split()
            current_year = int(current_year)

            if current_month == future_month and current_year == future_year:
                break  # ✅ target month/year reached

            # Compare dates
            current_date = datetime.strptime(f"{current_month} {current_year}", "%B %Y")

            if current_date < future_date:
                # Need to go forward
                next_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "p-datepicker-next")))
                next_btn.click()
            else:
                # (Optional) Go backward if future_date is before current_date
                prev_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "p-datepicker-prev")))
                prev_btn.click()

            time.sleep(0.5)

        # ✅ Once correct month/year → pick the day
        future_day_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//td//span[normalize-space()='{future_day}']"))
        )
        future_day_element.click()
        
        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='ENT'])[1]")

        login.implicitly_wait(5)

        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Let your patient know what this invoice is for'])[1]", "Booking Invoice")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//button[normalize-space()='Add Procedure/Item'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//input[@placeholder='Choose Procedure/Item'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//div[@class='item-name'][normalize-space()='Consultation'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//input[@id='from'])[2]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "//td[contains(@class,'p-datepicker-today')]//span") 

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//button[normalize-space()='Add'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "//button[contains(@class,'invoice-update-btn') and normalize-space()='Update']")

        message = get_snack_bar_message(login)
        print("Snack bar message:", message)

        time.sleep(5)
        wait_and_click(login, By.XPATH, "(//button[normalize-space()='Cancel Invoice'])[1]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//button[@class='cs-btn btn btn-primary settle-button'])[1]")

        message = get_snack_bar_message(login)
        print("Snack bar message:", message)

        time.sleep(3)

        wait_and_click(login, By.XPATH, "(//i[@class='fa fa-arrow-left'])[1]")
        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "//img[contains(@src,'viewinvoice.gif')]/following-sibling::span[normalize-space()='Invoices']")

        login.implicitly_wait(5)
        #Get first invoice ID dynamically
        first_invoice_id = login.find_element(
            By.XPATH, "(//tbody[@class='p-element p-datatable-tbody']//tr/td[1]/span)[1]"
        ).text
        print(f"First Invoice ID: {first_invoice_id}")

        # Get first row (latest invoice)
        first_row = login.find_element(
            By.XPATH, "(//tbody[@class='p-element p-datatable-tbody']//tr)[1]"
        )

        # Get status of first invoice
        status = first_row.find_element(
            By.XPATH, ".//td/span[contains(text(),'Cancelled')]"
        ).text
        print(f"Status for Invoice {first_invoice_id}: {status}")

        # Click "View" button of first invoice
        view_button = first_row.find_element(
            By.XPATH, ".//button[span[normalize-space()='View']]"
        )
        view_button.click()



    except Exception as e:
        allure.attach(  
        login.get_screenshot_as_png(),  
        name="full_page",  
        attachment_type=AttachmentType.PNG,
        ) 
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create Expense from Finance Module and change the status to Approved and Convert to Payout")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_create_expense_to_approved_and_convert_to_payout(login):
    wait = WebDriverWait(login, 30)
    try:
        time.sleep(5)
        wait_and_click(login, By.XPATH, "(//div[contains(text(),'Finance')])[1]")

        time.sleep(3)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Create Expense'])[1]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Purchase'])[1]")

        time.sleep(1)
        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Chavakkad'])[1]")

        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, "(//input[@id='expenseFor'])[1]", "Office Supplies")

        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, "(//input[@id='amount'])[1]", "1600")

        time.sleep(1)
        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]")

        time.sleep(2)
        
        wait_and_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='whiteboard transparent networks'])[1]")  

        time.sleep(3)
        wait_and_click(login, By.XPATH, "//button[.//span[normalize-space()='Save']]")

        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)

        time.sleep(5)

        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Expenses'])[1]")
        time.sleep(2)
        menu_button =  "//table[contains(@class,'p-datatable-table')]//tbody/tr[1]//button[@aria-haspopup='menu']"
        wait_and_locate_click(login, By.XPATH, menu_button)
        
        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Change Status'])[1]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//div[contains(text(),'Approved')])[1]")

        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)

        Approved_status_element = wait.until(
        EC.presence_of_element_located(
        (By.XPATH, "(//table[contains(@class,'p-datatable-table')]//tbody/tr[1]//span[normalize-space()='Approved'])[1]")
            )
        )
        Approved_status_text = Approved_status_element.text
        print(f"Status: {Approved_status_text}")
        assert Approved_status_text == "Approved", f"Expected 'Approved' status, but got {Approved_status_text}"

        menu_button =  "//table[contains(@class,'p-datatable-table')]//tbody/tr[1]//button[@aria-haspopup='menu']"
        wait_and_locate_click(login, By.XPATH, menu_button)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Convert to Payout'])[1]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='mdc-button__label'])[1]")

        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)

        Converted_status_element = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//table[contains(@class,'p-datatable-table')]//tbody/tr[1]//span[normalize-space()='Converted'])[1]")
            )
        )
        Converted_status_text = Converted_status_element.text
        print(f"Status: {Converted_status_text}")
        assert Converted_status_text == "Converted", f"Expected 'Converted' status, but got {Converted_status_text}"


        time.sleep(3)

    except Exception as e:
       allure.attach(
           login.get_screenshot_as_png(),
           name="full_page",
           attachment_type=AttachmentType.PNG,
       )

       raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create Revenue and Approved")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_create_revenue(login):
    wait = WebDriverWait(login, 30)
    try:
        time.sleep(3)
        wait_and_click(login, By.XPATH, "(//div[contains(text(),'Finance')])[1]")
        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Add Revenue'])[1]")
        time.sleep(2)

        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")
        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Chavakkad'])[1]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Booking Invoice'])[1]")

        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, "(//input[@id='paymentsInLabel'])[1]", "Booking")

        time.sleep(2)
        referenceNo = f"REF-{random.randint(100000, 999999)}"
        # wait_and_click(login, By.XPATH, "(//input[@placeholder='Referal Number'])[1]")
        wait_and_send_keys(login, By.XPATH, "(//input[@id='referenceNo'])[1]", referenceNo)
        print("Reference Number:", referenceNo) 

        time.sleep(2)
        Amount_element = f"{random.randint(2000, 5999)}"
        wait_and_send_keys(login, By.XPATH, "(//input[@id='amount'])[1]", Amount_element)
        print("Amount :", Amount_element)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]")
        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='whiteboard transparent networks'])[1]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='mdc-button__label'])[1]")

        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(5)


        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Revenue'])[1]")
        time.sleep(3)
        menu_button =  "//table[contains(@class,'p-datatable-table')]//tbody/tr[1]//button[@aria-haspopup='menu']"
        wait_and_locate_click(login, By.XPATH, menu_button)
        
        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Change Status'])[1]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//div[contains(text(),'Approved')])[1]")

        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)

        Approved_status_element = wait.until(
        EC.presence_of_element_located(
        (By.XPATH, "(//table[contains(@class,'p-datatable-table')]//tbody/tr[1]//span[normalize-space()='Approved'])[1]")
            )
        )
        Approved_status_text = Approved_status_element.text
        print(f"Status: {Approved_status_text}")
        assert Approved_status_text == "Approved", f"Expected 'Approved' status, but got {Approved_status_text}"

        time.sleep(5)

    except Exception as e:
       allure.attach(
           login.get_screenshot_as_png(),
           name="full_page",
           attachment_type=AttachmentType.PNG,
       )
       raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create Invoice on Finance Dasahboard with Service Date")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_createinvoice_servicedate(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Create Invoice']") 
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Name or Phone or Email or Id']", 9207206005) 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space(.)='Id : 2'])[1]")
        time.sleep(2)
        WebDriverWait(login, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='p-button-label']")
            )
        ).click()
        time.sleep(2)
        billings = WebDriverWait(login, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='mt-3 Billing-Address ng-star-inserted'])[1]")
            )
        )
        billings.click()
        time.sleep(3)
        textarea = WebDriverWait(login, 15).until(
            EC.visibility_of_element_located((By.XPATH, "(//div[@class='mt-3 Billing-Address ng-star-inserted']//textarea)[1]"))
        )
        textarea.click()
        random_billing_address = generate_random_billing_address()
        textarea.send_keys(random_billing_address)
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-label']") 
        time.sleep(2)
        reference_number = str(uuid.uuid4())
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Referal Number']", reference_number) 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add Procedure/Item']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//div[@class='item-name'][normalize-space()='Consultation']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[3]")
        time.sleep(3)
        today_date = datetime.now()
        today = today_date.day
        formatted_date = today_date.strftime("%d-%m-%Y")
        today_xpath = f"//td[contains(@class, 'p-datepicker-today')]/span[text()='{today}']"
        invoice_today = WebDriverWait(login, 15).until(
            EC.presence_of_element_located((By.XPATH, today_xpath))
        )
        invoice_today.click()
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add']")
        time.sleep(3)
        invoice_service_date1 = f"//tbody//tr[@class='service-name ng-star-inserted']//td[normalize-space() ='{formatted_date}']"
        invoice_service_date_xpath1 = login.find_element(By.XPATH, invoice_service_date1)
        actual__invoice_Service_date = invoice_service_date_xpath1.text
        print("actual__invoice_Service_date:", actual__invoice_Service_date)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Private Note']", "invoice for consultation")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Shared with patient']", "invoice for consultation shared")
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Terms and condition']", "T&C")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[normalize-space(.)='Update'])[1]")
        time.sleep(2)
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(2)
        invoice_service_date = f"//td[@class='quantity tb-display-none'][normalize-space()='{formatted_date}']"
        invoice_service_date_xpath = WebDriverWait(login, 15).until(
            EC.presence_of_element_located((By.XPATH, invoice_service_date))
        )
        Expected_invoice_Service_date = invoice_service_date_xpath.text
        print("Expected_invoice_Service_date :", Expected_invoice_Service_date)
        print(f"Expected_invoice_Service_date : {Expected_invoice_Service_date} but got actual__invoice_Service_date : {actual__invoice_Service_date}")
        assert actual__invoice_Service_date == Expected_invoice_Service_date, f"Expected_invoice_Service_date : {Expected_invoice_Service_date} but got actual__invoice_Service_date : {actual__invoice_Service_date}"
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Share Payment Link']")
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='mdc-button__label']")
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)
        time.sleep(3)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e    
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create Invoice on Finance Dasahboard and save as template")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_createinvoice_saveastemplate(login):
    wait = WebDriverWait(login, 30)
    try: 
        time.sleep(5)
        wait_and_click(login, By.XPATH, "(//div[contains(text(),'Finance')])[1]")

        time.sleep(3)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Create Invoice'])[1]")

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Enter Name or Phone or Email or Id'])[1]", "920720600")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Id : 2'])[1]")

        time.sleep(3)
        referal_number = f"REF-{random.randint(100000, 999999)}"
        # wait_and_click(login, By.XPATH, "(//input[@placeholder='Referal Number'])[1]")
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Referal Number'])[1]", referal_number)
        print("Referral Number:", referal_number)  


        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='p-icon'])[2]")

        # Calculate today + 5 days
        today = datetime.today()
        future_date = today + timedelta(days=5)
        future_day = future_date.day
        future_month = future_date.strftime("%B")   # e.g., 'October'
        future_year = future_date.year              # int

        while True:
            # Example header text: "September 2025"
            header_text = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "p-datepicker-title"))
            ).text.strip()

            # Split into month and year
            current_month, current_year = header_text.split()
            current_year = int(current_year)

            if current_month == future_month and current_year == future_year:
                break  # ✅ target month/year reached

            # Compare dates
            current_date = datetime.strptime(f"{current_month} {current_year}", "%B %Y")

            if current_date < future_date:
                # Need to go forward
                next_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "p-datepicker-next")))
                next_btn.click()
            else:
                # (Optional) Go backward if future_date is before current_date
                prev_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "p-datepicker-prev")))
                prev_btn.click()

            time.sleep(0.5)

        # ✅ Once correct month/year → pick the day
        future_day_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//td//span[normalize-space()='{future_day}']"))
        )
        future_day_element.click()
        
        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='ENT'])[1]")

        login.implicitly_wait(5)

        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Let your patient know what this invoice is for'])[1]", "Booking Invoice")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//button[normalize-space()='Add Procedure/Item'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//input[@placeholder='Choose Procedure/Item'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//div[@class='item-name'][normalize-space()='Consultation'])[1]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//input[@id='from'])[2]")

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "//td[contains(@class,'p-datepicker-today')]//span") 

        login.implicitly_wait(5)
        wait_and_click(login, By.XPATH, "(//button[normalize-space()='Add'])[1]")

        time.sleep(3)
        wait_and_click(login, By.XPATH, "(//button[normalize-space()='Save as Template'])[1]")

        temp_name = f"Temp-{random.randint(100000, 999999)}"

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@placeholder='Enter Template Name to Save'])[1]", temp_name)

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//div[normalize-space()='Save'])[1]")

        message = get_snack_bar_message(login)
        print("Snack bar Message:", message)

        time.sleep(5)

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e 
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create a Expense wit auto payout enable and try to to edit")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_createexpense_auto_payout_edit(login):
    wait = WebDriverWait(login, 30)
    try: 
        time.sleep(5)
        wait_and_click(login, By.XPATH, "(//div[contains(text(),'Finance')])[1]")

        time.sleep(3)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Expenses'])[1]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//*[name()='svg'][@class='mdc-switch__icon mdc-switch__icon--off'])[1]")

        message = get_snack_bar_message(login)
        print("Snack bar Message: ", message)
        time.sleep(3)

        wait_and_click(login, By.XPATH, "(//i[@class='fa fa-arrow-left'])[1]")
        time.sleep(2)

        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Expenses'])[1]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "//span[@class='p-button-label']")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Location'])[1]")

        time.sleep(1)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Chavakkad'])[1]")

        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, "(//input[@id='expenseFor'])[1]", "Stock Purchase")

        time.sleep(1)
        referenceNo = f"REF-{random.randint(100000, 999999)}"
        # wait_and_click(login, By.XPATH, "(//input[@placeholder='Referal Number'])[1]")
        wait_and_send_keys(login, By.XPATH, "(//input[@id='referenceNo'])[1]", referenceNo)
        print("Reference Number:", referenceNo) 

        wait_and_send_keys(login, By.XPATH, "(//input[@id='referenceNo'])[1]", referenceNo)

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "(//input[@id='amount'])[1]", "3600")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='MedCC'])[1]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='mdc-button__label'])[1]")

        message = get_snack_bar_message(login)
        print("Snack bar Message :", message)

        time.sleep(3)
        first_row = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//tbody[@class='p-element p-datatable-tbody']/tr)[1]"))
        )
        first_row.click()

        time.sleep(3)

        # Wait for a few seconds to see if the button appears
        WebDriverWait(login, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//button//span[text()='Update']"))
            )
            # If we reach here, button is visible -> FAIL
        assert False, "❌ Update button is visible, but it should NOT be"
    except TimeoutException:
        # Timeout means button is not visible -> PASS
        assert True
    except NoSuchElementException:
        # Element not in DOM at all -> also PASS
        assert True



        time.sleep(5)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create expense for a past date")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_create_expense_past_date(login):
    wait = WebDriverWait(login, 30)
    try: 
        time.sleep(5)
        wait_and_click(login, By.XPATH, "(//div[contains(text(),'Finance')])[1]")

        time.sleep(3)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Create Expense'])[1]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Purchase'])[1]")

        time.sleep(1)
        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Chavakkad'])[1]")

        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, "(//input[@id='expenseFor'])[1]", "Office Supplies")

        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, "(//input[@id='amount'])[1]", "1600")

        time.sleep(1)
        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]")

        time.sleep(2)
        
        wait_and_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='whiteboard transparent networks'])[1]")

        time.sleep(3)
        wait_and_click(login, By.XPATH, "(//input[@id='from'])[1]")

        time.sleep(3)
        wait_and_click(login, By.XPATH, "(//input[@id='from'])[1]")  # open datepicker

        # --- Select past date (go back 1 month, pick 15th) ---
        prev_arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'p-datepicker-prev')]"))
        )
        prev_arrow.click()

        past_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//td[not(contains(@class,'p-disabled'))]/span[normalize-space()='15']"))
        )
        past_date.click()


        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='mdc-button__label'])[1]")
        message  = get_snack_bar_message(login)
        print("Snack bar Message :", message)
        
        time.sleep(5)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create expense for a future date")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_create_expense_future_date(login):
    wait = WebDriverWait(login, 30)
    try:
        time.sleep(5)
        wait_and_click(login, By.XPATH, "(//div[contains(text(),'Finance')])[1]")

        time.sleep(3)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Create Expense'])[1]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Purchase'])[1]")

        time.sleep(1)
        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[normalize-space()='Chavakkad'])[1]")

        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, "(//input[@id='expenseFor'])[1]", "Office Supplies")

        time.sleep(1)
        wait_and_send_keys(login, By.XPATH, "(//input[@id='amount'])[1]", "1600")

        time.sleep(1)
        wait_and_click(login, By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='whiteboard transparent networks'])[1]")

        time.sleep(3)
        wait_and_click(login, By.XPATH, "(//input[@id='from'])[1]")

        time.sleep(1)
        # Example: go forward 1 month and pick 15
        months_forward = 1
        day = "15"

        for _ in range(months_forward):
            next_arrow = WebDriverWait(login, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'p-datepicker-next')]"))
            )
            next_arrow.click()

        # Select the future day (ensure it's not disabled)
        date_xpath = f"//td[not(contains(@class,'p-disabled'))]/span[normalize-space()='{day}']"
        future_date = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, date_xpath))
        )
        future_date.click()

        # ---- Capture and log selected date ----
        today = datetime.today()
        selected_month = today.replace(day=28) + timedelta(days=4)  # jump to next month
        selected_month = selected_month.replace(day=1)              # first day of next month
        selected_date = selected_month.replace(day=int(day))
        formatted_date = selected_date.strftime("%d %B")  # Example: "15 October"

        print(f"Selected Date: {formatted_date}")
        allure.attach(
            f"Selected Date: {formatted_date}",
            name="Selected Future Date",
            attachment_type=AttachmentType.TEXT,
        )

        time.sleep(2)
        wait_and_click(login, By.XPATH, "(//span[@class='mdc-button__label'])[1]")
        message  = get_snack_bar_message(login)
        print("Snack bar Message :", message)
        time.sleep(5)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page",
            attachment_type=AttachmentType.PNG,
        )
        raise e
