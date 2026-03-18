import pandas as pd
import matplotlib.pyplot as plt

log_file = "../logs/security_log.txt"

attacks = []

with open(log_file) as f:
    for line in f:
        if "Attack:" in line:
            attack = line.split("Attack:")[1].strip()
            attacks.append(attack)

df = pd.DataFrame(attacks, columns=["Attack"])

counts = df["Attack"].value_counts()

# Plot graph
counts.plot(kind="bar")

plt.title("SentinelShield Attack Detection Dashboard")
plt.xlabel("Attack Type")
plt.ylabel("Number of Attacks")

plt.show()