from Framework.common_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.parametrize('url', ["https://localhost:4200/business/"])
def test_create_catalogs(login):

    time.sleep(10)
    login.get("https://localhost:4200/business/rxorders/dashboard")

    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Catalogs')]"))
    ).click()
    time.sleep(5)

