from django.shortcuts import render
from django.views.generic import ListView, DetailView
from catalog.models import Author, Book, BookCopy


def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_book_instance = BookCopy.objects.all().count()
    num_instance_available = BookCopy.objects.filter(status='Available').count()

    return render(request, 'index.html', {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_instance': num_book_instance,
        'num_instance_available': num_instance_available

    })


class AuthorListView(ListView):
    model = Author
    template_name = 'authors_list.html'
    context_object_name = 'authors_list'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'book_list'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
