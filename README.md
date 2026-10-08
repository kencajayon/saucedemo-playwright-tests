# SauceDemo Playwright Tests

A personal practice project for UI test automation using Playwright (Python) and Pytest.
Tests are written against the public demo site https://www.saucedemo.com.

## Tests covered
- Valid login
- Invalid password (negative test)
- Locked-out user (negative test)
- Add item to cart
- Cart shows the correct item
- Remove item from cart
- Sort products by price (low to high)
- Logout
- Checkout with missing first name (negative test)
- Complete checkout

## How to run

1. Create and activate a virtual environment:
```
python -m venv venv
venv\Scripts\Activate.ps1
```

2. Install dependencies:
```
pip install pytest-playwright
playwright install
```

3. Run the tests:
```
pytest --headed
```

## Generate an HTML report
```
pip install pytest-html
pytest --html=report.html --self-contained-html
```
## Project structure
- `tests/` : test files (login, cart, checkout)
- `pages/` : Page Object Model classes (LoginPage, InventoryPage, CartPage, CheckoutPage)
- `pytest.ini` : pytest configuration

## Tools
Python, Playwright, Pytest, VS Code