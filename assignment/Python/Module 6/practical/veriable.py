"""
This program demonstrates the creation of variables and the use of 
different data types in Python, including strings, integers, floats, 
lists, tuples, sets, dictionaries, and booleans.
"""

# Integer
age = 25
print(f"Integer: Age = {age}, Type = {type(age)}")

# Float
height = 5.9  # Height in feet
print(f"Float: Height = {height}, Type = {type(height)}")

# String
name = "John Doe"
print(f"String: Name = '{name}', Type = {type(name)}")

# Boolean
is_student = True
print(f"Boolean: Is Student = {is_student}, Type = {type(is_student)}")

# List
hobbies = ["Reading", "Traveling", "Cycling"]
print(f"List: Hobbies = {hobbies}, Type = {type(hobbies)}")

# Tuple
coordinates = (12.34, 56.78)
print(f"Tuple: Coordinates = {coordinates}, Type = {type(coordinates)}")

# Set
unique_numbers = {1, 2, 3, 4, 5}
print(f"Set: Unique Numbers = {unique_numbers}, Type = {type(unique_numbers)}")

# Dictionary
person_info = {"name": "John", "age": 25, "is_student": True}
print(f"Dictionary: Person Info = {person_info}, Type = {type(person_info)}")

# NoneType
unknown = None
print(f"NoneType: Unknown = {unknown}, Type = {type(unknown)}")

# Complex Number
complex_num = 3 + 4j
print(f"Complex: Complex Number = {complex_num}, Type = {type(complex_num)}")

# Byte
byte_data = b"Hello"
print(f"Byte: Byte Data = {byte_data}, Type = {type(byte_data)}")
