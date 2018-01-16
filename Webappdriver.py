from flask import Flask, render_template, redirect, url_for, request
from LibraryClasses.Book import Book
from LibraryClasses.Person import Person
from LibraryClasses.Book_log import Book_log

my_log = []

person1 = Person("John", "PsyStreet")
person2 = Person("Mary", "NotPsyStreet")
book1 = Book(1, "Title1", "Author1")
book2 = Book(2, "Title2", "Author2")

booklog = Book_log(person1, book1)
booklog.check_out_book(person2, book2)
booklog.print_log()

app = Flask(__name__)


@app.route("/")#, methods=["GET", "POST"])
def my_page():
    """
    if request.method == "POST":
        new_person_name = request.form.get("person-name", "")
        new_person_address = ""
        new_book_title = request.form.get("book-title", "")
        new_book_id = 1
        new_book_author = ""

        new_person = Person(new_person_name, new_person_address)
        new_book = Book(new_book_id, new_book_title, new_book_author)
        new_book_log = BookLog(new_person, new_book)
        my_log.append(new_book_log)
        return redirect(url_for("my_page"))
    return render_template("index.html", my_log=my_log)
    """
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
