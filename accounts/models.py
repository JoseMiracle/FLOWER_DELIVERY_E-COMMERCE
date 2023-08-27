import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, phone_number,password=None, **extra_fields):
        """
        Create and save a user with the phone_number.
        """
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(phone_number, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=35)
    phone_number = models.CharField(unique=True, max_length=20) 
    email = models.EmailField(max_length=255, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
        
    def __str__(self):
        return self.phone_number
        
class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=25, null=False)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.phone_number} {self.otp}"
    
# NOTE: will get back to be after clarification
# class ClientFlowerReminder(models.Model):
#     """
#         This is for reminding a client about the flower
#         they 7 days before the delivery day
#     """
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     email = models.EmailField(max_length=40, blank=False, null=False)

