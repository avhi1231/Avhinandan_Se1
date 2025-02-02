def handle_multiple_exceptions():
    try:
        # Take user input
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        # Perform division
        result = num1 / num2
        
        # Access an element in a list
        sample_list = [10, 20, 30]
        index = int(input("Enter the index of the list (0-2): "))
        value = sample_list[index]
        
        print(f"Result of division: {result}")
        print(f"Value from the list: {value}")
    
    # Handle division by zero
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    
    # Handle invalid inputs
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
    
    # Handle index out of range
    except IndexError:
        print("Error: Index out of range. Please enter a valid index.")
    
    # Catch any other unexpected errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        print("Program execution complete.")

# Run the function
handle_multiple_exceptions()


