from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import User  # Assuming you're using a custom user model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

# Use get_user_model to allow for future flexibility
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, attrs):
        # Check if the passwords match
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        # Create the new user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']  # Use create_user to handle password hashing
        )
        
        # Generate a token for the user
        Token.objects.create(user=user)
        
        return user