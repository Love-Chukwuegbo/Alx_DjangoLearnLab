from django.contrib import admin
from .models import Book, Author, Librarian, Library
# Register your models here.
admin.register(Book,Author, Librarian,Library)