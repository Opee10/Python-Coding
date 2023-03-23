# Ask the user for input
user_input = input("Enter a string: ")

# Define a list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# Initialize counters for vowels, consonants, and words
num_vowels = 0
num_consonants = 0
num_words = 1  # We start with 1 word, assuming the input is at least one word
length = len(user_input)

# Loop through each character in the input string
for char in user_input:
    # If the character is a space, add 1 to the word counter
    if char == ' ':
        num_words += 1
    # If the character is a vowel, add 1 to the vowel counter
    elif char.lower() in vowels:
        num_vowels += 1
    # If the character is a consonant, add 1 to the consonant counter
    elif char.isalpha():
        num_consonants += 1

# Print the results
print(f"Number of vowels: {num_vowels}")
print(f"Number of consonants: {num_consonants}")
print(f"Number of words: {num_words}")
print(f"Length of string: {length}")
