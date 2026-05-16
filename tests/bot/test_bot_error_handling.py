""" THIS FILE CONTAINS ERROR HANDLING TESTS FOR THE BOT PART
eg: when entering invalid member we should get ValueError(f"{name} is not a valid family member" """

from unittest.mock import patch
from datetime import datetime, timedelta
import pytest
from expenses_functions.expenses_bot_guided import update_session, is_session_expired
from expenses_functions.expenses_bot_quick import parse_quick_message

#1.test to check invalid member raises value error f"{member} is not a valid family member"
@pytest.mark.bot_error_handling
@pytest.mark.parametrize("member", ["mark","teddy","moshe"])
def test_invalid_member_raises_value_error(member):
    """any member not in the list VALID_MEMBERS  should raise a ValueError"""

    with pytest.raises(ValueError, match=f"{member} is not a valid family member"):
        parse_quick_message(f"{member} 50 רכב gas")

#2.test to check invalid Category raises a value error f"{category} is not a valid category"
@pytest.mark.bot_error_handling
@pytest.mark.parametrize("category", ["work", "123", "balloons"])
def test_invalid_category_raises_value_error(category):
    """any category not in the list VALID_CATEGORIES  should raise a ValueError
    f"{category} is not a valid category"""

    with pytest.raises(ValueError, match=f"{category} is not a valid category"):
        parse_quick_message(f"דניאל 50 {category} gas")


#3. test to check  wrong_number_of_params _raises_value_error eg : "daniel 50 category < 4
@pytest.mark.bot_error_handling
@pytest.mark.parametrize("message", [
    "דניאל 50 רכב",   # too few params
])
def test_wrong_number_of_params_raises_value_error(message):
    """amount of params should be not less than 4
    name amount category note"""

    with pytest.raises(ValueError, match="Wrong format! pass 4 params : name amount category note. Example: daniel 50 car gas"):
        parse_quick_message(message)

#4. test to  check non_numeric_amount_raises_value_error(): -> "Amount must be a number. Example: daniel 50 car gas"
@pytest.mark.bot_error_handling
@pytest.mark.parametrize("message", [
    "דניאל abc רכב gas",  #chars instead of numbers
    "דניאל !@#$ רכב gas ", # special char instead of numbers
    "דניאל 123!! רכב gas ", # mixed nums with chars
])
def test_non_numeric_amount_raises_value_error(message):
    """non numeric amount should raise a ValueError eg abc or @#! or 23!!"""

    with pytest.raises(ValueError, match="Amount must be a number. Example: daniel 50 car gas"):
        parse_quick_message(message)

# 5. test to check is_session_expired() returns True after 15 minutes
@pytest.mark.bot_error_handling
def test_session_is_expired_after_15_minutes(tmp_path, monkeypatch,mock_phone):
    """is_session_expired() should return True if session timestamp is older than 15 minutes"""

    monkeypatch.setattr("expenses_functions.expenses_bot_guided.SESSION_FILE", str(tmp_path / "sessions.json"))
    fake_old_time = datetime.now() - timedelta(minutes=20)
    with patch("expenses_functions.expenses_bot_guided.datetime") as mock_datetime:
        mock_datetime.now.return_value = fake_old_time
        mock_datetime.strptime.side_effect = datetime.strptime
        update_session(mock_phone, "waiting_for_mode")
    assert is_session_expired(mock_phone) is True
