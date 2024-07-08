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
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.jaldee.com/royalclinic/")
    driver.maximize_window()
    yield driver


def test_booking(login):
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Book Now']"))
    ).click()

    # wait = WebDriverWait(login, 10)
    # location_button = wait.until(EC.presence_of_element_located(
    #     (By.XPATH, "//div[@class='deptName ng-star-inserted'][contains(text(),'Chavakkad')]")))
    # location_button.click()

    # wait = WebDriverWait(login, 10)
    # depart_button = wait.until(EC.presence_of_element_located(
    #     (By.XPATH, "//div[@class='deptName ng-star-inserted'][normalize-space()='ENT']")))
    # depart_button.click()

    # wait = WebDriverWait(login, 10)
    # wait.until(EC.presence_of_element_located(
    #     (By.XPATH, "//div[contains(text(),'Dr.Naveen KP')]"))).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//app-appointment-card[@class='ng-star-inserted']//div//div[@class='serviceName ng-star-inserted'][normalize-space()='Consultation']"))
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

    # user_data = create_user_data()

    # login.find_element(By.XPATH, "//input[@id='phone']").send_keys(user_data[3])
    # login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='phone']"))

    ).send_keys("9207206005")

    login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()


    time.sleep(5)

    otp_digits = "5555"

    # Wait for the OTP input fields to be present
    otp_inputs = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//input[contains(@id, 'otp_')]")))

    # print("Number of OTP input fields:", len(otp_inputs))
    # print(otp_inputs)
  
    for i, otp_input in enumerate(otp_inputs):
    
        # print(i)
        # print(otp_input)
        otp_input.send_keys(otp_digits[i])

    login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

    time.sleep(3)


    # time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//textarea[@placeholder='Add Notes you may have...']"))
    ).send_keys("Notes added from conumser side")
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='uploadFileTxt']"))
    ).click()

    time.sleep(8)
    # Get the current working directory
    current_working_directory = os.getcwd()

    # Construct the absolute path
    absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))
    pyautogui.write(absolute_path)
    pyautogui.press('enter')

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm']"))
    ).click()

    time.sleep(5)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
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

    time.sleep(8)
    # Get the current working directory
    current_working_directory = os.getcwd()

    # Construct the absolute path
    absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))
    pyautogui.write(absolute_path)
    pyautogui.press('enter')
    print("Successfully upload the file")

    time.sleep(3)
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

    time.sleep(8)
    # Get the current working directory
    current_working_directory = os.getcwd()

    # Construct the absolute path
    absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))
    pyautogui.write(absolute_path)
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
    today_xpath_expression = "//div[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today'][normalize-space()='{}']".format(
        today_date.day)
    print(today_xpath_expression)
    tomorrow_date = today_date + timedelta(days=1)
    print(tomorrow_date.day)

    # current_month_year = WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "//button[@aria-label='Choose month and year']//span[@class='mat-button-wrapper']"))
    # )
    # print(current_month_year.text)
    # print(current_month_year.text.lower())
    # print(tomorrow_date.strftime("%b %Y").lower())
    # if current_month_year.text.lower() != tomorrow_date.strftime("%b %Y").lower():
    #     login.find_element(By.XPATH, "//button[@aria-label='Next month']").click()
    # time.sleep(3)
    tomorrow_xpath_expression = "//div[@class='mat-calendar-body-cell-content mat-focus-indicator'][normalize-space()='{}']".format(
        tomorrow_date.day)
    print(tomorrow_xpath_expression)

    Tomorrow_Date = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, tomorrow_xpath_expression))
    )
    time.sleep(2)
    Tomorrow_Date.click()

    print("Tomorrow Date:", Tomorrow_Date.text)

    wait = WebDriverWait(login, 10)
    time_slot = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                       "//mat-chip[@class='mat-chip mat-focus-indicator text-center mat-primary mat-standard-chip mat-chip-selected ng-star-inserted']")))
    time_slot.click()
    print("Time Slot:", time_slot.text)

    time.sleep(2)
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

    time.sleep(2)

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

    time.sleep(8)
    # Get the current working directory
    current_working_directory = os.getcwd()

    # Construct the absolute path
    absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))
    pyautogui.write(absolute_path)
    pyautogui.press('enter')
    print("Successfully upload the file")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Send')]"))
    ).click()

    print("Send enquriy successfully")

