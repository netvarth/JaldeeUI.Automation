from Framework.common_utils import *
from Framework.common_dates_utils import *


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Edit Actions")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Edit_Actions(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='font-small']")
        time.sleep(3)
        WebDriverWait(login, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//div[contains(@class,'card action-card')]"))
        )
        cards = login.find_elements(By.XPATH, "//div[@class='card action-card']")
        print(f"Number of cards found: {len(cards)}")
        for index, card in enumerate(cards):
        # Print the current state of the card
            current_class = card.get_attribute('class')
            print(f"Card {index + 1} current class: {current_class}")

            # Check if the card is not selected
            if 'selected' not in current_class:
                print("Selecting card...")
                card.click()  # Click the card to select it
                time.sleep(3)
                # Wait for the card to be updated
                WebDriverWait(login, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='card action-card selected']")
                ))
                print("Card selected.")
            else:
                print("Card is already selected, skipping.")
                time.sleep(3)
       
        wait_and_locate_click(login, By.XPATH, "//button[@class='p-element p-button-primary p-button p-component']")
        print("Toast Message:", wait_for_text(login, By.CLASS_NAME, "p-toast-detail"))
        print("All cards have been selected.")


    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Max,Min and CloseTab")
@pytest.mark.parametrize("url", ["https://scale.jaldee.com/business/"])
def test_Edit_Actions(login):
    try:
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "//li[3]//a[1]//div[1]//span[1]//span[1]//img[1]") 
        time.sleep(2)
        wait_and_locate_click(login, By.XPATH, "//span[@class='font-small']")
        time.sleep(3)
        wait_and_locate_click(login, By.XPATH, "(//button[@type='button'])[11]")
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "(//button[@type='button'])[11]")
        time.sleep(5)
        wait_and_locate_click(login, By.XPATH, "(//button[@type='button'])[12]")
        time.sleep(5)
    except Exception as e:
        allure.attach(  
            login.get_screenshot_as_png(),  
            name="full_page",  
            attachment_type=AttachmentType.PNG,
        ) 
        raise e