# test_login.py
import pages.login_page as log

def test_valid_login(driver):
    login_page = log.LoginPage(driver)
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    # your code continues here
    login_page.enter_username("user")
    login_page.enter_password("user@123")
    login_page.click_login()
    assert driver.title == "ParaBank"