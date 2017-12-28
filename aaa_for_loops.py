'''
Created on Dec 27, 2017
@author: Babar Baig
Functions in this file are called by __main__ at the bottom of the file.
'''

def for_01(array1):
    """
    Print sum of numbers in input array1.
    Gracefully handle empty array
    """
    sum = 0
    for num in array1:
        sum += num
    return sum

def for_02(array1):
    """
    Print sum of numbers in input array1.
    Gracefully handle empty array
    """
    sum_sqr = 0
    for i in array1:
        sum_sqr += i * i
    return sum_sqr

def for_03(start, stop_before, jump):
    """
    Run a loop from start to stop_before, and print the square of each value.
    Jump by [jump] to next value.
    Note new style of print() that includes values of variables
    """
    for x in range(start, stop_before, jump):
        print("Square of %d is %d" % (x, x*x))

def prob_01(array1, array2):
    """
    Given 2 #arrays of ints, a and b, return True if they have the same first
    element or they have the same last element. Both arrays will be length 1 or more.
    Flag an exception if one or both the arrays are empty
    """
    assert(len(array1) > 0)
    assert(len(array2) > 0)
    return array1[0]==array2[0] or array1[-1]==array2[-1]

if __name__ == '__main__':
    retval = for_01([])
    print(retval)
    retval = for_01([1, 4, 9, 16, 25, 36, 49, 64, 81])
    print(retval)
    # Note new style of generating an array called list comprehension
    retval = for_02(list(range(0, 10)))
    print(retval)
    retval = for_03(2, 11, 2)
    print(retval)
    # print(prob_01([1, 2, 3], [7, 3]))        # True
    # print(prob_01([1, 2, 3], [7, 3, 4]))     # False
# end
