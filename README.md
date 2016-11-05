# OOP Bookstore

Today, we're in charge of migrating our Bookstore project into an Object Oriented approach. The functionality will remain similar, but we'll use OOP to model our system.

For this project we have identified 3 key classes: `Bookstore`, `Author` and `Book`.

A `Bookstore` will be the starting point. You'll be able to add books and search from books in a bookstore object. In the following example, we'll create a bookstore and assign a book to it:

```python
store = Bookstore("Rmotr's bookstore")
# No books yet
store.get_books() == []

# We create an author and book
borges = Author("Jorge Luis Borges", "Argentina")
ficciones = Book("Ficciones", author=borges)

# We add the book to the bookstore
store.add_book(ficciones)

store.get_books() == [<Object Book('ficciones')>]
```

The bookstore also has a "search" functionality. It works a little bit different than the previous one. In this case, you can search by book title or book author, or both title **and** author. The search method is the same one `search_books`, but you'll have to make it dynamic enough to support the three scenarios. Example:

```python
# Searching *just* by title:
store.search_books(title='raven')

# Searching *just* by author:
poe = Author('Edgar Allan Poe', 'US')
store.search_books(author=poe)

# Searching by both title *and* author:
poe = Author('Edgar Allan Poe', 'US')
store.search_books(title='raven', author=poe)
```

Finally, the `Book` and `Author` classes have special relationships between them, and we want you to pay special attention to it.
