import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService




driver = webdriver.Chrome(service=ChromeService(executable_path=r"Drivers\chromedriver-win64\chromedriver.exe"))   
driver.get(" https://scale.jaldee.com/RangSweets")
driver.implicitly_wait(10)
All_item_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "(//h2[@class='ng-star-inserted'])[4]"))
)
driver.execute_script("arguments[0].scrollIntoView(true);", All_item_button)


time.sleep(3)
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Gulab jamun']"))
).click()

time.sleep(3)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//button[normalize-space()='Add to cart']"))
).click()

time.sleep(2)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//input[@id='phone']"))
).send_keys("9207206005")

driver.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

driver.implicitly_wait(10)

otp_digits = "5555"

# Wait for the OTP input fields to be present
otp_inputs = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//input[contains(@id, 'otp_')]")
    )
)

# print("Number of OTP input fields:", len(otp_inputs))
# print(otp_inputs)

for i, otp_input in enumerate(otp_inputs):

    # print(i)
    # print(otp_input)
    otp_input.send_keys(otp_digits[i])

driver.find_element(By.XPATH, "//span[@class='continue ng-star-inserted']").click()

time.sleep(5)

Cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[@class='ms-1 display-large']"))
)
driver.execute_script("arguments[0].click();", Cart_button)

time.sleep(2)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//button[normalize-space()='Checkout']"))
).click()

time.sleep(2)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//button[normalize-space()='Proceed to payment']"))
).click()

time.sleep(3)
confirm_button = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located(
        (By.XPATH, "//button[normalize-space()='Confirm']"))
)
driver.execute_script("arguments[0].click();", confirm_button)

time.sleep(5)
Net_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//div[contains(text(),'NET BANKING')]")
    )
)
driver.execute_script("arguments[0].click();", Net_button)
time.sleep(3)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//button[normalize-space()='Pay']")
    )
).click()

time.sleep(2)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//p[contains(@class,'ptm-paymode-name ptm-lightbold')]")
    )
).click()

time.sleep(1)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'SBI')]"))
).click()

paybutton = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//div[contains(@class,'ptm-overlay-wrapper btn-enabled')]//button[contains(@class,'')][contains(text(),'Pay ₹525')]",
        )
    )
)
paybutton.click()

main_window_handle = driver.current_window_handle

# Wait until the new window is present
WebDriverWait(driver, 10).until(EC.new_window_is_opened)

# Get all window handles
all_window_handles = driver.window_handles

# Find the new window handle (the popup window)
new_window_handle = None
for handle in all_window_handles:
    if handle != main_window_handle:
        new_window_handle = handle
        break

# Switch to the new window
driver.switch_to.window(new_window_handle)

# Now interact with elements in the new window
# For example, clicking the success button
time.sleep(3)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[contains(text(),'Successful')]") 
    )
).click()

# Optionally, switch back to the main window

driver.switch_to.window(main_window_handle)
# time.sleep(15)

try:
    snack_bar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "snackbarnormal"))
    )
    message = snack_bar.text
    print("Snack bar message:", message)

except:

    snack_bar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "snackbarerror"))
    )
    message = snack_bar.text
    print("Snack bar message:", message)

time.sleep(2)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//button[normalize-space()='Home']"))
).click()

time.sleep(3)

driver.quit()
