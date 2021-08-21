from ajax_select import register, LookupChannel
from .models import Book

@register('books')
class BooksLookup(LookupChannel):

    model = Book
    min_length = 2

    def get_query(self, q, request):
        return self.model.objects.filter(name__icontains=q).order_by('name')[:50]

    def format_item_display(self, item):
        return "<span class='book'>{} - {}</span>".format(item.name, item.author)

    def format_match(self, item):
        return "<span class='book'>{} - {}</span>".format(item.name, item.author)
        
    def check_auth(self, request):
        if request.user.is_authenticated:
            return True 