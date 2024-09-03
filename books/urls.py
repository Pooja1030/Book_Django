from django.urls import path
from .views import AuthorListCreate, BookListCreate, UserRegistrationView,LogoutView

urlpatterns = [
    
    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
