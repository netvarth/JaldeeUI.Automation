from Framework.common_utils import *


@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_create_patient(login):
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

    service_option_xpath = "//span[@class='ng-star-inserted'][normalize-space()='Naveen Consultation']"
    WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
    print("Select Service : Naveen Consultation")
    time.sleep(3)

    # Select today's date

    today_date = WebDriverWait(login, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
    today_date.click()
    print("Today Date:", today_date.text)

    # Wait for time slots to become clickable
    wait = WebDriverWait(login, 10)
    time_slots = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//button[@aria-selected='true']")))
    time.sleep(3)

    # Define how many slots you want to select (e.g., 4 slots)
    slots_to_select = 4

    # Click the first 'slots_to_select' number of slots
    for i in range(slots_to_select):
        if i < len(time_slots):
            time_slots[i].click()
            print(f"Time Slot {i + 1}:", time_slots[i].text)
        else:

            print(f"Not enough available time slots to select {slots_to_select} slots.")
            break

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@name='consumerNote']"))
    ).send_keys("Block slot test")
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Confirm']"))
    ).click()
    # try:
    #
    #     snack_bar = WebDriverWait(login, 10).until(
    #         EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    #     )
    #     message = snack_bar.text
    #     print("Snack bar message:", message)
    #
    # except:
    #
    #     snack_bar = WebDriverWait(login, 10).until(
    #         EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
    #     )
    #     message = snack_bar.text
    #     print("Snack bar message:", message)

