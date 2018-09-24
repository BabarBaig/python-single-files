
class JustCounter:
    ''' Class variables are visible by default. Here's how to make them invisible.
    For this Python renames the variable, so using its name produces an error.  Print
    statements at the end of the example show how to access the secret variable '''

    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)

myCounter = JustCounter()
myCounter.count()
myCounter.count()
# print(myCounter.__secretCount)  # Error: __secretCount cannot be accessed
print(myCounter._JustCounter__secretCount)  # Success
print(myCounter.__doc__)
