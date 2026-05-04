"""MAIN BOT FILE - contains Flask app, welcome message and main router"""

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from expenses_bot_modes import bot_quick_mode, bot_guided_mode
from expenses_bot_guided import get_session, update_session, is_session_expired
from expenses_bot_quick import show_quick_mode_instructions
app = Flask(__name__) # creates a Flask application instance

def show_welcome_message():
    """show welcome message"""

    return (
        "Welcome back to Expense Bot!\n"
        "how  you would like to proceed ?:\n"
        "1:quick mode \n"
        "2:guided mode \n"

    )

@app.route("/bot", methods=["POST"])
def main_router():
    phone = request.form.get("From")
    incoming_msg = request.form.get("Body").strip()
    response = MessagingResponse()
    msg = response.message()
    session = get_session(phone)

    if not session or is_session_expired(phone):
        update_session(phone, "waiting_for_mode")
        msg.body(show_welcome_message())

    elif session["state"] == "waiting_for_mode":
        if incoming_msg == "1":
            update_session(phone, "quick_mode")
            msg.body(show_quick_mode_instructions())
        elif incoming_msg == "2":
            update_session(phone, "waiting_for_name")
            msg.body("What is your name?\n1 - Daniel\n2 - Inbar")
        else:
            msg.body("Please choose 1 or 2")

    elif session["state"] == "quick_mode":
        msg.body(bot_quick_mode(incoming_msg))

    else:
        msg.body(bot_guided_mode(phone, incoming_msg, session))

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)

