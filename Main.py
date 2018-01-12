#for giggles letting this be the main driver for this first iteration of re-learning how to use Python

from LibraryClasses.Book import Book
from LibraryClasses.Person import Person
from LibraryClasses.BookLog import BookLog

person1 = Person("John", "PsyStreet")
person2 = Person("Mary", "NotPsyStreet")
book1 = Book(1, "Title1", "Author1")
book2 = Book(2, "Title2", "Author2")


booklog = BookLog(person1, book1)
booklog.check_out_book(person2, book2)
booklog.print_log()