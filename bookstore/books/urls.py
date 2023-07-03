from django.urls import path 
from .views import BookList, BookDetail, EditBook, DeleteBook, AddReview, DelReview


urlpatterns=[
    path('', BookList.as_view(), name="book-list" ),
    path('<uuid:pk>/detail/', BookDetail.as_view(), name="book-detail" ),
    path('<uuid:pk>/edit/', EditBook.as_view(), name="edit-book"),
    path('<uuid:pk>/delete/', DeleteBook.as_view(), name="delete-book"),

    path('add-review/', AddReview, name="add_review"),
    path('delete-review/<pk>/', DelReview, name="del_review"),
]