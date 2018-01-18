from flask import Flask, render_template, redirect, url_for, request
from LibraryClasses.Book import Book
from LibraryClasses.Person import Person
from LibraryClasses.Book_log import Book_log

list = []
app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def my_page():
    if request.method == "POST": #This section takes data from HTML page
        #get data from html page
        #person = request.form.get("person", "")
        #book = request.form.get("book", "")
        patron_value = request.form.get("patron-value", "")
        book_value = request.form.get("book-value", "")
        a_person = Person(patron_value, "none")
        a_person.add_book_to_person(Book(1, book_value, "none"))
        list.append(a_person)



        #update psuedo backend
        #book_log.check_out_book(Person(person, "none"), Book(1, book, "none"))

        #redirect to the html page
        return redirect(url_for("my_page"))
    #pass data back to webpage
    return render_template("index.html", value=list) #This sends data to HTML page
   


if __name__ == "__main__":
    app.run(debug=True)
