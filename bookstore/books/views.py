from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, View

from .models import Book, Reviews
from .forms import ReviewForm

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


# class AddReview(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "books/book_detail.html", {'form':form})
def AddReview(request, pk):
    if request.method == "POST":
        review = request.POST['review']
        return HttpResponse(review)