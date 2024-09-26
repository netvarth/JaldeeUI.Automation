import uuid
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

from Framework.common_utils import *
 
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create confirmation template")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_token_confirmation(login):
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Settings')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Communications And Notifications']"))
        ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li//a//span[@class='lnk setings ml-auto' and normalize-space(text())='Notifications']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[normalize-space()='Custom Templates']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create New']"))
    ).click()
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel='context']//div[@aria-label='dropdown trigger']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='CHECKIN']"))
    ).click()
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
    ).click()
    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Token Confirmation']"))
    ).click()

    time.sleep(3)
    temp_name = "token_confirmation" + str(uuid.uuid4())[:4]
    template_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='off']"))
    )
    template_namebox.clear()
    template_namebox.send_keys(temp_name)

    login.find_element(By.XPATH, "//span[normalize-space()='Whatsapp']").click()
    login.find_element(By.XPATH, "//span[normalize-space()='Email']").click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save & Next']"))
    ).click()

    editer1= WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']"))
    )
    editer1.send_keys("Hello")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[1]"))
    ).click()
    
    Consumer_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Consumer name']")) 
    )
    Consumer_name.click()

    editer1.click()
    editer1.send_keys(Keys.ENTER)
    editer1.send_keys(Keys.ENTER)
    editer1.send_keys("Booking for")

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[1]"))
    ).click()

    business_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Business Name']"))
    )
    business_name.click()

    editer1.click()
    editer1.send_keys(Keys.ENTER)

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='pull-right tag-style mgn-lt-5' and contains(img/@src, 'VariableTag.png')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Consumer name']"))
    ).click()

    editer1.click()
    editer1.send_keys(Keys.ENTER)

    time.sleep(2)
    email_subject_line = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[1]/input[1]"))
    )
    email_subject_line.click()
    email_subject_line.send_keys("Confirmation")
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[2]")
    time.sleep(2)
    business_name = WebDriverWait(login, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//li[@aria-label='Business Name']")) 
    )
    business_name.click()
    time.sleep(2)
    header_notes = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[2]/input[1]"))
    )
    header_notes.click()
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[3]")
    consumer_name = WebDriverWait(login, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//li[@aria-label='Consumer name']")) 
    )
    consumer_name.click()
    time.sleep(2)
    salutation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[3]/input[1]"))
    )
    salutation.click()
    salutation.send_keys("Greetings!!")
    time.sleep(2)
    Signature = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[4]/input[1]"))
    )
    Signature.click()
    Signature.send_keys("Thank you for using Jaldee")
    time.sleep(2)
    Footer = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[5]/input[1]"))
    )
    Footer.click()
    Footer.send_keys("Powered by Jaldee business")
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='actiondiv mgn-lt-10 desktop-only']//button[@class='cs-btn btn btn-primary btn-transform']"))
    ).click()

    time.sleep(2)
    ripple_switch = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[contains(text(),'Inactive')])[1]"))
    )
    ripple_switch.click()
    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[@src='./assets/images/menu/home-color.png']"))
    ).click()

    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[contains(text(),'Tokens')]",
            )
        )
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[normalize-space()='Token']",
            )
        )
    )
    element.click()
    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
        )
    ).send_keys("920720600")
    time.sleep(2)
    login.implicitly_wait(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Id : 2']")
        )
    ).click()

    login.implicitly_wait(3)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "p-dropdown[optionlabel='place']")
        )
    ).click()

    login.implicitly_wait(5)
    login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
    print("location : Chavakkad")
    login.implicitly_wait(5)

    login.find_element(
        By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']"
    ).click()
    login.implicitly_wait(5)
    login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
    print("Department : ENT")
    user_dropdown_xpath = (
        "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-provider-checkin[1]/section[2]/div[1]/div[1]/div[1]/app-checkin-form[1]/section[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/p-dropdown[1]/div[1]/div[2]/span[1]"
    )
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))
    ).click()
    user_option_xpath = "//span[contains(text(),'Naveen KP')]"
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, user_option_xpath))
    ).click()
    print("Select user : Naveen")

    time.sleep(5)
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


    time.sleep(5)
    
 ###################################################################################################################################################   
    
