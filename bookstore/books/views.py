from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

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
def AddReview(request):
    if request.method == "POST":
        review = request.POST['review']
        book_id = request.POST["book_id"]
        book = Book.objects.filter(id = book_id).first()
        if len((review).strip()) < 1:
            messages.info(request, "can't be empty")
            return HttpResponseRedirect(reverse('book-detail', args=[str(book_id)]))
        Reviews.objects.create(
            book = book,
            review = review,
            user = request.user
        )
        messages.success(request, "review successfully added")
        
        return HttpResponseRedirect(reverse('book-detail', args=[str(book_id)]))
    

def DelReview(request, pk):
    review = Reviews.objects.filter(id = pk).first()

    if review and ( review.user == request.user ):
        review.delete()
        messages.success(request, "review deleted")

    # return HttpResponseRedirect(reverse())
    return redirect(request.META.get("HTTP_REFERER", "/")) 