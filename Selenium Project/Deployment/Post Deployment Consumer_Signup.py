import email
import time
from datetime import datetime, timedelta

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
from faker import Faker
import random
import string
from selenium.common import TimeoutException

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
    driver.quit() 

def generate_random_salutation():
    salutations = ["Mr.", "Ms.", "Mrs.", "Master", "Miss", "B/o", "Dr.", "Adv.", "Fr."]
    return random.choice(salutations)

def create_consumer_data():
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    random_digits = fake.numerify(text="#######")
    phonenumber = f"555{random_digits}"
    test_email = "@jaldee.com"
    email = f"{first_name}.{last_name}.{test_email}"

    return {
        "first_name": first_name,
        "last_name": last_name,
        "phonenumber": phonenumber,
        "email": email,
        "otp": "55555"  
    }

def test_signup_appointment_booking(login):

    current_date = datetime.now().strftime("%d-%m-%Y")
    print("Post-Deployment signup and Appointment booking",current_date)
    try:
        consumer_data = create_consumer_data()
        time.sleep(5)
        book_now_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Book Now']")
            )
        )
        login.execute_script("arguments[0].scrollIntoView();", book_now_button)
        clickable_book_now_button = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Book Now']"))
        )
        try:
            clickable_book_now_button.click()
        except:
            login.execute_script("arguments[0].click();", clickable_book_now_button)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//app-appointment-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][normalize-space()='Consultation']",
                )
            )
        ).click()
        time.sleep(2)
        login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
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
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='mdc-evolution-chip__cell mdc-evolution-chip__cell--primary'])[1]"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)
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
        ).send_keys(consumer_data['phonenumber'])
        print("New Consumer Phone Number:", consumer_data['phonenumber'])
        login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        time.sleep(5)
        otp_inputs = WebDriverWait(login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )
        for i, otp_input in enumerate(otp_inputs):
            otp_input.send_keys(consumer_data['otp'][i])
        login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='first_name'])[1]"))
        ).send_keys(consumer_data['first_name'])
        print("New Consumer Firstname:", consumer_data['first_name'])
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='first_name'])[2]"))
        ).send_keys(consumer_data['last_name'])
        print("New Consumer Lastname:", consumer_data['last_name'])
        login.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        time.sleep(5)
        consumer_notes = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Add Notes you may have...']")
            )
        )
        consumer_notes.send_keys("Notes added from conumser side")
        time.sleep(3)
        uploadfile = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='uploadFileTxt']"))
        )
        login.execute_script("arguments[0].scrollIntoView(true);", uploadfile)
        time.sleep(2)
        uploadfile.click()
        time.sleep(2)
        current_working_directory = os.getcwd()
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        time.sleep(3)
        confirmbutton = WebDriverWait(login, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm']")
            )
        )
        login.execute_script("arguments[0].scrollIntoView(true);", confirmbutton)
        time.sleep(2)
        confirmbutton.click()
        time.sleep(5)
        Ok_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
        )
        login.execute_script("arguments[0].scrollIntoView(true);", Ok_button)
        time.sleep(2)
        Ok_button.click()
        time.sleep(2)
        print("New Consumer Appointment booking confirmed successfully")
        time.sleep(3)

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(), 
            name="full_page", 
            attachment_type=AttachmentType.PNG,
        )
        raise e

