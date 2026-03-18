import pandas as pd

log_file = "../logs/security_log.txt"

attacks = []

with open(log_file) as f:
    for line in f:
        if "Attack:" in line:
            attack = line.split("Attack:")[1].strip()
            attacks.append(attack)

df = pd.DataFrame(attacks, columns=["Attack"])

print("\nAttack Summary:\n")
print(df["Attack"].value_counts())