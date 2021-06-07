import random
import string
from . import word_list


def get_valid_word_upper():
    word = random.choice(word_list.words)
    while '-' in word or ' ' in word:
        word = random.choice(word_list.words)
    return word.upper()


def play_hangman():
    word_upper = get_valid_word_upper()
    print(f'mystery word: {word_upper}')
    word_letters = set(word_upper)  # Create a set of unique letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()            # Corret/incorrect guesses so far

    while len(word_letters) > 0:
        print('You have used these letters: ', ' '.join(used_letters))
        display_word = [x if x in used_letters else '_' for x in word_upper]
        print('CUrrent word: ', ' '.join(display_word))

        user_letter_upper = input("Type a letter:  ").upper()[0]
        # Note set difference:
        if user_letter_upper in alphabet - used_letters:
            used_letters.add(user_letter_upper)		# Used-up another letter
            if user_letter_upper in word_letters:
                word_letters.remove(user_letter_upper)

        elif user_letter_upper in used_letters:
            print(f'[{user_letter_upper}] already used.  Guess another letter:  ')

        else:
            print(f'[{user_letter_upper}] is invalid character.  Guess another letter:  ')

    # No more letters left to guess!


if __name__ == "__main__":
    play_hangman()
