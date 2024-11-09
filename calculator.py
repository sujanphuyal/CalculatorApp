# calculator.py
# Adding a new function or modifying an existing function in a way that might conflict with other branches
def add(a, b):
    # Feature X change
    return a + b + 1

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
