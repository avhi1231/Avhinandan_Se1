# Define the list
List1 = ['apple', 'banana', 'mango']

# Iterate through the list
for fruit in List1:
    if fruit == 'banana':
        print(f"Found {fruit}, stopping the loop.")
        break  # Exit the loop when 'banana' is found
    print(fruit)
