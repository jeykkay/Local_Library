from django.urls import path, re_path

from catalog.views import index, AuthorListView, AuthorDetailView, BookListView, BookDetailView, BookCopyDetailView, \
    ReserveBookView

urlpatterns = [
    path('', index, name='index'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('books/', BookListView.as_view(), name='books'),

    re_path(r'^authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
    re_path(r'^books/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book-detail'),
    re_path(r'^bookcopy/(?P<pk>\d+)/$', BookCopyDetailView.as_view(), name='book-copy'),
    path('reserve_book/<int:book_id>/', ReserveBookView.as_view(), name='reserve-book')
]