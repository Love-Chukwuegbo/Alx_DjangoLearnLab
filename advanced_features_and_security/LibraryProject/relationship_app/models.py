from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser,UserManager
from django.db import models
from django.conf import settings

# Create your models here.



        


class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        permissions =[("can_add_book","can add book"),
                      ("can_change_book", "can change book"),
                      ("can_delete_book", "can delete book")]
    
    
    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name

User = settings.AUTH_USER_MODEL
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_choices=(
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member")
    )
    role =models.CharField(choices=role_choices,max_length=100)

    def __str__(self):
        return self.user

