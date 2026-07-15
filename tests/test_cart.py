from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import expect


def test_continue_shopping(cart_page):
    """
      Verify that user can return to the Products page
      by clicking the Continue Shopping button.
    """
    cart_page.back_to_shopping_page()

    products_page = ProductsPage(cart_page.page)
    products_page.is_loaded()

def test_checkout_button(cart_page):
    """
    Verify that user can navigate to the Checkout page
    by clicking the Checkout button.
    """
    cart_page.open_checkout_page()

    checkout_page = CheckoutPage(cart_page.page)
    checkout_page.is_loaded()


def test_remove_product_from_cart(logged_in_page):
    """
    Verify that a product can be removed from the shopping cart.
    """
    products_page = ProductsPage(logged_in_page)
    products_page.add_product_to_cart_by_name("Sauce Labs Backpack")
    products_page.open_cart()

    cart_page = CartPage(logged_in_page)

    expect(cart_page.cart_items).to_have_count(1)

    cart_page.remove_product_from_cart_by_name("Sauce Labs Backpack")

    expect(cart_page.cart_items).to_have_count(0)

def test_cart_contain_expected_products(cart_with_multiple_products):
    """
    Verify that all selected products are displayed in the shopping cart.
    """

    cart_page, products = cart_with_multiple_products

    products_names = cart_page.get_product_names()

    assert set(products_names) == set(products)


