from django.urls import path
from .views import AuthorListCreate, BookListCreate, UserRegistrationView,LogoutView, SendMessageView, GetMessagesView, GenerateContentView,geocode_address


urlpatterns = [
    
    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('messages/send/', SendMessageView.as_view(), name='send-message'),
    path('messages/', GetMessagesView.as_view(), name='get-messages'),
    path('generate-content/', GenerateContentView.as_view(), name='generate-content'),
   path('geocode_address/', geocode_address, name='geocode_address'),

]
