from flask import request, jsonify
from app.models.book_model import Book
from app import db

def add_book():
    data = request.get_json()
    new_book = Book (**data)
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Livro adicionado com sucesso!"}), 201

def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict()), 200

def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()
    book.title = data.get("title", book.title)
    book.author = data.get("author", book.author)
    book.year = data.get("year", book.year)
    book.genre = data.get("genre", book.genre)
    db.session.commit()
    return jsonify(book.to_dict()), 200

def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return '', 204
