<<<<<<< HEAD
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Baig-Admin
#
# Created:     07/10/2013
# Copyright:   (c) Baig-Admin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# ==============================================
def count(sequence, item):
    # Return how many times item occurs in sequence
    count = 0
    for my_item in sequence:
        if my_item == item:
            count += 1
    return count

def test_count():
    my_list = [1,2,1,1]
    print(count(my_list, 1))
# ==============================================
# Key/Value dictionary of letters and their Scrabble scores/values
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score1(string):
    # Uses while(), which is much more verbose
    str_len = len(string)
    index = 0
    word_score = 0
    while (index < str_len):
        my_char_key = string[index].lower()
        word_score += score[my_char_key]
        index += 1
    return word_score

def scrabble_score2(string):
    word_score = 0
    for my_char_key in string:
        word_score += score[my_char_key.lower()]
    return word_score

def test_scrabble_score():
    print(scrabble_score1('Helix'))
    print(scrabble_score2('Helix'))

# ==============================================
def censor1(text, censor_word):
    asterisks = '*' * len(censor_word)
    my_array = text.split(' ')  # Split text into words using space delimiters
    censored_array = []
    for next_word in my_array:
        if next_word ==  censor_word:
            censored_array.append(asterisks)
        else:
            censored_array.append(next_word)
    return ' '.join(censored_array)

def censor2(text, censor_word):
    asterisks = '*' * len(censor_word)
    return text.replace(censor_word, asterisks)

def test_censor():
    original_text = 'This is text abcdef that is abcdef censored'
    censor_text = 'abcdef'
    print(original_text)
    print(censor1(original_text, censor_text))
    print(censor2(original_text, censor_text))

# ==============================================
def anti_vowel1(string):
    # Uses while(), which is much more verbose
    str_len = len(string)
    index = 0
    vowels = 'aeiouAEIOU'
    anti_vowel_str = ''
    while (index < str_len):
        my_char = string[index]
        if my_char not in vowels:
            anti_vowel_str += my_char
        index += 1
    return anti_vowel_str

def anti_vowel2(string):
    vowels = 'aeiouAEIOU'
    anti_vowel_str = ''
    for my_char in string:
        if my_char not in vowels:
            anti_vowel_str += my_char
    return anti_vowel_str

def test_anti_vowel():
  print(anti_vowel1('A quIck BrOwn Fox jUmped ovEr the lazy dog 12 & 345'))
  print(anti_vowel2('A quIck BrOwn Fox jUmped ovEr the lazy dog 12 & 345'))

# ==============================================
def main():
    test_count()
#   test_scrabble_score()
#   test_censor()
#   test_anti_vowel()

if __name__ == '__main__':
  main()
=======
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Baig-Admin
#
# Created:     07/10/2013
# Copyright:   (c) Baig-Admin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# ==============================================
def count(sequence, item):
    # Return how many times item occurs in sequence
    count = 0
    for my_item in sequence:
        if my_item == item:
            count += 1
    return count

def test_count():
    my_list = [1,2,1,1]
    print(count(my_list, 1))
# ==============================================
# Key/Value dictionary of letters and their Scrabble scores/values
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score1(string):
    # Uses while(), which is much more verbose
    str_len = len(string)
    index = 0
    word_score = 0
    while (index < str_len):
        my_char_key = string[index].lower()
        word_score += score[my_char_key]
        index += 1
    return word_score

def scrabble_score2(string):
    word_score = 0
    for my_char_key in string:
        word_score += score[my_char_key.lower()]
    return word_score

def test_scrabble_score():
    print(scrabble_score1('Helix'))
    print(scrabble_score2('Helix'))

# ==============================================
def censor1(text, censor_word):
    asterisks = '*' * len(censor_word)
    my_array = text.split(' ')  # Split text into words using space delimiters
    censored_array = []
    for next_word in my_array:
        if next_word ==  censor_word:
            censored_array.append(asterisks)
        else:
            censored_array.append(next_word)
    return ' '.join(censored_array)

def censor2(text, censor_word):
    asterisks = '*' * len(censor_word)
    return text.replace(censor_word, asterisks)

def test_censor():
    original_text = 'This is text abcdef that is abcdef censored'
    censor_text = 'abcdef'
    print(original_text)
    print(censor1(original_text, censor_text))
    print(censor2(original_text, censor_text))

# ==============================================
def anti_vowel1(string):
    # Uses while(), which is much more verbose
    str_len = len(string)
    index = 0
    vowels = 'aeiouAEIOU'
    anti_vowel_str = ''
    while (index < str_len):
        my_char = string[index]
        if my_char not in vowels:
            anti_vowel_str += my_char
        index += 1
    return anti_vowel_str

def anti_vowel2(string):
    vowels = 'aeiouAEIOU'
    anti_vowel_str = ''
    for my_char in string:
        if my_char not in vowels:
            anti_vowel_str += my_char
    return anti_vowel_str

def test_anti_vowel():
  print(anti_vowel1('A quIck BrOwn Fox jUmped ovEr the lazy dog 12 & 345'))
  print(anti_vowel2('A quIck BrOwn Fox jUmped ovEr the lazy dog 12 & 345'))

# ==============================================
def main():
    test_count()
#   test_scrabble_score()
#   test_censor()
#   test_anti_vowel()

if __name__ == '__main__':
  main()
>>>>>>> 3a3eeac04cbe757a5a977da746abe95ab991826d
