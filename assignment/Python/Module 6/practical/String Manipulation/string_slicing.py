# Define a string
my_string = "Hello, World!"

# Slice from index 0 to 4 (up to but not including index 5)
substring1 = my_string[0:5]
print("Slicing from index 0 to 4:", substring1)  # Output: Hello

# Slice from index 7 to the end
substring2 = my_string[7:]
print("Slicing from index 7 to end:", substring2)  # Output: World!

# Slice from the beginning to index 5 (up to but not including index 5)
substring3 = my_string[:5]
print("Slicing from the beginning to index 4:", substring3)  # Output: Hello

# Slice the string in reverse (from end to start)
substring4 = my_string[::-1]
print("Reversed string:", substring4)  # Output: !dlroW ,olleH

# Slice with a step (every second character)
substring5 = my_string[::2]
print("Slicing with a step of 2:", substring5)  # Output: Hoo ol

# Slice from index 3 to 8 (up to but not including index 8)
substring6 = my_string[3:8]
print("Slicing from index 3 to 7:", substring6)  # Output: lo, W
