
def lcm_even_20(my_list_org):
    ''' Problem 005: Smallest multiple
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10
    without any remainder.  What is the smallest positive number that is evenly
    divisible by all of the numbers from 1 to 20?
    SOL: 232792560 / 232792560
    '''
    my_list = list(my_list_org)
    for i in (2, 3, 5, 7):
        for j in range(20):
            while(my_list[j] % i == 0):
                my_list[j] = int(my_list[j]/i)
    prod = 2 * 3 * 5 * 7
    for i in my_list:
        prod *= i
        print(i)
    print(prod)
    for i in my_list_org:
        result = int(prod / i)
        if result % 2 != 0:      # Odd divisor
            prod *= 2
    print(prod)

def main():
    my_list = list(range(1,21))
    lcm_even_20(my_list)

if __name__ == '__main__':
    main()
