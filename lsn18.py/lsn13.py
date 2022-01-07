# Task 1 Method overloading
def animal_sound(animal):
    return animal.talk()


class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        return 'woof woof'


class Cat(Animal):
    def talk(self):
        return 'meow'


dog = Dog()
cat = Cat()

print(animal_sound(dog))
print(animal_sound(cat))


# Task 2 Library
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        Book.books_count += 1
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author):
        return author

    def group_by_year(self, year):
        books = ''
        for book in self.books:
            if book.year == year:
                books += str(book)
        return books

    def __str__(self):
        authors = ''
        for author in self.authors:
            authors += str(author)
        return authors

    def __repr__(self):
        return self.__str__()


class Book:
    books_count = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        author.books.append(self)

    def __str__(self):
        return f'{self.name} {self.year}\n'

    def __repr__(self):
        return self.__str__()


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        books = ''
        for book in self.books:
            books += '\t'
            books += str(book)
        return f'\n{"-"*100}\n' \
               f'Name: {self.name}\n' \
               f'Country: {self.country}\n' \
               f'Birthday: {self.birthday}\n' \
               f'Books:\n{books}' \
               f'{"-"*100}'

    def __repr__(self):
        return self.__str__()


library = Library('Scylla')

author_1 = Author('Taras Shevchenko', 'Ukraine', '25.12.1814')
author_2 = Author('Alexandre Dumas', 'France', '24.07.1802')

library.new_book('Kobzar', 1840, author_1)
library.new_book('Hudozshnik', 1856, author_1)
library.new_book('Los tres Mosqueteros', 1844, author_2)
library.new_book('Monte Cristo', 1846, author_2)

print(library)
print(Book.books_count)


# Task 3 Fraction
class Fraction:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        num_2 = self.num_2 * other.num_2
        num_1 = (self.num_2*other.num_1) + (other.num_2*self.num_1)
        return Fraction(*self.cheker(num_1, num_2))

    def __sub__(self, other):
        num_2 = self.num_2 * other.num_2
        num_1 = (self.num_2 * other.num_1) - (other.num_2 * self.num_1)
        return Fraction(*self.cheker(num_1, num_2))

    def __mul__(self, other):
        num_1 = self.num_1 * other.num_1
        num_2 = self.num_2 * other.num_2
        return Fraction(*self.cheker(num_1, num_2))

    def __truediv__(self, other):
        other.num_1, other.num_2 = other.num_2, other.num_1
        num_1 = self.num_1 * other.num_1
        num_2 = self.num_2 * other.num_2
        return Fraction(*self.cheker(num_1, num_2))

    def cheker(self, num_1, num_2):
        for n in range(2, 11):
            if num_1 % n == 0 and num_2 % n == 0:
                checked_num_1 = num_1 / n
                checked_num_2 = num_2 / n
                return int(checked_num_1), int(checked_num_2),
        return num_1, num_2,

    def __str__(self):
        return f'{self.num_1}/{self.num_2}'

    def __repr__(self):
        self.__str__()


x = Fraction(1, 2)
y = Fraction(1, 4)
print(x + y)
print(x - y)
print(x * y)
print(x / y)
