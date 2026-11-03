import re

from playwright.sync_api import expect

from pages.base_page import BasePage


class CheckoutInfoPage(BasePage):
    """Step one: customer information form."""

    url_path = "/checkout-step-one.html"

    def __init__(self, page):
        super().__init__(page)
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input = page.locator("[data-test='lastName']")
        self.postal_code_input = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.cancel_button = page.locator("[data-test='cancel']")
        self.error_message = page.locator("[data-test='error']")

    def fill_info(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def cancel(self):
        self.cancel_button.click()

    def expect_error(self, text: str):
        expect(self.error_message).to_contain_text(text)


class CheckoutOverviewPage(BasePage):
    """Step two: order summary with totals."""

    url_path = "/checkout-step-two.html"

    def __init__(self, page):
        super().__init__(page)
        self.item_names = page.locator("[data-test='inventory-item-name']")
        self.item_prices = page.locator("[data-test='inventory-item-price']")
        self.subtotal_label = page.locator("[data-test='subtotal-label']")
        self.tax_label = page.locator("[data-test='tax-label']")
        self.total_label = page.locator("[data-test='total-label']")
        self.finish_button = page.locator("[data-test='finish']")
        self.cancel_button = page.locator("[data-test='cancel']")

    @staticmethod
    def _amount(text: str) -> float:
        return float(re.search(r"\$([\d.]+)", text).group(1))

    def expect_items(self, names: list[str]):
        expect(self.item_names).to_have_text(names)

    def item_prices_sum(self) -> float:
        return round(sum(self._amount(p) for p in self.item_prices.all_inner_texts()), 2)

    def subtotal(self) -> float:
        return self._amount(self.subtotal_label.inner_text())

    def tax(self) -> float:
        return self._amount(self.tax_label.inner_text())

    def total(self) -> float:
        return self._amount(self.total_label.inner_text())

    def finish(self):
        self.finish_button.click()

    def cancel(self):
        self.cancel_button.click()


class CheckoutCompletePage(BasePage):
    url_path = "/checkout-complete.html"

    def __init__(self, page):
        super().__init__(page)
        self.complete_header = page.locator("[data-test='complete-header']")
        self.back_home_button = page.locator("[data-test='back-to-products']")

    def expect_order_complete(self):
        expect(self.complete_header).to_have_text("Thank you for your order!")

    def back_home(self):
        self.back_home_button.click()
