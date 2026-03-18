from rules import attack_patterns

def detect_attack(request_data):

    for attack_type, patterns in attack_patterns.items():

        for pattern in patterns:

            if pattern.lower() in request_data.lower():
                return attack_type

    return None