#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Baig-Admin
#
# Created:     14/10/2013
# Copyright:   (c) Baig-Admin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# ==============================================
def test_dict():
    # Dict Hash Table
    # Python's efficient key/value hash table structure is called a "dict".
    # Build a dict by starting with the the empty dict {} and storing key/value
    # pairs: dict[key] = value-for-that-key
    #   dict = {}
    #   dict['a'] = 'alpha'
    #   dict['g'] = 'gamma'
    #   dict['o'] = 'omega'
    dict = {'a': 'alpha', 'g': 'gamma', 'o': 'omega'}   # Much shorter!

    print(dict)                 # {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
    print(dict['a'])            # Simple lookup, returns 'alpha'

    dict['a'] = 6               # Put new key/value into dict
    'a' in dict                 # True
#   print(dict['z'])            # Throws KeyError
    if 'z' in dict:
        print(dict['z'])        # Avoid KeyError
    print(dict.get('z'))        # None (instead of KeyError)

    # By default, iterating over a dict iterates over its keys.
    # Note that the keys are in a random order.
#   for key in dict:            # prints a \n g \n o
#       print(key)
#   for key in dict.keys():     # Exactly the same as above
#       print(key)

    # Get the .keys() list:
    print(dict.keys())          # ['a', 'o', 'g']
    # Likewise, there's a .values() list of values
    print(dict.values())        # ['alpha', 'omega', 'gamma']

    # Common case -- loop over the keys in sorted order, accessing each key/value
    for key in sorted(dict.keys()): # Sorting a dict is very tricky! Lots of posts
        print(key, dict[key])
    # .items() is the dict expressed as (key, value) tuples
    print(dict.items())         #  [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]

    # This loop syntax accesses the whole dict by looping over the .items() tuple
    # list, accessing one (key, value) pair on each iteration.
    for k, v in dict.items():
        print(k, '>', v)        # a > alpha    o > omega     g > gamma

    # Dict Formatting: Use the % operator to substitute values from a dict into a string by name
    print('The value of "a" is %(a)d' % dict)
    print('The value of "g" is %(g)s' % dict)

# ==============================================
def test_del():
    var1 = 5
    print(var1)
    del var1
#   print(var1)     UnboundLocalError: local variable 'var1' referenced before assignment

    list = ['a', 'b', 'c', 'd']
    print(list)     # ['a', 'b', 'c', 'd']
    del list[0]     # Delete first element
    print(list)     # ['b', 'c', 'd']
    del list[-2:]   # Delete last two elements
    print(list)     # ['b']

    dict = {'a':1, 'b':2, 'c':3}
    del dict['b']   # Delete key/value entry for 'b'
    print(dict)     # {'a':1, 'c':3}

# ==============================================
def main():
#   test_dict()
    test_del()

if __name__ == '__main__':
    main()
