# Bookstore management system

You're in charge of building a simple Bookstore system.

Please pay attention to the data structures used and the interfaces provided.

```python
store = Bookstore("Rmotr's bookstore")
store.books == []

borges = Author("Jorge Luis Borges", "Argentina")
ficciones = Book("Ficciones", author=borges)

store.add_book(ficciones)

store.search(title='ficciones')
store.search(author=borges)


```
