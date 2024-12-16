import sys
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from Framework.common_utils import *



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Basic user update notification setting")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])

def test_update_notification_checked(login):

    time.sleep(3)
    wait = WebDriverWait(login, 30)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[@src='./assets/images/menu/settings.png']")
        )
    ).click()

    time.sleep(3)
    feature_setting = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Features and Customization']")
        )
    )
    login.execute_script("arguments[0].scrollIntoView();", feature_setting)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='RBAC']")
        )
    ).click()

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h2[normalize-space()='Roles']")
        )
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[contains(text(),'Role Settings')])[1]")
        )
    ).click()

    notifictaion_and_comunication = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Notification and Communication']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", notifictaion_and_comunication)

    time.sleep(2)   
    update_notification_setting = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//mat-checkbox[.//label[normalize-space()='Update Notification Settings']]//input[@type='checkbox']"))
    )

    is_checked = update_notification_setting.is_selected()
    print("is_checked:",is_checked)

    if is_checked:
        pass
    else:
        update_notification_setting.click()
        print("clicked checkbox")

    time.sleep(3)   
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Save']")
        )
    ).click()

    time.sleep(3)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Yes']")
        )
    ).click()


    snack_bar = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    )
    message = snack_bar.text
    assert "Role Updated Successfully" in message, f"Unexpected message: {message}"
    print("Snack bar message:", message)

    home_button = WebDriverWait(login, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@id='kt_quick_user_toggle']//span[contains(@class, 'bname')]")
        )
    )
    login.execute_script("arguments[0].click();", home_button)

    time.sleep(2)
    signout_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Sign Out']"))
    )
    login.execute_script("arguments[0].click();", signout_button)


    print("Login with basic user")
    login_id = login.find_element(By.XPATH, "//input[@id='loginId']")
    login_id.clear()
    login_id.send_keys("praven@0291")

    password = login.find_element(By.XPATH, "//input[@id='password']")
    password.clear()
    password.send_keys("Jaldee01")

    login.find_element(By.XPATH, "//button[@type='submit']").click()  
    time.sleep(3)


