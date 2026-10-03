import pytest
from pages.registration_page import RegistrationPage
from utils.data_generator import generate_test_user_data

@pytest.mark.ui
def test_register_new_user(browser):

    test_user_data = generate_test_user_data()

    RegistrationPage(browser).open().register(test_user_data)

    assert "Customer Created" in browser.title, "Registration failed: 'Welcome' not found in page title"