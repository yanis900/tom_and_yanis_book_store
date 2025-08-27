from lib.book import Book

"""
Test if book constructs with id, title and author_name
"""
def test_book_constructs():
    book = Book(1, 'Fifty Shades Of Grey','E L James')
    assert book.id == 1
    assert book.title == 'Fifty Shades Of Grey'
    assert book.author_name == 'E L James'
    
"""
Test if book formats nicely
"""
def test_book_formats_nicely():
    book = Book(1, 'Fifty Shades Of Grey', 'E L James')
    assert str(book) == "1 - Fifty Shades Of Grey - E L James"
    
"""
Test if books are equal
"""
def test_books_are_equal():
    book1 = Book(1, 'Fifty Shades Of Grey','E L James')
    book2 = Book(1, 'Fifty Shades Of Grey','E L James')
    assert book1 == book2
