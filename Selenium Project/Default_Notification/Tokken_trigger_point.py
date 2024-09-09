import time

from Framework.common_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.severity(allure.severity_level.CRITICAL)
@allure.title(
    "Confirmation, Send_message, Send_Attachment, Prescription_Sharing, Case_Sharing, Auto and Manual Invoice, Reschedule, Cancellation"
)
@pytest.mark.parametrize("url", ["https://test.jaldee.com/business/"])
def test_walkin_token(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Tokens')]"))
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Token']"))
    )
    element.click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
        )
    ).send_keys("9207206005")
    time.sleep(2)
    login.implicitly_wait(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 1']"))
    ).click()

    time.sleep(3)
    wait = WebDriverWait(login, 10)
    Today_Date = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']",
            )
        )
    )
    Today_Date.click()
    print("Today Date:", Today_Date.text)

    print("Time Slot: 00:00 AM - 11:59 PM")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
    ).click()

    print("Token confirm successfully")

    time.sleep(4)

    while True:
        try:
            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                    )
                )
            )

            next_button.click()

        except:
            break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
            )
        )
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
    # ****************************** Send Message ****************************
    time.sleep(4)
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[normalize-space()='Send Message']")
        )
    ).click()

    time.sleep(2)
    login.find_element(By.XPATH, " //textarea[@id='messageData']").send_keys(
        "Send Message to the Patient"
    )

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//label[normalize-space()='Click here to select the files']")
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

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'send')]"))
    ).click()

    print("Send Message Successfully")

    # ******************* Send Attachment ************************
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[normalize-space()='Send Attachments']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//label[normalize-space()='Click here to select the files']")
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
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'send')]"))
    ).click()

    print("Attachment Send Successfully")

    # ********************* Create the Prescription and Sharing *************************

    time.sleep(5)
    WebDriverWait(login, 10)
    login.find_element(By.XPATH, "//span[normalize-space()='Prescriptions']").click()

    for i in range(5):
        login.find_element(
            By.XPATH, "//button[normalize-space()='+ Add Medicine']"
        ).click()
        login.find_element(By.XPATH, "//input[@role='searchbox']").send_keys("Medicine")

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

    time.sleep(1)
    login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    time.sleep(5)
    print("prescription created successfully")

    login.find_element(By.XPATH, "//img[@alt='share']").click()
    time.sleep(2)
    login.find_element(
        By.XPATH, "//textarea[@placeholder='Enter message description']"
    ).send_keys("prescription message")

    login.find_element(
        By.XPATH, "(//input[@class='mdc-checkbox__native-control'])[1]"
    ).click()
    login.find_element(
        By.XPATH, "//button[@type='button'][normalize-space()='Share']"
    ).click()
    print("Prescription Shared Successfully")

    # ************************* Case Creation and Sharing *********************

    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Patient Record']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='+ Create Case']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter Case Description']")
        )
    ).send_keys("test case for case")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Enter Chief Complaint']")
        )
    ).send_keys("Fever")

    element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
    login.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='History']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder = 'Enter History']")
        )
    ).send_keys("Viral fever")

    element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
    login.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Medication']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter Medication']")
        )
    ).send_keys("No medication")

    element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
    login.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    # toast_message = WebDriverWait(login, 10).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    # )
    # message = toast_message.text
    # print("Toast Message:", message)

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Immunization History']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter Immunization History']")
        )
    ).send_keys("No History of Immunization History")

    element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
    login.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Observations']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter Observations']")
        )
    ).send_keys("Minor fever")

    element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
    login.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Diagnosis']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter Diagnosis']")
        )
    ).send_keys("High temperature")

    element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
    login.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Share')]"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//textarea[@placeholder='Enter message description']")
        )
    ).send_keys("case sharing testing")

    login.find_element(By.XPATH, "//span[contains(text(),'Email')]").click()
    login.find_element(By.XPATH, "//span[contains(text(),'Whatsapp')]").click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Share')]"))
    ).click()

    print("Case file Shared successfully")

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//i[@class='pi pi-arrow-left back-btn-arrow']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
        )
    ).click()

    while True:
        try:
            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                    )
                )
            )

            next_button.click()

        except:
            break

    time.sleep(3)
    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
            )
        )
    )
    last_element_in_accordian.click()

    # # ************************* Auto Invoice and Sharing ************************

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
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
    ).click()

    time.sleep(5)
    print("Successfully send the Payment Link to the patient")

    login.find_element(By.XPATH, "//div/span/span[contains(text(),'Tokens')]").click()

    while True:
        try:
            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                    )
                )
            )

            next_button.click()

        except:

            break

    time.sleep(3)
    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
            )
        )
    )
    last_element_in_accordian.click()

    # ********************** Manual Invoice and Sharing ***********************

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='New Invoice']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Add Service/Item']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Choose Service/Item']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Consultation']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='cs-btn bt1 ml-0'][normalize-space()='Add']")
        )
    ).click()

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
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
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Send']"))
    ).click()

    time.sleep(5)
    print("Successfully send the Payment Link to the patient")

    login.find_element(By.XPATH, "//i[@class='fa fa-arrow-left']").click()

    while True:
        try:
            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                    )
                )
            )

            next_button.click()

        except:
            break

    time.sleep(3)
    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
            )
        )
    )
    last_element_in_accordian.click()

    time.sleep(3)
    print("Before clicking View Details button")
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

    # current_month = WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "//button[contains(@class, 'p-datepicker-month')]"))
    # )

    # current_year = WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "//button[contains(@class, 'p-datepicker-year')]"))
    # )

    # if current_month.text.lower() != tomorrow_date.strftime("%b").lower() or current_year.text.lower() != tomorrow_date.strftime("%Y").lower():

    #     login.find_element(By.XPATH, "//button[contains(@class, 'p-datepicker-next')]").click()

    tomorrow_xpath_expression = "//span[@class='example-custom-date-class d-pad-15 ng-star-inserted'][normalize-space()='{}']".format(
        tomorrow_date.day
    )
    print(tomorrow_xpath_expression)

    Tomorrow_Date = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, tomorrow_xpath_expression))
    )
    time.sleep(3)
    Tomorrow_Date.click()
    print("Tomorrow Date:", Tomorrow_Date.text)
    #
    # wait = WebDriverWait(login, 10)
    # time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected= 'false']")))
    # time_slot.click()
    # print("Time Slot:", time_slot.text)

    print("Time slot = 00:00AM - 11:59 PM")
    reschedule_button = WebDriverWait(login, 30).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[@class='btn btn-primary reschedule-btn']")
        )
    )
    reschedule_button.click()
    print("Reschedule Successfully")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Today')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Future']"))
    ).click()

    while True:
        try:
            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                    )
                )
            )

            next_button.click()

        except:
            break

    time.sleep(3)

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
            )
        )
    )
    last_element_in_accordian.click()

    # *******************Cancellation **********************

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Change Status']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Cancel')]"))
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
    time.sleep(5)
    print("Successfully Cancel Token")


