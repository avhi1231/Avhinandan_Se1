# Define the list of strings
List1 = ['apple', 'banana', 'mango']

# Define the string to search for
search_string = 'banana'

# Use a for loop to iterate through the list and check if the string is in the list
for fruit in List1:
    if fruit == search_string:
        print(f"Found '{search_string}' in the list.")
        break
else:
    print(f"'{search_string}' is not in the list.")
