# -*- coding: utf-8 -*-

"""Configuration file for expenses project contains all the
CONSTANTS FOR EXPENSES PROJECT"""

import os

# Member and category constants
VALID_MEMBERS = ["דניאל", "daniel", "inbar","ענבר"]
VALID_CATEGORIES = [
    "מצרכים ופארם",
    "רכב",
    "ביטוחים ומנויים",
    "כלבים",
    "חשבונות בית",
    "הדר",
    "ענבר",
    "דניאל",
    "פנאי ויציאות"
]
# Load test constants
NORMAL_LOAD = 100
MAX_LOAD = 1000
STRESS_LOAD = 10000
NORMAL_RUN_TIME = 1
MAX_RUN_TIME = 2
STRESS_RUN_TIME = 5

# Excel constants
FILE_PATH = "/tmp/expenses_table.xlsx" if os.environ.get("AWS_LAMBDA_FUNCTION_NAME") else "expenses_table.xlsx"
EXCEL_HEADER = ["Date", "User", "Category", "Amount", "Note"]
MONTHLY_BUDGET = 9000

#Bot constants
import os

# use /tmp on Lambda, local path otherwise
SESSION_FILE = "/tmp/sessions.json" if os.environ.get("AWS_LAMBDA_FUNCTION_NAME") else "sessions.json"

GITHUB_URL = "https://github.com/danielrutman/ExpenseProject"

# S3 bucket for persistent storage (Lambda only)
S3_BUCKET = "expense-bot-data-115643029932" if os.environ.get("AWS_LAMBDA_FUNCTION_NAME") else None
S3_KEY = "expenses_table.xlsx"