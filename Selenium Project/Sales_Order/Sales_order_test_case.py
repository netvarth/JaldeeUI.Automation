import time
import allure

from Framework.common_utils import *
from Framework.common_dates_utils import *
from selenium.common.exceptions import ElementClickInterceptedException



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Active cart for the tracking of online order")
@pytest.mark.parametrize("url, username, password", [(scale_url, sales_order_scale, password)])
def test_sale_order_1(login):
    try:
        time.sleep(5)
        driver = login
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//img)[2]"))
        ).click()

        time.sleep(3)
        WebDriverWait(login, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@id='actionRouteTo_ORD_Dashbrd'])[11]"))
        ).click()   


        rows = driver.find_elements(By.XPATH, "//table[@id='pr_id_121-table']//tbody//tr[contains(@class,'mobile-card')]")

        for row in rows:
            item = row.find_element(By.XPATH, ".//td[1]").text.strip()
            customer = row.find_element(By.XPATH, ".//td[2]").text.strip()
            phone = row.find_element(By.XPATH, ".//td[3]").text.strip()
            store = row.find_element(By.XPATH, ".//td[4]").text.strip()
            catalog = row.find_element(By.XPATH, ".//td[5]").text.strip()
            date = row.find_element(By.XPATH, ".//td[6]").text.strip()
            quantity = row.find_element(By.XPATH, ".//td[7]").text.strip()

            assert item, "Item missing"
            assert customer, "Customer missing"
            assert phone, "Phone missing"
            assert store, "Store missing"
            assert catalog, "Catalog missing"
            assert date, "Date missing"
            assert quantity.isdigit(), "Quantity is not numeric"

    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e