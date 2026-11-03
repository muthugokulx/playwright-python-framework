import re

from playwright.sync_api import Page, expect

from config.settings import settings


class BasePage:
    """Actions every page object can reuse."""

    url_path = "/"

    def __init__(self, page: Page):
        self.page = page
        self.page.set_default_timeout(settings.default_timeout)

    def open(self):
        self.page.goto(self.url_path)
        return self

    def title(self) -> str:
        return self.page.title()

    def expect_url_contains(self, text: str):
        expect(self.page).to_have_url(re.compile(re.escape(text)))
