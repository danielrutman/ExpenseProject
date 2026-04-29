"""CORE EXPENSES FUNCTION FILE contains
all the important functions for expenses project"""

import openpyxl
import os

VALID_CATEGORIES = ["car", "bills", "fun", "groceries", "child", "dogs", "other"]
VALID_MEMBERS = ["daniel", "inbar"]
NORMAL_LOAD = 100
MAX_LOAD = 1000
STRESS_LOAD = 10000
NORMAL_RUN_TIME = 1
MAX_RUN_TIME = 2
STRESS_RUN_TIME = 5
FILE_PATH = "expenses_table.xlsx"
EXCEL_HEADER = ["Date","User","Category","Amount","Note"]


def format_entry(name, amount, note):
    """ Formats an expense entry into a readable string.
     Returns str: Formatted string e.g. "Daniel 50 gas"""

    return f"{name} {amount} {note}"


def is_valid_category(category):
    """ Returns True if category is valid
    raises ValueError if category is not a valid category."""

    if category is None:
        raise ValueError("Category cannot be None")

    if category.strip().lower() not in VALID_CATEGORIES:
        raise ValueError(f"{category} is not a valid category")

    return category.strip().lower() in VALID_CATEGORIES

def validate_member(name):
    """ Validates family member name. Returns name in lowercase if valid.
    Raises ValueError if name is not a registered family member. """
    if name is None:
        raise ValueError("Name cannot be None")

    if name.strip().lower() not in VALID_MEMBERS:
        raise ValueError(f"{name} is not a valid family member")
    return name.strip().lower()

def add_expense(name, amount, category, note):
    """ Adds an expense to the expenses table
    eg : Saved daniel 50 gas to car in 22 April 2026 """

    validate_member(name)
    is_valid_category(category)

    entry = format_entry(name, amount, note)
    month = get_current_date()
    return f"Saved {entry} to {category} in {month}"

def get_current_date():
    """ Returns the current date in string format
    eg : "22 April 2026 """

    from datetime import datetime
    return datetime.now().strftime("%d %B %Y")  # "22 April 2026"

def validate_amount(amount):
    """ Validates expense amount. Returns amount if valid.
    Raises ValueError if amount is not a number or is less than or equal to 0. """

    if amount is None:
        raise ValueError("amount cannot be None")

    if not isinstance(amount, (int, float)):
        raise ValueError(f"{amount} Amount must be a number")
    if amount <= 0:
        raise ValueError(f"{amount} Amount must be positive")
    return amount

"""BELOW ARE FUNCTIONS FOR  EXCEL TABLE HANDLING"""

def open_file(FILE_PATH):
    """Opens existing Excel file or creates new one if doesn't exist.
    Returns workbook object."""

    if os.path.exists(FILE_PATH):
        return openpyxl.load_workbook(FILE_PATH)
    else:
        wb = openpyxl.Workbook()
        del wb[wb.sheetnames[0]]  # delete default sheet otherwise will have 2 sheets from start
        return wb

def get_or_create_sheet(wb, sheet_name):
    """Gets existing sheet or creates new one if doesn't exist.
    Returns worksheet object."""

    # wb.sheetnames  returns a list of all worksheet names in a loaded workbook
    if sheet_name in wb.sheetnames:
        return wb[ sheet_name]
    else:
        # wb.create_sheet(sheet_name) method in openpyxl is used to add a new worksheet to an existing workbook object
        return wb.create_sheet(sheet_name)


def write_headers(ws):
    """Writes column headers to row 1 of the sheet.
    Only called when sheet is newly created."""

    #excel columns start at index 1 thats why start is 1 for col, header in  will insert eg: c1 = "Date",c2 = "User" etc
    for col, header in enumerate(EXCEL_HEADER, start=1):
        #ws.cell For each header in our list, write it into row 1 at the correct column position.
        ws.cell(row=1, column=col, value=header)

def get_sheet_name():
    """Returns current month and year as sheet name.
    eg: 'April 2026'"""

    from datetime import datetime
    return datetime.now().strftime("%B %Y")  # "April 2026"



def save_expense_to_excel(name, category, amount, note, FILE_PATH):
    """saves expense to excel file."""

    sheet_name = get_sheet_name()

    #1. open or create excel file
    wb = open_file(FILE_PATH)
    #2. check if sheet exists create it if doesnt eg: april 2026
    ws = get_or_create_sheet(wb, sheet_name)
    if ws["A1"].value is None:
        #3. create headers if the sheet is new from const list EXCEL_HEADER
        write_headers(ws)
    #4.append data to sheet new raw
    ws.append([get_current_date(), name, category, amount, note])
    wb.save(FILE_PATH)







