class Rectangle:
    # "__" to make a variable private (within a class).
    # "_" to make a variable protected.
    __length = 0
    __width = 0

    def set_length(self, l):
        self.__length = l

    def set_width(self, w):
        self.__width = w

    def area(self):
        return self.__length * self.__width


rec = Rectangle
rec.set_width()
rec.set_length()