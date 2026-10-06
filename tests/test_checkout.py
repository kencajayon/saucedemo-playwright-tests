from playwright.sync_api import Page, expect


def login_and_add_item(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    page.click("#checkout")


def test_checkout_missing_first_name(page: Page):
    login_and_add_item(page)
    page.fill("#last-name", "Cajayon")
    page.fill("#postal-code", "4103")
    page.click("#continue")
    expect(page.locator('[data-test="error"]')).to_contain_text("First Name is required")


def test_complete_checkout(page: Page):
    login_and_add_item(page)
    page.fill("#first-name", "Kenneth")
    page.fill("#last-name", "Cajayon")
    page.fill("#postal-code", "4103")
    page.click("#continue")
    page.click("#finish")
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")