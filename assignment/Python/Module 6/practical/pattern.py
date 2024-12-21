# Define the number of rows for the right angle triangle
rows = 5

# Use a nested for loop to print the right angle triangle pattern
for i in range(1, rows + 1):
    for j in range(i):
        print('*', end=' ')
    print()  # Move to the next line after each row
