# Creating a tuple with multiple data types
mixed_tuple = (25, "Python", 3.14, True, [1, 2, 3], {"key": "value"})

# Display the tuple
print("Tuple with multiple data types:", mixed_tuple)

# Accessing each element and printing its type
for element in mixed_tuple:
    print(f"Element: {element}, Type: {type(element)}")