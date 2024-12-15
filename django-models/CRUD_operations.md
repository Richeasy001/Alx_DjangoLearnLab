<!-- Create Operations -->
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected Output will be: 
1984 by George Orwell (1949)

# Retrieve Operation

```python
books = Book.objects.all()
print(books)

# Expected outputs will be: 
<QuerySet [<Book: 1984 by George Orwell (1949)>]>

# Update Operation

```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Expected output after the update will be: 
Nineteen Eighty-Four by George Orwell (1949)

# Delete Operation

```python
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()

# Expected output will be: 
<QuerySet []>