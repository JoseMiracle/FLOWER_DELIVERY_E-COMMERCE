import random
from typing import Any

from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Q
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import OTP

User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):

    """
    Serializer for signing up
    """

    phone_number = serializers.CharField(write_only=True, min_length=10)

    class Meta:
        model = User
        fields = ("phone_number",)

    @transaction.atomic
    def create(self, validated_data: dict) -> dict[str, Any]:
        """
        This is for creating a user instance
        """
        # Generate a random integer with 5 digits
        generated_otp = random.randrange(100000, 1000000)
        user = User.objects.create_user(**validated_data)
        user_otp = OTP.objects.create(otp=generated_otp, user=user)
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["info"] = "Pls check your phone for an otp to continue the sign up process"
        return data


class SignInSerializer(serializers.ModelSerializer):
    """
    Serializer for signing in
    """

    phone_number = serializers.CharField(write_only=True, min_length=10)

    class Meta:
        model = User
        fields = ("phone_number",)

    def validate_phone_number(self, phone_number):
        """
        Validates if a number exist in the DB
        """
        error_messages = {
            "error-mssg-1": "Please recheck the phone number provided. or sign up"
        }

        user = User.objects.filter(phone_number=phone_number).first()

        if user.is_active:
            return phone_number

        else:
            raise serializers.ValidationError(error_messages["error-mssg-1"])


class VerifyOtpSerializer(serializers.Serializer):
    """
    This  serializer is for verifying the otp an unverified or inactive user provides
    """

    otp = serializers.CharField(min_length=6, write_only=True)
    phone_number = serializers.CharField(min_length=10, write_only=True)

    def validate(self, attrs):
        error_messages = {
            "error-mssg-1": {
                "INCORRECT CREDENTIALS": "Pls recheck the credentials provided"
            }
        }

        user = User.objects.filter(phone_number=attrs["phone_number"]).first()

        if user:
            user_otp = OTP.objects.filter(user=user, otp=attrs["otp"]).first()

            if user_otp and attrs["otp"] == user_otp.otp:
                user.is_active = True
                user.save()
                user_otp.delete()  # NOTE: Use celery to remove otp after a certain period
                return attrs
            else:
                raise serializers.ValidationError(error_messages["error-mssg-1"])

        else:
            raise serializers.ValidationError(error_messages["error-mssg-1"])


# class ResetOtpSerializer(serializers.Serializer):
#     """
#         This  serializer is for resetting password
#     """
#     phone_number = serializers.CharField(min_length=10, write_only=True)

#     def validate(self, attrs):
#         error_messages = {
#             "error-mssg-1": {
#                 "INCORRECT CREDENTIALS": "Pls recheck the credentials provided"
#             }
#         }

#         user = User.objects.filter(phone_number=attrs["phone_number"]).first()

#         if user:
#             generated_otp = random.randrange(100000,1000000)
#             user_otp = OTP.objects.create(otp=generated_otp, user=user)
#         else:
#              raise serializers.ValidationError(error_messages["error-mssg-1"])
