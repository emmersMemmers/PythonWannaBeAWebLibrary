class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return "Name: " + self.name + " Address: " + self.address

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address
