from django.contrib import admin
from .models import Book, Reviews

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price']
admin.site.register(Book, BookAdmin)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'review']
admin.site.register(Reviews, ReviewAdmin)