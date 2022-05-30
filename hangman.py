import random
import os


word_list = ['art', 'ball', 'ice', 'car']

# Randomly choose a word
word = random.choice(word_list)

# User guess set
guess_set = set()

# Print hidden word
def hidden_word(word, guess_set):
    hidden_word = ''
    for x in word:
        if x in guess_set:
            hidden_word += x
            hidden_word += ' '
        else:
            hidden_word += '_ '
    return hidden_word

# Ask the user to guess a letter
def get_a_guess():
    global guess_set
    guess = input ('\nGuess a letter: ').lower()
    if guess in guess_set:
        # print('...you\'ve already guessed that earlier')
        pass
    else:
        guess_set.add(guess)
    return guess

# Check the user guess
def check_a_guess(guess, word):
    global attempts
    global guess_set
    if word.count(guess) == 0:
        attempts -= 1
    if attempts == 0:
        os.system('CLS')
        print(f'The word was [{word}]')
        print(f'Your best result was [{hidden_word(word, guess_set)}]')
        print(f'But you\'ve tried letters as follows: {guess_set}')
        print('\n...let\'s try again?\n\n')

# User has 5 attempts to guess the word
attempts = 5

while attempts > 0:
    # Clear terminal
    os.system('CLS')
    h_word = hidden_word(word, guess_set)
    print(h_word)
    if h_word.count('_ ') != 0:
        print(f'\n*you have {attempts} attempts to guess')
        guess = get_a_guess()
        check_a_guess(guess, word)
    else:
        print('\nCongratulations!!! You win!!!\n\n')
        break
