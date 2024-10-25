from Framework.common_utils import *



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: lead work flow")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_lead_workflow(login):

    try:
        wait = WebDriverWait(login, 10)
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Settings')]"))
        ).click()

        lead_suite = login.find_element(By.XPATH, "//div[normalize-space()='Lead Suite']")
        login.execute_script("arguments[0].scrollIntoView();", lead_suite)

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[normalize-space()='Manage Leads']"))
        ).click()
        time.sleep(1)

        # wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//div[@class='mdc-switch__icons']//*[name()='svg']"))
        # ).click()

        switch_icon = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='mdc-switch__ripple']"))
        )
        login.execute_script("arguments[0].click();", switch_icon)

        time.sleep(1)

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


    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e