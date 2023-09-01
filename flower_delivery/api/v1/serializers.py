from rest_framework import serializers

from flower_delivery.models import (
    Cart, 
    Flower, 
    FlowerVariant, 
    Vase,
    CallMe,
    EmailsToRemindAboutDelivery,
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
    image = serializers.ImageField(required=True)
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
    """
        Serializer for adding items to cart
    """
    number_of_item = serializers.IntegerField(required=True)
    price = serializers.IntegerField()
    price_option = serializers.CharField(max_length=20, required=True)

    class Meta:
        model = Cart
        fields = ("item_name", "number_of_item", "price", "price_option")

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data["price"] = self.get_price(
            validated_data["price_option"], validated_data["price"]
        )

        item, created = Cart.objects.get_or_create(
            item_name=validated_data["item_name"],
            user=self.context["request"].user,
            defaults={
                "number_of_item": validated_data[
                    "number_of_item"
                ],  # Set the exact value from validated_data
                "price": validated_data["price"],
            },
        )

        if not created:
            new_number_of_item = item.number_of_item + validated_data["number_of_item"]
            Cart.objects.filter(
                item_name=validated_data["item_name"], user=self.context["request"].user
            ).update(number_of_item=new_number_of_item)

        return validated_data

    def get_price(self, price_option, price):
        """
        This is for getting the price based on a user's price option
        """
        if price_option == PRICE_OPTIONS["ONE_TIME"]:
            return price
        
        elif price_option == PRICE_OPTIONS["SUBSCRIPTION"]:
            return price - (price * 0.25)
        

class BookACallSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CallMe
        fields = ('phone_number',)

    def create(self, validated_data):
        return super().create(validated_data)

class EmailsToRemindAboutDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailsToRemindAboutDelivery
        fields = ('email',)
    
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        return super().create(validated_data)