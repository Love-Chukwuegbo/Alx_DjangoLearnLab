from .models import Book, Library, Librarian, Author

# Create authors and save them to the DB
achebe = Author.objects.create(name="Chinua Achebe")
adichie = Author.objects.create(name="Chimamanda Adichie")

# Create books with correct titles and saved authors
book1 = Book.objects.create(title="Things Fall Apart", author=achebe)
book2 = Book.objects.create(title="No Longer at Ease", author=achebe)
book3 = Book.objects.create(title="Purple Hibiscus", author=adichie)

# Query all books by Achebe
books_by_achebe = Book.objects.filter(author=achebe)

# Get library instance named 'lib1'
library_lib1 = Library.objects.get(name="lib1")

# List books in the library 'lib1'
books_in_lib1 = library_lib1.books.all()

# Retrieve the librarian for 'lib1'
librarian_for_lib1 = Librarian.objects.get(library__name="lib1")
