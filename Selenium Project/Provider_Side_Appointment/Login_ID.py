import time
import allure
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Framework.common_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import allure
from allure_commons.types import AttachmentType





@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Pre deployment testing")
def test_account_signup():
    login = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    login.get("https://test.jaldee.com/business/")
    login.maximize_window()




