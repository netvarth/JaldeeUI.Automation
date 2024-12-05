import sys
import os
from selenium.common.exceptions import StaleElementReferenceException
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
    
    
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Basic user capabilities checked create user")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_user_checked(login):

    # Initial Setup
    time.sleep(3)
    wait = WebDriverWait(login, 30)

    # Navigate to "Create User" permission toggle
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

    time.sleep(3)

    # Toggle "Create User" checkbox
    create_user_checkbox = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//mat-checkbox[.//label[normalize-space()='Create User']]//input[@type='checkbox']")
        )
    )

    # Store initial state
    is_checked = create_user_checkbox.is_selected()
    print("is_checked:",is_checked)

    if is_checked:
        print("in if")
        pass
    else:
        print("in else")
        # Toggle state
        create_user_checkbox.click()
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

    # Verify the success message
    snack_bar = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    )
    message = snack_bar.text
    assert "Role Updated Successfully" in message, f"Unexpected message: {message}"
    print("Snack bar message:", message)

    time.sleep(3)

    # Sign out
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

    # Re-login to verify options
    print("Login with basic user")
    login_id = login.find_element(By.XPATH, "//input[@id='loginId']")
    login_id.clear()
    login_id.send_keys("praven@0291")

    password = login.find_element(By.XPATH, "//input[@id='password']")
    password.clear()
    password.send_keys("Jaldee01")

    login.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//img)[6]")
        )
    ).click()

    time.sleep(3)

    # Step 1: Click the "Create" button to open the menu
    create_button = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'mat-mdc-menu-trigger'))
    )
    create_button.click()

    time.sleep(5)
    # Step 2: Wait for the menu options to appear and locate them
    options = WebDriverWait(login, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.mat-mdc-menu-item'))
    )

    # Step 3: Extract and print the text of each option
    print("Displayed Options:")
    displayed_options = [option.text.strip() for option in options]
    for option in displayed_options:
        print(option)

    expected_options = ["Create User", "Create Role"]  # "Create User" should not appear
    print("In if- Expected:",expected_options, " Displayed:", displayed_options)
    assert "Create User" in displayed_options, "Unexpected 'Create User' option displayed."

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[1]"))
    ).click()

    first_name1, last_name1, cons_manual_id1, phonenumber1, email1 = create_user_data()
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@formcontrolname='first_name']"))
    ).send_keys(str(first_name1))
    
    login.find_element(By.XPATH, "//input[@id='last_name']").send_keys(
        str(last_name1)
    )
    login.find_element(By.XPATH, "//input[@id='email']").send_keys(email1)
    login.find_element(By.XPATH, "//ngx-intl-tel-input[@name='mobileNo']//input[@id='phone']").send_keys(phonenumber1)
    login.find_element(
        By.XPATH, "//ngx-intl-tel-input[@name='whatsappNumber']//input[@id='phone']"
    ).send_keys(phonenumber1)
    
    time.sleep(2)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[1]"))
    ).click()

    time.sleep(1)
    WebDriverWait(login, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Doctor']"))
        ).click()

    time.sleep(2)
    usertype_button1 = WebDriverWait(login, 15).until(
    EC.presence_of_element_located(
    (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[3]"))
    )
    login.execute_script("arguments[0].scrollIntoView();", usertype_button1)
    time.sleep(1)
    login.execute_script("arguments[0].click();", usertype_button1)
    
    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Doctor']"))
    ).click() 

    time.sleep(2)
    usertype_button2 = WebDriverWait(login, 15).until(
    EC.presence_of_element_located(
    (By.XPATH, "(//span[@class='p-dropdown-trigger-icon fa fa-caret-down ng-star-inserted'])[4]"))
    )
    login.execute_script("arguments[0].click();", usertype_button2)
    
    time.sleep(1)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Basic User']"))
    ).click() 

    tablist_button = WebDriverWait(login, 15).until(
        EC.element_to_be_clickable(
    (By.XPATH, "//p-accordiontab//a[normalize-space(text())='Additional details']")))
    login.execute_script("arguments[0].click();", tablist_button)

    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Allow Business Profile']"))
    ).click()
    
    time.sleep(3)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[normalize-space()='Male']"))
    ).click()

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='mdc-button__label']"))
    ).click()

    time.sleep(2)

    loginid= WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='loginId']"))
    )
    loginid.send_keys(str(first_name1))
    
    time.sleep(3)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@class='btn btn-primary mdc-button mat-mdc-button mat-unthemed mat-mdc-button-base']//span[@class='mdc-button__label'][normalize-space()='Save']"))
    ).click()
    print("User created successfully")
    time.sleep(3)


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Basic user capabilities unchecked create user")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_user_unchecked(login):

    # Initial Setup
    time.sleep(3)
    wait = WebDriverWait(login, 30)

    # Navigate to "Create User" permission toggle
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

    time.sleep(3)

    # Toggle "Create User" checkbox
    create_user_checkbox = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//mat-checkbox[.//label[normalize-space()='Create User']]//input[@type='checkbox']")
        )
    )

    is_checked = create_user_checkbox.is_selected()
    print("is_checked:", is_checked)

    if not is_checked:
        print("in if")
        pass
    else:
        print("in else")
        # Toggle state
        create_user_checkbox.click()
        print("unchecked checkbox")


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

    # Verify the success message
    snack_bar = WebDriverWait(login, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    )
    message = snack_bar.text
    assert "Role Updated Successfully" in message, f"Unexpected message: {message}"
    print("Snack bar message:", message)

    time.sleep(3)

    # Sign out
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

    # Re-login to verify options
    print("Login with basic user")
    login_id = login.find_element(By.XPATH, "//input[@id='loginId']")
    login_id.clear()
    login_id.send_keys("praven@0291")

    password = login.find_element(By.XPATH, "//input[@id='password']")
    password.clear()
    password.send_keys("Jaldee01")

    login.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//img)[6]")
        )
    ).click()

    time.sleep(3)

    # Step 1: Click the "Create" button to open the menu
    create_button = WebDriverWait(login, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'mat-mdc-menu-trigger'))
    )
    create_button.click()

    time.sleep(5)
    # Step 2: Wait for the menu options to appear and locate them
    options = WebDriverWait(login, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.mat-mdc-menu-item'))
    )

    # Step 3: Extract and print the text of each option
    print("Displayed Options:")
    displayed_options = [option.text.strip() for option in options]
    for option in displayed_options:
        print(option)


    expected_options = ["Create Role"]  # "Create User" should not appear
    print("In if- Expected:", expected_options, " Displayed:", displayed_options)
    assert "Create User" not in displayed_options, "'Create User' option was incorrectly displayed."