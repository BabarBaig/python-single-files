"""
This is code from a tutorial by Kylie Ying, with trivial changes for additional clarity.
https://www.youtube.com/watch?v=8ext9G7xspg
It also references a data file from
https://www.randomlists.com/data/words.json
"""

import random
import string
import gm_hangman_words


def get_valid_word(guessed_so_far) -> str:
    """
    Choose a random word from a word list that doesn't have a space or hyphen in it.
    """

    word = random.choice(guessed_so_far)    
    while ' ' in word or '-' in word:
        word = random.choice(guessed_so_far)
    return word.lower()


def hangman():
    word = get_valid_word(gm_hangman_words.words)
    word_letters = set(word)        # letters in the hangman word
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    lives = 7

    # print(word)
    while len(word_letters) > 0 and lives > 0:
        print(f'\nYou have {lives} lives left')
        print("You've used these letters:\t", ' '.join(sorted(used_letters)))
        guessed_so_far = [letter if letter in used_letters else '_' for letter in word]
        print('Current word:\t', ' '.join(guessed_so_far))

        guessed_letter = input('Guess a letter (or ~ to quit):\t').lower()
        if guessed_letter == '~':
            print('Goodbuy ...')
            return
        if guessed_letter in alphabet - used_letters:
            used_letters.add(guessed_letter)
            if guessed_letter in word_letters:
                word_letters.remove(guessed_letter)
                if len(word_letters) > 0:
                    print('You guessed correctly!')
            else:
                lives -= 1
                if lives > 0:
                    print('Sorry, not a match!')
        elif guessed_letter in used_letters:
            print('You already guessed that letter!  Try again')
        else:
            print('Sorry invalid character!')

    if lives > 0:
        print('Congratulations, you correctly guessed:\t', word)
    else:
        print('Sorry you lose.\nThe word:\t', word)


hangman()
