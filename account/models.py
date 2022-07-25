from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='category')
    description = models.TextField()

    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='post')
    price = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    discount = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.title

    def get_price(self):
        price = self.price
        discount = self.discount
        chegirma = price*(100-discount)/100
        return chegirma

    def get_image(self):
        image = ImageProduct.objects.get(product=self)
        print(image)
        return image

class ImageProduct(models.Model):
    title = models.CharField(max_length=150)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'product')
    def __str__(self) -> str:
        return self.title

class Bannerlist(models.Model):
    bg_image = models.ImageField(upload_to='bgimage')
    img_product = models.ForeignKey(ImageProduct,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title

class Ads(models.Model):
    bg_image = models.ImageField(upload_to='ads')
    title = models.CharField(max_length=150)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title

class Brend(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='brend')
    description = models.TextField()
    def __str__(self) -> str:
        return self.title
        
class CustomUser(AbstractUser):
    slug = models.SlugField(max_length=255, unique=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(upload_to='profile/', null=True, default='profile/default.png')
    phonenumber = PhoneNumberField(blank=True, null=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
    def save(self,*args, **kwargs):
        print('check save')
        if not self.slug:
            slug = slugify(f'{self.username}-{uuid4()}')
            print(slug)
            self.slug =  slug
        super(CustomUser, self).save(*args, **kwargs)
    def __str__(self) -> str:
        return f'{self.username}...'

class Feedback(models.Model):
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    text = models.TextField(blank=True)

        