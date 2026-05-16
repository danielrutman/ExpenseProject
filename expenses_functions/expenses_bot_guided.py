"""CONTAINS ALL THE Functions NEEDED FOR THE GUIDED BOT MODE TO FUNCTION"""

import json
import os
from datetime import datetime
from config import SESSION_FILE

#1 guided bot mode load() session func
def load_sessions():
    """loads sessions from JSON file
    returns empty dict if file doesnt exist"""

    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, mode='r', encoding="utf-8") as file:
            return  json.load(file)

    else:
        return {}

#2 guided bot mode func to saves session dicts to json file
def save_sessions(sessions):
    """saves sessions dict to JSON file"""

    with open(SESSION_FILE, mode='w', encoding="utf-8") as file:
        json.dump(sessions, file)

#3 guided bot mode func to return session for a specific use or return none if no session exists
def get_session(phone):
    """gets session for a specific phone number
    returns None if no session exists"""

    sessions = load_sessions()
    return sessions.get(phone)

#4 guided bot mode func to update or create session for a specific phone number eg: for daniels 05088778895
def update_session(phone, state, data={}):
    """updates or creates session for a specific phone number
    stores state and any additional data like name, category etc"""

    #load session if exists or return empty
    sessions = load_sessions()
    #Update sessions[phone] with state + data + timestamp
    sessions[phone] = {
        "state": state,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        # **data — the double star unpacks the dict into the session ex : data = {"name": "daniel"}: will unpack daniel
        **data
    }

    #save session after update
    save_sessions(sessions)

#5 guided bot func to remove a user session after succsesful save
def clear_session(phone):
    """clears session for a specific phone number
    called after expense is successfully saved"""

    sessions = load_sessions()
    sessions.pop(phone, None)
    save_sessions(sessions)

#6 guided bot func to check if sessions has expired (older than 15m)
def is_session_expired(phone):
    """checks if session is older than 15 minutes
    returns True if expired, False if still valid"""

    session = get_session(phone)
    if not session:
        return True  # no session = treat as expired

    # convert stored timestamp string back to datetime object
    session_time = datetime.strptime(session["timestamp"], "%Y-%m-%d %H:%M:%S")

    # calculate difference between now and session time
    difference = datetime.now() - session_time

    # return True if older than 15 minutes
    return difference.total_seconds() > 900  # 900 seconds = 15 minutes
