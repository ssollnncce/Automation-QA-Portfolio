from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage: 

    URL = "https://parabank.parasoft.com/parabank/index.htm"

    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.button[value='Log In']")

    def __init__(self, driver): 
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        return self

    def login(self, username: str, password: str):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

        old_title = self.driver.title

        self.driver.find_element(*self.LOGIN_BUTTON).click()

        WebDriverWait(self.driver, 10).until(EC.none_of(EC.title_contains(old_title)))