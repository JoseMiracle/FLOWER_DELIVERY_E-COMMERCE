from rest_framework import generics, status, permissions
from rest_framework.response import Response
from flower_delivery.api.v1.serializers import (
    FlowerSerializer, 
    FlowerVariantSerializer, 
    ItemToCartSerializer, 
    VaseSerializer
)
from drf_spectacular.utils import OpenApiExample, extend_schema
from flower_delivery.permissions import IsAdminOrReadOnly
from flower_delivery.models import Flower, FlowerVariant, Vase

class FlowerAPIView(generics.ListCreateAPIView):
    serializer_class = FlowerSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Flower.objects.all()

    @extend_schema(
        examples=[
            OpenApiExample(
                "Example",
                response_only=True,
                value={
                    "info": "Success",
                    "code": 201 | 200,
                    "data": {
                        "flower_name": "MOON Delight",
                        "image": "http://localhost:8000/media/images/response_b7G1Uds.png"
                    },
                },
            )
        ]
    )

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)



class FlowerVariantAPIView(generics.ListCreateAPIView):
    serializer_class = FlowerVariantSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = FlowerVariant.objects.all()

    @extend_schema(
        examples=[
            OpenApiExample(
                "Example",
                response_only=True,
                value={
                    "info": "Success",
                    "code": 201 | 200,
                    "data": {
                        "variant_of_flower": "MOON Delight",
                        "image": "http://localhost:8000/media/images/response_b7G1Uds.png"
                    },
                },
            )
        ]
    )

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class VaseAPIView(generics.ListCreateAPIView):
    serializer_class = VaseSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Vase.objects.all()

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

class ItemToCartAPIView(generics.ListCreateAPIView):
   serializer_class = ItemToCartSerializer
   permission_classes = (permissions.IsAuthenticated,)
   

   def create(self, request, *args, **kwargs):
       return super().create(request, *args, **kwargs)
   