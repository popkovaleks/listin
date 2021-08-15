from django.urls import path, include

from . import views

app_name = 'listin'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>', views.book_detail, name='book_detail'),
    path('new_book/', views.new_book, name='new_book'),
    path('new_author/', views.new_author, name='new_author'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register_done/', views.register, name='register'),
]