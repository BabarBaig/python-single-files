
class Vector:
    ''' Point class represents and mainipulates x, y coordinates '''
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        # () around argument are necessary, or you get error:
        # TypeError: not enough arguments for format string
        # return ('Vector (%d, %d)' % (self.a, self.b))
        # The two return statements are identical
        return ('Vector ({0}, {1})'.format(self.a, self.b))

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1.__str__())
print(v2.__str__())
print( v1 + v2)
