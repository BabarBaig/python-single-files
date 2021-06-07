<<<<<<< HEAD

def a(x, y, z):
    if x:
        return y
    else:
        return z

def b(q, r):
    return a(q>r, q, r)

#print(a(False, 2, 3))
#print(b(3, 2))
#print(a(3>2, a, b))
print(b(a, b))

=======

def a(x, y, z):
    if x:
        return y
    else:
        return z

def b(q, r):
    return a(q>r, q, r)

#print(a(False, 2, 3))
#print(b(3, 2))
#print(a(3>2, a, b))
print(b(a, b))

>>>>>>> 3a3eeac04cbe757a5a977da746abe95ab991826d
