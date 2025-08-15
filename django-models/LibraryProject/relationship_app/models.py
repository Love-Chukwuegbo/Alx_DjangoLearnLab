from django.db import models

# Create your models here.
class Author(models.Model):
    name= models.CharField(max_length =50, null=True, blank=True)

class Book(models.Model):
    title = models.CharField(max_length = 100, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="book")

class Library(models.Model):
    name = models.CharField(max_length = 100, null=True, blank=True)
    books= models.ManyToManyField(Book, related_name="library")

class Librarian(models.Model):
    name = models.CharField(max_length = 100,null=True, blank=True)
    library= models.OneToOneField(Library, on_delete=models.CASCADE)