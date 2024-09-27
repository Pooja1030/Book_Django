from django.contrib import admin
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Author, Book

@login_required
def test_view(request):
    return JsonResponse({'status': 'User authenticated'}, status=200)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'rating', 'stock']
    list_filter = ['author']
    search_fields = ['title']
