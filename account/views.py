from unicodedata import category
from django.shortcuts import render

from account.models import Ads, Bannerlist, Brend, Category, ImageProduct, Product

# Create your views here.
def home(request):
    bannerlist = Bannerlist.objects.all()[:2]
    category = Category.objects.all()
    products = Product.objects.all().order_by('-created_date')[:8]
    productprice = Product.objects.all().order_by('-price')[:8]
    products1 = Product.objects.all().order_by('-created_date')[:1]
    imageproducts = ImageProduct.objects.all()[:1]
    ads = Ads.objects.all()[:2]
    brends = Brend.objects.all()[:4]

    context = {
        'bannerlist':bannerlist,
        'category':category,
        'products':products,
        'products1':products1,
        'imageproducts':imageproducts,
        'ads':ads,
        'brends':brends,
        'productprice':productprice,
        
    }
    return render(request,'account/index.html',context)

def login(request):
    return render(request,'account/login.html')

def myaccount(request):
    return render(request,'account/my-account.html')