import pytest

from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_valid_login(login_page, page, users):
    user = users["valid_user"]
    login_page.login(user["username"], user["password"])

    inventory = InventoryPage(page)
    inventory.expect_url_contains("inventory")
    inventory.expect_loaded()


@pytest.mark.regression
def test_locked_out_user_sees_error(login_page, users):
    user = users["locked_user"]
    login_page.login(user["username"], user["password"])
    login_page.expect_error("locked out")


@pytest.mark.regression
def test_invalid_password_sees_error(login_page, users):
    user = users["invalid_user"]
    login_page.login(user["username"], user["password"])
    login_page.expect_error("do not match")
