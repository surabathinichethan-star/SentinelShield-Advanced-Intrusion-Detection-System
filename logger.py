from datetime import datetime

LOG_FILE = "logs/security_log.txt"


def log_event(ip, attack_type):

    with open(LOG_FILE, "a") as f:

        f.write(
            f"{datetime.now()} | IP:{ip} | Attack:{attack_type}\n"
        )