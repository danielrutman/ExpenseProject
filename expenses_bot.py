"""MAIN BOT FILE - contains Flask app, welcome_message() and main_router()"""

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from expenses_functions.expenses_bot_modes import bot_quick_mode, bot_guided_mode
from expenses_functions.expenses_bot_guided import get_session, update_session, is_session_expired
from expenses_functions.expenses_bot_quick import show_quick_mode_instructions
from expenses_functions.expenses_excel import  generate_report
from config import FILE_PATH
app = Flask(__name__) # creates a Flask application instance

def show_welcome_message():
    """show welcome message"""

    return (
         "👋 Welcome to Expense Bot!\n"
        "How would you like to proceed?\n\n"
        "1 - ⚡ Quick mode\n"
        "2 - 📋 Guided mode\n"
        "if at any moment you would like to return to the main page please 'write welcome' "

    )

@app.route("/bot", methods=["POST"])
def main_router():
    """bot main router gives the user the ability to send messages
    in one of the following formats: quick mode, guided mode"""

    phone = request.form.get("From")
    incoming_msg = request.form.get("Body").strip()
    response = MessagingResponse()
    msg = response.message()
    session = get_session(phone)

    # user may request monthly report at any time of current spending state
    if incoming_msg.strip().lower() == "report":
        msg.body(generate_report(FILE_PATH))
        return str(response)

    #in case user wants to go back to welcome session at any given moment he should write welcome
    if incoming_msg.lower() == "welcome":
        update_session(phone, "waiting_for_mode")
        msg.body(show_welcome_message())

    # No session or expired — reset and greet user fresh
    elif not session or is_session_expired(phone):
        update_session(phone, "waiting_for_mode")
        msg.body(show_welcome_message())

    # User has been greeted — waiting to pick a mode (1 or 2)
    elif session["state"] == "waiting_for_mode":
        if incoming_msg == "1":
            update_session(phone, "quick_mode")
            msg.body(show_quick_mode_instructions())
        elif incoming_msg == "2":
            update_session(phone, "waiting_for_name")
            msg.body("What is your name?\n1 - Daniel\n2 - Inbar")
        else:
            msg.body("Please choose 1 or 2")

    # Quick mode — single message format
    elif session["state"] == "quick_mode":
        msg.body(bot_quick_mode(phone, incoming_msg))

    # User finished saving — ask if they want to add another
    elif session["state"] == "waiting_for_repeat":
        if incoming_msg == "1":
            previous_mode = session.get("previous_mode")
            if previous_mode == "quick_mode":
                update_session(phone, "quick_mode")
                msg.body(show_quick_mode_instructions())
            else:
                update_session(phone, "waiting_for_name")
                msg.body("👤 What is your name?\n1 - דניאל\n2 - ענבר")
        elif incoming_msg == "2":
            update_session(phone, "waiting_for_mode")
            msg.body(show_welcome_message())
        else:
            msg.body("Please choose 1 or 2")

    # Guided mode — multi-step flow
    else:
        msg.body(bot_guided_mode(phone, incoming_msg, session))

    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True) # 0.0.0.0 means listen on all interfaces — making Flask accessible from outside the container.
