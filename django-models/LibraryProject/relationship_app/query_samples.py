from .models import Library, Librarian,Author,Book

# Query all books by a specific author
achebe =Author(name = "Chinua Achebe")
achebe.save()

Books =[Book(title= "Things fall apart", author= achebe),
        Book(title= "No longer at ease", author= achebe)]

new_book =Book(title= "The beautiful ones", author= achebe)


Book.objects.bulk_create(Books)
new_book.save()

books_by_achebe= Book.objects.filter(author = achebe)


# List all books in a library
library= Library(name="Futo Library")

library.save()
library =Library.objects.get(name="Futo Library")
book_list =library.books.all()


#Retrieve the librarian for a library
librarian1=Librarian(name="Njoku",  library =library)
librarian1.save()

Librarian.objects.get(name ="Njoku")