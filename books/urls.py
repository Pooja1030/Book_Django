from django.urls import path
from .views import AuthorListCreate, BookListCreate, UserRegistrationView,LogoutView, SendMessageView, GetMessagesView, GenerateContentView,search_events, get_event_details,upload_book


urlpatterns = [
    
    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('messages/send/', SendMessageView.as_view(), name='send-message'),
    path('messages/', GetMessagesView.as_view(), name='get-messages'),
    path('generate-content/', GenerateContentView.as_view(), name='generate-content'),
    path('events/search/', search_events, name='search_events'),
    path('events/<int:event_id>/', get_event_details, name='get_event_details'),
    path('upload/', upload_book, name='upload-book'),
]
