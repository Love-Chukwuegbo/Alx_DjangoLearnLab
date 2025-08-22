from .models import Book, Library,Librarian,Author
# Query all books by a specific author\

achebe = Author(name = "Chinua Achebe")
adichie = Author(name ="Chimamanda Adichia")

book1 = Book.objects.create(title ="Things fall Apart", author = achebe)
book2 = Book.objects.create(title ="No longer at ease", author = achebe)
book3 = Book.objects.create(title ="Purple hibiscus", author = adichie)

books_by_achebe = Book.objects.filter(author = achebe)


# List all books in a library
lib1 = Library.objects.get(name = "lib1")
books_in_lib1=lib1.books.all()

# Retrieve the librarian for a library
libarian_for_lib1 = Librarian.objects.get(library__name= "lib1")