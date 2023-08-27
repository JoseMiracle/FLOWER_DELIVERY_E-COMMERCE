from django.db import models


class Flower(models.Model):
    flower_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.flower_name


class FlowerVariant(models.Model):
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    variant_of_flower = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images') 
    price = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.flower} {self.variant_of_flower}"

class Vase(models.Model):
    vase = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images') 
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.vase}"
    
    