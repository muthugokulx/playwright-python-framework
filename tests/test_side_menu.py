import pytest

from pages.login_page import LoginPage
from pages.side_menu import SideMenu


@pytest.mark.smoke
def test_logout(logged_in_page, page):
    SideMenu(page).logout()

    LoginPage(page).expect_on_page()


@pytest.mark.regression
def test_inventory_requires_login(login_page, page):
    page.goto("/inventory.html")

    login_page.expect_error("You can only access '/inventory.html' when you are logged in")


@pytest.mark.regression
def test_reset_app_state_clears_cart(logged_in_page, page):
    logged_in_page.add_item_to_cart("Sauce Labs Backpack")
    logged_in_page.expect_cart_count(1)

    SideMenu(page).reset_app_state()

    logged_in_page.expect_cart_empty()
