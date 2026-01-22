from Framework.common_utils import *

first_name, last_name, cons_manual_id, phonenumber, email = create_user_data()



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Assigning the doctor")
@pytest.mark.parametrize("url, username, password", [(scale_url, main_scale, password)])

def test_appt_assgin_doc(login):
    try:
        
        time.sleep(5)

        wait_and_locate_click(login, By.XPATH, "//div[contains(@class, 'font-small') and contains(text(),'Appointments')]")

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
        wait = WebDriverWait(login, 10)
        element_appoint = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//b[contains(text(),'Create New Patient')]")
            )
        )
        element_appoint.click()
        time.sleep(3)

        login.find_element(By.XPATH, "//input[@id='first_name']").send_keys(str(first_name))
        login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(str(last_name))
        login.find_element(By.XPATH, "//*[@id='customer_id']").send_keys(cons_manual_id)
        login.find_element(By.XPATH, "//*[@id='phone']").send_keys(phonenumber)
        login.find_element(
            By.XPATH, "//ngx-intl-tel-input[@name='whatsApp']//input[@id='phone']"
        ).send_keys(phonenumber)
        login.find_element(By.XPATH, "//input[@id='email_id']").send_keys(email)
        save_button= login.find_element(By.XPATH, "//span[contains(text(),'Save')]")
        login.execute_script("arguments[0].click();", save_button)
        
        msg = get_snack_bar_message(login)
        print("Sanck Bar Message :", msg)

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
        ).click()

        time.sleep(3)
        login.find_element(By.XPATH, "(//li[@id='p-highlighted-option'])[1]").click()
        print("location : Chavakkad")
        time.sleep(2)

        login.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='departmentName']").click()
        time.sleep(3)
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

        service_option_xpath = ("//li[@aria-label='Naveen Consultation']//div[1]")
        WebDriverWait(login, 10).until(EC.element_to_be_clickable((By.XPATH, service_option_xpath))).click()
        print("Select Service : Naveen Consultation")
        time.sleep(3)
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
        wait = WebDriverWait(login, 10)
        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-selected='true']"))
        )
        time_slot.click()
        print("Time Slot:", time_slot.text)
        note_input = login.find_element(By.XPATH, "//div[@class='chip-group']//div[1]")
        note_input.click()
        login.find_element(By.XPATH, "//textarea[@id='tctareaMsg_BUS_addNote']").send_keys(
            "test_selenium project"
        )
        WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Save']"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Confirm']")
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


        View_Detail_button = WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(), 'View Details')]")
            )
        )
        View_Detail_button.click()
        login.execute_script("arguments[0].click();", View_Detail_button)
        time.sleep(3)


    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

   