import pytest
from selenium import webdriver

from pages.registration_page import RegistrationPage
from utils.data_generator import generate_test_user_data


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def registered_user():
    # Create a registered user for testing purposes. This fixture generates test user data and returns it as a dictionary.

    driver = webdriver.Chrome()
    user_data = generate_test_user_data()

    user_data = generate_test_user_data()

    RegistrationPage(driver).open().register(user_data)

    driver.quit()

    yield user_data