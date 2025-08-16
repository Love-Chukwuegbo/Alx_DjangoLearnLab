from django.urls import path
from .views import LibraryDetailView, AllBooksView


urlpatterns = [path("all/", AllBooksView, name="list_books"),
               path("library/", LibraryDetailView.as_view(), name="library_detail")
               
]