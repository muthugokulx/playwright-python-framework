import pytest

from pages.cart_page import CartPage
from pages.checkout_page import (
    CheckoutCompletePage,
    CheckoutInfoPage,
    CheckoutOverviewPage,
)


@pytest.fixture
def checkout_info(logged_in_page, page, checkout_data):
    """Starts the test on checkout step one with the sample products in the cart."""
    for name in checkout_data["products"]:
        logged_in_page.add_item_to_cart(name)
    logged_in_page.open_cart()
    CartPage(page).checkout()
    return CheckoutInfoPage(page)


@pytest.mark.smoke
def test_complete_checkout(checkout_info, page, logged_in_page, checkout_data):
    customer = checkout_data["customer"]
    checkout_info.fill_info(customer["first_name"], customer["last_name"], customer["postal_code"])
    checkout_info.continue_checkout()

    overview = CheckoutOverviewPage(page)
    overview.expect_url_contains("checkout-step-two")
    overview.expect_items(checkout_data["products"])
    overview.finish()

    complete = CheckoutCompletePage(page)
    complete.expect_url_contains("checkout-complete")
    complete.expect_order_complete()
    logged_in_page.expect_cart_empty()


@pytest.mark.regression
def test_order_totals_are_correct(checkout_info, page, checkout_data):
    customer = checkout_data["customer"]
    checkout_info.fill_info(customer["first_name"], customer["last_name"], customer["postal_code"])
    checkout_info.continue_checkout()

    overview = CheckoutOverviewPage(page)
    assert overview.subtotal() == overview.item_prices_sum()
    assert overview.total() == round(overview.subtotal() + overview.tax(), 2)


@pytest.mark.regression
@pytest.mark.parametrize(
    "first_name, last_name, postal_code, error",
    [
        ("", "Doe", "600001", "First Name is required"),
        ("John", "", "600001", "Last Name is required"),
        ("John", "Doe", "", "Postal Code is required"),
    ],
)
def test_checkout_requires_all_fields(checkout_info, first_name, last_name, postal_code, error):
    checkout_info.fill_info(first_name, last_name, postal_code)
    checkout_info.continue_checkout()

    checkout_info.expect_error(error)


@pytest.mark.regression
def test_cancel_checkout_returns_to_cart(checkout_info, page):
    checkout_info.cancel()

    cart = CartPage(page)
    cart.expect_url_contains("cart.html")
    cart.expect_loaded()
