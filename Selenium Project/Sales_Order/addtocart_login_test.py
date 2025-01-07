from Framework.common_utils import *
from Framework.common_dates_utils import *

@pytest.mark.parametrize("url", ["https://scale.jaldeetest.in/business/"])
def test_providerlogin_addtocartlogin_disabled(login):
    time.sleep(2)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Settings')]"))
        ).click()
    time.sleep(2)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Add to Cart With Login']"))
        ).click()
    time.sleep(2)
    addcartlogin_togglebutton = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']")) 
            )
    aria_checked = addcartlogin_togglebutton.get_attribute("aria-checked")
    if aria_checked == "true":
        addcartlogin_togglebutton.click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)        
        time.sleep(2)
        aria_checked = addcartlogin_togglebutton.get_attribute("aria-checked")
        assert aria_checked == "false", "Add to Cart With Login toggle should be disabled."
    else:
        pass
    time.sleep(3)
    con_driver = webdriver.Chrome(
        service=ChromeService(
            executable_path=r"Drivers\chromedriver-win64\chromedriver.exe"
        )
    )
    con_driver.get("https://scale.jaldee.com/RangSweets")
    con_driver.maximize_window()
    time.sleep(2)
    Dessert = WebDriverWait(con_driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Dessert')]"))
        )
    con_driver.execute_script("arguments[0].scrollIntoView(true);", Dessert)
    time.sleep(2)    
    Dessert.click()
    time.sleep(3)
    wait_and_locate_click(con_driver, By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[1]")
    ptoast = WebDriverWait(con_driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@data-pc-section='detail']"))
                )                                 
    print("Toast_Message:", ptoast.text)
    try:
        time.sleep(2)
        WebDriverWait(con_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        )
        assert False, "Login page should not appear when toggle is disabled."
    except:
        cart_item = WebDriverWait(con_driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//span[@class='cart-count ng-star-inserted']"))
                )     
        print("Added_Cart_Item:", cart_item.text)
        assert cart_item, "Item was not added to the cart."
        print("Item successfully added to the cart without login.")
        cart_item.click()
    time.sleep(2)
    checkout = WebDriverWait(con_driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Checkout']"))
            )  
    checkout.click()
    time.sleep(2)
    try:
        WebDriverWait(con_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        )
        print("Login page appeared as expected after checkout.")
    except:
        assert False, "Login page did not appear after clicking checkout."
    time.sleep(2)
    

@pytest.mark.parametrize("url", ["https://scale.jaldeetest.in/business/"])
def test_providerlogin_addtocartlogin_enabled(login):
    time.sleep(2)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Settings')]"))
        ).click()
    time.sleep(2)
    WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Add to Cart With Login']"))
        ).click()
    time.sleep(2)
    addcartlogin_togglebutton = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@role='switch']")) 
            )
    aria_checked = addcartlogin_togglebutton.get_attribute("aria-checked")
    if aria_checked == "true":
        pass
    else:
        addcartlogin_togglebutton.click()
        message = get_snack_bar_message(login)
        print("Snack bar message:", message)        
        time.sleep(2)
        aria_checked = addcartlogin_togglebutton.get_attribute("aria-checked")
        assert aria_checked == "true", "Add to Cart With Login toggle should be enabled."
    time.sleep(3)
    con_driver = webdriver.Chrome(
        service=ChromeService(
            executable_path=r"Drivers\chromedriver-win64\chromedriver.exe"
        )
    )
    con_driver.get("https://scale.jaldee.com/RangSweets")
    con_driver.maximize_window()
    time.sleep(2)
    Dessert = WebDriverWait(con_driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Dessert')]"))
        )
    con_driver.execute_script("arguments[0].scrollIntoView(true);", Dessert)
    time.sleep(2)    
    Dessert.click()
    time.sleep(3)
    wait_and_locate_click(con_driver, By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[1]")
    
    try:
        time.sleep(2)
        WebDriverWait(con_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        )
        print("Login page appeared, which is expected.")
        assert True, "Login page should appear when toggle is enabled."
    except Exception as e:
        try:
            ptoast = WebDriverWait(con_driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@data-pc-section='detail']"))
                    )                                 
            print("Toast_Message:", ptoast.text)
            assert False, "Add to cart should not be available."
        except:
            print("Error: Login page did not appear, and no toast message was displayed.")
            assert False, "Neither login page nor toast message appeared when trying to add to cart."
    time.sleep(2)
    

