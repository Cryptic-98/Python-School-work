class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def set_make(self, m):
        self.__make = m

    def get_make(self):
        return self.__make

    def set_model(self, md):
        self.__model = md

    def get_model(self):
        return self.__model

    def set_year(self, y):
        if 1885 < y < 2024:
            self.__year = y

    def get_year(self):
        return self.__year


cr = Car('Toyota', 'Corolla', 2010)
cr.set_make(input('Enter car brand: ').strip().capitalize())
cr.set_model(str(input('Enter model: ').strip()))
cr.set_year(int(input('Enter year: ').strip()))
print(f'Make: {cr.get_make()}')
print(f'Model: {cr.get_model()}')
print(f'Year: {cr.get_year()}')
