from django.shortcuts import render
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login

# Create your views here.
def list_books(request):
    books = Book.objects.all()

    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    template_name = "relationship_app/library_detail.html"
    model = Library



class register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'