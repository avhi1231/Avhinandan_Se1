# Input the number to check
number = int(input("Enter a number: "))

# Check if the number is greater than 1
if number > 1:
    # Check for factors from 2 to sqrt(number)
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print(f"The number {number} is not a prime number.")
            print(f"It is divisible by {i}.")
            break
    else:
        # If no factors found, it is a prime number
        print(f"The number {number} is a prime number.")
else:
    # Numbers less than or equal to 1 are not prime
    print(f"The number {number} is not a prime number.")
