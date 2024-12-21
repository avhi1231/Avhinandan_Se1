# Input the percentage from the user
percentage = float(input("Enter your percentage: "))

# Determine the grade using if-else ladder
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 50:
    grade = "E"
else:
    grade = "F"

# Display the result
print(f"Your percentage is {percentage}%.")
print(f"Your grade is: {grade}")
