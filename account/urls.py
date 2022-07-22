from django.urls import path
from .views import  home, login, myaccount

urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('myaccount/',myaccount,name='myaccount'),
    
]
