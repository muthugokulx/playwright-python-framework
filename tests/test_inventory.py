import pytest


@pytest.mark.smoke
def test_products_are_listed(logged_in_page):
    logged_in_page.expect_loaded()
    assert logged_in_page.item_count() > 0


@pytest.mark.regression
def test_add_item_to_cart(logged_in_page):
    logged_in_page.add_first_item_to_cart()
    logged_in_page.expect_cart_count(1)
