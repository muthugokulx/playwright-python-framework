# Playwright Python Framework

A UI test automation framework built with **Playwright**, **Pytest** and the **Page Object Model**.
Sample tests run against the public demo site [SauceDemo](https://www.saucedemo.com).

## Folder structure

```
playwright-python-framework/
├── config/
│   └── settings.py         # Env-driven settings (credentials, timeouts)
├── pages/                  # Page Object Model classes
│   ├── base_page.py        # Common actions shared by all pages
│   ├── login_page.py
│   ├── inventory_page.py   # Product list, sorting, add/remove
│   ├── product_page.py     # Single product detail
│   ├── cart_page.py
│   ├── checkout_page.py    # Info form, overview, complete steps
│   └── side_menu.py        # Burger menu (logout, reset app state)
├── tests/                  # Test cases, grouped by feature
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_sorting.py
│   ├── test_product_detail.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_side_menu.py
├── test_data/
│   ├── users.json          # Test data kept out of test code
│   └── checkout.json       # Customer details and products to buy
├── utils/
│   ├── data_loader.py      # Helper to read test data files
│   └── logger.py           # Shared logger
├── reports/                # HTML report, screenshots, videos (git-ignored)
├── conftest.py             # Shared Pytest fixtures
├── pytest.ini              # Pytest + Playwright options
├── requirements.txt
├── .env.example            # Copy to .env and fill in
└── .gitignore
```

## Setup

```bash
python -m venv venv
# Windows: venv\Scripts\activate   |   Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
playwright install
cp .env.example .env
```

## Running tests

```bash
pytest                              # all tests, headless Chromium
pytest --headed                     # watch the browser
pytest --browser firefox            # different browser
pytest -m smoke                     # only smoke tests
pytest tests/test_login.py -v       # one file
```

After a run, open `reports/report.html`. Screenshots and videos of failed tests are saved in `reports/artifacts/`.

## Adding a new page

1. Create `pages/<name>_page.py` that extends `BasePage`.
2. Keep locators at the top of the class and expose actions as methods.
3. Write tests in `tests/test_<name>.py` that use the page object, never raw locators.
