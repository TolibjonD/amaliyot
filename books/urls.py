from .views import BookView, BookListView, BookDetailView
from django.urls import path

app_name = "books"
urlpatterns = [
    path("books<int:id>/detail", BookDetailView.as_view(), name="detail"),
    path("create/", BookView.as_view(), name="create"),
    path("books/", BookListView.as_view(), name="books-list"),
]
