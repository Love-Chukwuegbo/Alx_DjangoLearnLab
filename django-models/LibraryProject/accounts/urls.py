from django.urls import path
from .views import SignUpView

urlpatterns = [
    path("accounts/register", SignUpView.as_view(), name="register")
]