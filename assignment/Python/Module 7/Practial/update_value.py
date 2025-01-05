# Sample dictionary
student = {
    "name": "Alice",
    "age": 25,
    "major": "Computer Science"
}

# Print the original dictionary
print("Original dictionary:", student)

# Update the value associated with the key 'age'
student["age"] = 26

# Print the updated dictionary
print("Updated dictionary:", student)
# Using the update() method
student.update({"age": 27})

# Print the updated dictionary
print("Updated dictionary:", student)
