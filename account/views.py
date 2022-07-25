from unicodedata import category
from django.shortcuts import render,redirect
from account.forms import UserCreateForm

from account.models import Ads, Bannerlist, Brend, Category, Feedback, ImageProduct, Product

# Create your views here.
def home(request):
    bannerlist = Bannerlist.objects.all()[:2]
    category = Category.objects.all()
    products = Product.objects.all().order_by('-created_date')[:8]
    productprice = Product.objects.all().order_by('price')[:8]
    products1 = Product.objects.all().order_by('-created_date')[:1]
    imageproducts = ImageProduct.objects.all()[:1]
    ads = Ads.objects.all()[:2]
    brends = Brend.objects.all()[:4]
    feedback = Feedback.objects.all()[:2]

    context = {
        'bannerlist':bannerlist,
        'category':category,
        'products':products,
        'products1':products1,
        'imageproducts':imageproducts,
        'ads':ads,
        'brends':brends,
        'productprice':productprice,
        'feedback':feedback,
    }
    return render(request,'account/index.html',context)

def login(request):
    return render(request,'account/login.html')

def myaccount(request):
    return render(request,'account/my-account.html')
def CreateUser(request):
    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'): 
            user_form = UserCreateForm(data = request.POST)
            print(user_form)
            if user_form.is_valid():
                user = user_form.save() 
                user.set_password(request.POST.get('password1'))
                try:
                    user.save() 
                except:
                    print('err')
                message = 'The registration was successful. You can log in'
                request.session['message']= message
        # if form.is_valid():
            # form.save()
            return redirect('home')
        else:
            return redirect('registration')
    else:
        form = UserCreateForm()
    return render(request=request, template_name='registrations/registration.html', context={'form':form})