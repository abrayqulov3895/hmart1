from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'shop/about.html')

def ordertracking(request):
    return render(request,'shop/order-tracking.html')

def shop_right(request):
    return render(request,'shop/shop-right-sidebar.html')