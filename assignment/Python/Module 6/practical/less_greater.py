# Python program to find if a number is greater or less than a target number

# Input the target number and the number to compare
target = int(input("Enter the target number: "))
number = int(input("Enter the number to compare: "))

# Compare the numbers using if-else
if number > target:
    print(f"The number {number} is greater than {target}.")
elif number < target:
    print(f"The number {number} is less than {target}.")
else:
    print(f"The number {number} is equal to {target}.")
