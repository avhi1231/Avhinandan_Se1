# Importing the random module
import random

# Generating a random integer between two numbers (inclusive)
rand_int = random.randint(1, 100)
print(f"Random integer between 1 and 100: {rand_int}")

# Generating a random floating-point number between 0 and 1
rand_float = random.random()
print(f"Random floating-point number between 0 and 1: {rand_float}")

# Generating a random floating-point number between a given range
rand_uniform = random.uniform(10, 20)
print(f"Random floating-point number between 10 and 20: {rand_uniform}")

# Choosing a random element from a list
sample_list = [10, 20, 30, 40, 50]
rand_choice = random.choice(sample_list)
print(f"Random choice from the list {sample_list}: {rand_choice}")

# Shuffling a list randomly
random.shuffle(sample_list)
print(f"List after shuffling: {sample_list}")

# Generating a sample of unique elements from a list
rand_sample = random.sample(sample_list, 3)
print(f"Random sample of 3 elements from the list {sample_list}: {rand_sample}")
