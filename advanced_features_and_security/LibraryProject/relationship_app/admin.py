from django.contrib import admin
from .models import Book, Author, Librarian, Library



admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Librarian)
admin.site.register(Library)