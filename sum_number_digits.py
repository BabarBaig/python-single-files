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

def digit_sum(number: int) -> int:
    """
    Return the sum of the digits in input int: number
    """
    assert type(number) is int, "Input must be an int, got: " + str(number)

    sum = 0
    new_number = number
    while new_number > 0:
        right_most_digit = new_number % 10
        sum += right_most_digit
        new_number = new_number // 10       # Integer division
    return sum


def main():
    for val in (100, 1234, 4004, 4321, 99999):
        print(f'Sum of digits of {val}\tis {digit_sum(val)}')
    # Cause an error condition
    val = 1.5
    print(f'Sum of digits of {val}\tis {digit_sum(val)}')

if __name__ == '__main__':
    main()
