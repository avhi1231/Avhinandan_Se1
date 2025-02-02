import re

def match_word(text, word):
    """Match a word at the beginning of a string using re.match."""
    pattern = rf'^{word}\b'  # Ensures the word is matched at the start
    match = re.match(pattern, text, re.IGNORECASE)  # Case-insensitive match
    
    if match:
        print(f'Word "{word}" matched at the beginning of the text!')
    else:
        print(f'Word "{word}" not found at the beginning of the text.')

# Example usage
text = "Python is a powerful programming language."
word = "Python"
match_word(text, word)