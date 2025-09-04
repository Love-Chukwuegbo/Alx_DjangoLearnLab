from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# Register your models here.

from .models import Book  
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("title", "publication_year")

class  CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = ((None, {"fields":("date_of_birth",'profile_photo')})
                     ,)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Book, BookAdmin)
