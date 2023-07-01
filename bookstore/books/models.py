from django.db import models
from uuid import uuid4
from django.urls import reverse

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