"""CONFTEST DOC CONTAINS REUSABLE FIXTURES ACROSS  OUR PROJ """

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from expenses_bot import app


@pytest.fixture
def mock_date():
    """returns a fixed mock date string for testing"""
    return "22 April 2026"


@pytest.fixture
def mock_sheet_name():
    """returns a fixed mock sheet name for testing"""
    return "April 2026"

@pytest.fixture
def mock_new_month_sheet_name():
    """returns a fixed mock sheet name for a new month"""
    return "May 2026"

@pytest.fixture
def mock_new_month_date():
    """returns a fixed mock date string for a new month"""
    return "22 May 2026"


@pytest.fixture
def mock_phone():
    """returns a fixed mock phone number for testing"""
    return "+972501234567"


@pytest.fixture
def client():
    """function to create and return a client object"""

    # enable Flask testing mode — surfaces real exceptions instead of hiding them
    app.config["TESTING"] = True
    # create a fake HTTP client that simulates POST requests to /bot
    # without needing a real running server or real Twilio connection
    with app.test_client() as client:
        yield client  # hand the client to each test that requests it

@pytest.fixture
def driver(): # for selenium tests
    """creates and returns a Chrome webdriver instance"""
    # automatically installs correct ChromeDriver version
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver # hands the browser to the test function
    # teardown - close browser after test
    driver.quit()
