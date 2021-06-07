def print_word_list():
    word_list = ['hello', 'yes', 'goodbuye', 'last']
    print(word_list[0] + ', ' + word_list[1] + ', ' + word_list[2] + ', ' + word_list[3])
    print(word_list)
    for word in word_list:
        print(word, end=", ")
    print()
    print(', '.join(word_list))

def guess_number():
    GUESS = 45
    MIN = 1
    MAX = 100
    count = 0
    while(True):
        count += 1
        num = input("Please guess the number [1 - 100]:\t")
        try:
            num = int(num)
        except:
            print ('Invalid number, please guess again.')
            continue

        if num < GUESS:
            print('Your guess was low!')
        elif num > GUESS:
            print('Your guess was high!')
        else:       # guessed!
            break

    print(f'You guessed correctly in {count} tries!')

# ******************************************************************

# print_word_list()
# guess_number()

