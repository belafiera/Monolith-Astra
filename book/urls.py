from django.urls import path

from . import views
from .views import *

urlpatterns = [
    # path('', index),
    # path('categories/', categories),
    path('', views.start, name='index'),
    path('about/', views.about, name='about'),
    path('library/', views.library, name='libra_page'),
    path('book/', views.book, name='book_page'),
    path('review/', views.review, name='rev_page'),
    path('author/', views.author, name='author_page'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('form/', views.form, name='form'),
    path('show_post_author/<int:post_id>/', show_post_author, name='post'),
<<<<<<< HEAD
    # path('user/', views.user, name='user'),
=======
    path('user/', views.user, name='user'),
    path('api/book/', BookAPIView.as_view()),
>>>>>>> f5b2ec43c89288a6c0c162f245788152415df89e
]
