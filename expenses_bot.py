""" BOT  EXPENSES FUNCTION FILE contains
all the  BOT  important functions for expenses project"""

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from expenses import validate_member, is_valid_category, validate_amount, add_expense,get_current_date
from expenses_excel import save_expense_to_excel
from config import FILE_PATH
app = Flask(__name__) # creates a Flask application instance

#1. function to parse quick message from user
def parse_quick_message(message):
    """recives a quick message from the user and parses it"""

    parts = message.split() # "daniel 50 car gas" → ["daniel", "50", "car", "gas"]
    #if len is not 4 means we have more / less params than needed
    if len(parts) != 4:
        raise ValueError("Wrong format! pass 4 params : name amount category note. Example: daniel 50 car gas")
    #whats app accepts str msg from user we need to convert it to num before running our validate amount_func()
    try:
        amount = float(parts[1])
        if amount == int(amount):  # check if it's a whole number
            amount = int(amount)  # 50.0 → 50
    except ValueError:
        raise ValueError("Amount must be a number. Example: daniel 50 car gas")
    category = parts[2].strip().lower()
    note = parts[3].strip()
    name = validate_member(parts[0])    #python func to check its a valid regiesterd member eg: daniel / inbar
    validate_amount(amount) #python func to validate its a valid amount
    is_valid_category(category) # python func to check the category is correct
    return name, amount, category, note


#2.quick mode bot func
@app.route("/bot", methods=["POST"]) #the url route on which flas listens to http post requsest from twillio
def bot_quick_mode():
    """whats app quick_mode_bot function for expenses project
    recieves message from user in quick mode ex: "daniel 50 car gas"
    and parses it if successful
    returns f"Expense saved! {name} {amount} {category} note} {get_current_date()}") else returns error message"""


    incoming_msg = request.form.get("Body")  # get the WhatsApp message
    response = MessagingResponse()           # create Twilio response object
    try:
        name, amount, category, note = parse_quick_message(incoming_msg)

        #if parse_quick_message(incoming_msg) is succsesfull we pass the params to save to excel for further handling

        save_expense_to_excel(name, category, amount, note, FILE_PATH)
        #if save_expense_to_excel is succsesfull the bot creates a response message back to user
        msg = response.message()
        msg.body("Expense saved!\nName: " + name + "\nAmount: " + str(amount) + " NIS\nCategory: " + category + "\nNote: " + note + "\nDate: " + get_current_date())
        # else returns Error message back ot user
    except ValueError as e:
        msg = response.message()
        msg.body(str(e))  # send the error message back to user
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)