def test_signup_token_booking(login):
    
    current_date = datetime.now().strftime("%d-%m-%Y")
    print("Post-Deployment signup and Token booking",current_date)
    try:
        consumer_data = create_consumer_data()
        time.sleep(5)
        book_now_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Book Now']")
            )
        )
        login.execute_script("arguments[0].scrollIntoView();", book_now_button)

        clickable_book_now_button = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Book Now']"))
        )
        try:
            clickable_book_now_button.click()
        except:
            login.execute_script("arguments[0].click();", clickable_book_now_button)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//app-checkin-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][normalize-space()='Consultation']",
                )
            )
        ).click()
        time.sleep(2)
        login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        Today_Date = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@aria-pressed='true']")
            )
        )
        Today_Date.click()
        time.sleep(2)
        print("Today Date:", Today_Date.text)
        queue = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[@class='mdc-evolution-chip__cell mdc-evolution-chip__cell--primary']")
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
            EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        ).send_keys(consumer_data['phonenumber'])
        print("New Consumer Phone Number:", consumer_data['phonenumber'])
        login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        time.sleep(5)
        otp_inputs = WebDriverWait(login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )
        for i, otp_input in enumerate(otp_inputs):
            otp_input.send_keys(consumer_data['otp'][i])
        login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='first_name'])[1]"))
        ).send_keys(consumer_data['first_name'])
        print("New Consumer Firstname:", consumer_data['first_name'])
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='first_name'])[2]"))
        ).send_keys(consumer_data['last_name'])
        print("New Consumer Lastname:", consumer_data['last_name'])
        login.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        time.sleep(5)
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
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
        ).click()
        print("New Consumer Token booking confirmed successfully")
        time.sleep(3)
    
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(), 
            name="full_page", 
            attachment_type=AttachmentType.PNG,
        )
        raise e


def test_signup_familymember_appointment_booking(login):

    current_date = datetime.now().strftime("%d-%m-%Y")
    print("Post-Deployment add familymember Appointment booking",current_date)
    try:
        consumer_data = create_consumer_data()
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

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//app-appointment-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][normalize-space()='Consultation']",
                )
            )
        ).click()
        time.sleep(2)
        login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
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
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='mdc-evolution-chip__cell mdc-evolution-chip__cell--primary'])[1]"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)
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
        ).send_keys(consumer_data['phonenumber'])
        print("New Consumer Phone Number:", consumer_data['phonenumber'])
        login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        time.sleep(5)
        otp_inputs = WebDriverWait(login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )
        for i, otp_input in enumerate(otp_inputs):
            otp_input.send_keys(consumer_data['otp'][i])
        login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='first_name'])[1]"))
        ).send_keys(consumer_data['first_name'])
        print("New Consumer Firstname:", consumer_data['first_name'])
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='first_name'])[2]"))
        ).send_keys(consumer_data['last_name'])
        print("New Consumer Lastname:", consumer_data['last_name'])
        login.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        time.sleep(5)
        add_family_icon = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//i[@class='fa fa-pencil-square-o member']")
            )
        )
        add_family_icon.click()
        time.sleep(2)
        add_member = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[normalize-space()='Add Member']")
            )
        )
        add_member.click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@placeholder='Select']")
            )
        ).click()
        time.sleep(3)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//li[@aria-label='{salutation}']"
        salutation_option_element = WebDriverWait(login, 15).until(
            EC.element_to_be_clickable((By.XPATH, salutation_option_xpath))
        )
        salutation_option_element.click()
        time.sleep(3)
        consumer_data = create_consumer_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(consumer_data['first_name'])
        print("Add Familymember Firstname:", consumer_data['first_name'])
        login.find_element(By.XPATH, "//input[@id='lastname']").send_keys(consumer_data['last_name'])
        print("Add Familymember Lastname:", consumer_data['last_name'])
        login.find_element(By.XPATH, "//button[normalize-space()='Ok']").click()
        time.sleep(3)
        family_member_radio_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@class='mdc-radio'])[2]")
        )
        )
        family_member_radio_button.click()
        time.sleep(2)
        radio_button_label = family_member_radio_button.find_element(By.XPATH, ".//following-sibling::label")
        print("Selected Familymember:", radio_button_label.text)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Ok']")
            )
        ).click()
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
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
        ).click()
        print("Add Familymember Appointment booking confirmed successfully")
        time.sleep(3)

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(), 
            name="full_page", 
            attachment_type=AttachmentType.PNG,
        )
        raise e
    


