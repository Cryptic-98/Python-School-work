# creating a class
class Rectangle:
    length = 0
    width = 0

    def getArea(self):
        return self.length * self.width

    def getParameter(self):
        return 2 * (self.length + self.width)


# creating an object of class Rectangle.
obj = Rectangle()
obj.length = float(input('Enter length of your rectangle: '))
obj.width = float(input('Enter width of rectangle: '))
print(f'The area of the rectangle is {obj.getArea()}')
print(f'The parameter of the rectangle is {obj.getParameter()}')
