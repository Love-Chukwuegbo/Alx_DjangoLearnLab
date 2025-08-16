from django.shortcuts import render
from .models import Book,Author,Librarian,Library
from django.views.generic import DetailView

# Create your views here.
def AllBooksView(request):
    books = Book.objects.all()

    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    template_name = "relationship_app/library_detail.html"
    model = Library