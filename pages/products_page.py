from pages.base_page import BasePage
from utils.logger import logger


class ProductsPage(BasePage):
    """
        Represents the Products page displayed after a successful login..

    """

    def __init__(self, page):
        """
           Initializes the ProductsPage and defines all page locators.
           Args:
               page: Playwright Page instance.
        """
        super().__init__(page)
        self.title = self.page.locator(".title")
        self.cart_button = self.page.locator(".shopping_cart_link")
        self.inventory_items = self.page.locator(".inventory_item")
        self.sort_dropdown = self.page.locator(".product_sort_container")
        self.product_names = self.page.locator(".inventory_item_name")
        self.product_prices = self.page.locator(".inventory_item_price")

    def is_loaded(self):
        """
        Verifies that the Products page is displayed.
        """
        logger.info("Checking if Products page is loaded")
        self.should_have_text(self.title, "Products")

    def open_cart(self):
        """
        Clicks cart icon.
        """
        logger.info("Opening cart")
        self.click(self.cart_button)

    def get_products_count(self):
        """
        Returns number of products displayed.
        """
        return self.inventory_items.count()

    def _get_product_card(self, product_name):
        return self.inventory_items.filter(
            has=self.page.get_by_text(product_name)
        )

    def add_product_to_cart_by_name(self, product_name: str):
        """
        Adds product to cart by its visible name.
        """

        logger.info(f"Adding product to cart: {product_name}")
        self._get_product_card(product_name).locator("button").click()

    def remove_product_from_cart_by_name(self, product_name: str):
        """
        Remove product to cart by its visible name.
        """
        logger.info(f"Removing product from cart: {product_name}")

        self._get_product_card(product_name).locator("button").click()

    def sort_by_name_asc(self):
        """
        Sorts products by name (A to Z).
        """
        logger.info("Sorting products by name (A to Z)")
        self.sort_dropdown.select_option("az")

    def sort_by_name_desc(self):
        """
        Sorts products by name (Z to A).
        """
        logger.info("Sorting products by name (Z to A)")
        self.sort_dropdown.select_option("za")

    def sort_by_price_asc(self):
        """
        Sorts products by price low to high.
        """
        logger.info("Sorting products by price low to high")
        self.sort_dropdown.select_option("lohi")

    def sort_by_price_desc(self):
        """
        Sorts products by price high to low.
        """
        logger.info("Sorting products by price high to low")
        self.sort_dropdown.select_option("hilo")

    def get_product_names(self):
        """
        Returns a list of all displayed product names.
        """
        return self.product_names.all_text_contents()

    def get_product_prices(self):
        """
        Returns a list of displayed product prices as floats.
        """
        prices = self.product_prices.all_text_contents()
        return [float(price.replace("$", "")) for price in prices]


