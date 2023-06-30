from django.urls import path 
from .views import BookList, BookDetail, EditBook, DeleteBook


urlpatterns=[
    path('', BookList.as_view(), name="book-list" ),
    path('<int:pk>/detail/', BookDetail.as_view(), name="book-detail" ),
    path('<int:pk>/edit/', EditBook.as_view(), name="edit-book"),
    path('<int:pk>/delete/', DeleteBook.as_view(), name="delete-book"),
]