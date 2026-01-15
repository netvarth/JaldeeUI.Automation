from Framework.common_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Send message with attachment.")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_send_message(login):
    try:

        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "(//img)[3]")
        
        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//div[@id='actionCreate_BUS_bookList'])[1]",
                )
            )
        )
        element.click()
        time.sleep(3)
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='btnCreateCust_BUS_appt']")
            )
        )
        element_appoint.click()
        time.sleep(2)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()

        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(
            str(first_name)
        )
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(
            str(last_name)
        )
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(
            By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
        ).send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()
        
        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(3)

        wait_and_locate_click(
            login, By.XPATH, "//*[@id='selctLoc_BUS_apptForm']"
            )

        time.sleep(2)

        login.find_element(By.XPATH, "//*[@class='ng-star-inserted'][normalize-space()='Chavakkad']").click()
        print("location : Chavakkad")

        time.sleep(2)

        login.find_element(By.XPATH, "//*[@id='selectDept_BUS_apptForm']").click()
        
        time.sleep(2)

        login.find_element(By.XPATH, "//*[@class='ng-star-inserted'][normalize-space()='ENT']").click()
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

        service_option_xpath = "//li[@aria-label='Naveen Consultation']//div[1]"
        WebDriverWait(login, 10).until(EC.presence_of_element_located((By.XPATH, service_option_xpath))).click()
        print("Select Service : Naveen Consultation")
        time.sleep(3)
        Today_Date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
        Today_Date.click()
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(login, 10)
        time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
        time_slot.click()
        print("Time Slot:", time_slot.text)
        note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
        note_input.click()
        login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys("test_selenium project")
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()

        time.sleep(4)
        login.find_element(By.XPATH,
                        "//span[normalize-space()='Confirm']").click()

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)
         

        time.sleep(3)

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

        view_details_button = WebDriverWait(login, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'View Details')]"))
        )
        view_details_button.click()

        login.execute_script("arguments[0].click();", view_details_button)
        
        time.sleep(3)

        wait_and_locate_click(login, By.XPATH, "//button[@id='btnMoreactn_BUS_bookAction']")

        time.sleep(2)

        wait_and_locate_click(login, By.XPATH, "//button[@id='btnSendMsg_BUS_bookAction']")

        login.find_element(By.XPATH, " //textarea[@id='messageData']").send_keys("test_selenium project")

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Click here to select the files']"))
        ).click()

        time.sleep(4)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))
        pyautogui.write(absolute_path)
        time.sleep(3)
        pyautogui.press('enter')

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'send')]"))
        ).click()

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Send Message Successfully with out Phone number")    
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_send_message_1(login):
    try:

        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "(//img)[3]")
        
        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//div[@id='actionCreate_BUS_bookList'])[1]",
                )
            )
        )
        element.click()
        time.sleep(3)
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='btnCreateCust_BUS_appt']")
            )
        )
        element_appoint.click()
        time.sleep(2)

        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

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
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
        ).click()

        time.sleep(2)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        time.sleep(2)

        login.find_element(By.XPATH, "//*[@id='selectDept_BUS_apptForm']").click()

        time.sleep(2)
        login.find_element(By.XPATH, "//*[@class='ng-star-inserted'][normalize-space()='ENT']").click()
        print("Department : ENT")

        user_dropdown_xpath = (
            "(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
            "ng-dirty'])[1]")
        
        WebDriverWait(login, 30).until(EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 30).until(EC.element_to_be_clickable((By.XPATH, user_option_xpath))).click()

        print("Select user : Naveen")
        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        element = login.find_element(By.XPATH, service_dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        service_option_xpath = "//li[@aria-label='Naveen Consultation']//div[1]"
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
        print("Select Service : Naveen Consultation")
        time.sleep(3)
        Today_Date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
        Today_Date.click()
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(login, 10)
        time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
        time_slot.click()
        print("Time Slot:", time_slot.text)
        note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
        note_input.click()
        login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys("test_selenium project")
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))).click()


        time.sleep(4)
        login.find_element(By.XPATH,
                        "//span[normalize-space()='Confirm']").click()

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(3)

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
        time.sleep(2)
        view_details_button = WebDriverWait(login, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='View Details']"))
        )
        view_details_button.click()
        login.execute_script("arguments[0].click();", view_details_button)

        time.sleep(3)
        more_actions_button = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//button[normalize-space()='More Actions'])[1]"))
        )
        more_actions_button.click()

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Send Message']"))
        ).click()

        login.find_element(By.XPATH, " //textarea[@id='messageData']").send_keys("test_selenium project")

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'send')]"))
        ).click()

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        print("Send Message Successfully with out Phone number")

        time.sleep(3)
        # Patient with no mobile and no email updated
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Send Message without attachment.")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_send_message_2(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "(//img)[3]")
        
        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//div[@id='actionCreate_BUS_bookList'])[1]",
                )
            )
        )
        element.click()
        time.sleep(3)
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='btnCreateCust_BUS_appt']")
            )
        )
        element_appoint.click()
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
        ).click()

        time.sleep(2)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        time.sleep(2)

        login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
        time.sleep(2)
        login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
        print("Department : ENT")
        user_dropdown_xpath = (
            "(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
            "ng-dirty'])[1]")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_option_xpath))).click()
        print("Select user : Naveen")
        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        element = login.find_element(By.XPATH, service_dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        service_option_xpath = "//li[@aria-label='Naveen Consultation']//div[1]"
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
        print("Select Service : Naveen Consultation")
        time.sleep(3)
        Today_Date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
        Today_Date.click()
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(login, 10)
        time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
        time_slot.click()
        print("Time Slot:", time_slot.text)

        time.sleep(2)
        login.find_element(By.XPATH, "//span[normalize-space()='Confirm']").click()

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(3)

        while True:
            try:
                print("before in loop")
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//anglerighticon[@class='p-element p-icon-wrapper ng-star-inserted']"))
                )

                next_button.click()

            except:
                print("EC caught:")
                break

        last_element_in_accordian = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card my-1 p-0 ng-star-inserted')][last()]"))
        )
        last_element_in_accordian.click()

        time.sleep(2)
        view_details_button = WebDriverWait(login, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'View Details')]"))
        )
        view_details_button.click()
        login.execute_script("arguments[0].click();", view_details_button)
        
        time.sleep(3)
        more_actions_button = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='More Actions']"))
        )
        more_actions_button.click()

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Send Message']"))
        ).click()

        login.find_element(By.XPATH, " //textarea[@id='messageData']").send_keys("Automation test for send message ")

        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'send')]"))
        ).click()

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(3)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])
def test_send_message_3(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "(//img)[3]")
        
        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//div[@id='actionCreate_BUS_bookList'])[1]",
                )
            )
        )
        element.click()
        time.sleep(3)
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='btnCreateCust_BUS_appt']")
            )
        )
        element_appoint.click()
        time.sleep(2)
        first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()
        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']").send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        login.find_element(By.XPATH, "//span[contains(text(),'Save')]").click()

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
        ).click()

        time.sleep(2)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        time.sleep(2)

        login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
        time.sleep(2)
        login.find_element(By.XPATH, "(//li[@aria-label='ENT'])[1]").click()
        print("Department : ENT")
        user_dropdown_xpath = (
            "(//p-dropdown[@class='p-element p-inputwrapper p-inputwrapper-filled ng-untouched ng-valid "
            "ng-dirty'])[1]")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_dropdown_xpath))).click()
        user_option_xpath = "(//li[@aria-label='Naveen KP'])[1]"
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, user_option_xpath))).click()
        print("Select user : Naveen")
        service_dropdown_xpath = "//p-dropdown[@optionlabel='name']"
        element = login.find_element(By.XPATH, service_dropdown_xpath)
        login.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        service_option_xpath = "//li[@aria-label='Naveen Consultation']//div[1]"
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
        print("Select Service : Naveen Consultation")
        time.sleep(3)
        Today_Date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                "//span[@class='mat-calendar-body-cell-content mat-focus-indicator mat-calendar-body-selected mat-calendar-body-today']")))
        Today_Date.click()
        print("Today Date:", Today_Date.text)
        wait = WebDriverWait(login, 10)
        time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']")))
        time_slot.click()
        print("Time Slot:", time_slot.text)

        time.sleep(2)
        login.find_element(By.XPATH, "//span[normalize-space()='Confirm']").click()

        msg = get_snack_bar_message(login)
        print("Snack Bar Message :", msg)

        time.sleep(3)

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

        time.sleep(2)
        view_details_button = WebDriverWait(login, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'View Details')]"))
        )
        view_details_button.click()
        login.execute_script("arguments[0].click();", view_details_button)

        more_actions_button = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='More Actions']"))
        )
        more_actions_button.click()

        time.sleep(3)

        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Send Message']"))
        ).click()

        # login.find_element(By.XPATH, " //textarea[@id='messageData']").send_keys("Automation test for send message ")
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Click here to select the files']"))
        ).click()

        time.sleep(4)
        # Get the current working directory
        current_working_directory = os.getcwd()

        # Construct the absolute path
        absolute_path = os.path.abspath(os.path.join(current_working_directory, r'Extras\test.png'))
        pyautogui.write(absolute_path)
        pyautogui.press('enter')
        time.sleep(2)

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'send')]"))
        )

        send_button = login.find_element(By.XPATH, "//button[normalize-space()='send']")
        assert not send_button.is_enabled(), "Send button should be disabled"

        time.sleep(2)
    
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

