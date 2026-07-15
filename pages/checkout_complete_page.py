from pages.base_page import BasePage
from utils.logger import logger


class CheckoutCompletePage(BasePage):
    """
    Represents the Checkout Overview page displayed before completing an order.
    """

    def __init__(self, page):
        """
        Initializes the CheckoutCompletePage and defines all page locators.

        Args:
            page: Playwright Page instance.
        """
        super().__init__(page)
        self.title = self.page.locator(".title")
        self.complete_header = self.page.locator(".complete-header")
        self.complete_text = self.page.locator(".complete-text")
        self.back_home_button = self.page.locator("#back-to-products")

    def is_loaded(self):
        """
        Verify that the Checkout Complete page is displayed.
        """
        logger.info("Checking Checkout Complete page")
        self.should_have_text(self.title, "Checkout: Complete!")

    def get_success_message(self):
        """
        Returns the checkout success message.
        """
        return self.get_text(self.complete_header)

    def get_confirmation_message(self):
        """
        Returns the checkout confirmation text.
        """
        return self.get_text(self.complete_text)

    def back_home(self):
        """
        Return to the Products page.
        """
        logger.info("Returning to Products page")
        self.click(self.back_home_button)
