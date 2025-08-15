from django.shortcuts import render
from .models import Book,Author,Librarian,Library
from django.views.generic import DetailView

# Create your views here.
def AllBooksView(request):
    books = Book.objects.all()

    return render(request, "list_books", {"books": books})


class LibraryDetailView(DetailView):
    template_name = "library_detail.html"
    model = Library