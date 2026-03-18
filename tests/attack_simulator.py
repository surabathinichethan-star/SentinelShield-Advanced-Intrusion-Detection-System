import requests
import time

url = "http://127.0.0.1:5000/test"

payloads = [
    "?user=test",
    "?user=admin' OR '1'='1",
    "?q=<script>alert(1)</script>",
    "?file=../../etc/passwd",
    "?cmd=; ls",
]

for i in range(50):

    payload = payloads[i % len(payloads)]

    try:
        response = requests.get(url + payload)
        print(f"{i+1}: {response.text}")
    except:
        print("Request failed")

    time.sleep(0.2)