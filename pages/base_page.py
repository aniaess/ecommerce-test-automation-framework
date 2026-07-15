from playwright.sync_api import expect


class BasePage:
    """
    Base class for all Page Objects.

    Provides reusable methods for interacting with web elements,
    such as clicking, entering text, retrieving text, and checking
    element visibility.
    """

    def __init__(self, page):
        """
        Initializes the BasePage.
        Args:
            page: Playwright Page instance.
        """
        self.page = page

    def open_page(self, url):
        """
        Navigates to the specified URL.
        Args:
            url (str): URL of the page to open.
        """
        self.page.goto(url)


    def click(self, locator):
        """
        Clicks on a given locator.
        """
        locator.click()

    def fill(self, locator, value):
        """
        Fills input field with given value.
        """
        locator.fill(value)

    def get_text(self, locator):
        """
        Returns text content of an element.
        """
        return locator.text_content()

    def should_have_text(self, locator, expected_text):
        """
        Verify text content of an element.
        """
        expect(locator).to_have_text(expected_text)
