from django.contrib import admin
from .models import Book, Author, Librarian, Library
from .models import CustomUser,CustomUserManager
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class  ModelAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = ((None, {"fields":("date_of_birth",'profile_photo')})
                     ,)
admin.site.register(CustomUser,ModelAdmin)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Librarian)
admin.site.register(Library)