# Program to read the contents of a file and print them on the console

# Specify the file name
file_name = "example.txt"

try:
    # Open the file in read mode
    with open(file_name, "r") as file:
        # Read the content of the file
        content = file.read()
        # Print the content on the console
        print("File Content:")
        print(content)
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
