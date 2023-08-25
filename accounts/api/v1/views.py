from rest_framework import generics, permissions, status
from rest_framework.response import Response
from drf_spectacular.utils import OpenApiExample, extend_schema



from accounts.api.v1.serializers import (
    SignInSerializer,
    SignUpSerializer,
)


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
            return Response(serializer.data)
