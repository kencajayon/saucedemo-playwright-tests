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

def test_cart_shows_correct_item(page: Page):
    login(page)
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.locator(".cart_item .inventory_item_name")).to_have_text("Sauce Labs Backpack")


def test_remove_item_from_cart(page: Page):
    login(page)
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click("#remove-sauce-labs-backpack")
    expect(page.locator(".shopping_cart_badge")).to_have_count(0)


def test_sort_price_low_to_high(page: Page):
    login(page)
    page.select_option('[data-test="product-sort-container"]', "lohi")
    expect(page.locator(".inventory_item_price").first).to_have_text("$7.99")