from django.urls import path
from .views import list_books , LibraryDetailView, SignUpView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register/", SignUpView.as_view(), name= "register"),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path("books/", list_books, name="All_books"),
    # path("libraries", Librarylist.as_view(), name = "All_Libraries"),
    path("libraries/<int:id>", LibraryDetailView.as_view(), name = "specific_library_books"),
]