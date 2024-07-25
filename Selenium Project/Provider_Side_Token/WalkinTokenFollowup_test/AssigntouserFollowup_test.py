
from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.common import TimeoutException


@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_assignto_user_followup(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
            )
        )
    ).click()
    time.sleep(5)
    
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Token']"))
    ).click()
    time.sleep(5)
    lucenesearch = login.find_element(
        By.XPATH, "//input[@placeholder='Enter name or phone or id']"
    )
    lucenesearch.send_keys("5550004454")
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Id : 100']")
        )
    ).click()
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Select Location']")
        )
    ).click()
    dropdownelement = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel='place']"))
    )
    dropdownelement.click()
    time.sleep(5)
    droplocation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[@class='ng-star-inserted'][normalize-space()='Ashok Nagar']",
            )
        )
    )
    droplocation.click()
    print("Select Location:", droplocation.text)
    userelement = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@class='mt-2 col-lg-8 col-xxl-6'])[2]")
        )
    )
    userelement.click()
    time.sleep(3)
    dropgeneralservice = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='General Services']")
        )
    )
    dropgeneralservice.click()
    print("Select User:", dropgeneralservice.text)
    assignto = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//p-dropdown[@optionlabel='fullName']//div[@class='text-left p-dropdown p-component']",
            )
        )
    )
    assignto.click()
    time.sleep(3)
    assigntouser = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Miguel B']"))
    )
    assigntouser.click()
    print("Assignto:", assigntouser.text)
    consultation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//p-dropdown[@optionlabel='name']//div[@class='text-left p-dropdown p-component']",
            )
        )
    )
    consultation.click()
    time.sleep(3)
    dropconsultation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@aria-label='Consultation']"))
    )
    dropconsultation.click()
    print("Select service:", dropconsultation.text)
    time.sleep(3)
    today_xpath = (
        "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected "
        "mat-calendar-body-today']"
    )
    today_element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, today_xpath))
    )
    today_element.click()
    print("Today's Date:", today_element.text)
    queueelement = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@class='col-lg-12 col-xxl-12 p-2']//div[@class='p-inputgroup']",
            )
        )
    )
    queueelement.click()
    time.sleep(3)
    dropqueue = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//li[@class='p-ripple p-element p-dropdown-item p-highlight']["
                "@id='p-highlighted-option']",
            )
        )
    )
    dropqueue.click()
    print("Selected Queue", dropqueue.text)
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//label[normalize-space()='Please upload Notes/Files related to "
                "your service']",
            )
        )
    )
    # login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    login.execute_script("arguments[0].scrollIntoView();", element)
    notes = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='chip-group']//div[1]//a[1]")
        )
    )
    notes.click()
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//textarea[@placeholder='Add Note']")
        )
    ).send_keys("Hai Welcome")
    submitnotebutton = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    )
    submitnotebutton.click()
    time.sleep(3)
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    noteaccordions = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//label[normalize-space()='Notes Added']")
        )
    )
    noteaccordions.click()
    login.execute_script("arguments[0].scrollIntoView();", noteaccordions)
    time.sleep(5)
    added_notes = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='customerNoteDetails mt-2']")
        )
    )
    print("Input Added Notes", added_notes.text)
    noteaccordions.click()
    time.sleep(3)
    uploadfile = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Upload File']")
        )
    )
    uploadfile.click()
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
    uploadfileaccordion = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[contains(text(),'Files selected')]")
        )
    )
    uploadfileaccordion.click()
    print("Uploaded File Successfully")
    time.sleep(3)
    confirmed = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Confirm']")
        )
    )
    confirmed.click()
    try:
        snack_bar = WebDriverWait(login, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
    except TimeoutException:
        try:
            snackbarerror = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            print("Snackbar Message : ", snackbarerror.text)
            cancelbutton = WebDriverWait(login, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Cancel']")
                )
            )
            cancelbutton.click()
        except TimeoutException:
            cancelbutton = WebDriverWait(login, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Cancel']")
                )
            )
            cancelbutton.click()
            print("Cancelled Successfully")
        time.sleep(1)
    while True:
        try:
            print("Before in the loop")
            time.sleep(3)
            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//angledoublerighticon[@class='p-element p-icon-wrapper "
                        "ng-star-inserted']",
                    )
                )
            )
            next_button.click()
        except:
            print("EC Caught:Next button not found or clicked.")
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
    login.execute_script(
        "arguments[0].scrollIntoView(true);", last_element_in_accordian
    )
    time.sleep(5)
    print("Accordion expanded")
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")
        )
    ).click()
    time.sleep(3)
    print("ViewDetails Button Clicked") 
     # # **** FollowUp *****
     
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Follow Up']")
        )
    ).click()
    time.sleep(3)
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    xpath_tomorrow = "//span[@class='mat-calendar-body-cell-content mat-focus-indicator'][normalize-space()='{}']".format(
        tomorrow.day)
    date_tomorrow = WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath_tomorrow))
    )
    print("Tomorrow Date:", date_tomorrow)
    date_tomorrow.click()
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Confirm']")
        )
    ).click()
    snack_bar = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    )
    print("Snackbar Message :", snack_bar.text)
    time.sleep(3)

