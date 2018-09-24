
def is_palindrome(num):
    num_str = str(num)
    num_str_rev = num_str[::-1]
    return num_str==num_str_rev

def largest_palindrome():
    ''' Problem 004: Largest palindrome product
    A palindromic number reads the same both ways. The largest palindrome made from
    the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    Sol: 913 * 993 = 906609'''
    largest_palindrome = 0
    for i in range(100,999):
        for j in range (100, 999):
            prod = i*j
            # Following 2 lines are logically equivalent, but the un-commented line
            # takes 0.2s vs 0.6s for the commented-out line! Why? Because it saves a
            # large number of function calls and expensive string operations.
            # if is_palindrome(prod) and prod>largest_palindrome:
            if prod>largest_palindrome and is_palindrome(prod): 
                largest_palindrome = prod
    return largest_palindrome

def main():
    print(largest_palindrome())

if __name__ == '__main__':
    main()
