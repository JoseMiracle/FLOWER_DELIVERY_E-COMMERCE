from rest_framework import serializers
from flower_delivery.models import (
    Flower, FlowerVariant, Cart, Vase
)
from flower_delivery.utils import PRICE_OPTIONS
class FlowerSerializer(serializers.ModelSerializer):
    """
        Serializer for adding new flower
    """
    class Meta:
        model = Flower
        fields = ("flower_name", "image")
    
    def validate(self, attrs):
        return super().validate(attrs)
    
class FlowerVariantSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(read_only=True)
    price = serializers.IntegerField(required=True)
    class Meta:
        model = FlowerVariant
        fields = (
            "flower",
            "variant_of_flower",
            "image",
            "price",
        )

    def validate(self, attrs):
        return super().validate(attrs)


class VaseSerializer(serializers.ModelSerializer):

    price = serializers.IntegerField(required=True)
    class Meta:
        model = Vase
        fields = ("vase_name", "image", "price")

    def create(self, validated_data):
        return super().create(validated_data)
    
class ItemToCartSerializer(serializers.ModelSerializer):
    ...
    # """
    #     Serializer for adding items to cart
    # """
    # number_of_item = serializers.IntegerField(required=True)
    # price = serializers.SerializerMethodField()
    # price_option = serializers.CharField(max_length=20, required=True)
    

    # class Meta:
    #     model = Cart 
    #     fields = (
    #         "user",
    #         "item_name",
    #         "number_of_item",
    #         "price",
    #         "price_option"
    #     )

    # def validate(self, attrs):
    #     return super().validate(attrs)
    
    # def get_price(self):
    #     if self.price_option is PRICE_OPTIONS["ONE_TIME"]:
    #         return self.price
    #     elif self.price_option is PRICE_OPTIONS["SUBSCRIBTION"]:
    #         return self.price - (self.price * 0.25) 


