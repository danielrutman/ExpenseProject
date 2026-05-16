"""
VALIDATION TESTS - Ensures all invalid inputs are rejected
Any invalid member, category or amount must be rejected by the system
"""

# re is Python's regular expressions library used for pattern matching on strings. used in test 4
import re
import pytest
from expenses_functions.expenses import (
    validate_member,
    validate_amount,
    is_valid_category,
    get_current_date
)


#1. test to check invalid members raise a value error in validate_member()
@pytest.mark.validation
@pytest.mark.parametrize("member", ["david", "moshe", "", "שרה"])
def test_invalid_members(member):
    """invalid members should raise a ValueError"""
    with pytest.raises(ValueError):
        validate_member(member)

#2. test to check invalid category raises value error
@pytest.mark.validation
@pytest.mark.parametrize("category", ["candy", "clubs", "", "tables"])
def test_invalid_category(category):
    """invalid categories should raise a ValueError"""
    with pytest.raises(ValueError):
        is_valid_category(category)

#3. test to check invalid amounts raise value error for validate_amount()
@pytest.mark.validation
@pytest.mark.parametrize("amount", [-1,"#","10?",""])
def test_invalid_amount(amount):
    """invalid amounts should raise a ValueError"""
    with pytest.raises(ValueError):
        validate_amount(amount)

#4. test to check get_current_date() returns correct format "DD Month YYYY"
@pytest.mark.validation
def test_date_format_is_correct():
    """get_current_date() should return a string matching DD Month YYYY format"""
    result = get_current_date()
    # \d{2} exactly 2 digits \w+one or more word characters \d{4}exactly 4 digits
    assert re.match(r"\d{2} \w+ \d{4}", result)
