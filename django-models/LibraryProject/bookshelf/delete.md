# Delete Operation

## Command to delete the book:
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Expected output will be: <QuerySet []>