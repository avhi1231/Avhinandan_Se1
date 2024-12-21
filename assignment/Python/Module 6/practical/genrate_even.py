def generate_even_numbers():
    num = 2  # Start with the first even number
    for _ in range(10):  # Generate 10 even numbers
        yield num
        num += 2  # Move to the next even number

# Using the generator
for even in generate_even_numbers():
    print(even)
