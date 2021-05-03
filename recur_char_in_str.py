"""
Use recursion to search for a character in a sorted string.
"""

def isIn(char1, alpha_sorted) -> bool:
    """
    char1: a single character
    alpha_sorted: a sorted alphabetic string

    returns: True if char1 is in alpha_sorted; False otherwise
    """

    if alpha_sorted == '':
        return False
    alpha_sorted_len = len(alpha_sorted)
    print( char1, alpha_sorted, str(alpha_sorted_len))

    if alpha_sorted_len == 1:
        return char1 == alpha_sorted
    mid = alpha_sorted_len//2       # Use integer division to get string mid-point

    if char1 == alpha_sorted[mid]:
       return True
    elif char1 < alpha_sorted[mid]:
        return isIn(char1, alpha_sorted[:mid])
    else:
        return isIn(char1, alpha_sorted[mid+1:])

print( isIn('p', 'chijkloprstxz'))
print( isIn('d', 'aaabccddffjklmmtttwz'))
