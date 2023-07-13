from django.shortcuts import render, redirect
from .forms import BookForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book

# Create your views here.


class BookView(LoginRequiredMixin, View):
    def get(self, request):
        form = BookForm()
        return render(request, "books/create.html", {"book": form})

    def post(self, request):
        form = BookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("books:books-list")
        else:
            return render(request, "books/create.html", {"book": form})


class BookListView(LoginRequiredMixin, View):
    def get(self, request):
        books = Book.objects.all().order_by("-id")
        q = request.GET.get("q", "")
        if q:
            books = Book.objects.all().filter(title__icontains=q)
        return render(request, "books/books-list.html", {"books": books, "q": q})


class BookDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        return render(request, "books/detail.html", {"book": book})
