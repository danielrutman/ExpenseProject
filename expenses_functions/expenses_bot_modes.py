"""CONTAINS THE 2 BOT MODE WRAPPED FUNCTIONS QUICK MODE / GUIDED MODE"""

from expenses_functions.expenses_bot_quick import parse_quick_message
from expenses_functions.expenses_bot_guided import update_session
from expenses_functions.expenses import validate_member, is_valid_category, validate_amount, get_current_date
from expenses_functions.expenses_excel import save_expense_to_excel
from config import FILE_PATH, VALID_CATEGORIES

#1.quick mode bot func
def bot_quick_mode(phone,incoming_msg):
    """handles quick mode expense saving
    returns response string"""

    try:
        name, amount, category, note = parse_quick_message(incoming_msg)
        #if parse_quick_message(incoming_msg) is succsesfull we pass the params to save to excel for further handling
        remaining = save_expense_to_excel(name, category, amount, note, FILE_PATH)
        update_session(phone, "waiting_for_repeat", {"previous_mode": "quick_mode"})
        #if save_expense_to_excel is succsesfull the bot creates a response message back to user
        return (
            "Expense saved! ✅\n"
            f"👤 Name: {name}\n"
            f"💰 Amount: {amount} NIS\n"
            f"🏷️ Category: {category}\n"
            f"📝 Note: {note}\n"
            f"📅 Date: {get_current_date()}\n\n"
            f"💵 Remaining budget: {remaining} NIS\n\n"
            "Would you like to add another expense?\n"
            "1 - Yes ➕\n"
            "2 - No, return to main menu 🏠"
        )
    except ValueError as e:
        return str(e)

#2 guided bot main func to wrap its functionality
def bot_guided_mode(phone, incoming_msg, session):
    """guides expenses project bot function
    first asks for name than category than amount and finaly note
    returns-->  "Expense saved!\n"
                f"Name: {name}\n"
                f"Amount: {amount} NIS\n"
                f"Category: {category}\n"
                f"Note: {note}\n"
                f"Date: {get_current_date()}"""

    state = session["state"]

    if state == "waiting_for_name":
    # validate name, ask for category
        try:
            #take input for name from user and validate with validate_member() change state to wait for category
            name = validate_member(incoming_msg)  # validate the message as name
            update_session(phone, "waiting_for_category", {"name": name})  # save name, move to next state
            category_list = "\n".join(f"• {cat}" for cat in VALID_CATEGORIES)
            return f"👤 Got it {name}! Please choose a category:\n{category_list}"
        except ValueError as e:
            return str(e)  # send error back if invalid name

    elif state == "waiting_for_category":
    # validate category, ask for amount
        try:
            #take input from user for category and validate with is_valid_category() change state to wait for amount
            category = incoming_msg.strip().lower()
            is_valid_category(category) # validate category
            update_session(phone, "waiting_for_amount", {
                "name": session["name"],  # keep existing name
                "category": category  # add new category
            }) # save category, move to next state
            return f"🏷️ Got it {category}! Please enter an amount:\n"
        except ValueError as e:
            return str(e)  # send error back if invalid name

    elif state == "waiting_for_amount":
    # validate amount, ask for note
        try:
            #recieve amount from user and validate with validate_amount() change state to wait for note
            amount = float(incoming_msg)
            if amount == int(amount):
                amount = int(amount)
            validate_amount(amount)
            update_session(phone, "waiting_for_note", {
                "name": session["name"],  # keep existing name
                "category": session["category"], # keep existing category
                "amount": amount # add new amount
            })  # save amount, move to next state
            return f"💰 Got it {amount} NIS! Any notes?\n"
        except ValueError as e:
            return str(e)  # send error back if invalid name

    elif state == "waiting_for_note":
        # recieve note for user and save expense to excel
        note = incoming_msg.strip()
        name = session["name"]
        category = session["category"]
        amount = session["amount"]
        remaining = save_expense_to_excel(name, category, amount, note, FILE_PATH)
        update_session(phone, "waiting_for_repeat", {"previous_mode": "guided_mode"})

        # after expense was saved to excel friendly message will be returned to user
        return (
            "Expense saved! ✅\n"
            f"👤 Name: {name}\n"
            f"💰 Amount: {amount} NIS\n"
            f"🏷️ Category: {category}\n"
            f"📝 Note: {note}\n"
            f"📅 Date: {get_current_date()}\n\n"
            f"💵 Remaining budget: {remaining} NIS\n\n"
            "Would you like to add another expense?\n"
            "1 - Yes ➕\n"
            "2 - No, return to main menu 🏠"
        )
