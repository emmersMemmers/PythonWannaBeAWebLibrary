from LibraryClasses.Person import Person
from LibraryClasses.Book import Book

log = {}
book_collection = []


class Book_log:
    def __init__(self, person, book):
        log.update({person : book})

    def add_new_book(self, book):
            book_collection.append(book)

    def check_in_book(self, book, person):
        book_collection.append(book)
        log.pop(person)

    def check_out_book(self, person, book):
        if book in book_collection:
            book_collection.remove(book)
        log.update({person : book})

    def print_log(self):
        for item in log:
            print("Patron " + str(item.name) + " has book "+ str(log[item].title))
            #print("Patron " + str(item) + " has book: " + str(log[item]))
           # print(log[item])


