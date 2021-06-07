def digit_sum(number):
    sum = 0
    new_number = number
    while new_number > 0:
        right_most_digit = new_number % 10
        sum += right_most_digit
        new_number = new_number // 10
    return sum


def main():
    print(digit_sum(100))
    print(digit_sum(1234))
    print(digit_sum(4004))
    print(digit_sum(4321))
    print(digit_sum(99999))


if __name__ == '__main__':
    main()
