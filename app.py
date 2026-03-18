from flask import Flask, request

from detector import detect_attack
from logger import log_event
from rate_limiter import check_rate_limit

app = Flask(__name__)


@app.route("/")
def home():
    return "SentinelShield Web Protection Active"


@app.route("/test")
def test():

    ip = request.remote_addr

    if check_rate_limit(ip):
        return "IP blocked due to excessive requests"

    request_data = str(request.args)

    attack = detect_attack(request_data)

    if attack:
        log_event(ip, attack)
        return f"Attack detected: {attack}"

    return "Request allowed"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)