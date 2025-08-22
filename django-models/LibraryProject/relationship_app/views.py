from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import ListView,DetailView

# Function-based view to list all books
def booklist(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view to show library details using generic ListView
class Librarylist(ListView):
    model = Library
    template_name = "relationship_app/library_detail.html"

class LibraryDetail(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