@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_assignto_user_followup_futuredays(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
            )
        )
    ).click()
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Token']"))
    ).click()
    time.sleep(5)
    lucenesearch = login.find_element(
        By.XPATH, "//input[@placeholder='Enter name or phone or id']"
    )
    lucenesearch.send_keys("5550004454")
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Id : 100']")
        )
    ).click()
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Select Location']")
        )
    ).click()
    dropdownelement = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel='place']"))
    )
    dropdownelement.click()
    time.sleep(5)
    droplocation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[@class='ng-star-inserted'][normalize-space()='Ashok Nagar']",
            )
        )
    )
    droplocation.click()
    print("Select Location:", droplocation.text)
    userelement = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@class='mt-2 col-lg-8 col-xxl-6'])[2]")
        )
    )
    userelement.click()
    time.sleep(3)
    dropgeneralservice = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='General Services']")
        )
    )
    dropgeneralservice.click()
    print("Select User:", dropgeneralservice.text)
    assignto = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//p-dropdown[@optionlabel='fullName']//div[@class='text-left p-dropdown p-component']",
            )
        )
    )
    assignto.click()
    time.sleep(3)
    assigntouser = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Miguel B']"))
    )
    assigntouser.click()
    print("Assignto:", assigntouser.text)
    consultation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//p-dropdown[@optionlabel='name']//div[@class='text-left p-dropdown p-component']",
            )
        )
    )
    consultation.click()
    time.sleep(3)
    dropconsultation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@aria-label='Consultation']"))
    )
    dropconsultation.click()
    print("Select service:", dropconsultation.text)
    time.sleep(3)
    today_xpath = (
        "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected "
        "mat-calendar-body-today']"
    )
    today_element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, today_xpath))
    )
    today_element.click()
    print("Today's Date:", today_element.text)
    queueelement = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@class='col-lg-12 col-xxl-12 p-2']//div[@class='p-inputgroup']",
            )
        )
    )
    queueelement.click()
    time.sleep(3)
    dropqueue = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//li[@class='p-ripple p-element p-dropdown-item p-highlight']["
                "@id='p-highlighted-option']",
            )
        )
    )
    dropqueue.click()
    print("Selected Queue", dropqueue.text)
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//label[normalize-space()='Please upload Notes/Files related to "
                "your service']",
            )
        )
    )
    # login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    login.execute_script("arguments[0].scrollIntoView();", element)
    notes = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='chip-group']//div[1]//a[1]")
        )
    )
    notes.click()
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//textarea[@placeholder='Add Note']")
        )
    ).send_keys("Hai Welcome")
    submitnotebutton = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    )
    submitnotebutton.click()
    time.sleep(3)
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    noteaccordions = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//label[normalize-space()='Notes Added']")
        )
    )
    noteaccordions.click()
    login.execute_script("arguments[0].scrollIntoView();", noteaccordions)
    time.sleep(5)
    added_notes = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='customerNoteDetails mt-2']")
        )
    )
    print("Input Added Notes", added_notes.text)
    noteaccordions.click()
    time.sleep(3)
    uploadfile = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Upload File']")
        )
    )
    uploadfile.click()
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
    uploadfileaccordion = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[contains(text(),'Files selected')]")
        )
    )
    uploadfileaccordion.click()
    print("Uploaded File Successfully")
    time.sleep(3)
    confirmed = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Confirm']")
        )
    )
    confirmed.click()
    try:
        snack_bar = WebDriverWait(login, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
    except TimeoutException:
        try:
            snackbarerror = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            print("Snackbar Message : ", snackbarerror.text)
            cancelbutton = WebDriverWait(login, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Cancel']")
                )
            )
            cancelbutton.click()
        except TimeoutException:
            cancelbutton = WebDriverWait(login, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Cancel']")
                )
            )
            cancelbutton.click()
            print("Cancelled Successfully")
        time.sleep(1)
    while True:
        try:
            print("Before in the loop")
            time.sleep(3)
            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//angledoublerighticon[@class='p-element p-icon-wrapper "
                        "ng-star-inserted']",
                    )
                )
            )
            next_button.click()
        except:
            print("EC Caught:Next button not found or clicked.")
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
    login.execute_script(
        "arguments[0].scrollIntoView(true);", last_element_in_accordian
    )
    time.sleep(5)
    print("Accordion expanded")
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")
        )
    ).click()
    time.sleep(3)
    print("ViewDetails Button Clicked") 
     # # **** FollowUp *****
     
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Follow Up']")
        )
    ).click()
    time.sleep(3)
    calendar = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Choose month and year']"))
    )
    login.execute_script("arguments[0].scrollIntoView(true);", calendar)
    calendar.click()
    [year,month,day] = add_days(180)
    print(year)
    print(month)
    print(day)
    year_xpath = f"//span[normalize-space()='{year}']"
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, year_xpath))
    ).click()
    print(year_xpath)
    time.sleep(2)
    month_xpath = f"//span[normalize-space()='{month.upper()}']"
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, month_xpath))
    ).click()
    print(month_xpath)
    time.sleep(2)
    day_xpath = (
        f"//span[normalize-space()='{int(day)}' and not(contains(@class,'p-disabled'))]"
    )
    print(day_xpath)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, day_xpath))
    ).click()
    
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Confirm']")
        )
    ).click()
    snack_bar = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    )
    print("Snackbar Message :", snack_bar.text)
    time.sleep(3)

