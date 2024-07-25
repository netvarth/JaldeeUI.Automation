from ...Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.common import TimeoutException

@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_history_followup_sameday(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
            )
        )
    ).click()
    login.implicitly_wait(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@id='pr_id_7_label']//span[@class='ng-star-inserted']")
        )
    ).click()
    time.sleep(3)
    # *******Navigate to history bookings************
    history_button = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='History']"))
    )
    history_button.click()
    time.sleep(3)
    # *****Open filter options and Enter booking ID and apply filter*******
    filter_button = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='pi pi-filter-fill']"))
    )
    filter_button.click()
    time.sleep(3)
    booking_id_option = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[contains(@class, 'p-accordion-header-text') and contains(text(), 'Booking Id')]",
            )
        )
    )
    booking_id_option.click()
    time.sleep(3)
    booking_id_input = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='checkinEncId']"))
    )
    booking_id_input.send_keys("c-33b98s2-k0")
    time.sleep(3)
    filter_apply_button = WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Apply']"))
    )
    filter_apply_button.click()
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
    login.execute_script(
        "arguments[0].scrollIntoView(true);", last_element_in_accordian
    )
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")
        )
    ).click()
    time.sleep(5)
    print("ViewDetails Button Clicked")
    # # **** FollowUp for History Bookings *****
    follow_up_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Follow Up']")
        )
    )
    follow_up_button.click()
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
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
        )
    ).click()
    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='pi pi-filter-fill']"))
    ).click()
    time.sleep(3)
    filter_reset_button = WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Reset']"))
    )
    filter_reset_button.click()
    time.sleep(3)
    filter_close = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//*[name()='svg'][@class='p-icon p-sidebar-close-icon'])")
        )
    )
    filter_close.click()
    time.sleep(3)


@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_history_followup_tomorrow(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
            )
        )
    ).click()
    login.implicitly_wait(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@id='pr_id_7_label']//span[@class='ng-star-inserted']")
        )
    ).click()
    time.sleep(3)
    # *******Navigate to history bookings************
    history_button = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='History']"))
    )
    history_button.click()
    time.sleep(3)
    # *****Open filter options and Enter booking ID and apply filter*******
    filter_button = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='pi pi-filter-fill']"))
    )
    filter_button.click()
    time.sleep(3)
    booking_id_option = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[contains(@class, 'p-accordion-header-text') and contains(text(), 'Booking Id')]",
            )
        )
    )
    booking_id_option.click()
    time.sleep(3)
    booking_id_input = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='checkinEncId']"))
    )
    booking_id_input.send_keys("c-33b98s2-k0")
    time.sleep(3)
    filter_apply_button = WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Apply']"))
    )
    filter_apply_button.click()
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
    login.execute_script(
        "arguments[0].scrollIntoView(true);", last_element_in_accordian
    )
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")
        )
    ).click()
    time.sleep(5)
    print("ViewDetails Button Clicked")
    # # **** FollowUp for History Bookings *****
    follow_up_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Follow Up']")
        )
    )
    follow_up_button.click()
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
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
        )
    ).click()
    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='pi pi-filter-fill']"))
    ).click()
    time.sleep(3)
    filter_reset_button = WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Reset']"))
    )
    filter_reset_button.click()
    time.sleep(3)
    filter_close = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//*[name()='svg'][@class='p-icon p-sidebar-close-icon'])")
        )
    )
    filter_close.click()
    time.sleep(3)

@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_history_followup_previousday(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
            )
        )
    ).click()
    login.implicitly_wait(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@id='pr_id_7_label']//span[@class='ng-star-inserted']")
        )
    ).click()
    time.sleep(3)
    # *******Navigate to history bookings************
    history_button = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='History']"))
    )
    history_button.click()
    time.sleep(3)
    # *****Open filter options and Enter booking ID and apply filter*******
    filter_button = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='pi pi-filter-fill']"))
    )
    filter_button.click()
    time.sleep(3)
    booking_id_option = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[contains(@class, 'p-accordion-header-text') and contains(text(), 'Booking Id')]",
            )
        )
    )
    booking_id_option.click()
    time.sleep(3)
    booking_id_input = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='checkinEncId']"))
    )
    booking_id_input.send_keys("c-33b98s2-k0")
    time.sleep(3)
    filter_apply_button = WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Apply']"))
    )
    filter_apply_button.click()
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
    login.execute_script(
        "arguments[0].scrollIntoView(true);", last_element_in_accordian
    )
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")
        )
    ).click()
    time.sleep(5)
    print("ViewDetails Button Clicked")
    # # **** FollowUp for History Bookings *****
    follow_up_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Follow Up']")
        )
    )
    follow_up_button.click()
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
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
        )
    ).click()
    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='pi pi-filter-fill']"))
    ).click()
    time.sleep(3)
    filter_reset_button = WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Reset']"))
    )
    filter_reset_button.click()
    time.sleep(3)
    filter_close = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//*[name()='svg'][@class='p-icon p-sidebar-close-icon'])")
        )
    )
    filter_close.click()
    time.sleep(3)


