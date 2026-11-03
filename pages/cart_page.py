from playwright.sync_api import expect

from pages.base_page import BasePage


class CartPage(BasePage):
    url_path = "/cart.html"

    def __init__(self, page):
        super().__init__(page)
        self.header_title = page.locator("[data-test='title']")
        self.items = page.locator("[data-test='inventory-item']")
        self.item_names = page.locator("[data-test='inventory-item-name']")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")
        self.checkout_button = page.locator("[data-test='checkout']")

    def expect_loaded(self):
        expect(self.header_title).to_have_text("Your Cart")

    def names(self) -> list[str]:
        return self.item_names.all_inner_texts()

    def expect_items(self, names: list[str]):
        expect(self.item_names).to_have_text(names)

    def remove_item(self, name: str):
        self.items.filter(has_text=name).get_by_role("button", name="Remove").click()

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def checkout(self):
        self.checkout_button.click()
