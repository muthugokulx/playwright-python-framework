import pytest


@pytest.mark.regression
@pytest.mark.parametrize(
    "option, key, reverse",
    [
        ("Name (A to Z)", "names", False),
        ("Name (Z to A)", "names", True),
        ("Price (low to high)", "prices", False),
        ("Price (high to low)", "prices", True),
    ],
)
def test_sort_products(logged_in_page, option, key, reverse):
    logged_in_page.sort_by(option)

    values = getattr(logged_in_page, key)()
    assert values == sorted(values, reverse=reverse)
