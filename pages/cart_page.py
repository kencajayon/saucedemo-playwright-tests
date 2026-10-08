from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.item_names = page.locator(".cart_item .inventory_item_name")
        self.checkout_button = page.locator("#checkout")

    def checkout(self):
        self.checkout_button.click()