##############################################################################################################

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create reminder template")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_token_reminder(login):
  
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Settings')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Communications And Notifications']"))
        ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li//a//span[@class='lnk setings ml-auto' and normalize-space(text())='Notifications']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[normalize-space()='Custom Templates']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create New']"))
    ).click()
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel='context']//div[@aria-label='dropdown trigger']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='CHECKIN']"))
    ).click()
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
    ).click()
    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Token Reminder']"))
    ).click()

    time.sleep(3)
    temp_name = "token_reminder" + str(uuid.uuid4())[:4]
    template_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='off']"))
    )
    template_namebox.clear()
    template_namebox.send_keys(temp_name)

    login.find_element(By.XPATH, "//span[normalize-space()='Whatsapp']").click()
    login.find_element(By.XPATH, "//span[normalize-space()='Email']").click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save & Next']"))
    ).click()

    editer1= WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']"))
    )
    editer1.send_keys("Hello")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[1]"))
    ).click()
    
    Consumer_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Consumer name']")) 
    )
    Consumer_name.click()

    editer1.click()
    editer1.send_keys(Keys.ENTER)
    editer1.send_keys(Keys.ENTER)
    editer1.send_keys("Booking Reminder for")

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[1]"))
    ).click()

    business_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Business Name']"))
    )
    business_name.click()

    editer1.click()
    editer1.send_keys(Keys.ENTER)

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='pull-right tag-style mgn-lt-5' and contains(img/@src, 'VariableTag.png')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Consumer name']"))
    ).click()

    editer1.click()
    editer1.send_keys(Keys.ENTER)

    time.sleep(2)
    email_subject_line = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[1]/input[1]"))
    )
    email_subject_line.click()
    email_subject_line.send_keys("Reminder from")
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[2]")
    time.sleep(2)
    business_name = WebDriverWait(login, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//li[@aria-label='Business Name']")) 
    )
    business_name.click()
    time.sleep(2)
    header_notes = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[2]/input[1]"))
    )
    header_notes.click()
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[3]")
    consumer_name = WebDriverWait(login, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//li[@aria-label='Consumer name']")) 
    )
    consumer_name.click()
    time.sleep(2)
    salutation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[3]/input[1]"))
    )
    salutation.click()
    salutation.send_keys("Greetings!!")
    time.sleep(2)
    Signature = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[4]/input[1]"))
    )
    Signature.click()
    Signature.send_keys("Thank you for using Jaldee")
    time.sleep(2)
    Footer = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[5]/input[1]"))
    )
    Footer.click()
    Footer.send_keys("Powered by Jaldee business")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='actiondiv mgn-lt-10 desktop-only']//button[@class='cs-btn btn btn-primary btn-transform']"))
    ).click()

    time.sleep(2)
    ripple_switch = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[contains(text(),'Inactive')])[1]"))
    )
    ripple_switch.click()
    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[@src='./assets/images/menu/home-color.png']"))
    ).click()

    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[contains(text(),'Tokens')]",
            )
        )
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[normalize-space()='Token']",
            )
        )
    )
    element.click()
    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
        )
    ).send_keys("920720600")
    time.sleep(2)
    login.implicitly_wait(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Id : 2']")
        )
    ).click()

    login.implicitly_wait(3)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "p-dropdown[optionlabel='place']")
        )
    ).click()

    login.implicitly_wait(5)
    login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
    print("location : Chavakkad")
    login.implicitly_wait(5)

    login.find_element(
        By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']"
    ).click()
    login.implicitly_wait(5)
    login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
    print("Department : ENT")
    user_dropdown_xpath = (
        "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-provider-checkin[1]/section[2]/div[1]/div[1]/div[1]/app-checkin-form[1]/section[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/p-dropdown[1]/div[1]/div[2]/span[1]"
    )
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))
    ).click()
    user_option_xpath = "//span[contains(text(),'Naveen KP')]"
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, user_option_xpath))
    ).click()
    print("Select user : Naveen")

    time.sleep(5)
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

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Share Info']"))
    ).click()
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='mdc-button__label']"))
    ).click()


    time.sleep(5)

