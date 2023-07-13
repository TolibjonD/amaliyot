from django.contrib import admin
from .models import Book, Author, BookAuthor, Reviews


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    model = Book
    search_fields = ["title"]


class AuthorAdmin(admin.ModelAdmin):
    model = Author
    search_fields = ["first_name"]
    fields = ["first_name"]


class BookAuthorAdmin(admin.ModelAdmin):
    model = BookAuthor


class ReviewsAdmin(admin.ModelAdmin):
    model = Reviews
    search_fields = ["review"]


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(Reviews, ReviewsAdmin)
