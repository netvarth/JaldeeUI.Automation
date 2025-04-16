import random
import string
import time
import os
import pyautogui
import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def create_user_data():
    fake = Faker()
    first_name = fake.first_name()
    print(first_name)
    last_name = fake.last_name()
    print(last_name)
    cons_manual_id = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
    print(cons_manual_id)
    random_digits = ''.join(random.choices(string.digits, k=7))
    phonenumber = f"{555}{random_digits}"
    print(phonenumber)
    return [first_name, last_name, cons_manual_id, phonenumber]


@pytest.fixture()
def login():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://scale.jaldee.com/visionhospital/")
    driver.maximize_window()
    yield driver


def test_booking(login):
    # login.find_element(By.XPATH, "//span[contains(text(),'Book Now')]").click()
    time.sleep(5)
    book_now_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//span[normalize-space(.)='Book Now'])[1]")))
    login.execute_script("arguments[0].click();", book_now_button)
    
    time.sleep(2)
    location_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='deptName ng-star-inserted'][contains(text(),'Chavakkad')]"))
    )
    location_button.click()

    time.sleep(2)
    depart_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='deptName ng-star-inserted'][normalize-space()='ENT']"))
    )
    depart_button.click()

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Dr.Naveen KP')]"))
    ).click()

    login.find_element(By.XPATH,
                       "//app-appointment-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][contains(text(),'service zero')]").click()

    Today_Date = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-pressed='true'] [@aria-current='date']"))
    )

    Today_Date.click()

    print("Today Date:", Today_Date.text)

    wait = WebDriverWait(login, 10)
    time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-chip[@aria-selected='true']")))
    time_slot.click()
    print("Time Slot:", time_slot.text)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Next')]"))
    ).click()

    user_data = create_user_data()

    login.find_element(By.XPATH, "//input[@id='phone']").send_keys(user_data[3])
    login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

    time.sleep(3)

    otp_digits = "55555"

    # Wait for the OTP input fields to be present
    otp_inputs = WebDriverWait(login, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//input[contains(@id, 'otp_')]"))
    )

    print("Number of OTP input fields:", len(otp_inputs))
    print(otp_inputs)
    # Wait for each OTP input field to be clickable and then fill the digit
    for i, otp_input in enumerate(otp_inputs):
        print(i)
        print(otp_input)
        otp_input.send_keys(otp_digits[i])

    login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

    time.sleep(3)

    first_name_field = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='first_name']"))
    )
    first_name_field.clear()  # Clear the field to ensure it's empty before sending keys
    print(user_data[0])
    first_name_field.send_keys(user_data[0])
    print(user_data[1])
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@id='first_name'])[2]"))
    ).send_keys(user_data[1])

    # Explicit wait for the "Next" button after entering the first and last names
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Next'][1]")))
    next_button.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Add Notes you may have...']"))
    ).send_keys("Note from the consumer side")

    time.sleep(3)
    print("before")
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
    ).click()
    print("After")

    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Ok')]"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'My Bookings')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='more_opt']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Send Message')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@id='message']"))
    ).send_keys("Send message from consumer side")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][contains(text(),'Send')]"))
    ).click()

    print("Successfully send the message")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Send Attachments')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Click here to select the files')]"))
    ).click()
    time.sleep(3)
    # Get the current working directory
    current_working_directory = os.getcwd()

    # Construct the absolute path
    absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))
    pyautogui.write(absolute_path)
    pyautogui.press('enter')

    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'send')]"))
    ).click()

    print("Successfully send Attachment")






