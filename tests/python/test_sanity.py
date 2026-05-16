"""SANITY TESTS TO CHECK CORE FUNCTIONALITY OF
   EXPENSES IF DONT PASS TESTING SHOULD STOP TILL FIXED !"""

import pytest
from expenses_functions.expenses import (
    format_entry,
    is_valid_category,
    get_current_date,
    add_expense
)
from config import (
    VALID_CATEGORIES,
    VALID_MEMBERS
)

# 1. Test that  checks VALID_CATEGORIES is not empty
@pytest.mark.sanity
def test_valid_categories_is_not_empty():
    """VALID_CATEGORIES list should not be empty"""
    assert len(VALID_CATEGORIES) > 0

# 2. Test that  checks VALID_MEMBERS const list  is not empty
@pytest.mark.sanity
def test_valid_members_is_not_empty():
    """VALID_MEMBERS list should not be empty"""
    assert len(VALID_MEMBERS) > 0

# 3. Test that checks format_entry returns a string
@pytest.mark.sanity
def test_format_entry_is_a_string():
    """format_entry() should return a string"""
    result = format_entry("דניאל",50,"gas")
    assert isinstance(result, str)

# 4. Test that checks  is_valid_category returns a boolean
@pytest.mark.sanity
def test_is_valid_category_returns_boolean():
    """is_valid_category() should return a boolean"""
    result = is_valid_category("מצרכים ופארם")
    assert isinstance(result, bool)

#5. Test that that checks get_current_date returns a string
@pytest.mark.sanity
def test_get_current_date_returns_string():
    """get_current_date() should return a string"""
    result = get_current_date()
    assert isinstance(result, str)

#6. Test that that checks add_expense returns a string
@pytest.mark.sanity
def test_add_expense_returns_string():
    """add_expense() should return a string"""
    result = add_expense("דניאל", 50, "מצרכים ופארם", "gas")
    assert isinstance(result, str)
