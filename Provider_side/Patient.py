from Framework.common_utils import *


@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_patient(login):
    WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='active-menu']//img"))
    ).click()
