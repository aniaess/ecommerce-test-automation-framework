from pages.base_page import BasePage
from utils.logger import logger


class CheckoutOverviewPage(BasePage):
    """
    Represents the Checkout Overview page displayed before completing an order.
    """

    def __init__(self, page):
        """
        Initializes the CheckoutOverviewPage and defines all page locators.

        Args:
            page: Playwright Page instance.
        """
        super().__init__(page)

        self.title = self.page.locator(".title")

        self.cart_items = self.page.locator(".cart_item")
        self.item_names = self.page.locator(".inventory_item_name")
        self.item_prices = self.page.locator(".inventory_item_price")

        self.item_total = self.page.locator(".summary_subtotal_label")
        self.tax = self.page.locator(".summary_tax_label")
        self.total = self.page.locator(".summary_total_label")

        self.finish_button = self.page.get_by_role("button",name="Finish")
        self.cancel_button = self.page.get_by_role("button",name="Cancel")

    def is_loaded(self):
        """
        Verify that the Checkout Overview page is displayed.
        """
        logger.info("Checking Checkout Overview page")
        self.should_have_text(self.title, "Checkout: Overview")

    def get_product_names(self):
        """
        Returns a list of product names displayed in the overview.
        """
        return self.item_names.all_text_contents()

    def get_product_prices(self):
        """
        Returns a list of product prices as floats.
        """
        prices = self.item_prices.all_text_contents()
        return [float(price.replace("$", "")) for price in prices]

    def get_item_total(self):
        """
        Returns the item total value.
        """
        text = self.get_text(self.item_total)
        return float(text.replace("Item total: $", ""))

    def get_tax(self):
        """
        Returns the tax value.
        """
        text = self.get_text(self.tax)
        return float(text.replace("Tax: $", ""))

    def get_total(self):
        """
        Returns the total order value.
        """
        text = self.get_text(self.total)
        return float(text.replace("Total: $", ""))

    def cancel_checkout(self):
        """
        Cancel checkout and return to the Products page by clicking Cancel button.
        """
        logger.info("Cancelling checkout")
        self.click(self.cancel_button)

    def navigate_to_checkout_complete(self):
        """
        Complete Overview Checkout page by clicking Finish button.
        """
        logger.info("Complete checkout")
        self.click(self.finish_button)



