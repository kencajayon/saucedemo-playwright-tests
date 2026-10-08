from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

BACKPACK = "sauce-labs-backpack"


def login_as_standard_user(page: Page) -> InventoryPage:
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    return InventoryPage(page)


def test_add_item_to_cart(page: Page):
    inventory = login_as_standard_user(page)
    inventory.add_to_cart(BACKPACK)
    expect(inventory.cart_badge).to_have_text("1")


def test_logout(page: Page):
    inventory = login_as_standard_user(page)
    inventory.logout()
    expect(page).to_have_url("https://www.saucedemo.com/")


def test_cart_shows_correct_item(page: Page):
    inventory = login_as_standard_user(page)
    inventory.add_to_cart(BACKPACK)
    inventory.open_cart()
    cart = CartPage(page)
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(cart.item_names).to_have_text("Sauce Labs Backpack")


def test_remove_item_from_cart(page: Page):
    inventory = login_as_standard_user(page)
    inventory.add_to_cart(BACKPACK)
    inventory.remove_from_cart(BACKPACK)
    expect(inventory.cart_badge).to_have_count(0)


def test_sort_price_low_to_high(page: Page):
    inventory = login_as_standard_user(page)
    inventory.sort_by("lohi")
    expect(inventory.item_prices.first).to_have_text("$7.99")