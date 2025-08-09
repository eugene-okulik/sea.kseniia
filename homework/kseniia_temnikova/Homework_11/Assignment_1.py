class Book:
    made_of = 'бумага'
    text_persistance = True

    def __init__(self, title, author, pages_number, isbn, is_reserved):
        self.title = title
        self.author = author
        self.pages_number = pages_number
        self.isbn = isbn
        self.is_reserved = is_reserved

    def book_info(self):
        message = f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages_number},' \
                  f' материал: {self.made_of}'
        if self.is_reserved:
            print(message + ', зарезервирована ')
        else:
            print(message)


class TextBook(Book):

    def __init__(self, title, author, pages_number, isbn, is_reserved, subject, group, homework):
        super().__init__(title, author, pages_number, isbn, is_reserved)
        self.subject = subject
        self.group = group
        self.homework = homework

    def text_book_info(self):
        message = f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages_number},' \
                  f' предмет: {self.subject}, класс: {self.group}'
        if self.is_reserved:
            print(message + ', зарезервирована ')
        else:
            print(message)


dostoevsky_idiot_book = Book('Идиот', 'Достоевский', 500, 34567, True)
folklor_kolobok_book = Book('Колобок', 'Фольклор', 4, 76679, False)
pushkin_kapitan_book = Book('Капитанская дочка', 'Пушкин', 55, 98876, False)
pasternak_doctor_book = Book('Доктор Живаго', 'Пастернак', 100, 7665, False)
goncharov_oblomov_book = Book('Обломов', 'Гончаров', 89, 5673, False)

folklor_kolobok_book.is_reserved = True
dostoevsky_idiot_book.book_info()
folklor_kolobok_book.book_info()
pushkin_kapitan_book.book_info()
pasternak_doctor_book.book_info()
goncharov_oblomov_book.book_info()

math_book_9 = TextBook('Алгебра', 'Иванов', 400, 4639, False, 'Математика', 9, False)
russian_book_8 = TextBook('Тонкости русского языка', 'Петров', 150, 647483, False, 'Русский язык', 8, 'False')
physical_culture_book_10 = TextBook('Рост и развитие', 'Николаев', 45, 56747, False, 'Физ-ра', 10, False)

physical_culture_book_10.is_reserved = True
math_book_9.text_book_info()
russian_book_8.text_book_info()
physical_culture_book_10.text_book_info()
