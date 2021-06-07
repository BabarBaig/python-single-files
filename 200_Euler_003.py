<<<<<<< HEAD

import math

def largest_prime_factor_1(num):
    ''' We start by dividing by the smallest prime, and increment from there.
        If the num is divisible by a number, it is not prime, and the quotient
        is then tested as the next prime through recursion
    '''
    ## Check if the value is even, because we will want to iterate by two otherwise
    ## to save iterations
    if num%2 == 0:
        return largest_prime_factor_1(num/2)
    ## Starting from three, iterate by steps of two, and recursively eliminate 
    ## the composites
    x = 3
    # we only have to iterate up to math.sqrt(num) by eulers sieve
    while x < math.floor(math.sqrt(num)):
        if num%x == 0:
            return largest_prime_factor_1(num/x)
        x += 2
    return num

def largest_prime_factor_1(n):
    ''' Problem 003 Largest prime factor
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143? Sol: 6857 '''
    factors = []
    d = 2
    while n > 1:
        while n%d == 0:
            factors.append(d)
            n /= d
        d += 1
        if d*d > n:
            if n > 1:
                factors.append(n)
            break
    return max(factors)

def main():
    print(largest_prime_factor_1(600851475143))

if __name__ == '__main__':
    main()
=======

import math

def largest_prime_factor_1(num):
    ''' We start by dividing by the smallest prime, and increment from there.
        If the num is divisible by a number, it is not prime, and the quotient
        is then tested as the next prime through recursion
    '''
    ## Check if the value is even, because we will want to iterate by two otherwise
    ## to save iterations
    if num%2 == 0:
        return largest_prime_factor_1(num/2)
    ## Starting from three, iterate by steps of two, and recursively eliminate 
    ## the composites
    x = 3
    # we only have to iterate up to math.sqrt(num) by eulers sieve
    while x < math.floor(math.sqrt(num)):
        if num%x == 0:
            return largest_prime_factor_1(num/x)
        x += 2
    return num

def largest_prime_factor_1(n):
    ''' Problem 003 Largest prime factor
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143? Sol: 6857 '''
    factors = []
    d = 2
    while n > 1:
        while n%d == 0:
            factors.append(d)
            n /= d
        d += 1
        if d*d > n:
            if n > 1:
                factors.append(n)
            break
    return max(factors)

def main():
    print(largest_prime_factor_1(600851475143))

if __name__ == '__main__':
    main()
>>>>>>> 3a3eeac04cbe757a5a977da746abe95ab991826d
