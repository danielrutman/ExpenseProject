"""this file contains Bot load test with locust framework for EXPENSES BOT."""

# How to run:
# Terminal 1: source venv/bin/activate python3 expenses_bot.py
# Terminal 2: locust -f locustfile.py --host=http://localhost:5000


from locust import HttpUser, task, between
from expenses_functions.expenses_bot_guided import clear_session

class ExpenseBotUser(HttpUser): # HttpUser  Locust base class gives our simulated user the ability to make HTTP requests
    """simulates a real WhatsApp user sending expenses via the bot"""
    # wait 1-3 seconds between each action — mimics real user typing speed
    wait_time = between(1, 3)

    def on_start(self):
        """runs once when user spawns — sets up fresh session"""
        # clear any leftover session for this phone
        clear_session(self.phone)

        # send first message to trigger welcome
        self.client.post("/bot", data={
            "From": self.phone,
            "Body": "hello"
        })
        # choose quick mode
        self.client.post("/bot", data={
            "From": self.phone,
            "Body": "1"
        })

    @property
    def phone(self):
        """generates unique phone number per simulated user using object id"""
        return f"+972500{id(self) % 10000000}" # modulo operator, keeps the number to max 7 digits in israeli phone format

    # load test settings (set in Locust dashboard):
    # normal: 2 users, spawn rate 1
    # max:    3 users, spawn rate 1
    # stress: 6 users, spawn rate 2
    @task
    def send_valid_expense(self):
        """most common action — user sends a valid expense via quick_mode()"""
        self.client.post("/bot", data={
            "From": self.phone,
            "Body": "daniel 50 רכב gas"
        })