####################################################################################################################
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Reconfirmation")
@pytest.mark.parametrize("url", ["https://test.jaldee.com/business/"])
def test_patient_Reconfirmation(login):

    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Tokens')]"))
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Token']"))
    )
    element.click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
        )
    ).send_keys("9207206005")
    time.sleep(2)
    login.implicitly_wait(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 1']"))
    ).click()

    time.sleep(3)
    wait = WebDriverWait(login, 10)
    Today_Date = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']",
            )
        )
    )
    Today_Date.click()
    print("Today Date:", Today_Date.text)

    print("Time Slot: 00:00 AM - 11:59 PM")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
    ).click()

    print("Token confirm successfully")

    time.sleep(4)

    while True:
        try:
            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                    )
                )
            )

            next_button.click()

        except:
            break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
            )
        )
    )
    last_element_in_accordian.click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Change Status']")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Cancel')]"))
    ).click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'No Show Up')]")
        )
    ).click()

    login.find_element(By.XPATH, "//span[@class='mdc-button__label']").click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@type='checkbox'])[4]"))
    ).click()

    while True:
        try:

            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                    )
                )
            )

            next_button.click()

        except:

            break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
            )
        )
    )
    last_element_in_accordian.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Change Status']")
        )
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='status status-box']"))
    ).click()

    toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_message.text
    print("Toast Message:", message)


