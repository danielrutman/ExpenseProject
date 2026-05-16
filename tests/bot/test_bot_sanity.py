"""SANITY TESTS TO CHECK CORE FUNCTIONALITY OF
   EXPENSES BOT FUNCTIONALITY  IF DONT PASS TESTING SHOULD STOP TILL FIXED !"""

import pytest
from expenses_functions.expenses_bot_quick import parse_quick_message

#1.test to check parse_quick_message() returns 4 values if not there is no reason to continue
@pytest.mark.bot_sanity
def test_parse_quick_message_returns_4_values():
    """parse_quick_message() should return 4 values """

    name, amount, category, note = parse_quick_message("דניאל 50 רכב gas")
    assert name == "דניאל"
    assert amount == 50
    assert category == "רכב"
    assert note == "gas"


