class Bookstore(object):
	def __init__ (self, name): 
		self.name = name 
		self.books = []
	def get_books(self):
		return self.books

	def add_book(self, book):
		self.books.append(book)

	def search_books(self, title=None, author=None):
		answer = []		
		# need to figure out if we are searching by title or author
		if (title == None) and author:
			# search by Author
			pass
			for book in self.books:
				if author.name == book.author.name:
					answer.append(book)
		elif title and (author == None):
			# Search by title 
			for book in self.books:
				if title.lower() in book.title.lower():
					answer.append(book)
		return answer
class Author(object):
	def __init__ (self, name, nationality): 
		self.name = name
		self.nationality = nationality

	def get_books(self):
		authors_books = [self.name]

		return authors_books
class Book(object):
	def __init__ (self, title, author):
		self.title = title
		self.author = author
