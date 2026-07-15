from pages.checkout_complete_page import CheckoutCompletePage
from pages.products_page import ProductsPage
import pytest

def test_finish_checkout(overview_with_multiple_products):
    """
      Verify that user can navigate to the Products page
      by clicking the Finish Shopping button.
    """
    overview_page, _ = overview_with_multiple_products
    overview_page.navigate_to_checkout_complete()
    complete_page = CheckoutCompletePage(overview_page.page)
    complete_page.is_loaded()

def test_cancel_checkout(overview_with_multiple_products):
    """
    Verify that user can return to the Products page
    by clicking the Cancel button.
    """
    overview_page, _ = overview_with_multiple_products

    overview_page.cancel_checkout()

    products_page = ProductsPage(overview_page.page)
    products_page.is_loaded()

def test_overview_contains_expected_products(overview_with_multiple_products):
    """
    Verify that all selected products are displayed on the Checkout Overview page.
    """
    overview_page, expected_products = overview_with_multiple_products
    actual_products = overview_page.get_product_names()

    assert set(actual_products) == set(expected_products)

def test_item_total_is_correct(overview_with_multiple_products):
    """
    Verify that the item total equals the sum of all product prices.
    """
    overview_page, _ = overview_with_multiple_products
    prices = overview_page.get_product_prices()

    assert overview_page.get_item_total() == sum(prices)

def test_total_price_is_correct(overview_with_multiple_products):
    """
    Verify that the total price equals the item total plus tax.
    """
    overview_page, _ = overview_with_multiple_products

    expected_total = (
        overview_page.get_item_total()
        + overview_page.get_tax()
    )

    assert overview_page.get_total() == pytest.approx(expected_total)