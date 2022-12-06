from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

<<<<<<< HEAD
=======
from rest_framework import generics
from book.serializers import BookSerializer

>>>>>>> f5b2ec43c89288a6c0c162f245788152415df89e
from .forms import *
from .models import Library, Book, Author, Review, User
from .models import *

# Create your views here.


# menu = ["About task", "Our Books", "Our Authors", "Reviews", "Libraries"]
menu = [{'title': "The task", 'url_name': 'about'},
        {'title': "Our books", 'url_name': 'book_page'},
        {'title': "Our authors", 'url_name': 'author_page'},
        {'title': "Reviews", 'url_name': 'rev_page'},
        {'title': "Libraries", 'url_name': 'libra_page'}
        ]

<<<<<<< HEAD
=======
class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
>>>>>>> f5b2ec43c89288a6c0c162f245788152415df89e

def index(request):
    posts = Book.objects.all()
    return render(request, 'book/index.html', {'posts': posts, 'title': 'Main page', 'menu': menu})


def about(request):
    return render(request, 'book/about.html', {'menu': menu, 'title': 'Main task with options of this project:'})


def start(request):
    posts = Book.objects.all()
    return render(request, 'book/index.html', {'posts': posts, 'title': 'Main page', 'menu': menu})
    # return render(request, 'book/index.html', {'title': 'Welcome to our book site - MonolithAstra!'})


def form(request):
    if request.method == 'POST':
        form = AddReview(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Got issue while trying add a review, sorry')
    else:
        form = AddReview()
    return render(request, 'book/form.html', {'form': form, 'title': 'Add your review on existing book', 'menu': menu})


def book(request):
    posts = Book.objects.all()
    return render(request, 'book/index.html', {'posts': posts, 'title': 'The date base of available books.', 'menu': menu})
#
#     show_books = Book.objects.all()
#     books = Book.objects.order_by('name')
#     return render(request, 'book/book.html', {'title': 'The date base of available books.', 'books': show_books})


def show_post(request, post_id):
    post = get_object_or_404(Book, pk=post_id)
    context = {
        'post': post,
        'menu': menu,
        'title': post.name,
    }

    return render(request, 'book/post.html', context=context)


def library(request):
    posts_library = Library.objects.all()

    context = {
        'posts_library': posts_library,
        'menu': menu,
        'title': "The date base of shops that have our books.",
    }

    return render(request, 'book/library.html', context=context)


def review(request):
    boo = Book.objects.all()
    rev = Review.objects.all()
    return render(request, 'book/reviews.html', {'posts': rev, 'menu': menu, 'title': 'All the reviews:', 'book': boo})


def author(request):
    posts_author = Author.objects.all()
    context = {
        'posts_author': posts_author,
        'menu': menu,
        'title': 'The date base of our authors!'
    }
    return render(request, 'book/authors.html', context=context)


def user(request):
    us = User.objects.order_by('date_of_birth')
    return render(request, 'book/users.html', {'title': 'The amount and info of our users!'})


def show_post_author(request, post_id):
    post = get_object_or_404(Author, pk=post_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.name,
    }

    return render(request, 'book/postauth.html', context=context)

