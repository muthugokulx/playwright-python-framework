from playwright.sync_api import expect


class SideMenu:
    """Burger menu shared by every logged-in page."""

    def __init__(self, page):
        self.page = page
        self.open_button = page.locator("#react-burger-menu-btn")
        self.close_button = page.locator("#react-burger-cross-btn")
        self.all_items_link = page.locator("[data-test='inventory-sidebar-link']")
        self.logout_link = page.locator("[data-test='logout-sidebar-link']")
        self.reset_link = page.locator("[data-test='reset-sidebar-link']")

    def open(self):
        self.open_button.click()
        expect(self.logout_link).to_be_visible()

    def close(self):
        self.close_button.click()
        expect(self.logout_link).to_be_hidden()

    def logout(self):
        self.open()
        self.logout_link.click()

    def reset_app_state(self):
        self.open()
        self.reset_link.click()
        self.close()
