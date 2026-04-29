"""CONFTEST DOC CONTAINS REUSABLE FIXTURES ACROSS  OUR PROJ """

import pytest

@pytest.fixture
def mock_date():
    return "22 April 2026"



@pytest.fixture
def mock_sheet_name():
    return "April 2026"

@pytest.fixture
def mock_new_month_sheet_name():
    return "May 2026"

@pytest.fixture
def mock_new_month_date():
    return "22 May 2026"




