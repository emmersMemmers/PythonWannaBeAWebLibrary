from flask import Flask, render_template, redirect, url_for, request
from LibraryClasses.Book import Book
from LibraryClasses.Person import Person
from LibraryClasses.Book_log import Book_log

"""
my_log = []
person1 = Person("John", "PsyStreet")
person2 = Person("Mary", "NotPsyStreet")
book1 = Book(1, "Title1", "Author1")
book2 = Book(2, "Title2", "Author2")

booklog = Book_log(person1, book1)
booklog.check_out_book(person2, book2)
booklog.print_log()

my_log.append(booklog)

person1 = Person("John", "PsyStreet")
book1 = Book(1, "Title1", "Author1")
book_log = Book_log(Person, Book)
book_log.print_log()
"""

a_value = "Nothing"
list = []
app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def my_page():
    if request.method == "POST":
        #This section takes data from HTML page
        patron_value = request.form.get("patron-value", "")
        book_value = request.form.get("book-value", "")
        a_person = Person(patron_value, "none")
        a_person.add_book_to_person(Book(1, book_value, "none"))
        list.append(a_person)
        return redirect(url_for("my_page"))
    #pass data back to webpage
    return render_template("index.html", value=list)


@app.route("/another_page", methods=["GET", "POST"])
def cat_page():
    if request.method == "POST": #This section takes data from HTML page
        return redirect(url_for("my_page"))
    return render_template("cat_page.html") #This sends data to HTML page

if __name__ == "__main__":
    app.run(debug=True)
