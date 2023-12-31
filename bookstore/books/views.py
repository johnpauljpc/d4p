from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q

from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, View

from .models import Book, Reviews
from .forms import ReviewForm

# Create your views here.
#booklist book detailview CRUD
class BookList(ListView):
    model = Book
    # template_name = 'books/book-list.html'

# class BookDetail(PermissionRequiredMixin, DetailView):
#     model = Book
#     permission_required = ['books.special_status']
class BookDetail(LoginRequiredMixin,View):
    def get(self, request, pk):
        book = Book.objects.get(id = pk)
        context={
            'book':book
        }
        if request.user.has_perm('books.special_status'):
            return render(request, "books/book_detail.html", context)
        else:
            messages.info(request, f"dear {request.user}, to be authorized to read all the books pay once!")
            # return HttpResponseRedirect(reverse('book-order'))
            return redirect(request.META.get("HTTP_REFERER", "/"))
            return 

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

# @login_required(login_url="account_login")
class AddReview(LoginRequiredMixin,View):
    def get(self, request):
        
        return HttpResponseRedirect(reverse('book-list'))

    
    def post(self, request):
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
        messages.success(request, "review deleted successfully")
    else:
        messages.info(request, f"<b><i>Just dey play!</i></b> ONLY the author of the comment can delete it..")

    # return HttpResponseRedirect(reverse())
    return redirect(request.META.get("HTTP_REFERER", "/")) 


# class SearchView(View):
#     def get(self, request):
#         book = Book.objects.all()
#         q = request.GET['query']
#         print("************************")
#         print(q)
#         result = book.filter(Q(title__icontains = q) | Q(author__icontains = q))

#         context = {
#             'query':q,
#             'books':result
#         }
#         return render(request, "books/search-result.html", context)
    

class SearchView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/search-result.html'
    def get_queryset(self):
        q = self.request.GET['query']
        return Book.objects.filter(
    Q(title__icontains=q) | Q(title__icontains=q)
    )