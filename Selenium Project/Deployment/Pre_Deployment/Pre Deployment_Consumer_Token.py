import time
from datetime import datetime, timedelta
from Framework.consumer_common_utils import *
import pyautogui
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import os



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Pre-Deployment Consumer Appointment")
@pytest.mark.parametrize("url", [consumer_login_url_1])
def test_consumer_side_token(consumer_login):
    current_date = datetime.now().strftime("%d-%m-%Y")
    print("Pre-Deployment Existing Consumer Token",current_date)
    try:
        time.sleep(5)
        # Scroll to the element
        consultation = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//h3[normalize-space()='GET YOUR CONSULTATION TODAY'])[1]")
            )
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", consultation)
        
        time.sleep(3)
        wait = WebDriverWait(consumer_login, 30)

        book_now_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//button[@id='btnBookNow'])[3]")
            )
        )
        scroll_to_element(consumer_login, book_now_button)

        time.sleep(2)
        book_now_button.click()

        time.sleep(3)



            # wait = WebDriverWait(consumer_login, 10)
        location_button = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='deptName ng-star-inserted'][contains(text(),'Chavakkad')]",
                )
            )
        )
        location_button.click()

        # wait = WebDriverWait(consumer_login, 10)
        depart_button = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='deptName ng-star-inserted'][normalize-space()='ENT']",
                )
            )
        )
        depart_button.click()

        # wait = WebDriverWait(consumer_login, 10)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Dr.Naveen KP')]")
            )
        ).click()

        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//app-checkin-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][normalize-space()='service']",
                )
            )
        ).click()
        time.sleep(3)
        Today_Date = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@aria-pressed='true'][@aria-current='date']")
            )
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", Today_Date)
        time.sleep(2)
        Today_Date.click()
        time.sleep(2)
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(consumer_login, 10)
        queue = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='mdc-evolution-chip__cell mdc-evolution-chip__cell--primary']"))
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", queue)
        time.sleep(2)
        queue.click()
        print("Queue:", queue.text)
        time.sleep(2)
        next_button = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Next']")
            )
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", next_button)
        time.sleep(3)
        next_button.click()
        time.sleep(3)  
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='81234 56789'])[1]"))
        ).send_keys("9207206005")
        
        consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

        time.sleep(5)
        # otp_digits = "5555"
        otp_digits = "5555"
        # Wait for the OTP input fields to be present
        otp_inputs = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )
        for i, otp_input in enumerate(otp_inputs):
            otp_input.send_keys(otp_digits[i])

        consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        time.sleep(3)
        consumer_notes = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Add Notes you may have...']")
            )
        )
        consumer_notes.send_keys("Notes added from consumer side")
        time.sleep(3)
        consumer_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(consumer_login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='uploadFileTxt']"))
        ).click()
        time.sleep(2)

        current_working_directory = os.getcwd()
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        time.sleep(2)
        pyautogui.write(absolute_path)
        time.sleep(2)
        pyautogui.press("enter")

        time.sleep(3)
        confirmbutton = WebDriverWait(consumer_login, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm']")
            )
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", confirmbutton)
        time.sleep(2)
        confirmbutton.click()
        time.sleep(3)

        # Step 1: Extract Booking ID
        booking_id_element = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='bookingIdFlex']/div"))
        )
        booking_id = booking_id_element[1].text.strip()
        print(f"Booking ID: {booking_id}")

        Ok_button = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", Ok_button)
        time.sleep(3)
        Ok_button.click()
        time.sleep(2)
        bookings = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'My Bookings')]")
            )
        )
        bookings.click()
        time.sleep(5)
        # Step 1: Click "Show more" once (if present)
        try:
            show_more = WebDriverWait(consumer_login, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Show more']"))  
            )
            consumer_login.execute_script("arguments[0].scrollIntoView(true);", show_more)
            time.sleep(1)
            show_more.click()
            print("Clicked 'Show more'")
            time.sleep(5)  # Wait for new content to begin loading

            # Scroll to bottom to ensure all lazy-loaded cards are loaded
            last_height = consumer_login.execute_script("return document.body.scrollHeight")
            while True:
                consumer_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                new_height = consumer_login.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            print("Scrolled to bottom to load all cards.")
        except:
            print("No 'Show more' button found or it's already fully expanded.")

        # Step 2: Loop through all loaded cards to find the booking ID
        found = False
        cards = consumer_login.find_elements(By.XPATH, "//app-wl-card")
        print(f"Total cards found: {len(cards)}")

        for card in cards:
            try:
                # card_booking_id_elem = card.find_element(By.XPATH, ".//div[@class='cstmTxt field-head' and text()='Booking Id']/following-sibling::div")
                card_booking_id_elem = card.find_element(
                    By.XPATH,
                    ".//div[normalize-space(text())='Booking Id']/following-sibling::div"
                )

                card_booking_id = card_booking_id_elem.text.strip()
                print(f"Found booking ID in card: '{card_booking_id}'")  # <--- Debug print

                if card_booking_id == booking_id:
                    consumer_login.execute_script("arguments[0].scrollIntoView(true);", card)
                    print(f"Found matching booking ID card: {card_booking_id}")

                    # Click the 3-dot menu inside this card
                    three_dot = card.find_element(By.XPATH, ".//button[.//mat-icon[normalize-space(text())='more_horiz']]")
                    WebDriverWait(consumer_login, 5).until(EC.element_to_be_clickable(three_dot))
                    three_dot.click()
                    print("Clicked 3-dot menu.")
                    found = True
                    break
            except Exception as e:
                print(f"Error processing a card: {e}")

        if not found:
            print("Booking card not found.")

        time.sleep(3)

        wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//span[contains(text(),'Send Message')])[1]"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@id='message'])[1]")
            )
        ).send_keys("Test message from consumer side")

        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btnSelect']//i[@class='material-icons'][normalize-space()='attach_file']"))
        ).click()

        time.sleep(3)

        current_working_directory = os.getcwd()
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        time.sleep(3)
        pyautogui.press("enter")

        time.sleep(3)
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='ng-star-inserted'][normalize-space()='Send'])[1]"))
        ).click()

        toast_message = WebDriverWait(consumer_login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Send Attachments')])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='select-wrapper'])[1]")
            )
        ).click()
        time.sleep(2)
        current_working_directory = os.getcwd()
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        time.sleep(3)
        pyautogui.press("enter")

        time.sleep(2)
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='mdc-button__label'])[1]"))
        ).click()

        toast_message = WebDriverWait(consumer_login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)

        wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'View Attachments')])[1]"))
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='fa fa-window-close'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Reschedule')])[1]"))
        ).click()

        time.sleep(3)
        consumer_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        # Calculate tomorrow's date
        tomorrow_date = datetime.now() + timedelta(days=2)
        # Get the day as an integer to avoid leading zeros
        day = tomorrow_date.day  # e.g., 1 for October 1
        # Format for the XPath
        tomorrow_xpath_expression = f"//span[@class='mat-calendar-body-cell-content mat-focus-indicator'][normalize-space()='{day}']"

        print("Tomorrow's XPath Expression:", tomorrow_xpath_expression)

        # Get current month/year element
        current_month_year = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//button[@aria-label='Choose month and year']//span[@class='mat-mdc-button-persistent-ripple mdc-button__ripple']",
                )
            )
        )

        consumer_login.execute_script("arguments[0].scrollIntoView(true);", current_month_year)

        # Click next month if needed
        if current_month_year.text.lower() != tomorrow_date.strftime('%B %Y').lower():
            consumer_login.find_element(By.XPATH, "//button[@aria-label='Next month']").click()
        time.sleep(3)

        # Wait for tomorrow's date element to be clickable
        Tomorrow_Date = WebDriverWait(consumer_login, 10).until(
            EC.element_to_be_clickable((By.XPATH, tomorrow_xpath_expression))
        )
        # Click on tomorrow's date
        Tomorrow_Date.click()
        print("Clicked on Tomorrow Date:", day)
        time.sleep(2)
        wait = WebDriverWait(consumer_login, 20)
        time_slot = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//span[@class='mdc-evolution-chip__action mat-mdc-chip-action mdc-evolution-chip__action--primary mdc-evolution-chip__action--presentational'])[1]"
                )
            )
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Next']"))
        ).click()
        time.sleep(2)
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Reschedule']")
            )
        ).click()
        time.sleep(3)

        # Step 1: Extract Booking ID
        booking_id_element = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='bookingIdFlex']/div"))
        )
        booking_id = booking_id_element[1].text.strip()
        print(f"Booking ID: {booking_id}")

        consumer_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        confirmation_button = WebDriverWait(consumer_login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Ok']"))
        )
        confirmation_button.click()

        # toast_message = WebDriverWait(consumer_login, 10).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        # )
        # message = toast_message.text
        # print("Toast Message:", message)

        time.sleep(3)

        bookings = WebDriverWait(consumer_login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'My Bookings')]"))
        )
        bookings.click()
        time.sleep(3)
       
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(), \"Today's Booking\")]")
            )
        ).click()

        time.sleep(2)

        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(), \"Upcoming Bookings\")])[1]")
            )
        ).click()

        time.sleep(5)


        try:
            show_more = WebDriverWait(consumer_login, 30).until(
                EC.presence_of_element_located((By.XPATH, "(//a[normalize-space(.)='Show more'])[1]"))
            )
            consumer_login.execute_script("arguments[0].scrollIntoView(true);", show_more)
            time.sleep(1)
            show_more.click()
            print("Clicked 'Show more'")
            time.sleep(3)  # Wait for new content to begin loading

            # Scroll to bottom to ensure all lazy-loaded cards are loaded
            last_height = consumer_login.execute_script("return document.body.scrollHeight")
            while True:
                consumer_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                new_height = consumer_login.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            print("Scrolled to bottom to load all cards.")
        except:
            print("No 'Show more' button found or it's already fully expanded.")

        # Step 2: Loop through all loaded cards to find the booking ID
        found = False
        cards = consumer_login.find_elements(By.XPATH, "//app-wl-card")
        print(f"Total cards found: {len(cards)}")

        for card in cards:
            try:
                # card_booking_id_elem = card.find_element(By.XPATH, ".//div[@class='cstmTxt field-head' and text()='Booking Id']/following-sibling::div")
                card_booking_id_elem = card.find_element(
                    By.XPATH,
                    ".//div[normalize-space(text())='Booking Id']/following-sibling::div"
                )     

                card_booking_id = card_booking_id_elem.text.strip()
                print(f"Found booking ID in card: '{card_booking_id}'")  # <--- Debug print

                if card_booking_id == booking_id:
                    consumer_login.execute_script("arguments[0].scrollIntoView(true);", card)
                    print(f"Found matching booking ID card: {card_booking_id}")
                    time.sleep(2)

                    # Click the 3-dot menu inside this card
                    three_dot = card.find_element(By.XPATH, ".//button[.//mat-icon[normalize-space(text())='more_horiz']]")
                    WebDriverWait(consumer_login, 5).until(EC.element_to_be_clickable(three_dot))
                    three_dot.click()
                    
                    print("Clicked 3-dot menu.")
                    found = True
                    break
            except Exception as e:
                print(f"Error processing a card: {e}")

        if not found:
            print("Booking card not found.")

        

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//span[normalize-space(.)='Cancel'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'Change of Plans')])[1]")
            )
        ).click() 

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='mdc-button__label'])[1]")
            )
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[@id='btnUser'])[1]"))
        ).click()

        print("Token Cancelled Successfully")

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'Dashboard')])[1]")
            )
        ).click()

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='fa fa-home'])[1]")
            )
        ).click()

        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='fa fa-commenting-o'])[1]")
            )
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//textarea[@id='message'])[1]")
            )
        ).send_keys("consumer send the enquriy to the provider")

        time.sleep(1)
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//i[@class='material-icons'])[1]"))
        ).click() 

        time.sleep(2)
        current_working_directory = os.getcwd()
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        time.sleep(3)
        pyautogui.press("enter")

        time.sleep(3)
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Send')])[1]"))
        ).click()

        toast_message = WebDriverWait(consumer_login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)


        time.sleep(5)



    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            consumer_login.get_screenshot_as_png(),  # param1
            # consumer_login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    



