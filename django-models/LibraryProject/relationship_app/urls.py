from django.urls import path
from .views import list_books , LibraryDetailView
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("register/", views.register, name= "register"),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path("admins/" , views.admin, name = "Admin"),
    path("librarian/", views.librarian, name = "Librarian"),
    path("member/", views.member, name = "Member"),
    path("books/", list_books, name="All_books"),
    # path("libraries", Librarylist.as_view(), name = "All_Libraries"),
    path("libraries/<int:id>", LibraryDetailView.as_view(), name = "specific_library_books"),
]