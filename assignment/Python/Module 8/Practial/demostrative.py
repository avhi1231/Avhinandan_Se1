class Parent:
    def show_message(self):
        print("This is the Parent class method.")

class Child(Parent):
    # Overriding the method in the Parent class
    def show_message(self):
        print("This is the Child class method.")

# Create objects of Parent and Child classes
print("\nMethod Overriding:")
parent = Parent()
child = Child()

parent.show_message()  # Output: This is the Parent class method.
child.show_message()   # Output: This is the Child class method.
