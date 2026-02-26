import time
import allure

from Framework.common_utils import *
from Framework.consumer_common_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Enable Sales Manager")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_sales_order_1(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login


        wait_and_locate_click(
            driver, By.XPATH, "//img[@src='./assets/images/menu/settings.png']"
        )

        time.sleep(2)
        order_option = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, order_option)

        time.sleep(1)

        wait_and_locate_click(
            driver, By.XPATH, "//span[contains(normalize-space(), 'Sales Order')]"
        )

        time.sleep(1)
        toggle = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[@role='switch'])[1]"))
        )

        # Get current state
        state = toggle.get_attribute("aria-checked")

        # If disabled, enable it
        if state == "false":
            toggle.click()
            print("Toggle was disabled. Now enabled.")
        else:
            print("Toggle already enabled. No action taken.")

        time.sleep(2)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Disable Sales Manager")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_sales_order_2(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login


        wait_and_locate_click(
            driver, By.XPATH, "//img[@src='./assets/images/menu/settings.png']"
        )

        time.sleep(2)
        order_option = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, order_option)

        time.sleep(1)

        wait_and_locate_click(
            driver, By.XPATH, "//span[contains(normalize-space(), 'Sales Order')]"
        )

        time.sleep(1)
        toggle_xpath = "(//button[@role='switch'])[1]"

        toggle = wait.until(
            EC.element_to_be_clickable((By.XPATH, toggle_xpath))
        )

        initial_state = toggle.get_attribute("aria-checked")

        if initial_state == "true":
            # Enabled → Disable
            toggle.click()

            wait.until(
                EC.text_to_be_present_in_element_attribute(
                    (By.XPATH, toggle_xpath),
                    "aria-checked",
                    "false"
                )
            )

            # Enable again
            toggle = wait.until(
                EC.element_to_be_clickable((By.XPATH, toggle_xpath))
            )
            toggle.click()

            wait.until(
                EC.text_to_be_present_in_element_attribute(
                    (By.XPATH, toggle_xpath),
                    "aria-checked",
                    "true"
                )
            )

            print("Enabled → Disabled → Enabled")

        elif initial_state == "false":
            # Disabled → Enable
            toggle.click()

            wait.until(
                EC.text_to_be_present_in_element_attribute(
                    (By.XPATH, toggle_xpath),
                    "aria-checked",
                    "true"
                )
            )

            # Disable
            toggle = wait.until(
                EC.element_to_be_clickable((By.XPATH, toggle_xpath))
            )
            toggle.click()

            wait.until(
                EC.text_to_be_present_in_element_attribute(
                    (By.XPATH, toggle_xpath),
                    "aria-checked",
                    "false"
                )
            )

            # Enable again
            toggle = wait.until(
                EC.element_to_be_clickable((By.XPATH, toggle_xpath))
            )
            toggle.click()

            wait.until(
                EC.text_to_be_present_in_element_attribute(
                    (By.XPATH, toggle_xpath),
                    "aria-checked",
                    "true"
                )
            )

            print("Disabled → Enabled → Disabled → Enabled")

        else:
            print("Unexpected toggle state:", initial_state)

        time.sleep(2)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Order Id prefix is setup for the account")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_sales_order_3(login):
    try:
        time.sleep(5)
        wait = WebDriverWait(login, 30)
        driver = login


        wait_and_locate_click(
            driver, By.XPATH, "//img[@src='./assets/images/menu/settings.png']"
        )

        time.sleep(2)
        order_option = driver.find_element(By.XPATH, "//div[normalize-space()='POS Ordering']")
        scroll_to_element(driver, order_option)

        time.sleep(1)

        wait_and_locate_click(
            driver, By.XPATH, "//span[contains(normalize-space(), 'Sales Order')]"
        )

        time.sleep(1)
        toggle_xpath = "(//button[@role='switch'])[1]"

        toggle = wait.until(
            EC.element_to_be_clickable((By.XPATH, toggle_xpath))
        )

        initial_state = toggle.get_attribute("aria-checked")

        if initial_state == "true":
            # Enabled → Disable
            toggle.click()

            wait.until(
                EC.text_to_be_present_in_element_attribute(
                    (By.XPATH, toggle_xpath),
                    "aria-checked",
                    "false"
                )
            )

            # Enable again
            toggle = wait.until(
                EC.element_to_be_clickable((By.XPATH, toggle_xpath))
            )
            toggle.click()

            wait.until(
                EC.text_to_be_present_in_element_attribute(
                    (By.XPATH, toggle_xpath),
                    "aria-checked",
                    "true"
                )
            )

            print("Enabled → Disabled → Enabled")

        elif initial_state == "false":
            # Disabled → Enable
            toggle.click()

            wait.until(
                EC.text_to_be_present_in_element_attribute(
                    (By.XPATH, toggle_xpath),
                    "aria-checked",
                    "true"
                )
            )

            # Disable
            toggle = wait.until(
                EC.element_to_be_clickable((By.XPATH, toggle_xpath))
            )
            toggle.click()

            wait.until(
                EC.text_to_be_present_in_element_attribute(
                    (By.XPATH, toggle_xpath),
                    "aria-checked",
                    "false"
                )
            )

            # Enable again
            toggle = wait.until(
                EC.element_to_be_clickable((By.XPATH, toggle_xpath))
            )
            toggle.click()

            wait.until(
                EC.text_to_be_present_in_element_attribute(
                    (By.XPATH, toggle_xpath),
                    "aria-checked",
                    "true"
                )
            )

            print("Disabled → Enabled → Disabled → Enabled")

        else:
            print("Unexpected toggle state:", initial_state)

        time.sleep(2)

        wait_and_locate_click(
            driver, By.XPATH, "//button[normalize-space()='Advanced Order Settings']"
        )

        prefix_element = driver.find_element(By.XPATH, "//input[@placeholder='Enter Invoice Number Prefix']")
        prefix_element.click()
        time.sleep(1)
        prefix_element.clear()
        prefix_element.send_keys("AB-")
        
        time.sleep(1)
        wait_and_locate_click(
            driver, By.XPATH, "//button[normalize-space()='Update Settings']"
        )

        msg = get_snack_bar_message(driver)
        print("Snack Bar Message :", msg)
        time.sleep(3)

    except Exception as e:
        allure.attach(
            login.get_screenshot_as_png(),
            name="full_page_error",
            attachment_type=AttachmentType.PNG,
        )
        raise e


    


    
    

