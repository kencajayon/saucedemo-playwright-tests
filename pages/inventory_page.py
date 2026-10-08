from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.item_prices = page.locator(".inventory_item_price")
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")

    def add_to_cart(self, item: str):
        self.page.click(f"#add-to-cart-{item}")

    def remove_from_cart(self, item: str):
        self.page.click(f"#remove-{item}")

    def sort_by(self, option: str):
        self.sort_dropdown.select_option(option)

    def open_cart(self):
        self.cart_link.click()

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()