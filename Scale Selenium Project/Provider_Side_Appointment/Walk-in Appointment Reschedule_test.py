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

test_mail = "test@jaldee.com"


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
    email = f"{phonenumber}.{first_name}.{test_mail}"
    print(email)
    return [first_name, last_name, cons_manual_id, phonenumber, email]


@pytest.fixture()
def login():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://scale.jaldee.com/business/")
    driver.maximize_window()

    driver.find_element(By.ID, "phone").send_keys("5555556030")
    driver.find_element(By.ID, "password").send_keys("Jaldee01")
    driver.find_element(By.XPATH, "//div[@class='mt-2']").click()
    # time.sleep(10)
    driver.implicitly_wait(5)
    yield driver
    # driver.close()
    # driver.quit()


def test_appt_reschedule(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]"))
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]"))
    )
    element.click()
    time.sleep(3)
    wait = WebDriverWait(login, 10)
    element_appoint = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[contains(text(),'Create New Patient')]")))
    element_appoint.click()
    login.implicitly_wait(3)
    first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
    login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
    login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
    login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
    login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
    login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
    login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
    login.implicitly_wait(3)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
    ).click()

    login.implicitly_wait(5)
    login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
    print("location : Chavakkad")
    login.implicitly_wait(5)

    login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
    login.implicitly_wait(5)
    login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
    print("Department : ENT")
    user_dropdown_xpath = ("(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
                           "ng-dirty'])[1]")
    WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))).click()
    user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
    WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_option_xpath))).click()
    print("Select user : Naveen")
    # time.sleep(3)
    service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
    # WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_dropdown_xpath))).click()
    element = login.find_element(By.XPATH, service_dropdown_xpath)
    login.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    service_option_xpath = ("(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
                            "Consultation'])[2]")
    WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
    print("Select Service : Naveen Consultation")
    time.sleep(3)
    Today_Date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                            "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
    Today_Date.click()
    print("Today Date:", Today_Date.text)
    wait = WebDriverWait(login, 10)
    time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
    time_slot.click()
    print("Time Slot:", time_slot.text)
    note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
    note_input.click()
    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Upload File']"))
    ).click()

    time.sleep(4)
    pyautogui.write(r"C:\Users\Archana\PycharmProjects\SeleniumPython\test.png")
    pyautogui.press('enter')

    time.sleep(4)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
    ).click()

    time.sleep(3)

    while True:
        try:
            print("before in loop")
            # Find the "Next" button
            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
            )
            # if next_button.is_enabled():
            #     print("in if")
            #     time.sleep(3)
            next_button.click()

            # else:

            # break
        except:
            print("EC caught:")
            break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    # accordion_tab.click()
    time.sleep(3)
    last_element_in_accordian.click()

    time.sleep(3)
    print("Before clicking View Details button")
    View_Detail_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'View Details')]"))
    )
    View_Detail_button.click()

    # login.execute_script("arguments[0].click();", View_Detail_button)
    print("After clicking View Details button")
    # time.sleep(3)
    # WebDriverWait(login, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#p-accordiontab-628-content > div > div:nth-child(2) > app-booking-actions > div > div > button:nth-child(5)"))).click()
    time.sleep(3)
    login.find_element(By.XPATH, "//button[contains(text(),'Reschedule')]").click()
    time.sleep(3)

    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//button[@class='p-element p-ripple p-datepicker-trigger p-button-icon-only ng-tns-c86-58 p-button p-component ng-star-inserted']"))
    #
    # ).click()

    calendar_icon_xpath = "//button[contains(@class,'p-element p-ripple p-datepicker-trigger p-button-icon-only ng-tns-c86')]"

    WebDriverWait(login, 20).until(EC.element_to_be_clickable((By.XPATH, calendar_icon_xpath)))

    calendar_icon = WebDriverWait(login, 20).until(EC.visibility_of_element_located((By.XPATH, calendar_icon_xpath)))

    login.execute_script("arguments[0].click();", calendar_icon)

    print("calendar popup successful")

    today_date = datetime.now()
    print(today_date.day)
    today_xpath_expression = "//span[@class='example-custom-date-class d-pad-15 ng-star-inserted'][normalize-space()='{}']".format(
        today_date.day)
    print(today_xpath_expression)
    tomorrow_date = today_date + timedelta(days=1)
    print(tomorrow_date.day)
    tomorrow_xpath_expression = "//span[@class='example-custom-date-class d-pad-15 ng-star-inserted'][normalize-space()='{}']".format(
        tomorrow_date.day)
    print(tomorrow_xpath_expression)

    Tomorrow_Date = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, tomorrow_xpath_expression))
    )
    Tomorrow_Date.click()
    print("Tomorrow Date:", Tomorrow_Date.text)

    wait = WebDriverWait(login, 10)
    time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected= 'false']")))
    time_slot.click()
    print("Time Slot:", time_slot.text)

    reschedule_button = WebDriverWait(login, 30).until(
        EC.visibility_of_element_located((By.XPATH,
                                          "//div[@class='col-12 col-sm-12 col-md-12 col-lg-12 mgn-up-20 mgn-bt-20 footerlinks no-padding reschedulebtn ng-star-inserted']//button[@class='btn btn-primary reschedule-btn']"))
    )
    reschedule_button.click()
    print("Reschedule Successfully")

