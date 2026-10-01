from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------- EDIT THESE VALUES TO TEST DIFFERENT SCENARIOS ----------
USERNAME = "Naveenprabu"
PASSWORD = "naveen"
NEW_STREET = "45 Updated Street"
NEW_CITY = "Coimbatore"
NEW_STATE = "Tamil Nadu"
NEW_ZIP = "641002"
NEW_PHONE = "9998887777"
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

    # ---------- GO TO UPDATE CONTACT INFO ----------
    driver.find_element(By.LINK_TEXT, "Update Contact Info").click()
    wait.until(EC.visibility_of_element_located((By.ID, "customer.address.street")))

    street_field = driver.find_element(By.ID, "customer.address.street")
    street_field.clear()
    street_field.send_keys(NEW_STREET)

    city_field = driver.find_element(By.ID, "customer.address.city")
    city_field.clear()
    city_field.send_keys(NEW_CITY)

    state_field = driver.find_element(By.ID, "customer.address.state")
    state_field.clear()
    state_field.send_keys(NEW_STATE)

    zip_field = driver.find_element(By.ID, "customer.address.zipCode")
    zip_field.clear()
    zip_field.send_keys(NEW_ZIP)

    phone_field = driver.find_element(By.ID, "customer.phoneNumber")
    phone_field.clear()
    phone_field.send_keys(NEW_PHONE)

    driver.find_element(By.XPATH, "//input[@value='Update Profile']").click()

    # ---------- ASSERTION ----------
    confirmation = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Profile Updated']")))
    assert confirmation.is_displayed()
    print("TEST PASSED: Profile updated successfully")

except AssertionError as e:
    print(f"TEST FAILED: {e}")

except Exception as e:
    print(f"TEST ERROR: {e}")

finally:
    time.sleep(12)
    driver.quit()