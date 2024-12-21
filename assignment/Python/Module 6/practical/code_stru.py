# Import statements
import math
from datetime import datetime

# Constants and global variables
PI = 3.14159
DEFAULT_USERNAME = "Guest"

# Function definitions
def calculate_circle_area(radius):
    """Calculate the area of a circle."""
    return PI * (radius**2)

def get_current_time():
    """Get the current system time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Class definitions
class User:
    """Represents a user in the system."""

    def __init__(self, username):
        self.username = username

    def greet(self):
        """Greet the user."""
        return f"Hello, {self.username}!"

# Main program logic
def main():
    """Main program entry point."""
    print(f"Current time: {get_current_time()}")
    
    user = User(DEFAULT_USERNAME)
    print(user.greet())

    radius = 5
    area = calculate_circle_area(radius)
    print(f"The area of a circle with radius {radius} is {area:.2f}")

# Run the program
if __name__ == "__main__":
    main()
