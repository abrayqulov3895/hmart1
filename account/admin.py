from django.contrib import admin

from account.models import Ads, Bannerlist, Brend, Category, Feedback, ImageProduct, Product
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreateForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form: UserCreateForm
    form = CustomUserChangeForm
    model: CustomUser
    list_display = ['email','username',]

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ImageProduct)
admin.site.register(Bannerlist)
admin.site.register(Ads)
admin.site.register(Brend)
admin.site.register(Feedback)