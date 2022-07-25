from django.db import models

from account.models import CustomUser, Product

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f'{self.name} {self.message[:40]}...'


class Cart(models.Model):
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=1)
    order = models.BooleanField()

class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    total = models.FloatField()
    ordered_time = models.DateTimeField(auto_now_add=True)
    finished_time = models.DateTimeField(auto_now=True)
    cencal = models.BooleanField()
    cancal_time = models.DateTimeField(auto_now_add=True)
    
  