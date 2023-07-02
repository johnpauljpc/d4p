from django.urls import path 
from .views import BookList, BookDetail, EditBook, DeleteBook, AddReview


urlpatterns=[
    path('', BookList.as_view(), name="book-list" ),
    path('<uuid:pk>/detail/', BookDetail.as_view(), name="book-detail" ),
    path('<uuid:pk>/edit/', EditBook.as_view(), name="edit-book"),
    path('<uuid:pk>/delete/', DeleteBook.as_view(), name="delete-book"),

    path('<uuid:pk>/add-review/', AddReview.as_view(), name="add_review"),
]