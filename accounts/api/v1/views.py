from allauth.socialaccount.providers.apple.views import AppleOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from django.contrib.auth import get_user_model
from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.api.v1.serializers import (
    SignInSerializer,
    SignUpSerializer,
    VerifyOtpSerializer,
)

User = get_user_model()


class SignUpAPIView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ("post",)

    @extend_schema(
        examples=[
            OpenApiExample(
                "Example",
                response_only=True,
                value={
                    "info": "Success",
                    "code": 201,
                    "data": {
                        "first_name": "string",
                        "last_name": "string",
                        "email": "user@example.com",
                    },
                },
            )
        ]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class SignInAPIView(generics.GenericAPIView):
    serializer_class = SignInSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ("post",)

    @extend_schema(
        examples=[
            OpenApiExample(
                "Example",
                response_only=True,
                value={
                    "status": "Success",
                    "code": 200,
                    "data": {"refresh_token": "string", "access_token": "string"},
                },
            )
        ]
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = User.objects.get(
                phone_number=serializer.validated_data["phone_number"]
            )
            refresh = RefreshToken.for_user(user)
            return Response(
                {"Info": "Welcome user", "access_token": str(refresh.access_token)},
                status=status.HTTP_200_OK,
            )


class VerifyOtpAPIView(generics.GenericAPIView):
    serializer_class = VerifyOtpSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ("post",)

    @extend_schema(
        examples=[
            OpenApiExample(
                "Example",
                response_only=True,
                value={
                    "status": "Ok",
                    "code": 200,
                    "data": {"Info": "Account activated"},
                },
            )
        ]
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(
                {"Info": "Account activated"},
                status=status.HTTP_200_OK,
            )

# class ResetOtpAPIView(generics.GenericAPIView):
#     serializer_class = VerifyOtpSerializer
#     permission_classes = (permissions.AllowAny,)
#     http_method_names = ("post",)

#     @extend_schema(
#         examples=[
#             OpenApiExample(
#                 "Example",
#                 response_only=True,
#                 value={
#                     "status": "Ok",
#                     "code": 200,
#                     "data": {"Info": "Account activated"},
#                 },
#             )
#         ]
#     )
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             return Response(
#                 {"Info": "Account activated"},
#                 status=status.HTTP_200_OK,
#             )


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class AppleLoginView(SocialLoginView):
    adapter_class = AppleOAuth2Adapter