def test_signup_token_familymember_booking(login):

    current_date = datetime.now().strftime("%d-%m-%Y")
    print("Post-Deployment add familymember Token booking",current_date)
    try:
        consumer_data = create_consumer_data()
        time.sleep(5)
        book_now_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Book Now']")
            )
        )
        login.execute_script("arguments[0].scrollIntoView();", book_now_button)

        clickable_book_now_button = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Book Now']"))
        )
        try:
            clickable_book_now_button.click()
        except:
            login.execute_script("arguments[0].click();", clickable_book_now_button)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//app-checkin-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][normalize-space()='Consultation']",
                )
            )
        ).click()
        time.sleep(2)
        login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        Today_Date = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@aria-pressed='true']")
            )
        )
        Today_Date.click()
        time.sleep(2)
        print("Today Date:", Today_Date.text)
        queue = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[@class='mdc-evolution-chip__cell mdc-evolution-chip__cell--primary']")
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
            EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        ).send_keys(consumer_data['phonenumber'])
        print("New Consumer Phone Number:", consumer_data['phonenumber'])
        login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        time.sleep(5)
        otp_inputs = WebDriverWait(login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )
        for i, otp_input in enumerate(otp_inputs):
            otp_input.send_keys(consumer_data['otp'][i])
        login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='first_name'])[1]"))
        ).send_keys(consumer_data['first_name'])
        print("New Consumer Firstname:", consumer_data['first_name'])
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='first_name'])[2]"))
        ).send_keys(consumer_data['last_name'])
        print("New Consumer Lastname:", consumer_data['last_name'])
        login.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        time.sleep(5)
        add_family_icon = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//i[@class='fa fa-pencil-square-o member']")
            )
        )
        add_family_icon.click()
        time.sleep(2)
        add_member = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[normalize-space()='Add Member']")
            )
        )
        add_member.click()
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p-dropdown[@placeholder='Select']")
            )
        ).click()
        time.sleep(3)
        salutation = generate_random_salutation()
        salutation_option_xpath = f"//li[@aria-label='{salutation}']"
        salutation_option_element = WebDriverWait(login, 15).until(
            EC.element_to_be_clickable((By.XPATH, salutation_option_xpath))
        )
        salutation_option_element.click()
        time.sleep(3)
        consumer_data = create_consumer_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(consumer_data['first_name'])
        print("Add Familymember Firstname:", consumer_data['first_name'])
        login.find_element(By.XPATH, "//input[@id='lastname']").send_keys(consumer_data['last_name'])
        print("Add Familymember Lastname:", consumer_data['last_name'])
        login.find_element(By.XPATH, "//button[normalize-space()='Ok']").click()
        time.sleep(3)
        family_member_radio_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@class='mdc-radio'])[2]")
        )
        )
        family_member_radio_button.click()
        time.sleep(2)
        radio_button_label = family_member_radio_button.find_element(By.XPATH, ".//following-sibling::label")
        print("Selected Familymember:", radio_button_label.text)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Ok']")
            )
        ).click()
        time.sleep(3)
        consumer_notes = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Add Notes you may have...']")
            )
        )
        consumer_notes.send_keys("Notes added from conumser side")
        time.sleep(3)
        uploadfile = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='uploadFileTxt']"))
        )
        login.execute_script("arguments[0].scrollIntoView(true);", uploadfile)
        time.sleep(2)
        uploadfile.click()
        time.sleep(2)
        current_working_directory = os.getcwd()
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        time.sleep(3)
        confirmbutton = WebDriverWait(login, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm']")
            )
        )
        login.execute_script("arguments[0].scrollIntoView(true);", confirmbutton)
        time.sleep(2)
        confirmbutton.click()
        time.sleep(5)
        Ok_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
        )
        login.execute_script("arguments[0].scrollIntoView(true);", Ok_button)
        time.sleep(2)
        Ok_button.click()
        time.sleep(2)
        print("Add Familymember token booking confirmed successfully")
        time.sleep(3)
    except Exception as e:
        allure.attach( 
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        )
        raise e


