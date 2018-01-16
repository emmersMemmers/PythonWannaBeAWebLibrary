import unittest
from LibraryClasses.Book import Book
from LibraryClasses.Person import Person
from LibraryClasses.Book_log import Book_log

class MyTestCase(unittest.TestCase):

#use setUp and tearDown for test setup and cleanup

    def test_book_not_null(self):
        book = Book(1, "title", "author")
        self.assertIsNotNone(book)

    def test_person_not_null(self):
        person = Person("Bob", "Wallabe Way")
        self.assertIsNotNone(person)

    def test_book_log_not_null(self):
        book_log = Book_log(Person("Bob", "Wallabe Way"), Book(1, "title", "author"))
        self.assertIsNotNone(book_log)

if __name__ == '__main__':
    unittest.main()
