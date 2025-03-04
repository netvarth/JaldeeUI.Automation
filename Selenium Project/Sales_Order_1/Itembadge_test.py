
from Framework.common_utils import *
from Framework.common_dates_utils import *

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Provider Created Item Badge")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_create_Badge(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Items']") 
        time.sleep(2)
        while True:
            try: 
                next_button = WebDriverWait(login, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//angledoublerighticon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']"))
                )
                if next_button.is_enabled():
                    next_button.click()
                else:
                    break
            except Exception as e:
                print("Current item page is showing")
                break
        wait_and_locate_click(login, By.XPATH, "(//button[@class='p-element mat-mdc-menu-trigger btn fw-bold p-button-light p-button p-component'][normalize-space()='Actions'])[last()]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-label']") 
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//i[@class='fw-normal fa fa-pencil card p-2 shadow rounded-circle'])[1]") 
        time.sleep(2)
        current_working_directory = os.getcwd()
        absolute_path = os.path.abspath(
            os.path.join(current_working_directory, r"Extras\Dessert.jpeg")
        )
        pyautogui.write(absolute_path)
        pyautogui.press("enter")
        time.sleep(3)
        global badge_name
        badge_name = "Chocolates_" + ''.join(random.choices(string.ascii_letters, k=6)) 
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Badge Name']", badge_name)
        time.sleep(2)
        wait_and_send_keys(login, By.XPATH, "//input[@placeholder='Enter Badge Link']", "https://www.flurys.com/")
        time.sleep(2)
        global badge_link
        badge_link = "https://www.flurys.com/"
        wait_and_locate_click(login, By.XPATH, "//span[@class='p-button-label'][normalize-space()='Add Badge']") 
        time.sleep(2)
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(2)
        scroll_to_window(login)
        windows_before = login.window_handles
        print(f"Windows before clicking the link: {len(windows_before)}")
        wait_and_locate_click(login, By.XPATH, "//i[@class='fa fa-external-link pointer-cursor ng-star-inserted']") 
        time.sleep(2)
        windows_after = login.window_handles
        print(f"Windows after clicking the link: {len(windows_after)}")
        assert len(windows_after) == len(windows_before) + 1, "New Browser Tab is not open!"
        login.switch_to.window(windows_after[-1])
        current_url = login.current_url
        print(f"Expected_Itemurl : {badge_link} ; Current_Itemurl : {current_url}")
        assert current_url == badge_link, f"Redirect failed: expected {badge_link} but got {current_url}"
        login.close()
        login.switch_to.window(windows_before[0])
        time.sleep(2)
        # wait_and_locate_click(login, By.XPATH, "//i[@class='fa fa-external-link pointer-cursor ng-star-inserted']") 
        # time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  



from Framework.common_utils import *
@pytest.fixture()
def consumer_login():

    driver = webdriver.Chrome(
        service=ChromeService(
            executable_path=r"Drivers\chromedriver-win64\chromedriver.exe"
        )
    )
    driver.get("https://scale.jaldee.com/RangSweets")
    driver.maximize_window()
    yield driver
    driver.quit() 

  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Consumer Viewing the  Item_badge")
def test_view_itembadge(consumer_login):
    try:
        time.sleep(5)
        Dessert = WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Dessert')]"))
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", Dessert)
        time.sleep(5)
        Dessert.click()
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "//div[normalize-space()='Rasmalai']")
        time.sleep(2)
        wait_and_locate_click(consumer_login, By.XPATH, "//h4[normalize-space()='Product Credentials']")
        time.sleep(2)
        view_badge_name = wait_for_text(consumer_login, By.XPATH, "//span[@class='badge-name']")
        print(f"Provider created Item badge_name : {badge_name} ; Consumer viewable Item badge_name : {view_badge_name}")
        assert badge_name == view_badge_name, f"Provider created Item badge_name : {badge_name} ; but got Consumer viewable Item badge_name   : {view_badge_name}"
        time.sleep(2)
        windows_before = consumer_login.window_handles
        print(f"Windows before clicking the link: {len(windows_before)}")
        wait_and_locate_click(consumer_login, By.XPATH, "//i[@class='fa fa-external-link pointer-cursor ng-star-inserted']") 
        time.sleep(2)
        windows_after = consumer_login.window_handles
        print(f"Windows after clicking the link: {len(windows_after)}")
        assert len(windows_after) == len(windows_before) + 1, "New Browser Tab is not open!"
        consumer_login.switch_to.window(windows_after[-1])
        current_url = consumer_login.current_url
        print(f"Expected_Itemurl : {badge_link} ; Current_Itemurl : {current_url}")
        assert current_url == badge_link, f"Redirect failed: Expected_Itemurl {badge_link} but got Current_Itemurl {current_url}"
        consumer_login.close()
        consumer_login.switch_to.window(windows_before[0])
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            consumer_login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Provider deleted the Item_Badge")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_deleted_Badge(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[@class='my-1 font-small ng-star-inserted'][normalize-space()='Items']") 
        time.sleep(2)
        while True:
            try: 
                next_button = WebDriverWait(login, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//angledoublerighticon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']"))
                )
                if next_button.is_enabled():
                    next_button.click()
                else:
                    break
            except Exception as e:
                print("Current item page is showing")
                break
        wait_and_locate_click(login, By.XPATH, "(//button[@class='p-element mat-mdc-menu-trigger btn fw-bold p-button-light p-button p-component'][normalize-space()='Actions'])[last()]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "(//span[@class='mdc-list-item__primary-text'])[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//i[@class='fa fa-close']") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//button[normalize-space()='Yes']") 
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  