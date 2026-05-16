"""CORE  python  EXPENSES FUNCTION FILE contains
all the important functions for expenses project"""

from config import VALID_CATEGORIES, VALID_MEMBERS



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





