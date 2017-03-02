# Hint 1 - The interface

If you check the tests, the public interface of our classes is obvious. For example, to create a bookstore you do:

```python
Bookstore("Rmotr's bookstore")
```

That means, that the the bookstore has an `__init__` method that receives a `name` parameter:

```python
class Bookstore(object):
    def __init__(self, name):
        self.name = name
```

We also have a few methods exposed on the bookstore class:

* `get_books()` receives no parameters and returns a list of books in our bookstore
* `search_books` receives **either** `title` or `author` and returns all the books that satisfy that condition (start with the given title or were written by the given author)

So we can say that those methods will be defined as:

```python
class Bookstore(object):
    def get_books(self):  # no paramters
        pass
        
    def search_books(self, title=None, author=None):  # Both parameters are optional
        pass
```
