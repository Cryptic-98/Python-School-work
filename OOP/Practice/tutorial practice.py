class Book:
    def __init__(self, title, author, genre, year_published):
        self.title = title
        self.author = author
        self.genre = genre
        self.year_published = year_published

    def display_book_info(self):
        print(f'Book Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Genre: {self.genre}')
        print(f'Year Published: {self.year_published}')

bookInfo = Book('1984', 'George Orwell', 'Fantasy', '1933')
bookInfo.display_book_info()