@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_assignto_user_followup_sameday(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
            )
        )
    ).click()
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Token']"))
    ).click()
    time.sleep(5)
    lucenesearch = login.find_element(
        By.XPATH, "//input[@placeholder='Enter name or phone or id']"
    )
    lucenesearch.send_keys("5550004454")
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Id : 100']")
        )
    ).click()
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Select Location']")
        )
    ).click()
    dropdownelement = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel='place']"))
    )
    dropdownelement.click()
    time.sleep(5)
    droplocation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[@class='ng-star-inserted'][normalize-space()='Ashok Nagar']",
            )
        )
    )
    droplocation.click()
    print("Select Location:", droplocation.text)
    userelement = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@class='mt-2 col-lg-8 col-xxl-6'])[2]")
        )
    )
    userelement.click()
    time.sleep(3)
    dropgeneralservice = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='General Services']")
        )
    )
    dropgeneralservice.click()
    print("Select User:", dropgeneralservice.text)
    assignto = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//p-dropdown[@optionlabel='fullName']//div[@class='text-left p-dropdown p-component']",
            )
        )
    )
    assignto.click()
    time.sleep(3)
    assigntouser = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Miguel B']"))
    )
    assigntouser.click()
    print("Assignto:", assigntouser.text)
    consultation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//p-dropdown[@optionlabel='name']//div[@class='text-left p-dropdown p-component']",
            )
        )
    )
    consultation.click()
    time.sleep(3)
    dropconsultation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@aria-label='Consultation']"))
    )
    dropconsultation.click()
    print("Select service:", dropconsultation.text)
    time.sleep(3)
    today_xpath = (
        "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected "
        "mat-calendar-body-today']"
    )
    today_element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, today_xpath))
    )
    today_element.click()
    print("Today's Date:", today_element.text)
    queueelement = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@class='col-lg-12 col-xxl-12 p-2']//div[@class='p-inputgroup']",
            )
        )
    )
    queueelement.click()
    time.sleep(3)
    dropqueue = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//li[@class='p-ripple p-element p-dropdown-item p-highlight']["
                "@id='p-highlighted-option']",
            )
        )
    )
    dropqueue.click()
    print("Selected Queue", dropqueue.text)
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//label[normalize-space()='Please upload Notes/Files related to "
                "your service']",
            )
        )
    )
    # login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    login.execute_script("arguments[0].scrollIntoView();", element)
    notes = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='chip-group']//div[1]//a[1]")
        )
    )
    notes.click()
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//textarea[@placeholder='Add Note']")
        )
    ).send_keys("Hai Welcome")
    submitnotebutton = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    )
    submitnotebutton.click()
    time.sleep(3)
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    noteaccordions = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//label[normalize-space()='Notes Added']")
        )
    )
    noteaccordions.click()
    login.execute_script("arguments[0].scrollIntoView();", noteaccordions)
    time.sleep(5)
    added_notes = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='customerNoteDetails mt-2']")
        )
    )
    print("Input Added Notes", added_notes.text)
    noteaccordions.click()
    time.sleep(3)
    uploadfile = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Upload File']")
        )
    )
    uploadfile.click()
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
    uploadfileaccordion = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[contains(text(),'Files selected')]")
        )
    )
    uploadfileaccordion.click()
    print("Uploaded File Successfully")
    time.sleep(3)
    confirmed = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Confirm']")
        )
    )
    confirmed.click()
    try:
        snack_bar = WebDriverWait(login, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
    except TimeoutException:
        try:
            snackbarerror = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            print("Snackbar Message : ", snackbarerror.text)
            cancelbutton = WebDriverWait(login, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Cancel']")
                )
            )
            cancelbutton.click()
        except TimeoutException:
            cancelbutton = WebDriverWait(login, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Cancel']")
                )
            )
            cancelbutton.click()
            print("Cancelled Successfully")
        time.sleep(1)
    while True:
        try:
            print("Before in the loop")
            time.sleep(3)
            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//angledoublerighticon[@class='p-element p-icon-wrapper "
                        "ng-star-inserted']",
                    )
                )
            )
            next_button.click()
        except:
            print("EC Caught:Next button not found or clicked.")
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
    login.execute_script(
        "arguments[0].scrollIntoView(true);", last_element_in_accordian
    )
    time.sleep(5)
    print("Accordion expanded")
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")
        )
    ).click()
    time.sleep(3)
    print("ViewDetails Button Clicked") 
     # # **** FollowUp *****
     
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Follow Up']")
        )
    ).click()
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Confirm']")
        )
    ).click()
    snack_bar = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    )
    print("Snackbar Message :", snack_bar.text)
    time.sleep(3)

