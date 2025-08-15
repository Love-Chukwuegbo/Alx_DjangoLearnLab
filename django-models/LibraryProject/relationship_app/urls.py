from django.urls import path
from .views import LibraryDetailView, AllBooksView


urlpatterns = [path("all/", AllBooksView.asview(), name="list_books"),
               path("library/", LibraryDetailView, name="library_detail")
               
]