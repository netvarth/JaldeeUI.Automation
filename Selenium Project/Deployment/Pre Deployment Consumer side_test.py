import time
from datetime import datetime, timedelta

import pyautogui
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import os


@pytest.fixture()
def login():

    driver = webdriver.Chrome(
        service=ChromeService(
            executable_path=r"Drivers\chromedriver-win64\chromedriver.exe"
        )
    )
    driver.get("https://scale.jaldee.com/visionhospital/")
    driver.maximize_window()
    yield driver
    driver.quit()  # Ensure the browser is closed properly


def scroll_until_visible(login, element):
    """Scroll the page until the given element is visible."""
    while True:
        try:
            login.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(1)  # Wait for scrolling to complete
            # Verify if element is visible
            if element.is_displayed():
                break
        except Exception as e:
            print(f"Exception during scrolling: {e}")
            break

def test_booking(login):
    time.sleep(5)
    # Scroll to the element
    book_now_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Book Now']")
        )
    )
    login.execute_script("arguments[0].scrollIntoView();", book_now_button)

    # Wait for the element to be clickable
    clickable_book_now_button = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Book Now']"))
    )

    # Attempt to click the element
    try:
        clickable_book_now_button.click()
    except:
        # If click is intercepted, click using JavaScript
        login.execute_script("arguments[0].click();", clickable_book_now_button)

    wait = WebDriverWait(login, 10)
    location_button = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@class='deptName ng-star-inserted'][contains(text(),'Chavakkad')]",
            )
        )
    )
    location_button.click()

    wait = WebDriverWait(login, 10)
    depart_button = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@class='deptName ng-star-inserted'][normalize-space()='ENT']",
            )
        )
    )
    depart_button.click()

    wait = WebDriverWait(login, 10)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Dr.Naveen KP')]")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//app-appointment-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][contains(text(),'service')]",
            )
        )
    ).click()
    time.sleep(3)
    # login.find_element(By.XPATH,
    #                    "//app-appointment-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][contains(text(),'service zero')]").click()
    # time.sleep(2)
    Today_Date = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-pressed='true'] [@aria-current='date']")
        )
    )
    Today_Date.click()
    time.sleep(2)
    print("Today Date:", Today_Date.text)
    wait = WebDriverWait(login, 10)
    time_slot = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//mat-chip[@aria-selected='true']"))
    )
    time_slot.click()
    print("Time Slot:", time_slot.text)
    login.execute_script("arguments[0].scrollIntoView();", time_slot)
    # login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Next']")
        )
    ).click()
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
    ).send_keys("5550002254")
    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located(
    #        (By.XPATH, "//a[normalize-space()='My Bookings']")
    #     )).click()
    # time.sleep(2)
    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
    # ).send_keys("5550002254")
    login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

    time.sleep(5)

    # otp_digits = "5555"
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

    login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

    time.sleep(3)

    time.sleep(3)
    consumer_notes = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//textarea[@placeholder='Add Notes you may have...']")
        )
    )
    consumer_notes.send_keys("Notes added from conumser side")
    time.sleep(3)
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='uploadFileTxt']"))
    ).click()
    time.sleep(2)
    # Get the current working directory
    current_working_directory = os.getcwd()

    # Construct the absolute path
    absolute_path = os.path.abspath(
        os.path.join(current_working_directory, r"Extras\test.png")
    )
    pyautogui.write(absolute_path)
    pyautogui.press("enter")
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    confirmbutton = WebDriverWait(login, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[normalize-space()='Confirm']")
        )
    )
    confirmbutton.click()
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
    ).click()

    print("Consumer create appointment successfully")

    time.sleep(3)

    # # Locate the element containing the booking ID
    # booking_id_element = login.find_element(
    #     By.XPATH, "//div[contains(@class, 'bookingIdFlex')]"
    # )

    # # Extract the text of the booking ID
    # booking_id = booking_id_element.text
    # print(f"Booking ID: {booking_id}")

    # # Split the text to get only the booking ID
    # # Assuming the booking ID is after a colon and space (': ')
    # if ":" in booking_id:
    #     booking_id = (
    #         booking_id.replace(" ", "")
    #         .replace("\n", " ")
    #         .replace("\r", "")
    #         .split(":")[1]
    #         .strip()
    #     )
    #     print("in IF", booking_id)
    # else:
    #     booking_id = booking_id.strip()  # fallback in case the format is different
    #     print("in else", booking_id)

    # print(f"Booking ID: {booking_id}")

    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
    # ).click()

    # snack_bar = WebDriverWait(login, 10).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    # )
    # message = snack_bar.text
    # print("Snack bar message:", message)

    # print("Consumer create appointment successfully")

    # time.sleep(3)

    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "//div[contains(text(),'My Bookings')]")
    #     )
    # ).click()

    # time.sleep(2)
    # WebDriverWait(login, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//a[@class='show_more']"))
    # ).click()

    # time.sleep(3)

    # appt_xpath = f"//div[contains(text(), '{booking_id}')]"
    # print(appt_xpath)

    # # Locate the booking with the same ID
    # booking_to_cancel = WebDriverWait(login, 20).until(
    #     EC.presence_of_element_located((By.XPATH, appt_xpath))
    # )
    # login.execute_script("arguments[0].scrollIntoView();", booking_to_cancel)
    # # booking_to_cancel.click()

    # time.sleep(2)
    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//mat-icon[@role='img'][last()]"))
    # ).click()
    bookings = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'My Bookings')]")
        )
    )
    bookings.click()
    time.sleep(3)
    while True:
        try:
            more_button = WebDriverWait(login, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Show more')]")))  # Update with the actual ID or selector
            # Scroll until the button is visible
            scroll_until_visible(login, more_button)
            WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Show more')]"))).click()
            time.sleep(3)
            login.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        except:
            break
    my_Bookings = WebDriverWait(login, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//mat-icon[@role='img']"))
    )
    if my_Bookings:
            last_booking = my_Bookings[-1]
            # Ensure the last booking is visible and clickable
            scroll_until_visible(login, last_booking)
            WebDriverWait(login, 10).until(EC.element_to_be_clickable(last_booking)).click()
    else:
        print("No bookings found. Waiting for new bookings to load...")
        time.sleep(3)
    ######################### Sending Message from consumer side ################################
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Send Message']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@id='message']"))
    ).send_keys(" Message to the provider ")

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//button[@type='button']//i[@class='material-icons'][normalize-space()='attach_file']",
            )
        )
    ).click()

    time.sleep(3)
    # Get the current working directory
    current_working_directory = os.getcwd()

    # Construct the absolute path
    absolute_path = os.path.abspath(
        os.path.join(current_working_directory, r"Extras\flower.jpg")
    )
    pyautogui.write(absolute_path)
    pyautogui.press("enter")

    print("Successfully upload the file")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Send']")
        )
    ).click()

    print("Send message successfully")

    ################## Sending attachment to provider #################
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Send Attachments']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Click here to select the files']")
        )
    ).click()

    time.sleep(3)
    # Get the current working directory
    current_working_directory = os.getcwd()

    # Construct the absolute path
    absolute_path = os.path.abspath(
        os.path.join(current_working_directory, r"Extras\prescription.pdf")
    )
    pyautogui.write(absolute_path)
    pyautogui.press("enter")
    print("Successfully upload the file")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='send']"))
    ).click()

    print("Send attachment successfully")
    time.sleep(3)
    ################## View Attachment to the Booking ##################
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='View Attachments']")
        )
    ).click()
    time.sleep(2)

    print("View attachment successfully")
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//i[@class='fa fa-window-close']")
        )
    ).click()
    time.sleep(3)
    ################## Rescheduling the Appointment ##################
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Reschedule']")
        )
    ).click()

    today_date = datetime.now()
    print(today_date.day)
    today_xpath_expression = "//div[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today'][normalize-space()='{}']".format(
        today_date.day
    )
    print(today_xpath_expression)
    tomorrow_date = today_date + timedelta(days=1)
    print(tomorrow_date.day)

    current_month_year = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//button[@aria-label='Choose month and year']//span[@class='mat-button-wrapper']",
            )
        )
    )
    if current_month_year.text.lower() != tomorrow_date.strftime("%b %Y").lower():
        login.find_element(By.XPATH, "//button[@aria-label='Next month']").click()
    time.sleep(3)
    tomorrow_xpath_expression = "//div[@class='mat-calendar-body-cell-content mat-focus-indicator'][normalize-space()='{}']".format(
        tomorrow_date.day
    )
    print(tomorrow_xpath_expression)

    Tomorrow_Date = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, tomorrow_xpath_expression))
    )
    Tomorrow_Date.click()

    print("Tomorrow Date:", Tomorrow_Date.text)

    wait = WebDriverWait(login, 10)
    time_slot = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//mat-chip[@class='mat-chip mat-focus-indicator text-center mat-primary mat-standard-chip mat-chip-selected ng-star-inserted']"
            )
        )
    )
    time_slot.click()
    print("Time Slot:", time_slot.text)
    login.execute_script("arguments[0].scrollIntoView();", time_slot)
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Next']"))
    ).click()

    time.sleep(2)
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Reschedule']")
        )
    ).click()
    time.sleep(3)
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    confirmation_button = WebDriverWait(login, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.confirmationBtn"))
    )
    confirmation_button.click()
    print("Appointment Rescheduled successfully")
    time.sleep(2)
    ################## Enquiry to the Provider ##################
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//mat-icon[normalize-space()='home']"))
    ).click()

    login.find_element(By.XPATH, "//i[@class='fa fa-commenting-o']").click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@id='message']"))
    ).send_keys("Message to Provider")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//i[@class='material-icons']"))
    ).click()

    time.sleep(3)
    # Get the current working directory
    current_working_directory = os.getcwd()

    # Construct the absolute path
    absolute_path = os.path.abspath(
        os.path.join(current_working_directory, r"Extras\sea.jpg")
    )
    pyautogui.write(absolute_path)
    pyautogui.press("enter")
    print("Successfully upload the file")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Send')]"))
    ).click()

    print("Send enquriy successfully")    
    ################## Cancel the appointment from Upcoming bookings. #################
    login.refresh()
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//i[@class='fa fa-user-circle-o']")
        )
    ).click()
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Dashboard')]")
        )
    ).click()
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[normalize-space()='My Bookings']")
        )
    ).click()
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//mat-select[@role='combobox']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Upcoming Bookings')]")
        )
    ).click()
    time.sleep(3)
    while True:
        try:
            more_button = WebDriverWait(login, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Show more')]")))  # Update with the actual ID or selector
            # Scroll until the button is visible
            scroll_until_visible(login, more_button)
            WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Show more')]"))).click()
            time.sleep(3)
            login.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        except:
            break
    my_Bookings = WebDriverWait(login, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//mat-icon[@role='img']"))
    )
    if my_Bookings:
            last_booking = my_Bookings[-1]
            # Ensure the last booking is visible and clickable
            scroll_until_visible(login, last_booking)
            WebDriverWait(login, 10).until(EC.element_to_be_clickable(last_booking)).click()
            WebDriverWait(login, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Cancel']"))
            ).click()
            time.sleep(2)
            WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//mat-chip[normalize-space()='Change of Plans']")
                )
            ).click()
            time.sleep(2)
            WebDriverWait(login, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Confirm']"))
            ).click()
            print("Appointment cancelled successfully")
            time.sleep(3)
    else:
        print("No bookings found. Waiting for new bookings to load...")
        time.sleep(3)
    
                
    # time.sleep(5)
    # WebDriverWait(login, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//a[@class='show_more']"))
    # ).click()

    # time.sleep(3)

    # Locate the booking with the same ID
    # booking_to_cancel = WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, f"//div[contains(text(), '{booking_id}')]")
    #     )
    # )
    # booking_to_cancel.click()

    # time.sleep(2)
    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//mat-icon[@role='img'][last()]"))
    # ).click()

    # time.sleep(2)
    