@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_assignto_user_followup_previousday(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
            )
        )
    ).click()
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Token']"))
    ).click()
    time.sleep(5)
    lucenesearch = login.find_element(
        By.XPATH, "//input[@placeholder='Enter name or phone or id']"
    )
    lucenesearch.send_keys("5550004454")
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Id : 100']")
        )
    ).click()
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Select Location']")
        )
    ).click()
    dropdownelement = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel='place']"))
    )
    dropdownelement.click()
    time.sleep(5)
    droplocation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[@class='ng-star-inserted'][normalize-space()='Ashok Nagar']",
            )
        )
    )
    droplocation.click()
    print("Select Location:", droplocation.text)
    userelement = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@class='mt-2 col-lg-8 col-xxl-6'])[2]")
        )
    )
    userelement.click()
    time.sleep(3)
    dropgeneralservice = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='General Services']")
        )
    )
    dropgeneralservice.click()
    print("Select User:", dropgeneralservice.text)
    assignto = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//p-dropdown[@optionlabel='fullName']//div[@class='text-left p-dropdown p-component']",
            )
        )
    )
    assignto.click()
    time.sleep(3)
    assigntouser = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Miguel B']"))
    )
    assigntouser.click()
    print("Assignto:", assigntouser.text)
    consultation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//p-dropdown[@optionlabel='name']//div[@class='text-left p-dropdown p-component']",
            )
        )
    )
    consultation.click()
    time.sleep(3)
    dropconsultation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@aria-label='Consultation']"))
    )
    dropconsultation.click()
    print("Select service:", dropconsultation.text)
    time.sleep(3)
    today_xpath = (
        "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected "
        "mat-calendar-body-today']"
    )
    today_element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, today_xpath))
    )
    today_element.click()
    print("Today's Date:", today_element.text)
    queueelement = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@class='col-lg-12 col-xxl-12 p-2']//div[@class='p-inputgroup']",
            )
        )
    )
    queueelement.click()
    time.sleep(3)
    dropqueue = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//li[@class='p-ripple p-element p-dropdown-item p-highlight']["
                "@id='p-highlighted-option']",
            )
        )
    )
    dropqueue.click()
    print("Selected Queue", dropqueue.text)
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//label[normalize-space()='Please upload Notes/Files related to "
                "your service']",
            )
        )
    )
    # login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    login.execute_script("arguments[0].scrollIntoView();", element)
    notes = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='chip-group']//div[1]//a[1]")
        )
    )
    notes.click()
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//textarea[@placeholder='Add Note']")
        )
    ).send_keys("Hai Welcome")
    submitnotebutton = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    )
    submitnotebutton.click()
    time.sleep(3)
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    noteaccordions = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//label[normalize-space()='Notes Added']")
        )
    )
    noteaccordions.click()
    login.execute_script("arguments[0].scrollIntoView();", noteaccordions)
    time.sleep(5)
    added_notes = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='customerNoteDetails mt-2']")
        )
    )
    print("Input Added Notes", added_notes.text)
    noteaccordions.click()
    time.sleep(3)
    uploadfile = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Upload File']")
        )
    )
    uploadfile.click()
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
    uploadfileaccordion = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[contains(text(),'Files selected')]")
        )
    )
    uploadfileaccordion.click()
    print("Uploaded File Successfully")
    time.sleep(3)
    confirmed = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Confirm']")
        )
    )
    confirmed.click()
    try:
        snack_bar = WebDriverWait(login, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
    except TimeoutException:
        try:
            snackbarerror = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            print("Snackbar Message : ", snackbarerror.text)
            cancelbutton = WebDriverWait(login, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Cancel']")
                )
            )
            cancelbutton.click()
        except TimeoutException:
            cancelbutton = WebDriverWait(login, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Cancel']")
                )
            )
            cancelbutton.click()
            print("Cancelled Successfully")
        time.sleep(1)
    while True:
        try:
            print("Before in the loop")
            time.sleep(3)
            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//angledoublerighticon[@class='p-element p-icon-wrapper "
                        "ng-star-inserted']",
                    )
                )
            )
            next_button.click()
        except:
            print("EC Caught:Next button not found or clicked.")
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
    login.execute_script(
        "arguments[0].scrollIntoView(true);", last_element_in_accordian
    )
    time.sleep(5)
    print("Accordion expanded")
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")
        )
    ).click()
    time.sleep(3)
    print("ViewDetails Button Clicked") 
     # # **** FollowUp *****
     
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Follow Up']")
        )
    ).click()
    time.sleep(3)
    today = datetime.now().date()
    previous_day = today - timedelta(days=1)
    xpath_previous_day = "//span[@class='mat-calendar-body-cell-content mat-focus-indicator'][normalize-space()='{}']".format(
        previous_day.day)
    date_previous_day = WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath_previous_day))
    )
    print("Previous Date:", date_previous_day)
    date_previous_day.click()
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Confirm']")
        )
    ).click()
    snack_bar = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    )
    print("Snackbar Message :", snack_bar.text)
    time.sleep(3)


