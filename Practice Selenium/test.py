from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


#################   Enable the Inventory Setting   #############################
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_lucenesearch(login):

    time.sleep(3)
    # login.find_element(By.XPATH, "// span[contains(text(), 'Tokens')]").click()
    WebDriverWait(login, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='my-1 font-small ng-star-inserted']//span["
                                                  "normalize-space()='Tokens']"))
    ).click()
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Token']"))
    ).click()
    time.sleep(5)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter name or phone or id']"))
    ).send_keys(555000)
    time.sleep(3)
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='gayathri']"))
    ).click()
    time.sleep(5)