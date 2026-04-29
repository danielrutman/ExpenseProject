"""SANITY TESTS TO CHECK CORE FUNCTIONALITY OF
   EXPENSES IF DONT PASS TESTING SHOULD STOP TILL FIXED !"""

import pytest
from expenses import (
    format_entry,
    is_valid_category,
    validate_member,
    get_current_date,
    add_expense,
    VALID_CATEGORIES,
    VALID_MEMBERS
)

# 1. Test that  checks VALID_CATEGORIES is not empty
@pytest.mark.sanity
def test_valid_categories_is_not_empty():
    assert len(VALID_CATEGORIES) > 0

# 2. Test that  checks VALID_MEMBERS const list  is not empty
@pytest.mark.sanity
def test_valid_members_is_not_empty():
     assert len(VALID_MEMBERS) > 0

# 3. Test that checks format_entry returns a string
@pytest.mark.sanity
def test_format_entry_is_a_string():
    result = format_entry("daniel",50,"gas")
    assert isinstance(result, str)

# 4. Test that checks  is_valid_category returns a boolean
@pytest.mark.sanity
def test_is_valid_category_returns_boolean():
    result = is_valid_category("groceries")
    assert isinstance(result, bool)

#5. Test that that checks get_current_date returns a string
@pytest.mark.sanity
def test_get_current_date_returns_string():
    result = get_current_date()
    assert isinstance(result, str)

#6. Test that that checks add_expense returns a string
@pytest.mark.sanity
def test_add_expense_returns_string():
    result = add_expense("daniel", 50, "groceries", "gas")
    assert isinstance(result, str)