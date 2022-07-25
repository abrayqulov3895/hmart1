from django.contrib import admin

from blog.models import Cart, CartItem, Contact

# Register your models here.

admin.site.register(Contact)
admin.site.register(Cart)
admin.site.register(CartItem)