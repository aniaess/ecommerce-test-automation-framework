from pages.cart_page import CartPage
from pages.checkout_overview_page import CheckoutOverviewPage
from utils.data_loader import get_checkout_data
from utils.messages import Messages
import pytest


def test_cancel_checkout(checkout_page):
    """
    Verify that user can cancel checkout
    and return to the shopping cart.
    """

    checkout_page.cancel_checkout()

    cart_page = CartPage(checkout_page.page)
    cart_page.is_loaded()

def test_success_checkout(checkout_page):
    """
    Verify that user can continue to the Checkout Overview page
    after providing valid information.
    """

    checkout_data = get_checkout_data("valid_checkout")

    checkout_page.fill_checkout_information(
        checkout_data["first_name"],
        checkout_data["last_name"],
        checkout_data["postal_code"]
    )

    checkout_page.continue_checkout()

    overview_page = CheckoutOverviewPage(checkout_page.page)
    overview_page.is_loaded()

@pytest.mark.parametrize(
    "user_key, expected_error",
    [
        ("empty_first_name", Messages.EMPTY_FIRST_NAME),
        ("empty_last_name", Messages.EMPTY_LAST_NAME),
        ("empty_postal_code", Messages.EMPTY_POSTAL_CODE),

    ]
)

def test_negative_checkout(checkout_page, user_key, expected_error):
    """
    Verify that checkout validation errors are displayed
    when required fields are missing.
    """
    checkout_page.is_loaded()

    checkout_data = get_checkout_data(user_key)
    checkout_page.fill_checkout_information(
        checkout_data["first_name"],
        checkout_data["last_name"],
        checkout_data["postal_code"]
    )

    checkout_page.continue_checkout()

    assert expected_error in checkout_page.get_error_message()




    
