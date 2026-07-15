from pages.base_page import BasePage
from utils.logger import logger


class CheckoutPage(BasePage):
    """
    Represents the shopping Checkout page.

    """
    def __init__(self, page):
        super().__init__(page)
        self.title = self.page.locator(".title")
        self.first_name_input = self.page.get_by_placeholder("First Name")
        self.last_name_input = self.page.get_by_placeholder("Last Name")
        self.postal_code_input = self.page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = self.page.get_by_role("button",name="Continue")
        self.cancel_button = self.page.get_by_role("button",name="Cancel")

        self.error_message = self.page.locator("[data-test='error']")


    def is_loaded(self):
        """
        Verifies that the Checkout page is visible.
        """
        logger.info("Checking if Cart page is loaded")
        self.should_have_text(self.title, "Checkout: Your Information" )

    def continue_checkout(self):
        """
        Continue to checkout overview page.
        """
        logger.info("Continuing checkout")
        self.click(self.continue_button)

    def cancel_checkout(self):
        """
        Cancel checkout and return to cart.
        """
        logger.info("Cancelling checkout")
        self.click(self.cancel_button)

    def fill_checkout_information(self, first_name, last_name, postal_code):
        """
        Fill checkout customer information.
        """
        logger.info("Filling checkout information")

        self.fill(self.first_name_input, first_name)
        self.fill(self.last_name_input, last_name)
        self.fill(self.postal_code_input, postal_code)

    def get_error_message(self):
        """
        Returns checkout validation error message.
        """
        return self.get_text(self.error_message)
