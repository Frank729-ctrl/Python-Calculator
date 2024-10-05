# My Calculator

# for addition 
def add(a, b):
    return a + b

# for subtraction
def sub(a, b):
    return a - b

# for division
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is undefined."

# for multiplication
def mul(a, b):
    return a * b

# for modulo 
def mod(a, b):
    return a % b

# MAIN FUNCTION 
def calculator():
    allowed_symbols = ['+', '-', '/', '*', '%']  # Allowed operations
    
    while True:
        try:
            # Input first number
            a = int(input("Input first number: "))

            # Input operator
            op = input("Input operator ('+', '-', '/', '*', '%'): ")
            
            # Check if operator is valid
            if op not in allowed_symbols:
                print("Invalid operation symbol. Please try again.")
                continue

            # Input second number
            b = int(input("Input second number: "))
            
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Decision making based on the operator
        if op == "+":
            print("Sum: ", add(a, b))
        elif op == "-":
            print("Subtraction: ", sub(a, b))
        elif op == "/":
            print("Division: ", div(a, b))
        elif op == "*":
            print("Multiplication: ", mul(a, b))
        elif op == "%":
            print("Modulo: ", mod(a, b))

        # Ask if the user wants to continue
        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != "yes":
            break

# Call the calculator function
calculator()
