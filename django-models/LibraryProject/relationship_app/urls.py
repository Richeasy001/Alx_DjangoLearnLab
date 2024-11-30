from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, CustomLoginView, CustomLogoutView, register

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]