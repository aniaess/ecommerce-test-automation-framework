from pages.base_page import BasePage
from utils.logger import logger
from utils.config import BASE_URL


class LoginPage(BasePage):
    """
        Page Object representing the SauceDemo login page.

        Provides methods for opening the page, performing user login,
        and retrieving login error messages.
    """

    def __init__(self, page):
        """
           Initializes the LoginPage and defines all page locators.
           Args:
               page: Playwright Page instance.
        """
        super().__init__(page)
        self.username_input = self.page.get_by_placeholder("Username")
        self.password_input = self.page.get_by_placeholder("Password")
        self.login_button = self.page.locator("#login-button")
        self.error_message = self.page.locator("h3")

    def open(self):
        """
            Opens the SauceDemo login page.
        """
        logger.info("Opening Login page")
        self.open_page(BASE_URL)


    def login(self, username, password):
        """
            Logs in using the provided user credentials.
            Args:
                username (str): Username used for login.
                password (str): Password used for login.
        """
        logger.info(f"Logging in as '{username}'")
        self.click(self.username_input)
        self.fill(self.username_input, username)

        self.click(self.password_input)
        self.fill(self.password_input, password)

        self.click(self.login_button)

    def get_error_message(self):
        """
           Returns the login error message if the login attempt was unsuccessful.
           Returns:
                str: Login error message displayed on the page.
        """
        return self.get_text(self.error_message)