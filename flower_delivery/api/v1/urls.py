from django.urls import path
from flower_delivery.api.v1.views import (
    FlowerAPIView, 
    FlowerVariantAPIView, 
    VaseAPIView, 
    CartAPIView,
    BookACallAPIView,
    EmailsToRemindAboutDeliveryAPIView
)
urlpatterns = [
    path("flowers/", FlowerAPIView.as_view(), name="flowers"),
    path("flower-variants/", FlowerVariantAPIView.as_view(), name="flower-variants"),
    path("vases/", VaseAPIView.as_view(), name="vases"),
    path("cart/", CartAPIView.as_view(), name="cart"),
    path("book-a-call/", BookACallAPIView.as_view(), name="book-a-call"),
    path('remind-to-deliver-flower/', EmailsToRemindAboutDeliveryAPIView.as_view(), name="remind-to-deliver-flower")
]
