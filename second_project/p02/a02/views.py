from django.shortcuts import render,HttpResponse
from datetime import datetime
from a02.models import Todo
from django.contrib import messages
# Create your views here.
def home(request):

    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        print(name, desc)
        ins = Todo(name=name,desc = desc, date = datetime.today())
        ins.save()
        messages.success(request, "Your message has been sent.")
    return render(request,'home.html')
def tasks(request):
    allTasks = Todo.objects.all()
    context = {'tasks':allTasks}
    return render(request,'task.html',context)