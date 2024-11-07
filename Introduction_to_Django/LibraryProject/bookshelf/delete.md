# Delete Operation

## Command to delete the book:
```python
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()

# Expected output will be: <QuerySet []>