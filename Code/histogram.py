import random
import re

def read_text(file_name):
    """Read text from a file and return it as a string."""
    with open(file_name, 'r') as file:
        return file.read()

def tokenize_text(text):
    """Tokenize the text into words, dismissing capitalization and punctuation."""
    # Use regular expression to find words and dismiss capitalization and punctuation
    words = re.findall(r'\b\w+\b', text.lower())
    return words

def count_word_frequency(words):
    """Count the frequency of each word in the list of words."""
    word_freq = {}
    for word in words:
        # Increment the count for each word
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

def display_histogram(word_freq):
    """Display the word and its frequency in the terminal."""
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

# Read text from a file
file_name = 'data/word.txt'
text = read_text(file_name)

# Tokenize the text into words, dismissing capitalization and punctuation
words = tokenize_text(text)

# Shuffle the words to randomize the order
random.shuffle(words)

# Count the frequency of each word
word_freq = count_word_frequency(words)

# Display the word and its frequency in the terminal
display_histogram(word_freq)














