from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Flower(models.Model):
    flower_name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.flower_name


class FlowerVariant(models.Model):
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    variant_of_flower = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images') 
    price = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.flower} {self.variant_of_flower}"

class Vase(models.Model):
    vase_name = models.CharField(max_length=40, unique=True)
    image = models.ImageField(upload_to='images') 
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.vase}"

# class Cart(models.Model):
    ...
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # item_name = models.CharField(max_length=50)
    # number_of_item = models.IntegerField(default=0)
    # price = models.IntegerField(default=0)
    # price_option = models.CharField(max_length=20, null=False, blank=False)
    # created_time = models.DateTimeField(auto_now_add=True)
    # updated_time = models.DateTimeField(auto_now=True)


