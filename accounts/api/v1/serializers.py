from typing import Any

from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    
    """
    Serializer for signing up 
    """

    phone_number = serializers.CharField(write_only=True, min_length=25)

    class Meta:
        model = User
        fields = (
            "phone_number",
        )

    @transaction.atomic
    def create(self, validated_data: dict) -> dict[str, Any]:
        """
            This is for creating a user instance
        """
        user = User.objects.create_user(**validated_data)
        return user

class SignInSerializer(serializers.ModelSerializer):
    """
    Serializer for signing in
    """

    phone_number = serializers.CharField(write_only=True, min_length=10)

    class Meta:
        model = User
        fields = (
            "phone_number",
        )

    def validate_phone_number(self, attrs):
        """
            Validates if a number exist in the DB
        """
        user = User.objects.filter(phone_number=attrs["phone_number"]).first()
        
        if user.DoesNotExist():
            return {
                "error":"Pls receheck the info provided or signup" 
            }
        
        else:
            return {
            "message": "Welcome"
        }
    
    @transaction.atomic
    def create(self, validated_data: dict) -> dict[str, Any]:
        """
        This is for creating a user instance
        """
        user = User.objects.create_user(**validated_data)
        return user