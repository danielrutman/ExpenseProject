"""LOAD TEST CASES FILE
containts all the load cases to check the functionality of the prog under different loads"""

# imported time library for time() - start to measure the run time in the tests
import time
import pytest
from expenses_functions.expenses import (
    add_expense,
)
from config import (
    NORMAL_LOAD,
    MAX_LOAD,
    STRESS_LOAD,
    NORMAL_RUN_TIME,
    MAX_RUN_TIME,
    STRESS_RUN_TIME
)


#1.test to see our prog doesnt crash under normal load  100 SAVED EXPENSES and runs under 1 sec
@pytest.mark.load
@pytest.mark.parametrize(
    "name, amount, category, note, expected",
    [
        ("דניאל", 50, "רכב", "gas", "Saved דניאל 50 gas to רכב in 22 April 2026")
    ]
)
def test_normal_load(name, amount, category, note, expected, monkeypatch,mock_date):
    """system should handle 100 expenses without crashing and run under 1 second"""
    # mock date with built in pytest mock  monkeypatch
    monkeypatch.setattr("expenses_functions.expenses.get_current_date", lambda: mock_date)
    start = time.time()
    for i in range(NORMAL_LOAD):
        result = add_expense(name, amount, category, note)
        assert result == expected
    duration = time.time() - start
    assert duration < NORMAL_RUN_TIME

#2.test to see our prog doesnt crash under normal load  1000 SAVED EXPENSES and runs under 2 sec
@pytest.mark.load
@pytest.mark.parametrize(
    "name, amount, category, note, expected",
    [
        ("דניאל", 50, "רכב", "gas", "Saved דניאל 50 gas to רכב in 22 April 2026")
    ]
)
def test_max_load(name, amount, category, note, expected, monkeypatch,mock_date):
    """system should handle 1000 expenses without crashing and run under 2 seconds"""
    # mock date with built in pytest mock  monkeypatch
    monkeypatch.setattr("expenses_functions.expenses.get_current_date", lambda: mock_date)
    start = time.time()
    for i in range(MAX_LOAD):
        result = add_expense(name, amount, category, note)
        assert result == expected
    duration = time.time() - start
    assert duration < MAX_RUN_TIME


#3.test to see our prog doesnt crash under stress  load  10000 SAVED EXPENSES and runs under 5 sec
@pytest.mark.load
@pytest.mark.parametrize(
    "name, amount, category, note, expected",
    [
        ("דניאל", 50, "רכב", "gas", "Saved דניאל 50 gas to רכב in 22 April 2026")
    ]
)
def test_stress_load(name, amount, category, note, expected, monkeypatch,mock_date):
    """system should handle 10000 expenses without crashing and run under 5 seconds"""
    # mock date with built in pytest mock  monkeypatch
    monkeypatch.setattr("expenses_functions.expenses.get_current_date", lambda: mock_date)
    start = time.time()
    for i in range(STRESS_LOAD):
        result = add_expense(name, amount, category, note)
        assert result == expected
    duration = time.time() - start
    assert duration < STRESS_RUN_TIME
