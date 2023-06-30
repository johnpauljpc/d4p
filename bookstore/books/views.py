from django.shortcuts import render

from .models import Book
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

# Create your views here.
#booklist book detailview CRUD
class BookList(ListView):
    model = Book
    # template_name = 'books/book-list.html'

class BookDetail(DetailView):
    model = Book

class EditBook(UpdateView):
    model = Book
    fields = ('title', 'author', 'price')
    template_name = 'books/book_edit.html'

class DeleteBook(DeleteView):
    model = Book