import time
import allure
import sys
import os
import allure
import pytest
from ast import arguments
from tkinter import Label
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Framework.common_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
from selenium.webdriver.common.action_chains import ActionChains



##########################################################################################################################################################

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Appointment Pre deployment testing")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale_2, password)])
def test_walkin_appointment(login): 

   
    try:

        time.sleep(5)
       
        # print("New patient create")
        
        wait_and_click(login, By.XPATH, "(//div[@class='p-card p-component'])[3]")

        # time.sleep(3)
      
        # wait_and_click(login, By.XPATH, "(//div[@id='actionCreate_BUS_bookList'])[1]")
        
        # time.sleep(3)
        # print("Create new patient")
       
        # wait_and_click(login, By.XPATH, "(//span[@id='btnCreateCust_BUS_appt'])[1]")
        
        # login.implicitly_wait(3)
        # first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        # wait_and_send_keys(login, By.XPATH, "//input[@id='first_name']", str(first_name))
        # wait_and_send_keys(login, By.XPATH, "//input[@id='last_name']", str(last_name))
        # # wait_and_send_keys(login, By.XPATH, "//*[@id='customer_id']", cons_manual_id)
        # wait_and_send_keys(login, By.XPATH, "//*[@id='phone']", phonenumber)
        # wait_and_send_keys(login, By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']", phonenumber)
        # wait_and_send_keys(login, By.XPATH, "//input[@id='email_id']", email)
        # wait_and_click(login, By.XPATH, "//span[contains(text(),'Save')]")

        # time.sleep(3)
        # user_dropdown_xpath = ("//*[@id='selectUser_BUS_apptForm']")

        # wait_and_click(login, By.XPATH, user_dropdown_xpath)
        
        # user_option_xpath = ("//*[@class='ng-star-inserted'][normalize-space()='Anjali K']")
        # wait_and_click(login, By.XPATH, user_option_xpath)
        # print("Select user : Anjali K")

        # time.sleep(2)
        # wait_and_locate_click(
        #     login, By.XPATH, "//*[@id='selectService_BUS_apptForm']"
        # )

        # time.sleep(2)
        # wait_and_locate_click(login, By.XPATH, "//div[normalize-space()='Anjaly service 1']")
        # print("Select Service : Anjaly service 1")
        
        # time.sleep(3)

        # Today_Date = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (
        #             By.XPATH,
        #             "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']",
        #         )    
        #     )
        # )

        # click_to_element(login, Today_Date)
        # print("Today Date:", Today_Date.text)
        # wait = WebDriverWait(login, 10)
        # time_slot = wait.until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']"))
        # )
        # click_to_element(login, time_slot)

        # wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Confirm']")
        # time.sleep(4)
        
        # # WebDriverWait(login, 15).until(
        # #     EC.presence_of_element_located(
        # #         (By.XPATH, "//img[@src='./assets/images/menu/settings.png']"))
        # # ).click()
        
        
        # # fea_cust = login.find_element(By.XPATH, "//div[normalize-space()='Features and Customization']")
        # # login.execute_script("arguments[0].scrollIntoView();", fea_cust)
        
        # # time.sleep(3)
        # # WebDriverWait(login, 10).until(
        # #     EC.presence_of_element_located(
        # #         (By.XPATH, "//span[normalize-space()='Custom Fields']"))
        # # ).click()
        
        # # WebDriverWait(login, 10).until(
        # #     EC.presence_of_element_located(
        # #         (By.XPATH, "//span[normalize-space()='Label']"))
        # # ).click()
        
        # # label_name1 = "Label" + str(uuid.uuid1())[:3]
        # # label_namebox1 = WebDriverWait(login, 10).until(
        # # EC.presence_of_element_located((By.XPATH, "//input[@id='displayName']"))
        # # )
        # # label_namebox1.clear()
        # # label_namebox1.send_keys(label_name1)
        
        # # WebDriverWait(login, 10).until(
        # #     EC.presence_of_element_located(
        # #         (By.XPATH, "//span[@class='mdc-button__label']"))
        # # ).click()
        
        # # WebDriverWait(login, 10).until(
        # #     EC.presence_of_element_located(
        # #         (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']"))
        # # ).click()
        
        
        time.sleep(3)
        # wait_and_locate_click(login, By.XPATH, "(//img)[3]")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[normalize-space()='Appointment'])[1]")

        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter name or phone or id']", "9207206005")
        time.sleep(2)
        login.implicitly_wait(5)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Id : 26']")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//*[@id='selectUser_BUS_apptForm']")
        time.sleep(1)
        service = login.find_element(By.XPATH, "//span[normalize-space()='General Services']")
        scroll_to_element(login, service)
        service.click()

        # time.sleep(1)
        # wait_and_locate_click(login, By.XPATH, "//*[@id='selectService_BUS_apptForm']")

        # time.sleep(3)
        # service_option = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, ("//div[normalize-space()='geethu service 1']")))
        # )
        # click_to_element(login, service_option)
        
        # print("Select Service : geethu service 1']")

        time.sleep(3)
        Today_Date = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']",
                )
            )
        )
        time.sleep(2)
        click_to_element(login, Today_Date)

        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)

        wait_and_locate_click(login, By.XPATH, "//a[contains(text(),'Notes')]")
        
        wait_and_send_keys(login, By.XPATH, "//*[@id='tctareaMsg_BUS_addNote']", "Note added for walkin appointment")

        wait_and_visible_click(login, By.XPATH, "//span[normalize-space()='Save']")
         
        print("Note added for walkin appointment")

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Upload File']")

        time.sleep(4)
       # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        print("Successfully upload the file")

        time.sleep(3)

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnConfirm_BUS_apptForm'])[1]")
        
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)

        time.sleep(3)

        while True:
            try:
                
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                
                if next_button.is_enabled():
                   
                    login.execute_script("arguments[0].click();", next_button)
                else:
                  
                    break

            except Exception as e:
                
                break

        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(3)
        View_Detail_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnbooks_BUS_bookAction']")
            )
        )
        click_to_element(login, View_Detail_button)
        
        
        #************************************** Apply Label ***********************************************
        
        # time.sleep(3)
        # more_actions_button = WebDriverWait(login, 10).until(
        #     EC.visibility_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='More Actions']")
        #     )
        # )
        # more_actions_button.click()
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='Apply Labels']"))
        # ).click()
        
        # login.implicitly_wait(5)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='Create New']"))
        # ).click()
        
        # label_name = "Label" + str(uuid.uuid1())[:3]
        # label_namebox = WebDriverWait(login, 10).until(
        # EC.presence_of_element_located((By.XPATH, "//input[@id='displayName']"))
        # )
        # label_namebox.clear()
        # label_namebox.send_keys(label_name)
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='Create']"))
        # ).click()
        
        # label_xpath = f"//label[normalize-space()='{label_name}']"  

        # # Wait for the label to appear and click on it
        # label = WebDriverWait(login, 10).until(
        # EC.presence_of_element_located((By.XPATH, label_xpath))
        # )
        # login.execute_script("arguments[0].scrollIntoView();", label_xpath)
        # label.click()
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='Apply']"))
        # ).click()
        
        # Selected_label = WebDriverWait(login, 10).until(
        # EC.presence_of_element_located(
        #         (By.XPATH, label_xpath))
        # )

        # # Get the text of the confirmation message
        # actual_label = Selected_label.text
        # print("Selected Label:", actual_label)

        # # Assert the expected text
        # expected_label = Selected_label.text
        # assert (
        #     actual_label == expected_label
        # ), f"Expected '{expected_label}', but got '{actual_label}'"
        
        # # Applying Filter
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']"))
        # ).click()
        
        # login.implicitly_wait(5)
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//i[@class='pi pi-filter-fill']"))
        # ).click()
        
        # time.sleep(3)
        # Label_filter = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[contains(text(),'Labels')]"))
        # )
        # login.execute_script("arguments[0].scrollIntoView();", Label_filter)
        # Label_filter.click()
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//div[contains(text(),'Select Labels')]"))
        # ).click()

        # time.sleep(3)
        
        #  # Wait for the list to be visible
        # WebDriverWait(login, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, "//ul[@role='listbox']"))
        # )
        
        # # Locate all the list items
        # list_items = WebDriverWait(login, 10).until(
        #     EC.presence_of_all_elements_located((By.XPATH, "//ul[@role='listbox']//li"))
        # )

        # # Get the last item in the list
        # last_item = list_items[-1]

        # # Initialize ActionChains
        # actions = ActionChains(login)

        # # Move to the last item and click it
        # actions.move_to_element(last_item).click().perform()
        
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//timesicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']//*[name()='path' and contains(@d,'M8.01186 7')]"))
        # ).click()
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[contains(text(),'Apply')]"))
        # ).click()
        
        # time.sleep(3)
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')]"))
        #     ).click()
        
        # time.sleep(3)
        # assert (
        #     actual_label == expected_label
        # ), f"Expected '{expected_label}', but got '{actual_label}'"
        
        # time.sleep(2)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//i[@class='pi pi-filter-fill']"))
        # ).click()
        
        # time.sleep(3)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[normalize-space()='Reset']"))
        # ).click()
        
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//timesicon[contains(@class, 'p-element') and contains(@class, 'p-icon-wrapper') and contains(@class, 'ng-star-inserted')]//*[contains(@class, 'p-icon')]"))
        # ).click()
        
        # time.sleep(2)
        # login.refresh()
        
        # # time.sleep(5)
        # while True:
        #     try:
        #         # Attempt to locate the "Next" button using the button's class
        #         next_button = WebDriverWait(login, 10).until(
        #             EC.presence_of_element_located(
        #                 (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
        #             )
        #         )

        #         # Check if the button is enabled (i.e., not disabled)
        #         if next_button.is_enabled():
        #             # print("Next button found and clickable.")
        #             # Click using JavaScript to avoid interception issues
        #             login.execute_script("arguments[0].click();", next_button)
        #         else:
        #             # print("Next button is disabled. Reached the last page.")
        #             break

        #     except Exception as e:
        #         # # If no next button is found or any other exception occurs, exit the loop
        #         # print("End of pages or error encountered:", e)
        #         break

        # # After clicking through all pages, locate and click the last accordion
        # time.sleep(3)
        # last_element_in_accordian = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        # )
        # last_element_in_accordian.click()
        
        time.sleep(3)
        more_actions_button = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[normalize-space()='More Actions']")
            )
        )
        click_to_element(login, more_actions_button)
       
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//button[@id='btnChangeStat_BUS_bookAction'])[2]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//tr[@id='selectRow_BUS_assignUser'])[3]")

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "//*[normalize-space()='Yes']")

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)
        time.sleep(3)

        more_actions_button = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[normalize-space()='More Actions']")
            )
        )
        click_to_element(login, more_actions_button)

        time.sleep(2)
            
        # ****************************** Send Message **********************************************
    
        message_button = WebDriverWait(login, 15).until(
        EC.presence_of_element_located(
        (By.XPATH, "//button[normalize-space()='Send Message']"))
        )
        click_to_element(login, message_button)

        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//textarea[@id='messageData']", "Send Message to the Patient")

        time.sleep(3)
        wait_and_click(login, By.XPATH, "//label[normalize-space()='Click here to select the files']")
        
        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(4)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'send')]")

        get_snack_bar_message(login)
        print("Snack bar message:", get_snack_bar_message(login))

        # ******************* Send Attachment ************************
        time.sleep(5)
        wait_and_visible_click(login, By.XPATH, "//button[normalize-space()='Send Attachments']")

        time.sleep(2)
        wait_and_click(login, By.XPATH, "//label[normalize-space()='Click here to select the files']")

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()
        time.sleep(2)
        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        time.sleep(1)
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[contains(text(),'send')]")

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)
        
        # ********************* Create the Prescription and Sharing ******************************

        time.sleep(3)
        WebDriverWait(login, 10)

        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Prescriptions']")

        for i in range(5):
            wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='+ Add Medicine']")
            wait_and_send_keys( login, By.XPATH, "//input[@role='searchbox']", "Medicine")

            before_XPath = "//*[contains(@id, 'pr_id')]/tbody/tr"
            aftertd_XPath_1 = "/td[2]"
            aftertd_XPath_2 = "/td[3]"
            aftertd_XPath_3 = "/td[4]"
            aftertd_XPath_4 = "/td[5]"
            textarea_xpath = "//input[@role='searchbox']"
            row = i + 1
            if i > 0:
                trXPath = before_XPath + str([row])
            else:
                trXPath = before_XPath

            PreFinalXPath = trXPath + aftertd_XPath_1
            FinalXPath = PreFinalXPath + textarea_xpath

            Dose = login.find_element(By.XPATH, PreFinalXPath)
            Dose.click()
            Dose1 = login.find_element(By.XPATH, FinalXPath)
            Dose1.send_keys("650 mg")

            PreFinalXPath = trXPath + aftertd_XPath_2
            FinalXPath = PreFinalXPath + textarea_xpath

            Frequency = login.find_element(By.XPATH, PreFinalXPath)
            Frequency.click()
            Frequency1 = login.find_element(By.XPATH, FinalXPath)
            Frequency1.send_keys("1-1-1")

            PreFinalXPath = trXPath + aftertd_XPath_3
            FinalXPath = PreFinalXPath + textarea_xpath
            Duration = login.find_element(By.XPATH, PreFinalXPath)
            Duration.click()
            Duration1 = login.find_element(By.XPATH, FinalXPath)
            Duration1.send_keys("5 Days")

            PreFinalXPath = trXPath + aftertd_XPath_4
            FinalXPath = PreFinalXPath + textarea_xpath
            Notes = login.find_element(By.XPATH, PreFinalXPath)
            Notes.click()
            Notes1 = login.find_element(By.XPATH, FinalXPath)
            Notes1.send_keys("After Food")

        # Handle the dropdown element
        # dropdown_locator_xpath = ("//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-provider-appointment-detail[1]/div[1]/div[1]/div[1]/div[1]/app-booking-details[1]/div[2]/app-customer-record[1]/div[1]/div[2]/div[1]/app-prescriptions[1]/div[1]/div[1]/div[2]/div[1]/app-create[1]/div[1]/div[3]/div[1]/span[1]/mat-select[1]/div[1]/div[2]/div[1]/*[1]")
        # dropdown_element = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, dropdown_locator_xpath))
        # )
        # dropdown_element.click()
        # wait_and_locate_click(login, By.XPATH, "//mat-select[@aria-haspopup='listbox']")
        
        # time.sleep(3)
        # element3 = login.find_element(By.XPATH, "//span[@class='mdc-list-item__primary-text']//div[contains(text(),'Naveen KP')]")
        # click_to_element(login, element3)
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Save']")
        
        # toast_message = WebDriverWait(login, 10).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        # )
        # message = toast_message.text
        # print("Toast Message:", message)

        # print("prescription created successfully")
        time.sleep(2)

        login.find_element(By.XPATH, "//img[@alt='share']").click()

        time.sleep(2)
        login.find_element(
            By.XPATH, "//textarea[@placeholder='Enter message description']"
        ).send_keys("prescription message")

        login.find_element(
            By.XPATH, "(//input[@class='mdc-checkbox__native-control'])[1]"
        ).click()
        login.find_element(By.XPATH, "//span[normalize-space()='Whatsapp']").click()
        login.find_element(By.XPATH, "//button[@type='button'][normalize-space()='Share']").click()

        print("Prescription Shared Successfully")


        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//img[@src='./assets/images/menu/settings.png'])[1]")

        time.sleep(2)
        setting_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[normalize-space()='POS Ordering'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", setting_element)

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//p[normalize-space()='RX Push Management System'])[1]")

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//*[name()='svg'][@class='mdc-switch__icon mdc-switch__icon--off'])[1]")

        get_snack_bar_message(login)
        print("Snack bar message:", get_snack_bar_message(login))
        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "(//img)[3]")

        time.sleep(2)
        while True:
            try:
                
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                
                if next_button.is_enabled():
                   
                    login.execute_script("arguments[0].click();", next_button)
                else:
                  
                    break

            except Exception as e:
                
                break

        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(3)
        View_Detail_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(), 'View Details')]")
            )
        )
        click_to_element(login, View_Detail_button)

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Prescriptions']")

        time.sleep(2)

        # Loop through rows and interact with each row
        # Medicines: first is manual, rest are normal
        medicines_to_add = [
            {"name": "Paracetamol", "manual": True},  # manual entry
            {"name": "Dolo", "manual": False},
            {"name": "Crocin", "manual": False}
        ]
        for index, med in enumerate(medicines_to_add):
            # Click the "+ Add Medicine" button
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[normalize-space()='+ Add Medicine']")
                )
            ).click()

            # Find the search box
            search_box = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[role='searchbox']"))
            )
            search_box.clear()
            search_box.send_keys(med["name"])
            time.sleep(1)

            if not med["manual"]:
                # Normal item → pick from autocomplete
                suggestions = login.find_elements(By.CSS_SELECTOR, ".p-autocomplete-item")
                if suggestions:
                    suggestions[0].click()
            else:
                # Manual (ADOCH) item → confirm typed entry
                search_box.send_keys(Keys.ENTER)

            time.sleep(1)

            # Locate the current row
            row = wait.until(
                EC.presence_of_element_located((By.XPATH, f"//tbody/tr[{index + 1}]"))
            )

            # Duration
            duration = row.find_element(By.XPATH, ".//td[5]/input[@type='number']")
            duration.clear()
            duration.send_keys("5")

            # Frequency dropdown
            dropdown_trigger = row.find_element(
                By.XPATH, ".//td[4]//div[contains(@class, 'p-dropdown-trigger')]"
            )
            dropdown_trigger.click()

            dropdown_options = WebDriverWait(login, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//div[contains(@class,'p-dropdown-items-wrapper')]//li")
                )
            )
            if dropdown_options:
                option_to_click = random.choice(dropdown_options)
                login.execute_script("arguments[0].scrollIntoView(true);", option_to_click)
                time.sleep(0.5)
                login.execute_script("arguments[0].click();", option_to_click)

            # Qty
            qty_input = row.find_element(By.XPATH, ".//td[6]/input[@type='number']")
            qty_input.clear()
            qty_input.send_keys("1")

            
            # Remarks
            row.find_element(By.XPATH, ".//td[7]").click()
            remarks = row.find_element(By.XPATH, "//input[@role='searchbox']")
            remarks.clear()
            remarks.send_keys(f"Notes for {med['name']}")

            time.sleep(1)

        # Finally submit
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Create Prescription']")
            )
        ).click()

        time.sleep(3)  # Wait for the prescription to be processed
        
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Push RX']"))
        ).click()

        store = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[normalize-space()='Thrissur']"))
        )
        store.click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[normalize-space()='Push']"))
        ).click()

        msg = get_toast_message(login)
        print("Toast Message : ", msg) 
        time.sleep(3)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//img)[6]"))
        ).click()



        time.sleep(2)
        
        RX_request_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='btnRXReq_ORD_Dashbrd']"))
        )

        scroll_to_element(login, RX_request_element) 
        time.sleep(1)
        RX_request_element.click()

        time.sleep(2)
        # Wait for the table to be present
        table_body = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody"))
        )

        # Locate the first table row
        first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")
                                                                    
        # Find the status element within the first row
        status_element = first_row.find_element(By.XPATH, '(.//span[contains(@class, "status-")])[2]')
        status_text = status_element.text
        expected_status = "Pushed"

        print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

        # Assert that the status is "Pushed"
        assert status_text == "Pushed", f"Expected status to be 'Pushed', but got '{status_text}'"

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//img[@src='./assets/images/menu/settings.png'])[1]")

        time.sleep(2)
        setting_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//div[normalize-space()='POS Ordering'])[1]"))
        )

        login.execute_script("arguments[0].scrollIntoView();", setting_element)

        time.sleep(1)
        wait_and_locate_click(login, By.XPATH, "(//p[normalize-space()='RX Push Management System'])[1]")

        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//label[normalize-space()='RX Push  On'])[1]")

        msg = get_snack_bar_message(login)
        print("Snack bar message:", msg)


        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//img)[3]")    

        time.sleep(3)
        while True:
            try:
                
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                
                if next_button.is_enabled():
                   
                    login.execute_script("arguments[0].click();", next_button)
                else:
                  
                    break

            except Exception as e:
                
                break

        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(3)
        View_Detail_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(), 'View Details')]")
            )
        )
        click_to_element(login, View_Detail_button)



        # ************************* Case Creation and Sharing *********************

        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//span[normalize-space()='Patient Record']")
        
        login.implicitly_wait(5)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='+ Create Case']")
    
        time.sleep(3)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Case Description']", "test case for case")
        

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']")
            )
        ).click()

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder = 'Enter Chief Complaint']")
            )
        ).send_keys("Fever")

        element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']"))
        )
        login.execute_script("arguments[0].click();", element)
        
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='History']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder ='Enter History']"))
        ).send_keys("viral fever",Keys.RETURN)
        
        element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']"))
        )
        login.execute_script("arguments[0].click();", element)

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Medication']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Medication']"))
        ).send_keys("no medication",Keys.RETURN)
        
        time.sleep(1)
        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].click();", element)
        

        # time.sleep(2)
        # toast_message = WebDriverWait(login, 10).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        # )
        # message = toast_message.text
        # print("Toast Message:", message)

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Vital Signs']")
            )
        ).click()

        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Pulse Rate , Max : 999']"
        ).send_keys("560")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Respiration , Max : 90']"
        ).send_keys("62")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Temperature in °F , Max : 200']"
        ).send_keys("123")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Systolic , Max : 500']"
        ).send_keys("264")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Diastolic , Max : 500']"
        ).send_keys("287")

        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        # login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Treatment Plan']"))
        ).click()
        
    
        treat_name = "Treatment" + str(uuid.uuid4())[:4]
        treat_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@role='searchbox']"))
        )
        treat_namebox.clear()
        treat_namebox.send_keys(treat_name)
        
        
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='p-multiselect-label p-placeholder']"))
        ).click()
        
        
        dropdown_xpath = "//span[normalize-space()='Geethu N P']"
        element = login.find_element(By.XPATH, dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        
        time.sleep(3)
        
        
        WebDriverWait(login, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@class='btn btn-white shadow fw-bold']"))
        ).click()
        
        step_name = "Step" + str(uuid.uuid1())[:1]
        step_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Name']"))
        )
        step_namebox.clear()
        step_namebox.send_keys(step_name)
        
        
        WebDriverWait(login, 10).until(
           EC.presence_of_element_located(
               (By.XPATH, "//p-multiselect[@optionlabel='firstName']//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted']"))
       ).click()
        
        time.sleep(2)
        element1 = login.find_element(By.XPATH, dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element1)
        element1.click()
        
        time.sleep(3)
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='d-flex']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']")
            )
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='In Progress']"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Step Notes']"))
        ).send_keys("Steps for notes")
        
        WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//label[@for='treatmentPlanAattachments']")
        )
        ).click()

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Treatment Notes']"))
        ).send_keys("Note for the treatment")
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']"))
        ).click()
        

        
        element2 = login.find_element(By.XPATH, "//span[normalize-space()='Add the sections you need for this medical record']")
        login.execute_script("arguments[0].scrollIntoView();", element2)
        element2.click()

        # time.sleep(2)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='Observations']")
        #     )
        # ).click()

        # time.sleep(3)
        
        # login.find_element(
        #     By.XPATH, "//input[@placeholder='Enter Observations']"
        # ).send_keys("Minor fever",Keys.RETURN)
        
        # time.sleep(2)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[normalize-space()='minor fever']")
        #     )
        # ).click()

        # element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        # login.execute_script("arguments[0].scrollIntoView();", element)
        # element.click()

        # toast_message = WebDriverWait(login, 10).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        # )
        # message = toast_message.text
        # print("Toast Message:", message)

        # time.sleep(2)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='Diagnosis']")
        #     )
        # ).click()

        # login.find_element(
        #     By.XPATH, "//input[@placeholder='Enter Diagnosis']"
        # ).send_keys("High temperature",Keys.RETURN)
        
        # time.sleep(2)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[normalize-space()='high temperature']")
        #     )
        # ).click()

        # element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        # login.execute_script("arguments[0].scrollIntoView();", element)
        # element.click()

        # toast_message = WebDriverWait(login, 10).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        # )
        # message = toast_message.text
        # print("Toast Message:", message)

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Prescription']")
            )
        ).click()

        for i in range(5):
            login.find_element(
                By.XPATH, "//button[normalize-space()='+ Add Medicine']"
            ).click()
            login.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(
                "Medicine"
            )

            before_XPath = "//*[contains(@id, 'pr_id')]/tbody/tr"
            aftertd_XPath_1 = "/td[2]"
            aftertd_XPath_2 = "/td[3]"
            aftertd_XPath_3 = "/td[4]"
            aftertd_XPath_4 = "/td[5]"
            textarea_xpath = "//input[@role='searchbox']"
            row = i + 1
            if i > 0:
                trXPath = before_XPath + str([row])
            else:
                trXPath = before_XPath

            PreFinalXPath = trXPath + aftertd_XPath_1
            FinalXPath = PreFinalXPath + textarea_xpath

            Dose = login.find_element(By.XPATH, PreFinalXPath)
            Dose.click()
            Dose1 = login.find_element(By.XPATH, FinalXPath)
            Dose1.send_keys("650 mg")

            PreFinalXPath = trXPath + aftertd_XPath_2
            FinalXPath = PreFinalXPath + textarea_xpath

            Frequency = login.find_element(By.XPATH, PreFinalXPath)
            Frequency.click()
            Frequency1 = login.find_element(By.XPATH, FinalXPath)
            Frequency1.send_keys("1-1-1")

            PreFinalXPath = trXPath + aftertd_XPath_3
            FinalXPath = PreFinalXPath + textarea_xpath
            Duration = login.find_element(By.XPATH, PreFinalXPath)
            Duration.click()
            Duration1 = login.find_element(By.XPATH, FinalXPath)
            Duration1.send_keys("5 Days")

            PreFinalXPath = trXPath + aftertd_XPath_4
            FinalXPath = PreFinalXPath + textarea_xpath
            Notes = login.find_element(By.XPATH, PreFinalXPath)
            Notes.click()
            Notes1 = login.find_element(By.XPATH, FinalXPath)
            Notes1.send_keys("After Food")

        
       
        # dropdown_element= WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//mat-select[@aria-haspopup='listbox']"))
        # )
        # dropdown_element.click()
        
        # time.sleep(3)
        # element3 = login.find_element(By.XPATH, "//span[@class='mdc-list-item__primary-text']//div[contains(text(),'Naveen KP')]")
        # login.execute_script("arguments[0].click();", element3)
        
        
    
        time.sleep(2)
        login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        time.sleep(2)
        # toast_message = WebDriverWait(login, 10).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        # )
        # message = toast_message.text
        # print("Toast Message:", message)
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[@class='add-action-btn']"))
        ).click()
        
        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Share')]")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter message description']")
            )
        ).send_keys("case sharing testing")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Email')]"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Whatsapp')]"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(),'Share')]")
            )
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        # print("Case file Shared successfully")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//i[@class='pi pi-arrow-left back-btn-arrow']")
            )
        ).click()

        WebDriverWait(login, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
            )
        ).click()

        while True:
            try:
                # Attempt to locate the "Next" button using the button's class
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                # Check if the button is enabled (i.e., not disabled)
                if next_button.is_enabled():
                    # print("Next button found and clickable.")
                    # Click using JavaScript to avoid interception issues
                    login.execute_script("arguments[0].click();", next_button)
                else:
                    # print("Next button is disabled. Reached the last page.")
                    break

            except Exception as e:
                # # If no next button is found or any other exception occurs, exit the loop
                # print("End of pages or error encountered:", e)
                break

        # After clicking through all pages, locate and click the last accordion
        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        # ************************* Auto Invoice and Sharing ************************

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='View Invoice']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Send']")
            )
        ).click()
        print("Auto Invoice")
        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Edit']"))
        ).click()
        
        time.sleep(2)
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        ).click()
        time.sleep(1)
        user_service = login.find_element(By.XPATH, "//input[@placeholder='Choose Procedure/Item']")
        user_service.click()
        time.sleep(2)
        user_service.send_keys("g")

        time.sleep(2)    
        service1 = login.find_element(By.XPATH, "//div[contains(text(),'geethu service 1')]")
        scroll_to_element(login, service1)
        service1.click()

        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add']")
        print("Added Sub Service to the Invoice")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add Procedure/Item']")
        
        item_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Choose Procedure/Item']"))
        )
        item_button.click()
        item_button.send_keys("item1234")
          
        time.sleep(3)
        price = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='mat-input-4'])[2]"))
        )
        price.clear()
        price.click()
        price.send_keys("1")
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Add']")
        print("Added ADHOC item to the Invoice")
        
        time.sleep(3)
        update_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", update_button)
        update_button.click()
        
          
        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)        
        time.sleep(3)
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Send']")
            )
        ).click()
        
        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)
        
        time.sleep(4)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Pay by Cash']"))
        ).click()

        pay_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Pay']"))
        )
        login.execute_script("arguments[0].click();", pay_button)

        time.sleep(3)
        yes_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space(.)='Yes']"))
        )
        login.execute_script("arguments[0].click();", yes_button)
        
        
        time.sleep(3)

        login.find_element(By.XPATH, "//i[@class='fa fa-arrow-left']").click()

        while True:
            try:
                # Attempt to locate the "Next" button using the button's class
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                # Check if the button is enabled (i.e., not disabled)
                if next_button.is_enabled():
                    # print("Next button found and clickable.")
                    # Click using JavaScript to avoid interception issues
                    login.execute_script("arguments[0].click();", next_button)
                else:
                    # print("Next button is disabled. Reached the last page.")
                    break

            except Exception as e:
                # # If no next button is found or any other exception occurs, exit the loop
                # print("End of pages or error encountered:", e)
                break

        # After clicking through all pages, locate and click the last accordion
        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        # ********************** Manual Invoice and Sharing ***********************

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='New Invoice']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']")
            )
        ).click()

        time.sleep(1)
        time.sleep(1)
        user_service = login.find_element(By.XPATH, "//input[@placeholder='Choose Procedure/Item']")
        user_service.click()
        time.sleep(2)
        user_service.send_keys("g")
        
        time.sleep(2)    
        service1 = login.find_element(By.XPATH, "//div[contains(text(),'geethu service 1')]")
        scroll_to_element(login, service1)
        service1.click()

        wait_and_locate_click(login, By.XPATH, "//*[normalize-space()='Add']")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Update']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Send']")
            )
        ).click()
        print("Manual Invoice")

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)
    
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Edit']"))
        ).click()
        
        time.sleep(2)
        
        add_service = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        )
        login.execute_script("arguments[0].click();", add_service)
        
        time.sleep(3)    
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='Naveen Consultation 1']"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        print("Added Sub Service to the Invoice")
        
        time.sleep(2)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        # ).click()
        login.execute_script("arguments[0].click();", add_service)
        item_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Choose Procedure/Item']"))
        )
        item_button.click()
        item_button.send_keys("item1234")
        
        time.sleep(3)
        price = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='mat-input-4'])[2]"))
        )
        price.clear()
        price.click()
        price.send_keys("102")
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        print("Added ADHOC item to the Invoice")
        
        time.sleep(3)
        update_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", update_button)
        update_button.click()
        
        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)
          
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Send']")
            )
        ).click()
        
        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)
        

        time.sleep(3)
        # print("Successfully send the Payment Link to the patient")

        login.find_element(By.XPATH, "//i[@class='fa fa-arrow-left']").click()

        while True:
            try:
                # Attempt to locate the "Next" button using the button's class
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                # Check if the button is enabled (i.e., not disabled)
                if next_button.is_enabled():
                    # print("Next button found and clickable.")
                    # Click using JavaScript to avoid interception issues
                    login.execute_script("arguments[0].click();", next_button)
                else:
                    # print("Next button is disabled. Reached the last page.")
                    break

            except Exception as e:
                # # If no next button is found or any other exception occurs, exit the loop
                # print("End of pages or error encountered:", e)
                break

        # After clicking through all pages, locate and click the last accordion
        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(3)
        # print("Before clicking View Details button")
        View_Detail_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(), 'View Details')]")
            )
        )
        View_Detail_button.click()

        # *************************** Reschedule **********************

        time.sleep(3)
        login.find_element(By.XPATH, "//button[contains(text(),'Reschedule')]").click()
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='reschedule-date-picker']")
            )
        ).click()

        today_date = datetime.now()
        print(today_date.day)
        today_xpath_expression = "//span[@class='example-custom-date-class d-pad-15 ng-star-inserted'][normalize-space()='{}']".format(
            today_date.day
        )
        print(today_xpath_expression)
        tomorrow_date = today_date + timedelta(days=1)
        print(tomorrow_date.day)