@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_history_followup_nextmonth(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
            )
        )
    ).click()
    login.implicitly_wait(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@id='pr_id_7_label']//span[@class='ng-star-inserted']")
        )
    ).click()
    time.sleep(3)
    # *******Navigate to history bookings************
    history_button = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='History']"))
    )
    history_button.click()
    time.sleep(3)
    # *****Open filter options and Enter booking ID and apply filter*******
    filter_button = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='pi pi-filter-fill']"))
    )
    filter_button.click()
    time.sleep(3)
    booking_id_option = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[contains(@class, 'p-accordion-header-text') and contains(text(), 'Booking Id')]",
            )
        )
    )
    booking_id_option.click()
    time.sleep(3)
    booking_id_input = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='checkinEncId']"))
    )
    booking_id_input.send_keys("c-33b98s2-k0")
    time.sleep(3)
    filter_apply_button = WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Apply']"))
    )
    filter_apply_button.click()
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
    login.execute_script(
        "arguments[0].scrollIntoView(true);", last_element_in_accordian
    )
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")
        )
    ).click()
    time.sleep(5)
    print("ViewDetails Button Clicked")
    # # **** FollowUp for History Bookings *****
    follow_up_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Follow Up']")
        )
    )
    follow_up_button.click()
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
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
        )
    ).click()
    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='pi pi-filter-fill']"))
    ).click()
    time.sleep(3)
    filter_reset_button = WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Reset']"))
    )
    filter_reset_button.click()
    time.sleep(3)
    filter_close = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//*[name()='svg'][@class='p-icon p-sidebar-close-icon'])")
        )
    )
    filter_close.click()
    time.sleep(3) 

    
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_history_followup_futuredays(login):
    time.sleep(5)
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//img[contains(@src, 'tokens.gif')]//following::div[@class='my-1 font-small ng-star-inserted']//span[normalize-space(text())='Tokens']",
            )
        )
    ).click()
    login.implicitly_wait(5)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@id='pr_id_7_label']//span[@class='ng-star-inserted']")
        )
    ).click()
    time.sleep(3)
    # *******Navigate to history bookings************
    history_button = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='History']"))
    )
    history_button.click()
    time.sleep(3)
    # *****Open filter options and Enter booking ID and apply filter*******
    filter_button = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='pi pi-filter-fill']"))
    )
    filter_button.click()
    time.sleep(3)
    booking_id_option = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[contains(@class, 'p-accordion-header-text') and contains(text(), 'Booking Id')]",
            )
        )
    )
    booking_id_option.click()
    time.sleep(3)
    booking_id_input = WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='checkinEncId']"))
    )
    booking_id_input.send_keys("c-33b98s2-k0")
    time.sleep(3)
    filter_apply_button = WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Apply']"))
    )
    filter_apply_button.click()
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
    login.execute_script(
        "arguments[0].scrollIntoView(true);", last_element_in_accordian
    )
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='View Details']")
        )
    ).click()
    time.sleep(5)
    print("ViewDetails Button Clicked")
    # # **** FollowUp for History Bookings *****
    follow_up_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Follow Up']")
        )
    )
    follow_up_button.click()
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
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='fa fa-arrow-left pointer-cursor']")
        )
    ).click()
    time.sleep(3)
    WebDriverWait(login, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='pi pi-filter-fill']"))
    ).click()
    time.sleep(3)
    filter_reset_button = WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Reset']"))
    )
    filter_reset_button.click()
    time.sleep(3)
    filter_close = WebDriverWait(login, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//*[name()='svg'][@class='p-icon p-sidebar-close-icon'])")
        )
    )
    filter_close.click()
    time.sleep(3) 
    