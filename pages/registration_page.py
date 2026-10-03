from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:

    URL = "https://parabank.parasoft.com/parabank/register.htm"

    FIRST_NAME_INPUT = (By.ID, "customer.firstName")
    LAST_NAME_INPUT = (By.ID, "customer.lastName")
    ADDRESS_INPUT = (By.ID, "customer.address.street")
    CITY_INPUT = (By.ID, "customer.address.city")
    STATE_INPUT = (By.ID, "customer.address.state")
    ZIP_CODE_INPUT = (By.ID, "customer.address.zipCode")
    PHONE_INPUT = (By.ID, "customer.phoneNumber")
    SSN_INPUT = (By.ID, "customer.ssn")
    USERNAME_INPUT = (By.ID, "customer.username")
    PASSWORD_INPUT = (By.ID, "customer.password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "repeatedPassword")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "input.button[value='Register']")

    USERNAME_ERROR_MESSAGE = (By.ID, "customer.username.errors")
    SSN_ERROR_MESSAGE = (By.ID, "customer.ssn.errors")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        return self

    def register(self, user_data: dict):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(user_data["firstName"])
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(user_data["lastName"])
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(user_data["address"])
        self.driver.find_element(*self.CITY_INPUT).send_keys(user_data["city"])
        self.driver.find_element(*self.STATE_INPUT).send_keys(user_data["state"])
        self.driver.find_element(*self.ZIP_CODE_INPUT).send_keys(user_data["zipCode"])
        self.driver.find_element(*self.PHONE_INPUT).send_keys(user_data["phone"])
        self.driver.find_element(*self.SSN_INPUT).send_keys(user_data["ssn"])
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(user_data["username"])
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(user_data["password"])
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).send_keys(user_data["password"])

        old_title = self.driver.title

        self.driver.find_element(*self.REGISTER_BUTTON).click()

        WebDriverWait(self.driver, 10).until(
            EC.any_of(
                EC.title_contains("Customer Created"),
                EC.visibility_of_element_located(self.USERNAME_ERROR_MESSAGE),
                EC.visibility_of_element_located(self.SSN_ERROR_MESSAGE)
            )
        )

    def get_error_message(self, locator):

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return error_message.text