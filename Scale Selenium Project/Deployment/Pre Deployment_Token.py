import time

from Framework.common_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_walkin_token(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(),'Tokens')]"))
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Token']"))
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

    service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
    element = login.find_element(By.XPATH, service_dropdown_xpath)
    login.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    # service_option_xpath = ("(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
    #                         "Consultation'])[2]")
    # WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
    # print("Select Service : Naveen Consultation")
    time.sleep(3)
    Today_Date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                            "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
    Today_Date.click()
    print("Today Date:", Today_Date.text)

    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//span[@id='pr_id_21_label']"))
    # ).click()
    # time.sleep(2)
    #
    # WebDriverWait(login, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='00:00 AM - 11:59 PM']"))
    # )

    print("Time Slot: 00:00 AM - 11:59 PM")

    # wait = WebDriverWait(login, 10)
    # time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
    # time_slot.click()
    # print("Time Slot:", time_slot.text)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Notes')]"))
    ).click()

    login.find_element(By.XPATH, "//textarea[@id='message']").send_keys("Note for the walkin Token")

    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    ).click()
    print("Note added for walkin token")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Upload File']"))
    ).click()

    time.sleep(4)
    pyautogui.write(r"C:\Users\Archana\PycharmProjects\SeleniumPython\test.png")
    pyautogui.press('enter')
    print("Successfully upload the file")

    time.sleep(6)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]"))
    ).click()

    print("Token confirm successfully")

    time.sleep(4)

    while True:
        try:
            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
            )

            next_button.click()

        except:
            break

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    View_Detail_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'View Details')]"))
    )
    View_Detail_button.click()

    time.sleep(3)
    more_actions_button = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='More Actions']"))
    )
    more_actions_button.click()
    # ****************************** Send Message ****************************
    time.sleep(4)
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Send Message']"))
    ).click()

    login.find_element(By.XPATH, " //textarea[@id='messageData']").send_keys("Send Message to the Patient")

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Click here to select the files']"))
    ).click()

    time.sleep(4)
    pyautogui.write(r"C:\Users\Archana\PycharmProjects\SeleniumPython\test.png")
    pyautogui.press('enter')

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'send')]"))
    ).click()

    print("Send Message Successfully")

    # ******************* Send Attachment ************************
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Send Attachments']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Click here to select the files']"))
    ).click()

    time.sleep(3)
    pyautogui.write(r"C:\Users\Archana\PycharmProjects\SeleniumPython\test.png")
    pyautogui.press('enter')

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
        login.find_element(By.XPATH, "//div[@class='add']").click()
        login.find_element(By.XPATH, "//input[@role='searchbox']").send_keys("Medicine")

        before_XPath = "//*[contains(@id, 'pr_id')]/tbody/tr"
        aftertd_XPath_1 = "/td[2]"
        aftertd_XPath_2 = "/td[3]"
        aftertd_XPath_3 = "/td[4]"
        aftertd_XPath_4 = "/td[5]"
        textarea_xpath = "/p-celleditor/textarea"
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

    dropdown_locator_xpath = "//mat-select[@aria-haspopup='listbox']"
    dropdown_element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, dropdown_locator_xpath)))

    dropdown_element.click()

    option_locator_xpath = "//div[normalize-space()='Naveen KP']"
    option_element = WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, option_locator_xpath)))

    option_element.click()

    login.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    time.sleep(5)
    print("prescription created successfully")

    login.find_element(By.XPATH, "//img[@alt='share']").click()

    login.find_element(By.XPATH, "//textarea[@placeholder='Enter message description']").send_keys(
        "prescription message")

    login.find_element(By.XPATH, "(//input[@class='mdc-checkbox__native-control'])[1]").click()
    login.find_element(By.XPATH, "//button[@type='button'][normalize-space()='Share']").click()
    print("Prescription Shared Successfully")

    # ************************* Case Creation and Sharing *********************

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Patient Record']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='+ Create Case']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Case Description']"))
    ).send_keys("test case for case")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder = 'Enter Chief Complaint']"))
    ).send_keys("Fever")

    element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
    login.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='History']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder = 'Enter History']"))
    ).send_keys("Viral fever")

    element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
    login.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Medication']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Medication']"))
    ).send_keys(" No medication")

    element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
    login.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Vital Signs']"))
    ).click()

    login.find_element(By.XPATH, "//input[@placeholder='Enter Pulse Rate , Max : 999']").send_keys("560")
    login.find_element(By.XPATH, "//input[@placeholder='Enter Respiration , Max : 90']").send_keys("62")
    login.find_element(By.XPATH, "//input[@placeholder='Enter Temperature in °F , Max : 200']").send_keys("123")
    login.find_element(By.XPATH, "//input[@placeholder='Enter Systolic , Max : 500']").send_keys("264")
    login.find_element(By.XPATH, "//input[@placeholder='Enter Diastolic , Max : 500']").send_keys("287")

    element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
    login.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Immunization History']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Immunization History']"))
    ).send_keys("No History of Immunization History")

    element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
    login.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Observations']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Observations']"))
    ).send_keys("Minor fever")

    element = login.find_element(By.XPATH, "//button[normalize-space()='Save']")
    login.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Diagnosis']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Diagnosis']"))
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
        EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Enter message description']"))
    ).send_keys("case sharing testing")

    login.find_element(By.XPATH, "//span[contains(text(),'Email')]").click()
    login.find_element(By.XPATH, "//span[contains(text(),'Whatsapp')]").click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Share')]"))
    ).click()

    print("Case file Shared successfully")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//i[@class='pi pi-arrow-left back-btn-arrow']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']"))
    ).click()

    while True:
        try:
            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
            )

            next_button.click()

        except:
            break

    time.sleep(3)
    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    # # ************************* Auto Invoice and Sharing ************************

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Invoice']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Get Payment']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Share Payment Link']"))
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
                    (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
            )

            next_button.click()

        except:

            break

    time.sleep(3)
    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    # ********************** Manual Invoice and Sharing ***********************

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='New Invoice']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add Service/Item']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Choose Service/Item']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='service']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='cs-btn bt1 ml-0'][normalize-space()='Add']"))
    ).click()

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
    ).click()

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Get Payment']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Share Payment Link']"))
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
                    (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
            )

            next_button.click()

        except:
            break

    time.sleep(3)
    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    time.sleep(3)
    print("Before clicking View Details button")
    View_Detail_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'View Details')]"))
    )
    View_Detail_button.click()

    # *************************** Reschedule **********************

    time.sleep(3)
    login.find_element(By.XPATH, "//button[contains(text(),'Reschedule')]").click()
    time.sleep(2)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='reschedule-date-picker']"))
    ).click()

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
        EC.visibility_of_element_located((By.XPATH,
                                          "//div[@class='col-12 col-sm-12 col-md-12 col-lg-12 mgn-up-20 mgn-bt-20 footerlinks no-padding reschedulebtn ng-star-inserted']//button[@class='btn btn-primary reschedule-btn']"))
    )
    reschedule_button.click()
    print("Reschedule Successfully")

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']"))
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
                    (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
            )

            next_button.click()

        except:
            break

    time.sleep(3)

    last_element_in_accordian = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
    )
    last_element_in_accordian.click()

    # *******************Cancellation **********************

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Change Status']"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Cancel')]"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'No Show Up')]"))
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Ok']"))
    ).click()
    time.sleep(5)
    print("Successfully Cancel Token")
