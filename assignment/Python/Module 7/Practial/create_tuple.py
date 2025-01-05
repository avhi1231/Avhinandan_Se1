# Creating a tuple with multiple data types
mixed_tuple = (42, "Hello", 3.14, True, [1, 2, 3], {"key": "value"})

# Display the tuple
print("Tuple with multiple data types:", mixed_tuple)

# Accessing and printing each element with its type
for element in mixed_tuple:
    print(f"Element: {element}, Type: {type(element)}")
