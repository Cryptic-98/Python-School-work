# working with constructors
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    # what do we do if we want to change a value.
    # we create getters and setters

    def set_length(self, l):
        self.length = l

    def get_length(self):
        return self.length

    def set_width(self, w):
        self.width = w

    def get_width(self):
        return self.width

    def area(self):
        return self.length * self.width

    def parameter(self):
        return 2 * (self.length + self.width)


rec = Rectangle(10, 8)
rec.set_length(15)
rec.set_width(3)
# ↑ constructor
print(f'The parameter of a rectangle is {rec.parameter()}cm')
print(f'The area of a rectangle is {rec.area()}cm²')
