# Create a list with elements of various data types
multi_type_list = [
    25,                  # Integer
    3.14,                # Float
    "Hello, Python!",    # String
    True,                # Boolean
    None,                # NoneType
    [1, 2, 3],           # Nested List
    (4, 5, 6),           # Tuple
    {"name": "Alice"},   # Dictionary
    {7, 8, 9},           # Set
    bytes([65, 66, 67])  # Bytes
]

# Print the list
print("List with Multiple Data Types:")
print(multi_type_list)

# Accessing and displaying individual elements
print("\nAccessing individual elements:")
for i, element in enumerate(multi_type_list):
    print(f"Element at index {i}: {element} (Type: {type(element)})")
