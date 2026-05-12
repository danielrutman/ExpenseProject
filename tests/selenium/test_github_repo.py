"""SELENIUM TEST FILE FOR EXPENSES BOT
checks that the github repo is public and contains the correct files"""

import pytest
from selenium.webdriver.chrome.service import Service



GITHUB_URL = "https://github.com/danielrutman/ExpenseProject"

#1.test to check github_repo_is_accessible and public
@pytest.mark.selenium
def test_github_repo_is_accessible(driver):
    """repo should be public and accessible"""
    driver.get(GITHUB_URL)
    assert "ExpenseProject" in driver.title

#2.test to check github_repo_key_files_exist
@pytest.mark.selenium
def test_github_repo_key_files_exist(driver):
    """key project files should be visible in repo"""
    driver.get(GITHUB_URL)
    page = driver.page_source
    assert "expenses_bot.py" in page # our expense bot main()
    assert "locustfile.py" in page  # file that contains bot load test
    assert "conftest.py" in page  # file that contains project fixtures
    assert "expenses_functions" in page  # folder  that contains project core function files excel , bot , python
    assert "tests" in page # folder that contains our project core test files excel , bot , python , e2e