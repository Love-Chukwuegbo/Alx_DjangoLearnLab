
from django.db import models

# Create your models here.
from .models import Book, Library, Librarian, Author

# Create and save authors
achebe = Author.objects.create(name="Chinua Achebe")
adichie = Author.objects.create(name="Chimamanda Adichie")

# Create books for authors
book1 = Book.objects.create(title="Things Fall Apart", author=achebe)
book2 = Book.objects.create(title="No Longer at Ease", author=achebe)
book3 = Book.objects.create(title="Purple Hibiscus", author=adichie)

# Query all books by Achebe
books_by_achebe = Book.objects.filter(author=achebe)

# Get library named 'lib1'
library_lib1 = Library.objects.get(name="lib1")  # if one library expected

# List all books in library 'lib1'
books_in_lib1 = library_lib1.books.all()

# Retrieve the librarian for library 'lib1'
librarian_for_lib1 = Librarian.objects.get(library__name="lib1")