#===============================================================
        # current_month = WebDriverWait(login, 10).until(
        # EC.presence_of_element_located(
        #     (By.XPATH, "//button[contains(@class, 'p-datepicker-month')]"))
        # )

        # current_year = WebDriverWait(login, 10).until(
        # EC.presence_of_element_located(
        #     (By.XPATH, "//button[contains(@class, 'p-datepicker-year')]"))
        # )

        # if current_month.text.lower() != tomorrow_date.strftime("%b").lower() or current_year.text.lower() != tomorrow_date.strftime("%Y").lower():

        #     login.find_element(By.XPATH, "//button[contains(@class, 'p-datepicker-next')]").click()
#===============================================================
        tomorrow_xpath_expression = "//span[@class='example-custom-date-class d-pad-15 ng-star-inserted'][normalize-space()='{}']".format(
            tomorrow_date.day
        )
        print(tomorrow_xpath_expression)

        Tomorrow_Date = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, tomorrow_xpath_expression))
        )
        Tomorrow_Date.click()
        print("Tomorrow Date:", Tomorrow_Date.text)

        wait = WebDriverWait(login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected= 'false']"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)

        reschedule_button = WebDriverWait(login, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='btn btn-primary reschedule-btn']")
            )
        )
        reschedule_button.click()

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
        # print("Reschedule Successfully")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Today')]")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Future']")
            )
        ).click()

        time.sleep(3)
        last_accordian = WebDriverWait(login, 15).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
                )
            )
        )
        last_accordian.click()

        # *******************Cancellation **********************

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Change Status']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Cancel')]")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'No Show Up')]")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Ok']"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message) 

        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
        ).click()

        time.sleep(1)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Today'])[1]"))
        ).click()

        time.sleep(1)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Appointment'])[1]")) 
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
            )
        ).send_keys("9207206005")
        time.sleep(2)
        login.implicitly_wait(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Id : 2']")
            )
        ).click()


        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//i[@class='fa fa-pencil-square-o'])[1]"))
        ).click()

        time.sleep(1)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//label[normalize-space()='Archana Gopi'])[1]"))
        ).click()

        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='Okay'])[1]"))
        ).click()

        time.sleep(2)
        user_dropdown_xpath = (
            "(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
            "ng-dirty'])[1]"
        )
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))
        ).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, user_option_xpath))
        ).click()
        print("Select user : Naveen")

        # service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        element = login.find_element(By.XPATH, "//p-dropdown[@optionlabel='name']")
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        # service_option_xpath = ("//li[@aria-label='Naveen Consultation']//div[1]")
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, ("//li[@aria-label='Naveen Consultation']//div[1]")))
        ).click()
        print("Select Service : Naveen Consultation")
        time.sleep(5)
        Today_Date = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']",
                )
            )
        )
        time.sleep(2)
        Today_Date.click()
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Notes')]"))
        ).click()

        login.find_element(By.XPATH, "//textarea[@id='message']").send_keys(
            "Note for the walkin appointment"
        )

        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[normalize-space()='Save']")
            )
        ).click()
        print("Note added for walkin appointment")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Upload File']")
            )
        ).click()

        time.sleep(4)
       # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        print("Successfully upload the file")

        time.sleep(3)

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Confirm')]")
            )
        ).click()

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

        time.sleep(3)

        while True:
            try:
                
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                
                if next_button.is_enabled():
                   
                    login.execute_script("arguments[0].click();", next_button)
                else:
                  
                    break

            except Exception as e:
                
                break

        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(3)
        View_Detail_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(), 'View Details')]")
            )
        )
        View_Detail_button.click()

        time.sleep(3)
        more_actions_button = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[normalize-space()='More Actions']")
            )
        )
        more_actions_button.click()
        
        
            
        # ****************************** Send Message **********************************************
    
        time.sleep(3)
        message_button = WebDriverWait(login, 15).until(
        EC.presence_of_element_located(
        (By.XPATH, "//button[normalize-space()='Send Message']"))
        )
        login.execute_script("arguments[0].click();", message_button)

        time.sleep(2)
        login.find_element(By.XPATH, " //textarea[@id='messageData']").send_keys(
            "Send Message to the Patient"
        )

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//label[normalize-space()='Click here to select the files']",
                )
            )
        ).click()

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(4)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'send')]")
            )
        ).click()

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

        # print("Send Message Successfully")

        # ******************* Send Attachment ************************
        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[normalize-space()='Send Attachments']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//label[normalize-space()='Click here to select the files']",
                )
            )
        ).click()

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'send')])[1]")
            )
        ).click()

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

        # print("Attachment Send Successfully")

        # ********************* Create the Prescription and Sharing ******************************

        time.sleep(5)
        WebDriverWait(login, 10)
        login.find_element(
            By.XPATH, "//span[normalize-space()='Prescriptions']"
        ).click()

        for i in range(5):
            login.find_element(
                By.XPATH, "//button[normalize-space()='+ Add Medicine']"
            ).click()
            login.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(
                "Medicine"
            )

            before_XPath = "//*[contains(@id, 'pr_id')]/tbody/tr"
            aftertd_XPath_1 = "/td[2]"
            aftertd_XPath_2 = "/td[3]"
            aftertd_XPath_3 = "/td[4]"
            aftertd_XPath_4 = "/td[5]"
            textarea_xpath = "//input[@role='searchbox']"
            row = i + 1
            if i > 0:
                trXPath = before_XPath + str([row])
            else:
                trXPath = before_XPath

            PreFinalXPath = trXPath + aftertd_XPath_1
            FinalXPath = PreFinalXPath + textarea_xpath

            Dose = login.find_element(By.XPATH, PreFinalXPath)
            Dose.click()
            Dose1 = login.find_element(By.XPATH, FinalXPath)
            Dose1.send_keys("650 mg")

            PreFinalXPath = trXPath + aftertd_XPath_2
            FinalXPath = PreFinalXPath + textarea_xpath

            Frequency = login.find_element(By.XPATH, PreFinalXPath)
            Frequency.click()
            Frequency1 = login.find_element(By.XPATH, FinalXPath)
            Frequency1.send_keys("1-1-1")

            PreFinalXPath = trXPath + aftertd_XPath_3
            FinalXPath = PreFinalXPath + textarea_xpath
            Duration = login.find_element(By.XPATH, PreFinalXPath)
            Duration.click()
            Duration1 = login.find_element(By.XPATH, FinalXPath)
            Duration1.send_keys("5 Days")

            PreFinalXPath = trXPath + aftertd_XPath_4
            FinalXPath = PreFinalXPath + textarea_xpath
            Notes = login.find_element(By.XPATH, PreFinalXPath)
            Notes.click()
            Notes1 = login.find_element(By.XPATH, FinalXPath)
            Notes1.send_keys("After Food")

        # Handle the dropdown element
        # dropdown_locator_xpath = ("//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-provider-appointment-detail[1]/div[1]/div[1]/div[1]/div[1]/app-booking-details[1]/div[2]/app-customer-record[1]/div[1]/div[2]/div[1]/app-prescriptions[1]/div[1]/div[1]/div[2]/div[1]/app-create[1]/div[1]/div[3]/div[1]/span[1]/mat-select[1]/div[1]/div[2]/div[1]/*[1]")
        # dropdown_element = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, dropdown_locator_xpath))
        # )
        # dropdown_element.click()

        dropdown_element= WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//mat-select[@aria-haspopup='listbox']"))
        )
        dropdown_element.click()
        
        time.sleep(3)
        element3 = login.find_element(By.XPATH, "//span[@class='mdc-list-item__primary-text']//div[contains(text(),'Naveen KP')]")
        login.execute_script("arguments[0].click();", element3)
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']"))
        ).click()
        
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        # print("prescription created successfully")
        time.sleep(2)
        login.find_element(By.XPATH, "//img[@alt='share']").click()

        time.sleep(2)
        login.find_element(
            By.XPATH, "//textarea[@placeholder='Enter message description']"
        ).send_keys("prescription message")

        login.find_element(
            By.XPATH, "(//input[@class='mdc-checkbox__native-control'])[1]"
        ).click()
        login.find_element(By.XPATH, "//span[normalize-space()='Whatsapp']").click()
        login.find_element(By.XPATH, "//button[@type='button'][normalize-space()='Share']").click()
        login.find_element(
            By.XPATH, "//textarea[@placeholder='Enter message description']"
        ).send_keys("Prescription Message to Patient")

        # toast_message = WebDriverWait(login, 10).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        # )
        # message = toast_message.text
        # print("Toast Message:", message)

        print("Prescription Shared Successfully")

        # ************************* Case Creation and Sharing *********************

        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Patient Record']"))
        ).click()

        login.implicitly_wait(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='+ Create Case']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Case Description']")
            )
        ).send_keys("test case for case")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']")
            )
        ).click()

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder = 'Enter Chief Complaint']")
            )
        ).send_keys("Fever")

        element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']"))
        )
        login.execute_script("arguments[0].click();", element)
        
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='History']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder ='Enter History']"))
        ).send_keys("viral fever",Keys.RETURN)
        
        element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']"))
        )
        login.execute_script("arguments[0].click();", element)

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Medication']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Medication']"))
        ).send_keys("no medication",Keys.RETURN)
        
        time.sleep(1)
        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].click();", element)
        

        # time.sleep(2)
        # toast_message = WebDriverWait(login, 10).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        # )
        # message = toast_message.text
        # print("Toast Message:", message)

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Vital Signs']")
            )
        ).click()

        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Pulse Rate , Max : 999']"
        ).send_keys("560")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Respiration , Max : 90']"
        ).send_keys("62")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Temperature in °F , Max : 200']"
        ).send_keys("123")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Systolic , Max : 500']"
        ).send_keys("264")
        login.find_element(
            By.XPATH, "//input[@placeholder='Enter Diastolic , Max : 500']"
        ).send_keys("287")

        element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        # login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Treatment Plan']"))
        ).click()
        
    
        treat_name = "Treatment" + str(uuid.uuid4())[:4]
        treat_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@role='searchbox']"))
        )
        treat_namebox.clear()
        treat_namebox.send_keys(treat_name)
        
        
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='p-multiselect-label p-placeholder']"))
        ).click()
        
        
        dropdown_xpath = "//span[normalize-space()='Naveen KP']"
        element = login.find_element(By.XPATH, dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        
        time.sleep(3)
        
        
        WebDriverWait(login, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@class='btn btn-white shadow fw-bold']"))
        ).click()
        
        step_name = "Step" + str(uuid.uuid1())[:1]
        step_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Name']"))
        )
        step_namebox.clear()
        step_namebox.send_keys(step_name)
        
        
        WebDriverWait(login, 10).until(
           EC.presence_of_element_located(
               (By.XPATH, "//p-multiselect[@optionlabel='firstName']//span[@class='p-multiselect-trigger-icon fa fa-caret-down ng-star-inserted']"))
       ).click()
        
        time.sleep(2)
        element1 = login.find_element(By.XPATH, dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element1)
        element1.click()
        
        time.sleep(3)
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='d-flex']//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted']")
            )
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='In Progress']"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Step Notes']"))
        ).send_keys("Steps for notes")
        
        WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//label[@for='treatmentPlanAattachments']")
        )
        ).click()

        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter Treatment Notes']"))
        ).send_keys("Note for the treatment")
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Save']"))
        ).click()
        

        
        element2 = login.find_element(By.XPATH, "//span[normalize-space()='Add the sections you need for this medical record']")
        login.execute_script("arguments[0].scrollIntoView();", element2)
        element2.click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Prescription']")
            )
        ).click()

        for i in range(5):
            login.find_element(
                By.XPATH, "//button[normalize-space()='+ Add Medicine']"
            ).click()
            login.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(
                "Medicine"
            )

            before_XPath = "//*[contains(@id, 'pr_id')]/tbody/tr"
            aftertd_XPath_1 = "/td[2]"
            aftertd_XPath_2 = "/td[3]"
            aftertd_XPath_3 = "/td[4]"
            aftertd_XPath_4 = "/td[5]"
            textarea_xpath = "//input[@role='searchbox']"
            row = i + 1
            if i > 0:
                trXPath = before_XPath + str([row])
            else:
                trXPath = before_XPath

            PreFinalXPath = trXPath + aftertd_XPath_1
            FinalXPath = PreFinalXPath + textarea_xpath

            Dose = login.find_element(By.XPATH, PreFinalXPath)
            Dose.click()
            Dose1 = login.find_element(By.XPATH, FinalXPath)
            Dose1.send_keys("650 mg")

            PreFinalXPath = trXPath + aftertd_XPath_2
            FinalXPath = PreFinalXPath + textarea_xpath

            Frequency = login.find_element(By.XPATH, PreFinalXPath)
            Frequency.click()
            Frequency1 = login.find_element(By.XPATH, FinalXPath)
            Frequency1.send_keys("1-1-1")

            PreFinalXPath = trXPath + aftertd_XPath_3
            FinalXPath = PreFinalXPath + textarea_xpath
            Duration = login.find_element(By.XPATH, PreFinalXPath)
            Duration.click()
            Duration1 = login.find_element(By.XPATH, FinalXPath)
            Duration1.send_keys("5 Days")

            PreFinalXPath = trXPath + aftertd_XPath_4
            FinalXPath = PreFinalXPath + textarea_xpath
            Notes = login.find_element(By.XPATH, PreFinalXPath)
            Notes.click()
            Notes1 = login.find_element(By.XPATH, FinalXPath)
            Notes1.send_keys("After Food")

        
       
        dropdown_element= WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//mat-select[@aria-haspopup='listbox']"))
        )
        dropdown_element.click()
        
        time.sleep(3)
        element3 = login.find_element(By.XPATH, "//span[@class='mdc-list-item__primary-text']//div[contains(text(),'Naveen KP')]")
        login.execute_script("arguments[0].click();", element3)
        
        
    
        time.sleep(2)
        login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        time.sleep(2)
        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[@class='add-action-btn']"))
        ).click()
        
        time.sleep(3)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\test.png")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Share')]")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Enter message description']")
            )
        ).send_keys("case sharing testing")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Email')]"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Whatsapp')]"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(),'Share')]")
            )
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)

        # print("Case file Shared successfully")

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//i[@class='pi pi-arrow-left back-btn-arrow']")
            )
        ).click()

        WebDriverWait(login, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
            )
        ).click()

        while True:
            try:
                # Attempt to locate the "Next" button using the button's class
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
                    )
                )

                # Check if the button is enabled (i.e., not disabled)
                if next_button.is_enabled():
                    # print("Next button found and clickable.")
                    # Click using JavaScript to avoid interception issues
                    login.execute_script("arguments[0].click();", next_button)
                else:
                    # print("Next button is disabled. Reached the last page.")
                    break

            except Exception as e:
                # # If no next button is found or any other exception occurs, exit the loop
                # print("End of pages or error encountered:", e)
                break

        # After clicking through all pages, locate and click the last accordion
        time.sleep(1)
        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(3)
        View_Detail_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(), 'View Details')]")
            )
        )
        View_Detail_button.click()

        time.sleep(3)

    # #####************************* Auto Invoice and Sharing ************************#######

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='View Invoice']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Send']")
            )
        ).click()
        print("Auto Invoice")
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
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Edit']"))
        ).click()
        
        time.sleep(2)
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        ).click()
        
        time.sleep(2)    
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='Naveen Consultation 1']"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        print("Added Sub Service to the Invoice")
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        ).click()
        
        item_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Choose Procedure/Item']"))
        )
        item_button.click()
        item_button.send_keys("item1234")
        
        time.sleep(3)
        price = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='mat-input-4'])[2]"))
        )
        price.clear()
        price.click()
        price.send_keys("1")
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        print("Added ADHOC item to the Invoice")
        
        time.sleep(3)
        update_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", update_button)
        update_button.click()
        
          
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
        
        time.sleep(3)
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Send']")
            )
        ).click()
        
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

        time.sleep(4)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Pay by Cash']"))
        ).click()

        pay_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Pay']"))
        )
        login.execute_script("arguments[0].click();", pay_button)

        yes_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Yes']"))
        )
        login.execute_script("arguments[0].click();", yes_button)
        
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='fa fa-arrow-left'])[1]")
        time.sleep(2)

        # login.find_element(By.XPATH, "(//span[@class='fa fa-arrow-left pointer-cursor'])[1]").click()

        # time.sleep(3)
        # while True:
        #     try:
        #         # Attempt to locate the "Next" button using the button's class
        #         next_button = WebDriverWait(login, 10).until(
        #             EC.presence_of_element_located(
        #                 (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
        #             )
        #         )

        #         # Check if the button is enabled (i.e., not disabled)
        #         if next_button.is_enabled():
        #             # print("Next button found and clickable.")
        #             # Click using JavaScript to avoid interception issues
        #             login.execute_script("arguments[0].click();", next_button)
        #         else:
        #             # print("Next button is disabled. Reached the last page.")
        #             break

        #     except Exception as e:
        #         # # If no next button is found or any other exception occurs, exit the loop
        #         # print("End of pages or error encountered:", e)
        #         break

        # # After clicking through all pages, locate and click the last accordion
        # time.sleep(1)
        # last_element_in_accordian = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        # )
        # last_element_in_accordian.click()

        # time.sleep(3)
        # View_Detail_button = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[contains(text(), 'View Details')]")
        #     )
        # )
        # View_Detail_button.click()

        

        # ********************** Manual Invoice and Sharing ***********************

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[normalize-space()='New Invoice'])[1]")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']")
            )
        ).click()

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Choose Procedure/Item']")
            )
        ).click()

        time.sleep(1)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@class='item-name'][normalize-space()='Naveen Consultation']",
                )
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//button[@class='cs-btn bt1 ml-0'][normalize-space()='Add']",
                )
            )
        ).click()

        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Update']")
            )
        ).click()

        time.sleep(5)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Send']")
            )
        ).click()
        print("Manual Invoice")

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
    
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Edit']"))
        ).click()
        
        time.sleep(2)
        
        add_service = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        )
        login.execute_script("arguments[0].click();", add_service)
        
        time.sleep(3)    
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='Naveen Consultation 1']"))
        ).click()
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        print("Added Sub Service to the Invoice")
        
        time.sleep(2)
        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='Add Procedure/Item']"))
        # ).click()
        login.execute_script("arguments[0].click();", add_service)
        item_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Choose Procedure/Item']"))
        )
        item_button.click()
        item_button.send_keys("item1234")
        
        time.sleep(3)
        price = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='mat-input-4'])[2]"))
        )
        price.clear()
        price.click()
        price.send_keys("102")
        
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Add']"))
        ).click()
        print("Added ADHOC item to the Invoice")
        
        time.sleep(3)
        update_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Update']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", update_button)
        update_button.click()
        
        
        
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
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Get Payment']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']")
            )
        ).click()

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Send']")
            )
        ).click()
        
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
        

        time.sleep(3)
    #     # print("Successfully send the Payment Link to the patient")

        login.find_element(By.XPATH, "//i[@class='fa fa-arrow-left']").click()

        # while True:
        #     try:
        #         # Attempt to locate the "Next" button using the button's class
        #         next_button = WebDriverWait(login, 10).until(
        #             EC.presence_of_element_located(
        #                 (By.XPATH, "//button[contains(@class, 'p-paginator-next')]")
        #             )
        #         )

        #         # Check if the button is enabled (i.e., not disabled)
        #         if next_button.is_enabled():
        #             # print("Next button found and clickable.")
        #             # Click using JavaScript to avoid interception issues
        #             login.execute_script("arguments[0].click();", next_button)
        #         else:
        #             # print("Next button is disabled. Reached the last page.")
        #             break

        #     except Exception as e:
        #         # # If no next button is found or any other exception occurs, exit the loop
        #         # print("End of pages or error encountered:", e)
        #         break

        # # After clicking through all pages, locate and click the last accordion
        # time.sleep(5)
        # last_element_in_accordian = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        # )
        # last_element_in_accordian.click()

        # time.sleep(3)
        # # print("Before clicking View Details button")
        # View_Detail_button = WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[contains(text(), 'View Details')]")
        #     )
        # )
        # View_Detail_button.click()

        # *************************** Reschedule **********************

        time.sleep(3)
        login.find_element(By.XPATH, "(//button[normalize-space()='Reschedule'])[1]").click()
        time.sleep(2)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='reschedule-date-picker']")
            )
        ).click()

        today_date = datetime.now()
        print(today_date.day)
        today_xpath_expression = "//span[@class='example-custom-date-class d-pad-15 ng-star-inserted'][normalize-space()='{}']".format(
            today_date.day
        )
        print(today_xpath_expression)
        tomorrow_date = today_date + timedelta(days=1)
        print(tomorrow_date.day)
