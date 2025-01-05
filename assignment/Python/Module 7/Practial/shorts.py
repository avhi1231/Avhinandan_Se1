# Define a list of numbers
numbers = [5, 2, 9, 1, 5, 6]

# Sort the list using sort() (in-place sorting)
numbers.sort()
print("Sorted list using sort():", numbers)

# Reset the list to its original order
numbers = [5, 2, 9, 1, 5, 6]

# Sort the list using sorted() (returns a new sorted list)
sorted_numbers = sorted(numbers)
print("Sorted list using sorted():", sorted_numbers)

# Demonstrate reverse sorting with sorted()
reverse_sorted_numbers = sorted(numbers, reverse=True)
print("Reverse sorted list using sorted():", reverse_sorted_numbers)

# Demonstrate reverse sorting with sort()
numbers.sort(reverse=True)
print("Reverse sorted list using sort():", numbers)