import time
import pytest
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_framework.utils import *

# Helper functions
def create_user_data():
    first_name = "TestFirstName"
    last_name = "TestLastName"
    cons_manual_id = "12345"
    phonenumber = "5551234567"
    email = "testuser@example.com"
    return first_name, last_name, cons_manual_id, phonenumber, email

def fill_prescription_details(login, row, dose, frequency, duration, notes):
    base_xpath = f"//*[contains(@id, 'pr_id')]/tbody/tr[{row}]"
    dose_xpath = f"{base_xpath}/td[2]/p-celleditor/textarea"
    frequency_xpath = f"{base_xpath}/td[3]/p-celleditor/textarea"
    duration_xpath = f"{base_xpath}/td[4]/p-celleditor/textarea"
    notes_xpath = f"{base_xpath}/td[5]/p-celleditor/textarea"

    fill_cell(login, dose_xpath, dose)
    fill_cell(login, frequency_xpath, frequency)
    fill_cell(login, duration_xpath, duration)
    fill_cell(login, notes_xpath, notes)

def fill_cell(login, cell_xpath, value):
    cell = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, cell_xpath)))
    cell.click()
    textarea = WebDriverWait(login, 10).until(EC.visibility_of_element_located((By.XPATH, cell_xpath)))
    textarea.clear()
    textarea.send_keys(value)

# Test function
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_Prescription(login):
    try:
        login.get("https://scale.jaldee.com/business/")
        time.sleep(5)

        WebDriverWait(login, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Appointments ')]"))).click()
        time.sleep(3)
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Appointment']"))).click()
        time.sleep(3)

        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, "//b[contains(text(),'Create New Patient')]"))).click()
        login.implicitly_wait(3)

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(first_name)
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(last_name)
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
        login.implicitly_wait(3)

        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))).click()
        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        login.implicitly_wait(5)

        login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
        login.implicitly_wait(5)
        login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
        print("Department : ENT")

        user_dropdown_xpath = ("(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid ng-dirty'])[1]")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_option_xpath))).click()
        print("Select user : Naveen")

        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        element = login.find_element(By.XPATH, service_dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        service_option_xpath = "(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen Consultation'])[2]"
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
        print("Select Service : Naveen Consultation")
        time.sleep(3)

        Today_Date = WebDriverWait(login, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
        login.execute_script("arguments[0].scrollIntoView();", Today_Date)
        Today_Date.click()
        print("Today Date:", Today_Date.text)

        time_slot = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
        time_slot.click()
        print("Time Slot:", time_slot.text)

        note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
        note_input.click()
        login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("test_selenium project")
        WebDriverWait(login, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Upload File']"))).click()
        time.sleep(4)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))
        pyautogui.write(absolute_path)
        pyautogui.press('enter')
        time.sleep(4)
        WebDriverWait(login, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))).click()
        time.sleep(3)

        accordion_tab = WebDriverWait(login, 10).until(EC.presence_of_element_located((By.XPATH, "//p-table[@class='p-element']")))
        accordion_tab.click()
        time.sleep(3)
        print("Before clicking View Details button")

        view_details_button = WebDriverWait(login, 30).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'View Details')]")))
        login.execute_script("arguments[0].click();", view_details_button)

        login.find_element(By.XPATH, "//span[normalize-space()='Prescriptions']").click()

        for i in range(5):
            login.find_element(By.XPATH, "//div[@class='add']").click()
            login.find_element(By.XPATH, "//input[@role='searchbox']").send_keys("Medicine")
            fill_prescription_details(login, i + 1, "650 mg", "1-1-1", "5 Days", "After Food")
        
    except Exception as e:
        print(f"Test failed: {e}")
        raise e