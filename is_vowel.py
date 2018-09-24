
def isVowel( c):
    ''' Return True if input character c is a vowel '''
    return c.lower() in 'aeiou'

if __name__ == '__main__':
    print('c is a vowel?  {0}' .format(isVowel('c')))
    print(f"I is a vowel?  {isVowel('I')}")
