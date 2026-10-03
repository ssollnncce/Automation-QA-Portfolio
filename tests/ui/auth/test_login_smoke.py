import pytest

from pages.login_page import LoginPage

@pytest.mark.ui
def test_login_with_registered_user(browser, registered_user):
    LoginPage(browser).open().login(registered_user["username"], registered_user["password"])

    assert "Accounts Overview" in browser.title, "Login failed: Accounts Overview page not displayed"

