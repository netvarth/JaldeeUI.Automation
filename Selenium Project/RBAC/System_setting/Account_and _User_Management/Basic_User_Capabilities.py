import sys
import os

# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from Framework.common_utils import *


# from Framework.common_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Basic user capabilities (View Account Profile)")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_view_account_profile_enable(login):

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

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h2[normalize-space()='Roles']"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[contains(text(),'Role Settings')])[1]"))
    ).click()

    # wait.until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "//label[normalize-space()='View Account Profile']"))
    # ).click()

    # Check if the checkbox is checked
    checked_xpath = "(//input[contains(@class, 'mdc-checkbox--selected') and @class='mdc-checkbox__native-control'])[1]"
    unchecked_xpath = "(//input[not(contains(@class, 'mdc-checkbox--selected')) and @class='mdc-checkbox__native-control'])[1]"

    is_checked = len(login.find_elements("xpath", checked_xpath)) > 0
    is_unchecked = len(login.find_elements("xpath", unchecked_xpath)) > 0

    # Assert the state
    assert is_checked or is_unchecked, "Checkbox is neither checked nor unchecked!"
    if is_checked:
        print("The checkbox is checked.")
    elif is_unchecked:
        print("The checkbox is unchecked.")

    home_button = WebDriverWait(login, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@id='kt_quick_user_toggle']//span[contains(@class, 'bname')]")
        ))
        
    login.execute_script("arguments[0].click();", home_button)

    time.sleep(2)
    signout_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[normalize-space()='Sign Out']"))
    )
    login.execute_script("arguments[0].click();", signout_button)

    print("Login with basic user")
    time.sleep(5)
    login_id = login.find_element(By.XPATH, "//input[@id='loginId']")
    login_id.clear()
    login_id.send_keys("praven@0291")

    password = login.find_element(By.XPATH, "//input[@id='password']")
    password.clear()
    password.send_keys("Jaldee01")

    login.find_element(By.XPATH,"//button[@type='submit']").click()

    time.sleep(3)

       
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Basic user capabilities (View Account Profile)")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_view_account_profile_disable(login):

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

    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h2[normalize-space()='Roles']"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[contains(text(),'Role Settings')])[1]"))
    ).click()

    time.sleep(3)

    select_option = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//input[@id='mat-mdc-checkbox-3-input'])[1]"))
    )

    login.execute_script("arguments[0].click();", select_option)

    time.sleep(3)
    # Check if the checkbox is checked
    checked_xpath = "(//input[contains(@class, 'mdc-checkbox--selected') and @class='mdc-checkbox__native-control'])[1]"
    unchecked_xpath = "(//input[not(contains(@class, 'mdc-checkbox--selected')) and @class='mdc-checkbox__native-control'])[1]"

    is_checked = len(login.find_elements("xpath", checked_xpath)) > 0
    is_unchecked = len(login.find_elements("xpath", unchecked_xpath)) > 0

    # Assert the state
    assert is_checked or is_unchecked, "Checkbox is neither checked nor unchecked!"
    if is_checked:
        print("The checkbox is checked.")
    elif is_unchecked:
        print("The checkbox is unchecked.")
    
    
    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Save']"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Yes']" ))
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


    time.sleep(2)

    home_button = WebDriverWait(login, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@id='kt_quick_user_toggle']//span[contains(@class, 'bname')]")
        ))
        
    login.execute_script("arguments[0].click();", home_button)

    time.sleep(2)
    signout_button = WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[normalize-space()='Sign Out']"))
    )
    login.execute_script("arguments[0].click();", signout_button)

    print("Login with basic user")
    time.sleep(5)
    login_id = login.find_element(By.XPATH, "//input[@id='loginId']")
    login_id.clear()
    login_id.send_keys("praven@0291")

    password = login.find_element(By.XPATH, "//input[@id='password']")
    password.clear()
    password.send_keys("Jaldee01")

    login.find_element(By.XPATH,"//button[@type='submit']").click()


    time.sleep(3)

    
    


    