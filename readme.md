# Family Expense Tracker Bot

## Description
A WhatsApp bot that tracks family expenses and stores them in an Excel spreadsheet.
Built by DanielRutman as a learning project to practice Python, pytest, and automation.
## Tech Stack
- Python 3.12
- pytest — automated testing
- openpyxl — Excel integration 
- Flask — WhatsApp bot web framework
- Twilio — WhatsApp bot integration
- Locust — load testing
- Selenium — UI testing -> (doesnt test the bot itself)
- Docker — containerization (coming)
- GitHub Actions — CI/CD (coming)
- AWS Lambda — deployment (coming)

## Project Structure
ExpenseProject/
├── expenses_bot.py              # Flask app + main_router() — entry point
├── config.py                    # all constants
├── conftest.py                  # shared fixtures
├── pytest.ini                   # pytest configuration
├── requirements.txt             # dependencies
├── readme.md                    # project documentation
├── sessions.json                # WhatsApp session state (gitignored)
├── expense_bot_flow_diagram.svg # bot flow diagram
│
├── expenses_functions/          # core logic
│   ├── expenses.py
│   ├── expenses_excel.py
│   ├── expenses_bot_guided.py
│   ├── expenses_bot_modes.py
│   └── expenses_bot_quick.py
│
└── tests/
    ├── test_e2e.py
    ├── selenium/
    │ └── test_github_repo.py
    ├── python/
    │   ├── test_sanity.py
    │   ├── test_validation.py
    │   ├── test_functionality.py
    │   ├── test_error_handling.py
    │   ├── test_edge_cases.py
    │   └── test_load.py
    ├── excel/
    │   ├── test_excel_sanity.py
    │   └── test_excel_functionality.py
    └── bot/
        ├── test_bot_sanity.py
        ├── test_bot_error_handling.py
        └── test_bot_functionality.py


## How To Run Tests
```bash
# Run all tests
pytest

# Run specific suite
pytest -m sanity
pytest -m validation
pytest -m functionality
pytest -m error_handling
pytest -m edge_cases
pytest -m load
pytest -m excel_sanity
pytest -m excel_functionality
pytest -m bot_sanity
pytest -m bot_error_handling
pytest -m bot_functionality

# Run with verbose output
pytest -v

# Generate HTML report
pytest --html=reports/results_report.html --self-contained-html

#Generate HTML test coverage report  into coverage_report folder
pytest --cov=. --cov-report=html:coverage_reports
# to open use below cmd
xdg-open coverage_reports/index.html

# Generate Allure report more  detailed report with charts and more friendly GUI
# Clear old allure data first
rm -rf reports/allure/*
pytest --alluredir=reports/allure
allure serve reports/allure

# Run the WhatsApp bot locally
# Terminal 1 - Start Flask
source venv/bin/activate
python expenses_bot.py

# Terminal 2 - Start ngrok tunnel
ngrok http 5000

# Run Locust load tests
# Terminal 1 - Start Flask
python3 expenses_bot.py
# Terminal 2 - Start Locust
locust -f locustfile.py --host=http://localhost:5000
# Open http://localhost:8089


# Run everything except load tests
pytest -m "not load"
```

## Test Suites
| Suite | File | Description |
|---|---|---|
| Sanity | test_sanity.py | Core smoke tests — run first |
| Validation | test_validation.py | Invalid input rejection |
| Functionality | test_functionality.py | Happy path testing |
| Error Handling | test_error_handling.py | Correct error messages |
| Edge Cases | test_edge_cases.py | Boundaries and unusual inputs |
| Load | test_load.py | Performance & stability testing |
| Excel Sanity | test_excel_sanity.py | Excel smoke tests |
| Excel Functionality | test_excel_functionality.py | Excel happy path |
| Bot Sanity | test_bot_sanity.py | Bot smoke tests |
| Bot Error Handling | test_bot_error_handling.py | Bot error cases |
| Bot Functionality | test_bot_functionality.py | Bot happy path |
| E2E | test_e2e.py | Full flow end to end tests |
| Bot Locust Load | locustfile.py | Real HTTP load testing |
| Selenium | test_github_repo.py | GitHub repo UI tests (excluded by default) |


## Test Documentation
STD (Software Test Document) is maintained in Google Sheets:
[Expense Project STD](https://docs.google.com/spreadsheets/d/1hNtPti5yw5r6y07iU7BEoJLcB2uskqmu85_cSE7KYfs/edit?gid=0#gid=0)

## Test Results
| Suite | Tests | Status |
|---|-|---|
| Sanity | 6 | ✅ Pass |
| Validation | 13 | ✅ Pass |
| Functionality | 23 | ✅ Pass |
| Error Handling | 19 | ✅ Pass |
| Edge Cases | 8 | ✅ Pass |
| Load | 3 | ✅ Pass |
| Excel Sanity | 4 | ✅ Pass |
| Excel Functionality | 4 | ✅ Pass |
| Bot Sanity | 1 | ✅ Pass |
| Bot Error Handling | 11 | ✅ Pass |
| Bot Functionality | 10 | ✅ Pass |
| Bot Locust Load | 3 | ✅ Pass |
| E2E |3| ✅ Pass |
| Selenium | 2 | ✅ Pass |
| **Total** | **108** | ✅ All Pass |

## Coverage
- Total coverage: 95%
- Generated with pytest-cov

## Bot Features
- Quick mode — single message format: `name amount category note`
- Guided mode — step by step flow
- Monthly budget tracking — remaining budget shown after each expense
- Session management — 15 minute timeout
- Repeat flow — option to add another expense after saving
- Welcome escape — type "welcome" at any point to return to main menu
- Monthly report — type "report" to see spending per category

## Roadmap
- [x] Core Python logic
- [x] Full test suite (108 tests across 14 suites)
- [x] Load testing (normal/max/stress)
- [x] Excel integration with openpyxl
- [x] WhatsApp bot quick mode (Twilio + Flask)
- [x] WhatsApp bot guided mode
- [x] Session management
- [x] Monthly budget tracking
- [x] E2E tests (Flask test client)
- [x] 98% test coverage
- [x] Locust load tests for bot
- [x] Selenium GitHub repo test
- [x] Monthly report by category
- [ ] Docker containerization
- [ ] CI/CD with GitHub Actions
- [ ] AWS Lambda deployment



