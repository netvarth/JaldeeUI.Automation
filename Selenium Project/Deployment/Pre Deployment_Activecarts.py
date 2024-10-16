import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
import time

@pytest.fixture(scope='session')
def driver():
    service = ChromeService(executable_path=r"Drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

@pytest.fixture()
def consumer_login(driver):
    driver.get("https://scale.jaldee.com/RangSweets")
    driver.maximize_window()
    yield driver

@pytest.fixture()
def provider_login(driver):
    driver.get("https://scale.jaldee.com/business/")
    driver.maximize_window()
    
    # Use explicit waits instead of sleep
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "loginId"))
    ).send_keys("5555998844")  # Ideally use environment variables here

    driver.find_element(By.ID, "password").send_keys("Jaldee123")  # Avoid hardcoding
    driver.find_element(By.XPATH, "//div[@class='mt-2']").click()

    # Wait for the next page to load
    WebDriverWait(driver, 10).until(
        EC.url_changes("https://scale.jaldee.com/business/")
    )
    
    yield driver

    # Attach a screenshot if needed for debugging
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()

@pytest.mark.usefixtures("consumer_login", "provider_login")
class TestShoppingFlow:

    def test_add_item_to_cart(self, consumer_login):
        # Example test logic: Add item to cart on the consumer side
        # You will need to replace this with actual logic for your test case
        # Wait for the item element and click it
        Dessert = WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='category-name d-flex justify-content-between'][normalize-space()='Dessert']"))
        )
        consumer_login.execute_script("arguments[0].scrollIntoView(true);", Dessert)
        time.sleep(5)
        Dessert.click()
        time.sleep(3)
        WebDriverWait(consumer_login, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add']"))
        )
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='item-class'][1]"))
        ).click()  # Replace with actual XPath of the item

        # Click on the "Add to Cart" button
        driver.find_element(By.XPATH, "//button[@id='add-to-cart']").click()  # Replace with actual XPath

        # Verify item is added successfully
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='success-message']"))
        )
        assert "Item added successfully" in driver.page_source  # Adjust based on your confirmation message

    # def test_check_provider_cart(self, provider_login):
    #     # Example test logic: Check if the item is in the provider cart
    #     WebDriverWait(provider_login, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//div[@class='provider-cart-item']"))
    #     )

    #     cart_items = provider_login.find_elements(By.XPATH, "//div[@class='provider-cart-item']")
    #     assert any("Expected Item Name" in item.text for item in cart_items)  # Replace with actual expected text