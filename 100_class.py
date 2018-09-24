import sys

class Employee:
    'MyClass.__doc__ http://www.tutorialspoint.com/python/python_classes_objects.htm'
    empCount = 0

    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print('Total Employee %d' % Employee.empCount)  # Note syntax for empCount

    def displayEmployee(self):
        print('Name:', self.name, ', Salary:', self.salary)

def main():
    John = Employee('John', 60000)
    Jack = Employee('Jack', 70000)
    John.displayEmployee()
    Jack.displayEmployee()
    John.displayCount()     # Class variable assessed via class instance
    Jack.displayCount()
    print('Total Employee %d' % Employee.empCount)  # Directly access class variable!

    # You can add, remove or modify attributes of classes and objects at any time:
    # I think this is poor coding style--directly manipulating class variables
    # John.age = 47  # Add an 'age' attribute.
    # print('John\'s age: %d' % John.age)
    # John.age = 48  # Modify 'age' attribute.
    # print('John\'s age: %d' % John.age)
    # del John.age  # Delete 'age' attribute.

    # Better to use getters/setters
    print('We know John\' age: %s' % hasattr(John, 'age'))    # Returns true if 'age' attribute exists
    setattr(John, 'age',38)
    print('We know John\'s age: %s' % hasattr(John, 'age'))    # Returns true if 'age' attribute exists
    print('John is: %d years old' % getattr(John, 'age'))    # Returns value of 'age' attribute
    delattr(John, 'age')
    print('We know John\' age: %s' % hasattr(John, 'age'))    # Returns true if 'age' attribute exists
    '''
    Every Python class keeps following built-in attributes and they can be accessed
    using dot operator like any other attribute:
    __dict__  : Dictionary containing the class's namespace.
    __doc__   : Class documentation string or None if undefined.
    __name__  : Class name.
    __module__: Module name in which the class is defined. This attribute is "__main__" in interactive mode.
    __bases__ : A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.
    '''
    print("Employee.__doc__:"   , Employee.__doc__)
    print("Employee.__name__:"  , Employee.__name__)
    print("Employee.__module__:", Employee.__module__)
    print("Employee.__bases__:" , Employee.__bases__)
    print("Employee.__dict__:"  , Employee.__dict__)

    #for i in range (10):
    #    print("Hello, world!!!")
    #print(sys.argv)    # print command line arguments as a list [hello.py aaa bbb ccc]

if __name__ == '__main__':
    main()
