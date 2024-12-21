# Define the list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Define the function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Use filter() to filter out even numbers
even_numbers = list(filter(is_even, numbers))

# Print the list of even numbers
print("Even numbers:", even_numbers)
