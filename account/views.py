from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'account/index.html')

def login(request):
    return render(request,'account/login.html')

def myaccount(request):
    return render(request,'account/my-account.html')