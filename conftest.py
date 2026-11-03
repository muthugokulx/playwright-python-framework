import pytest

from config.settings import settings
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.data_loader import load_json


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Apply common context settings to every test."""
    return {
        **browser_context_args,
        "viewport": {"width": 1366, "height": 768},
    }


@pytest.fixture(scope="session")
def users():
    return load_json("users.json")


@pytest.fixture(scope="session")
def checkout_data():
    return load_json("checkout.json")


@pytest.fixture
def login_page(page):
    login = LoginPage(page)
    login.open()
    return login


@pytest.fixture
def logged_in_page(login_page, page):
    """Starts the test already logged in as the standard user."""
    login_page.login(settings.username, settings.password)
    return InventoryPage(page)
