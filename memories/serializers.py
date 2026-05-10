from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from .models import MemoryPost
import re 

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

    # Custom username validation
    def validate_username(self, value):

           value = value.strip()

           if len(value) < 3:
                  raise serializers.ValidationError(
                          "Username must be at least 3 characters."
                  )

           if " " in value:
                        raise serializers.ValidationError(
                             "Username cannot contain spaces."
                        )

           return value
    
    # =========================================
    # PASSWORD VALIDATION
    # =========================================

    def validate_password(self, value):

        # Minimum length

        if len(value) < 8:

            raise serializers.ValidationError(
                'Password must be at least 8 characters long.'
            )

        # Maximum length

        if len(value) > 12:

            raise serializers.ValidationError(
                'Password must not exceed 12 characters.'
            )

        # Must contain uppercase letter

        if not re.search(r'[A-Z]', value):

            raise serializers.ValidationError(
                'Password must contain at least one uppercase letter.'
            )

        # Must contain lowercase letter

        if not re.search(r'[a-z]', value):

            raise serializers.ValidationError(
                'Password must contain at least one lowercase letter.'
            )

        # Must contain number

        if not re.search(r'[0-9]', value):

            raise serializers.ValidationError(
                'Password must contain at least one number.'
            )

        # Must contain special character

        if not re.search(r'[@$!%*#?&]', value):

            raise serializers.ValidationError(
                'Password must contain at least one special character.'
            )

        return value

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )

        return user


class MemoryPostSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(
        source='user.username'
    )

    likes_count = serializers.SerializerMethodField()

    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = MemoryPost

        fields = [
            'id',
            'user',
            'image',
            'description',
            'likes_count',
            'is_liked',
            'created_at'
        ]

        read_only_fields = [
            'id',
            'user',
            'created_at'
        ]

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):

        request = self.context.get('request')

        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()

        return False