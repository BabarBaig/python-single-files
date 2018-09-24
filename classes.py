<<<<<<< HEAD
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Baig-Admin
#
# Created:     13/10/2013
# Copyright:   (c) Baig-Admin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# ================================================================
class Car(object):
    # object is the most basic type of class to inherit from
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

    def display_car(self):
        return "This is a " + self.color + " " + self.model + " with " + \
            str(self.mpg) + " " + "MPG."

    def drive_car(self):
        self.condition = "used"

class ElectricCar(Car):
    #class ChildClass(ParentClass)
    # Note child class is inheriting from Parent, not object
    # Also note CamelCase naming
    def __init__(self, battery_type, model, color, mpg):
#   def __init__(self, model, color, mpg, battery_type):
        # Note that location of battery_type doesn't matter
        self.battery_type = battery_type
        self.model = model
        self.color = color
        self.mpg   = mpg

    def drive_car(self):
        # Note ovveride of parent method drive_car()
        self.condition = "like new"

def test_car():
    my_car = Car("DeLorean", "silver", 88)
    print("===================")
    print(my_car.model)
    print(my_car.color)
    print(my_car.mpg)
    print(my_car.condition)
    my_car.drive_car()
    print(my_car.condition)
    print("===================")

    my_car_e = ElectricCar("molten salt", "BMW", "black", 99.5)
    print(my_car_e.model)
    print(my_car_e.color)
    print(my_car_e.mpg)
    print(my_car_e.battery_type)
    print(my_car_e.condition)
    my_car_e.drive_car()
    print(my_car_e.condition)

# ================================================================
# Following class is completely unrelated to Car class. It's here because
# I want to keep all class-related concepts in one file
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        # Override the built-in representation method to correctly print a 3D
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

def test_3D():
    my_point = Point3D(1, 2, 3)
    print(my_point)     # Awesome functionality!

# ================================================================

def main():
#   test_car()
    test_3D()

if __name__ == '__main__':
    main()
=======
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Baig-Admin
#
# Created:     13/10/2013
# Copyright:   (c) Baig-Admin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# ================================================================
class Car(object):
    # object is the most basic type of class to inherit from
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

    def display_car(self):
        return "This is a " + self.color + " " + self.model + " with " + \
            str(self.mpg) + " " + "MPG."

    def drive_car(self):
        self.condition = "used"

class ElectricCar(Car):
    #class ChildClass(ParentClass)
    # Note child class is inheriting from Parent, not object
    # Also note CamelCase naming
    def __init__(self, battery_type, model, color, mpg):
#   def __init__(self, model, color, mpg, battery_type):
        # Note that location of battery_type doesn't matter
        self.battery_type = battery_type
        self.model = model
        self.color = color
        self.mpg   = mpg

    def drive_car(self):
        # Note ovveride of parent method drive_car()
        self.condition = "like new"

def test_car():
    my_car = Car("DeLorean", "silver", 88)
    print("===================")
    print(my_car.model)
    print(my_car.color)
    print(my_car.mpg)
    print(my_car.condition)
    my_car.drive_car()
    print(my_car.condition)
    print("===================")

    my_car_e = ElectricCar("molten salt", "BMW", "black", 99.5)
    print(my_car_e.model)
    print(my_car_e.color)
    print(my_car_e.mpg)
    print(my_car_e.battery_type)
    print(my_car_e.condition)
    my_car_e.drive_car()
    print(my_car_e.condition)

# ================================================================
# Following class is completely unrelated to Car class. It's here because
# I want to keep all class-related concepts in one file
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        # Override the built-in representation method to correctly print a 3D
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

def test_3D():
    my_point = Point3D(1, 2, 3)
    print(my_point)     # Awesome functionality!

# ================================================================

def main():
#   test_car()
    test_3D()

if __name__ == '__main__':
    main()
>>>>>>> 3a3eeac04cbe757a5a977da746abe95ab991826d
