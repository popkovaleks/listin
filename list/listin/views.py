from django.http import request
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

import pdb




from .models import Book, Post
from .forms import AuthorForm, BookForm, RegistrationForm, LoginForm
# Create your views here.


def index(request):
    books = Book.objects.order_by('author')
    context = {'books': books}
    return render(request, 'listin/index.html', context)

def my_posts(request):
    posts = Post.objects.filter(author=request.user.id)
    return render(request, 'listin/my_posts.html', {'posts': posts})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'listin/book_detail.html', {'book': book})


def new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return HttpResponseRedirect(reverse('listin:index'))
    else:
        form = BookForm()
    return render(request, 'listin/new_book.html', {'form': form})

def new_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid:
            author = form.save(commit=False)
            author.save()
            return HttpResponseRedirect(reverse('listin:index'))
    else:
        form = AuthorForm()
    return render(request, 'listin/new_author.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('listin:index'))
                else:
                    return HttpResponse('Account is disabled')
            else:
                return HttpResponse('No such account')
    else:
        form = LoginForm()
    return render(request, 'listin/login.html', {'form': form})
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('listin:index'))

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'listin/register_done.html', {'new_user': new_user})
    else:
        form = RegistrationForm()
    return render(request, 'listin/register.html', {'form': form})