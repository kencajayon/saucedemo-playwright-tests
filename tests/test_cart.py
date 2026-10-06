from playwright.sync_api import Page, expect


def login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")


def test_add_item_to_cart(page: Page):
    login(page)
    page.click("#add-to-cart-sauce-labs-backpack")
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")


def test_logout(page: Page):
    login(page)
    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")
    expect(page).to_have_url("https://www.saucedemo.com/")