from utils.messages import Messages
from pages.products_page import ProductsPage

def test_checkout_success_message(complete_checkout):
    """
    Verify that the success message is displayed after completing checkout.
    """
    assert complete_checkout.get_success_message() == Messages.CHECKOUT_COMPLETE


def test_checkout_confirmation_message(complete_checkout):
    """
    Verify that the checkout confirmation message is displayed correctly.
    """
    assert complete_checkout.get_confirmation_message() == Messages.CHECKOUT_CONFIRMATION


def test_back_home(complete_checkout):
    """
    Verify that user can return to the Products page
    by clicking the Back Home button.
    """
    complete_checkout.back_home()

    products_page = ProductsPage(complete_checkout.page)
    products_page.is_loaded()