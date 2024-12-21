# Define the list of numbers
numbers = [1, 2, 3, 4, 5]

# Define the function to square a number
def square(number):
    return number ** 2

# Apply the map() function to square each number in the list
squared_numbers = list(map(square, numbers))

# Print the squared numbers
print(squared_numbers)