##############################################################################################################  
 
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Token Reschedule template")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_token_Reschedule(login):
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Settings')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Communications And Notifications']"))
        ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li//a//span[@class='lnk setings ml-auto' and normalize-space(text())='Notifications']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[normalize-space()='Custom Templates']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create New']"))
    ).click()
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel='context']//div[@aria-label='dropdown trigger']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='CHECKIN']"))
    ).click()
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
    ).click()
    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Token Reschedule']"))
    ).click()

    time.sleep(3)
    temp_name = "token_reschedule" + str(uuid.uuid4())[:4]
    template_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='off']"))
    )
    template_namebox.clear()
    template_namebox.send_keys(temp_name)

    login.find_element(By.XPATH, "//span[normalize-space()='Whatsapp']").click()
    login.find_element(By.XPATH, "//span[normalize-space()='Email']").click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save & Next']"))
    ).click()

    editer1= WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']"))
    )
    editer1.send_keys("Hello")
   
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[1]"))
    ).click()
    
    Consumer_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Consumer name']")) 
    )
    Consumer_name.click()

    editer1.click()
    editer1.send_keys(Keys.ENTER)
    editer1.send_keys(Keys.ENTER)
    editer1.send_keys("Booking Reschedule for")

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[1]"))
    ).click()

    business_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Business Name']"))
    )
    business_name.click()

    editer1.click()
    editer1.send_keys(Keys.ENTER)

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='pull-right tag-style mgn-lt-5' and contains(img/@src, 'VariableTag.png')]"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Consumer name']"))
    ).click()

    editer1.click()
    editer1.send_keys(Keys.ENTER)


    time.sleep(2)
    email_subject_line = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[1]/input[1]"))
    )
    email_subject_line.click()
    email_subject_line.send_keys("Reschedule")
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[2]")
    time.sleep(2)
    business_name = WebDriverWait(login, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//li[@aria-label='Business Name']")) 
    )
    business_name.click()
    time.sleep(2)
    header_notes = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[2]/input[1]"))
    )
    header_notes.click()
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[3]")
    consumer_name = WebDriverWait(login, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//li[@aria-label='Consumer name']")) 
    )
    consumer_name.click()
    time.sleep(2)
    salutation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[3]/input[1]"))
    )
    salutation.click()
    salutation.send_keys("Greetings!!")
    time.sleep(2)
    Signature = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[4]/input[1]"))
    )
    Signature.click()
    Signature.send_keys("Thank you for using Jaldee")
    time.sleep(2)
    Footer = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[5]/input[1]"))
    )
    Footer.click()
    Footer.send_keys("Powered by Jaldee business")
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='actiondiv mgn-lt-10 desktop-only']//button[@class='cs-btn btn btn-primary btn-transform']"))
    ).click()

    time.sleep(2)
    ripple_switch = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[contains(text(),'Inactive')])[1]"))
    )
    ripple_switch.click()
    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[@src='./assets/images/menu/home-color.png']"))
    ).click()

    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[contains(text(),'Tokens')]",
            )
        )
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[normalize-space()='Token']",
            )
        )
    )
    element.click()
    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
        )
    ).send_keys("920720600")
    time.sleep(2)
    login.implicitly_wait(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Id : 2']")
        )
    ).click()

    login.implicitly_wait(3)
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "p-dropdown[optionlabel='place']")
        )
    ).click()

    login.implicitly_wait(5)
    login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
    print("location : Chavakkad")
    login.implicitly_wait(5)

    login.find_element(
        By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']"
    ).click()
    login.implicitly_wait(5)
    login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
    print("Department : ENT")
    user_dropdown_xpath = (
        "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-provider-checkin[1]/section[2]/div[1]/div[1]/div[1]/app-checkin-form[1]/section[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/p-dropdown[1]/div[1]/div[2]/span[1]"
    )
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))
    ).click()
    user_option_xpath = "//span[contains(text(),'Naveen KP')]"
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, user_option_xpath))
    ).click()
    print("Select user : Naveen")

    time.sleep(5)
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
    
    
    WebDriverWait(login, 10).until(
       EC.presence_of_element_located(
           (By.XPATH, "//button[normalize-space()='View Details']")) 
    ).click()
    
    time.sleep(2)
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Reschedule']"))
    ).click()
    
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


    time.sleep(5)   
   
