import turtle   # This Module has the Tutle class in it

__author__ = 'Bob'

class Shape():
    def __init__(self, shape1='turtle', speed1=10, color1='yellow'):
        self.wn = turtle.Screen()
        self.wn.bgcolor(color1)
        self.turtle1 = turtle.Turtle()
        self.turtle1.shape(shape1)
        self.turtle1.speed(speed1)

    def draw_square(self, distance):
        self.turtle1.forward(distance)
        self.turtle1.right(90)
        self.turtle1.forward(distance)
        self.turtle1.right(90)
        self.turtle1.forward(distance)
        self.turtle1.right(90)
        self.turtle1.forward(distance)
        self.turtle1.right(90)

    def draw_triangle(self, distance):
        self.turtle1.forward(distance)
        self.turtle1.right(120)
        self.turtle1.forward(distance)
        self.turtle1.right(120)
        self.turtle1.forward(distance)
        self.turtle1.right(120)

    def draw_squares(self):
        MAX_SQUARES =   9
        NUM_DEGREES =  40  # Turn 40-degrees
        LEN_OF_SIDE = 300

        for i in range (MAX_SQUARES):
            self.draw_square(LEN_OF_SIDE)
            self.turtle1.right(NUM_DEGREES)

    def draw_triangles(self):
        MAX_TRIANGLES =   9
        NUM_DEGREES   =  40  # Turn 40-degrees
        LEN_OF_SIDE   = 300

        for i in range (MAX_TRIANGLES):
            self.draw_triangle(LEN_OF_SIDE)
            self.turtle1.right(NUM_DEGREES)

    def exit1(self):
        self.wn.mainloop()
        #self.wn.exitonclick()

def main():
    # print(sys.argv)    # print command line arguments as a list [hello.py aaa bbb ccc]
    shape1 = Shape('turtle', 1)
    shape1.draw_triangles()
    shape1.draw_squares()
    shape1.exit1()

if __name__ == '__main__':
    main()
