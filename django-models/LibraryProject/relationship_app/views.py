from django.shortcuts import render,redirect,get_object_or_404

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

from django.contrib.auth.decorators import user_passes_test, permission_required
from . import helpers
from  . import forms
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
def admin_view(request):
    render(request, "relationship_app/admin_view.html")


@user_passes_test(helpers.is_librarian)
def librarian_view(request):
    render(request, "relationship_app/librarian_view.html")

@user_passes_test(helpers.is_member)
def member_view(request):
    render(request, "relationship_app/member_view.html")



@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    if request.method == "POST":

        form = forms.CreateBook(request.POST)

        if form.is_valid():
            book = form.save()
            return redirect("book_detail",pk = book.pk  )

    else:
        form = forms.CreateBook()
    return render(request, "relationship_app/add_books.html", {"form":form} )
    
def book_detail(request, pk):
    book = Book.objects.get(id=pk)
    return render(request, "relationship_app/book_detail.html",{"book" : book})


@permission_required("relationship_app.can_change_book",raise_exception=True)
def change_book(request,pk):
    book = get_object_or_404(Book, pk = pk)

    if request.method == "POST":
        form = forms.CreateBook(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_detail", pk = book.pk)
    else:
        form=forms.CreateBook(instance= book)
    
    return render(request, "relationship_app/add_books.html",{ "form":form })
    


@permission_required("relationship_app.can_delete_book",raise_exception=True)
def delete_book(request, pk):
    book=get_object_or_404(book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    else:
        return render(request," relationship_app/confirm_delete.html",{"book":book})
