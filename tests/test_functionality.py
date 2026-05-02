"""
FUNCTIONALITY TESTS - ensures all positive functionalities are
passing by the system ex : groceries is a valid category
"""


import pytest
from expenses import (
    format_entry,
    is_valid_category,
    validate_member,
    get_current_date,
    add_expense,
    validate_amount
)
from config import (
    VALID_CATEGORIES,
    VALID_MEMBERS
)


#1. test to check valid_members() passes with valid memebers
@pytest.mark.functionality
@pytest.mark.parametrize("member", ["daniel","inbar"])
def test_valid_members(member):
    assert validate_member(member) == member


#2. test to check is_valid_category passes with the correct categories
@pytest.mark.functionality
@pytest.mark.parametrize("category", ["car", "bills", "fun", "groceries", "child", "dogs", "other"])
def test_valid_category(category):
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
        ("daniel", 50, "car", "gas", "Saved daniel 50 gas to car in 22 April 2026"),
        ("daniel", 50, "groceries", "food", "Saved daniel 50 food to groceries in 22 April 2026"),
        ("daniel", 50, "dogs", "dog food", "Saved daniel 50 dog food to dogs in 22 April 2026"),
        ("daniel", 50, "fun", "bar", "Saved daniel 50 bar to fun in 22 April 2026"),
        ("inbar", 50, "child", "diapers", "Saved inbar 50 diapers to child in 22 April 2026"),
        ("inbar", 50, "other", "flowers", "Saved inbar 50 flowers to other in 22 April 2026"),
    ]
)
def test_add_expense(name, amount, category, note, expected, monkeypatch,mock_date):
    # mock date with built in pytest mock  monkeypatch
    monkeypatch.setattr("expenses.get_current_date", lambda: mock_date)

    result = add_expense(name, amount, category, note)

    assert result == expected