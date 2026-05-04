"""
FUNCTIONALITY TESTS - ensures all positive functionalities of the BOT
 ARE WORKING AS EXPECTED eg : amount == 50.5 passes
"""

from expenses_bot_quick import parse_quick_message
import pytest

#1.test to check parse_quick_message() passes with a float amount
@pytest.mark.bot_functionality
@pytest.mark.parametrize("message", [
    "daniel 100.555 car gas "
])
def test_valid_input_with_float_amount(message):
    """parse_quick_message() should pass with a float amount"""

    name, amount, category, note = parse_quick_message(message)
    assert amount == 100.555

#2.test to check parse_quick_message() passes with a int amount
@pytest.mark.bot_functionality
@pytest.mark.parametrize("message", [
    "daniel 100 car gas "
])
def test_valid_input_with_int_amount(message):
    """parse_quick_message() should pass with a int amount"""

    name, amount, category, note = parse_quick_message(message)
    assert amount == 100

#3.test to check parse_quick_message() passes with case insensative names
@pytest.mark.bot_functionality
@pytest.mark.parametrize("message", [
    "DaNiel 100 car gas "
])
def test_case_insensitive_member_name(message): #eg :DaNiel passes in lower case
    """parse_quick_message() should pass with case insensitive member_names eg DaNiel in lower case -> daniel"""

    name, amount, category, note = parse_quick_message(message)
    assert name == "daniel"