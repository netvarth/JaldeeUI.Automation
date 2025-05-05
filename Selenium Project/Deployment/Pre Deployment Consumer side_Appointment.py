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
import allure
from allure_commons.types import AttachmentType

@pytest.fixture()
def login():

    driver = webdriver.Chrome(
        service=ChromeService(
            executable_path=r"Drivers\chromedriver-win64\chromedriver.exe"
        )   
    )
    # driver.get("https://scale.jaldee.com/visionhospital/")
    driver.get("https://scale.jaldee.com/visionhospital/")
    driver.maximize_window()
    yield driver
    driver.quit()  # Ensure the browser is closed properly
 

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

    current_date = datetime.now().strftime("%d-%m-%Y")
    print("Pre-Deployment Existing Consumer Appointment",current_date)   
    try:    
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
        Today_Date = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@aria-pressed='true'] [@aria-current='date']")
            )
        )
        login.execute_script("arguments[0].scrollIntoView(true);", Today_Date)
        time.sleep(3)
        Today_Date.click()
        time.sleep(3)  
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='mdc-evolution-chip__cell mdc-evolution-chip__cell--primary'])[1]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", time_slot)
        time.sleep(3)
        time_slot.click()
        
        print("Time Slot:", time_slot.text)
        
        login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Next']")
            )
        ).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='81234 56789'])[1]"))
        ).send_keys("9207206005")
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #        (By.XPATH, "//a[normalize-space()='My Bookings']")
        #     )).click()
        # time.sleep(2)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        # ).send_keys("5550004454")#22
        login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

        time.sleep(5)

        otp_digits = "5555"
        # otp_digits = "55555"
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

        # time.sleep(3)

        time.sleep(3)
        consumer_notes = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//textarea[@placeholder='Add Notes you may have...']")
        )
        )
        consumer_notes.send_keys("Notes added from conumser side")
        time.sleep(5)
        login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
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

    
   
    
    except Exception as e:
            allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
            )
            raise e
    
    