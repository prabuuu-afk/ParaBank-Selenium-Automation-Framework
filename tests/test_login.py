# test_login.py
import pages.login_page as log

def test_valid_login(driver):
    login_page = log.LoginPage(driver)
    driver.get("https://parabank.parasoft.com/parabank/index.html")
    # your code continues here
    