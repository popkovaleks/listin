from django import forms

from .models import Book, Author, Genre

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'author', 'release_date', 'language', 'genre', 'description')

class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')

class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = ('name',)