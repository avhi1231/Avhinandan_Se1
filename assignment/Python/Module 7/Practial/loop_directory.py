# Two lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

# Initialize an empty dictionary
merged_dict = {}

# Loop through the lists and merge them into the dictionary
for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]

# Print the merged dictionary
print("Merged Dictionary:", merged_dict)
