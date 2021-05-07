<<<<<<< HEAD

class Point:
    ''' Point class represents and mainipulates x, y coordinates '''

    def __init__(self, x=0, y=0):
        ''' Create a new point at origin '''
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return (self.x**2 + self.y**2)**0.5

p = Point(3, 4)   # Instantiate an object of type Point
q = Point(6, 3)

print(p.x, p.y, q.x, q.y)
print(p.distance_from_origin())
=======

class Point:
    ''' Point class represents and mainipulates x, y coordinates '''

    def __init__(self, x=0, y=0):
        ''' Create a new point at origin '''
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return (self.x**2 + self.y**2)**0.5

p = Point(3, 4)   # Instantiate an object of type Point
q = Point(6, 3)

print(p.x, p.y, q.x, q.y)
print(p.distance_from_origin())
>>>>>>> 3a3eeac04cbe757a5a977da746abe95ab991826d
