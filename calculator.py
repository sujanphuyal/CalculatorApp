# calculator.py
def add(a, b):
    # Resolved conflict manually by balancing operation 
    return (a + b) * 2 / 2
    
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
