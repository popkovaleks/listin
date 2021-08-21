from django.http import request
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

import pdb




from .models import Book, Post, Author
from .forms import AuthorForm, BookForm, RegistrationForm, LoginForm, PostForm
# Create your views here.


def index(request):
    posts = Post.objects.filter(invisible=False).order_by('published_date')
    context = {'posts': posts}
    return render(request, 'listin/index.html', context)

#Posts
def my_posts(request):
    posts = Post.objects.filter(author=request.user.id)
    return render(request, 'listin/my_posts.html', {'posts': posts})

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'listin/post.html', {'post': post})

    
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        print('post request')
        # try:
        #     Book.objects.get(name=form['book'].value())
        # except (Book.DoesNotExist):
        #     # form = PostForm()
        #     return render(request, 'listin/new_post.html', {'form': form, 'error_message': "This book does not exist on our site. Please, add it"})
        if form.is_valid():
            print('form is valid')
            form.instance.author = request.user
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(reverse('listin:my_posts'))
        
    else:
        print('else')
        form = PostForm()
    return render(request, 'listin/new_post.html', {'form': form})


#Books
def all_books(request):
    books = Book.objects.order_by('author')
    context = {'books': books}
    return render(request, 'listin/all_books.html', context)

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

#Authors

def all_authors(request):
    authors = Author.objects.all()
    return render(request, 'listin/all_authors.html', {'authors': authors})

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


#Users
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