from . import models

# Query all books by a specific author
achebe =models.Author(name = "Chinua Achebe")
achebe.save()

Books =[models.Book(title= "Things fall apart", author= achebe),
        models.Book(title= "No longer at ease", author= achebe)]

new_book =models.Book(title= "The beautiful ones", author= achebe)


models.Book.objects.bulk_create(Books)
new_book.save()

books_by_achebe= models.Book.objects.filter(author = achebe)


# List all books in a library
futo= models.Library(name="Futo Library")

futo.save()
models.Library.objects.get(name= "Futo Library" )

models.Library.books.all()

#Retrieve the librarian for a library
librarian1=models.Librarian(name="Njoku",  library =futo)
librarian1.save()

models.Librarian.objects.filter(library =futo)