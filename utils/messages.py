class Messages:
    """
    Central place for all expected error messages in the application.
    """
    # Login errors
    INVALID_LOGIN = "Username and password do not match any user in this service"
    LOCKED_USER = "Sorry, this user has been locked out."
    EMPTY_USERNAME = "Username is required"
    EMPTY_PASSWORD = "Password is required"

    # Checkout errors
    EMPTY_FIRST_NAME = "Error: First Name is required"
    EMPTY_LAST_NAME = "Error: Last Name is required"
    EMPTY_POSTAL_CODE = "Error: Postal Code is required"

    # successfully completed order message
    CHECKOUT_COMPLETE = "Thank you for your order!"
    CHECKOUT_CONFIRMATION = (
        "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
    )