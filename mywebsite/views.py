from django.shortcuts import render, HttpResponse
from mywebsite.models import *


# Create your views here.
def home(request):
    return render(request, 'home.html')

def jobs(request):
    jobs = Jobs.objects.all()
    context = {'jobs': jobs}
    return render(request, 'jobposts.html', context)

def search(request):
    return render(request, 'search.html')

def jobposts(request, slug):
    postb = Jobs.objects.filter(slug=slug).first()
    context = {'postb': postb}
    
    return render(request, 'jobpostbase.html', context)
    #return HttpResponse(f"You are viewing {slug}")

def contact(request):
    context = {'success': False}
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name, email, phone, desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        context = {'success': True}
    return render(request, 'contact.html', context)

def message(request):
    return render(request, 'message.html')


