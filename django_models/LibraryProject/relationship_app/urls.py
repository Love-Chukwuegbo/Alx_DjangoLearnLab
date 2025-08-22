from django.urls import path
from . import views 

urlpatterns = [
    path("books", views.booklist, name="All_books"),
    path("libraries", views.Librarylist.as_view(), name = "All_Libraries"),
    path("libraries/<int:id>", views.LibraryDetail.as_view(), name = "specific_library_books"),
]