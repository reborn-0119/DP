import random

def load_words(filename):
    with open(filename, 'r') as file:
        
        words = [word for line in file for word in line.strip().split()]
    return words

def generate_password(words, num_words=8):
    
    selected_words = random.sample(words, num_words)
    return ' '.join(selected_words)  

dictionary_file = 'prog5.txt'
words = load_words(dictionary_file)

password = generate_password(words)
print("Generated password:", password)
