def collect_vowels(s):
    '''(str) -> str
    >>> collect_vowels('Happy Anniversary!')
    'aAiea'
    >>> collect_vowels('xyz')
    ''
    '''
    vowels='aeiouAEIOU'
    vowels_found=''
    for char in s:
        if char in vowels:
            vowels_found = vowels_found + char
    return vowels_found

def count_vowels(s):
    '''(str) -> int
    Return the number of vowels in s. Don't treat 'y' as a vowel.
    >>> count_vowels('Happy Anniversary!')
    5
    >>> count_vowels('xyz')
    0
    '''
    vowels='aeiou'
    s_lower=s.lower()
    num_vowels=0
    for vowel in vowels:
        num_vowels = num_vowels + s_lower.count(vowel)
    return num_vowels
