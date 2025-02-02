class Animal:
    def speak(self, sound=None):
        if sound:
            print(f"The animal says: {sound}")
        else:
            print("The animal makes a sound.")

class Dog(Animal):
    # Overriding the speak method
    def speak(self, sound="Bark"):
        print(f"The dog says: {sound}")

# Create objects of Animal and Dog classes
print("\nCombining Overloading and Overriding:")
animal = Animal()
dog = Dog()

# Method overloading in Animal class
animal.speak()             # Output: The animal makes a sound.
animal.speak("Roar")       # Output: The animal says: Roar.

# Method overriding in Dog class
dog.speak()                # Output: The dog says: Bark.
dog.speak("Woof")          # Output: The dog says: Woof.
