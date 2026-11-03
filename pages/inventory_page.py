from playwright.sync_api import expect

from pages.base_page import BasePage


class InventoryPage(BasePage):
    url_path = "/inventory.html"

    def __init__(self, page):
        super().__init__(page)
        self.header_title = page.locator(".title")
        self.items = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def expect_loaded(self):
        expect(self.header_title).to_have_text("Products")

    def item_count(self) -> int:
        return self.items.count()

    def add_first_item_to_cart(self):
        self.items.first.get_by_role("button", name="Add to cart").click()

    def expect_cart_count(self, count: int):
        expect(self.cart_badge).to_have_text(str(count))
