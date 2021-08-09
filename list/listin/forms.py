from django import forms

from .models import Book, Author, Genre

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'author', 'release_date', 'language', 'genre', 'description')