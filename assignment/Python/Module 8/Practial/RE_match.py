import re

def search_word(text, word):
    """Search for a word in a string using re.search."""
    pattern = rf'\b{word}\b'  # Ensures the word is matched as a whole
    match = re.search(pattern, text, re.IGNORECASE)  # Case-insensitive search
    
    if match:
        print(f'Word "{word}" found in the text!')
    else:
        print(f'Word "{word}" not found in the text.')

# Example usage
text = "Python is a powerful programming language."
word = "powerful"
search_word(text, word)
