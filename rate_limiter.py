import time

request_log = {}

MAX_REQUESTS = 10
TIME_WINDOW = 60


def check_rate_limit(ip):

    current_time = time.time()

    if ip not in request_log:
        request_log[ip] = []

    request_log[ip].append(current_time)

    request_log[ip] = [
        t for t in request_log[ip]
        if current_time - t < TIME_WINDOW
    ]

    if len(request_log[ip]) > MAX_REQUESTS:
        return True

    return False