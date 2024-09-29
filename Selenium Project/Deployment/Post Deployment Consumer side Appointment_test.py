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

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//app-appointment-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][normalize-space()='Consultation']",
            )
        )
    ).click()
    time.sleep(3)
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    Today_Date = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//button[@aria-pressed='true'] [@aria-current='date']",
            )
        )
    )

    Today_Date.click()

    print("Today Date:", Today_Date.text)

    wait = WebDriverWait(login, 10)
    time_slot = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='mdc-evolution-chip__cell mdc-evolution-chip__cell--primary'])[1]"))
    )
    login.execute_script("arguments[0].scrollIntoView();", time_slot)
    time.sleep(3)
    time_slot.click()
    print("Time Slot:", time_slot.text)
    time.sleep(1)
    next_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Next']")
        )
    )
    login.execute_script("arguments[0].scrollIntoView(true);", next_button)
    time.sleep(3)
    next_button.click()
    time.sleep(3)
    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located(
    #        (By.XPATH, "//a[normalize-space()='My Bookings']")
    #     )).click()
    # time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
    ).send_keys("5550004454")

    login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

    time.sleep(5)

    otp_digits = "55555"
    wait = WebDriverWait(login, 10)
    # Wait for the OTP input fields to be present
    otp_inputs = wait.until(
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
    login.execute_script("arguments[0].scrollIntoView(true);", consumer_notes)
    consumer_notes.send_keys("Notes added from conumser side")
    time.sleep(3)
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='uploadFileTxt']"))
    ).click()

    time.sleep(5)
    current_working_directory = os.getcwd()
    absolute_path = os.path.abspath(
        os.path.join(current_working_directory, r"Extras\test.png")
    )
    pyautogui.write(absolute_path)
    pyautogui.press("enter")

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Confirm']")
        )
    ).click()

    time.sleep(3)
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
    ).click()

    print("Consumer create appointment successfully")

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

    ######################## Sending Message from consumer side ################################

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Send Message']")
        )
    ).click()
    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@id='message']"))
    ).send_keys(" Message to the provider ")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//button[@type='button']//i[@class='material-icons'][normalize-space()='attach_file']",
            )
        )
    ).click()

    time.sleep(8)

    current_working_directory = os.getcwd()
    absolute_path = os.path.abspath(
        os.path.join(current_working_directory, r"Extras\test.png")
    )
    pyautogui.write(absolute_path)
    pyautogui.press("enter")
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Send']")
        )
    ).click()

    snack_bar = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    )
    message = snack_bar.text
    print("Snack bar message:", message)

    ################## Sending attachment to provider #################
    time.sleep(2)
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

    time.sleep(8)
 
    current_working_directory = os.getcwd()
    absolute_path = os.path.abspath(
        os.path.join(current_working_directory, r"Extras\test.png")
    )
    pyautogui.write(absolute_path)
    pyautogui.press("enter")
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='send']"))
    ).click()
    
    snack_bar = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    )
    message = snack_bar.text
    print("Snack bar message:", message)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mat-mdc-menu-item-text'])[5]")
        )
    ).click()
    time.sleep(2)
    ################## View Attachment to the Booking ##################
    print("View attachment successfully")
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//i[@class='fa fa-window-close']")
        )
    ).click()
    time.sleep(3)
    
    ################# Rescheduling the Appointment ##################
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Reschedule']")
        )
    ).click()
    time.sleep(3)
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    today_date = datetime.now()
    print(today_date.day)
    today_xpath_expression = "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today'][normalize-space()='{}']".format(
        today_date.day
    )
    print(today_xpath_expression)
    tomorrow_date = today_date + timedelta(days=1)
    print(tomorrow_date.day)
    # Get tomorrow's date
    tomorrow = (datetime.now() + timedelta(days=1)).strftime('%B %d, %Y')  # Format: "September 27, 2024"
    print("Tomorrow's Date:", tomorrow)

    # Create the XPath for tomorrow's date
    tomorrow_xpath_expression = "//button[contains(@class, 'mat-calendar-body-cell') and @aria-label='{}']".format(tomorrow)
    print("Tomorrow's XPath Expression:", tomorrow_xpath_expression)

    # current_month_year = WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "//button[@aria-label='Choose month and year']//span[@class='mat-button-wrapper']",
    #         )
    #     )
    # )
    # if current_month_year.text.lower() != tomorrow_date.strftime("%b %Y").lower():
    #     login.find_element(By.XPATH, "//button[@aria-label='Next month']").click()
    # time.sleep(5)
    # tomorrow_xpath_expression = "//span[normalize-space()='{}']".format(
    #     tomorrow_date.day
    # )
    # print(tomorrow_xpath_expression)

    Tomorrow_Date = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, tomorrow_xpath_expression))
    )
    # # Attempt to click the element
    try:
        Tomorrow_Date.click()
    except:
    #If click is intercepted, click using JavaScript
        login.execute_script("arguments[0].scrollIntoView();", Tomorrow_Date)
        login.execute_script("arguments[0].click();", Tomorrow_Date)
        Tomorrow_Date.click()
    
    print("Tomorrow Date:", Tomorrow_Date.text)
    time.sleep(3)
    wait = WebDriverWait(login, 20)
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
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Ok']"))
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
   
    current_working_directory = os.getcwd()
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
    print("Send enquriy successfully")    
    time.sleep(5)
    ################# Cancel the appointment from Upcoming bookings. #################
    login.refresh()
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='mat-mdc-menu-trigger mdc-icon-button mat-mdc-icon-button mat-unthemed mat-mdc-button-base']")
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

            Confirmed_booking_found = False # Confirmed_booking  is not processed

            # Iterate from the last booking to the first
            for i in range(len(my_Bookings) - 1, -1, -1):
                last_booking = my_Bookings[i]
                scroll_until_visible(login, last_booking)

                # Construct XPath expressions for status and confirmed based on index
                status_xpath = f"(//div[@class='cstmTxt field-head'][normalize-space()='Status'])[position()={i+1}]"
                confirmed_xpath = f"(//span[@class='greenc ng-star-inserted'][normalize-space()='Confirmed'])[position()={i+1}]"

                try:
                    status_element = login.find_element(By.XPATH, status_xpath)
                    confirmed_element = login.find_element(By.XPATH, confirmed_xpath)

                    # Check if the status is 'Confirmed'
                    if status_element.text.strip() == "Status" and confirmed_element.text.strip() == "Confirmed":
                        WebDriverWait(login, 10).until(EC.element_to_be_clickable(last_booking)).click()

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

                        print("Appointment cancelled successfully")
                        Confirmed_booking_found = True # Confirmed_booking_found booking is  processed 
                        break  # Exit the loop after successfully canceling
                except Exception as e:
                    print(f"Error processing booking {i}: {e}")

            if not Confirmed_booking_found:
                print("No need to processed further Confirmed booking")
                break  # While loop exit

        except Exception as e:
            # print(f"Error in processing bookings: {e}")
            break
    
