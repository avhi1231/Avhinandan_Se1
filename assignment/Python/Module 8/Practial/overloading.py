class Calculator:
    # Method overloading using default arguments
    def add(self, a, b=0, c=0):
        return a + b + c

# Create an object of the Calculator class
calc = Calculator()

# Call the add method with different numbers of arguments
print("Method Overloading:")
print(calc.add(5))         # Output: 5 (single argument)
print(calc.add(5, 10))     # Output: 15 (two arguments)
print(calc.add(5, 10, 15)) # Output: 30 (three arguments)
