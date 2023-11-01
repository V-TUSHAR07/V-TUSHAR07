from django.shortcuts import render,HttpResponse
from datetime import datetime
from a01.models import Contact,Blog
from django.contrib import messages,messages
# Create your views here.
def about(request):
    return render(request,'about.html')
def about2(request):
    return render(request,'about2.html')
def home(request):
    return render(request,"home.html")

def search(request):
    return render(request,'search.html')
def view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        ins = Blog(title = name,desc = desc)
        ins.save()
        messages.success(request, "Your comment has been updated.")
    return render(request,'view.html')
def view11(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        ins = Blog(title = name,desc = desc)
        ins.save()
        messages.success(request, "Your comment has been updated.")
    return render(request,'view11.html')
def view22(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        ins = Blog(title = name,desc = desc)
        ins.save()
        messages.success(request, "Your comment has been updated.")
    return render(request,'view22.html')
def view33(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        ins = Blog(title = name,desc = desc)
        ins.save()
        messages.success(request, "Your comment has been updated.")
    return render(request,'view33.html')
def view44(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        ins = Blog(title = name,desc = desc)
        ins.save()
        messages.success(request, "Your comment has been updated.")
    return render(request,'view44.html')
def blog1(request):
    
    blogs=Blog.objects.all()
    context={'blogs':blogs}
    return render(request,'blog1.html',context)

def view2(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        ins = Blog(title = name,desc = desc)
        ins.save()
        messages.success(request, "Your comment has been updated.")
    return render(request,'view2.html')
def view3(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        ins = Blog(title = name,desc = desc)
        ins.save()
        messages.success(request, "Your comment has been updated.")
    return render(request,'view3.html')
def view4(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        ins = Blog(title = name,desc = desc)
        ins.save()
        messages.success(request, "Your comment has been updated.")
    return render(request,'view4.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email = email,phone = phone,desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")

    return render(request,"contact.html")
def book(request):
    return HttpResponse("book")