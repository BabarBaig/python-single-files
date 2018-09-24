# import webbrowser

class Parent():
    def __init__(self, last_name, eye_color):
        print('Parent constructor called')
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print('Last Name - ' + self.last_name)
        print('Eye Color - ' + self.eye_color)

    def print_hello_parent(self):
        print('I\'m in the parent!')

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        Parent.__init__(self, last_name, eye_color)     # parent constructor called first
        self.number_of_toys = number_of_toys

    def print_hello_child(self):
        print('I\'m in the child!')

    def show_info(self):
        ''' Note that we access parent class' variables the EXACT same way as child
        class variables '''
        print('Last Name - ' + self.last_name)
        print('Eye Color - ' + self.eye_color)
        # Note that parent and child methods are invoked the exact same way
        self.print_hello_parent()
        self.print_hello_child()
        print('Number of Toys - ' + str(self.number_of_toys))

# billy_cyrus = Parent("Cyrus", "blue")
# billy_cyrus.show_info()
# print(billy_cyrus.last_name)
miley_cyrus = Child('Cyrus', 'Blue', 5)
    # Child class calls an inherited parent method below.  But if child has it's own
    # implementation, *that* implementation is called, overriding parent implementation
miley_cyrus.show_info()
# print(miley_cyrus.last_name)
# print(miley_cyrus.number_of_toys)
