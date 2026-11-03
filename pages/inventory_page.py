from playwright.sync_api import expect

from pages.base_page import BasePage


class InventoryPage(BasePage):
    url_path = "/inventory.html"

    def __init__(self, page):
        super().__init__(page)
        self.header_title = page.locator(".title")
        self.items = page.locator(".inventory_item")
        self.item_names = page.locator("[data-test='inventory-item-name']")
        self.item_prices = page.locator("[data-test='inventory-item-price']")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")

    def expect_loaded(self):
        expect(self.header_title).to_have_text("Products")

    def item_count(self) -> int:
        return self.items.count()

    def add_first_item_to_cart(self):
        self.items.first.get_by_role("button", name="Add to cart").click()

    def _item(self, name: str):
        return self.items.filter(has=self.page.get_by_text(name, exact=True))

    def add_item_to_cart(self, name: str):
        self._item(name).get_by_role("button", name="Add to cart").click()

    def remove_item_from_cart(self, name: str):
        self._item(name).get_by_role("button", name="Remove").click()

    def expect_item_button(self, name: str, label: str):
        expect(self._item(name).locator("button")).to_have_text(label)

    def open_item(self, name: str):
        self.item_names.filter(has_text=name).click()

    def sort_by(self, option: str):
        """option is the visible label, e.g. 'Price (low to high)'."""
        self.sort_dropdown.select_option(label=option)

    def names(self) -> list[str]:
        return self.item_names.all_inner_texts()

    def prices(self) -> list[float]:
        return [float(p.lstrip("$")) for p in self.item_prices.all_inner_texts()]

    def open_cart(self):
        self.cart_link.click()

    def expect_cart_count(self, count: int):
        expect(self.cart_badge).to_have_text(str(count))

    def expect_cart_empty(self):
        expect(self.cart_badge).to_be_hidden()
