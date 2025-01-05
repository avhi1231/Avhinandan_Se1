# Define a list with various elements
my_list = [10, "Python", 3.14, True, [1, 2, 3], "Hello"]

# Print the original list
print("Original List:")
print(my_list)

# Access elements using positive indexing
print("\nAccessing elements using positive indexing:")
print(f"Element at index 0: {my_list[0]}")
print(f"Element at index 1: {my_list[1]}")
print(f"Element at index 4: {my_list[4]}")

# Access elements using negative indexing
print("\nAccessing elements using negative indexing:")
print(f"Element at index -1 (last element): {my_list[-1]}")
print(f"Element at index -3: {my_list[-3]}")
print(f"Element at index -5: {my_list[-5]}")

# Nested list access
print("\nAccessing elements of a nested list:")
nested_list_element = my_list[4][1]  # Accessing the second element of the nested list [1, 2, 3]
print(f"Second element of the nested list: {nested_list_element}")
