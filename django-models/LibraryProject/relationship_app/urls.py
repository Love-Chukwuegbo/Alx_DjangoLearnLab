from django.urls import path
from .views import list_books , LibraryDetailView

urlpatterns = [
    path("books", list_books, name="All_books"),
    # path("libraries", Librarylist.as_view(), name = "All_Libraries"),
    path("libraries/<int:id>", LibraryDetailView.as_view(), name = "specific_library_books"),
]