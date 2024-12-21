"""
This program calculates the area and perimeter of a rectangle.

It demonstrates proper use of:
1. Indentation
2. Comments
3. Variables
4. Functions
5. Naming conventions following PEP 8
"""

# Constants for default dimensions
DEFAULT_LENGTH = 10
DEFAULT_WIDTH = 5


def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width


def calculate_perimeter(length, width):
    """Calculate the perimeter of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The perimeter of the rectangle.
    """
    return 2 * (length + width)


def main():
    """Main function to demonstrate rectangle calculations."""
    # User input for dimensions
    length = float(input("Enter the length of the rectangle: ") or DEFAULT_LENGTH)
    width = float(input("Enter the width of the rectangle: ") or DEFAULT_WIDTH)

    # Calculate area and perimeter
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)

    # Display results
    print(f"\nRectangle Dimensions: Length = {length}, Width = {width}")
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")


if __name__ == "__main__":
    main()
