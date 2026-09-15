from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------- EDIT THESE VALUES TO TEST DIFFERENT SCENARIOS ----------
USERNAME = "user"
PASSWORD = "user123"
# ---------------------------------------------------------------------

BASE_URL = "https://parabank.parasoft.com/parabank/index.htm"

# ---------- SETUP ----------
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    # ---------- NAVIGATE ----------
    driver.get(BASE_URL)

    # ---------- LOGIN ACTIONS ----------
    username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    username_field.send_keys(USERNAME)

    password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    password_field.send_keys(PASSWORD)

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Log In']")))
    login_button.click()

    # ---------- ASSERTION ----------
    wait.until(EC.url_contains("overview.htm"))
    assert "overview.htm" in driver.current_url, "Login failed — did not reach Accounts Overview page"
    print("TEST PASSED: Login successful")

except AssertionError as e:
    print(f"TEST FAILED: {e}")

except Exception as e:
    print(f"TEST ERROR: {e}")

finally:
    time.sleep(2)
    driver.quit()