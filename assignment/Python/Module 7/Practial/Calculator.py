def add(a, b):
    """Function to add two numbers."""
    return a + b

def subtract(a, b):
    """Function to subtract one number from another."""
    return a - b

def multiply(a, b):
    """Function to multiply two numbers."""
    return a * b

def divide(a, b):
    """Function to divide one number by another."""
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    """Function to display the calculator menu and perform operations."""
    print("Select Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = int(input("Enter choice (1/2/3/4): "))
        if choice in [1, 2, 3, 4]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == 1:
                print(f"Result: {add(num1, num2)}")
            elif choice == 2:
                print(f"Result: {subtract(num1, num2)}")
            elif choice == 3:
                print(f"Result: {multiply(num1, num2)}")
            elif choice == 4:
                print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid input. Please select a valid operation.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

# Run the calculator
calculator()
