from django.shortcuts import render

from django.views.generic import ListView, DetailView, UpdateView, DeleteView

# Create your views here.
#booklist book detailview CRUD
class BookList(ListView):
    pass

class BookDetail(DetailView):
    pass

class EditBook(UpdateView):
    pass

class DeleteBook(DeleteView):
    pass