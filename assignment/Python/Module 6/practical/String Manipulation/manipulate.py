# Define a string
my_string = "  Hello, Python World!  "

# 1. Using strip() to remove leading and trailing spaces
stripped_string = my_string.strip()
print("Stripped string:", stripped_string)  # Output: "Hello, Python World!"

# 2. Using lower() to convert the string to lowercase
lower_case_string = my_string.lower()
print("Lowercase string:", lower_case_string)  # Output: "  hello, python world!  "

# 3. Using upper() to convert the string to uppercase
upper_case_string = my_string.upper()
print("Uppercase string:", upper_case_string)  # Output: "  HELLO, PYTHON WORLD!  "

# 4. Using replace() to replace part of the string
replaced_string = my_string.replace("Python", "Java")
print("Replaced string:", replaced_string)  # Output: "  Hello, Java World!  "

# 5. Using split() to split the string into a list
split_string = my_string.split(",")
print("Split string:", split_string)  # Output: ['  Hello', ' Python World!  ']

# 6. Using find() to find the index of a substring
index = my_string.find("Python")
print("Index of 'Python':", index)  # Output: 8

# 7. Using join() to join elements of a list into a string
words = ['Hello', 'Python', 'World']
joined_string = " ".join(words)
print("Joined string:", joined_string)  # Output: "Hello Python World"

# 8. Using count() to count occurrences of a substring
count = my_string.count("o")
print("Count of 'o':", count)  # Output: 2

# 9. Using isdigit() to check if a string contains only digits
numeric_string = "12345"
print("Is the numeric string a digit?", numeric_string.isdigit())  # Output: True

# 10. Using isalpha() to check if a string contains only alphabetic characters
alpha_string = "Hello"
print("Is the string alphabetic?", alpha_string.isalpha())  # Output: True

# 11. Using startswith() to check if a string starts with a specific substring
starts_with_hello = my_string.startswith("  Hello")
print("Does the string start with '  Hello'?", starts_with_hello)  # Output: True

# 12. Using endswith() to check if a string ends with a specific substring
ends_with_world = my_string.endswith("World!  ")
print("Does the string end with 'World!  '?", ends_with_world)  # Output: True