# Define a list
my_list = [10, 20, 30, 40, 50, 60]

print("Original List:")
print(my_list)

# Using pop() to remove an element by index
removed_element = my_list.pop(2)  # Removes the element at index 2
print(f"\nAfter using pop(2) to remove the element at index 2 ({removed_element}):")
print(my_list)

# Using pop() to remove the last element
last_element = my_list.pop()  # Removes the last element
print(f"\nAfter using pop() to remove the last element ({last_element}):")
print(my_list)

# Using remove() to remove a specific element by value
my_list.remove(20)  # Removes the first occurrence of the value 20
print(f"\nAfter using remove(20) to remove the element with value 20:")
print(my_list)

# Attempting to remove an element not in the list
try:
    my_list.remove(100)  # Tries to remove an element that doesn't exist
except ValueError as e:
    print(f"\nError: {e}")

# Using pop() on an empty list
empty_list = []
try:
    empty_list.pop()
except IndexError as e:
    print(f"\nError: {e}")
