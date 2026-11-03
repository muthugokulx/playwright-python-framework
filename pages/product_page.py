from playwright.sync_api import expect

from pages.base_page import BasePage


class ProductPage(BasePage):
    url_path = "/inventory-item.html"

    def __init__(self, page):
        super().__init__(page)
        self.name = page.locator("[data-test='inventory-item-name']")
        self.description = page.locator("[data-test='inventory-item-desc']")
        self.price = page.locator("[data-test='inventory-item-price']")
        self.add_to_cart_button = page.locator("[data-test='add-to-cart']")
        self.remove_button = page.locator("[data-test='remove']")
        self.back_button = page.locator("[data-test='back-to-products']")

    def expect_product(self, name: str, price: str):
        expect(self.name).to_have_text(name)
        expect(self.price).to_have_text(price)
        expect(self.description).not_to_be_empty()

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def remove_from_cart(self):
        self.remove_button.click()

    def back_to_products(self):
        self.back_button.click()
