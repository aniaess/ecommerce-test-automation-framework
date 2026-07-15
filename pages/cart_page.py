from pages.base_page import BasePage
from utils.logger import logger


class CartPage(BasePage):
    """
    Represents the shopping cart page.

    Provides methods for interacting with products added to the cart.
    """
    def __init__(self, page):
        super().__init__(page)
        self.title = self.page.locator(".title")
        self.cart_items = self.page.locator(".cart_item")
        self.item_names = self.page.locator(".inventory_item_name")
        self.continue_shopping_button= self.page.locator("#continue-shopping")
        self.checkout_button = self.page.get_by_role("button", name="Checkout")

    def is_loaded(self):
        """
        Verifies that the Cart page is visible.
        """
        logger.info("Checking if Cart page is loaded")
        self.should_have_text(self.title, "Your Cart" )

    def get_items_count(self):
        """
           Returns the number of products currently displayed in the cart.
        """
        return self.cart_items.count()

    def is_product_in_cart(self, product_name):
        """
        Checks whether a product with the given name is present in the cart.
        Args:
            product_name (str): Product name.
        Returns:
            bool: True if the product is present.
        """
        return self.page.get_by_text(product_name).is_visible()

    def back_to_shopping_page(self):
        """
        Navigates back to the Products page.
        """
        logger.info("Returning to Products page")
        self.click(self.continue_shopping_button)

    def remove_product_from_cart_by_name(self, product_name: str):
        """
        Remove product from cart by its visible name.
        """
        product_card = self.cart_items.filter(
            has=self.page.get_by_text(product_name))
        logger.info(f"Removing '{product_name}' from cart")
        product_card.locator("button").click()

    def get_product_names(self):
        """
        Returns names of all products currently in the cart.
        """
        return self.item_names.all_text_contents()

    def open_checkout_page(self):
        """
        Navigates to checkout page by clicking checkout button.
        """
        logger.info("Opening checkout page")
        self.click(self.checkout_button)

