from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser,UserManager
from django.db import models
from django.conf import settings

# Create your models here.

class CustomUserManager(UserManager):
    def create_user(self, username, email = None, password = None, **extra_fields):
        if not email:
            raise ValueError('Users must havee an email addresss')
        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, username, email= None, password = None, **extra_fields):
        extra_fields.setdefault ("is_staff" ,True)
        extra_fields.setdefault("is_superuser", True)
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_staff = True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser = True.")
        if not extra_fields.get("is_active"):
            raise ValueError("Superuser must have is_active = True.")

        return self.create_user(username, password, **extra_fields)

        
class CustomUser(AbstractUser):
    date_of_birth= models.DateField(null=True, blank= True)
    profile_photo=models.ImageField(upload_to="profile_photos/",  null=True, blank=True)
    objects = CustomUserManager()

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

