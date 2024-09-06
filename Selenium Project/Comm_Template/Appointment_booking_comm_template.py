import uuid
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

from Framework.common_utils import *
# 
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create confirmation template")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appt_confirmation(login):
    
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
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='APPOINTMENT']"))
    ).click()
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@aria-label='dropdown trigger'])[2]"))
    ).click()
    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Appointment Confirmation']"))
    ).click()

    time.sleep(3)
    temp_name = "appt_confirmation" + str(uuid.uuid4())[:4]
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
            (By.XPATH, "//div[@class='pull-right tag-style mgn-lt-5' and contains(img/@src, 'VariableTag.png')]"))
    ).click()
    
    Consumer_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Consumer name']")) 
    )
    Consumer_name.click()

    editer1.click()
    editer1.send_keys(Keys.ENTER)
    editer1.send_keys("Booking for")

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='pull-right tag-style mgn-lt-5' and contains(img/@src, 'VariableTag.png')]"))
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
            (By.XPATH, "//li[@aria-label='User name']"))
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
                "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]",
            )
        )
    ).click()
    time.sleep(3)
    element = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'my-1') and .//span[text()='Appointment']]",
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

    service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
    element = login.find_element(By.XPATH, service_dropdown_xpath)
    login.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

    service_option_xpath = (
        "(//div[@class='option-container ng-star-inserted'][normalize-space()='Naveen "
        "Consultation'])[2]"
    )
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))
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
    
    Today_Date.click()
    print("Today Date:", Today_Date.text)
    wait = WebDriverWait(login, 10)
    time_slot = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']"))
    )
    time_slot.click()
    print("Time Slot:", time_slot.text)

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

##########################################################################################################################################################################    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create Cancellation template")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appt_cancellation(login):

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
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='APPOINTMENT']"))
    ).click()
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@aria-label='dropdown trigger'])[2]"))
    ).click()
    
    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Appointment Cancellation']"))
    ).click()

    time.sleep(3)
    temp_name = "appt_cancellation" + str(uuid.uuid4())[:4]
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
            (By.XPATH, "//div[@class='pull-right tag-style mgn-lt-5' and contains(img/@src, 'VariableTag.png')]"))
    ).click()
    
    Consumer_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Consumer name']")) 
    )
    Consumer_name.click()

    editer1.click()
    editer1.send_keys(Keys.ENTER)
    editer1.send_keys("Booking Cancelled for")

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='pull-right tag-style mgn-lt-5' and contains(img/@src, 'VariableTag.png')]"))
    ).click()

    business_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Service name']"))
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
            (By.XPATH, "//li[@aria-label='Business Name']"))
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
                "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]",
            )
        )
    ).click()
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

#################################################################################################################################################################

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Appointment Reconfirmation template")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appt_reconfirmation(login):
     
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
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='APPOINTMENT']"))
    ).click()
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@aria-label='dropdown trigger'])[2]"))
    ).click()
    
    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Appointment Reconfirmation']"))
    ).click()

    time.sleep(3)
    temp_name = "appt_reconfirmation" + str(uuid.uuid4())[:4]
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
            (By.XPATH, "//div[@class='pull-right tag-style mgn-lt-5' and contains(img/@src, 'VariableTag.png')]"))
    ).click()
    
    Consumer_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Consumer name']")) 
    )
    Consumer_name.click()

    editer1.click()
    editer1.send_keys(Keys.ENTER)
    editer1.send_keys("Booking Reconfirmation for")

    time.sleep(2)

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='pull-right tag-style mgn-lt-5' and contains(img/@src, 'VariableTag.png')]"))
    ).click()

    business_name = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[@aria-label='Service name']"))
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
            (By.XPATH, "//li[@aria-label='Business Name']"))
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
                "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]",
            )
        )
    ).click()

    WebDriverWait(login, 10).until(
         EC.presence_of_element_located(
              (By.XPATH, "(//input[@type='checkbox'])[4]"))
    ).click()

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
            (By.XPATH, "//button[normalize-space()='Change Status']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='status status-box']")
        )
    ).click()

    toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_message.text
    print("Toast Message:", message)

    time.sleep(3)

#############################################################################################################################################################################
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Appointment started template")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appt_started(login):
     
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
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='APPOINTMENT']"))
    ).click()
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@aria-label='dropdown trigger'])[2]"))
    ).click()
    
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Appointment Started']"))
    ).click()

    time.sleep(3)
    temp_name = "appt_started" + str(uuid.uuid4())[:4]
    template_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='off']"))
    )
    template_namebox.clear()
    template_namebox.send_keys(temp_name)

    login.find_element(By.XPATH, "//span[normalize-space()='Email']").click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save & Next']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[1]/input[1]"))
    ).send_keys("Your booking with")


    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[2]/input[1]"))
    ).send_keys("Consultaion Started")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/div[1]/div[1]/app-template-details[1]/section[1]/div[3]/div[2]/div[2]/div[2]/div[3]/input[1]"))
    ).send_keys("Hello")
    
    
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
                "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]",
            )
        )
    ).click()

    WebDriverWait(login, 10).until(
         EC.presence_of_element_located(
              (By.XPATH, "(//input[@type='checkbox'])[4]"))
    ).click()

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
            (By.XPATH, "//button[normalize-space()='Change Status']")
        )
    ).click()

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Start')]")
        )
    ).click()

    toast_message = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "p-toast-detail"))
    )
    message = toast_message.text
    print("Toast Message:", message)

    time.sleep(3)