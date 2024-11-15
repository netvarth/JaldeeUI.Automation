from re import I
from Framework.common_utils import *  # Ensure you have imported this correctly in your project.
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Block the four slot")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_create_patient(login):
    # Navigate and interact with the website
    time.sleep(6)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]"))
    ).click()
    time.sleep(3)
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Block Slots']"))
    ).click()
    time.sleep(3)
    
    # Select location and department
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
    ).click()
    login.implicitly_wait(5)
    login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
    print("Location : Chavakkad")
    
    login.implicitly_wait(5)
    login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
    login.implicitly_wait(5)
    login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
    print("Department : ENT")
    
    # Select user
    user_dropdown_xpath = ("(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
                           "ng-dirty'])[1]")
    WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))).click()
    user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
    WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_option_xpath))).click()
    print("Select user : Naveen")
    
    # Select service
    service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
    element = login.find_element(By.XPATH, service_dropdown_xpath)
    login.execute_script("arguments[0].scrollIntoView();", element)
    element.click()
    
    service_option_xpath = "//span[@class='ng-star-inserted'][normalize-space()='Naveen Consultation']"
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
    print("Select Service : Naveen Consultation")
    time.sleep(3)
    
    # Select today's date
    today_date = WebDriverWait(login, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
    today_date.click()
    print("Today Date:", today_date.text)

        # --- Slot Selection and Text Capturing ---
    # Find all mat-chip-option elements
    slots = login.find_elements(By.CLASS_NAME, 'mat-mdc-chip-option')

    # Initialize a list to store selected slots' text
    selected_slots_text = []

   # Select four slots
    selected_count = 0
    for slot in slots:
        # Check if the slot is not already selected (aria-selected="false")
        if selected_count < 4 and "mat-mdc-chip-selected" not in slot.get_attribute("class"):
            # Capture the slot text and add it to the list
            selected_slots_text.append(slot.text)

            # Find the button inside the chip option and click it to select it
            button = slot.find_element(By.TAG_NAME, 'button')
            button.click()
            selected_count += 1
            # Optional: Wait for the selection to be applied
            time.sleep(0.5)  # Adjust timing if necessary

    # Optionally, print out the selected options for debugging
    print("Selected Slots:", selected_slots_text)

    
    # Add a note and confirm slot blocking
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@name='consumerNote']"))
    ).send_keys("Block slot test")
    time.sleep(3)
    
    confirm_button = WebDriverWait(login, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm']"))
    )
    login.execute_script("arguments[0].scrollIntoView(true);", confirm_button)
    confirm_button.click()

    # Verification of snackbar message
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
        
    

    # # Loop through tabs to check if the blocked slots appear in the "accord" tab
    # tabs = login.find_elements(By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')]")  # Modify this XPath to select the correct tab
    
    # # Click on the "Accord" tab if it's found
    # tabs[I].click()

    tabs = login.find_elements(By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')]")

    if tabs:
        for index, tab in enumerate(tabs):
            # Optional check if the tab is already expanded, for example using aria attributes
            is_expanded = tab.get_attribute('aria-expanded')
            if is_expanded != 'true':  # Adjust this condition based on the actual attribute your tabs use for expansion state
                try:
                    tab.click()
                    print(f"Accordion tab {index + 1} clicked")
                    # Optionally, you can add a delay if needed
                    time.sleep(1)  # Adjust the timing as necessary based on your UI's response time
                except Exception as e:
                    print(f"Failed to click tab {index + 1}: {e}")
    else:
        print("No tabs found")

    time.sleep(3)

    # Now, navigate through the pages and verify the slots
    page_number = 1
    matched_slots = []

    while True:
        print(f"Checking page {page_number}...")

        # Find all blocked slots on the current page (adjust this selector based on your dashboard's structure)
        dashboard_slots = login.find_elements(By.CLASS_NAME, 'blocked-slot-class')  # Modify the class name to match the slot's container
        
        # Check if any of the selected slots' times are found
        for dashboard_slot in dashboard_slots:
            try:
                slot_time = dashboard_slot.find_element(By.XPATH, ".//span[contains(@class, 'slot-time')]").text  # Adjust XPath if needed
                if slot_time in selected_slots_text:
                    matched_slots.append(slot_time)
                    print(f"Found blocked slot: {slot_time}")
            except:
                print("Error finding slot time on page.")
                continue

        # Check if all selected slots are found
        if len(matched_slots) >= len(selected_slots_text):
            print("All blocked slots found on the dashboard.")
            break
        
        # If not all slots are found, go to the next page
        try:
            next_page_button = login.find_element(By.XPATH, "//button[contains(@class, 'next-page')]")  # Modify XPath for the next page button
            next_page_button.click()
            time.sleep(2)  # Wait for the page to load
            page_number += 1
        except:
            print("No more pages to check.")
            break

    # Final validation
    if len(matched_slots) < len(selected_slots_text):
        print("Some blocked slots were not found on the dashboard.")
        return False
    else:
        print("All blocked slots successfully verified.")
        return True