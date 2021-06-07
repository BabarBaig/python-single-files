import math

def area(base, height):
    '''(number, nmuber) -> float
    Return the area of a triangle with dimensions base and height.
    >>>area(10, 40)
    200.0
    >>>area(3.4, 7.5)
    12.75
    '''
    return base * height / 2

def perimeter(side1, side2, side3):
    '''(number, number, number) -> number
    Return the perimenter of a triangle, given the length of its three sides
    side1, side2, side3
    >>>perimeter(3, 4, 5)
    12
    >>>perimeter(105., 6, 9.3)
    25.8
    '''
    return side1+side2+side3

def semiperimeter(side1, side2, side3):
    '''(number, number, number) -> float
    Return the semiperemeter of a triangle, given the length of sides
    side1, side2, side3
    semiperimeter(3, 4, 5)
    6.0
    semiperemeter(10.5, 6, 9.3)
    12.9
    '''
    return perimeter(side1, side2, side3)/2


def area_hero(side1, side2, side3):
    '''
    (number, number, number) -> float
    Using Hero's formula, return the area of a triangle given sides of length
    side1, side2, side3
    >>>area_hero(3, 4, 5)
    6.0
    >>>area_hero(10.5, 6, 9.3)
    27.73168584850189
    '''
    semi = semiperimeter(side1, side2, side3)
    return math.sqrt(semi*(semi-side1)*(semi-side2)*(semi-side3))
