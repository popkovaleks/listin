from django import forms
from django.contrib.auth.models import User


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

class RegistrationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['confirm_password']