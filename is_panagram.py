def is_pangram(str):
""" Optimized function.  Checks if (potentially very long) input string 
    has all the letters of the alphabet.  Exits immediately if all 26
    letters are found, without checking the rest of the string
"""
    letters_seen = set()    # Create a set of letters seen so far
    for chr in str:
        chr = chr.lower()
        if 'a' <= chr <= 'z':
            letters_seen.add(chr)
            if len(letters_seen) == 26:    # Input str is a panagram
                return True                # Stop immediately when all letters found
    return False
