from django.db import models

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
        
