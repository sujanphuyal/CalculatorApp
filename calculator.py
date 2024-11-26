# calculator.py
def add(a, b):
    # Resolved conflict by combining changes
    return a + b + 1 - 1  # or whatever resolution you prefer

def subtract(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
