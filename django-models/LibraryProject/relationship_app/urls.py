from django.urls import path
from . import views
from .views import list_books, libraryDetailView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/int:pk>/', views.libraryDetailView.as_view(), name='library_detail'),
]