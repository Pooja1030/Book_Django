from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Author, Book


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')  



class MessageSerializer(serializers.Serializer):
    receiver_id = serializers.IntegerField()
    content = serializers.CharField()

    

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source='author')

    class Meta:
        model = Book
        fields = ['id', 'title', 'author_id', 'price', 'rating', 'stock']


#Gemini Prediction
class GeminiPredictionSerializer(serializers.Serializer):
    input_data = serializers.ListField(
        child=serializers.FloatField()
    )
    prediction = serializers.FloatField(read_only=True)