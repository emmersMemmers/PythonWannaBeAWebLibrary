class Person:


    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books_person_has = []

    def __str__(self):
        return "Name: " + self.name + " Address: " + self.address

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def add_book_to_person(self, book):
        self.books_person_has.append(book)

