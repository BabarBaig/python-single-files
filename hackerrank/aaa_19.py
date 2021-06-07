def aaa_19(x, y):
    """ Handle zero division """

    try:
        print(x / y)
    except ZeroDivisionError as e:
        print("Error Code:", e)


def main_file():
    with open('aaa_19_data.txt') as fh:
        count = int(fh.readline())
        for line in fh:
            x, y = map(str, line.split())
            aaa_19(x, y)

if __name__ == '__main__':
    main_file()
    main_stdin()
