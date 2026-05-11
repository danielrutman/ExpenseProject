"""FILE CONTAINS E2E TESTS FOR EXPENSES BOT
CHECKS THE QUICK_MODE AND GUIDED_MODE OF OUR BOT"""

import pytest
from expenses_bot import main_router , show_welcome_message
from expenses_bot_guided import clear_session

#1.E2E quick mode test to check full bot quick_mode
@pytest.mark.bot_e2e
def test_quick_mode_e2e(client, mock_phone):
    """E2E QUICK_MODE TEST FOR EXPENSES BOT"""

    # clear any existing session before starting
    clear_session(mock_phone)

    # Step 1 — user enters whats app and sends his first message -> welcome message expected
    response = client.post("/bot", data={
        "From": mock_phone,
        "Body": "hello"
    })
    assert "Welcome to Expense Bot" in response.data.decode("utf-8")

    # Step 2 — user picks quick mode instructions for quick mode appear
    response = client.post("/bot", data={
        "From": mock_phone,
        "Body": "1"
    })
    assert "Quick mode" in response.data.decode("utf-8")

    # Step 3 — user sends expense in quick format saved expense should appear and remaining monthly budget

    response = client.post("/bot", data={
        "From": mock_phone,
        "Body": "דניאל 50 רכב gas"
    })
    assert "Expense saved" in response.data.decode("utf-8")
    assert "Remaining budget" in response.data.decode("utf-8")

    # Step 4 — user chooses to add another expense
    response = client.post("/bot", data={
        "From": mock_phone,
        "Body": "1"
    })
    # quick mode instructions should reappear
    assert "Quick mode" in response.data.decode("utf-8")

    # Step 5 — user saves a second expense
    response = client.post("/bot", data={
        "From": mock_phone,
        "Body": "דניאל 50 רכב gas"
    })
    assert "Expense saved" in response.data.decode("utf-8")
    assert "Remaining budget" in response.data.decode("utf-8")

    # Step 6 — user chooses not to add another expense, welcome message should reappear
    response = client.post("/bot", data={
        "From": mock_phone,
        "Body": "2"
    })
    assert "Welcome to Expense Bot" in response.data.decode("utf-8")

#2.E2E guided mode test to check full bot guided mode
@pytest.mark.bot_e2e
def test_guided_mode_e2e(client, mock_phone):
    """E2E GUided MODE TEST FOR EXPENSES BOT"""

    # clear any existing session before starting
    clear_session(mock_phone)

    # Step 1 — user enters whats app and sends his first message -> welcome message expected
    response = client.post("/bot", data={
        "From": mock_phone,
        "Body": "hello"
    })
    assert "Welcome to Expense Bot" in response.data.decode("utf-8")

    # Step 2 — user picks guided mode  request for name is expected
    response = client.post("/bot", data={
        "From": mock_phone,
        "Body": "2"
    })
    assert "name" in response.data.decode("utf-8").lower()

    # Step 3 — user sends name next question expected category
    response = client.post("/bot", data={
        "From": mock_phone,
        "Body": "דניאל"
    })
    assert "category" in response.data.decode("utf-8").lower()

    # Step 4 — user sends category  next question for amount is expected
    response = client.post("/bot", data={
        "From": mock_phone,
        "Body": "רכב"
    })
    assert "amount" in response.data.decode("utf-8").lower()

    # Step 5 — user sends amount next question for note is expected
    response = client.post("/bot", data={
        "From": mock_phone,
        "Body": "50"
    })
    assert "notes" in response.data.decode("utf-8").lower()

    # Step 6 — user sends note saved expense + remaining budget expected
    response = client.post("/bot", data={
        "From": mock_phone,
        "Body": "gas"
    })
    assert "Expense saved" in response.data.decode("utf-8")
    assert "Remaining budget" in response.data.decode("utf-8")

    # Step 7 — user chooses to add another expense, name prompt expected to reappear
    response = client.post("/bot", data={
        "From": mock_phone,
        "Body": "1"
    })
    assert "name" in response.data.decode("utf-8").lower()

    # Step 8 — user sends name again
    response = client.post("/bot", data={
        "From": mock_phone,
        "Body": "דניאל"
    })
    assert "category" in response.data.decode("utf-8").lower()

    # Step 9 — user sends category again
    response = client.post("/bot", data={
        "From": mock_phone,
        "Body": "רכב"
    })
    assert "amount" in response.data.decode("utf-8").lower()

    # Step 10 — user sends amount again
    response = client.post("/bot", data={
        "From": mock_phone,
        "Body": "50"
    })
    assert "notes" in response.data.decode("utf-8").lower()

    # Step 11 — user sends note, second expense saved
    response = client.post("/bot", data={
        "From": mock_phone,
        "Body": "gas"
    })
    assert "Expense saved" in response.data.decode("utf-8")
    assert "Remaining budget" in response.data.decode("utf-8")

    # Step 12 — user chooses not to add another expense, welcome message expected to reappear
    response = client.post("/bot", data={
        "From": mock_phone,
        "Body": "2"
    })
    assert "Welcome to Expense Bot" in response.data.decode("utf-8")

#3.E2E welcome escape test — verify "welcome" returns to main screen from any mode
@pytest.mark.bot_e2e
def test_welcome_escape_e2e(client, mock_phone):
    """typing 'welcome' at any point returns user to the main screen"""

    # clear any existing session before starting
    clear_session(mock_phone)

    # Step 1 — first message, welcome expected
    response = client.post("/bot", data={"From": mock_phone, "Body": "hello"})
    assert "Welcome to Expense Bot" in response.data.decode("utf-8")

    # Step 2 — pick quick mode
    response = client.post("/bot", data={"From": mock_phone, "Body": "1"})
    assert "Quick mode" in response.data.decode("utf-8")

    # Step 3 — type welcome from inside quick mode → main screen expected
    response = client.post("/bot", data={"From": mock_phone, "Body": "welcome"})
    assert "Welcome to Expense Bot" in response.data.decode("utf-8")

    # Step 4 — pick guided mode
    response = client.post("/bot", data={"From": mock_phone, "Body": "2"})
    assert "name" in response.data.decode("utf-8").lower()

    # Step 5 — type welcome from inside guided mode → main screen expected
    response = client.post("/bot", data={"From": mock_phone, "Body": "welcome"})
    assert "Welcome to Expense Bot" in response.data.decode("utf-8")