###################################################################################################################################
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Started")
@pytest.mark.parametrize("url", ["https://test.jaldee.com/business/"])
def test_patient_started(login):

    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Tokens')]"))
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Token']"))
    )
    element.click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
        )
    ).send_keys("9207206005")
    time.sleep(2)
    login.implicitly_wait(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 1']"))
    ).click()

    time.sleep(3)
    wait = WebDriverWait(login, 10)
    Today_Date = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']",
            )
        )
    )
    Today_Date.click()
    print("Today Date:", Today_Date.text)

    print("Time Slot: 00:00 AM - 11:59 PM")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
    ).click()

    print("Token confirm successfully")

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

    while True:
        try:

            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                    )
                )
            )

            next_button.click()

        except:

            break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
                )
            )
        )
        last_element_in_accordian.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Change Status']")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Start')]"))
    ).click()

    toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_message.text
    print("Toast Message:", message)


####################################################################################################################################
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Reminder Message")
@pytest.mark.parametrize("url", ["https://test.jaldee.com/business/"])
def test_reminder(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Tokens')]"))
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Token']"))
    )
    element.click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
        )
    ).send_keys("9207206005")
    time.sleep(2)
    login.implicitly_wait(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 1']"))
    ).click()

    time.sleep(3)
    wait = WebDriverWait(login, 10)
    Today_Date = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']",
            )
        )
    )
    Today_Date.click()
    print("Today Date:", Today_Date.text)

    print("Time Slot: 00:00 AM - 11:59 PM")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
    ).click()

    print("Token confirm successfully")

    time.sleep(4)

    while True:
        try:
            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                    )
                )
            )

            next_button.click()

        except:
            break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
            )
        )
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

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Share Info']")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='mdc-button__label']"))
    ).click()


####################################################################################################################
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Completed Messages")
@pytest.mark.parametrize("url", ["https://test.jaldee.com/business/"])
def test_completed_message(login):

    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Tokens')]"))
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Token']"))
    )
    element.click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
        )
    ).send_keys("9207206005")
    time.sleep(2)
    login.implicitly_wait(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Id : 1']"))
    ).click()

    time.sleep(3)
    wait = WebDriverWait(login, 10)
    Today_Date = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']",
            )
        )
    )
    Today_Date.click()
    print("Today Date:", Today_Date.text)

    print("Time Slot: 00:00 AM - 11:59 PM")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
    ).click()

    print("Token confirm successfully")

    time.sleep(4)

    while True:
        try:
            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']",
                    )
                )
            )

            next_button.click()

        except:
            break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]",
            )
        )
    )
    last_element_in_accordian.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Change Status']")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Complete')]"))
    ).click()

    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
    ).click()

    toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_message.text
    print("Toast Message:", message)


