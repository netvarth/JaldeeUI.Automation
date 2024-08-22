from Framework.common_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create comfirmation template")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_appt_confirmation(login):

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Settings')]"))
    ).click()

    time.sleep(2)
    notification_option = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Communications And Notifications']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", notification_option)

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li//a//span[@class='lnk setings ml-auto' and normalize-space(text())='Notifications']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//h2[normalize-space()='Custom Templates']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Create New']"))
    ).click()

    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p-dropdown[@optionlabel='context']//div[@aria-label='dropdown trigger']"))
    ).click()

    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='APPOINTMENT']"))
    ).click()

    template_namebox = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='off']"))
    )

    time.sleep(2)
    temp_name = "appt_confirmation" + str(uuid.uuid4())[:4]
    template_namebox.click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='form-group']//input[contains(@class, 'p-inputtext')]"))
    ).send_keys(temp_name)

    login.find_element(By.XPATH, "//span[normalize-space()='Whatsapp']").click()
    login.find_element(By.XPATH, "//span[normalize-space()='Email']").click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Edit Saved Template']"))
    ).click()
    

    time.sleep(5)



 


