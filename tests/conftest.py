import pytest
from playwright.sync_api import sync_playwright
import os
from datetime import datetime
from pathlib import Path
import logging

from pytest_playwright.pytest_playwright import browser

from pages.checkout_overview_page import CheckoutOverviewPage
from utils.logger import setup_test_logger
from utils.data_loader import get_user_login_data, get_checkout_data
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage
from utils.data_loader import get_products


@pytest.fixture(scope="function")
def page(request):

    logger = setup_test_logger(request.node.name)

    logger.info("========== TEST STARTED ==========")

    with sync_playwright() as p:
        headless = os.getenv("CI") == "true"
        browser = p.chromium.launch(headless=headless)

        context = browser.new_context()
        page = context.new_page()

        yield page

        logger.info("========== TEST FINISHED ==========")

        context.close()
        browser.close()

@pytest.fixture
def logged_in_page(page):
    user = get_user_login_data("standard_user")

    login_page = LoginPage(page)
    login_page.open()
    login_page.login(
        user["username"],
        user["password"]
    )

    return page

@pytest.fixture
def products_page(logged_in_page):
    return ProductsPage(logged_in_page)

@pytest.fixture
def cart_page(logged_in_page):
    """
    Opens the shopping cart page.

    Returns:
        CartPage object.
    """
    products_page = ProductsPage(logged_in_page)
    products_page.open_cart()

    return CartPage(logged_in_page)

@pytest.fixture
def cart_with_multiple_products(logged_in_page):
    products_page = ProductsPage(logged_in_page)

    products = get_products("multiple_products")

    for product in products:
        products_page.add_product_to_cart_by_name(product)

    products_page.open_cart()

    return CartPage(logged_in_page), products

@pytest.fixture
def checkout_page(logged_in_page):
    """
    Opens the Checkout Information page.

    Returns:
        CheckoutPage: Checkout Information page object.
    """
    products_page = ProductsPage(logged_in_page)
    products_page.open_cart()

    cart_page = CartPage(logged_in_page)
    cart_page.open_checkout_page()

    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.is_loaded()

    return checkout_page

@pytest.fixture
def overview_with_multiple_products(cart_with_multiple_products):
    """
    Opens the Checkout Overview page with multiple products in the cart.

    Returns:
        tuple:
            - CheckoutOverviewPage
            - list of expected product names
    """
    cart_page, products = cart_with_multiple_products

    cart_page.open_checkout_page()

    checkout_page = CheckoutPage(cart_page.page)

    checkout_data = get_checkout_data("valid_checkout")

    checkout_page.fill_checkout_information(
        checkout_data["first_name"],
        checkout_data["last_name"],
        checkout_data["postal_code"]
    )

    checkout_page.continue_checkout()

    overview_page = CheckoutOverviewPage(cart_page.page)
    overview_page.is_loaded()

    return overview_page, products

@pytest.fixture
def complete_checkout(overview_with_multiple_products):
    overview_page, _ = overview_with_multiple_products

    overview_page.navigate_to_checkout_complete()

    complete_page = CheckoutCompletePage(overview_page.page)
    complete_page.is_loaded()

    return complete_page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Takes screenshots for failed tests
    and logs test result.
    """

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        logger = logging.getLogger("framework_logger")

        page = None

        for fixture_value in item.funcargs.values():
            if hasattr(fixture_value, "screenshot"):
                page = fixture_value
                break

        if report.failed:
            logger.error("========== TEST FAILED ==========")

            if page:
                screenshots_dir = Path(__file__).parent.parent / "screenshots"
                screenshots_dir.mkdir(exist_ok=True)

                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                screenshot_path = (
                    screenshots_dir /
                    f"{item.name}_{timestamp}.png"
                )

                page.screenshot(path=str(screenshot_path))

                logger.error(
                    f"Screenshot saved: {screenshot_path}"
                )

        elif report.passed:
            logger.info("========== TEST PASSED ==========")
