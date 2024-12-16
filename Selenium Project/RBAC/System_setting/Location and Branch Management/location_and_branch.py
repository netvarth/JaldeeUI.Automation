import sys
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from Framework.common_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Basic user capabilities create location")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_location_checked(login):

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

    location_and_branch = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Location and Branch Management']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", location_and_branch)

    time.sleep(2)   
    create_location = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//mat-checkbox[.//label[normalize-space()='Create Locations']]//input[@type='checkbox']"))
    )

     

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
            (By.XPATH, "//img[@src='./assets/images/menu/settings.png']")
        ) 
    ).click()

    time.sleep(3)

    feature_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Features and Customization']"))
    )

    login.execute_script("arguments[0].scrollIntoView();", feature_button)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[normalize-space()='All the locations you operate from.']"))
    ).click()

    time.sleep(3)

    add_location_button = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[normalize-space()='Add Location']")
    ))

    # Assert its visibility
    assert add_location_button.is_displayed(), "Add Location button is not visible, but it should be when 'Create Location' is checked."
    print("Add Location button is visible.")

    add_location_button.click()

    time.sleep(2)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Choose your location in the MAP']"))
    ).click()

    time.sleep(3)

    try:
        # Locate the input field using XPath
        input_field = login.find_element(By.XPATH, "//input[@id='pac-input']")

        # Input "Thrissur" into the text field
        input_field.send_keys("Thrissur")
        time.sleep(3)

        # Wait for the suggestions to appear and select the appropriate one
        wait = WebDriverWait(login, 10)
        suggestions = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='pac-item']"))
        )

        time.sleep(3)

        # Iterate through the suggestions and select the one that matches "Thrissur, Kerala, India"
        for suggestion in suggestions:
            if "Thrissur, Kerala, India" in suggestion.text:
                suggestion.click()
                break

    finally:
        print("Loaction : Thrissur, Kerala, India")

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Basic user capabilities create location unchecked")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_location_unchecked(login):

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

    location_and_branch = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Location and Branch Management']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", location_and_branch)

    time.sleep(2)   
    create_location = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//mat-checkbox[.//label[normalize-space()='Create Locations']]//input[@type='checkbox']"))
    )

    is_checked = create_location.is_selected()
    print("is_checked:", is_checked)

    if is_checked:
        create_location.click()
        print("Unchecked 'Create Location' checkbox")
    else:
        print("'Create Location' checkbox is already unchecked")

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
            (By.XPATH, "//img[@src='./assets/images/menu/settings.png']")
        ) 
    ).click()

    time.sleep(3)

    feature_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Features and Customization']"))
    )

    login.execute_script("arguments[0].scrollIntoView();", feature_button)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[normalize-space()='All the locations you operate from.']"))
    ).click()

    time.sleep(3)

    # Verify the absence of the "Add Location" button
    add_location_buttons = login.find_elements(By.XPATH, "//span[normalize-space()='Add Location']")  # Use find_elements

    # Assert that the button is either not present or not visible
    assert len(add_location_buttons) == 0 or not add_location_buttons[0].is_displayed(), \
        "'Add Location' button is visible, but it should not be when 'Create Location' is unchecked."
    print("Add Location button is not visible as expected.")

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Basic user capabilities update locations checked")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_update_locations_checked(login):

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

    location_and_branch = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Location and Branch Management']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", location_and_branch)

    time.sleep(2)   
    create_location = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//mat-checkbox[.//label[normalize-space()='Update Locations']]//input[@type='checkbox']"))
    )

    is_checked = create_location.is_selected()
    print("is_checked:", is_checked)

    if is_checked:
        create_location.click()
        print("Unchecked 'Create Location' checkbox")
    else:
        print("'Create Location' checkbox is already unchecked")

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
            (By.XPATH, "//img[@src='./assets/images/menu/settings.png']")
        ) 
    ).click()

    time.sleep(3)

    feature_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[normalize-space()='Features and Customization']"))
    )

    login.execute_script("arguments[0].scrollIntoView();", feature_button)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[normalize-space()='All the locations you operate from.']"))
    ).click()

    time.sleep(3)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h3[normalize-space()='Vyttila']"))
    ).click()

    time.sleep(2)
    enable_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='mdc-switch__ripple']"))
    )
    login.execute_script("arguments[0].click();", enable_button)

