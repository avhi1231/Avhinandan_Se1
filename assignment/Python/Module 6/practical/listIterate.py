class ListIterator:
    def __init__(self, int_list):
        self.int_list = int_list
        self.index = 0  # Initialize the starting index

    def __iter__(self):
        return self  # The object itself is the iterator

    def __next__(self):
        if self.index < len(self.int_list):
            value = self.int_list[self.index]
            self.index += 1  # Move to the next index
            return value
        else:
            raise StopIteration  # End of iteration

# Using the custom iterator
integers = [10, 20, 30, 40, 50]
custom_iterator = ListIterator(integers)

print("Iterating over the list:")
for number in custom_iterator:
    print(number)