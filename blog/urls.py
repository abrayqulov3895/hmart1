from django.urls import path
from blog.views import blog, contact

urlpatterns = [
    path('',blog,name='blog'),
    path('contact/',contact,name='contact')
]
