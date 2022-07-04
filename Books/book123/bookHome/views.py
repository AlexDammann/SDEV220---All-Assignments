from flask import Flask
Home = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

Home.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(Home)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

def __repr__(self):
    return f"{self.name} - {self.description}"

@Home.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {'name': Book.name, 'description': Book.description}
        output.appened(book_data)
    return {"books": output}