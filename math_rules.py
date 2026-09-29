# math_rules.py
def calculate_ratio(part, total):
    if total == 0:
        return 0.0
    return (part / total) * 100.0

def safe_divide(a, b):
    if b == 0:
        return 0.0
    return a / b
