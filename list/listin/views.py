from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse



from .models import Book
from .forms import BookForm
# Create your views here.


def index(request):
    books = Book.objects.order_by('author')
    context = {'books': books}
    return render(request, 'listin/index.html', context)


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