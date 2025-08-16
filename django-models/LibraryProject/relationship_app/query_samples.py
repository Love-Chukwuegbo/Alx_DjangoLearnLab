from .models import Library, Librarian,Author,Book

# Query all books by a specific author
achebe =Author.objects.create(name = "Chinua Achebe")


Books =[Book(title= "Things fall apart", author= achebe),
        Book(title= "No longer at ease", author= achebe)]
new_book =Book.objects.create(title= "The beautiful ones", author= achebe)
Book.objects.bulk_create(Books)


author = achebe
books_by_achebe= Book.objects.filter(author = author)


# List all books in a library
library= Library(name="Futo Library")

library.save()
library_name = "Futo Library"
library =Library.objects.get(name=library_name)
book_list =library.books.all()


#Retrieve the librarian for a library
librarian1=Librarian(name="Njoku",  library =library)
librarian1.save()

Librarian.objects.get(name ="Njoku")