
from Framework.common_utils import *


@pytest.fixture()
def consumer_login():

    driver = webdriver.Chrome(
        service=ChromeService(
            executable_path=r"Drivers\chromedriver-win64\chromedriver.exe"
        )
    )
    driver.get("https://www.jaldee.com/02s7i59")
    driver.maximize_window()
    yield driver
    driver.quit() 

def create_consumer_data():
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    random_digits = fake.numerify(text="#######")
    phonenumber = f"555{random_digits}"
    test_email = "@jaldee.com"
    email = f"{first_name}.{last_name}{test_email}"

    return {
        "first_name": first_name,
        "last_name": last_name,
        "phonenumber": phonenumber,
        "email": email,
        "otp": "55555"  
    }

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create_Online_Order")
def test_create_Online_order(consumer_login):
    try:
        time.sleep(5)
        global consumer_data
        consumer_data = create_consumer_data()
        # Dessert = WebDriverWait(consumer_login, 20).until(
        #     EC.presence_of_element_located((By.XPATH, "//div[@class='category-name d-flex justify-content-between'][normalize-space()='Dessert']"))
        # )
        Dessert = WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Dessert')]"))
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", Dessert)
        time.sleep(5)
        Dessert.click()
        time.sleep(3)
        wait_and_locate_click(consumer_login, By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[2]")
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        ).send_keys(consumer_data['phonenumber'])
        print("New Consumer Phone Number:", consumer_data['phonenumber'])
        consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        time.sleep(5)
        otp_inputs = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//input[contains(@id, 'otp_')]")
            )
        )
        for i, otp_input in enumerate(otp_inputs):
            otp_input.send_keys(consumer_data['otp'][i])
        consumer_login.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()
        time.sleep(3)
        WebDriverWait(consumer_login, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@id='first_name'])[1]"))
        ).send_keys(consumer_data['first_name'])
        print("New Consumer Firstname:", consumer_data['first_name'])
        WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@id='first_name'])[2]"))
        ).send_keys(consumer_data['last_name'])
        print("New Consumer Lastname:", consumer_data['last_name'])
        consumer_login.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        time.sleep(5)
        # Verify item is added to cart
        print("Toast Message: Item added to cart")
        global cart_item_counts
        cart_item_count = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='cart-count ng-star-inserted']"))
        )
        cart_item_counts = cart_item_count.text
        print ("cart_Added_item_counts :",cart_item_counts)
        assert int(cart_item_counts) > 0, "Cart is empty. Item not added successfully."
        cart_item_count.click()
        time.sleep(3)
        global cart_item_name
        cart_item_names = WebDriverWait(consumer_login, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='fw-bold item-name']"))
        )
        cart_item_name = cart_item_names.text
        print("Added_cart_item_name :",cart_item_name)
        time.sleep(2)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  
    
from Framework.common_utils import *
from Framework.common_dates_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Active Carts")
@pytest.mark.parametrize("url", ["https://www.jaldee.com/business"])
def test_activecarts(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//div[contains(text(),'Active Cart')]")
        time.sleep(3)
        scroll_to_window(login)
        time.sleep(3)
        while True:
            try:
                next_button = WebDriverWait(login, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//angledoublerighticon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']"))
                )
                next_button.click()
                time.sleep(3)
            except:
                print("EC Caught:Next button not found or clicked.")
                break
        # Locate the last added cart item (most recent)
        recent_added_cart_element = WebDriverWait(login, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//tr[@class='mobile-card ng-star-inserted'])[last()]"))
        )

        # Extract details of the last item in the cart
        expected_item_name = recent_added_cart_element.find_element(By.XPATH, "./td[1]").text
        print(f"Expected Item Name: {expected_item_name}")

        expected_consumer_name = recent_added_cart_element.find_element(By.XPATH, "./td[2]").text
        print(f"Expected Consumer Name: {expected_consumer_name}")

        expected_item_quantity = recent_added_cart_element.find_element(By.XPATH, "./td[5]").text
        print(f"Expected Item Quantity: {expected_item_quantity}")

        # Assert that the item in the active cart matches the item added by the consumer
        print(f"Actual Item name :'{cart_item_name.strip()}', Active_cart Item name :'{expected_item_name.strip()}'")
        print(f"Actual Consumer name :'{consumer_data['first_name']} {consumer_data['last_name']}', Active_cart Consumer name :'{expected_consumer_name}'")
        print(f"Actual Item quantity  :'{cart_item_counts}', Active_cart Item quantity :'{expected_item_quantity}'")
        assert cart_item_name.strip() == expected_item_name.strip(), f"Item name mismatch: Expected '{cart_item_name.strip()}', but found '{expected_item_name.strip()}'"
        assert f"{consumer_data['first_name']} {consumer_data['last_name']}" == expected_consumer_name, f"Consumer name mismatch: Expected '{consumer_data['first_name']} {consumer_data['last_name']}', but found '{expected_consumer_name}'"
        assert cart_item_counts == expected_item_quantity , f"Item quantity mismatch: Expected '{cart_item_counts}', but found '{expected_item_quantity}'"

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e  



