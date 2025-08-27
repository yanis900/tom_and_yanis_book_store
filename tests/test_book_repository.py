from lib.book_repository import BookRepository
from lib.book import Book
from lib.database_connection import DatabaseConnection

"""
Test if all method returns all books.
"""
def test_all_method_returns_all_books(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repo = BookRepository(db_connection)

    books = repo.all()

    assert books == [
        Book(1,'Nineteen Eighty-Four', 'George Orwell'),
        Book(2,'Mrs Dalloway', 'Virginia Woolf'),
        Book(3,'Emma', 'Jane Austen'),
        Book(4,'Dracula', 'Bram Stoker'),
        Book(5,'The Age of Innocence', 'Edith Wharton'),
    ]