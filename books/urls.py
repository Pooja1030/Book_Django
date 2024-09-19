from django.urls import path
from .views import AuthorListCreate, BookListCreate, UserRegistrationView,LogoutView, SendMessageView, GetMessagesView, GeminiPredictionView


urlpatterns = [
    
    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('messages/send/', SendMessageView.as_view(), name='send-message'),
    path('messages/', GetMessagesView.as_view(), name='get-messages'),
     path('gemini/predict/', GeminiPredictionView.as_view(), name='gemini-predict'), 
]
