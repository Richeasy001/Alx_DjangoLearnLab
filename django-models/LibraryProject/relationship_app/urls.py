from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, LoginView, LogoutView, register, admin_view, librarian_view, member_view

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]