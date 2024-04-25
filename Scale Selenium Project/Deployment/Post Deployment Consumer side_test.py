import random
import string
import time
from datetime import datetime, timedelta

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
    driver.get("https://jaldee.com/royalclinic/")
    driver.maximize_window()
    yield driver


def test_booking(login):
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Book Now']"))
    ).click()

    wait = WebDriverWait(login, 10)
    location_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@class='deptName ng-star-inserted'][contains(text(),'Chavakkad')]")))
    location_button.click()

    wait = WebDriverWait(login, 10)
    depart_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@class='deptName ng-star-inserted'][normalize-space()='ENT']")))
    depart_button.click()

    wait = WebDriverWait(login, 10)
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[contains(text(),'Dr.Naveen KP')]"))).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//app-appointment-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][contains(text(),'service')]"))
    ).click()
    # login.find_element(By.XPATH,
    #                    "//app-appointment-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][contains(text(),'service zero')]").click()

    Today_Date = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-pressed='true'] [@aria-current='date']"))
    )

    Today_Date.click()

    print("Today Date:", Today_Date.text)

    wait = WebDriverWait(login, 10)
    time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-chip[@aria-selected='true']")))
    time_slot.click()
    print("Time Slot:", time_slot.text)

    login.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()

    user_data = create_user_data()

    login.find_element(By.XPATH, "//input[@id='phone']").send_keys(user_data[3])
    login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

    time.sleep(3)

    otp_digits = "55555"

    # Wait for the OTP input fields to be present
    otp_inputs = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//input[contains(@id, 'otp_')]")))

    print("Number of OTP input fields:", len(otp_inputs))
    print(otp_inputs)
    # Wait for each OTP input field to be clickable and then fill the digit
    for i, otp_input in enumerate(otp_inputs):
        # wait.until(EC.element_to_be_clickable((By.XPATH, otp_input))).send_keys(
        #     otp_digits[i])
        print(i)
        print(otp_input)
        otp_input.send_keys(otp_digits[i])

    login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

    time.sleep(3)

    first_name_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='first_name']")))
    first_name_field.clear()  # Clear the field to ensure it's empty before sending keys
    print(user_data[0])
    first_name_field.send_keys(user_data[0])
    print(user_data[1])
    wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='first_name'])[2]"))).send_keys(user_data[1])

    # Explicit wait for the "Next" button after entering the first and last names
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Next'][1]")))
    next_button.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Add Notes you may have...']"))
    ).send_keys("Note from the consumer side")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='uploadFileTxt']"))
    ).click()
    time.sleep(3)
    pyautogui.write(r"C:\Users\Archana\PycharmProjects\SeleniumPython\test.png")
    pyautogui.press('enter')

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
    ).click()

    time.sleep(5)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Ok')]"))
    ).click()

    print("Consumer create appointment successfully")

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'My Bookings')]"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//mat-icon[@role='img'][last()]"))
    ).click()

    ######################### Sending Message from consumer side ################################

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send Message']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@id='message']"))
    ).send_keys(" Message to the provider ")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@type='button']//i[@class='material-icons'][normalize-space()='attach_file']"))
    ).click()

    time.sleep(3)
    pyautogui.write(r"C:\Users\Archana\PycharmProjects\SeleniumPython\test.png")
    pyautogui.press('enter')
    print("Successfully upload the file")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Send']"))
    ).click()

    # snack_bar = WebDriverWait(login, 10).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    # )
    # message = snack_bar.text
    # print("Snack bar message:", message)

    ################## Sending attachment to provider #################
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send Attachments']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Click here to select the files']"))
    ).click()

    time.sleep(3)
    pyautogui.write(r"C:\Users\Archana\PycharmProjects\SeleniumPython\test.png")
    pyautogui.press('enter')
    print("Successfully upload the file")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='send']"))
    ).click()
    #
    # snack_bar = WebDriverWait(login, 10).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    # )
    # message = snack_bar.text
    # print("Snack bar message:", message)

    ################## Rescheduling the Appointment ##################
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Reschedule']"))
    ).click()

    today_date = datetime.now()
    print(today_date.day)
    today_xpath_expression = "//table[@class='mat-calendar-table']//button[contains(@class, 'mat-calendar-body-cell')][normalize-space()='{}']".format(
        today_date.day)
    print(today_xpath_expression)
    tomorrow_date = today_date + timedelta(days=1)
    print(tomorrow_date.day)
    tomorrow_xpath_expression = "//table[@class='mat-calendar-table']//button[contains(@class, 'mat-calendar-body-cell')][normalize-space()='{}']".format(
        tomorrow_date.day)
    print(tomorrow_xpath_expression)

    time.sleep(2)
    Tomorrow_Date = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, tomorrow_xpath_expression))
    )
    Tomorrow_Date.click()

    print("Tomorrow Date:", Tomorrow_Date.text)

    wait = WebDriverWait(login, 10)
    time_slot = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                       "//mat-chip[@class='mat-chip mat-focus-indicator text-center mat-primary mat-standard-chip mat-chip-selected ng-star-inserted']")))
    time_slot.click()
    print("Time Slot:", time_slot.text)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Next']"))
    ).click()

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Reschedule']"))
    ).click()

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
    ).click()

    login.implicitly_wait(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='My Bookings']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//mat-select[@role='combobox']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Upcoming Bookings')]"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//mat-icon[@role='img'][last()]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Cancel']"))
    ).click()
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//mat-chip[normalize-space()='Change of Plans']"))
    ).click()
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Confirm']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[@alt='Home']"))
    ).click()

    login.find_element(By.XPATH, "//i[@class='fa fa-commenting-o']").click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@id='message']"))
    ).send_keys("Message to Provider")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//i[@class='material-icons']"))
    ).click()

    time.sleep(3)
    pyautogui.write(r"C:\Users\Archana\PycharmProjects\SeleniumPython\test.png")
    pyautogui.press('enter')
    print("Successfully upload the file")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Send')]"))
    ).click()