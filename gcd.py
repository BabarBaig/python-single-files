
def gcdRecur(a, b):
    '''
    a, b: positive integers
    Algorithm: A clever mathematical trick (due to Euclid):
    Suppose that a and b are two positive integers:
        If b = 0, then the answer is a
        Otherwise, gcd(a, b) is the same as gcd(b, a % b)
   return: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    return gcdRecur(b, a % b)

def gcdIter(a, b):
    '''
    a, b: positive integers
    Algorithm:  Begin with a test value equal to the smaller of the two input arguments,
    and iteratively reduce this test value by 1 until you either reach a case where the
    test divides both a and b without remainder, or you reach 1
    return: a positive integer, the greatest common divisor of a & b.
    '''
    x = min(a, b)
    while x > 1:
        if (a % x == 0 and b % x == 0):
            return x
        x -= 1
    return x
