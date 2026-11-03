import pytest

from pages.product_page import ProductPage


@pytest.mark.regression
def test_product_detail_matches_listing(logged_in_page, page):
    name = logged_in_page.names()[0]
    price = f"${logged_in_page.prices()[0]:.2f}"

    logged_in_page.open_item(name)

    product = ProductPage(page)
    product.expect_url_contains("inventory-item.html")
    product.expect_product(name, price)


@pytest.mark.regression
def test_add_and_remove_from_product_detail(logged_in_page, page):
    logged_in_page.open_item("Sauce Labs Backpack")
    product = ProductPage(page)

    product.add_to_cart()
    logged_in_page.expect_cart_count(1)

    product.remove_from_cart()
    logged_in_page.expect_cart_empty()


@pytest.mark.regression
def test_back_to_products(logged_in_page, page):
    logged_in_page.open_item("Sauce Labs Backpack")
    ProductPage(page).back_to_products()

    logged_in_page.expect_url_contains("inventory.html")
    logged_in_page.expect_loaded()
