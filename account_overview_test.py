from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------- EDIT THESE VALUES TO TEST DIFFERENT SCENARIOS ----------
USERNAME = "Naveen"
PASSWORD = "naveen123#"
# ---------------------------------------------------------------------

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

    # ---------- READ ACCOUNT TABLE ----------
    table = wait.until(EC.visibility_of_element_located((By.ID, "accountTable")))
    rows = table.find_elements(By.TAG_NAME, "tr")

    print(f"Total rows found (including header): {len(rows)}")

    account_rows = rows[1:]  # skip header only, no assumption about a Total row

    print(f"Number of accounts found: {len(account_rows)}")

    for row in account_rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) >= 2:
            account_number = cells[0].text
            balance = cells[1].text
            print(f"Account: {account_number} | Balance: {balance}")

    # ---------- ASSERTION ----------
    assert len(account_rows) >= 1, "No accounts found on Accounts Overview page"
    print("TEST PASSED: Accounts Overview displays accounts correctly")

except AssertionError as e:
    print(f"TEST FAILED: {e}")

except Exception as e:
    print(f"TEST ERROR: {e}")

finally:
    time.sleep(2)
    driver.quit()