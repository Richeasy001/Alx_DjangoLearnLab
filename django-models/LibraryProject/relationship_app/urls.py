from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, LoginView, LogoutView, register

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view("relationship_app/login.html"), name='login'),
    path('logout/', LogoutView.as_view("relationship_app/logout.html"), name='logout'),
    path('register/', views.register, name='register'),
]