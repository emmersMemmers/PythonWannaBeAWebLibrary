class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author

    def __str__(self):
        return "ID: " + str(self.id) + " Title: " + self.title + " Author " + self.author

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_id(self):
        return self.id