from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# ---------- EDIT THESE VALUES TO TEST DIFFERENT SCENARIOS ----------
USERNAME = "Naveenprabu"
PASSWORD = "naveen"
TRANSFER_AMOUNT = "77"   # use a distinctive amount so we know it's THIS test's transaction
# ---------------------------------------------------------------------

BASE_URL = "https://parabank.parasoft.com/parabank/index.htm"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    # ---------- LOGIN ----------
    driver.get(BASE_URL)
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//input[@value='Log In']").click()
    wait.until(EC.url_contains("overview.htm"))

    # ---------- STEP 1: DO A FRESH TRANSFER ----------
    driver.find_element(By.LINK_TEXT, "Transfer Funds").click()
    wait.until(lambda d: len(Select(d.find_element(By.ID, "fromAccountId")).options) > 1)

    driver.find_element(By.ID, "amount").send_keys(TRANSFER_AMOUNT)

    from_account_dropdown = Select(driver.find_element(By.ID, "fromAccountId"))
    to_account_dropdown = Select(driver.find_element(By.ID, "toAccountId"))
    from_account_dropdown.select_by_index(0)
    to_account_dropdown.select_by_index(1)

    driver.find_element(By.XPATH, "//input[@value='Transfer']").click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#showResult h1")))
    print(f"Transfer of {TRANSFER_AMOUNT} completed — now searching for it")

    # ---------- STEP 2: FIND IT VIA FIND TRANSACTIONS (same account) ----------
    driver.find_element(By.LINK_TEXT, "Find Transactions").click()
    wait.until(EC.visibility_of_element_located((By.ID, "amount")))

    driver.find_element(By.ID, "amount").send_keys(TRANSFER_AMOUNT)
    driver.find_element(By.ID, "findByAmount").click()

    # ---------- READ RESULTS ----------
    wait.until(EC.visibility_of_element_located((By.ID, "transactionTable")))
    table = driver.find_element(By.ID, "transactionTable")
    rows = table.find_elements(By.TAG_NAME, "tr")
    result_rows = rows[1:]

    print(f"Transactions found: {len(result_rows)}")
    for row in result_rows:
        print(row.text)

    # ---------- ASSERTION ----------
    assert len(result_rows) >= 1, "No transactions found for the given amount"
    print("TEST PASSED: Transaction search returned results")

except AssertionError as e:
    print(f"TEST FAILED: {e}")

except Exception as e:
    print(f"TEST ERROR: {e}")

finally:
    time.sleep(2)
    driver.quit()