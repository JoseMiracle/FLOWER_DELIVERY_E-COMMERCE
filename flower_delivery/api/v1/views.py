from rest_framework import generics, status, permissions
from rest_framework.response import Response
from flower_delivery.api.v1.serializers import (
    FlowerSerializer, 
    FlowerVariantSerializer,  
    VaseSerializer,
    ItemToCartSerializer,
    BookACallSerializer,
    EmailsToRemindAboutDeliverySerializer,
)
from drf_spectacular.utils import OpenApiExample, extend_schema
from flower_delivery.permissions import IsAdminOrReadOnly
from flower_delivery.models import Flower, FlowerVariant, Vase, Cart

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
    
    def post(self, request, *args, **kwargs): # NOTE: only an admin can use the post method to add flower
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
    
    def post(self, request, *args, **kwargs): # NOTE: only an admin can use the post method to add flower
        return super().post(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

class VaseAPIView(generics.ListCreateAPIView):
    serializer_class = VaseSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Vase.objects.all()

    @extend_schema(
        examples=[
            OpenApiExample(
                "Example",
                response_only=True,
                value={
                    "info": "Success",
                    "code":200,
                    "data": {
                        "variant_of_flower": "MOON Delight",
                        "image": "http://localhost:8000/media/images/response_b7G1Uds.png"
                    },
                },
            )
        ]
    )
    def post(self, request, *args, **kwargs): # NOTE: only an admin can add new vases
        return super().post(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

class CartAPIView(generics.ListCreateAPIView):
   serializer_class = ItemToCartSerializer
   permission_classes = (permissions.IsAuthenticated,)
   queryset = Cart.objects.all()
   
   
   @extend_schema(
        examples=[
            OpenApiExample(
                "Example",
                response_only=True,
                value={
                    "info": "Success",
                    "code":200,
                    "data": {
                        "item_name": "New DAY",
                        "number_of_item": 5,
                        "price": 100,
                        "price_option": "ONE_TIME"
                    },
                },
            )
        ]
    )
   def create(self, request, *args, **kwargs):
       return super().create(request, *args, **kwargs)
   
   def get(self, request, *args, **kwargs):
       return super().get(request, *args, **kwargs)
   

class BookACallAPIView(generics.CreateAPIView):
    serializer_class = BookACallSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
# class RemoveItemFromCart(generics.RetrieveUpdateDestroyAPIView):


class EmailsToRemindAboutDeliveryAPIView(generics.CreateAPIView):
    serializer_class = EmailsToRemindAboutDeliverySerializer
    permission_classes = (permissions.AllowAny,)

    @extend_schema(
        examples=[
            OpenApiExample(
                "Example",
                response_only=True,
                value={
                    "info": "Success",
                    "code":201,
                    "data": {
                    "email": "mimi@mail.com"
                    },
                },
            )
        ]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
