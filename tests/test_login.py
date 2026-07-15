from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.data_loader import get_user_login_data
from utils.messages import Messages
import pytest
from playwright.sync_api import expect


def test_login_success(page):
    """
    Test: User should be able to log in with valid credentials.
    """

    user = get_user_login_data("standard_user")

    login_page = LoginPage(page)
    login_page.open()

    login_page.login(
        user["username"],
        user["password"]
    )
    products_page = ProductsPage(page)
    products_page.is_loaded()

@pytest.mark.parametrize(
    "user_key, expected_error",
    [
        ("locked_user", Messages.LOCKED_USER),
        ("invalid_user", Messages.INVALID_LOGIN),
        ("empty_username", Messages.EMPTY_USERNAME),
        ("empty_password", Messages.EMPTY_PASSWORD),
    ],
    ids = [
        "locked user",
        "invalid user",
        "empty username",
        "empty password"]
    )

def test_login_negative(page, user_key, expected_error):
    """
    Verify that login displays the appropriate error message
    for invalid login scenarios.
    """
    user = get_user_login_data(user_key)

    login_page = LoginPage(page)
    login_page.open()

    login_page.login(
        user["username"],
        user["password"]
    )

    assert expected_error in login_page.get_error_message()

