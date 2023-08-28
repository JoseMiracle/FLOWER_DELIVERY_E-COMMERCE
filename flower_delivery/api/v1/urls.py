from django.urls import path
from flower_delivery.api.v1.views import FlowerAPIView, FlowerVariantAPIView


urlpatterns = [
    path("add-or-get-flower/", FlowerAPIView.as_view(), name="add_or_get_flower"),
    path("add-or-get-flower-variant/", FlowerVariantAPIView.as_view(), name="add_or_get_flower_variant")
]
