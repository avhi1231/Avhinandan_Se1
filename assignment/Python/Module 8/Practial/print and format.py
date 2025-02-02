# Define variables
name = "John"
age = 25
salary = 50000.75
experience = 3

# Using print() and f-strings to format the output
print(f"Employee Details:")
print(f"Name       : {name}")
print(f"Age        : {age} years")
print(f"Salary     : ${salary:,.2f} per year")  # Formats salary with commas and 2 decimal places
print(f"Experience : {experience} years")

# Perform calculations and include them in the formatted string
monthly_salary = salary / 12
print(f"Monthly Salary: {monthly_salary:,.2f}")