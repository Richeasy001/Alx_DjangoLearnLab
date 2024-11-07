# Update Operation

## Command:
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Expected output after the update will be: Nineteen Eighty-Four by George Orwell (1949)