"""
FUNCTIONALITY TESTS - ensures all positive functionalities are
passing by the system ex : groceries is a valid category
"""


import pytest
from expenses_functions.expenses import (
    is_valid_category,
    validate_member,
    add_expense,
    validate_amount
)


#1. test to check valid_members() passes with valid memebers
@pytest.mark.functionality
@pytest.mark.parametrize("member", ["דניאל","ענבר"])
def test_valid_members(member):
    assert validate_member(member) == member


#2. test to check is_valid_category passes with the correct categories
@pytest.mark.functionality
@pytest.mark.parametrize("category", ["רכב", "חשבונות בית", "פנאי ויציאות", "מצרכים ופארם", "הדר", "כלבים", "ביטוחים ומנויים", "דניאל", "ענבר"])
def test_valid_category(category):
    """is_valid_category() should return True for all valid categories"""
    assert is_valid_category(category) == True


#3. test to check validate_amount() passes with  positive values higher than 0 which are float or int
@pytest.mark.functionality
@pytest.mark.parametrize("amount", [1.1, 10, 100, 1000 ])
def test_valid_amount(amount):
    assert validate_amount(amount) == amount

#4. test to check that the user can add different valid expenses with different valid member , categories , notes
@pytest.mark.functionality
@pytest.mark.parametrize(
    "name, amount, category, note, expected",
    [
        ("דניאל", 50, "רכב", "gas", "Saved דניאל 50 gas to רכב in 22 April 2026"),
        ("דניאל", 50, "מצרכים ופארם", "food", "Saved דניאל 50 food to מצרכים ופארם in 22 April 2026"),
        ("דניאל", 50, "כלבים", "dog food", "Saved דניאל 50 dog food to כלבים in 22 April 2026"),
        ("דניאל", 50, "פנאי ויציאות", "bar", "Saved דניאל 50 bar to פנאי ויציאות in 22 April 2026"),
        ("ענבר", 50, "הדר", "diapers", "Saved ענבר 50 diapers to הדר in 22 April 2026"),
        ("ענבר", 50, "ביטוחים ומנויים", "insurance", "Saved ענבר 50 insurance to ביטוחים ומנויים in 22 April 2026"),
        ("דניאל", 50, "דניאל", "personal", "Saved דניאל 50 personal to דניאל in 22 April 2026"),
        ("ענבר", 50, "ענבר", "personal", "Saved ענבר 50 personal to ענבר in 22 April 2026"),
    ]
)
def test_add_expense(name, amount, category, note, expected, monkeypatch,mock_date):
    """add_expense() should return correctly formatted string for valid inputs"""
    # mock date with built in pytest mock  monkeypatch
    monkeypatch.setattr("expenses_functions.expenses.get_current_date", lambda: mock_date)

    result = add_expense(name, amount, category, note)

    assert result == expected