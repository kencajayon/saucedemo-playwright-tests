# SauceDemo Playwright Tests

A personal practice project for UI test automation using Playwright (Python) and Pytest.
Tests are written against the public demo site https://www.saucedemo.com.

## Tests covered
- Valid login
- Invalid password (negative test)
- Locked-out user (negative test)
- Add item to cart
- Logout

## How to run
1. Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\Activate.ps1
2. Install dependencies:
   pip install pytest-playwright
   playwright install
3. Run the tests:
   pytest --headed

## Tools
Python, Playwright, Pytest, VS Code