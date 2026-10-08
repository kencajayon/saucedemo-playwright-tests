from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

BACKPACK = "sauce-labs-backpack"


def go_to_checkout(page: Page) -> CheckoutPage:
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.add_to_cart(BACKPACK)
    inventory.open_cart()
    CartPage(page).checkout()
    return CheckoutPage(page)


def test_checkout_missing_first_name(page: Page):
    checkout = go_to_checkout(page)
    checkout.fill_details("", "Cajayon", "4103")
    checkout.continue_to_overview()
    expect(checkout.error_message).to_contain_text("First Name is required")


def test_complete_checkout(page: Page):
    checkout = go_to_checkout(page)
    checkout.fill_details("Kenneth", "Cajayon", "4103")
    checkout.continue_to_overview()
    checkout.finish()
    expect(checkout.complete_header).to_have_text("Thank you for your order!")