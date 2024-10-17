class Animal:
    def speak(self):
        print(f'Animal speaks')


class Dog(Animal):
    def speak(self):
        print(f'Dog barks')


animal_speak = Dog()
animal_speak.speak()
