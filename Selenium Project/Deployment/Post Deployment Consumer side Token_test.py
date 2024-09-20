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
from selenium.webdriver.common.action_chains import ActionChains
import os


@pytest.fixture()
def login():
    driver = webdriver.Chrome(
        service=ChromeService(
            executable_path=r"Drivers\chromedriver-win64\chromedriver.exe"
        )
    )
    driver.get("https://www.jaldee.com/royalclinic/")
    driver.maximize_window()
    yield driver
    driver.quit


def scroll_until_visible(login, element):
    #####Scroll the page until the given element is visible.#####
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
    
    element = login.find_element(By.XPATH, "//span[normalize-space()='Book Now']")
    login.execute_script("arguments[0].scrollIntoView();", element)

    # Optionally move the mouse over the button to see if it helps
    ActionChains(login).move_to_element(element).perform()

    bookbutton = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Book Now']"))
    )
    bookbutton.click()
    time.sleep(2)
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    consultation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//app-checkin-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][normalize-space()='Consultation']",
            )
        )
    )
    login.execute_script("arguments[0].scrollIntoView(true);", consultation)
    consultation.click()
    time.sleep(2)
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    Today_Date = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-pressed='true']")
        )
    )
    Today_Date.click()
    print("Today Date:", Today_Date.text)
    wait = WebDriverWait(login, 10)
    queue = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//mat-chip[@aria-selected='true']"))
    )
    login.execute_script("arguments[0].scrollIntoView(true);", queue)
    time.sleep(2)
    queue.click()
    print("Queue:", queue.text)
    next_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Next']")
        )
    )
    login.execute_script("arguments[0].scrollIntoView(true);", next_button)
    time.sleep(3)
    next_button.click()
    time.sleep(3)  
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
    ).send_keys("5550033354")
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
    for i, otp_input in enumerate(otp_inputs):
        otp_input.send_keys(otp_digits[i])

    login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
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
    current_working_directory = os.getcwd()
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
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    button = login.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    print("Consumer create token successfully")
    time.sleep(3)
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
        # ######################### Sending Message from consumer side ################################
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Send Message']")
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
            (By.XPATH, "//button[i[contains(text(),'attach_file')] and contains(text(), 'Send Attachments')]")
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
            (By.XPATH, "//button[i[text()='attach_file'] and contains(text(), 'View Attachments')]")
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
    ################# Rescheduling the Token ##################
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Reschedule']")
        )
    ).click()
    time.sleep(2)
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    today_date = datetime.now()
    tomorrow_date = today_date + timedelta(days=1)
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
        EC.element_to_be_clickable((By.XPATH, tomorrow_xpath_expression))
    )
    Tomorrow_Date.click()
    print("Tomorrow Date:", Tomorrow_Date.text)
    queue = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//mat-chip[@role='option']")
        )
    )
    login.execute_script("arguments[0].scrollIntoView(true);", queue)
    time.sleep(2)
    queue.click()
    print("Queue:", queue.text)
    time.sleep(2)
    next_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Next']")
        )
    )
    login.execute_script("arguments[0].scrollIntoView(true);", next_button)
    time.sleep(3)
    next_button.click()
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Reschedule']")
        )
    ).click()
    time.sleep(5)
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    button = login.find_element(By.XPATH, "//button[normalize-space()='Ok']")
    button.click()
    print(" Token rescheduled successfully")
    time.sleep(3)
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
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted']"))
    ).click()
    print("Send enquiry successfully")
    ################# Cancel the Token from Upcoming bookings. #################
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
    while True:
        try:
            my_Bookings = WebDriverWait(login, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//mat-icon[@role='img']"))
            )
            if not my_Bookings:
                print("No bookings found.")
                break

            Checked_in_booking_found = False #Checked in booking is not processed 

            # Iterate from the last booking to the first
            for i in range(len(my_Bookings) - 1, -1, -1):
                last_booking = my_Bookings[i]
                scroll_until_visible(login, last_booking)

                # Construct XPath expressions for status and Checked in based on index
                status_xpath = f"(//div[@class='cstmTxt field-head'][normalize-space()='Status'])[position()={i+1}]"
                checked_in_xpath = f"(//span[@class='greenc ng-star-inserted'][normalize-space()='Checked in'])[position()={i+1}]"

                try:
                    status_element = login.find_element(By.XPATH, status_xpath)
                    checked_in_element = login.find_element(By.XPATH, checked_in_xpath)

                    # Check if the status is 'Checked-in'
                    if status_element.text.strip() == "Status" and checked_in_element.text.strip() == "Checked in":
                        WebDriverWait(login, 10).until(EC.element_to_be_clickable(last_booking)).click()
                        time.sleep(1)
                        WebDriverWait(login, 10).until(
                            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Cancel']"))
                        ).click()
                        time.sleep(2)

                        WebDriverWait(login, 10).until(
                            EC.presence_of_element_located((By.XPATH, "//mat-chip[normalize-space()='Change of Plans']"))
                        ).click()
                        time.sleep(2)

                        WebDriverWait(login, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Confirm']"))
                        ).click()

                        print("Token cancelled successfully")
                        Checked_in_booking_found = True #Checked in booking is  processed 
                        break  # Exit the for loop after successfully canceling
                except Exception as e:
                    print(f"Error processing booking {i}: {e}")

            if not Checked_in_booking_found:
                print("No need to processed further Checked in booking")
                break  ### While loop exit

        except Exception as e:
            print(f"Error in processing bookings: {e}")
            break
