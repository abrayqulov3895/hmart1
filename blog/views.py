from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request,'blog/blog-list.html')

def contact(request):
    return render(request,'blog/contact.html')