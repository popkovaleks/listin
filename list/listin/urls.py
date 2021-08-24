from django.urls import path, include

from . import views

app_name = 'listin'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>', views.book_detail, name='book_detail'),
    path('new_book/', views.new_book, name='new_book'),
    path('new_author/', views.new_author, name='new_author'),
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('register_done/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout_user'),
    path('my_posts/', views.my_posts, name='my_posts'),
    path('new_post/', views.new_post, name='new_post'),
    path('<int:post_id>/', views.post, name='post'),
    path('all_books/', views.all_books, name='all_books'),
    path('all_authors/', views.all_authors, name='all_authors'),
    path('search_book/', views.search_book, name='search_book'),
]