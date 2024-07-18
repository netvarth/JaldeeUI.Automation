from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.common import TimeoutException

@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_patient_MR(login):
    time.sleep(5)
    WebDriverWait(login,20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//img[contains(@src, 'customers.gif')]//following::div[contains(text(),'Patients')]")
    )
    ).click()
    time.sleep(3)
