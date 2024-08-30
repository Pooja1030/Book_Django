# books/admin.py
from django.contrib import admin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']  # Using a list
    search_fields = ['name']  # Using a list

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'rating', 'stock']  # Use a list
    list_filter = ['author']  # Using a list
    search_fields = ['title']  # Using a list
