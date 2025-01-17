import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from Framework.common_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Basic user capabilities create patient group checked")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_patient_group_checked(login):

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

    Team_Group_Management = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Location and Branch Management']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", Team_Group_Management)

    time.sleep(2)   
    create_group = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//mat-checkbox[.//label[normalize-space()='Create Patient Group']]//input[@type='checkbox']"))
    )

    is_checked = create_group.is_selected()
    print("is_checked:",is_checked)

    if is_checked:
        pass
    else:
        create_group.click()
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

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//li[5]//a[1]//div[1]//span[1]//span[1]//img[1]")
        ) 
    ).click() 


    time.sleep(3)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//p-button[@class='p-element mat-mdc-menu-trigger mesg-btn add-btn']//span[@class='p-button-label ng-star-inserted'][normalize-space()='Add New']"))
    ).click()

    time.sleep(2)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='cdk-overlay-container']//button[2]//span[1]"))
    ).click()

    group_name = "group_"+ str(uuid.uuid4())[:4]

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='exampleInputPassword1']"))
    ).send_keys(group_name)


    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Create']"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Not Now']"))
    ).click()

    # try:

    #     snack_bar = WebDriverWait(login, 10).until(
    #         EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    #     )
    #     message = snack_bar.text
    #     print("Snack bar message:", message)

    # except:

    #     snack_bar = WebDriverWait(login, 10).until(
    #         EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
    #     )
    #     message = snack_bar.text
    #     print("Snack bar message:", message)



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Basic user capabilities create patient group unchecked")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_patient_group_unchecked(login):

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

    Team_Group_Management = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Team and Group Management']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", Team_Group_Management)

    time.sleep(2)   
    create_group = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//mat-checkbox[.//label[normalize-space()='Create Patient Group']]//input[@type='checkbox']"))
    )

    is_checked = create_group.is_selected()
    print("is_checked:", is_checked)

    if is_checked:
        create_group.click()
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
            (By.XPATH, "(//img)[5]"))
    ).click()

    time.sleep(2)

    add_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-button-label ng-star-inserted'][normalize-space()='Add New'])[1]"))
    )
    add_button.click()

    time.sleep(2)

    menu_options = WebDriverWait(login, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'mat-mdc-menu-content')]//button"))
    )

    displayed_options = [
    option.find_element(By.XPATH, ".//span[@class='mdc-list-item__primary-text']").text.strip()
    for option in menu_options
    ]

    print("Displayed Options:", displayed_options)

    # Assert only "Patient" option is displayed
    assert displayed_options == ["Patient"], f"Unexpected options displayed: {displayed_options}"
    print("Assertion passed: Only 'Patient' option is displayed.")

    time.sleep(3)



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Basic user capabilities view and updtate group unchecked")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_view_patient_group_unchecked(login):

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

    Team_Group_Management = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Team and Group Management']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", Team_Group_Management)

    time.sleep(2)   
   # List of checkboxes with their corresponding labels and XPATHs
    checkboxes = [
        ("Create Patient Group", "//mat-checkbox[.//label[normalize-space()='Create Patient Group']]//input[@type='checkbox']"),
        ("View Patient Group", "//mat-checkbox[.//label[normalize-space()='View Patient Group']]//input[@type='checkbox']"),
        ("Update Patient Group", "//mat-checkbox[.//label[normalize-space()='Update Patient Group']]//input[@type='checkbox']"),
        ("Add or Remove Patient to Group", "//mat-checkbox[.//label[normalize-space()='Add or Remove Patient to Group']]//input[@type='checkbox']")
    ]

    # Iterate through the checkboxes
    for label, xpath in checkboxes:
        # Locate the checkbox using its XPATH
        checkbox = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

        # Check if the checkbox is selected
        is_checked = checkbox.is_selected()
        print(f"'{label}' is_checked: {is_checked}")

        # Uncheck if it is currently selected
        if is_checked:
            checkbox.click()
            print(f"Unchecked '{label}' checkbox")
        else:
            print(f"'{label}' checkbox is already unchecked")
    
    time.sleep(3)   
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Save']")
        )
    ).click()

    time.sleep(3)
    yes_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Yes']")
        ))
    login.execute_script("arguments[0].click();", yes_button)


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
            (By.XPATH, "(//img)[5]"))
    ).click()

    time.sleep(2)

    add_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//span[@class='p-button-label ng-star-inserted'][normalize-space()='Add New'])[1]"))
    )
    add_button.click()

    time.sleep(2)

    menu_options = WebDriverWait(login, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'mat-mdc-menu-content')]//button"))
    )

    displayed_options = [
    option.find_element(By.XPATH, ".//span[@class='mdc-list-item__primary-text']").text.strip()
    for option in menu_options
    ]

    print("Displayed Options:", displayed_options)

    # Assert only "Patient" option is displayed
    assert displayed_options == ["Patient"], f"Unexpected options displayed: {displayed_options}"
    print("Assertion passed: Only 'Patient' option is displayed.")

    time.sleep(3)


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Basic user capabilities remove patient from group unchecked")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_remove_patient_group_unchecked(login):

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

    Team_Group_Management = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Team and Group Management']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", Team_Group_Management)

    time.sleep(2)   
    create_group = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//mat-checkbox[.//label[normalize-space()='Add or Remove Patient to Group']]//input[@type='checkbox']"))
    )

    is_checked = create_group.is_selected()
    print("is_checked:", is_checked)

    if is_checked:
        create_group.click()
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
            (By.XPATH, "(//img)[5]"))
    ).click()

    time.sleep(3)
    group_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Groups']"))
    )
    login.execute_script("arguments[0].click();", group_button)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='disp-flex']//div//span[@class='cust-name'][normalize-space()='group_9d53']"))
    ).click()

    time.sleep(3)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//input[@name='Checkboxes4'])[1]"))
    ).click()

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "(//img[@class='label-all'])[1]"))
    ).click()

    time.sleep(2)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Yes']"))
    ).click()

    Permission_error = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='mat-mdc-snack-bar-label mdc-snackbar__label']"))
    )

    permission_error_message = Permission_error.text
    print("Permission error message:", permission_error_message)

    # Assert the expected message
    expected_message = "Sorry! You have no permission to process this request!!!"
    assert permission_error_message == expected_message, f"Unexpected error message: {permission_error_message}"

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Basic user capabilities remove patient from group checked")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_remove_patient_group_checked(login):

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

    Team_Group_Management = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Team and Group Management']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", Team_Group_Management)

    time.sleep(2)   
    create_group = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//mat-checkbox[.//label[normalize-space()='Add or Remove Patient to Group']]//input[@type='checkbox']"))
    )

    is_checked = create_group.is_selected()
    print("is_checked:",is_checked)

    if is_checked:
        pass
    else:
        create_group.click()
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
            (By.XPATH, "(//img)[5]"))
    ).click()

    time.sleep(3)
    group_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Groups']"))
    )
    login.execute_script("arguments[0].click();", group_button)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='disp-flex']//div//span[@class='cust-name'][normalize-space()='group_9d53']"))
    ).click()

    time.sleep(3)
    checkbox = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//input[@name='Checkboxes4'])[1]"))
    )
    login.execute_script("arguments[0].click();", checkbox)

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "(//img[@class='label-all'])[1]"))
    ).click()

    time.sleep(2)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Yes']"))
    ).click()

    print("Patient removed successfully")
    time.sleep(2)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[@class='pointer-cursor ng-star-inserted'])[1]"))
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//input[@name='Checkboxes4'])[2]"))
    ).click()

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "(//span[normalize-space()='Add'])[1]"))
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


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Basic user capabilities remove patient from group unchecked")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_label_unchecked(login):

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

    Team_Group_Management = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[normalize-space()='Team and Group Management']"))
    )
    login.execute_script("arguments[0].scrollIntoView();", Team_Group_Management)

    time.sleep(2)   
    create_label = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//mat-checkbox[.//label[normalize-space()='Create Patient Label']]//input[@type='checkbox']"))
    )

    is_checked = create_label.is_selected()
    print("is_checked:", is_checked)

    if is_checked:
        create_label.click()
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
            (By.XPATH, "(//img)[5]"))
    ).click()

    time.sleep(3)

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, ""))
    )