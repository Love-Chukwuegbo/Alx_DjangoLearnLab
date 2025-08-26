from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic import ListView

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth import login
from django.contrib.auth import logout

from django.contrib.auth.decorators import user_passes_test
from . import helpers

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view to show library details using generic ListView
class Librarylist(ListView):
    model = Library
    template_name = "relationship_app/library_detail.html"

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})



@user_passes_test(helpers.is_admin)
def admin(request):
    render(request, "admin_view.html")


@user_passes_test(helpers.is_librarian)
def librarian(request):
    render(request, "librarian_view.html")

@user_passes_test(helpers.is_member)
def member(request):
    render(request, "member_view.html")
