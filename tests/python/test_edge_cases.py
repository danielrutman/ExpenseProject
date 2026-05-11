"""EDGE CASES FUNCTION FILE
include all the irregular edge cases that stress the system"""

import pytest
from expenses_functions.expenses import (
    is_valid_category,
    validate_member,
    validate_amount,

)

#1. test to check valid_members() raise ValueError for invalid edge cases  None, combined valid n: "danielinbar"
@pytest.mark.edge_cases
@pytest.mark.parametrize("member", [None, "דניאלענבר"])
def test_invalid_member_edge_cases(member):
    with pytest.raises(ValueError):
        validate_member(member)
#1.2 test to check valid_members() should pass for valid categories with spaces " דניאל "
@pytest.mark.edge_cases
def test_valid_members_with_spaces_accepted():
    assert validate_member(" דניאל ") == "דניאל"

#2.test to check is_valid_category() raises ValueError for invalid category edge cases - None and combined category names
@pytest.mark.edge_cases
@pytest.mark.parametrize("category", [None, "רכבכלבים"])
def test_invalid_category_edge_cases(category):
    with pytest.raises(ValueError):
        is_valid_category(category)

#2.2 test to check is_valid_category() should pass for valid categories with spaces  eg: " מצרכים ופארם "
@pytest.mark.edge_cases
def test_valid_category_with_spaces_accepted():
    assert is_valid_category(" מצרכים ופארם ") == True

#3. test to check validate_amount() raise ValueError for invalid edge cases  None,str nums:  " 50 "
@pytest.mark.edge_cases
@pytest.mark.parametrize("amount", [None, " 50 "])
def test_invalid_amount_edge_cases(amount):
    with pytest.raises(ValueError):
        validate_amount(amount)


