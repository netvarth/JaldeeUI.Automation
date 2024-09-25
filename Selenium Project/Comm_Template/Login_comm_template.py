import uuid
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

from Framework.common_utils import *
# 
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create confirmation template")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])

def test_add_user(login):
    
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "" ))
    )