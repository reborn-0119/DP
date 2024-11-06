import random

def load_words(filename):
    with open(filename, 'r') as file:
        # Split each line into words and flatten them into a single list
        words = [word for line in file for word in line.strip().split()]
    return words

def generate_password(words, num_words=8):
    # Select exactly 8 random words from the list
    selected_words = random.sample(words, num_words)
    return ' '.join(selected_words)  # Use spaces or another separator

# Load words from the dictionary file
dictionary_file = 'dictionary.txt'
words = load_words(dictionary_file)

# Generate an 8-word random password
password = generate_password(words)
print("Generated password:", password)
