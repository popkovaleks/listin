from django.shortcuts import get_object_or_404, render



from .models import Book
# Create your views here.


def index(request):
    books = Book.objects.order_by('author')
    context = {'books': books}
    return render(request, 'listin/index.html', context)


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'listin/book_detail.html', {'book': book})