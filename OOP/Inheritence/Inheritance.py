class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def set_length(self, l):
        self.length = l

    def get_length(self):
        return self.length

    def set_width(self, w):
        self.width = w

    def get_width(self):
        return self.width

    # inheriting ↓
class Rectangle(Shape):
    def __init__(self, l, w):
        super.__init__(l, w)

    def get_area(self):
        return self.length * self.width

    def get_parameter(self):
        return 2 * (self.length + self.width)


rec = Rectangle(10, 7)
rec.set_length('9')
rec.set_width('18')
print(f'The area of your rectangle is {rec.get_area()}')
print(f'The parameter of your rectangle is {rec.get_parameter()}')