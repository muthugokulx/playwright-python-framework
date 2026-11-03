import pytest

from pages.cart_page import CartPage


@pytest.mark.regression
def test_cart_shows_added_items(logged_in_page, page, checkout_data):
    products = checkout_data["products"]
    for name in products:
        logged_in_page.add_item_to_cart(name)
    logged_in_page.expect_cart_count(len(products))

    logged_in_page.open_cart()

    cart = CartPage(page)
    cart.expect_loaded()
    cart.expect_items(products)


@pytest.mark.regression
def test_remove_item_on_inventory_page(logged_in_page):
    logged_in_page.add_item_to_cart("Sauce Labs Onesie")
    logged_in_page.expect_item_button("Sauce Labs Onesie", "Remove")

    logged_in_page.remove_item_from_cart("Sauce Labs Onesie")

    logged_in_page.expect_item_button("Sauce Labs Onesie", "Add to cart")
    logged_in_page.expect_cart_empty()


@pytest.mark.regression
def test_remove_item_in_cart(logged_in_page, page, checkout_data):
    first, second = checkout_data["products"]
    logged_in_page.add_item_to_cart(first)
    logged_in_page.add_item_to_cart(second)
    logged_in_page.open_cart()

    cart = CartPage(page)
    cart.remove_item(first)

    cart.expect_items([second])
    logged_in_page.expect_cart_count(1)


@pytest.mark.regression
def test_continue_shopping_returns_to_inventory(logged_in_page, page):
    logged_in_page.open_cart()
    CartPage(page).continue_shopping()

    logged_in_page.expect_url_contains("inventory.html")
    logged_in_page.expect_loaded()
