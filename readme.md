# Family Expense Tracker Bot

## Description
A WhatsApp bot that tracks family expenses and stores them in an Excel spreadsheet.
Built by DanielRutman as a learning project to practice Python, pytest, and automation.

## Tech Stack
- Python 3.12
- pytest — automated testing
- openpyxl — Excel integration 
- Twilio — WhatsApp bot integration (coming)
- Docker — containerization (coming)
- GitHub Actions — CI/CD (coming)
- AWS EC2 — deployment (coming)

## Project Structure

ExpenseProject/
├── expenses.py          # core logic
├── conftest.py          # shared fixtures
├── pytest.ini           # pytest configuration
├── README.md            # project documentation
└── tests/
├── test_sanity.py         # smoke tests ✅
├── test_validation.py     # negative testing ✅
├── test_functionality.py  # positive testing ✅
├── test_error_handling.py # error message testing ✅
├── test_edge_cases.py     # boundary testing ✅
├── test_load.py           # load testing ✅
├── test_excel_sanity.py      # excel sanity tests ✅
├── test_excel_functionality.py  # excel functionality tests ✅
├── test_bot.py            # whatsapp bot (coming)
└── test_e2e.py            # end to end (coming)

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

# Run with verbose output
pytest -v

# Generate HTML report
pytest --html=reports/results_report.html --self-contained-html

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


## Test Documentation
STD (Software Test Document) is maintained in Google Sheets:
[Expense Project STD](https://docs.google.com/spreadsheets/d/1hNtPti5yw5r6y07iU7BEoJLcB2uskqmu85_cSE7KYfs/edit?gid=0#gid=0)

## Test Results
| Suite | Tests | Status |
|---|---|---|
| Sanity | 6 | ✅ Pass |
| Validation | 4 | ✅ Pass |
| Functionality | 4 | ✅ Pass |
| Error Handling | 3 | ✅ Pass |
| Edge Cases | 5 | ✅ Pass |
| Load | 3 | ✅ Pass |
| Excel Sanity | 4 | ✅ Pass |
| Excel Functionality | 4 | ✅ Pass |
| Total | 76 | ✅ All Pass |

## Roadmap
- [x] Core Python logic
- [x] Full test suite (76 tests across 8 suites)
- [x] Load testing (normal/max/stress)
- [x] Excel integration with openpyxl
- [ ] WhatsApp bot with Twilio
- [ ] Docker containerization
- [ ] CI/CD with GitHub Actions
- [ ] AWS EC2 deployment



