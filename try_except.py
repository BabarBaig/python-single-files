<<<<<<< HEAD
#-------------------------------------------------------------------------------
# Name:        switch_equivalent.py
# Purpose:
#
# Author:      Baig-Admin
#
# Created:     2013-09-21
# Copyright:   (c) Baig-Admin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os

def function1():
    print("You chose one")

def function2():
    print("You chose two")

def function3():
    print("You chose three")

def switch_equivalent():
    switch = {      # Use a dictionary of functions
        'one':  function1,
        'two':  function2,
        'three':function3
    }
    choice = input("Enter one, two, or three: ")

    try:
        result = switch[choice]
    except KeyError:
        print("I don't understand your choice.  Please enter only: one, two, "
            "or three")
    else:
        result()

def main():
    switch_equivalent()

if __name__ == '__main__':
    main()

=======
#-------------------------------------------------------------------------------
# Name:        switch_equivalent.py
# Purpose:
#
# Author:      Baig-Admin
#
# Created:     2013-09-21
# Copyright:   (c) Baig-Admin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os

def function1():
    print("You chose one")

def function2():
    print("You chose two")

def function3():
    print("You chose three")

def switch_equivalent():
    switch = {      # Use a dictionary of functions
        'one':  function1,
        'two':  function2,
        'three':function3
    }
    choice = input("Enter one, two, or three: ")

    try:
        result = switch[choice]
    except KeyError:
        print("I don't understand your choice.  Please enter only: one, two, "
            "or three")
    else:
        result()

def main():
    switch_equivalent()

if __name__ == '__main__':
    main()

>>>>>>> 3a3eeac04cbe757a5a977da746abe95ab991826d
