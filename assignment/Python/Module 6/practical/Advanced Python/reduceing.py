from functools import reduce

# Define the list of numbers
numbers = [1, 2, 3, 4, 5]

# Define the function to multiply two numbers
def multiply(x, y):
    return x * y

# Use reduce() to find the product of all numbers in the list
product = reduce(multiply, numbers)

# Print the product
print("Product of the list:", product)
