class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(f'Brand: {self.brand}')


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_info(self):
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')


carInfo = Car('Ford', 'Puma')
carInfo.show_info()
