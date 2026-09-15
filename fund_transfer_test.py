from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

USERNAME = "Naveen"
PASSWORD = "naveen123#" 
TRANSFER_AMOUNT = "100"

BASE_URL = "https://parabank.parasoft.com/parabank/index.htm"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    # ---------- LOGIN FIRST ----------
    driver.get(BASE_URL)
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//input[@value='Log In']").click()
    wait.until(EC.url_contains("overview.htm"))

    # ---------- GO TO TRANSFER FUNDS ----------
    driver.find_element(By.LINK_TEXT, "Transfer Funds").click()

    wait.until(lambda d: len(Select(d.find_element(By.ID, "fromAccountId")).options) > 1)

    driver.find_element(By.ID, "amount").send_keys(TRANSFER_AMOUNT)

    from_account_dropdown = Select(driver.find_element(By.ID, "fromAccountId"))
    to_account_dropdown = Select(driver.find_element(By.ID, "toAccountId"))
    from_account_dropdown.select_by_index(0)
    to_account_dropdown.select_by_index(1)

    driver.find_element(By.XPATH, "//input[@value='Transfer']").click()

    # ---------- ASSERTION ----------
    confirmation = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#showResult h1")))
    assert "Transfer Complete!" in confirmation.text
    print("TEST PASSED: Fund transfer successful")

except AssertionError as e:
    print(f"TEST FAILED: {e}")

except Exception as e:
    print(f"TEST ERROR: {e}")

finally:
    time.sleep(2)
    driver.quit()