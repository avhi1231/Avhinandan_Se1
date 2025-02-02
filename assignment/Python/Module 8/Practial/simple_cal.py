def simple_calculator():
    try:
        # Take user inputs
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /): ")

        # Perform the calculation based on the operator
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            # Handle division by zero
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result = num1 / num2
        else:
            # Handle invalid operator
            raise ValueError("Invalid operator. Please use +, -, *, or /.")

        print(f"The result is: {result}")

    except ValueError as ve:
        # Handle invalid input or operator
        print(f"Error: {ve}")
    except ZeroDivisionError as zde:
        # Handle division by zero
        print(f"Error: {zde}")
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the simple calculator.")

# Run the calculator
simple_calculator()
