class Person:
    # Constructor to initialize the properties
    def __init__(self, name, age):
        self.name = name  # Instance variable for name
        self.age = age    # Instance variable for age

    # Method to display the details
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create an object of the class
person1 = Person("Alice", 25)

# Access properties using the object
print(f"Accessing properties directly: Name = {person1.name}, Age = {person1.age}")

# Call the method to display details
person1.display_info()
