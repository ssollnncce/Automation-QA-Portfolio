import pytest
from pages.registration_page import RegistrationPage
from utils.data_generator import generate_test_user_data

@pytest.mark.ui
def test_register_with_existing_username(browser, registered_user):

    new_user_data = generate_test_user_data()
    new_user_data['username'] = registered_user['username']  # Use the username of the already registered user
    RegistrationPage(browser).open().register(new_user_data)

    error_message = RegistrationPage(browser).get_error_message(RegistrationPage.USERNAME_ERROR_MESSAGE)

    assert "This username already exists" in error_message, "Expected error message not found for existing username"

@pytest.mark.ui
@pytest.mark.xfail(reason="Bug")
def test_register_with_existing_ssn_number(browser, registered_user):

    new_user_data = generate_test_user_data()
    new_user_data['phone'] = registered_user['phone']  # Use the phone number of the already registered user
    RegistrationPage(browser).open().register(new_user_data)

    error_message = RegistrationPage(browser).get_error_message(RegistrationPage.SSN_ERROR_MESSAGE)

    assert "This ssn number already exists" in error_message, "Expected error message not found for existing ssn number"
    