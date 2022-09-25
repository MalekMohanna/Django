from multiprocessing import context
from django.shortcuts import render,redirect
from .models import User

def index(request):
    context = {
        'users':User.objects.all()
    }
    return render(request,'index.html',context)

def data(request):
    User.objects.create(first_name = request.POST['first'], last_name = request.POST['last'], email= request.POST['email'], age = request.POST['age'])

    return redirect('/')

def delete(request):
    c=User.objects.get(id=request.POST['id'])
    c.delete()
    return redirect('/')