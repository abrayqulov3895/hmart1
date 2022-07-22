from django.urls import path
from .views import about, ordertracking, shop_right

urlpatterns = [
    path('about/',about,name='about'),
    path('ordertracking/',ordertracking,name='ordertracking'),
    path('',shop_right,name='shopright'),
]
