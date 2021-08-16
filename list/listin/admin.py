from django.contrib import admin

from .models import Book, Author, Genre, Post


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Post)
# Register your models here.
