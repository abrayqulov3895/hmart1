from django.contrib import admin

from account.models import Ads, Bannerlist, Brend, Category, ImageProduct, Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ImageProduct)
admin.site.register(Bannerlist)
admin.site.register(Ads)
admin.site.register(Brend)
