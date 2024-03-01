# Text Analysis Tool

def text_analysis(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    word_count = len(text.split())
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    paragraph_count = text.count('\n\n') + 1
    words = text.split()
    average_word_length = sum(len(word) for word in words) / len(words)
    word_freq = {}
    for word in words:
        word = word.strip(",.!?").lower()
        if word.isalpha():
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    most_common_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]
    print("Word count:", word_count)
    print("Sentence count:", sentence_count)
    print("Paragraph count:", paragraph_count)
    print("Average word length:", average_word_length)
    print("Most common words and their frequencies:")
    for word, freq in most_common_words:
        print(f"{word}: {freq}")

file_path = "The_Little_Prince.txt"  
text_analysis(file_path)


# Hangman Game

import random
def choose_word():
    words = ["apple", "banana", "orange", "grape", "pineapple", "watermelon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_attempts = 6
    word = choose_word()
    guessed_letters = []
    attempts = 0
    print("Hangman")
    print("Guess the word")
    while True:
        print(display_word(word, guessed_letters))
        guess = input("\nGuess a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        guessed_letters.append(guess)
        if guess not in word:
            attempts += 1
            print("Incorrect guess.")
            print(f"You have {max_attempts - attempts} attempts left.")
            if attempts >= max_attempts:
                print("Sorry, you lost! The word was:", word)
                break
        else:
            print("Correct guess!")
            if all(letter in guessed_letters for letter in word):
                print("Congratulations, you won!")
                break
hangman()


# Number guessing game

import random

def number_guessing_game():
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1
        if guess < target_number:
            print("Too low, Try again.")
        elif guess > target_number:
            print("Too high, Try again.")
        else:
            print(f"You guessed the number {target_number} correctly in {attempts} attempts!")
            break

number_guessing_game()


