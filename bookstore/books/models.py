from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4
from django.urls import reverse

User = get_user_model()

# Create your models here
class Book(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk':self.pk})

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    review = models.CharField( max_length=200)

    def __str__(self):
        return f"review on {self.book}"