##############################################################################################################    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Token Cancellation template")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_token_cancellation(login):
          
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Settings')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Communications And Notifications']"))
        ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li//a//span[@class='lnk setings ml-auto' and normalize-space(text())='Notifications']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[normalize-space()='Custom Templates']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create New']"))
    ).click()
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p-dropdown[@optionlabel='context']//div[@aria-label='dropdown trigger']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='CHECKIN']"))
    ).click()
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[2]"))
    ).click()
    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Token Cancellation']"))
    ).click()

    time.sleep(3)
    temp_name = "Token_cancellation" + str(uuid.uuid4())[:4]
    template_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='off']"))
    )
    template_namebox.clear()
    template_namebox.send_keys(temp_name)

    login.find_element(By.XPATH, "//span[normalize-space()='Whatsapp']").click()
    login.find_element(By.XPATH, "//span[normalize-space()='Email']").click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save & Next']"))
    ).click()

    editer1= WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@aria-label='Rich Text Editor. Editing area: main']"))
    )
    editer1.send_keys("Hello")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[1]"))
    ).click()
    
    Consumer_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Consumer name']")) 
    )
    Consumer_name.click()

    editer1.click()
    editer1.send_keys(Keys.ENTER)
    editer1.send_keys(Keys.ENTER)
    editer1.send_keys("Booking Cancelled for")

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[1]"))
    ).click()

    business_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Business Name']"))
    )
    business_name.click()

    editer1.click()
    editer1.send_keys(Keys.ENTER)

    
    time.sleep(2)
    email_subject_line = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[1]/input[1]"))
    )
    email_subject_line.click()
    email_subject_line.send_keys("Cancellation")
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[2]")
    time.sleep(2)
    business_name = WebDriverWait(login, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//li[@aria-label='Business Name']")) 
    )
    business_name.click()
    time.sleep(2)
    header_notes = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[2]/input[1]"))
    )
    header_notes.click()
    time.sleep(2)
    wait_and_locate_click(login, By.XPATH, "(//span[@class='mgn-lt-5'][normalize-space()='Add Variables'])[3]")
    consumer_name = WebDriverWait(login, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//li[@aria-label='Consumer name']")) 
    )
    consumer_name.click()
    time.sleep(2)
    salutation = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[3]/input[1]"))
    )
    salutation.click()
    salutation.send_keys("Greetings!!")
    time.sleep(2)
    Signature = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[4]/input[1]"))
    )
    Signature.click()
    Signature.send_keys("Thank you for using Jaldee")
    time.sleep(2)
    Footer = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[5]/input[1]"))
    )
    Footer.click()
    Footer.send_keys("Powered by Jaldee business")
    
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='pull-right tag-style mgn-lt-5' and contains(img/@src, 'VariableTag.png')]"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Consumer name']"))
    ).click()

    editer1.click()
    editer1.send_keys(Keys.ENTER)


    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='actiondiv mgn-lt-10 desktop-only']//button[@class='cs-btn btn btn-primary btn-transform']"))
    ).click()

    time.sleep(2)
    ripple_switch = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[contains(text(),'Inactive')])[1]"))
    )
    ripple_switch.click()
    time.sleep(3)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[@src='./assets/images/menu/home-color.png']"))
    ).click()

    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[contains(text(),'Tokens')]",
            )
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

    
################################################################################################################


   
    
    
    