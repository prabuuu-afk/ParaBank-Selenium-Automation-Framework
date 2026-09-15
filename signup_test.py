#due to the humanconformation page <anti-automation control> We here used a negative test case="Blank First Name correctly rejected with validation error"
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BASE_URL = "https://parabank.parasoft.com/parabank/register.htm"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    driver.get(BASE_URL)

    # Deliberately leave First Name BLANK, fill everything else
    driver.find_element(By.ID, "customer.lastName").send_keys("Kumar")
    driver.find_element(By.ID, "customer.address.street").send_keys("12 Main Street")
    driver.find_element(By.ID, "customer.address.city").send_keys("Coimbatore")
    driver.find_element(By.ID, "customer.address.state").send_keys("Tamil Nadu")
    driver.find_element(By.ID, "customer.address.zipCode").send_keys("641001")
    driver.find_element(By.ID, "customer.phoneNumber").send_keys("9876543210")
    driver.find_element(By.ID, "customer.ssn").send_keys("123456789")
    driver.find_element(By.ID, "customer.username").send_keys("blank_fname_test")
    driver.find_element(By.ID, "customer.password").send_keys("Test@1234")
    driver.find_element(By.ID, "repeatedPassword").send_keys("Test@1234")

    register_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Register']")))
    register_button.click()

    # ---------- ASSERTION: expect a validation error, NOT successful registration ----------
    error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".error")))
    assert "First name is required" in error_message.text
    print("TEST PASSED: Blank First Name correctly rejected with validation error")

except AssertionError as e:
    print(f"TEST FAILED: {e}")

except Exception as e:
    print(f"TEST ERROR: {e}")

finally:
    time.sleep(2)
    driver.quit()