from LibraryClasses.Person import Person
from LibraryClasses.Book import Book

#log = {}
#book_collection = []


class Book_log:
    def __init__(self, person, book):
        self.log = {}
        self.book_collection = []
        self.log.update({person : book})

    def add_new_book(self, book):
        book_collection.append(book)

    def check_in_book(self, book, person):
        self.book_collection.append(book)
        self.log.pop(person)

    def check_out_book(self, person, book):
        if book in self.book_collection:
            self.book_collection.remove(book)
        self.log.update({person : book})

    def print_log(self):
        for item in self.log:
            print("Patron " + str(item.name) + " has book "+ str(log[item].title))
            #print("Patron " + str(item) + " has book: " + str(log[item]))
           # print(log[item])


