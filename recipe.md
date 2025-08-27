# {{TABLE NAME}} Model and Repository Classes Design Recipe

## 1. Design and create the Table

```
# EXAMPLE

Table: books

Columns:
title | author_name
```

## 2. Create Test SQL seeds

## 3. Define the class names

```python
# EXAMPLE
# Table name: books

# Model class
# (in lib/books.py)
class Books


# Repository class
# (in lib/book_repository.py)
class BookRepository
```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# Table name: books

# Model class
# (in lib/books.py)

class Books:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.author_name = ""

    def __eq__(self):
        pass

    def __repr__(self):
        pass

# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> book = Book()
# >>> book.title = "Fifty Shades Of Gray"
# >>> book.author_name = "E L James"
# >>> book.title
# 'Fifty Shades Of Gray'
# >>> book.author_name
# 'E L James'

```

## 5. Define the Repository Class interface

```python
# EXAMPLE
# Table name: books

# Repository class
# (in lib/Book_repository.py)

class BookRepository():

    def __init__(self):
        self.connection = <connection>
    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, title, author_name FROM books;

        # Returns an array of Book objects.
```

## 6. Write Test Examples

```python
# EXAMPLES

"""
Test if book constructs with id, title and author_name
"""
book = Book(1, 'Fifty Shades Of Grey','E L James')
assert book.id == 1
assert book.title == 'Fifty Shades Of Grey'
assert book.author_name == 'E L James'

"""
Test if book formats nicely
"""
book = Book(1, 'Fifty Shades Of Grey','E L James')
assert str(book) == "Book(1, 'Fifty Shades Of Grey','E L James')"

"""
Test if books are equal
"""
book1 = Book(1, 'Fifty Shades Of Grey','E L James')
book2 = Book(1, 'Fifty Shades Of Grey','E L James')
assert book1 == book2


"""
Test if all method returns all books.
"""
db_connection.seed("seeds/book_store.sql")
repo = BookRepository(dbconnection)

books = repo.all()

assert books = [
    Book(1,'Nineteen Eighty-Four', 'George Orwell'),
    Book(2,'Mrs Dalloway', 'Virginia Woolf'),
    Book(3,'Emma', 'Jane Austen'),
    Book(4,'Dracula', 'Bram Stoker'),
    Book(5,'The Age of Innocence', 'Edith Wharton'),
]
```

Encode this example as a test.

## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
