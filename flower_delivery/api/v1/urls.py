from django.urls import path
from flower_delivery.api.v1.views import FlowerAPIView, FlowerVariantAPIView, ItemToCartAPIView, VaseAPIView
urlpatterns = [
    path("flowers/", FlowerAPIView.as_view(), name="add_or_get_flower"),
    path("flower-variants/", FlowerVariantAPIView.as_view(), name="add_or_get_flower_variant"),
    path("vases/", VaseAPIView.as_view(), name="add_or_get_vase_variant")
    # path("add-item-to-cart/", ItemToCartAPIView.as_view(), name="item_to_cart")
]
