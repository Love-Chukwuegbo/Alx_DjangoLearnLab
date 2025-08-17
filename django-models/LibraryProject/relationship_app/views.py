from django.shortcuts import render,redirect
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