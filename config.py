"""Configuration file for expenses project contains all the
CONSTANTS FOR EXPENSES PROJECT"""

# Member and category constants
VALID_CATEGORIES = ["car", "bills", "fun", "groceries", "child", "dogs", "other"]
VALID_MEMBERS = ["daniel", "inbar"]

# Load test constants
NORMAL_LOAD = 100
MAX_LOAD = 1000
STRESS_LOAD = 10000
NORMAL_RUN_TIME = 1
MAX_RUN_TIME = 2
STRESS_RUN_TIME = 5

# Excel constants
FILE_PATH = "expenses_table.xlsx"
EXCEL_HEADER = ["Date", "User", "Category", "Amount", "Note"]