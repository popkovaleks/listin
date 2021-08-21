from django import forms
from django.contrib.auth.models import User
from ajax_select.fields import AutoCompleteSelectField


from .models import Book, Author, Genre, Post

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

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('Passwords don\'t match. Please check it')
        return cd['confirm_password']

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class PostForm(forms.ModelForm):
    # book = forms.ModelChoiceField(queryset=Book.objects.all(), widget=forms.TextInput)
    class Meta:
        model = Post
        fields = ('title', 'book', 'content', 'invisible')

    book = AutoCompleteSelectField('books', required=True)

    def clean_book(self):
        cd = self.cleaned_data
        print(cd['book'])
        print(Book.objects.get(name=cd['book']))
        if not Book.objects.get(name=cd['book']):
            raise forms.ValidationError('This book does not exists. Please add it')
        return cd['book']