@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_assignto_user_followup_nextmonth(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
            )
        )
    ).click()
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Token']"))
    ).click()
    time.sleep(5)
    lucenesearch = login.find_element(
        By.XPATH, "//input[@placeholder='Enter name or phone or id']"
    )
    lucenesearch.send_keys("5550004454")
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Id : 100']")
        )
    ).click()
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Select Location']")
        )
    ).click()
    dropdownelement = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel='place']"))
    )
    dropdownelement.click()
    time.sleep(5)
    droplocation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//span[@class='ng-star-inserted'][normalize-space()='Ashok Nagar']",
            )
        )
    )
    droplocation.click()
    print("Select Location:", droplocation.text)
    userelement = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@class='mt-2 col-lg-8 col-xxl-6'])[2]")
        )
    )
    userelement.click()
    time.sleep(3)
    dropgeneralservice = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='General Services']")
        )
    )
    dropgeneralservice.click()
    print("Select User:", dropgeneralservice.text)
    assignto = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//p-dropdown[@optionlabel='fullName']//div[@class='text-left p-dropdown p-component']",
            )
        )
    )
    assignto.click()
    time.sleep(3)
    assigntouser = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Miguel B']"))
    )
    assigntouser.click()
    print("Assignto:", assigntouser.text)
    consultation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//p-dropdown[@optionlabel='name']//div[@class='text-left p-dropdown p-component']",
            )
        )
    )
    consultation.click()
    time.sleep(3)
    dropconsultation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@aria-label='Consultation']"))
    )
    dropconsultation.click()
    print("Select service:", dropconsultation.text)
    time.sleep(3)
    today_xpath = (
        "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected "
        "mat-calendar-body-today']"
    )
    today_element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, today_xpath))
    )
    today_element.click()
    print("Today's Date:", today_element.text)
    queueelement = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@class='col-lg-12 col-xxl-12 p-2']//div[@class='p-inputgroup']",
            )
        )
    )
    queueelement.click()
    time.sleep(3)
    dropqueue = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//li[@class='p-ripple p-element p-dropdown-item p-highlight']["
                "@id='p-highlighted-option']",
            )
        )
    )
    dropqueue.click()
    print("Selected Queue", dropqueue.text)
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//label[normalize-space()='Please upload Notes/Files related to "
                "your service']",
            )
        )
    )
    # login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    login.execute_script("arguments[0].scrollIntoView();", element)
    notes = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='chip-group']//div[1]//a[1]")
        )
    )
    notes.click()
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//textarea[@placeholder='Add Note']")
        )
    ).send_keys("Hai Welcome")
    submitnotebutton = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
    )
    submitnotebutton.click()
    time.sleep(3)
    login.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    noteaccordions = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//label[normalize-space()='Notes Added']")
        )
    )
    noteaccordions.click()
    login.execute_script("arguments[0].scrollIntoView();", noteaccordions)
    time.sleep(5)
    added_notes = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='customerNoteDetails mt-2']")
        )
    )
    print("Input Added Notes", added_notes.text)
    noteaccordions.click()
    time.sleep(3)
    uploadfile = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Upload File']")
        )
    )
    uploadfile.click()
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
    uploadfileaccordion = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[contains(text(),'Files selected')]")
        )
    )
    uploadfileaccordion.click()
    print("Uploaded File Successfully")
    time.sleep(3)
    confirmed = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Confirm']")
        )
    )
    confirmed.click()
    try:
        snack_bar = WebDriverWait(login, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        print("Snackbar Message :", snack_bar.text)
    except TimeoutException:
        try:
            snackbarerror = WebDriverWait(login, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
            )
            print("Snackbar Message : ", snackbarerror.text)
            cancelbutton = WebDriverWait(login, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Cancel']")
                )
            )
            cancelbutton.click()
        except TimeoutException:
            cancelbutton = WebDriverWait(login, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Cancel']")
                )
            )
            cancelbutton.click()
            print("Cancelled Successfully")
        time.sleep(1)
    while True:
        try:
            print("Before in the loop")
            time.sleep(3)
            next_button = WebDriverWait(login, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//angledoublerighticon[@class='p-element p-icon-wrapper "
                        "ng-star-inserted']",
                    )
                )
            )
            next_button.click()
        except:
            print("EC Caught:Next button not found or clicked.")
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
    login.execute_script(
        "arguments[0].scrollIntoView(true);", last_element_in_accordian
    )
    time.sleep(5)
    print("Accordion expanded")
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")
        )
    ).click()
    time.sleep(3)
    print("ViewDetails Button Clicked") 
     # # **** FollowUp *****
     
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Follow Up']")
        )
    ).click()
    time.sleep(3)
    calendar_header = WebDriverWait(login, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "mat-calendar-header"))
            )
    next_month_button = calendar_header.find_element(By.CSS_SELECTOR, "button[aria-label='Next month']")
    print(next_month_button)
    next_month_button.click()
    time.sleep(3)
    calendar_firstday_select = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='mat-calendar-body-cell-content mat-focus-indicator'][normalize-space()='1']"))
    )
    calendar_firstday_select.click()
    print("follow up on the first day of the upcoming month:",calendar_firstday_select)
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Confirm']")
        )
    ).click()
    snack_bar = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    )
    print("Snackbar Message :", snack_bar.text)
    time.sleep(3)