#########################################################################################################################
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Confirmation,Reschedule,Send Message, Send attachment")
@pytest.mark.parametrize("url", ["https://test.jaldee.com/53b6eu1/"])
def test_confirmation(con_login):
    time.sleep(3)
    book_now_button = WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Book Now']")
        )
    )
    con_login.execute_script("arguments[0].scrollIntoView();", book_now_button)

    # Wait for the element to be clickable
    clickable_book_now_button = WebDriverWait(con_login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Book Now']"))
    )

    # Attempt to click the element
    try:
        clickable_book_now_button.click()
    except:
        # If click is intercepted, click using JavaScript
        con_login.execute_script("arguments[0].click();", clickable_book_now_button)

    time.sleep(2)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class,'serviceName ng-star-inserted')]")
        )
    ).click()

    time.sleep(2)
    Today_Date = WebDriverWait(con_login, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[@aria-pressed='true'] [@aria-current='date']",
            )
        )
    )

    Today_Date.click()

    print("Today Date:", Today_Date.text)

    wait = WebDriverWait(con_login, 10)
    time_slot = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//mat-chip[@aria-selected='true']"))
    )
    time_slot.click()
    print("Time Slot:", time_slot.text)

    con_login.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
    ).send_keys("9207206005")

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='continue ng-star-inserted']")
        )
    ).click()

    time.sleep(2)
    otp_digits = "5555"

    # Wait for the OTP input fields to be present
    otp_inputs = WebDriverWait(con_login, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//input[contains(@id, 'otp_')]")
        )
    )

    for i, otp_input in enumerate(otp_inputs):
        otp_input.send_keys(otp_digits[i])

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='continue ng-star-inserted']")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
    ).click()

    time.sleep(3)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Ok')]"))
    ).click()

    time.sleep(3)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'My Bookings')]")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span//mat-icon[@class='mat-icon notranslate material-icons mat-ligature-font mat-icon-no-color']",
            )
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Reschedule']")
        )
    ).click()

    today_date = datetime.now()
    print(today_date.day)
    today_xpath_expression = "//div[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-today'][normalize-space()='{}']".format(
        today_date.day
    )
    print(today_xpath_expression)
    tomorrow_date = today_date + timedelta(days=1)
    print(tomorrow_date.day)

    time.sleep(3)
    tomorrow_xpath_expression = "//div[@class='mat-calendar-body-cell-content mat-focus-indicator'][normalize-space()='{}']".format(
        tomorrow_date.day
    )
    print(tomorrow_xpath_expression)

    Tomorrow_Date = WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, tomorrow_xpath_expression))
    )
    Tomorrow_Date.click()

    print("Tomorrow Date:", Tomorrow_Date.text)

    wait = WebDriverWait(con_login, 10)
    time_slot = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//mat-chip[@class='mat-chip mat-focus-indicator text-center mat-primary mat-standard-chip mat-chip-selected ng-star-inserted']",
            )
        )
    )
    time_slot.click()
    print("Time Slot:", time_slot.text)

    time.sleep(2)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Next']"))
    ).click()

    time.sleep(2)

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Reschedule']")
        )
    ).click()

    time.sleep(3)

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Ok']"))
    ).click()

    print("Appointment Rescheduled successfully")

    time.sleep(2)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='My Bookings']")
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span//mat-icon[@class='mat-icon notranslate material-icons mat-ligature-font mat-icon-no-color']",
            )
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Send Message']")
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@id='message']"))
    ).send_keys(" Message to the provider ")

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//button[@type='button']//i[@class='material-icons'][normalize-space()='attach_file']",
            )
        )
    ).click()

    time.sleep(8)
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
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Send']")
        )
    ).click()

    time.sleep(2)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Send Attachments']")
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Click here to select the files']")
        )
    ).click()

    time.sleep(8)
    # Get the current working directory
    current_working_directory = os.getcwd()

    # Construct the absolute path
    absolute_path = os.path.abspath(
        os.path.join(current_working_directory, r"Extras\test.png")
    )
    pyautogui.write(absolute_path)
    pyautogui.press("enter")
    print("Successfully upload the file")

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='send']"))
    ).click()

    time.sleep(2)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//mat-select[@role='combobox']"))
    ).click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Upcoming Bookings')]")
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span//mat-icon[@class='mat-icon notranslate material-icons mat-ligature-font mat-icon-no-color']",
            )
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Cancel']"))
    ).click()

    con_login.find_element(
        By.XPATH, "//mat-chip[normalize-space()='Change of Plans']"
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Confirm']")
        )
    ).click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-arrow-left']"))
    ).click()

    time.sleep(3)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[@alt='Home']"))
    ).click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-commenting-o']"))
    ).click()

    time.sleep(1)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@id='message']"))
    ).send_keys("Message to provider")

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted']"))
    ).click()

    time.sleep(3)
