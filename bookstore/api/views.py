from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from books.models import Book
from .forms import IndexSerializer

# Create your views here.
class Home(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = IndexSerializer

class BookRUD(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = IndexSerializer