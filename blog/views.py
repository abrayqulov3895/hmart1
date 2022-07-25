from django.http import JsonResponse
from django.shortcuts import render

from blog.forms import ContactForm

# Create your views here.
def blog(request):
    return render(request,'blog/blog-list.html')

def contact(request):
    if request.method =="GET":
        print('__post__')
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        print(request.headers)
        print(is_ajax)
        if is_ajax:
            form = ContactForm(request.GET)
            if form.is_valid():
                form.save()
                message = 'Your message is save to data base!'
                
                return JsonResponse({'result':True, 'message':message})
            print(form)
            print(request.GET)
            message = 'we must enter all dates'
           
            return JsonResponse({'result':False, 'message':message})
    return render(request,'blog/contact.html')