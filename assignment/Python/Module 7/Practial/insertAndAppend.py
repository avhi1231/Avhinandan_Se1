# Define an initial list
my_list = [10, 20, 30, 40]

print("Original List:")
print(my_list)

# Using append() to add an element at the end
my_list.append(50)
print("\nAfter using append() to add 50:")
print(my_list)

# Using insert() to add an element at a specific position
my_list.insert(2, 25)  # Inserts 25 at index 2
print("\nAfter using insert() to add 25 at index 2:")
print(my_list)

# Adding another element using append()
my_list.append(60)
print("\nAfter using append() to add 60:")
print(my_list)

# Using insert() to add an element at the beginning
my_list.insert(0, 5)  # Inserts 5 at index 0
print("\nAfter using insert() to add 5 at the beginning:")
print(my_list)
