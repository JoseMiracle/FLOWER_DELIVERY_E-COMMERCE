"""
URL configuration for core project.
The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/4.2/topics/http/urls/

"""
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from accounts.api.v1.views import AppleLoginView, GoogleLoginView

urlpatterns = [
    path("to-be-hidden/", admin.site.urls),
    path("api/accounts/", include("accounts.api.v1.urls"), name="accounts"),
    path(
        "api/flower_delivery/",
        include("flower_delivery.api.v1.urls"),
        name="flower_delivery",
    ),
]


# SWAGGER UI STUFF
urlpatterns += [
    # YOUR PATTERNS
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

# OAUTH LOGINS
urlpatterns += [
    path("rest-auth/google/", GoogleLoginView.as_view(), name="google_login"),
    path("rest-auth/apple", AppleLoginView.as_view(), name="apple_view"),
]
