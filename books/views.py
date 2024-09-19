from firebase_admin import firestore
from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer, UserRegistrationSerializer, UserSerializer, MessageSerializer, GeminiPredictionSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, serializers
from .services.gemini_service import predict_gemini_model
import logging



db = firestore.client()

logger = logging.getLogger(__name__)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            logger.info(f'User {user.username} registered successfully.')

            # Generate JWT token for the new user
            tokens = get_tokens_for_user(user)
            return Response({
                'username': user.username,
                'message': 'User registered successfully!',
                'refresh': tokens['refresh'],
                'access': tokens['access'],
            }, status=status.HTTP_201_CREATED)
        logger.error(f'User registration failed: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    

# Message sending using Firebase
class SendMessageView(generics.GenericAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            sender = request.user
            receiver_id = serializer.validated_data['receiver_id']
            content = serializer.validated_data['content']

              # Log IDs for debugging
            logger.info(f'Sender ID: {sender.id}')
            logger.info(f'Receiver ID: {receiver_id}')
        
            try:
                receiver = User.objects.get(id=receiver_id)
            except User.DoesNotExist:
                return Response({'error': 'Receiver not found'}, status=status.HTTP_404_NOT_FOUND)
            
            try:
                # Save message to Firestore
                db.collection('messages').add({
                    'sender_id': sender.id,
                    'receiver_id': receiver.id,
                    'content': content,
                    'timestamp': firestore.SERVER_TIMESTAMP
                })
            except Exception as e:
                # Log the Firestore error
                logger.error(f'Firestore error: {e}')
                return Response({'error': 'Failed to send message'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({'message': 'Message sent successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GetMessagesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user

        # Fetch messages from Firestore where user is the receiver
        messages_ref = db.collection('messages').where('receiver_id', '==', user.id).stream()
        
        message_list = []
        for message in messages_ref:
            message_data = message.to_dict()
            message_list.append({
                'sender_id': message_data['sender_id'],
                'content': message_data['content'],
                'timestamp': message_data['timestamp']
            })

        return Response(message_list, status=status.HTTP_200_OK)




class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh_token')
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({"message": "Successfully logged out"}, status=205)
            except Exception as e:
                return Response({"error": str(e)}, status=400)
        return Response({"error": "Refresh token required"}, status=400)

class GeminiPredictionView(generics.GenericAPIView):
    serializer_class = GeminiPredictionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            input_data = serializer.validated_data['input_data']
            try:
                prediction = predict_gemini_model(input_data)
                return Response({'prediction': prediction}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)