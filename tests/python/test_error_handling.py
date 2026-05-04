""" THIS FILE CONTAINS ERROR HANDLING TESTS
eg: when entering invalid member we should get ValueError(f"{name} is not a valid family member" """

import pytest
from expenses import (
    format_entry,
    is_valid_category,
    validate_member,
    get_current_date,
    add_expense,
    validate_amount,

)
from config import (
    VALID_CATEGORIES,
    VALID_MEMBERS
)

#1. test to check valid_members() raise ValueError(f"{name} is not a valid family member") for invalid members
@pytest.mark.error_handling
@pytest.mark.parametrize("member", ["mark","teddy",""])
def test_invalid_member_raises_value_error(member):
    with pytest.raises(ValueError, match=f"{member} is not a valid family member"):
        validate_member(member)

#2. test to check is_valid_category raises(ValueError, match=f"{category} is not a valid categories" for invalid category
@pytest.mark.error_handling
@pytest.mark.parametrize("category", ["work", "123", "@","",])
def test_invalid_category_raises_value_error(category):
    with pytest.raises(ValueError, match=f"{category} is not a valid category"):
        is_valid_category(category)

# 3a.  test to check negative/zero amounts —  rasises value error with "Amount must be positive" eg : 0 , -1 , -1.1
@pytest.mark.error_handling
@pytest.mark.parametrize("amount", [-1, -2.2, 0])
def test_negative_amount_error_message(amount):
    with pytest.raises(ValueError, match="Amount must be positive"):
        validate_amount(amount)

# 3b. test to check non-numeric amounts — raises value error with "Amount must be a number" eg: ? , abc etc ...
@pytest.mark.error_handling
@pytest.mark.parametrize("amount", ["", "abc", "#?!"])
def test_non_numeric_amount_error_message(amount):
    with pytest.raises(ValueError, match="Amount must be a number"):
        validate_amount(amount)

#4a. test to check that the user cant add different valid expenses  with invalid member
@pytest.mark.error_handling
@pytest.mark.parametrize("name", ["mark", "teddy", ""])

def test_add_expense_with_invalid_member(name):
    with pytest.raises(ValueError, match=f"{name} is not a valid family member"):
        add_expense(name, 50, "groceries", "gas")


#4b. test to check that the user cant add different valid expenses  with invalid category
@pytest.mark.error_handling
@pytest.mark.parametrize("category", ["temu", "amazon", ""])
def test_add_expense_invalid_category_error_message(category):
    with pytest.raises(ValueError, match=f"{category} is not a valid category"):
        add_expense("daniel", 50, category, "other")




