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
PAYEE_NAME = "Electric Company"
PAYEE_ADDRESS = "123 Utility Road"
PAYEE_CITY = "Coimbatore"
PAYEE_STATE = "Tamil Nadu"
PAYEE_ZIP = "641001"
PAYEE_PHONE = "9876543210"
ACCOUNT_NUMBER = "12345"
AMOUNT = "50"
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

    # ---------- GO TO BILL PAY ----------
    driver.find_element(By.LINK_TEXT, "Bill Pay").click()
    wait.until(EC.visibility_of_element_located((By.NAME, "payee.name")))

    driver.find_element(By.NAME, "payee.name").send_keys(PAYEE_NAME)
    driver.find_element(By.NAME, "payee.address.street").send_keys(PAYEE_ADDRESS)
    driver.find_element(By.NAME, "payee.address.city").send_keys(PAYEE_CITY)
    driver.find_element(By.NAME, "payee.address.state").send_keys(PAYEE_STATE)
    driver.find_element(By.NAME, "payee.address.zipCode").send_keys(PAYEE_ZIP)
    driver.find_element(By.NAME, "payee.phoneNumber").send_keys(PAYEE_PHONE)
    driver.find_element(By.NAME, "payee.accountNumber").send_keys(ACCOUNT_NUMBER)
    driver.find_element(By.NAME, "verifyAccount").send_keys(ACCOUNT_NUMBER)
    driver.find_element(By.NAME, "amount").send_keys(AMOUNT)

    driver.find_element(By.XPATH, "//input[@value='Send Payment']").click()

    # ---------- ASSERTION ----------
    confirmation = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#billpayResult h1")))
    assert "Bill Payment Complete" in confirmation.text
    print("TEST PASSED: Bill payment successful")

except AssertionError as e:
    print(f"TEST FAILED: {e}")

except Exception as e:
    print(f"TEST ERROR: {e}")

finally:
    time.sleep(2)
    driver.quit()