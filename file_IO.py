# https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
'''
Question 9:
Write a program that accepts a sequence of whitespace separated words as input and prints
the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again. Then, the output should be:
again and hello makes perfect practice world
    s = raw_input()
    words = [word for word in s.split(" ")]
    print " ".join(sorted(list(set(words))))
'''
def rmDups(filepath):
    with open(filepath) as fp:
        my_array = fp.readlines()   # Read data.txt as a single string in list[""]
    # De-dent => implicitly close filepath
    my_array = my_array[0].split(' ')   # Break single string into separate words
    my_array = set(my_array)    # Use set()- container to remove duplicates from list my_array[]
    my_array = sorted(my_array)
    return my_array

print(rmDups("C:/001/01/Python/Data/data_001.txt"))


'''Write a program which accepts a sequence of comma separated 4 digit binary numbers as
its input and then check whether they are divisible by 5 or not. The numbers that are
divisible by 5 are to be printed in a comma separated sequence.
Example:                   0100,0011,1010,1001
Then the output should be: 1010
Notes: Assume the data is input by console.
Hints: In case of input data being supplied to the question, it should be assumed to be a
console input.
Solution:
value = []
items=[x for x in raw_input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)
print ','.join(value)'''
# End
