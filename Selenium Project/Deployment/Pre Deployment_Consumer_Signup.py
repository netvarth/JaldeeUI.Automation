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
    driver.get("https://scale.jaldee.com/visionhospital/")
    driver.maximize_window()
    yield driver
    driver.quit()  # Ensure the browser is closed properly

def create_consumer_data():
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    random_digits = fake.numerify(text="#######")
    phonenumber = f"555{random_digits}"
    test_mail = "@jaldee.com"  # Define a domain or use a placeholder
    email = f"{first_name}.{last_name}{test_mail}"
    
    return {
        "first_name": first_name,
        "last_name": last_name,
        "phonenumber": phonenumber,
        "email": email,
        "otp": "55555"  # Define or generate the OTP as needed
    }

def generate_random_salutation():
    salutations = ["Mr.", "Ms.", "Mrs.", "Master", "Miss", "B/o", "Dr.", "Adv.", "Fr."]
    return random.choice(salutations)


def test_signup_appointment_booking(login):
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
    Today_Date.click()
    time.sleep(2)
    print("Today Date:", Today_Date.text)
    wait = WebDriverWait(login, 10)
    time_slot = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//mat-chip[@aria-selected='true']"))
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
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
    ).click()
    print("New Consumer Appointment booking confirmed successfully")
    time.sleep(3)


def test_signup_token_booking(login):
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
                "//app-checkin-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][normalize-space()='service']",
            )
        )
    ).click()
    time.sleep(3)
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
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
    ).click()
    print("New Consumer token booking confirmed successfully")
    time.sleep(3)


def test_signup_familymember_appointment_booking(login):
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
    Today_Date.click()
    time.sleep(2)
    print("Today Date:", Today_Date.text)
    wait = WebDriverWait(login, 10)
    time_slot = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//mat-chip[@aria-selected='true']"))
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
    print("New Consumer Firstname:", consumer_data['first_name'])
    login.find_element(By.XPATH, "//input[@id='lastname']").send_keys(consumer_data['last_name'])
    print("New Consumer Lastname:", consumer_data['last_name'])
    login.find_element(By.XPATH, "//button[normalize-space()='Ok']").click()
    time.sleep(3)
    family_member_radio_button = WebDriverWait(login, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "(//span[@class='mat-radio-label-content'])[2]")
    )
    )
    family_member_radio_button.click()
    time.sleep(2)
    print("Selected Familymember:", family_member_radio_button.text)
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
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
    ).click()
    print("New Consumer Appointment booking confirmed successfully")
    time.sleep(3)



def test_signup_token_familymember_booking(login):
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
                "//app-checkin-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][normalize-space()='service']",
            )
        )
    ).click()
    time.sleep(3)
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
    print("New Consumer Firstname:", consumer_data['first_name'])
    login.find_element(By.XPATH, "//input[@id='lastname']").send_keys(consumer_data['last_name'])
    print("New Consumer Lastname:", consumer_data['last_name'])
    login.find_element(By.XPATH, "//button[normalize-space()='Ok']").click()
    time.sleep(3)
    family_member_radio_button = WebDriverWait(login, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "(//span[@class='mat-radio-label-content'])[2]")
    )
    )
    family_member_radio_button.click()
    time.sleep(2)
    print("Selected Familymember:", family_member_radio_button.text)
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
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
    ).click()
    print("New Consumer token booking confirmed successfully")
    time.sleep(3)


