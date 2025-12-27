def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,       
    "-": subtract,
    "/": divide,
    "*": multiply
}

def calculator():
    num1 = float(input("Enter the first number: "))
    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)
        
        operation_choice = input("Choose an operation: ")
        
        if operation_choice not in operations:
            print("Invalid operation. Please try again.")
            continue
        
        num2 = float(input("Enter the second number: "))
        
        calculation_function = operations[operation_choice]
        
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_choice} {num2} = {answer}")
        
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        
        if choice == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()