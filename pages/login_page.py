# login_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//input[@value='Log In']")

    def enter_username(self, username):
        field = self.wait.until(EC.visibility_of_element_located(self.username_field))
        field.send_keys(username)

    def enter_password(self, password):
        field = self.wait.until(EC.visibility_of_element_located(self.password_field))
        field.send_keys(password)

    def click_login(self):
        button = self.wait.until(EC.element_to_be_clickable(self.login_button))
        button.click()