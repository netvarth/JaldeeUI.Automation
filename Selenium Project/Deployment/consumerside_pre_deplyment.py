from Framework.common_utils import *
from Framework.common_dates_utils import *



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Basic Member Ship flow")
@pytest.mark.parametrize("url", [consumer_url])

def test_consumer_booking(con_login):

    try:
        wait_and_locate_click(login, )
        wait = WebDriverWait(con_login, 20)
        time.sleep(2)
        booking_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//span[normalize-space()='Book Now'])[1]"))
        )
        con_login.execute_script("arguments[0].scrollIntoView();", booking_button)
        time.sleep(2)
        con_login.execute_script("arguments[0].click();", booking_button)

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='deptName ng-star-inserted'][contains(text(),'Chavakkad')]"))
        ).click()

        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='deptName ng-star-inserted'][normalize-space()='ENT']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Dr.Naveen KP')]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='serviceName ng-star-inserted'][normalize-space()='service'])[1]"))
        ).click()

        time.sleep(3)
        Today_Date = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@aria-pressed='true'] [@aria-current='date']")
            )
        )
        con_login.execute_script("arguments[0].scrollIntoView(true);", Today_Date)
        time.sleep(2)
        Today_Date.click()
        time.sleep(2)  
        print("Today Date:", Today_Date.text)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='mdc-evolution-chip__cell mdc-evolution-chip__cell--primary'])[1]"))
        )
        con_login.execute_script("arguments[0].scrollIntoView();", time_slot)
        time.sleep(2)
        time_slot.click()
        
        print("Time Slot:", time_slot.text)
        
        con_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Next']")
            )
        ).click()
        time.sleep(3)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='81234 56789'])[1]"))
        ).send_keys("9207206005")

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='continue ng-star-inserted']"))
        ).click()

        time.sleep(5)
        otp_digits = "5555"
        otp_inputs = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )

        for i, otp_input in enumerate(otp_inputs):

            otp_input.send_keys(otp_digits[i])

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='continue ng-star-inserted']"))
        ).click()

        time.sleep(3)
        consumer_notes = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//textarea[@placeholder='Add Notes you may have...']")
        )
        )
        consumer_notes.send_keys("Notes added from consumer side")
        time.sleep(3)
        con_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='uploadFileTxt']"))
        ).click()

        time.sleep(4)
        image_path = os.path.join(os.path.dirname(__file__), 'Extras', 'test.png')
        pyautogui.write(image_path)
        time.sleep(2)
        pyautogui.press("enter")
        print("Successfully uploaded the file")
        
    
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm']"))
        ).click()
        time.sleep(3)
        booking_id_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='bookingIdFlex ng-star-inserted']/div[last()]"))
        )
        booking_id = booking_id_element.text.strip()
        print(f"Captured Booking Id: {booking_id}")
        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Ok']"))
        ).click()

        print("Consumer create appointment successfully")

        time.sleep(3)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'My Bookings')]"))
        ).click()
        time.sleep(3)
       # Click on Show More until all cards are loaded
        while True:
            show_more_buttons = con_login.find_elements(By.XPATH, "(//a[normalize-space()='Show more'])[1]")
            if not show_more_buttons:
                print("No more 'Show More' buttons available.")
                break

            con_login.execute_script("arguments[0].scrollIntoView(true);", show_more_buttons[0])
            time.sleep(1)
            show_more_buttons[0].click()
            print("Clicked on 'Show More' button.")
            time.sleep(3)

        # Find all booking cards
        booking_cards = con_login.find_elements(By.XPATH, "//app-appt-card")

        # Loop through the booking cards to find the matching Booking ID
        for card in booking_cards:
            try:
                # Locate and extract the Booking ID text
                booking_text_element = card.find_element(By.XPATH, ".//div[contains(@class,'cstmTxtInfo')]")
                if booking_text_element.text.strip() == booking_id:
                    print(f"Matching Booking ID found: {booking_id}")
                    
                    # Locate and click the more_horiz button
                    more_horiz_button = card.find_element(By.XPATH, ".//button[.//mat-icon[text()='more_horiz']]")
                    con_login.execute_script("arguments[0].scrollIntoView(true);", more_horiz_button)
                    wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[.//mat-icon[text()='more_horiz']]"))).click()
                    
                    print("More options button clicked successfully.")
                    break
            except Exception as e:
                print(f"Error while verifying booking card or clicking more_horiz: {e}")

        time.sleep(5)

    except Exception as e:
        allure.attach(
            con_login.get_screenshot_as_png(),
            name="error_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        print(f"Test Failed: {e}")  # Ensure failure reason is visible in logs
        raise e

    