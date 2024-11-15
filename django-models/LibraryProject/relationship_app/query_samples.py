import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# Query 2: Get all books in a specific library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # Many-to-many relation
    return books

# Query 3: Retrieve the librarian for a specific library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

if __name__ == "__main__":
    # Example: Query books by author "J.K. Rowling"
    books = books_by_author("J.K. Rowling")
    print("Books by J.K. Rowling:")
    for book in books:
        print(book.title)

    # Example: Query all books in a library "Central Library"
    books = books_in_library("Central Library")
    print("\nBooks in Central Library:")
    for book in books:
        print(book.title)

    # Example: Get librarian for library "Central Library"
    librarian = librarian_for_library("Central Library")
    print(f"\nLibrarian of Central Library: {librarian.name}")