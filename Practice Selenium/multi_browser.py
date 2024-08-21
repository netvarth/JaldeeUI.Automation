import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=ChromeService(
            executable_path=r"Drivers\chromedriver-win64\chromedriver.exe"
        ),
        options=chrome_options
    )

    yield driver

    driver.quit()

def test_login_1(browser):
    login_data = {'username': 'user1', 'password': 'password1'}
    driver = browser
    driver.get("https://scale.jaldee.com/business/")
    driver.maximize_window()
    driver.find_element(By.ID, "loginId").send_keys(login_data['username'])
    driver.find_element(By.ID, "password").send_keys(login_data['password'])
    driver.find_element(By.XPATH, "//div[@class='mt-2']").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//some_element_xpath"))
    )
    assert "Expected Element" in driver.page_source

def test_login_2(browser):
    login_data = {'username': 'user2', 'password': 'password2'}
    driver = browser
    driver.get("https://scale.jaldee.com/business/")
    driver.maximize_window()
    driver.find_element(By.ID, "loginId").send_keys(login_data['username'])
    driver.find_element(By.ID, "password").send_keys(login_data['password'])
    driver.find_element(By.XPATH, "//div[@class='mt-2']").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//some_element_xpath"))
    )
    assert "Expected Element" in driver.page_source
