""" THIS FILE CONTAINS ERROR HANDLING TESTS FOR THE BOT PART
eg: when entering invalid member we should get ValueError(f"{name} is not a valid family member" """

from expenses_bot import parse_quick_message
import pytest

#1.test to check invalid member raises value error f"{member} is not a valid family member"
@pytest.mark.bot_error_handling
@pytest.mark.parametrize("member", ["mark","teddy","moshe"])
def test_invalid_member_raises_value_error(member):
    """any member not in the list VALID_MEMBERS  should raise a ValueError"""

    with pytest.raises(ValueError, match=f"{member} is not a valid family member"):
        parse_quick_message(f"{member} 50 car gas")

#2.test to check invalid Category raises a value error f"{category} is not a valid category"
@pytest.mark.bot_error_handling
@pytest.mark.parametrize("category", ["work", "123", "balloons"])
def test_invalid_category_raises_value_error(category):
    """any category not in the list VALID_CATEGORIES  should raise a ValueError
    f"{category} is not a valid category"""

    with pytest.raises(ValueError, match=f"{category} is not a valid category"):
        parse_quick_message(f"daniel 50 {category} gas")


#3. test to check  wrong_number_of_params _raises_value_error eg : "daniel 50 category < 4
@pytest.mark.bot_error_handling
@pytest.mark.parametrize("message", [
    "daniel 50 car",   # too few params
])
def test_wrong_number_of_params_raises_value_error(message):
    """amount of params should be not less than 4
    name amount category note"""

    with pytest.raises(ValueError, match="Wrong format! pass 4 params : name amount category note. Example: daniel 50 car gas"):
        parse_quick_message(message)

#4. test to  check non_numeric_amount_raises_value_error(): -> "Amount must be a number. Example: daniel 50 car gas"
@pytest.mark.bot_error_handling
@pytest.mark.parametrize("message", [
    "daniel abc car gas",  #chars instead of numbers
    "daniel !@#$ car gas ", # special char instead of numbers
    "daniel 123!! car gas ", # mixed nums with chars
])
def test_non_numeric_amount_raises_value_error(message):
    """non numeric amount should raise a ValueError eg abc or @#! or 23!!"""

    with pytest.raises(ValueError, match="Amount must be a number. Example: daniel 50 car gas"):
        parse_quick_message(message)


