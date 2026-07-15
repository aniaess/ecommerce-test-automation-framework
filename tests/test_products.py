from pages.cart_page import CartPage
from playwright.sync_api import expect
from pages.products_page import ProductsPage
from utils.data_loader import get_products
import pytest
from utils.config import EXPECTED_PRODUCTS_COUNT


def test_products_page_load(products_page):
    """
    Verify that the Products page is displayed after successful login.
    """
    products_page.is_loaded()

def test_products_count(products_page):
    """
    Verify that the Products page displays the expected number of products.
    """
    assert products_page.get_products_count() == EXPECTED_PRODUCTS_COUNT

def test_open_cart(products_page):
    """
    Verify that user can open the shopping cart page after login.
    """
    products_page.open_cart()

    cart_page = CartPage(products_page.page)
    cart_page.is_loaded()

def test_add_single_product_to_cart(logged_in_page):
    """
    Verify that single product can be added from the shopping cart.
    """
    products_page = ProductsPage(logged_in_page)

    products_page.add_product_to_cart_by_name("Sauce Labs Backpack")

    products_page.open_cart()

    cart_page = CartPage(logged_in_page)

    expect(cart_page.cart_items).to_have_count(1)

def test_add_multiple_products_to_cart(cart_with_multiple_products):
    """
    Verify that multiple product can be added from the shopping cart.
    """
    cart_page, products = cart_with_multiple_products

    expect(cart_page.cart_items).to_have_count(3)


@pytest.mark.parametrize(
    "sort_method, reverse",
    [
        ("sort_by_name_asc", False),
        ("sort_by_name_desc", True),
        ("sort_by_price_asc", False),
        ("sort_by_price_desc", True),
    ]
)

def test_products_sorting(products_page, sort_method, reverse):
    """
    Verify that products can be sorted correctly.
    """
    getattr(products_page, sort_method)()

    if "price" in sort_method:
        values = products_page.get_product_prices()
    else:
        values = products_page.get_product_names()

    assert values == sorted(values, reverse=reverse)


