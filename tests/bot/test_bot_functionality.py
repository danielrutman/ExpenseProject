"""
FUNCTIONALITY TESTS - ensures all positive functionalities of the BOT
 ARE WORKING AS EXPECTED eg : amount == 50.5 passes
"""

from expenses_functions.expenses_bot_guided import load_sessions, update_session, get_session, clear_session, is_session_expired
from datetime import datetime
from expenses_functions.expenses_bot_quick import parse_quick_message
import pytest

#1.test to check parse_quick_message() passes with a float amount
@pytest.mark.bot_functionality
@pytest.mark.parametrize("message", [
    "דניאל 100.555 רכב gas "
])
def test_valid_input_with_float_amount(message):
    """parse_quick_message() should pass with a float amount"""

    name, amount, category, note = parse_quick_message(message)
    assert amount == 100.555

#2.test to check parse_quick_message() passes with a int amount
@pytest.mark.bot_functionality
@pytest.mark.parametrize("message", [
    "דניאל 100 רכב gas "
])
def test_valid_input_with_int_amount(message):
    """parse_quick_message() should pass with a int amount"""

    name, amount, category, note = parse_quick_message(message)
    assert amount == 100

#3.test to check parse_quick_message() passes with case insensative names
@pytest.mark.bot_functionality
@pytest.mark.parametrize("message", [
    "דניאל 100 רכב gas "
])
def test_case_insensitive_member_name(message): #eg :DaNiel passes in lower case
    """parse_quick_message() should pass with case insensitive member_names eg DaNiel in lower case -> daniel"""

    name, amount, category, note = parse_quick_message(message)
    assert name == "דניאל"

# 4. test to check load_sessions() returns empty dict when no file exists
@pytest.mark.bot_functionality
def test_load_sessions_returns_empty_dict_when_no_file(tmp_path, monkeypatch):
    """load_sessions() should return empty dict if sessions.json doesn't exist"""

    monkeypatch.setattr("expenses_functions.expenses_bot_guided.SESSION_FILE", str(tmp_path / "sessions.json"))
    result = load_sessions()
    assert result == {}

# 5. test to check update_session() creates a new session correctly
@pytest.mark.bot_functionality
def test_update_session_creates_new_session(tmp_path, monkeypatch,mock_phone):
    """update_session() should create a new session with correct state"""

    monkeypatch.setattr("expenses_functions.expenses_bot_guided.SESSION_FILE", str(tmp_path / "sessions.json"))
    update_session(mock_phone, "waiting_for_mode")
    session = get_session(mock_phone)
    assert session["state"] == "waiting_for_mode"

# 6. test to check update_session() updates an existing session
@pytest.mark.bot_functionality
def test_update_session_updates_existing_session(tmp_path, monkeypatch,mock_phone):
    """update_session() should overwrite existing session with new state"""

    monkeypatch.setattr("expenses_functions.expenses_bot_guided.SESSION_FILE", str(tmp_path / "sessions.json"))
    update_session(mock_phone, "waiting_for_mode")
    update_session(mock_phone, "waiting_for_name")
    session = get_session(mock_phone)
    assert session["state"] == "waiting_for_name"

# 7. test to check get_session() returns correct session data
@pytest.mark.bot_functionality
def test_get_session_returns_correct_data(tmp_path, monkeypatch,mock_phone):
    """get_session() should return the session dict for the correct phone number"""

    monkeypatch.setattr("expenses_functions.expenses_bot_guided.SESSION_FILE", str(tmp_path / "sessions.json"))
    update_session(mock_phone, "quick_mode", {"name": "דניאל"})
    session = get_session(mock_phone)
    assert session["name"] == "דניאל"

# 8. test to check get_session() returns None if no session exists
@pytest.mark.bot_functionality
def test_get_session_returns_none_when_no_session(tmp_path, monkeypatch,mock_phone):
    """get_session() should return None if phone number has no session"""

    monkeypatch.setattr("expenses_functions.expenses_bot_guided.SESSION_FILE", str(tmp_path / "sessions.json"))
    result = get_session(mock_phone)
    assert result is None

# 9. test to check clear_session() removes the session
@pytest.mark.bot_functionality
def test_clear_session_removes_session(tmp_path, monkeypatch,mock_phone):
    """clear_session() should remove the session for the given phone number"""

    monkeypatch.setattr("expenses_functions.expenses_bot_guided.SESSION_FILE", str(tmp_path / "sessions.json"))
    update_session(mock_phone, "waiting_for_name")
    clear_session(mock_phone)
    result = get_session(mock_phone)
    assert result is None

# 10. test to check is_session_expired() returns False for a fresh session
@pytest.mark.bot_functionality
def test_session_is_not_expired_when_fresh(tmp_path, monkeypatch,mock_phone):
    """is_session_expired() should return False for a newly created session"""

    monkeypatch.setattr("expenses_functions.expenses_bot_guided.SESSION_FILE", str(tmp_path / "sessions.json"))
    update_session(mock_phone, "waiting_for_mode")
    assert is_session_expired(mock_phone) is False