#===============================================================
        # current_month = WebDriverWait(login, 10).until(
        # EC.presence_of_element_located(
        #     (By.XPATH, "//button[contains(@class, 'p-datepicker-month')]"))
        # )

        # current_year = WebDriverWait(login, 10).until(
        # EC.presence_of_element_located(
        #     (By.XPATH, "//button[contains(@class, 'p-datepicker-year')]"))
        # )

        # if current_month.text.lower() != tomorrow_date.strftime("%b").lower() or current_year.text.lower() != tomorrow_date.strftime("%Y").lower():

        #     login.find_element(By.XPATH, "//button[contains(@class, 'p-datepicker-next')]").click()
#===============================================================
        tomorrow_xpath_expression = "//span[@class='example-custom-date-class d-pad-15 ng-star-inserted'][normalize-space()='{}']".format(
            tomorrow_date.day
        )
        print(tomorrow_xpath_expression)

        Tomorrow_Date = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, tomorrow_xpath_expression))
        )
        Tomorrow_Date.click()
        print("Tomorrow Date:", Tomorrow_Date.text)

        wait = WebDriverWait(login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected= 'false']"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)

        reschedule_button = WebDriverWait(login, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='btn btn-primary reschedule-btn']")
            )
        )
        reschedule_button.click()

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
        # print("Reschedule Successfully")

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'Today')]")
            )
        ).click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Future']")
            )
        ).click()

        time.sleep(3)
        last_accordian = WebDriverWait(login, 15).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
                )
            )
        )
        last_accordian.click()

        # *******************Cancellation **********************

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Change Status']")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Cancel')]")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(),'No Show Up')]")
            )
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Ok']"))
        ).click()

        toast_message = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
        )
        message = toast_message.text
        print("Toast Message:", message)
        
        
        



    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

##############################################################################################################################################################


