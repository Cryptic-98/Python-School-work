class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    def set_title(self, t):
        self.__title = t

    def get_title(self):
        return self.__title

    def set_author(self, a):
        self.__author = a

    def get_author(self):
        return self.__author

    def set_price(self, p):
        if p > 0:
            self.__price = p

    def get_price(self):
        return self.__price


bk = Book('1984', 'George Orwell', '300')
bk.set_title(str(input('Enter book name: ').strip().capitalize()))
bk.set_author(str(input('Enter author name').strip().capitalize()))
bk.set_price(float(input('Enter book price: ').strip()))
print(f'Book name: {bk.get_title()}')
print(f'Author: {bk.get_author()}')
print(f'Price: {bk.get_price()}')
