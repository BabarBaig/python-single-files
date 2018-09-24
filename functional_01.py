<<<<<<< HEAD

def calc(func, x, y):
    return func(x, y)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def main():
    print (calc(add, 10, 15))
    print (calc(lambda x, y: x + y, 10, 15))
    print (calc(sub, 25, 8))
    print (calc(lambda x, y: x - y, 25, 8))

if __name__ == '__main__':
    main()
=======

def calc(func, x, y):
    return func(x, y)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def main():
    print (calc(add, 10, 15))
    print (calc(lambda x, y: x + y, 10, 15))
    print (calc(sub, 25, 8))
    print (calc(lambda x, y: x - y, 25, 8))

if __name__ == '__main__':
    main()
>>>>>>> 3a3eeac04cbe757a5a977da746abe95ab991826d
