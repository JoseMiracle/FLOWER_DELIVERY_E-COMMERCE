from django.urls import path

from accounts.api.v1.views import SignInAPIView, SignUpAPIView, VerifyOtpAPIView

urlpatterns = [
    path("sign-up/", SignUpAPIView.as_view(), name="sign-up"),
    path("sign-in/", SignInAPIView.as_view(), name="sign-in"),
    path("verify-otp/", VerifyOtpAPIView.as_view(), name="verify-otp"),
]
