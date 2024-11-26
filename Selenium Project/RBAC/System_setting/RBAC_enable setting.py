
from Framework.common_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Enabling the RBAC setting")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_enable_rbac(login):

    time.sleep(3)

    wait = WebDriverWait(login, 30)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//img[@src='./assets/images/menu/settings.png']"))
    ).click()

    time.sleep(3)
    feature_setting = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Features and Customization']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", feature_setting)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='RBAC']"))
    ).click()

    time.sleep(3)
    enable_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@class='mdc-switch__ripple'])[1]"))
    )
    login.execute_script("arguments[0].click();", enable_button)


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
    enable_button1 = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@class='mdc-switch__ripple'])[2]"))
    )
    login.execute_script("arguments[0].click();", enable_button1)

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
    enable_button2 = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@class='mdc-switch__ripple'])[3]"))
    )
    login.execute_script("arguments[0].click();", enable_button2)
   
    
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










