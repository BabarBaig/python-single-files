# Start with a procedural implementation, then make it more functional
# Looks good, except the syntax is not 100%, output is all wrong

def incr(x):
    return x + 1

def increment_each1(list1):
    list_incremented = []
    for x in list1:
        list_incremented.append(incr(x))
    return list_incremented

def main():
    print(increment_each1([1, 2, 3]))
    print((map(incr, [1, 2, 3])))
    #print(map(lambda x: x + 1, [1, 2, 3]))

if __name__ == '__main__':
    main()
