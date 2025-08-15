from django.contrib import admin
from .models import Author, Book, Library, Librarian

# Register your models here.
admin.register(Author, Book, Library,Librarian)