
from Framework.common_utils import*


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Create Invoice for token Walkin")
@pytest.mark.parametrize('url', ["https://test.jaldee.com/business/"])
def test_create_invoice_token_walkin(login):
    time.sleep(5)
    try:
        WebDriverWait(login, 15).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "overlay"))  # Adjust this class if needed
        )
        print("Overlay has disappeared.")
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/app-sidebar-menu[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]/div[1]/span[1]/span[1]/span[1]/img[1]"))
        ).click()

        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Token']"))
        )
        element.click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
            )
        ).send_keys("9207206005")

        time.sleep(3)

        # Store the patient's name after selecting it
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Id : 2']")
            )
        ).click()
        


        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[normalize-space()='Id : 2']")
        #     )
        # ).click()


        login.implicitly_wait(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

        time.sleep(2)
        booking_number = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='fw-bold ng-star-inserted'])[1]"))
        )

        booking_id = booking_number.text


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Invoices'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

         # Capture the booking id on the invoice page for assertion
        invoice_booking_id = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='col-lg-3 col-md-6 invoice-detail-style d-flex text-start'])[1]"))
        ).text

        print(f"Expected booking id: '{booking_id}', Actual booking id: '{invoice_booking_id}'")
        # Assert that the patient's name matches
        assert invoice_booking_id.strip() == booking_id.strip(), f"Expected booking id '{booking_id.strip()}', but found '{invoice_booking_id.strip()}' on invoice."


        time.sleep(2)
        payment_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", payment_button)
        payment_button.click()
        
        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

        time.sleep(3)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1 
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Pay by cash")
@pytest.mark.parametrize('url', ["https://test.jaldee.com/business/"])
def test_pay_by_cash(login):
    time.sleep(5)
    try:
        WebDriverWait(login, 15).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "overlay"))  # Adjust this class if needed
        )
        print("Overlay has disappeared.")
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/app-sidebar-menu[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]/div[1]/span[1]/span[1]/span[1]/img[1]"))
        ).click()

        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Token']"))
        )
        element.click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
            )
        ).send_keys("9207206005")

        time.sleep(3)

        # Store the patient's name after selecting it
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Id : 2']")
            )
        ).click()
        


        # WebDriverWait(login, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//span[normalize-space()='Id : 2']")
        #     )
        # ).click()


        login.implicitly_wait(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

        time.sleep(2)
        booking_number = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='fw-bold ng-star-inserted'])[1]"))
        )

        booking_id = booking_number.text


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Invoices'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

         # Capture the booking id on the invoice page for assertion
        invoice_booking_id = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='col-lg-3 col-md-6 invoice-detail-style d-flex text-start'])[1]"))
        ).text

        print(f"Expected booking id: '{booking_id}', Actual booking id: '{invoice_booking_id}'")

        # Assert that the patient's name matches
        assert invoice_booking_id.strip() == booking_id.strip(), f"Expected booking id '{booking_id.strip()}', but found '{invoice_booking_id.strip()}' on invoice."


        time.sleep(2)
        payment_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", payment_button)
        payment_button.click()
        
        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Pay by Cash']"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Pay']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Yes']"))
        ).click()

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

        time.sleep(3)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1 
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Pay by others")
@pytest.mark.parametrize('url', ["https://test.jaldee.com/business/"])
def test_pay_by_others(login):
    time.sleep(5)
    try:
        WebDriverWait(login, 15).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "overlay"))  # Adjust this class if needed
        )
        print("Overlay has disappeared.")
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/app-sidebar-menu[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]/div[1]/span[1]/span[1]/span[1]/img[1]"))
        ).click()

        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Token']"))
        )
        element.click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
            )
        ).send_keys("9207206005")

        time.sleep(3)

        # Store the patient's name after selecting it
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Id : 2']")
            )
        ).click()
        
        login.implicitly_wait(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

        time.sleep(2)
        booking_number = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='fw-bold ng-star-inserted'])[1]"))
        )

        booking_id = booking_number.text


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Invoices'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

         # Capture the booking id on the invoice page for assertion
        invoice_booking_id = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='col-lg-3 col-md-6 invoice-detail-style d-flex text-start'])[1]"))
        ).text

        print(f"Expected booking id: '{booking_id}', Actual booking id: '{invoice_booking_id}'")

        # Assert that the patient's name matches
        assert invoice_booking_id.strip() == booking_id.strip(), f"Expected booking id '{booking_id.strip()}', but found '{invoice_booking_id.strip()}' on invoice."


        time.sleep(2)
        payment_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", payment_button)
        payment_button.click()
        
        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Pay by Others']"))
        ).click()

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Pay']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Yes']"))
        ).click()

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

        time.sleep(3)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1 
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Share the PDF Invoice")
@pytest.mark.parametrize('url', ["https://test.jaldee.com/business/"])
def test_share_pdf(login):
    time.sleep(5)
    try:
        WebDriverWait(login, 15).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "overlay"))  # Adjust this class if needed
        )
        print("Overlay has disappeared.")
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/app-sidebar-menu[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]/div[1]/span[1]/span[1]/span[1]/img[1]"))
        ).click()

        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Token']"))
        )
        element.click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
            )
        ).send_keys("9207206005")

        time.sleep(3)

        # Store the patient's name after selecting it
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Id : 2']")
            )
        ).click()
        
        login.implicitly_wait(3)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

        time.sleep(2)
        booking_number = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='fw-bold ng-star-inserted'])[1]"))
        )

        booking_id = booking_number.text


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Invoices'])[1]"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

         # Capture the booking id on the invoice page for assertion
        invoice_booking_id = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='col-lg-3 col-md-6 invoice-detail-style d-flex text-start'])[1]"))
        ).text

        print(f"Expected booking id: '{booking_id}', Actual booking id: '{invoice_booking_id}'")

        # Assert that the patient's name matches
        assert invoice_booking_id.strip() == booking_id.strip(), f"Expected booking id '{booking_id.strip()}', but found '{invoice_booking_id.strip()}' on invoice."


        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Share PDF']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

        time.sleep(3)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1 
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Apply the discount")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_apply_discount(login):
    time.sleep(3)
    try:
        WebDriverWait(login, 15).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "overlay"))  # Adjust this class if needed
        )
        print("Overlay has disappeared.")
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/app-sidebar-menu[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]/div[1]/span[1]/span[1]/span[1]/img[1]"))
        ).click()

        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Token']"))
        )
        element.click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
            )
        ).send_keys("9207206005")

        time.sleep(3)

        # Store the patient's name after selecting it
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Id : 2']")
            )
        ).click()
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

        time.sleep(2)
        booking_number = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='fw-bold ng-star-inserted'])[1]"))
        )

        booking_id = booking_number.text


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
        ).click()

        time.sleep(3)
        invoice_card = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Invoices'])[1]"))
        )
        login.execute_script("arguments[0].click();", invoice_card)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

         # Capture the booking id on the invoice page for assertion
        invoice_booking_id = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='col-lg-3 col-md-6 invoice-detail-style d-flex text-start'])[1]"))
        ).text

        print(f"Expected booking id: '{booking_id}', Actual booking id: '{invoice_booking_id}'")

        # Assert that the patient's name matches
        assert invoice_booking_id.strip() == booking_id.strip(), f"Expected booking id '{booking_id.strip()}', but found '{invoice_booking_id.strip()}' on invoice."


        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Edit']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='svg-icon svg-icon-lg svg-icon-success']//*[name()='svg']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-list-item__primary-text'][normalize-space()='Apply Discount']"))
        ).click()

        time.sleep(1)
        select_discount = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//select[./option[text()='Select Discount']])[3]"))
        )
        select_discount.click()

        login.implicitly_wait(3)
        demand_discount = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//option[normalize-space()='On Demand Discount'])[3]"))
        )
        demand_discount.click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter Amount']"))
        ).send_keys("10")

        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='modal-footer']//button[contains(text(), 'Apply')]"))
        )

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Update']"))
        ).click()

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

        time.sleep(2)
        payment_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", payment_button)
        payment_button.click()
        
        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)



        time.sleep(3)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1 
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Add item in the Invoice")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_add_item(login):
    time.sleep(3)
    try:
        WebDriverWait(login, 15).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "overlay"))  # Adjust this class if needed
        )
        print("Overlay has disappeared.")
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/app-sidebar-menu[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]/div[1]/span[1]/span[1]/span[1]/img[1]"))
        ).click()

        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Token']"))
        )
        element.click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
            )
        ).send_keys("9207206005")

        time.sleep(3)

        # Store the patient's name after selecting it
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Id : 2']")
            )
        ).click()
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

        time.sleep(2)
        booking_number = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='fw-bold ng-star-inserted'])[1]"))
        )

        booking_id = booking_number.text


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
        ).click()

        time.sleep(3)
        invoice_card = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Invoices'])[1]"))
        )
        login.execute_script("arguments[0].click();", invoice_card)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

         # Capture the booking id on the invoice page for assertion
        invoice_booking_id = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='col-lg-3 col-md-6 invoice-detail-style d-flex text-start'])[1]"))
        ).text

        print(f"Expected booking id: '{booking_id}', Actual booking id: '{invoice_booking_id}'")

        # Assert that the patient's name matches
        assert invoice_booking_id.strip() == booking_id.strip(), f"Expected booking id '{booking_id.strip()}', but found '{invoice_booking_id.strip()}' on invoice."


        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Edit']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='svg-icon svg-icon-lg svg-icon-success']//*[name()='svg']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Add Procedure/']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Choose Procedure/Item']"))
        ).click()

        time.sleep(1)
        select_item = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'item5')]"))
        )
        login.execute_script("arguments[0].scrollIntoView();", select_item)
        select_item.click()
        
        login.implicitly_wait(3)
        wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add']"))
        ).click()

        time.sleep(2)
        update_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Update']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", update_button)
        update_button.click()

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

        time.sleep(2)
        payment_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", payment_button)
        payment_button.click()
        
        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)



        time.sleep(3)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1 
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Add Adhoc item in the Invoice")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_add_adhoc_item(login):
    time.sleep(3)
    try:
        WebDriverWait(login, 15).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "overlay"))  # Adjust this class if needed
        )
        print("Overlay has disappeared.")
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/app-sidebar-menu[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]/div[1]/span[1]/span[1]/span[1]/img[1]"))
        ).click()

        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Token']"))
        )
        element.click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
            )
        ).send_keys("9207206005")

        time.sleep(3)

        # Store the patient's name after selecting it
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Id : 2']")
            )
        ).click()
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

        time.sleep(2)
        booking_number = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='fw-bold ng-star-inserted'])[1]"))
        )

        booking_id = booking_number.text


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
        ).click()

        time.sleep(3)
        invoice_card = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Invoices'])[1]"))
        )
        login.execute_script("arguments[0].click();", invoice_card)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

         # Capture the booking id on the invoice page for assertion
        invoice_booking_id = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='col-lg-3 col-md-6 invoice-detail-style d-flex text-start'])[1]"))
        ).text

        print(f"Expected booking id: '{booking_id}', Actual booking id: '{invoice_booking_id}'")

        # Assert that the patient's name matches
        assert invoice_booking_id.strip() == booking_id.strip(), f"Expected booking id '{booking_id.strip()}', but found '{invoice_booking_id.strip()}' on invoice."


        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Edit']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='svg-icon svg-icon-lg svg-icon-success']//*[name()='svg']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Add Procedure/']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Choose Procedure/Item']"))
        ).send_keys("Adhoc-item")

        time.sleep(1)
        item_price = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@id='mat-input-4'])[2]"))
        )
        item_price.clear()
        item_price.send_keys("45")

        login.implicitly_wait(3)
        wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add']"))
        ).click()

        time.sleep(4)
        update_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Update']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", update_button)
        update_button.click()

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

        time.sleep(5)
        payment_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", payment_button)
        payment_button.click()
        
        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)



        time.sleep(3)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1 
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Add sub service in the Invoice")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_add_subservice(login):
    time.sleep(3)
    try:
        WebDriverWait(login, 15).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "overlay"))  # Adjust this class if needed
        )
        print("Overlay has disappeared.")
        
        time.sleep(3)
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//body/app-root[1]/app-business[1]/div[1]/app-sidebar-menu[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]/div[1]/span[1]/span[1]/span[1]/img[1]"))
        ).click()

        time.sleep(3)
        element = WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Token']"))
        )
        element.click()

        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter name or phone or id']")
            )
        ).send_keys("9207206005")

        time.sleep(3)

        # Store the patient's name after selecting it
        WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Id : 2']")
            )
        ).click()
        
        time.sleep(2)
        WebDriverWait(login, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "p-dropdown[optionlabel='place']"))
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

        time.sleep(2)
        booking_number = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='fw-bold ng-star-inserted'])[1]"))
        )

        booking_id = booking_number.text


        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
        ).click()

        time.sleep(3)
        invoice_card = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[normalize-space()='Invoices'])[1]"))
        )
        login.execute_script("arguments[0].click();", invoice_card)

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//span[contains(text(),'View')])[1]"))
        ).click()

         # Capture the booking id on the invoice page for assertion
        invoice_booking_id = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='col-lg-3 col-md-6 invoice-detail-style d-flex text-start'])[1]"))
        ).text

        print(f"Expected booking id: '{booking_id}', Actual booking id: '{invoice_booking_id}'")

        # Assert that the patient's name matches
        assert invoice_booking_id.strip() == booking_id.strip(), f"Expected booking id '{booking_id.strip()}', but found '{invoice_booking_id.strip()}' on invoice."


        time.sleep(2)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Edit']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='svg-icon svg-icon-lg svg-icon-success']//*[name()='svg']"))
        ).click()

        time.sleep(2)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Add Procedure/']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Choose Procedure/Item']"))
        ).click()

        time.sleep(1)
        select_subservice = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[normalize-space()='Naveen Consultation 1']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", select_subservice)
        select_subservice.click()

        login.implicitly_wait(3)
        wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add']"))
        ).click()

        time.sleep(2)
        update_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[normalize-space()='Update']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", update_button)
        update_button.click()

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

        time.sleep(2)
        payment_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"))
        )
        login.execute_script("arguments[0].scrollIntoView();", payment_button)
        payment_button.click()
        
        time.sleep(1)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Share Payment Link']"))
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='mdc-button__label']"))
        ).click()

        snack_bar = WebDriverWait(login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)



        time.sleep(3)
    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1 
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: Consumer taking prepayment booking")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/visionhospital/"])
def test_add_con_prepayment(con_login):
    global con_booking_id_1  
    time.sleep(5)
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
    try:
        clickable_book_now_button.click()
    except:
        con_login.execute_script("arguments[0].click();", clickable_book_now_button)
        # wait = WebDriverWait(login, 10)
    location_button = WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@class='deptName ng-star-inserted'][contains(text(),'Chavakkad')]",
            )
        )
    )
    location_button.click()

    # wait = WebDriverWait(login, 10)
    depart_button = WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@class='deptName ng-star-inserted'][normalize-space()='ENT']",
            )
        )
    )
    depart_button.click()

    # wait = WebDriverWait(login, 10)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Dr.Naveen KP')]")
        )
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[normalize-space()='Naveen service prepayment']",
            )
        )
    ).click()
    time.sleep(3)
    Today_Date = WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-pressed='true'][@aria-current='date']")
        )
    )
    con_login.execute_script("arguments[0].scrollIntoView(true);", Today_Date)
    time.sleep(2)
    Today_Date.click()
    time.sleep(2)
    print("Today Date:", Today_Date.text)
    wait = WebDriverWait(con_login, 10)
    queue = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='mdc-evolution-chip__cell mdc-evolution-chip__cell--primary']"))
    )
    con_login.execute_script("arguments[0].scrollIntoView(true);", queue)
    time.sleep(2)
    queue.click()
    print("Queue:", queue.text)
    time.sleep(2)
    next_button = WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Next']")
        )
    )
    con_login.execute_script("arguments[0].scrollIntoView(true);", next_button)
    time.sleep(3)
    next_button.click()
    time.sleep(3)  
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
    ).send_keys("9207206005") 

    con_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

    time.sleep(5)
    # otp_digits = "5555"
    otp_digits = "5555"
    # Wait for the OTP input fields to be present
    otp_inputs = WebDriverWait(con_login, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//input[contains(@id, 'otp_')]")
        )
    )
    for i, otp_input in enumerate(otp_inputs):
        otp_input.send_keys(otp_digits[i])

    con_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
    time.sleep(3)
    
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'NET BANKING')]")
        )
    ).click()

    time.sleep(3)
    # Scroll to the bottom of the page
    con_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    makepayment = WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//button[@type='button']//span[@class='mat-mdc-button-touch-target']",
            )
        )
    )
    # con_login.execute_script("arguments[0].scrollInView();", makepayment)
    con_login.execute_script("arguments[0].click();", makepayment)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[contains(@class,'ptm-paymode-name ptm-lightbold')]")
        )
    ).click()

    time.sleep(1)

    WebDriverWait(con_login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'SBI')]"))
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'ptm-overlay-wrapper btn-enabled')]//button[contains(@class,'')][contains(text(),'Pay ₹175')]",
            )
        )
    ).click()

    # Handle the popup window
    # Save the current window handle
    main_window_handle = con_login.current_window_handle

    # Wait until the new window is present
    WebDriverWait(con_login, 10).until(EC.new_window_is_opened)

    # Get all window handles
    all_window_handles = con_login.window_handles

    # Find the new window handle (the popup window)
    new_window_handle = None
    for handle in all_window_handles:
        if handle != main_window_handle:
            new_window_handle = handle
            break

    # Switch to the new window
    con_login.switch_to.window(new_window_handle)

    # Now interact with elements in the new window
    # For example, clicking the success button
    time.sleep(3)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='btn btnd']"))
    ).click()

    # Optionally, switch back to the main window

    con_login.switch_to.window(main_window_handle)
    # time.sleep(15)

    try:
        snack_bar = WebDriverWait(con_login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

    except:

        snack_bar = WebDriverWait(con_login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)


    time.sleep(3)

    con_booking_element = WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='bookingIdFlex ng-star-inserted']"))
    )

    bookings_id_number = con_login.find_element(By.XPATH, "//div[@class='bookingIdFlex ng-star-inserted']")
    full_texts = bookings_id_number.text
    con_booking_id_1 = full_texts.split(":")[1].strip()
    print("Consumer Booking ID:", con_booking_id_1)

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Ok']"))
    ).click()

    time.sleep(2)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='My Bookings']"))
    ).click()
    
    con_login.quit()
    # con_login.close()

     # Provider Login Section
    login_data = {'username': '5555556030', 'password': 'Jaldee01'}
    pro_driver = webdriver.Chrome(
        service=ChromeService(executable_path="Drivers/chromedriver-win64/chromedriver.exe")
    )

    pro_driver.get("https://scale.jaldee.com/business/")
    pro_driver.maximize_window()
    pro_driver.find_element(By.ID, "loginId").send_keys(login_data['username'])
    pro_driver.find_element(By.ID, "password").send_keys(login_data['password'])
    pro_driver.find_element(By.XPATH, "//div[@class='mt-2']").click()

    # # Ensure expected element is loaded on provider page
    # WebDriverWait(pro_driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//some_element_xpath"))
    # )
    # assert "Expected Element" in pro_driver.page_source

    time.sleep(3)
    WebDriverWait(pro_driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
    ).click()

    time.sleep(2)
    invoice_card1 = WebDriverWait(pro_driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='Invoices'])[1]"))

    )
    pro_driver.execute_script("arguments[0].click();", invoice_card1)
    
    WebDriverWait(pro_driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[contains(text(),'View')])[1]"))
    ).click()

        # Capture the booking id on the invoice page for assertion
    invoice_booking_id = WebDriverWait(pro_driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@class='col-lg-3 col-md-6 invoice-detail-style d-flex text-start'])[1]"))
    ).text

    print(f"Expected booking id: '{con_booking_id_1}', Actual booking id: '{invoice_booking_id}'")

    # Assert that the patient's name matches
    assert invoice_booking_id.strip() == con_booking_id_1.strip(), f"Expected booking id '{con_booking_id_1.strip()}', but found '{invoice_booking_id.strip()}' on invoice."
    wait = WebDriverWait(pro_driver, 20)
    time.sleep(3)
    payment_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-label p-inputtext p-placeholder ng-star-inserted'])[1]"))
    )
    pro_driver.execute_script("arguments[0].scrollIntoView();", payment_button)
    payment_button.click()
    
    time.sleep(1)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Share Payment Link']"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='mdc-button__label']"))
    ).click()

    snack_bar = WebDriverWait(pro_driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    )
    message = snack_bar.text
    print("Snack bar message:", message)

    time.sleep(3)
    


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: for donation")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/visionhospital/"])
def test_donation(con_login):
    # global con_booking_id_1  
    time.sleep(5)
    dontate_button = WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Donate']")
        )
    )
    con_login.execute_script("arguments[0].click();", dontate_button)
    
    
    
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
    ).send_keys("9207206005") 

    con_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

    time.sleep(5)
    # otp_digits = "5555"
    otp_digits = "5555"
    # Wait for the OTP input fields to be present
    otp_inputs = WebDriverWait(con_login, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//input[contains(@id, 'otp_')]")
        )
    )
    for i, otp_input in enumerate(otp_inputs):
        otp_input.send_keys(otp_digits[i])

    con_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()


    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='₹400 - ₹800']"))
    ).send_keys("500")
    
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//img[@src='assets/images/payment-modes/NB.png'])[1]"))
    ).click()


    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Proceed']"))
    ).click()

    # WebDriverWait(con_login, 10).until(
    #     EC.presence_of_element_located(By.XPATH, "//p[@class='ptm-paymode-name ptm-lightbold ']")
    # ).click()


    time.sleep(3)
    # # Scroll to the bottom of the page
    # con_login.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # makepayment = WebDriverWait(con_login, 10).until(
    #     EC.presence_of_element_located(
    #         (
    #             By.XPATH,
    #             "//button[@type='button']//span[@class='mat-mdc-button-touch-target']",
    #         )
    #     )
    # )
    # # con_login.execute_script("arguments[0].scrollInView();", makepayment)
    # con_login.execute_script("arguments[0].click();", makepayment)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[contains(@class,'ptm-paymode-name ptm-lightbold')]")
        )
    ).click()

    time.sleep(1)

    WebDriverWait(con_login, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'SBI')]"))
    ).click()

    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'ptm-overlay-wrapper btn-enabled')]//button[contains(@class,'')][contains(text(),'Pay ₹500')]",
            )
        )
    ).click()

    # Handle the popup window
    # Save the current window handle
    main_window_handle = con_login.current_window_handle

    # Wait until the new window is present
    WebDriverWait(con_login, 10).until(EC.new_window_is_opened)

    # Get all window handles
    all_window_handles = con_login.window_handles

    # Find the new window handle (the popup window)
    new_window_handle = None
    for handle in all_window_handles:
        if handle != main_window_handle:
            new_window_handle = handle
            break

    # Switch to the new window
    con_login.switch_to.window(new_window_handle)

    # Now interact with elements in the new window
    # For example, clicking the success button
    time.sleep(3)
    WebDriverWait(con_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='btn btnd']"))
    ).click()

    # Optionally, switch back to the main window

    con_login.switch_to.window(main_window_handle)
    # time.sleep(15)

    try:
        snack_bar = WebDriverWait(con_login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

    except:

        snack_bar = WebDriverWait(con_login, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
        )
        message = snack_bar.text
        print("Snack bar message:", message)

    
    
    time.sleep(3)
    
    con_login.quit()
    # con_login.close() 

     # Provider Login Section
    login_data = {'username': '5555556030', 'password': 'Jaldee01'}
    pro_driver = webdriver.Chrome(
        service=ChromeService(executable_path="Drivers/chromedriver-win64/chromedriver.exe")
    )

    pro_driver.get("https://scale.jaldee.com/business/")
    pro_driver.maximize_window()
    pro_driver.find_element(By.ID, "loginId").send_keys(login_data['username'])
    pro_driver.find_element(By.ID, "password").send_keys(login_data['password'])
    pro_driver.find_element(By.XPATH, "//div[@class='mt-2']").click()

    # # Ensure expected element is loaded on provider page
    # WebDriverWait(pro_driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//some_element_xpath"))
    # )
    # assert "Expected Element" in pro_driver.page_source

    time.sleep(3)
    WebDriverWait(pro_driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[6]//a[1]//div[1]//span[1]//span[1]//img[1]"))
    ).click()

    time.sleep(2)
    revenue_card1 = WebDriverWait(pro_driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='Revenue'])[1]"))

    )
    pro_driver.execute_script("arguments[0].click();", revenue_card1)
    
    # WebDriverWait(pro_driver, 10).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "(//span[contains(text(),'View')])[1]"))
    # ).click()
    time.sleep(2)
    # Wait for the table to be present
    table_body = WebDriverWait(pro_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
    )

    # Locate the first table row
    first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[2]")

    # Find the status element within the first row
    time.sleep(2)
    status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
    status_text = status_element.text
    expected_status = "New"

    print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

    # Assert that the status is "New"
    assert status_text == "New", f"Expected status to be 'New', but got '{status_text}'"

    WebDriverWait(pro_driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[@type='button'])[3]"))
    ).click()

    time.sleep(1)
    WebDriverWait(pro_driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='mdc-list-item__primary-text']"))
    ).click()

    WebDriverWait(pro_driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Approved')]"))
    ).click()

    time.sleep(2)
     # Wait for the table to be present
    table_body = WebDriverWait(pro_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//tbody"))
    )

    # Locate the first table row
    first_row = table_body.find_element(By.XPATH, "(//tr[@class='ng-star-inserted'])[2]")

    # Find the status element within the first row
    time.sleep(2)
    status_element = first_row.find_element(By.XPATH, './/span[contains(@class, "status-")]')
    status_text = status_element.text
    expected_status = "Approved"

    print(f"Expected status: '{expected_status}', Actual status: '{status_text}'")

    # Assert that the status is "APPROVED"
    assert status_text == "Approved", f"Expected status to be 'Approved', but got '{status_text}'"

    



    