def test_prepayment_appointment_booking(login):
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
                "//div[@class='deptName ng-star-inserted'][normalize-space()='Global Service']",
            )
        )
    )
    depart_button.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//app-appointment-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][contains(text(),' Prepayment Consultation ')]",
            )
        )
    ).click()
    time.sleep(3)
    Today_Date = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-pressed='true']")
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
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='email_id']")
        )
    ).send_keys(consumer_data['email'])
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='mat-focus-indicator pass_butt mat-button mat-button-base']"))
    ).click()
    time.sleep(3)

    WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'NET BANKING')]")
            )
    ).click()

    time.sleep(3)
    makepayment = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                    "//div[@class='text-center mgn-up-10']//button[@type='button']",
            )
        )
    )
    login.execute_script("arguments[0].scrollIntoView(true);", makepayment)
    login.execute_script("arguments[0].click();", makepayment)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[contains(@class,'ptm-paymode-name ptm-lightbold')]")
        )
    ).click()

    time.sleep(1)

    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'SBI')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'ptm-emi-overlay')]//div[contains(@class,'')]//div[@id='checkout-button']//button[contains(@class,'ptm-nav-selectable')][contains(text(),'Pay ₹100')]",
            )
        )
    ).click()

        # Handle the popup window
        # Save the current window handle
    main_window_handle = login.current_window_handle

        # Wait until the new window is present
    WebDriverWait(login, 10).until(EC.new_window_is_opened)

        # Get all window handles
    all_window_handles = login.window_handles

        # Find the new window handle (the popup window)
    new_window_handle = None
    for handle in all_window_handles:
        if handle != main_window_handle:
            new_window_handle = handle
            break

        # Switch to the new window
    login.switch_to.window(new_window_handle)

        # Now interact with elements in the new window
        # For example, clicking the success button
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='btn btnd']"))
    ).click()

        # Optionally, switch back to the main window

    login.switch_to.window(main_window_handle)
        # time.sleep(15)

    try:
        snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

    except:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

    time.sleep(5)
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
    ).click()
    print("New Consumer Appointment booking confirmed successfully")
    time.sleep(3)



def test_prepayment_token_booking(login):
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
                "//div[@class='deptName ng-star-inserted'][normalize-space()='Global Service']",
            )
        )
    )
    depart_button.click()
    service_card = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@class='service-container']"
            )
        )
    )
    login.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", service_card)
    prepayment_checkin =WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//app-checkin-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][contains(text(),'Prepayment Consultation')]",
            )
        )
    )
    prepayment_checkin.click()
    time.sleep(3)
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    Today_Date = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-pressed='true']")
        )
    )
    login.execute_script("arguments[0].scrollIntoView();", Today_Date)
    Today_Date.click()
    print("Today Date:", Today_Date.text)
    wait = WebDriverWait(login, 10)
    queue = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//mat-chip[@aria-selected='true']"))
    )
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
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='email_id']")
        )
    ).send_keys(consumer_data['email'])
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='mat-checkbox-label']")
        )
    ).click()
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='mat-focus-indicator pass_butt mat-button mat-button-base']"))
    ).click()
    time.sleep(3)

    WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'NET BANKING')]")
            )
    ).click()

    time.sleep(3)
    makepayment = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                    "//div[@class='text-center mgn-up-10']//button[@type='button']",
            )
        )
    )
    login.execute_script("arguments[0].scrollIntoView(true);", makepayment)
    login.execute_script("arguments[0].click();", makepayment)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[contains(@class,'ptm-paymode-name ptm-lightbold')]")
        )
    ).click()

    time.sleep(1)

    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'SBI')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'ptm-emi-overlay')]//div[contains(@class,'')]//div[@id='checkout-button']//button[contains(@class,'ptm-nav-selectable')][contains(text(),'Pay ₹100')]",
            )
        )
    ).click()

        # Handle the popup window
        # Save the current window handle
    main_window_handle = login.current_window_handle

        # Wait until the new window is present
    WebDriverWait(login, 10).until(EC.new_window_is_opened)

        # Get all window handles
    all_window_handles = login.window_handles

        # Find the new window handle (the popup window)
    new_window_handle = None
    for handle in all_window_handles:
        if handle != main_window_handle:
            new_window_handle = handle
            break

        # Switch to the new window
    login.switch_to.window(new_window_handle)

        # Now interact with elements in the new window
        # For example, clicking the success button
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='btn btnd']"))
    ).click()

        # Optionally, switch back to the main window

    login.switch_to.window(main_window_handle)
        # time.sleep(15)

    try:
        snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

    except:

            snack_bar = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            message = snack_bar.text
            print("Snack bar message:", message)

    time.sleep(5)
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
    ).click()
    print("New Consumer token booking confirmed successfully")
    time.sleep(3)

