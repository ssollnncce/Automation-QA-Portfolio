import pytest 
from pages.login_page import LoginPage

@pytest.mark.ui
@pytest.mark.parametrize("username, password", [
    ("invalid_username", "invalid_password"),
    (None, "invalid_password"),
    ("invalid_username", None),
    ("", "")])
def test_login_with_invalid_credentials(browser, registered_user, username, password):

    username = registered_user["username"] if username is None else username
    password = registered_user["password"] if password is None else password

    LoginPage(browser).open().login(username, password)
    assert "ParaBank | Error" in browser.title, "Login succeeded with invalid credentials, which is unexpected"